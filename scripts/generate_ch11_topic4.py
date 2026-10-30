# scripts/generate_ch11_topic4.py
# MH-9-SCIT-11-11.4: Ray Diagrams for Convex Mirror & Uses
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-11-11.4"

exam_data = [
    # 1-10: Ray Rules & Image Formation in Convex Mirrors
    ("How does an incident ray traveling parallel to the principal axis reflect from a convex mirror?",
     ["It appears to diverge from the principal focus (F) located behind the mirror",
      "It converges to a real focal point in front of the mirror",
      "It passes directly through the center of curvature C",
      "It retraces its path back to the light source"],
     "A", "OSC", "easy",
     "Parallel rays reflecting from a convex mirror diverge outward such that their backward extensions pass through the virtual focus F behind the mirror."),

    ("How does an incident ray directed towards the virtual focus (F) of a convex mirror reflect?",
     ["It emerges parallel to the principal axis",
      "It passes through the pole P",
      "It reflects at 90 deg to the surface",
      "It is completely absorbed by the glass"],
     "A", "OSC", "easy",
     "By optical reversibility, a ray heading toward the virtual focus F behind the mirror reflects parallel to the principal axis."),

    ("Why does a light ray directed towards the center of curvature (C) of a convex mirror retrace its path?",
     ["Because it strikes the convex surface along the normal (radius), giving an angle of incidence i = 0 deg",
      "Because the center of curvature is a physical obstacle",
      "Because convex mirrors only reflect rays through C",
      "Because light slows down to zero at C"],
     "A", "OSC", "easy",
     "Any line heading toward C coincides with the radius of curvature and hits the surface normally (i = 0 deg, r = 0 deg), causing the ray to retrace its trajectory."),

    ("Where is the image formed by a convex mirror when a real object is placed at optical infinity?",
     ["At the virtual focus (F) behind the mirror",
      "At the center of curvature C behind the mirror",
      "At the pole P",
      "In front of the mirror at distance f"],
     "A", "OSC", "easy",
     "For an object at infinity, parallel incident rays diverge such that their backward virtual extensions intersect at focus F behind the mirror."),

    ("What are the characteristics of the image formed when an object is placed at infinity in front of a convex mirror?",
     ["Virtual, erect, and highly diminished (point-sized)",
      "Real, inverted, and magnified",
      "Real, erect, and of the same size",
      "Virtual, inverted, and enlarged"],
     "A", "OSC", "easy",
     "Parallel rays from infinity form an infinitely diminished (point-like), virtual, and erect image at F behind the mirror."),

    ("Where is the image formed when a real object is placed at any finite distance between infinity and the pole of a convex mirror?",
     ["Between the pole (P) and the principal focus (F) behind the mirror",
      "Beyond the center of curvature C behind the mirror",
      "In front of the mirror between P and F",
      "At infinity in front of the mirror"],
     "A", "OSC", "easy",
     "For any real object between infinity and the pole, the image always forms between P and F behind the mirror."),

    ("What are the nature and size of the image formed by a convex mirror for any finite object distance?",
     ["Virtual, erect, and diminished (smaller than the object)",
      "Real, inverted, and magnified",
      "Virtual, inverted, and diminished",
      "Real, erect, and magnified"],
     "A", "OSC", "easy",
     "A convex mirror always forms a virtual, upright (erect), and diminished image (0 < m < +1) of any real object."),

    ("What is the range of linear magnification (m) produced by a convex mirror for a real object?",
     ["0 < m < +1 (positive and less than 1)",
      "m > +1",
      "m < -1",
      "-1 < m < 0"],
     "A", "OSC", "easy",
     "Because the image is always erect (positive sign) and diminished (image height < object height), m lies strictly between 0 and +1."),

    ("Can a convex mirror ever form a real image of a real object?",
     ["No, it always forms a virtual image for all real object positions",
      "Yes, when the object is placed very close to the pole",
      "Yes, when the object is at infinity",
      "Yes, when placed in water"],
     "A", "OSC", "easy",
     "Reflected rays from a convex mirror always diverge into real space; their physical intersection in front of the mirror is impossible for a real object."),

    ("What happens to the position and size of the virtual image in a convex mirror as an object moves closer to the pole P?",
     ["The image moves closer to the pole P and its size increases (approaching the object size)",
      "The image moves toward the focus F and becomes point-sized",
      "The image turns real and flips upside down",
      "The image recedes to infinity"],
     "A", "OSC", "medium",
     "As the object approaches P from infinity, the virtual image moves from F toward P behind the mirror, growing larger from point-sized towards object size (m -> 1)."),

    # 11-20: Uses & Driving Mirrors
    ("Why are convex mirrors universally preferred as rear-view (wing) mirrors in automobiles?",
     ["They always provide an erect image and offer a much wider field of view because they curve outwards",
      "They produce magnified real images of distant vehicles",
      "They absorb headlight glare completely",
      "They make cars look closer than they actually are"],
     "A", "OSC", "easy",
     "A convex mirror curves outwards, allowing drivers to view a far wider panoramic field behind the vehicle with upright, diminished images of overtaking traffic."),

    ("What safety warning is typically etched onto passenger-side convex rear-view mirrors?",
     ["'Objects in mirror are closer than they appear'",
      "'Do not touch the reflective glass'",
      "'Objects in mirror are magnified'",
      "'Use only in daytime'"],
     "A", "OSC", "easy",
     "Because a convex mirror produces a diminished image, drivers might perceive vehicles as farther away than their actual physical distance, necessitating the warning."),

    ("Why is a plane mirror inferior to a convex mirror as a vehicle rear-view mirror?",
     ["A plane mirror has a much narrower field of view, creating large blind spots for the driver",
      "A plane mirror inverts vehicles upside down",
      "A plane mirror cannot reflect red taillights",
      "A plane mirror magnifies objects excessively"],
     "A", "OSC", "easy",
     "Although a plane mirror forms an erect image of 1:1 scale, its flat surface provides a restricted field of view compared to the wide divergent view of a convex mirror."),

    ("Which optical mirror is installed at blind intersections and sharp mountain hairpin bends to prevent road accidents?",
     ["A large circular convex mirror",
      "A concave shaving mirror",
      "A flat plane mirror strip",
      "A cylindrical glass prism"],
     "A", "OSC", "easy",
     "Convex mirrors placed at blind corners spread outgoing rays widely, allowing drivers approaching from one side to spot hidden oncoming vehicles around the bend."),

    ("Why are convex mirrors mounted in high ceiling corners of large department stores and supermarkets?",
     ["As anti-theft surveillance mirrors providing a wide-angle overview of aisles to store security",
      "To focus sunlight onto merchandise displays",
      "To make the ceiling appear higher",
      "To reflect decorative ambient colors"],
     "A", "OSC", "easy",
     "A single convex mirror covers a wide visual angle, enabling security personnel or cashiers to monitor multiple aisles from a central location."),

    ("Why are small convex mirrors often embedded next to ATM keypad screens?",
     ["To allow users to detect anyone standing behind them attempting to spy on their PIN code",
      "To magnify the ATM cash dispenser slot",
      "To reflect laser beams from the currency scanner",
      "To verify customer face recognition biometrics"],
     "A", "OSC", "easy",
     "A wide-angle convex mirror allows ATM users to see over-the-shoulder shoulder-surfers without turning around."),

    ("In street lighting, why are convex reflectors sometimes utilized?",
     ["To diverge and scatter light over a broad municipal roadway area",
      "To concentrate light into a single sharp spot",
      "To change the color of sodium vapor lamps",
      "To generate solar electricity"],
     "A", "OSC", "easy",
     "Convex reflectors spread light outwards over a wide geographical ground area, increasing the illuminated street coverage."),

    ("Comparing the field of view of a plane mirror, a concave mirror, and a convex mirror of equal aperture, which mirror has the largest field of view?",
     ["Convex mirror", "Plane mirror", "Concave mirror", "All three have identical field of view"],
     "A", "OSC", "easy",
     "Due to outward curvature, reflected rays diverge over a wide angular span, giving the convex mirror the largest field of view."),

    ("Which mirror has the smallest field of view among spherical and plane mirrors?",
     ["Concave mirror", "Convex mirror", "Plane mirror", "Cylindrical convex mirror"],
     "A", "OSC", "easy",
     "A concave mirror converges light rays towards the axis, creating a narrower angular field of view than flat or convex surfaces."),

    ("What type of image is formed of a driver's face when looking closely into a convex rear-view mirror?",
     ["Virtual, erect, and diminished",
      "Real, inverted, and magnified",
      "Virtual, erect, and magnified",
      "Real, inverted, and diminished"],
     "A", "OSC", "easy",
     "Regardless of distance, a convex mirror always presents a virtual, erect, and diminished image."),

    # 21-30: OMC, OTF, OAR Questions
    ("Which of the following are practical applications of convex mirrors? (Select all that apply)",
     ["Automobile rear-view side mirrors",
      "Security mirrors in supermarkets and ATMs",
      "Blind corner road safety mirrors at hairpin bends",
      "Dentist teeth examination mirrors"],
     "A", "OMC", "easy",
     "Convex mirrors serve as rear-view, security, and blind-turn mirrors due to their wide field of view. Dentist mirrors are concave to magnify cavities."),

    ("Assertion (A): Convex mirrors are used as rear-view mirrors in automobiles.\nReason (R): Convex mirrors always produce an erect, diminished image and have a much wider field of view than plane mirrors.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Both statements are true: outward curvature diverges rays to provide an erect image across an expansive visual angle."),

    ("Assertion (A): A convex mirror can be used as a solar concentrator in solar cookers.\nReason (R): Convex mirrors converge all incident light rays to a real focus in front of the mirror.",
     ["Both Assertion (A) and Reason (R) are false",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true",
      "Both Assertion (A) and Reason (R) are true"],
     "A", "OAR", "easy",
     "Both are false: convex mirrors diverge light rather than converging it, and have a virtual focus behind the mirror; concave mirrors are used for solar cookers."),

    ("State whether the following statement is True or False: A convex mirror can form an inverted image of a real object if the object is placed very far away.",
     ["False", "True"],
     "A", "OTF", "easy",
     "For all real object positions from infinity to the pole, a convex mirror strictly produces an upright (erect) virtual image."),

    ("State whether the following statement is True or False: The image formed by a convex mirror always lies between the pole P and focus F behind the mirror for a finite real object.",
     ["True", "False"],
     "A", "OTF", "easy",
     "For any finite object distance, the virtual image forms within the focal length behind the mirror (between P and F)."),

    ("State whether the following statement is True or False: The magnification m of a convex mirror is always positive and less than 1 (0 < m < 1) for a real object.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because the image is erect (m > 0) and diminished (image size < object size), m is strictly a positive fraction."),

    ("An object of height 6 cm is placed 20 cm in front of a convex mirror of focal length 20 cm. What is the height of the image?",
     ["3 cm", "6 cm", "12 cm", "1.5 cm"],
     "A", "OSC", "medium",
     "Using mirror formula: 1/v = 1/f - 1/u = 1/20 - (-1/20) = 1/20 + 1/20 = 2/20 = 1/10, so v = +10 cm. Magnification m = -v/u = -10/(-20) = +0.5. Image height h_2 = m * h_1 = 0.5 * 6 cm = 3 cm."),

    ("An object is placed at a distance of 30 cm in front of a convex mirror of focal length 15 cm. Where is the image formed?",
     ["10 cm behind the mirror", "30 cm behind the mirror", "15 cm in front of the mirror", "60 cm behind the mirror"],
     "A", "OSC", "medium",
     "Here u = -30 cm, f = +15 cm. 1/v = 1/f - 1/u = 1/15 - (-1/30) = 1/15 + 1/30 = 3/30 = 1/10, so v = +10 cm (10 cm behind the mirror)."),

    ("A car is traveling behind a bus. The driver of the bus sees the car in his convex rear-view mirror of focal length 2 m. If the car is 6 m away, what is the image distance?",
     ["1.5 m behind the mirror", "2 m behind the mirror", "3 m in front of the mirror", "0.75 m behind the mirror"],
     "A", "OSC", "medium",
     "Here u = -6 m, f = +2 m. 1/v = 1/f - 1/u = 1/2 - (-1/6) = 1/2 + 1/6 = 4/6 = 2/3, so v = +1.5 m (behind the mirror)."),

    ("What is the nature of the focal length of a convex mirror according to Cartesian sign conventions?",
     ["Always positive (+)", "Always negative (-)", "Zero", "Positive only in daylight"],
     "A", "OSC", "easy",
     "Because the focus F lies behind the mirror in the positive direction of incident light, f is always positive for convex mirrors.")
,
    # 31-40: Additional Exam Questions
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
]

