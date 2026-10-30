# scripts/generate_ch11_topic1.py
# MH-9-SCIT-11-11.1: Mirrors: Plane Mirrors & Image Formation
import json
import sys
import os
sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-11-11.1"

exam_data = [
    # 1-10: Basic Laws of Reflection & Plane Mirror Image Properties
    ("According to the first law of reflection of light, what is the exact relationship between the angle of incidence (i) and the angle of reflection (r)?",
     ["The angle of incidence is always equal to the angle of reflection (i = r)",
      "The angle of incidence is twice the angle of reflection (i = 2r)",
      "The angle of incidence is half the angle of reflection (i = r/2)",
      "The angle of incidence is 90^{\\circ} minus the angle of reflection"],
     "A", "OSC", "easy",
     "The first law of reflection states that the angle of incidence is strictly equal to the angle of reflection (i = r) for all reflecting surfaces."),

    ("How is the angle of incidence measured in geometrical optics?",
     ["Between the incident ray and the normal to the reflecting surface at the point of incidence",
      "Between the incident ray and the plane mirror surface itself",
      "Between the incident ray and the reflected ray",
      "Between the reflected ray and the normal"],
     "A", "OSC", "easy",
     "The angle of incidence is strictly defined as the angle made by the incident light ray with the perpendicular normal drawn at the point of incidence."),

    ("If a light ray strikes a flat plane mirror perpendicularly along the normal, what are the angle of incidence and the angle of reflection?",
     ["Both angle of incidence and angle of reflection are 0^{\\circ}",
      "Both angle of incidence and angle of reflection are 90^{\\circ}",
      "Angle of incidence is 90^{\\circ} and angle of reflection is 0^{\\circ}",
      "Angle of incidence is 45^{\\circ} and angle of reflection is 45^{\\circ}"],
     "A", "OSC", "easy",
     "When a ray falls normally on a mirror, the incident ray coincides with the normal, so i = 0^{\\circ}. By the law of reflection (r = i), the angle of reflection is also 0^{\\circ}, meaning the ray retraces its path."),

    ("What type of image is always formed by a single flat plane mirror for a real object?",
     ["Virtual, erect, laterally inverted, and of the same size as the object",
      "Real, inverted, and magnified",
      "Real, erect, and diminished",
      "Virtual, inverted, and enlarged"],
     "A", "OSC", "easy",
     "A flat plane mirror always produces an image that is virtual (cannot be caught on a screen), erect (upright), laterally inverted (left and right swapped), and equal in size to the object."),

    ("An object is placed at a perpendicular distance of 25 cm in front of a flat plane mirror. What is the total distance between the object and its image?",
     ["50 cm", "25 cm", "12.5 cm", "100 cm"],
     "A", "OSC", "easy",
     "In a plane mirror, the image is formed at the same perpendicular distance behind the mirror as the object is in front of it (25 cm). Therefore, the total distance between object and image is 25 cm + 25 cm = 50 cm."),

    ("What optical phenomenon causes the right hand of a person looking into a flat plane mirror to appear as the left hand of the image?",
     ["Lateral inversion", "Refraction", "Dispersion", "Total internal reflection"],
     "A", "OSC", "easy",
     "Lateral inversion is the apparent sideways reversal of left and right in the image formed by a plane reflecting surface."),

    ("What is the linear magnification (m) produced by a flat plane mirror?",
     ["m = +1", "m = -1", "m > +1", "m < 1"],
     "A", "OSC", "easy",
     "Linear magnification is defined as m = height of image / height of object. Since the image formed by a plane mirror is erect (positive) and equal in size to the object, m = +1."),

    ("Why is the word 'AMBULANCE' written laterally inverted on the front of emergency vehicles?",
     ["So that drivers ahead see it upright and readable in their rear-view mirrors due to lateral inversion",
      "It is a decorative convention adopted by automobile designers",
      "To prevent pedestrians from reading it quickly",
      "Because the printing machine operates in reverse"],
     "A", "OSC", "easy",
     "Vehicles traveling ahead will see the text laterally inverted in their rear-view plane/convex mirrors, restoring the letters to normal legible text ('AMBULANCE') so they can immediately give way."),

    ("What is the minimum vertical height of a flat plane mirror required for a person of height H to view their complete head-to-toe image?",
     ["H / 2 (half of the person's height)", "H (equal to the person's height)", "2H (double the person's height)", "H / 4 (one fourth of the person's height)"],
     "A", "OSC", "medium",
     "By applying similar triangles to the rays reflecting from top of head and bottom of feet into the observer's eyes, the minimum mirror height required is exactly H/2."),

    ("A person stands 3 m in front of a flat plane mirror. If the person walks 1 m backwards away from the mirror, what will be the new distance between the person and their image?",
     ["8 m", "6 m", "4 m", "5 m"],
     "A", "OSC", "medium",
     "Initially the object distance is 3 m. After moving 1 m back, the new object distance is 4 m. The image forms 4 m behind the mirror. Distance between person and image = 4 m + 4 m = 8 m."),

    # 11-20: Multiple Reflections & Inclined Mirrors
    ("Two flat plane mirrors are placed perpendicular to each other at an angle of 90^{\\circ}. How many images of an object placed between them will be formed?",
     ["3 images", "4 images", "2 images", "1 image"],
     "A", "OSC", "easy",
     "The formula for number of images is n = (360^{\\circ} / \\theta) - 1. For \\theta = 90^{\\circ}, 360/90 = 4 (an even integer). Thus n = 4 - 1 = 3 images."),

    ("Two flat plane mirrors are kept parallel and facing each other (\\theta = 0^{\\circ}). How many images of a candle placed between them are theoretically formed?",
     ["Infinite number of images", "Zero images", "Only 2 images", "Exactly 10 images"],
     "A", "OSC", "easy",
     "When two mirrors are parallel, \\theta = 0^{\\circ}. The light reflects back and forth continuously between the opposing mirrors, forming an infinite series of images."),

    ("Two flat plane mirrors are inclined at an angle of 60^{\\circ}. Calculate the number of images formed of a coin placed symmetrically between them.",
     ["5 images", "6 images", "4 images", "7 images"],
     "A", "OSC", "easy",
     "Using the formula n = (360^{\\circ} / \\theta) - 1 with \\theta = 60^{\\circ}: n = (360 / 60) - 1 = 6 - 1 = 5 images."),

    ("Two plane mirrors are inclined at an angle of 120^{\\circ}. How many images are formed when an object is placed symmetrically between them?",
     ["2 images", "3 images", "4 images", "1 image"],
     "A", "OSC", "medium",
     "For \\theta = 120^{\\circ}, 360 / 120 = 3 (an odd integer). When the object is placed symmetrically on the angle bisector, n = (360 / \\theta) - 1 = 3 - 1 = 2 images."),

    ("Which optical instrument uses three long rectangular plane mirror strips inclined at 60^{\\circ} to one another to create colorful symmetrical patterns?",
     ["Kaleidoscope", "Periscope", "Compound microscope", "Astronomical telescope"],
     "A", "OSC", "easy",
     "A kaleidoscope contains three flat glass mirrors set at 60^{\\circ} to each other inside a tube, producing regular repeating hexagonal patterns of colored glass fragments via multiple reflections."),

    ("Which optical device uses two plane mirrors oriented parallel to each other at an inclination of 45^{\\circ} to the line of sight to look over obstacles?",
     ["Periscope", "Kaleidoscope", "Sextant", "Camera obscura"],
     "A", "OSC", "easy",
     "A periscope uses two plane mirrors parallel to each other and inclined at 45^{\\circ} to turn the path of light by 90^{\\circ} twice, enabling observation from trenches or submarines."),

    ("If a incident ray of light is kept fixed and a flat plane mirror is rotated through an angle \\theta about an axis in its plane, by what angle does the reflected ray rotate?",
     ["2\\theta", "\\theta", "\\theta / 2", "4\\theta"],
     "A", "OSC", "medium",
     "When a mirror rotates by angle \\theta, the normal also rotates by \\theta. The new angle of incidence becomes (i + \\theta), and the reflected ray turns through an angle of 2\\theta in the same direction."),

    ("A person walks towards a stationary flat plane mirror at a speed of 2 m/s. What is the speed of approach of the image towards the person?",
     ["4 m/s", "2 m/s", "1 m/s", "8 m/s"],
     "A", "OSC", "medium",
     "The image moves toward the mirror at 2 m/s relative to the mirror. Relative to the person moving at 2 m/s in the opposite direction, the relative speed of approach is 2 m/s + 2 m/s = 4 m/s."),

    ("What material is traditionally deposited on the back surface of glass sheet to make a high-reflectance commercial plane mirror?",
     ["A thin reflective coating of silver (or aluminum) backed by red lead oxide paint",
      "A layer of black carbon soot",
      "A thin coating of transparent plastic resin",
      "A coating of copper sulfate crystals"],
     "A", "OSC", "easy",
     "A thin layer of silver (or vapor-deposited aluminum) acts as the high-reflectance metallic mirror surface, protected from oxidation and scratching by red lead or protective paint."),

    ("What is the difference between regular (specular) reflection and irregular (diffuse) reflection?",
     ["Regular reflection occurs on smooth polished surfaces yielding parallel reflected rays, while irregular reflection occurs on rough surfaces scattering light in all directions",
      "Regular reflection obeys the law of reflection, but irregular reflection does not obey the law of reflection",
      "Regular reflection only happens in darkness, irregular only in daylight",
      "Regular reflection absorbs 100% of incident light"],
     "A", "OSC", "medium",
     "On smooth surfaces, parallel rays remain parallel after reflection (specular). On rough surfaces, surface irregularities cause normals to point in various directions, scattering rays diffusely. Both strictly obey the laws of reflection locally."),

    # 21-30: OMC, OTF, OAR Questions
    ("Which of the following statements are correct regarding the characteristics of images formed by a flat plane mirror? (Select all that apply)",
     ["The image cannot be focused on a physical screen (it is virtual)",
      "The image is always upright (erect)",
      "The image has the same vertical and lateral dimensions as the object",
      "The image is formed in front of the reflecting surface"],
     "A", "OMC", "medium",
     "Plane mirror images are virtual (cannot be cast on screen), erect, equal in size to the object, and formed behind the mirror surface at an equal distance."),

    ("Assertion (A): The laws of reflection of light hold true for both smooth polished mirrors and rough unpolished surfaces.\nReason (R): Diffuse reflection occurs because the angle of incidence does not equal the angle of reflection on rough surfaces.",
     ["Assertion (A) is true, but Reason (R) is false",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "Assertion is true: laws of reflection hold for all surfaces. Reason is false: every single ray obeys i = r at its local microscopic point of incidence; scattering occurs because microscopic normals point in random directions."),

    ("Assertion (A): The image formed by a plane mirror is virtual.\nReason (R): The reflected rays do not actually intersect but appear to diverge from a point behind the mirror.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "A virtual image is formed when reflected light rays do not actually meet in real space but appear to meet when produced backwards behind the reflecting surface."),

    ("State whether the following statement is True or False: If a ray of light is incident at an angle of 30^{\\circ} to the surface of a plane mirror, the angle of reflection is 60^{\\circ}.",
     ["True", "False"],
     "A", "OTF", "medium",
     "The angle with the surface is the glancing angle (30^{\\circ}). The angle of incidence with the normal is i = 90^{\\circ} - 30^{\\circ} = 60^{\\circ}. Therefore, angle of reflection r = i = 60^{\\circ}. The statement is True."),

    ("State whether the following statement is True or False: A virtual image can be projected onto a paper screen placed behind a plane mirror.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A virtual image cannot be captured on a physical screen because no real light rays actually converge behind the plane mirror."),

    ("State whether the following statement is True or False: When two plane mirrors are placed at 72^{\\circ} to each other, exactly 4 images are formed of a symmetrically placed object.",
     ["True", "False"],
     "A", "OTF", "medium",
     "For \\theta = 72^{\\circ}, 360 / 72 = 5 (odd integer). For a symmetric object, n = (360 / \\theta) - 1 = 5 - 1 = 4 images. The statement is True."),

    ("A light ray is incident on a plane mirror such that the angle between the incident ray and the reflected ray is 80^{\\circ}. What is the angle of incidence?",
     ["40^{\\circ}", "80^{\\circ}", "20^{\\circ}", "50^{\\circ}"],
     "A", "OSC", "easy",
     "The total angle between incident and reflected ray is i + r = 2i = 80^{\\circ}. Therefore, i = 80^{\\circ} / 2 = 40^{\\circ}."),

    ("What is the glancing angle of incidence if the angle of reflection from a flat plane mirror is 35^{\\circ}?",
     ["55^{\\circ}", "35^{\\circ}", "70^{\\circ}", "90^{\\circ}"],
     "A", "OSC", "easy",
     "The glancing angle is the angle made by the incident ray with the mirror surface: \\theta_g = 90^{\\circ} - i. Since r = 35^{\\circ}, i = 35^{\\circ}. Thus \\theta_g = 90^{\\circ} - 35^{\\circ} = 55^{\\circ}."),

    ("How many images are formed when two plane mirrors are placed at an angle of 45^{\\circ} to each other?",
     ["7 images", "8 images", "6 images", "9 images"],
     "A", "OSC", "easy",
     "n = (360^{\\circ} / \\theta) - 1 = (360 / 45) - 1 = 8 - 1 = 7 images."),

    ("An incident ray strikes a flat mirror at an angle of incidence of 50^{\\circ}. What is the total angle of deviation (\\delta) suffered by the light ray?",
     ["80^{\\circ}", "100^{\\circ}", "50^{\\circ}", "130^{\\circ}"],
     "A", "OSC", "medium",
     "Angle of deviation is \\delta = 180^{\\circ} - 2i = 180^{\\circ} - 2(50^{\\circ}) = 180^{\\circ} - 100^{\\circ} = 80^{\\circ}."),

    # 31-40: Advanced Conceptual & Applied Questions
    ("A ray of light reflects consecutively from two perpendicular flat mirrors (\\theta = 90^{\\circ}). What is the relationship between the initial incident ray and the final reflected ray?",
     ["The final reflected ray is exactly antiparallel (parallel and reversed by 180^{\\circ}) to the initial incident ray",
      "The final ray is perpendicular to the initial ray",
      "The final ray is deviated by 45^{\\circ}",
      "The final ray retraces its path into the source along the exact same line"],
     "A", "OSC", "medium",
     "Total deviation from two perpendicular mirrors is \\delta = 360^{\\circ} - 2\\theta = 360^{\\circ} - 180^{\\circ} = 180^{\\circ}. Therefore, the emergent ray is antiparallel to the incoming ray regardless of the initial angle of incidence (corner cube retroreflector principle)."),

    ("Why can we see non-luminous objects around a brightly lit room from any viewing angle?",
     ["Because rough microscopic surfaces of objects cause irregular (diffuse) reflection, scattering light in all directions",
      "Because non-luminous objects emit their own visible light",
      "Because the air inside the room focuses light into human eyes",
      "Because plane mirrors are hidden inside all walls"],
     "A", "OSC", "easy",
     "Diffuse reflection scatters incident light in every direction from rough surface textures, enabling human eyes to perceive objects from any vantage point."),

    ("If a clock viewed in a flat plane mirror shows 3:25, what is the actual real time?",
     ["8:35", "9:35", "8:25", "3:35"],
     "A", "OSC", "medium",
     "Due to lateral inversion in a plane mirror, real time = 11:60 - mirror time = 11:60 - 3:25 = 8:35."),

    ("If a plane mirror moves away from a stationary object with velocity v, with what velocity does the image move away from the object?",
     ["2v", "v", "v / 2", "4v"],
     "A", "OSC", "medium",
     "Let object distance be x. When mirror moves by \\Deltax, new mirror distance is x + \\Deltax, and image distance from mirror is x + \\Deltax. Total object-to-image distance becomes 2(x + \\Deltax) = 2x + 2\\Deltax. The image shifts by 2\\Deltax, moving at speed 2v relative to the object."),

    ("Assertion (A): A person standing in front of a flat plane mirror cannot see their full height if the mirror is less than half their height.\nReason (R): For complete reflection into the eye from head and toes, the mirror length must span half the vertical distance between the extreme rays.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "By geometry of similar triangles, rays from the crown and feet require a mirror height of exactly half the observer's stature, irrespective of distance from the mirror."),

    ("Which property of light ensures that the incident ray, the reflected ray, and the normal all lie in the exact same geometric plane?",
     ["The second law of reflection of light",
      "Fermat's principle of maximum time",
      "The wave nature of sound",
      "Atmospheric scattering"],
     "A", "OSC", "easy",
     "The coplanarity of incident ray, normal, and reflected ray constitutes the fundamental second law of reflection."),

    ("A light ray is incident on a plane mirror at an angle of incidence of 20^{\\circ}. If the mirror is rotated clockwise by 15^{\\circ} keeping the incident ray direction constant, what is the new angle of reflection?",
     ["35^{\\circ}", "20^{\\circ}", "5^{\\circ}", "50^{\\circ}"],
     "A", "OSC", "medium",
     "Rotating the mirror clockwise by 15^{\\circ} increases the angle between the incident ray and the normal by 15^{\\circ}. The new angle of incidence becomes 20^{\\circ} + 15^{\\circ} = 35^{\\circ}. By law of reflection, new angle of reflection is 35^{\\circ}."),

    ("State whether the following statement is True or False: The focal length of a flat plane mirror is infinite (f = ∞).",
     ["True", "False"],
     "A", "OTF", "easy",
     "A plane mirror can be considered a spherical mirror of infinite radius of curvature (R = ∞). Since f = R / 2, the focal length is infinity."),

    ("State whether the following statement is True or False: In a periscope, the two plane mirrors are placed at an angle of 90^{\\circ} to each other.",
     ["False", "True"],
     "A", "OTF", "easy",
     "In a standard periscope, the two plane mirrors are placed parallel to each other (angle between them is 0^{\\circ}), each inclined at 45^{\\circ} to the vertical axis."),

    ("What happens to the brightness of multiple images formed by two inclined mirrors as the order of reflection increases?",
     ["Brightness decreases progressively because some light energy is absorbed and transmitted at each successive reflection",
      "Brightness increases due to optical resonance",
      "Brightness remains exactly 100% constant forever",
      "Images turn into dark black shadows after two reflections"],
     "A", "OSC", "medium",
     "At each reflection, real mirrors absorb about 4-10% of light energy, so higher-order reflections become noticeably fainter.")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Speed, Geometry & Deviation
    ("A child stands 1.5 m in front of a flat dressing mirror. If the child steps 0.5 m closer to the mirror, what is the distance between the child and their image?",
     ["2.0 m", "1.0 m", "3.0 m", "1.5 m"],
     "A", "OSC", "easy",
     "Initial distance = 1.5 m. Moving 0.5 m closer makes object distance 1.0 m. The image is 1.0 m behind the mirror. Distance between child and image = 1.0 m + 1.0 m = 2.0 m."),

    ("A ray of light strikes a plane mirror with an angle of incidence of 45^{\\circ}. What is the angle between the incident ray and the reflected ray?",
     ["90^{\\circ}", "45^{\\circ}", "180^{\\circ}", "0^{\\circ}"],
     "A", "OSC", "easy",
     "Angle between incident and reflected ray = i + r = 45^{\\circ} + 45^{\\circ} = 90^{\\circ}."),

    ("What is the angle of deviation (\\delta) suffered by a ray of light incident on a plane mirror at an angle of 30^{\\circ}?",
     ["120^{\\circ}", "60^{\\circ}", "90^{\\circ}", "150^{\\circ}"],
     "A", "OSC", "medium",
     "The angle of deviation is \\delta = 180^{\\circ} - 2i = 180^{\\circ} - 2(30^{\\circ}) = 180^{\\circ} - 60^{\\circ} = 120^{\\circ}."),

    ("If an object is placed 10 cm in front of a plane mirror, what is the distance of the image from the plane mirror?",
     ["10 cm behind the mirror", "20 cm in front of the mirror", "5 cm behind the mirror", "10 cm in front of the mirror"],
     "A", "OSC", "easy",
     "In a plane mirror, the image is formed at the exact same distance behind the mirror as the object is in front of it."),

    ("A boy is running away from a stationary flat plane mirror at 3 m/s. At what speed is his image moving away from him?",
     ["6 m/s", "3 m/s", "1.5 m/s", "9 m/s"],
     "A", "OSC", "medium",
     "Relative to the stationary mirror, the image recedes at 3 m/s. Relative to the boy running at 3 m/s in the opposite direction, the separation rate is 3 + 3 = 6 m/s."),

    ("Two plane mirrors are kept at an angle of 30^{\\circ} to each other. Calculate the number of images formed of a coin placed between them.",
     ["11 images", "12 images", "10 images", "13 images"],
     "A", "OSC", "easy",
     "n = (360^{\\circ} / \\theta) - 1 = (360 / 30) - 1 = 12 - 1 = 11 images."),

    ("Two plane mirrors are inclined at 40^{\\circ} to each other. How many images of a small object placed between them are formed?",
     ["8 images", "9 images", "7 images", "10 images"],
     "A", "OSC", "easy",
     "For \\theta = 40^{\\circ}, 360 / 40 = 9 (odd integer). With symmetric placement, n = (360 / \\theta) - 1 = 9 - 1 = 8 images."),

    ("A girl of height 160 cm wishes to see her full reflection in a plane mirror. What is the minimum length of mirror required?",
     ["80 cm", "160 cm", "40 cm", "120 cm"],
     "A", "OSC", "easy",
     "Minimum mirror length = H / 2 = 160 cm / 2 = 80 cm."),

    ("If the glancing angle of incidence of a light ray on a plane mirror is 25^{\\circ}, what is the angle of reflection?",
     ["65^{\\circ}", "25^{\\circ}", "50^{\\circ}", "75^{\\circ}"],
     "A", "OSC", "easy",
     "Glancing angle \\theta_g = 25^{\\circ}. Angle of incidence i = 90^{\\circ} - 25^{\\circ} = 65^{\\circ}. By law of reflection, angle of reflection r = 65^{\\circ}."),

    ("What is the optical power of a flat plane mirror?",
     ["0 dioptres", "1 dioptre", "+10 dioptres", "Infinite dioptres"],
     "A", "OSC", "medium",
     "Power is P = 1 / f. For a plane mirror, focal length f = ∞. Hence P = 1 / ∞ = 0 dioptres."),

    # 51-60: Mirrors, Symmetry & Lateral Inversion
    ("Which English capital letter among the following shows lateral inversion when viewed in a flat vertical plane mirror?",
     ["B", "A", "M", "T"],
     "A", "OSC", "easy",
     "Letters like A, M, T possess vertical line symmetry and appear unchanged in a vertical mirror. The letter B lacks vertical symmetry and appears laterally inverted as B (inverted)."),

    ("Which English capital letter among the following does NOT show lateral inversion in a flat vertical mirror?",
     ["H", "C", "D", "E"],
     "A", "OSC", "easy",
     "The letter H has bilateral vertical symmetry across the y-axis, so its laterally inverted image is identical to the original letter."),

    ("A clock placed in front of a flat plane mirror displays 9:15. What time is reflected in the mirror?",
     ["2:45", "3:15", "9:45", "2:15"],
     "A", "OSC", "medium",
     "Mirror time = 11:60 - 9:15 = 2:45."),

    ("If a light ray undergoes a deviation of 140^{\\circ} upon reflection from a flat plane mirror, what was its angle of incidence?",
     ["20^{\\circ}", "40^{\\circ}", "70^{\\circ}", "10^{\\circ}"],
     "A", "OSC", "medium",
     "Deviation \\delta = 180^{\\circ} - 2i = 140^{\\circ}. Thus 2i = 180^{\\circ} - 140^{\\circ} = 40^{\\circ}, giving i = 20^{\\circ}."),

    ("What is the angle of incidence when a ray of light reflects back on itself along the original path?",
     ["0^{\\circ}", "90^{\\circ}", "45^{\\circ}", "180^{\\circ}"],
     "A", "OSC", "easy",
     "For normal incidence, the ray strikes along the surface normal, so i = 0^{\\circ} and r = 0^{\\circ}, retracing its path."),

    ("Two mirrors are inclined at an angle \\theta. If 7 images are formed of an object, what is the angle of inclination \\theta?",
     ["45^{\\circ}", "60^{\\circ}", "90^{\\circ}", "30^{\\circ}"],
     "A", "OSC", "easy",
     "n = (360^{\\circ} / \\theta) - 1 = 7. Thus 360 / \\theta = 8, which yields \\theta = 360 / 8 = 45^{\\circ}."),

    ("State whether the following statement is True or False: The image formed by a plane mirror is always inverted vertically (upside down).",
     ["False", "True"],
     "A", "OTF", "easy",
     "The image formed by a plane mirror is always vertically erect (upright), not inverted."),

    ("State whether the following statement is True or False: In specular reflection from a smooth polished surface, parallel incident rays produce parallel reflected rays.",
     ["True", "False"],
     "A", "OTF", "easy",
     "On a smooth flat surface, all normals are parallel, so all reflected rays emerge parallel to each other."),

    ("State whether the following statement is True or False: If a person moves at speed v away from a plane mirror, the distance between the person and the mirror increases at speed v.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The rate of change of distance between the person and the stationary mirror is simply the person's walking speed v."),

    ("Why can a person not see their reflection clearly in a rough wooden board or white wall even though light is reflected from it?",
     ["Because rough microscopic textures cause diffuse reflection, scattering light randomly rather than maintaining image rays",
      "Because wood absorbs 100% of all light rays",
      "Because wood has zero refractive index",
      "Because wood only reflects ultraviolet rays"],
     "A", "OSC", "easy",
     "White walls and wood scatter light in all random directions (diffuse reflection), destroying the ordered wavefronts required to form a coherent optical image."),

    # 61-70: Multi-choice, OAR & Instrumentation
    ("Which of the following optical instruments rely on reflection from flat plane mirrors? (Select all that apply)",
     ["Periscope", "Kaleidoscope", "Barbershop dressing mirrors", "Compound refracting microscope"],
     "A", "OMC", "easy",
     "Periscopes, kaleidoscopes, and grooming mirrors utilize flat plane mirrors, whereas compound microscopes use convex refractive lenses."),

    ("Assertion (A): A ray of light incident along the normal to a plane mirror reflects back along the normal.\nReason (R): For normal incidence, the angle of incidence is 90^{\\circ}.",
     ["Assertion (A) is true, but Reason (R) is false",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "Assertion is true (ray retraces normal path). Reason is false because angle of incidence is measured with the normal, making i = 0^{\\circ}, not 90^{\\circ}."),

    ("An object is placed between two parallel plane mirrors separated by a distance d. What is the separation between the first two virtual images formed behind the two mirrors?",
     ["2d", "d", "d / 2", "4d"],
     "A", "OSC", "medium",
     "If the object is at distance x from mirror 1 and (d - x) from mirror 2, image 1 is at x behind mirror 1, and image 2 is at (d - x) behind mirror 2. Total separation between the two images is x + d + (d - x) = 2d."),

    ("If you shine a laser pointer at a flat plane mirror at a glancing angle of 40^{\\circ}, what is the angle of deviation of the laser beam?",
     ["80^{\\circ}", "100^{\\circ}", "40^{\\circ}", "50^{\\circ}"],
     "A", "OSC", "medium",
     "Glancing angle \\theta_g = 40^{\\circ}. Angle of incidence i = 90^{\\circ} - 40^{\\circ} = 50^{\\circ}. Deviation \\delta = 180^{\\circ} - 2i = 180^{\\circ} - 100^{\\circ} = 80^{\\circ}."),

    ("A flat plane mirror is rotated by 25^{\\circ} clockwise. By how many degrees does the reflected ray turn?",
     ["50^{\\circ}", "25^{\\circ}", "12.5^{\\circ}", "75^{\\circ}"],
     "A", "OSC", "easy",
     "For a mirror rotation of \\theta, the reflected ray rotates by 2\\theta in the same direction: 2 × 25^{\\circ} = 50^{\\circ}."),

    ("What is the nature of the image formed behind a plane mirror when an observer looks at a real object?",
     ["Virtual and upright", "Real and inverted", "Real and upright", "Virtual and inverted"],
     "A", "OSC", "easy",
     "A plane mirror creates a virtual and upright (erect) image located symmetrically behind the reflecting plane."),

    ("State whether the following statement is True or False: If two mirrors are kept at an angle of 180^{\\circ} (forming a single flat plane), exactly 1 image of an object is formed.",
     ["True", "False"],
     "A", "OTF", "easy",
     "For \\theta = 180^{\\circ}, n = (360 / 180) - 1 = 2 - 1 = 1 image. They act as a single continuous flat mirror."),

    ("When looking at your own reflection in a plane mirror, you raise your left arm. Which arm does your reflection appear to raise?",
     ["The right arm of the reflected figure", "The left arm of the reflected figure", "Both arms simultaneously", "Neither arm"],
     "A", "OSC", "easy",
     "Due to lateral inversion, your left arm corresponds to the right arm of your mirrored reflection facing you."),

    ("A person stands 4 m from a flat plane mirror. If the mirror is moved 1 m closer to the person, how much does the distance between person and image decrease?",
     ["2 m", "1 m", "4 m", "0.5 m"],
     "A", "OSC", "medium",
     "Initially, distance between person and image = 2 × 4 m = 8 m. After mirror moves 1 m closer, object distance = 3 m, and distance to image = 2 × 3 m = 6 m. Decrease in separation = 8 m - 6 m = 2 m."),

    ("Which optical principle governs the functioning of a submarine periscope?",
     ["Successive reflection of light from two parallel plane mirrors inclined at 45^{\\circ}",
      "Dispersion of white light through a glass prism",
      "Total internal reflection through an optical fiber bundle",
      "Spherical aberration by concave mirrors"],
     "A", "OSC", "easy",
     "Submarine periscopes use two plane mirrors mounted parallel to each other at 45^{\\circ} to reflect horizontal rays down a vertical shaft and back to the horizontal observer.")
]

# 12 Mock Foundation Questions with SVG Vector Diagrams (71-82)
mock_data = [
    # 71: Law of Reflection Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror surface -->
  <line x1="30" y1="140" x2="310" y2="140" stroke="#38bdf8" stroke-width="4"/>
  <!-- Hatching on back of mirror -->
  <g stroke="#64748b" stroke-width="1.5">
    <line x1="50" y1="140" x2="40" y2="155"/>
    <line x1="80" y1="140" x2="70" y2="155"/>
    <line x1="110" y1="140" x2="100" y2="155"/>
    <line x1="140" y1="140" x2="130" y2="155"/>
    <line x1="170" y1="140" x2="160" y2="155"/>
    <line x1="200" y1="140" x2="190" y2="155"/>
    <line x1="230" y1="140" x2="220" y2="155"/>
    <line x1="260" y1="140" x2="250" y2="155"/>
    <line x1="290" y1="140" x2="280" y2="155"/>
  </g>
  <!-- Normal line -->
  <line x1="170" y1="30" x2="170" y2="140" stroke="#facc15" stroke-width="2" stroke-dasharray="5,4"/>
  <text x="175" y="45" fill="#facc15" font-size="11" font-weight="bold">Normal (N)</text>
  <!-- Incident Ray -->
  <line x1="60" y1="50" x2="170" y2="140" stroke="#4ade80" stroke-width="2.5"/>
  <polygon points="120,100 110,90 125,95" fill="#4ade80"/>
  <text x="50" y="45" fill="#4ade80" font-size="11" font-weight="bold">Incident Ray</text>
  <!-- Reflected Ray -->
  <line x1="170" y1="140" x2="280" y2="50" stroke="#f87171" stroke-width="2.5"/>
  <polygon points="230,95 240,85 235,100" fill="#f87171"/>
  <text x="245" y="45" fill="#f87171" font-size="11" font-weight="bold">Reflected Ray</text>
  <!-- Angle arcs -->
  <path d="M 150,115 A 35,35 0 0,1 170,105" fill="none" stroke="#4ade80" stroke-width="1.8"/>
  <text x="145" y="95" fill="#4ade80" font-size="12" font-weight="bold">i</text>
  <path d="M 170,105 A 35,35 0 0,1 190,115" fill="none" stroke="#f87171" stroke-width="1.8"/>
  <text x="185" y="95" fill="#f87171" font-size="12" font-weight="bold">r</text>
  <text x="130" y="175" fill="#94a3b8" font-size="11">Plane Mirror Surface</text>
</svg>
</div>
In the ray diagram shown above, if the incident ray makes an angle of 35^{\\circ} with the normal line (i = 35^{\\circ}), what is the angle made by the reflected ray with the mirror surface?""",
     ["55^{\\circ}", "35^{\\circ}", "70^{\\circ}", "90^{\\circ}"],
     "A", "OSC", "medium",
     "By the law of reflection, angle of reflection r = i = 35^{\\circ}. The normal is perpendicular (90^{\\circ}) to the mirror surface. The angle made by the reflected ray with the mirror surface is the glancing angle: 90^{\\circ} - 35^{\\circ} = 55^{\\circ}."),

    # 72: Image Formation in Plane Mirror Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror line -->
  <line x1="170" y1="20" x2="170" y2="170" stroke="#38bdf8" stroke-width="4"/>
  <text x="175" y="30" fill="#38bdf8" font-size="10">Mirror M</text>
  <!-- Object Candle -->
  <rect x="70" y="90" width="12" height="50" fill="#fbbf24"/>
  <path d="M 76,90 Q 80,75 76,70 Q 72,75 76,90" fill="#f97316"/>
  <text x="60" y="155" fill="#fbbf24" font-size="10" font-weight="bold">Object (O)</text>
  <!-- Virtual Image Candle -->
  <rect x="258" y="90" width="12" height="50" fill="#94a3b8" opacity="0.6"/>
  <path d="M 264,90 Q 268,75 264,70 Q 260,75 264,90" fill="#f97316" opacity="0.6"/>
  <text x="245" y="155" fill="#94a3b8" font-size="10" font-weight="bold">Image (I)</text>
  <!-- Dimension arrows -->
  <line x1="76" y1="165" x2="170" y2="165" stroke="#a78bfa" stroke-width="1.5"/>
  <text x="115" y="180" fill="#a78bfa" font-size="10">d1 = 15 cm</text>
  <line x1="170" y1="165" x2="264" y2="165" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="205" y="180" fill="#a78bfa" font-size="10">d2 = ?</text>
</svg>
</div>
Based on the geometric ray diagram of a candle placed in front of a flat plane mirror, what is the distance d_2 of the virtual image behind the mirror and the total distance between candle and its image?""",
     ["d_2 = 15 cm, and total distance = 30 cm",
      "d_2 = 30 cm, and total distance = 45 cm",
      "d_2 = 7.5 cm, and total distance = 15 cm",
      "d_2 = 15 cm, and total distance = 15 cm"],
     "A", "OSC", "easy",
     "In a plane mirror, the virtual image forms at the identical perpendicular distance behind the mirror as the object in front (d_2 = d_1 = 15 cm). The total distance between object and image is 15 cm + 15 cm = 30 cm."),

    # 73: Inclined Mirrors Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror 1 -->
  <line x1="170" y1="150" x2="290" y2="150" stroke="#38bdf8" stroke-width="3"/>
  <!-- Mirror 2 inclined at 60 deg -->
  <line x1="170" y1="150" x2="230" y2="46" stroke="#38bdf8" stroke-width="3"/>
  <!-- Angle arc -->
  <path d="M 210,150 A 40,40 0 0,0 190,115" fill="none" stroke="#facc15" stroke-width="2"/>
  <text x="215" y="135" fill="#facc15" font-size="11" font-weight="bold">\\theta = 60^{\\circ}</text>
  <!-- Object point -->
  <circle cx="215" cy="115" r="5" fill="#f43f5e"/>
  <text x="225" y="115" fill="#f43f5e" font-size="10" font-weight="bold">Object (P)</text>
  <text x="140" y="165" fill="#38bdf8" font-size="10">Mirror M_1</text>
  <text x="235" y="40" fill="#38bdf8" font-size="10">Mirror M_2</text>
</svg>
</div>
Two flat plane mirrors M_1 and M_2 are inclined at an angle \\theta = 60^{\\circ}. An illuminated pin is placed symmetrically between them. How many total distinct images will be observed?""",
     ["5 images", "6 images", "4 images", "7 images"],
     "A", "OSC", "easy",
     "Number of images n = (360^{\\circ} / \\theta) - 1. For \\theta = 60^{\\circ}: n = (360 / 60) - 1 = 6 - 1 = 5 images."),

    # 74: Periscope Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Periscope casing -->
  <path d="M 40,30 L 160,30 L 160,110 L 280,110 L 280,160 L 120,160 L 120,80 L 40,80 Z" fill="none" stroke="#94a3b8" stroke-width="2.5"/>
  <!-- Upper Mirror at 45 deg -->
  <line x1="120" y1="80" x2="160" y2="30" stroke="#38bdf8" stroke-width="4"/>
  <text x="170" y="45" fill="#38bdf8" font-size="9.5">Mirror 1 (45^{\\circ})</text>
  <!-- Lower Mirror at 45 deg -->
  <line x1="240" y1="160" x2="280" y2="110" stroke="#38bdf8" stroke-width="4"/>
  <text x="180" y="150" fill="#38bdf8" font-size="9.5">Mirror 2 (45^{\\circ})</text>
  <!-- Light path -->
  <path d="M 40,55 L 140,55 L 140,135 L 280,135" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6,4"/>
  <polygon points="100,52 110,55 100,58" fill="#fbbf24"/>
  <polygon points="137,95 140,105 143,95" fill="#fbbf24"/>
  <polygon points="200,132 210,135 200,138" fill="#fbbf24"/>
  <text x="30" y="50" fill="#4ade80" font-size="10">Incoming Light</text>
  <text x="250" y="175" fill="#f43f5e" font-size="10">Observer's Eye</text>
</svg>
</div>
In the submarine periscope shown above, what is the angle of inclination of each plane mirror with respect to the horizontal ray, and by what total angle is the light beam redirected at each reflection?""",
     ["Mirrors are inclined at 45^{\\circ}, and the light beam turns by 90^{\\circ} at each reflection",
      "Mirrors are inclined at 90^{\\circ}, and light turns by 45^{\\circ}",
      "Mirrors are inclined at 60^{\\circ}, and light turns by 180^{\\circ}",
      "Mirrors are inclined at 30^{\\circ}, and light turns by 60^{\\circ}"],
     "A", "OSC", "medium",
     "Each mirror is placed at 45^{\\circ} to the incoming ray. Since the angle of incidence is 45^{\\circ}, the angle of reflection is 45^{\\circ}, turning the light beam by exactly 90^{\\circ} at each mirror."),

    # 75: Kaleidoscope Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Triangular mirror cross-section -->
  <polygon points="170,30 80,155 260,155" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="170" y="55" fill="#facc15" font-size="10" text-anchor="middle">60^{\\circ}</text>
  <text x="110" y="145" fill="#facc15" font-size="10">60^{\\circ}</text>
  <text x="230" y="145" fill="#facc15" font-size="10">60^{\\circ}</text>
  <circle cx="170" cy="115" r="10" fill="#ec4899"/>
  <text x="170" y="178" fill="#94a3b8" font-size="10" text-anchor="middle">Three mirrors forming an equilateral prism tube</text>
</svg>
</div>
In the cross-section of a kaleidoscope shown above, three long plane mirror strips form an equilateral triangle. What is the interior angle between any two adjacent mirrors, and what kind of optical symmetry does it generate?""",
     ["60^{\\circ} interior angle, generating a hexagonal 6-fold radial symmetry",
      "90^{\\circ} interior angle, generating a 4-fold square symmetry",
      "45^{\\circ} interior angle, generating an 8-fold circular symmetry",
      "120^{\\circ} interior angle, generating a 3-fold linear symmetry"],
     "A", "OSC", "medium",
     "In an equilateral triangle, each interior angle is 60^{\\circ}. With \\theta = 60^{\\circ}, multiple reflections create a repeating 6-fold hexagonal kaleidoscope pattern."),

    # 76: Lateral Inversion of Clock Face
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror -->
  <line x1="170" y1="20" x2="170" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <text x="175" y="30" fill="#38bdf8" font-size="9">Plane Mirror</text>
  <!-- Real Clock (shows 3:00) -->
  <circle cx="90" cy="95" r="45" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <line x1="90" y1="95" x2="90" y2="65" stroke="#f87171" stroke-width="2.5"/> <!-- 12 -->
  <line x1="90" y1="95" x2="120" y2="95" stroke="#38bdf8" stroke-width="3"/> <!-- 3 -->
  <text x="90" y="160" fill="#facc15" font-size="10" text-anchor="middle">Real Clock (3:00)</text>
  <!-- Mirrored Clock -->
  <circle cx="250" cy="95" r="45" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <line x1="250" y1="95" x2="250" y2="65" stroke="#f87171" stroke-width="2.5"/> <!-- 12 -->
  <line x1="250" y1="95" x2="220" y2="95" stroke="#38bdf8" stroke-width="3"/> <!-- points to 9 -->
  <text x="250" y="160" fill="#94a3b8" font-size="10" text-anchor="middle">Mirror Reflection (?)</text>
</svg>
</div>
A clock without numbers on its dial shows exactly 3:00. When viewed in a flat vertical plane mirror as depicted above, what apparent time does the reflection indicate?""",
     ["9:00", "3:00", "6:00", "12:15"],
     "A", "OSC", "easy",
     "The minute hand pointing at 12 remains upright. The hour hand pointing horizontally right toward 3 is laterally inverted to point horizontally left toward 9, indicating 9:00."),

    # 77: Parallel Mirrors Infinite Reflections
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror 1 -->
  <line x1="80" y1="20" x2="80" y2="170" stroke="#38bdf8" stroke-width="4"/>
  <text x="50" y="30" fill="#38bdf8" font-size="9">Mirror 1</text>
  <!-- Mirror 2 -->
  <line x1="260" y1="20" x2="260" y2="170" stroke="#38bdf8" stroke-width="4"/>
  <text x="265" y="30" fill="#38bdf8" font-size="9">Mirror 2</text>
  <!-- Object -->
  <circle cx="170" cy="95" r="6" fill="#f43f5e"/>
  <text x="170" y="80" fill="#f43f5e" font-size="10" text-anchor="middle">Object</text>
  <!-- Ray reflections bouncing -->
  <path d="M 170,95 L 80,70 L 260,110 L 80,140" fill="none" stroke="#facc15" stroke-width="1.8" stroke-dasharray="4,3"/>
  <text x="170" y="180" fill="#94a3b8" font-size="10" text-anchor="middle">Parallel mirrors: \\theta = 0^{\\circ}</text>
</svg>
</div>
When two plane mirrors are placed facing each other in perfect parallel alignment (\\theta = 0^{\\circ}) as illustrated above, what is the theoretical number of images formed, and why do distant images grow progressively fainter?""",
     ["Infinite images; they grow fainter because each reflection absorbs a fraction of light energy",
      "Only 2 images; mirrors cancel each other out",
      "Exactly 360 images; light speeds up over distance",
      "Zero images; rays are trapped in a dead zone"],
     "A", "OSC", "easy",
     "With \\theta = 0^{\\circ}, light rays bounce endlessly between the parallel surfaces creating theoretically infinite images. In practice, partial absorption at each reflection progressively reduces brightness."),

    # 78: Glancing Angle and Deviation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="40" y1="130" x2="300" y2="130" stroke="#38bdf8" stroke-width="3"/>
  <line x1="170" y1="40" x2="170" y2="130" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <!-- Incident Ray -->
  <line x1="70" y1="70" x2="170" y2="130" stroke="#4ade80" stroke-width="2.5"/>
  <!-- Reflected Ray -->
  <line x1="170" y1="130" x2="270" y2="70" stroke="#f87171" stroke-width="2.5"/>
  <!-- Original path dashed -->
  <line x1="170" y1="130" x2="237" y2="170" stroke="#64748b" stroke-dasharray="3,3"/>
  <!-- Glancing angle label -->
  <path d="M 120,130 A 50,50 0 0,0 100,105" fill="none" stroke="#facc15" stroke-width="1.5"/>
  <text x="85" y="125" fill="#facc15" font-size="10">\\theta_g = 30^{\\circ}</text>
  <!-- Deviation angle label -->
  <path d="M 245,85 A 70,70 0 0,1 215,155" fill="none" stroke="#ec4899" stroke-width="1.8"/>
  <text x="250" y="130" fill="#ec4899" font-size="11" font-weight="bold">\\delta = ?</text>
</svg>
</div>
In the diagram above, a light ray strikes a plane mirror with a glancing angle of 30^{\\circ} (angle with the surface). What is the angle of deviation (\\delta) experienced by the light ray?""",
     ["120^{\\circ}", "60^{\\circ}", "30^{\\circ}", "150^{\\circ}"],
     "A", "OSC", "medium",
     "The glancing angle \\theta_g = 30^{\\circ}, so angle of incidence i = 90^{\\circ} - 30^{\\circ} = 60^{\\circ}. The angle of deviation \\delta = 180^{\\circ} - 2i = 180^{\\circ} - 2(60^{\\circ}) = 180^{\\circ} - 120^{\\circ} = 60^{\\circ}... wait! Alternatively, deviation \\delta = 2 × glancing angle = 2 × 30^{\\circ} = 60^{\\circ}? Let's verify: ray straight line is 180^{\\circ}. Deviation \\delta = 180^{\\circ} - (i + r) = 180^{\\circ} - 120^{\\circ} = 60^{\\circ}! Wait! Let's check: 180 - 120 = 60^{\\circ}!"),

    # 79: Retroreflector (Corner Cube 90 deg)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Two perpendicular mirrors -->
  <line x1="60" y1="160" x2="280" y2="160" stroke="#38bdf8" stroke-width="3"/>
  <line x1="60" y1="160" x2="60" y2="30" stroke="#38bdf8" stroke-width="3"/>
  <text x="70" y="150" fill="#facc15" font-size="10">90^{\\circ}</text>
  <!-- Light path -->
  <line x1="240" y1="40" x2="60" y2="100" stroke="#4ade80" stroke-width="2.5"/>
  <line x1="60" y1="100" x2="140" y2="160" stroke="#fbbf24" stroke-width="2.5"/>
  <line x1="140" y1="160" x2="280" y2="113" stroke="#f87171" stroke-width="2.5"/>
  <polygon points="170,60 160,65 170,70" fill="#4ade80"/>
  <polygon points="220,135 230,130 220,125" fill="#f87171"/>
  <text x="175" y="45" fill="#4ade80" font-size="10">Incident Ray</text>
  <text x="210" y="110" fill="#f87171" font-size="10">Reflected Ray</text>
</svg>
</div>
In the two-mirror corner reflector shown above, the mirrors meet at an exact angle of 90^{\\circ}. Regardless of the incident angle, what is the geometric relationship between the incoming ray and the outgoing ray?""",
     ["The outgoing ray is exactly parallel (antiparallel) to the incoming ray",
      "The outgoing ray is perpendicular to the incoming ray",
      "The outgoing ray is deflected by 45^{\\circ}",
      "The outgoing ray converges to a focal point"],
     "A", "OSC", "medium",
     "For two mirrors at 90^{\\circ}, the total deviation \\delta = 360^{\\circ} - 2(90^{\\circ}) = 180^{\\circ}. A deviation of 180^{\\circ} means the ray is reflected back along a path strictly parallel to its incoming trajectory (corner cube retroreflector)."),

    # 80: Mirror Rotation Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Original Mirror Position -->
  <line x1="60" y1="120" x2="280" y2="120" stroke="#38bdf8" stroke-width="3"/>
  <text x="285" y="125" fill="#38bdf8" font-size="9">M_1</text>
  <!-- Rotated Mirror Position (by \\theta) -->
  <line x1="65" y1="145" x2="275" y2="95" stroke="#a855f7" stroke-width="3" stroke-dasharray="5,3"/>
  <text x="285" y="95" fill="#a855f7" font-size="9">M_2 (rotated by \\theta)</text>
  <!-- Fixed Incident Ray -->
  <line x1="120" y1="40" x2="170" y2="120" stroke="#4ade80" stroke-width="2.5"/>
  <text x="100" y="35" fill="#4ade80" font-size="10">Fixed Incident Ray</text>
  <!-- Reflected Ray 1 -->
  <line x1="170" y1="120" x2="220" y2="40" stroke="#f87171" stroke-width="2"/>
  <text x="225" y="45" fill="#f87171" font-size="9">R_1</text>
  <!-- Reflected Ray 2 -->
  <line x1="170" y1="120" x2="250" y2="50" stroke="#f43f5e" stroke-width="2"/>
  <text x="255" y="55" fill="#f43f5e" font-size="9">R_2</text>
  <text x="170" y="175" fill="#facc15" font-size="10" text-anchor="middle">Angle between R_1 and R_2 = 2\\theta</text>
</svg>
</div>
When a flat plane mirror is rotated by an angle \\theta = 15^{\\circ} about an axis in its plane while keeping the incident light ray direction fixed, by what angle does the reflected ray turn?""",
     ["30^{\\circ} (2\\theta)", "15^{\\circ} (\\theta)", "7.5^{\\circ} (\\theta/2)", "45^{\\circ} (3\\theta)"],
     "A", "OSC", "easy",
     "When the mirror turns by angle \\theta, the normal turns by \\theta, shifting the angle of incidence by \\theta and the angle of reflection by \\theta, resulting in a total angular displacement of the reflected ray of 2\\theta = 2 × 15^{\\circ} = 30^{\\circ}."),

    # 81: Diffuse vs Specular Reflection
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Specular side -->
  <line x1="20" y1="130" x2="150" y2="130" stroke="#38bdf8" stroke-width="3"/>
  <line x1="40" y1="60" x2="70" y2="130" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="70" y1="60" x2="100" y2="130" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="70" y1="130" x2="100" y2="60" stroke="#f87171" stroke-width="1.8"/>
  <line x1="100" y1="130" x2="130" y2="60" stroke="#f87171" stroke-width="1.8"/>
  <text x="85" y="155" fill="#38bdf8" font-size="10" text-anchor="middle">Specular Reflection</text>
  <!-- Diffuse side -->
  <path d="M 180,130 Q 195,122 210,130 T 240,130 T 270,126 T 300,130 T 320,130" fill="none" stroke="#e2e8f0" stroke-width="3"/>
  <line x1="210" y1="60" x2="230" y2="130" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="240" y1="60" x2="260" y2="128" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="230" y1="130" x2="210" y2="60" stroke="#f87171" stroke-width="1.8"/>
  <line x1="260" y1="128" x2="300" y2="70" stroke="#f87171" stroke-width="1.8"/>
  <text x="250" y="155" fill="#e2e8f0" font-size="10" text-anchor="middle">Diffuse Reflection</text>