practice_data = [
    # 31-40: Quantitative & Conceptual Practice
    ("If a convex mirror has a radius of curvature of 3 m, what is its focal length?",
     ["+1.5 m", "-1.5 m", "+3.0 m", "+6.0 m"],
     "A", "OSC", "easy",
     "Focal length f = +R / 2 = +3 / 2 = +1.5 m."),

    ("A bus is located at a distance of 5 m from a truck's convex rear-view mirror of radius of curvature 2 m. Where does the image of the bus appear?",
     ["+0.83 m behind the mirror", "+1.25 m behind the mirror", "-1.0 m in front", "+2.5 m behind"],
     "A", "OSC", "medium",
     "Here R = 2 m so f = +1 m, and u = -5 m. 1/v = 1/f - 1/u = 1/1 - (-1/5) = 1 + 0.2 = 1.2 = 6/5. Thus v = 5/6 \approx +0.83 m behind the mirror."),

    ("What is the linear magnification of a convex mirror when an object of height 10 cm forms an image of height 4 cm?",
     ["+0.4", "-0.4", "+2.5", "-2.5"],
     "A", "OSC", "easy",
     "Magnification m = h_2 / h_1 = +4 / 10 = +0.4 (erect and diminished)."),

    ("State whether the following statement is True or False: As an object moves further away from a convex mirror, its image shrinks and approaches the focus F.",
     ["True", "False"],
     "A", "OTF", "easy",
     "As u increases towards infinity, v approaches f and the image shrinks towards a point."),

    ("State whether the following statement is True or False: A convex mirror can be used as a makeup mirror to get a magnified view of the face.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A convex mirror always diminishes images; a concave mirror is needed for magnification."),

    ("Why does a security guard at a parking garage prefer a convex mirror over a plane mirror?",
     ["It gives a wide-angle view covering the entire driveway from one viewpoint",
      "It makes license plates appear larger",
      "It illuminates the car undercarriage",
      "It functions without any light"],
     "A", "OSC", "easy",
     "The outward curved shape offers an extensive panoramic field of view, surveying wide driveways."),

    ("An object is placed 10 cm in front of a convex mirror of focal length 10 cm. What is the image distance?",
     ["+5 cm (5 cm behind the mirror)", "+10 cm", "-5 cm", "+20 cm"],
     "A", "OSC", "medium",
     "1/v = 1/f - 1/u = 1/10 - (-1/10) = 2/10 = 1/5, so v = +5 cm behind the mirror."),

    ("What is the magnification in the previous question where u = -10 cm and v = +5 cm?",
     ["+0.5", "-0.5", "+2.0", "-2.0"],
     "A", "OSC", "easy",
     "m = -v / u = -(+5) / (-10) = +0.5."),

    ("Which of the following optical components always forms a virtual, erect, and diminished image of a real object?",
     ["Convex mirror and concave lens",
      "Concave mirror and convex lens",
      "Plane mirror and prism",
      "Cylindrical concave mirror"],
     "A", "OSC", "medium",
     "Both convex mirrors and concave lenses always form virtual, erect, and diminished images for all real object positions."),

    ("If you look at your reflection in the back (bulging) side of a polished metal spoon, what do you see?",
     ["An upright, diminished reflection of your face",
      "An upside-down, enlarged reflection",
      "An upside-down, diminished reflection",
      "No reflection at all"],
     "A", "OSC", "easy",
     "The bulging outer surface functions as a convex mirror, producing an erect and diminished image."),

    # 41-50: Advanced Conceptual Practice
    ("Assertion (A): The virtual image formed by a convex mirror can never be captured on a physical photographic paper screen placed behind the mirror.\nReason (R): No real light rays penetrate behind the opaque reflecting surface of a mirror.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "A virtual image is an apparent intersection of backward ray projections; no physical photons travel behind the silvered surface to expose screen paper."),

    ("When an object moves with uniform speed towards a convex mirror, how does the speed of its virtual image change?",
     ["The image moves towards the pole with speed less than the object speed",
      "The image moves away from the pole with speed greater than the object speed",
      "The image speed is strictly equal to the object speed",
      "The image remains completely stationary"],
     "A", "OSC", "medium",
     "Since image distance v is bounded between 0 and f while u spans 0 to infinity, the longitudinal image velocity v_img = m^2 * v_obj is smaller than object speed because m < 1."),

    ("A convex mirror has focal length 25 cm. Where should an object be placed to form an image of half its size (m = +0.5)?",
     ["25 cm in front of the mirror", "50 cm in front", "12.5 cm in front", "75 cm in front"],
     "A", "OSC", "medium",
     "Using m = f / (f - u): 0.5 = 25 / (25 - u) => 25 - u = 50 => u = -25 cm (25 cm in front of the mirror)."),

    ("State whether the following statement is True or False: For a convex mirror, as object distance u approaches infinity, image distance v approaches f.",
     ["True", "False"],
     "A", "OTF", "easy",
     "1/v = 1/f - 1/infinity = 1/f, so v approaches f."),

    ("State whether the following statement is True or False: The field of view of a convex mirror is narrower than that of a plane mirror of the same size.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The convex mirror curves outward, providing a considerably wider field of view than a flat plane mirror."),

    ("Why is a convex mirror installed at hallway intersections in hospitals and schools?",
     ["To allow staff and students to see approaching traffic from intersecting blind corridors",
      "To illuminate dark ceilings",
      "To check facial grooming",
      "To disinfect corridor air with UV light"],
     "A", "OSC", "easy",
     "Corner convex mirrors give visibility around blind intersecting hallways, preventing collisions with gurneys or pedestrians."),

    ("What is the focal length of a convex mirror that produces an image at 12 cm behind the mirror when an object is placed 20 cm in front?",
     ["+30 cm", "+15 cm", "+7.5 cm", "+60 cm"],
     "A", "OSC", "medium",
     "Here u = -20 cm, v = +12 cm. 1/f = 1/v + 1/u = 1/12 - 1/20 = (5 - 3)/60 = 2/60 = 1/30. Thus f = +30 cm."),

    ("If an object is placed at the pole P of a convex mirror, what is the magnification?",
     ["m = +1", "m = 0", "m = -1", "m = infinity"],
     "A", "OSC", "easy",
     "At the pole P, u = 0 and v = 0, so the image coincides with the object with equal size and erect orientation: m = +1."),

    ("Can a convex mirror produce an inverted image if a virtual object is used?",
     ["Yes, if a converging beam of light forms a virtual object behind the mirror beyond F, a real inverted image can be formed",
      "No, convex mirrors can never form inverted images under any conditions",
      "Only in a vacuum",
      "Only if the mirror is painted black"],
     "A", "OSC", "medium",
     "For virtual objects (converging incident rays), if the virtual object lies beyond focus F behind the mirror, the reflected rays can intersect in front of the mirror to form a real inverted image."),

    ("Why is linear magnification m positive for all real objects in a convex mirror?",
     ["Because the image is always erect (upright)",
      "Because the mirror has positive electrical charge",
      "Because the radius of curvature is negative",
      "Because light rays travel faster after reflection"],
     "A", "OSC", "easy",
     "Linear magnification is defined with image height; an erect image has positive height, making m strictly positive.")
,
    # 51-60: Additional Practice Questions
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
]

mock_data = [
    # 71: Convex Mirror Parallel Ray Divergence Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="320" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <path d="M 130,25 A 130,130 0 0,1 130,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Focus F behind mirror -->
  <circle cx="210" cy="95" r="4" fill="#facc15"/>
  <text x="207" y="85" fill="#facc15" font-size="11" font-weight="bold">F</text>
  <!-- Parallel ray 1 -->
  <line x1="20" y1="50" x2="138" y2="50" stroke="#4ade80" stroke-width="2"/>
  <line x1="138" y1="50" x2="40" y2="10" stroke="#f87171" stroke-width="2"/>
  <line x1="138" y1="50" x2="210" y2="95" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Parallel ray 2 -->
  <line x1="20" y1="140" x2="138" y2="140" stroke="#4ade80" stroke-width="2"/>
  <line x1="138" y1="140" x2="40" y2="180" stroke="#f87171" stroke-width="2"/>
  <line x1="138" y1="140" x2="210" y2="95" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="60" y="175" fill="#facc15" font-size="10">Object at Infinity: Virtual point-sized image at Focus F</text>
</svg>
</div>
In the ray diagram for a convex mirror with incoming parallel rays from infinity, where do the reflected rays appear to meet, and what is the nature of the image?""",
     ["They appear to diverge from the virtual focus F behind the mirror, forming a virtual, erect, and point-sized image""",
     "They converge to a real focus in front of the mirror""",
     "They intersect at the center of curvature C in front""",
     "They form a real magnified image on the glass surface"],
     "A", "OSC", "easy""",
     "Parallel incoming rays diverge outward upon reflection; extending the divergent rays backward shows they emanate from the virtual focus F behind the mirror."),

    # 72: Finite Object Distance Ray Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="320" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 140,25 A 130,130 0 0,1 140,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="152" cy="120" r="3" fill="#facc15"/><text x="148" y="135" fill="#facc15" font-size="10">P</text>
  <circle cx="210" cy="120" r="3" fill="#4ade80"/><text x="206" y="135" fill="#4ade80" font-size="10">F</text>
  <circle cx="270" cy="120" r="3" fill="#f87171"/><text x="266" y="135" fill="#f87171" font-size="10">C</text>
  <!-- Real Object AB -->
  <line x1="50" y1="120" x2="50" y2="50" stroke="#fbbf24" stroke-width="3"/>
  <polygon points="46,55 50,45 54,55" fill="#fbbf24"/>
  <text x="35" y="40" fill="#fbbf24" font-size="10" font-weight="bold">Object</text>
  <!-- Virtual diminished image A'B' between P and F -->
  <line x1="180" y1="120" x2="180" y2="85" stroke="#ec4899" stroke-width="2.5" stroke-dasharray="3,2"/>
  <polygon points="177,90 180,80 183,90" fill="#ec4899"/>
  <text x="175" y="75" fill="#ec4899" font-size="10" font-weight="bold">Image</text>
  <!-- Ray 1: Parallel then diverging from F -->
  <line x1="50" y1="50" x2="146" y2="50" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="146" y1="50" x2="60" y2="10" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="146" y1="50" x2="210" y2="120" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Ray 2: Directed towards C -->
  <line x1="50" y1="50" x2="150" y2="85" stroke="#f87171" stroke-width="1.5"/>
  <line x1="150" y1="85" x2="270" y2="120" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="50" y="175" fill="#cbd5e1" font-size="10">Finite object: Virtual, erect & diminished image between P & F</text>
</svg>
</div>
According to the ray diagram for a finite object in front of a convex mirror, what are the properties of the image formed between P and F?""",
     ["Virtual, erect, and diminished (smaller than object)""",
     "Real, inverted, and magnified""",
     "Virtual, erect, and magnified""",
     "Real, inverted, and diminished"],
     "A", "OSC", "easy""",
     "The reflected rays diverge in front of the mirror, and their backward dashed extensions intersect between P and F behind the mirror, creating a virtual, upright, and diminished image."),

    # 73: Wide Field of View Comparison
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Plane Mirror Field of View -->
  <line x1="60" y1="70" x2="60" y2="130" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 60,70 L 10,40 L 10,160 L 60,130 Z" fill="#38bdf8" fill-opacity="0.1"/>
  <text x="20" y="30" fill="#38bdf8" font-size="10">Plane Mirror (Narrow)</text>
  <!-- Convex Mirror Field of View -->
  <path d="M 240,70 A 50,50 0 0,1 240,130" fill="none" stroke="#ec4899" stroke-width="4"/>
  <path d="M 240,70 L 170,30 L 170,170 L 240,130 Z" fill="#ec4899" fill-opacity="0.15"/>
  <text x="180" y="25" fill="#ec4899" font-size="10" font-weight="bold">Convex Mirror (Wide Field)</text>
  <text x="50" y="180" fill="#facc15" font-size="10">Convex curvature diverges boundary rays, providing panoramic coverage</text>