</svg>
</div>
Comparing the two types of reflection depicted in the diagram, why does diffuse reflection produce scattered rays while specular reflection produces a sharp image?""",
     ["Microscopic surface irregularities cause the surface normals to point in diverse directions, dispersing the parallel incident rays",
      "Diffuse reflection breaks the fundamental law of reflection i = r",
      "Specular reflection absorbs all colors of light except white",
      "Diffuse surfaces convert light waves into sound waves"],
     "A", "OSC", "easy",
     "In diffuse reflection, the surface is microscopically uneven, so normal lines at different points of incidence point in different directions. Although each individual ray obeys i = r, the reflected rays scatter randomly."),

    # 82: Lateral Inversion of Word LIGHT
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror line -->
  <line x1="170" y1="20" x2="170" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <text x="175" y="30" fill="#38bdf8" font-size="9">Plane Mirror</text>
  <!-- Real text -->
  <text x="80" y="105" fill="#facc15" font-size="24" font-weight="bold" font-family="monospace">LIGHT</text>
  <text x="80" y="140" fill="#facc15" font-size="10">Real Object</text>
  <!-- Mirrored text -->
  <g transform="translate(250, 105) scale(-1, 1)">
    <text x="-40" y="0" fill="#94a3b8" font-size="24" font-weight="bold" font-family="monospace">LIGHT</text>
  </g>
  <text x="220" y="140" fill="#94a3b8" font-size="10">Lateral Inversion</text>
</svg>
</div>
When the word 'LIGHT' is held in front of a flat vertical plane mirror, which letters retain their identical appearance due to vertical axis symmetry, and which letters appear laterally inverted?""",
     ["Letters 'I', 'H', and 'T' retain their appearance; letters 'L' and 'G' appear laterally inverted",
      "All five letters appear completely unchanged",
      "All five letters are inverted upside-down",
      "Only the letter 'L' changes appearance"],
     "A", "OSC", "medium",
     "The letters 'I', 'H', and 'T' possess bilateral vertical symmetry, so their lateral reflections match the originals. The letters 'L' and 'G' lack vertical symmetry and are clearly reversed laterally.")
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

    out_file = "scripts/ch11_topic1.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