</svg>
</div>
Why does a convex mirror have a much larger field of view than a flat plane mirror of the same aperture size, as illustrated in the comparison?""",
     ["Because its outward curvature reflects incoming boundary rays across a much wider angular span into the driver's eye""",
     "Because convex mirrors bend light by refraction""",
     "Because plane mirrors block peripheral light rays""",
     "Because convex mirrors absorb all side glare"],
     "A", "OSC", "easy""",
     "The outward bulging surface disperses the reflected rays outwards, enabling rays from a substantially wider angular sector to enter the observer's eye."),

    # 74: Automobile Rear-View Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Wing mirror housing -->
  <rect x="50" y="35" width="240" height="120" rx="20" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
  <!-- Convex glass -->
  <rect x="60" y="45" width="220" height="100" rx="15" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <!-- Diminished erect car in mirror -->
  <rect x="140" y="80" width="60" height="30" rx="5" fill="#f43f5e"/>
  <circle cx="150" cy="110" r="6" fill="#0f172a"/>
  <circle cx="190" cy="110" r="6" fill="#0f172a"/>
  <text x="80" y="135" fill="#facc15" font-size="8">OBJECTS IN MIRROR ARE CLOSER THAN THEY APPEAR</text>
  <text x="85" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Automobile Rear-View Mirror</text>
</svg>
</div>
Why does the rear-view mirror display the safety warning 'OBJECTS IN MIRROR ARE CLOSER THAN THEY APPEAR'?""",
     ["Because the diminished virtual image makes trailing vehicles appear farther away than their actual physical position""",
     "Because the mirror magnifies vehicles""",
     "Because the mirror inverts cars upside down""",
     "Because the glass slows down vehicular motion"],
     "A", "OSC", "easy""",
     "Human depth perception equates smaller retinal image size with greater distance. Since convex mirrors diminish vehicles, drivers might overestimate the distance to trailing cars, risking collision."),

    # 75: Blind Corner Road Safety Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Round convex mirror on pole -->
  <circle cx="170" cy="75" r="45" fill="#1e293b" stroke="#f97316" stroke-width="5"/>
  <path d="M 140,55 A 40,40 0 0,1 200,55" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <line x1="170" y1="120" x2="170" y2="175" stroke="#94a3b8" stroke-width="6"/>
  <!-- Reflected vehicles from two sides -->
  <text x="30" y="60" fill="#4ade80" font-size="10">Road A Approach</text>
  <line x1="100" y1="65" x2="135" y2="75" stroke="#4ade80" stroke-width="2"/>
  <text x="235" y="60" fill="#f87171" font-size="10">Road B Approach</text>
  <line x1="240" y1="65" x2="205" y2="75" stroke="#f87171" stroke-width="2"/>
  <text x="60" y="185" fill="#f97316" font-size="10" font-weight="bold">Hairpin Bend Blind-Turn Mirror Prevents Head-On Collisions</text>
</svg>
</div>
How does a large circular convex mirror installed at a mountainous hairpin bend help prevent head-on vehicle collisions?""",
     ["It gives drivers approaching from blind angles a wide-angle erect view of oncoming vehicles hidden around the curve""",
     "It focuses headlight beams to warm icy mountain roads""",
     "It magnifies roadside warning signs""",
     "It sounds an automatic audio siren"],
     "A", "OSC", "easy""",
     "The wide-angle convex reflector allows approaching drivers on either side of an obstructed corner to see reflections of oncoming vehicles, eliminating blind spots."),

    # 76: Store Anti-Theft Surveillance Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Corner dome mirror -->
  <path d="M 40,40 L 40,110 A 70,70 0 0,0 110,40 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <!-- Aisle lines spreading out -->
  <line x1="110" y1="40" x2="280" y2="70" stroke="#facc15" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="40" y1="110" x2="180" y2="160" stroke="#facc15" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="140" y="110" fill="#facc15" font-size="10">Supermarket Shopping Aisles</text>
  <text x="130" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Ceiling-Corner Security Convex Mirror</text>
  <text x="60" y="180" fill="#cbd5e1" font-size="10">Provides single-point overview across multiple store aisles</text>
</svg>
</div>
Why are high-mounted convex dome mirrors placed in supermarket ceiling corners for anti-theft security?""",
     ["Their wide-angle reflection lets store clerks monitor multiple shopping aisles from a single checkout counter""",
     "They record video footage without electricity""",
     "They detect metal barcodes on merchandise""",
     "They brighten shop corners by concentrating fluorescent light"],
     "A", "OSC", "easy""",
     "A single convex mirror provides a wide panoramic overview of several long aisles, allowing staff to spot shoplifters over partitions."),

    # 77: ATM Security Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="70" y="30" width="200" height="130" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- ATM Screen -->
  <rect x="90" y="50" width="100" height="60" fill="#0284c7"/>
  <text x="105" y="85" fill="#f8fafc" font-size="10">ATM Display</text>
  <!-- Small convex mirror above screen -->
  <circle cx="230" cy="80" r="22" fill="#334155" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 215,80 A 15,15 0 0,1 245,80" fill="none" stroke="#facc15" stroke-width="2"/>
  <text x="210" y="120" fill="#38bdf8" font-size="9">Convex Mirror</text>
  <text x="60" y="180" fill="#facc15" font-size="10">Allows user to see who is standing behind them</text>
</svg>
</div>
What is the specific security purpose of the small convex mirror fitted on automated teller machines (ATMs)?""",
     ["It gives the user a wide-angle rear view to detect anyone standing behind them attempting to peek at their secret PIN""",
     "It verifies user retinal scans""",
     "It illuminates the numeric keypad""",
     "It connects to the bank's CCTV server"],
     "A", "OSC", "easy""",
     "The wide-angle convex view lets the ATM user discreetly see persons standing directly behind or to the side, preventing PIN shoulder-surfing."),

    # 78: Street Light Convex Reflector
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Lamp post and convex shade -->
  <path d="M 120,40 A 50,50 0 0,0 220,40" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="170" cy="50" r="8" fill="#facc15"/>
  <!-- Diverging beam spreading widely -->
  <line x1="170" y1="50" x2="30" y2="160" stroke="#facc15" stroke-width="2" stroke-dasharray="4,3"/>
  <line x1="170" y1="50" x2="310" y2="160" stroke="#facc15" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="100" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Street Light Convex Reflector</text>
  <text x="60" y="180" fill="#facc15" font-size="10">Diverges light across a broad roadway area rather than a spot</text>
</svg>
</div>
Why are convex reflectors used in street lighting lamps?""",
     ["To diverge light over a wide roadway area, illuminating as much pavement surface as possible""",
     "To produce a parallel spotlight beam for searching aircraft""",
     "To focus intense heat onto cars below""",
     "To produce magnified images of street pedestrians"],
     "A", "OSC", "easy""",
     "Unlike concave reflectors that concentrate light into a narrow beam, convex reflectors disperse light outward to maximize municipal street surface coverage."),

    # 79: Virtual vs Real Object Behavior
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 150,25 A 130,130 0 0,1 150,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="210" cy="95" r="3" fill="#4ade80"/><text x="206" y="85" fill="#4ade80" font-size="9">F</text>
  <circle cx="270" cy="95" r="3" fill="#f87171"/><text x="266" y="85" fill="#f87171" font-size="9">C</text>
  <text x="30" y="50" fill="#fbbf24" font-size="10">Real Object in front</text>
  <text x="30" y="70" fill="#4ade80" font-size="10">→ Virtual Erect Diminished Image between P &amp; F</text>
  <text x="30" y="130" fill="#ec4899" font-size="10">Magnification m is strictly: 0 &lt; m &lt; +1</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="10">Universal Rule: Convex mirror NEVER produces an inverted real image of real objects</text>
</svg>
</div>
What is the universal rule governing image formation by a convex mirror for any real object placed in front of it?""",
     ["The image is always virtual, erect, and diminished, located between pole P and focus F behind the mirror""",
     "The image is always real and inverted""",
     "The image size is always equal to the object""",
     "The image is magnified when placed inside the focal length"],
     "A", "OSC", "easy""",
     "Regardless of real object distance, reflected rays diverge outward into space; their backward virtual extensions strictly intersect between P and F, ensuring 0 < m < +1."),

    # 80: Reversal of Scale at Distance
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 200,25 A 130,130 0 0,1 200,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Near car object -->
  <line x1="120" y1="120" x2="120" y2="80" stroke="#4ade80" stroke-width="2.5"/>
  <text x="100" y="70" fill="#4ade80" font-size="9">Near Car (u_1)</text>
  <!-- Far truck object -->
  <line x1="40" y1="120" x2="40" y2="60" stroke="#f87171" stroke-width="3.5"/>
  <text x="20" y="50" fill="#f87171" font-size="9">Distant Truck (u_2)</text>
  <!-- Images behind mirror -->
  <line x1="230" y1="120" x2="230" y2="95" stroke="#4ade80" stroke-width="2" stroke-dasharray="2,2"/>
  <line x1="250" y1="120" x2="250" y2="105" stroke="#f87171" stroke-width="2" stroke-dasharray="2,2"/>
  <text x="60" y="175" fill="#facc15" font-size="10">Both vehicles fit in small mirror; farther vehicle appears closer to Focus F</text>
</svg>
</div>
In traffic rear-view monitoring, how does a convex mirror handle both a near vehicle and a distant truck simultaneously?""",
     ["Both vehicles form erect, diminished images simultaneously between P and F, fitting a large traffic scene onto a compact mirror""",
     "The distant truck blocks the near car completely""",
     "The near car is magnified to fill 100% of the mirror""",
     "The distant truck flips upside down"],
     "A", "OSC", "easy""",
     "Because all real objects compress into the small focal zone between P and F as erect diminished images, multiple vehicles at varying distances remain clearly visible simultaneously."),

    # 81: Spoon Back Experiment
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Spoon outer face -->
  <path d="M 170,30 Q 230,95 170,160 Q 190,95 170,30 Z" fill="#94a3b8"/>
  <text x="60" y="75" fill="#38bdf8" font-size="11" font-weight="bold">Outer bulging surface</text>
  <text x="60" y="95" fill="#38bdf8" font-size="9.5">Reflects as a Convex Mirror</text>
  <text x="60" y="115" fill="#4ade80" font-size="9.5">→ Erect &amp; Diminished Image</text>
  <text x="60" y="175" fill="#facc15" font-size="10">Observe your face: Reflection remains upright no matter how far you hold it</text>
</svg>
</div>
When you hold the bulging back of a shiny metal spoon at arm's length and slowly bring it closer to your nose, what happens to your facial reflection?""",
     ["The image remains upright (erect) at all times and gradually increases in size as it nears the spoon""",
     "The image inverts upside down when held far away and turns upright close by""",
     "The image is magnified 10 times at arm's length""",
     "The image disappears at the midpoint"],
     "A", "OSC", "easy""",
     "The bulging surface acts as a convex mirror: the image is always upright (erect) and grows moderately larger (approaching object size) as the spoon approaches the face."),

    # 82: Security Mirror Fisheye Perspective
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <circle cx="170" cy="95" r="70" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="4"/>
  <!-- Curved grid lines representing fisheye perspective -->
  <path d="M 120,40 Q 150,95 120,150" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 220,40 Q 190,95 220,150" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 105,75 Q 170,90 235,75" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 105,115 Q 170,100 235,115" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="120" y="98" fill="#facc15" font-size="11" font-weight="bold">Panoramic View</text>
  <text x="60" y="180" fill="#cbd5e1" font-size="10">Curved surface compresses 180^{\circ} spatial sector into visible aperture</text>
</svg>
</div>
What optical advantage does the curved fisheye geometry of a surveillance convex mirror provide in commercial premises?""",
     ["It compresses an entire 180^{\circ} room horizon into the observer's line of sight, eliminating corner hiding spots""",
     "It projects holographic 3D security warnings""",
     "It filters out infrared spy cameras""",
     "It reverses shadows to reveal dark corners"],
     "A", "OSC", "easy""",
     "The pronounced outward curvature captures rays from nearly a full hemispherical 180^{\circ} horizon, condensing the broad environment into a single compact, easily observed mirror face.")
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

    out_file = "scripts/ch11_topic4.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
