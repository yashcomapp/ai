# scripts/generate_ch11_topic2.py
# MH-9-SCIT-11-11.2: Spherical Mirrors: Concave vs Convex Mirror Terminology
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-11-11.2"

exam_data = [
    # 1-10: Basic Definitions & Mirror Classification
    ("What is a spherical mirror geometrically defined as?",
     ["A mirror whose reflecting surface is part of a hollow sphere of glass",
      "A flat glass plate with silver paint on one side",
      "A cylindrical prism with two curved faces",
      "A triangular glass pyramid"],
     "A", "OSC", "easy",
     "A spherical mirror is an optical mirror whose curved reflecting surface forms an arc segment of a hollow sphere of glass."),

    ("Which spherical mirror has its reflecting surface curved inwards towards the center of the sphere?",
     ["Concave mirror (converging mirror)",
      "Convex mirror (diverging mirror)",
      "Plane mirror",
      "Parabolic diverging lens"],
     "A", "OSC", "easy",
     "In a concave mirror, the inner hollowed-out surface acts as the reflecting boundary while the outer bulging side is silvered/opaque, converging incident parallel light rays."),

    ("Which spherical mirror has its reflecting surface curved outwards away from the center of the sphere?",
     ["Convex mirror (diverging mirror)",
      "Concave mirror (converging mirror)",
      "Plane mirror",
      "Biconcave cylindrical lens"],
     "A", "OSC", "easy",
     "In a convex mirror, the outer bulging surface reflects light while the inner surface is silvered/opaque, causing incident parallel rays to diverge outwards."),

    ("What is the geometric center of the reflecting surface of a spherical mirror called?",
     ["Pole of the mirror (P)",
      "Center of curvature (C)",
      "Principal focus (F)",
      "Optical aperture"],
     "A", "OSC", "easy",
     "The pole (P) is the exact physical midpoint or geometric center of the curved reflecting surface of a spherical mirror."),

    ("What is the center of the hollow sphere of glass of which the spherical mirror forms a part called?",
     ["Center of curvature (C)",
      "Pole (P)",
      "Principal focus (F)",
      "Optical center (O)"],
     "A", "OSC", "easy",
     "The center of curvature (C) is the geometric center of the original hollow sphere from which the spherical mirror cut was derived."),

    ("What is the radius of the hollow sphere of which the mirror's reflecting surface is a part called?",
     ["Radius of curvature (R)",
      "Focal length (f)",
      "Aperture diameter",
      "Angular thickness"],
     "A", "OSC", "easy",
     "The radius of curvature (R) is the linear distance from the pole (P) to the center of curvature (C), representing the radius of the parent sphere."),

    ("What straight line passing through both the pole (P) and the center of curvature (C) of a spherical mirror is called?",
     ["Principal axis",
      "Normal tangent",
      "Aperture axis",
      "Focal chord"],
     "A", "OSC", "easy",
     "The principal axis is the unique straight line passing through the pole (P) and the center of curvature (C) of the spherical mirror."),

    ("What is the principal focus (F) of a concave mirror?",
     ["The point on the principal axis where rays initially parallel to the principal axis actually converge after reflection",
      "The point behind the mirror where rays appear to disperse",
      "The exact midpoint between the mirror surface and the observer",
      "The top edge of the mirror rim"],
     "A", "OSC", "easy",
     "In a concave mirror, light rays traveling parallel to the principal axis reflect and intersect at a common real point on the axis termed the principal focus (F)."),

    ("Why is the principal focus of a convex mirror termed a 'virtual focus'?",
     ["Because reflected rays do not actually intersect but appear to diverge from a point located behind the mirror",
      "Because the mirror is made of virtual digital glass",
      "Because no light ever reflects from a convex mirror",
      "Because it only exists in complete darkness"],
     "A", "OSC", "easy",
     "Reflected rays from a convex mirror diverge into space; when traced backwards behind the mirror, they appear to emanate from a virtual focal point F behind the surface."),

    ("What is the distance between the pole (P) and the principal focus (F) of a spherical mirror called?",
     ["Focal length (f)",
      "Radius of curvature (R)",
      "Linear aperture",
      "Optical magnification"],
     "A", "OSC", "easy",
     "The focal length (f) is the distance measured along the principal axis between the pole (P) and the principal focus (F)."),

    # 11-20: Relations, Properties & Aperture
    ("What is the mathematical relationship between the focal length (f) and the radius of curvature (R) of a spherical mirror of small aperture?",
     ["f = R / 2 (or R = 2f)",
      "f = 2R",
      "f = R^2",
      "f = 1 / R"],
     "A", "OSC", "easy",
     "For spherical mirrors of small aperture, the principal focus lies exactly halfway between the pole and the center of curvature, giving f = R / 2."),

    ("If a concave mirror has a radius of curvature of 30 cm, what is its focal length?",
     ["15 cm", "30 cm", "60 cm", "10 cm"],
     "A", "OSC", "easy",
     "Using the formula f = R / 2: f = 30 cm / 2 = 15 cm."),

    ("If a convex mirror has a focal length of 20 cm, what is its radius of curvature?",
     ["40 cm", "20 cm", "10 cm", "80 cm"],
     "A", "OSC", "easy",
     "Using R = 2f: R = 2 * 20 cm = 40 cm."),

    ("What does the 'aperture' of a spherical mirror refer to?",
     ["The effective diameter of the circular boundary of the reflecting surface",
      "The distance between the focus and the center of curvature",
      "The thickness of the glass coating",
      "The angle of incidence of the central ray"],
     "A", "OSC", "medium",
     "Aperture is the linear diameter of the circular rim of the reflecting spherical surface that admits light rays into the mirror system."),

    ("Where does the center of curvature of a concave mirror lie relative to its reflecting surface?",
     ["In front of the reflecting surface",
      "Behind the reflecting surface",
      "On the reflecting surface itself",
      "At optical infinity"],
     "A", "OSC", "medium",
     "Because a concave mirror curves inwards towards its center, its center of curvature C lies in front of the reflective face in real space."),

    ("Where does the center of curvature of a convex mirror lie relative to its reflecting surface?",
     ["Behind the reflecting surface",
      "In front of the reflecting surface",
      "At the pole P",
      "Inside the incoming light source"],
     "A", "OSC", "medium",
     "Since a convex mirror bulges outwards away from its center, the center of curvature C lies behind the silvered reflective surface."),

    ("Why is a line joining any point on the spherical mirror surface to the center of curvature (C) always perpendicular to the surface at that point?",
     ["Because the radius of a sphere is always perpendicular to the tangent at any point on its spherical surface",
      "Because light rays only travel in straight lines",
      "Because the mirror has zero focal length",
      "Because the glass is ground with diamond tools"],
     "A", "OSC", "medium",
     "From Euclidean geometry, any line passing through the center of curvature of a sphere acts as a normal (radius) perpendicular to the tangent plane at that surface point."),

    ("What happens to a light ray passing through or directed toward the center of curvature (C) after reflecting from a spherical mirror?",
     ["It retraces its path back along the exact same line (angle of incidence i = 0^{\circ})",
      "It reflects at 90^{\circ} to the principal axis",
      "It converges directly to the pole",
      "It is completely absorbed by the glass"],
     "A", "OSC", "medium",
     "Since the ray passes through C, it strikes the mirror surface along the normal (i = 0^{\circ}). By law of reflection, r = 0^{\circ}, so the ray reflects back along its incident path."),

    ("A concave mirror is also widely known as what type of optical system?",
     ["A converging mirror",
      "A diverging mirror",
      "A plane reflector",
      "A refractive prism"],
     "A", "OSC", "easy",
     "A concave mirror converges incoming parallel rays of light towards a single real focal point F, earning the name converging mirror."),

    ("A convex mirror is also widely known as what type of optical system?",
     ["A diverging mirror",
      "A converging mirror",
      "An achromatic doublet",
      "A planar retroreflector"],
     "A", "OSC", "easy",
     "A convex mirror spreads or diverges incoming parallel rays away from the principal axis, earning the title diverging mirror."),

    # 21-30: OMC, OTF, OAR Questions
    ("Which of the following points and lines lie on the principal axis of a spherical mirror? (Select all that apply)",
     ["The Pole (P)", "The Principal Focus (F)", "The Center of Curvature (C)", "The outer rim of the aperture"],
     "A", "OMC", "easy",
     "The principal axis is the collinear axis containing the Pole P, Focus F, and Center of curvature C."),

    ("Assertion (A): The focus of a concave mirror is a real point in front of the mirror.\nReason (R): Parallel incident rays actually converge and intersect at the focus of a concave mirror.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "The focus of a concave mirror is real because parallel incident rays physically intersect at that point in real space in front of the mirror."),

    ("Assertion (A): The focal length of a spherical mirror depends on the medium in which it is placed (e.g. air vs water).\nReason (R): The focal length of a spherical mirror is given by f = R / 2.",
     ["Assertion (A) is false, but Reason (R) is true",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false"],
     "A", "OAR", "medium",
     "Assertion is false: reflection obeys geometric laws independent of surrounding refractive index; focal length of a mirror depends only on radius of curvature (f = R / 2). Reason is true."),

    ("State whether the following statement is True or False: For a concave mirror, the radius of curvature is twice its focal length (R = 2f).",
     ["True", "False"],
     "A", "OTF", "easy",
     "By definition of spherical geometry for small apertures, the radius of curvature is exactly double the focal length (R = 2f)."),

    ("State whether the following statement is True or False: The pole of a spherical mirror lies outside the physical body of the mirror.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The pole is the geometric center of the reflecting surface itself and therefore lies directly on the mirror."),

    ("State whether the following statement is True or False: The focus of a convex mirror lies behind the reflecting surface.",
     ["True", "False"],
     "A", "OTF", "easy",
     "In a convex mirror, parallel rays diverge and appear to meet behind the mirror at the virtual focus F."),

    ("A spherical mirror has a focal length of 25 cm. What is the distance between its pole and its center of curvature?",
     ["50 cm", "25 cm", "12.5 cm", "100 cm"],
     "A", "OSC", "easy",
     "The distance between pole and center of curvature is the radius of curvature R = 2f = 2 * 25 cm = 50 cm."),

    ("If the radius of curvature of a convex mirror is 36 cm, what is the distance from its pole to its principal focus?",
     ["18 cm", "36 cm", "72 cm", "9 cm"],
     "A", "OSC", "easy",
     "The distance between pole and focus is the focal length f = R / 2 = 36 cm / 2 = 18 cm."),

    ("What geometric shape do spherical mirrors approximate when their aperture is significantly smaller than their radius of curvature?",
     ["A paraboloid (parabolic mirror)", "A flat plane", "A hyperbola", "A torus"],
     "A", "OSC", "medium",
     "For small apertures, a spherical cap closely matches a paraboloid, minimizing spherical aberration and focusing paraxial rays cleanly at f = R / 2."),

    ("What happens to parallel incident rays that strike a spherical mirror far away from the principal axis (marginal rays)?",
     ["They focus closer to the pole than paraxial rays, causing spherical aberration",
      "They reflect back into the light bulb",
      "They change into x-rays",
      "They pass through without reflecting"],
     "A", "OSC", "medium",
     "Marginal rays reflect with larger angles and intersect the principal axis slightly closer to the pole than paraxial rays, a defect known as spherical aberration.")
,
    # 31-40: Additional Exam Questions
    ("What are 'paraxial rays' in the study of spherical mirrors?",
     ["Light rays that travel very close to the principal axis making very small angles with it",
      "Rays that strike the extreme outer perimeter of the mirror",
      "Rays that travel perpendicular to the principal axis",
      "Rays that are completely absorbed by the glass surface"],
     "A", "OSC", "easy",
     "Paraxial rays are incident rays that strike near the pole P and travel nearly parallel to the principal axis, ensuring a sharp focus at f = R / 2."),

    ("What is the 'focal plane' of a spherical mirror?",
     ["A plane perpendicular to the principal axis passing through the principal focus (F)",
      "A plane parallel to the principal axis passing through the pole",
      "The flat plane tangential to the center of curvature",
      "The silvered back face of the mirror"],
     "A", "OSC", "easy",
     "The focal plane is the geometric plane oriented perpendicular to the principal axis passing directly through the principal focus F."),

    ("Where do parallel rays of light coming from a distant star at a slight angle to the principal axis converge in a concave mirror?",
     ["At a point on the focal plane above or below the principal focus",
      "At the center of curvature C",
      "At the pole P",
      "They scatter randomly without converging"],
     "A", "OSC", "medium",
     "Parallel rays inclined at an angle to the principal axis converge at a secondary focus lying in the focal plane."),

    ("In the New Cartesian Sign Convention, which point is chosen as the origin (0, 0)?",
     ["The Pole of the mirror (P)",
      "The Center of curvature (C)",
      "The Principal focus (F)",
      "The center of the object"],
     "A", "OSC", "easy",
     "The pole P of the spherical mirror is taken as the origin of the coordinate axes for all distance measurements."),

    ("Why cannot a convex mirror be used to ignite a piece of dry paper using sunlight?",
     ["Because a convex mirror diverges parallel sunlight rays away from each other rather than concentrating them",
      "Because convex mirrors absorb all thermal energy",
      "Because convex mirrors only reflect ultraviolet radiation",
      "Because the glass in convex mirrors is too thick"],
     "A", "OSC", "easy",
     "Ignition requires intense concentration of solar heat at a real focal point. A convex mirror diverges sunlight, spreading energy over a wider area."),

    ("What distinguishes the Pole of a mirror from the Optical Center of a lens?",
     ["The Pole lies on the reflecting surface of a mirror, whereas the Optical Center lies inside the central body of a lens",
      "Both represent identical mathematical concepts with no physical difference",
      "The Pole is only defined for convex lenses",
      "The Optical Center only exists in flat plane mirrors"],
     "A", "OSC", "medium",
     "The pole P is the geometric center on the surface of a mirror, while the optical center O is a point on the principal axis inside a lens through which rays pass undeviated."),

    ("What is the 'angular aperture' of a spherical mirror?",
     ["The angle subtended by the diameter of the mirror at the center of curvature C",
      "The angle between the principal axis and the normal",
      "The glancing angle of incidence at the rim",
      "The total 360^{\circ} circular angle of the parent sphere"],
     "A", "OSC", "medium",
     "The angular aperture is the plane angle subtended by the circular boundary of the mirror at its center of curvature C."),

    ("Can the real focus of a concave mirror be projected onto a paper screen?",
     ["Yes, because real light rays physically converge at that spatial location",
      "No, because the focus is an imaginary mathematical point",
      "No, because mirrors only produce virtual images",
      "Only when placed in a complete vacuum"],
     "A", "OSC", "easy",
     "Because parallel rays physically converge and intersect at F, placing a white paper screen at the focus catches a real bright point image of the source."),

    ("If a concave mirror has a radius of curvature of 80 cm, what is the distance from the center of curvature C to the principal focus F?",
     ["40 cm", "80 cm", "20 cm", "160 cm"],
     "A", "OSC", "easy",
     "Focal length f = R / 2 = 80 / 2 = 40 cm. Since F is the midpoint between C and P, CF = f = 40 cm."),

    ("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\nReason (R): For small apertures, paraxial rays obey the small-angle approximation tan(theta) \approx sin(theta) \approx theta.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "The geometric proof of R = 2f relies on the paraxial condition where angles are small, allowing the arc and chord approximations.")
]

practice_data = [
    # 31-40: Practical Measurements & Relations
    ("What is the radius of curvature of a plane mirror?",
     ["Infinite (R = infinity)", "Zero (R = 0)", "1 meter", "100 cm"],
     "A", "OSC", "easy",
     "A flat plane can be considered a sphere of infinite radius of curvature; thus R = infinity and f = infinity."),

    ("If the focal length of a concave makeup mirror is 12 cm, what is its radius of curvature?",
     ["24 cm", "12 cm", "6 cm", "48 cm"],
     "A", "OSC", "easy",
     "R = 2f = 2 * 12 cm = 24 cm."),

    ("A spherical mirror has R = 50 cm. What is its focal length?",
     ["25 cm", "50 cm", "100 cm", "12.5 cm"],
     "A", "OSC", "easy",
     "f = R / 2 = 50 cm / 2 = 25 cm."),

    ("Which point on a spherical mirror always reflects an incident light ray along the normal with zero angle of incidence?",
     ["Any ray directed towards or through the center of curvature (C)",
      "Any ray directed towards the focus (F)",
      "Any ray traveling parallel to the principal axis",
      "Any ray striking the outer aperture rim"],
     "A", "OSC", "easy",
     "A ray directed through C strikes along the normal (radius), making i = 0^{\circ} and r = 0^{\circ}."),

    ("Where is the principal focus located on the principal axis for a spherical mirror of radius of curvature R?",
     ["At the midpoint between the pole (P) and the center of curvature (C)",
      "At the center of curvature (C)",
      "At the pole (P)",
      "At double the radius of curvature (2R)"],
     "A", "OSC", "easy",
     "Because f = R / 2, the focus F is situated exactly halfway along the segment connecting P and C."),

    ("State whether the following statement is True or False: A concave mirror can focus parallel rays of sunlight onto a paper sheet to ignite it.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because a concave mirror converges parallel rays to a real focal point, it concentrates radiant thermal energy powerfully enough to ignite paper."),

    ("State whether the following statement is True or False: A convex mirror has a real principal focus.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A convex mirror has a virtual focus located behind its reflecting surface."),

    ("If a light ray passes through the focus of a concave mirror and strikes its surface, how does it reflect?",
     ["It reflects parallel to the principal axis",
      "It retraces its path back through the focus",
      "It passes through the center of curvature",
      "It emerges perpendicular to the mirror surface"],
     "A", "OSC", "easy",
     "By optical reversibility, any ray passing through the focus reflects parallel to the principal axis."),

    ("What is the sign of the focal length of a concave mirror according to the New Cartesian Sign Convention?",
     ["Negative (-)", "Positive (+)", "Zero", "Variable depending on room temperature"],
     "A", "OSC", "medium",
     "In Cartesian sign convention, distances measured against the direction of incident light (to the left of pole) are negative. Since focus F lies in front of a concave mirror, f is negative."),

    ("What is the sign of the focal length of a convex mirror according to the New Cartesian Sign Convention?",
     ["Positive (+)", "Negative (-)", "Zero", "Always infinite"],
     "A", "OSC", "medium",
     "The focus of a convex mirror lies behind the mirror (in the direction of incident light travel), making its focal length positive (+)."),

    # 41-50: More conceptual questions
    ("A ray of light is incident at the pole P of a concave mirror at an angle of 30^{\circ} to the principal axis. At what angle to the principal axis does it reflect?",
     ["30^{\circ} below the principal axis", "60^{\circ} above the principal axis", "90^{\circ} to the principal axis", "0^{\circ} along the principal axis"],
     "A", "OSC", "easy",
     "The principal axis acts as the normal at the pole P. By law of reflection, i = r = 30^{\circ} on the opposite side of the axis."),

    ("Why does dipping a concave mirror into a bucket of water NOT change its focal length?",
     ["Because reflection depends solely on the radius of curvature of the mirror and not on the refractive index of the medium",
      "Because water turns into glass",
      "Because light travels faster in water",
      "Because water neutralizes the center of curvature"],
     "A", "OSC", "medium",
     "Unlike lenses whose focal length depends on the refractive index ratio, mirror focal length is strictly determined by surface geometry: f = R / 2."),

    ("Which of the following describes the aperture of a mirror?",
     ["The diameter of the circular light-reflecting area of the mirror",
      "The distance between focus and pole",
      "The angle between incident and reflected ray",
      "The mass of the glass mirror"],
     "A", "OSC", "easy",
     "Aperture measures the linear diameter across the circular boundary of the mirror surface."),

    ("If the distance between the focus (F) and center of curvature (C) of a concave mirror is 10 cm, what is its focal length?",
     ["10 cm", "20 cm", "5 cm", "15 cm"],
     "A", "OSC", "easy",
     "Since F is the midpoint between P and C, the distance FC equals the distance PF. Thus focal length f = PF = FC = 10 cm."),

    ("In a spherical mirror, if R = 44 cm, what is the distance between the focus and the pole?",
     ["22 cm", "44 cm", "11 cm", "88 cm"],
     "A", "OSC", "easy",
     "Distance between focus and pole is f = R / 2 = 44 cm / 2 = 22 cm."),

    ("Assertion (A): A ray passing through the center of curvature of a concave mirror retraces its path after reflection.\nReason (R): The angle of incidence for such a ray is 0^{\circ}.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "A ray through C travels along the normal to the surface, giving i = 0^{\circ} and r = 0^{\circ}, so it reflects back along its incident path."),

    ("State whether the following statement is True or False: The principal axis of a spherical mirror is normal to the mirror at its pole.",
     ["True", "False"],
     "A", "OTF", "easy",
     "The principal axis passes through C and P, making it exactly normal to the spherical surface at the pole P."),

    ("State whether the following statement is True or False: Convex mirrors can form a real focus for parallel rays of light.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Convex mirrors diverge light and only form a virtual focus behind the mirror."),

    ("What type of spherical mirror is obtained by polishing the outer bulging surface and reflecting from the inner hollow surface?",
     ["Concave mirror", "Convex mirror", "Plane mirror", "Parabolic lens"],
     "A", "OSC", "easy",
     "A concave mirror has its inner curved surface as the reflector."),

    ("What type of spherical mirror is obtained by silvering the inner hollow surface and reflecting from the outer bulging surface?",
     ["Convex mirror", "Concave mirror", "Cylindrical lens", "Prism"],
     "A", "OSC", "easy",
     "A convex mirror has its outer curved surface as the reflector."),

    # 51-60: Synthesis
    ("If an incident ray is parallel to the principal axis of a convex mirror, how does the reflected ray behave?",
     ["It appears to diverge from the virtual principal focus behind the mirror",
      "It converges to a real focus in front of the mirror",
      "It passes through the center of curvature",
      "It turns backwards along the exact same path"],
     "A", "OSC", "easy",
     "In a convex mirror, rays parallel to the principal axis reflect outward such that their backward extensions pass through the virtual focus F."),

    ("What is the radius of curvature of a concave mirror whose focal length is 18 cm?",
     ["36 cm", "18 cm", "9 cm", "72 cm"],
     "A", "OSC", "easy",
     "R = 2f = 2 * 18 cm = 36 cm."),

    ("Where does the center of curvature lie for a concave mirror of focal length 15 cm?",
     ["30 cm in front of the mirror", "30 cm behind the mirror", "15 cm in front of the mirror", "15 cm behind the mirror"],
     "A", "OSC", "medium",
     "C lies in front of the concave mirror at distance R = 2f = 30 cm from the pole."),

    ("Where does the virtual focus lie for a convex mirror of radius of curvature 40 cm?",
     ["20 cm behind the mirror", "20 cm in front of the mirror", "40 cm behind the mirror", "40 cm in front of the mirror"],
     "A", "OSC", "medium",
     "Virtual focus of a convex mirror lies behind the mirror at f = R / 2 = 20 cm from the pole."),

    ("State whether the following statement is True or False: For mirrors with large apertures, all parallel rays converge precisely to a single sharp focus.",
     ["False", "True"],
     "A", "OTF", "medium",
     "Mirrors with large apertures suffer from spherical aberration where marginal rays focus closer to the pole than paraxial rays."),

    ("Which device uses a parabolic rather than a spherical concave mirror to eliminate spherical aberration?",
     ["Astronomical reflecting telescopes and high-intensity searchlights",
      "Ordinary shaving mirrors",
      "Classroom optical benches",
      "Rear-view side mirrors"],
     "A", "OSC", "medium",
     "Parabolic reflectors bring all parallel rays to a single focal point regardless of beam width, eliminating spherical aberration in telescopes and searchlights."),

    ("If a concave mirror has a diameter of 10 cm across its circular rim, what does this 10 cm dimension represent?",
     ["The linear aperture of the mirror", "The radius of curvature", "The focal length", "The principal axis"],
     "A", "OSC", "easy",
     "The diameter of the circular reflecting rim is the linear aperture."),

    ("How many centers of curvature does a single spherical mirror possess?",
     ["Exactly one", "Two", "Infinite", "Zero"],
     "A", "OSC", "easy",
     "A spherical mirror is part of a single sphere and thus has exactly one center of curvature."),

    ("How many focal points does a thin spherical lens have compared to a single spherical mirror?",
     ["A lens has two foci, while a mirror has only one focus",
      "Both have two foci",
      "Both have one focus",
      "A lens has one focus, a mirror has two"],
     "A", "OSC", "easy",
     "A lens has two refractive surfaces and two principal foci, whereas a mirror has only one reflecting surface and one principal focus."),

    ("What is the angle of incidence when a ray of light strikes the pole P of a spherical mirror along the principal axis?",
     ["0^{\circ}", "90^{\circ}", "45^{\circ}", "180^{\circ}"],
     "A", "OSC", "easy",
     "Because the principal axis is normal to the surface at P, a ray along the axis has i = 0^{\circ} and reflects straight back.")
]

mock_data = [
    # 71: Concave Mirror Terminology Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Principal axis -->
  <line x1="20" y1="95" x2="320" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>
  <!-- Concave mirror arc -->
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Hatching behind concave mirror -->
  <g stroke="#64748b" stroke-width="1.5">
    <line x1="280" y1="35" x2="295" y2="30"/>
    <line x1="272" y1="65" x2="287" y2="60"/>
    <line x1="268" y1="95" x2="283" y2="95"/>
    <line x1="272" y1="125" x2="287" y2="130"/>
    <line x1="280" y1="155" x2="295" y2="160"/>
  </g>
  <!-- Pole P -->
  <circle cx="268" cy="95" r="4" fill="#facc15"/>
  <text x="260" y="85" fill="#facc15" font-size="11" font-weight="bold">P</text>
  <!-- Focus F -->
  <circle cx="178" cy="95" r="4" fill="#4ade80"/>
  <text x="174" y="85" fill="#4ade80" font-size="11" font-weight="bold">F</text>
  <!-- Center C -->
  <circle cx="88" cy="95" r="4" fill="#f87171"/>
  <text x="84" y="85" fill="#f87171" font-size="11" font-weight="bold">C</text>
  <!-- Dimension arrows -->
  <line x1="178" y1="115" x2="268" y2="115" stroke="#a78bfa" stroke-width="1.5"/>
  <text x="215" y="130" fill="#a78bfa" font-size="10">f = 12 cm</text>
  <line x1="88" y1="145" x2="268" y2="145" stroke="#ec4899" stroke-width="1.5"/>
  <text x="165" y="160" fill="#ec4899" font-size="10">R = ?</text>
  <text x="50" y="35" fill="#38bdf8" font-size="11" font-weight="bold">Concave Mirror (Converging)</text>
</svg>
</div>
In the diagram of the concave spherical mirror shown above, the focal length between Pole (P) and Focus (F) is measured as 12 cm. What is the radius of curvature R between Pole (P) and Center of curvature (C)?""",
     ["24 cm", "12 cm", "6 cm", "36 cm"],
     "A", "OSC", "easy""",
     "For a spherical mirror, R = 2f = 2 * 12 cm = 24 cm."),

    # 72: Convex Mirror Terminology Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="320" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>
  <!-- Convex mirror arc -->
  <path d="M 100,30 A 130,130 0 0,1 100,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Hatching on inner hollow surface -->
  <g stroke="#64748b" stroke-width="1.5">
    <line x1="100" y1="35" x2="85" y2="30"/>
    <line x1="108" y1="65" x2="93" y2="60"/>
    <line x1="112" y1="95" x2="97" y2="95"/>
    <line x1="108" y1="125" x2="93" y2="130"/>
    <line x1="100" y1="155" x2="85" y2="160"/>
  </g>
  <!-- Pole P -->
  <circle cx="112" cy="95" r="4" fill="#facc15"/>
  <text x="110" y="85" fill="#facc15" font-size="11" font-weight="bold">P</text>
  <!-- Virtual Focus F -->
  <circle cx="185" cy="95" r="4" fill="#4ade80"/>
  <text x="182" y="85" fill="#4ade80" font-size="11" font-weight="bold">F</text>
  <!-- Center of Curvature C -->
  <circle cx="260" cy="95" r="4" fill="#f87171"/>
  <text x="257" y="85" fill="#f87171" font-size="11" font-weight="bold">C</text>
  <text x="160" y="35" fill="#38bdf8" font-size="11" font-weight="bold">Convex Mirror (Diverging)</text>
  <text x="175" y="130" fill="#94a3b8" font-size="10">Focus and Center lie behind mirror</text>
</svg>
</div>
In the convex mirror illustrated above, where do the principal focus (F) and the center of curvature (C) lie relative to the reflecting surface?""",
     ["Both F and C lie behind the reflecting surface""",
     "Both F and C lie in front of the reflecting surface""",
     "F lies in front, while C lies behind""",
     "F lies at the pole, while C is at infinity"],
     "A", "OSC", "easy""",
     "Because a convex mirror bulges outwards towards the observer, the spherical center C and the virtual focus F are located behind the mirror surface."),

    # 73: Concave Mirror Parallel Ray Convergence
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="300" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Focus F -->
  <circle cx="170" cy="95" r="4" fill="#facc15"/>
  <text x="167" y="85" fill="#facc15" font-size="11" font-weight="bold">F</text>
  <!-- Incident Ray 1 -->
  <line x1="30" y1="50" x2="272" y2="50" stroke="#4ade80" stroke-width="2"/>
  <polygon points="140,47 150,50 140,53" fill="#4ade80"/>
  <!-- Reflected Ray 1 to F -->
  <line x1="272" y1="50" x2="100" y2="125" stroke="#f87171" stroke-width="2"/>
  <!-- Incident Ray 2 -->
  <line x1="30" y1="140" x2="272" y2="140" stroke="#4ade80" stroke-width="2"/>
  <polygon points="140,137 150,140 140,143" fill="#4ade80"/>
  <!-- Reflected Ray 2 to F -->
  <line x1="272" y1="140" x2="100" y2="65" stroke="#f87171" stroke-width="2"/>
  <text x="130" y="175" fill="#4ade80" font-size="10">Parallel incident rays converge to focus F</text>
</svg>
</div>
What fundamental property of a concave mirror is visually demonstrated by the ray paths converging at point F in the diagram?""",
     ["It acts as a converging mirror, focusing parallel light rays onto its real focus""",
     "It disperses white light into seven spectral colors""",
     "It inverts left and right without changing ray angles""",
     "It creates virtual magnification only"],
     "A", "OSC", "easy""",
     "Incident rays traveling parallel to the principal axis reflect through the real focus F, demonstrating the converging property of concave mirrors."),

    # 74: Convex Mirror Divergence
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="320" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <path d="M 120,30 A 130,130 0 0,1 120,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Virtual focus F -->
  <circle cx="210" cy="95" r="4" fill="#facc15"/>
  <text x="207" y="85" fill="#facc15" font-size="11" font-weight="bold">F</text>
  <!-- Incident ray 1 -->
  <line x1="20" y1="55" x2="128" y2="55" stroke="#4ade80" stroke-width="2"/>
  <!-- Divergent reflected ray 1 -->
  <line x1="128" y1="55" x2="40" y2="15" stroke="#f87171" stroke-width="2"/>
  <!-- Virtual extension to F -->
  <line x1="128" y1="55" x2="210" y2="95" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Incident ray 2 -->
  <line x1="20" y1="135" x2="128" y2="135" stroke="#4ade80" stroke-width="2"/>
  <!-- Divergent reflected ray 2 -->
  <line x1="128" y1="135" x2="40" y2="175" stroke="#f87171" stroke-width="2"/>
  <line x1="128" y1="135" x2="210" y2="95" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="50" y="180" fill="#f87171" font-size="10">Rays diverge outwards</text>
</svg>
</div>
In the convex mirror ray trace shown above, why do the reflected rays diverge away from the axis, and how is the virtual focus F determined?""",
     ["Rays diverge outward upon reflection; their backward dashed extensions intersect behind the mirror at virtual focus F""",
     "Rays converge to a physical point in front of the mirror""",
     "The mirror absorbs paraxial light and emits heat""",
     "Rays retrace their path to infinity"],
     "A", "OSC", "easy""",
     "A convex mirror diverges parallel incident rays outward into space; extending these divergent reflected rays backward inside the mirror defines the virtual principal focus F."),

    # 75: Normal through Center of Curvature
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="300" y2="95" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Center of Curvature C -->
  <circle cx="80" cy="95" r="4" fill="#facc15"/>
  <text x="75" y="85" fill="#facc15" font-size="11" font-weight="bold">C</text>
  <!-- Normal line from C to mirror surface at point M -->
  <line x1="80" y1="95" x2="268" y2="55" stroke="#fbbf24" stroke-width="2"/>
  <circle cx="268" cy="55" r="3" fill="#fbbf24"/>
  <text x="275" y="55" fill="#fbbf24" font-size="10">Point M</text>
  <!-- Double headed arrow indicating retracing -->
  <polygon points="170,72 180,75 174,80" fill="#fbbf24"/>
  <polygon points="180,78 170,75 176,70" fill="#fbbf24"/>
  <text x="90" y="150" fill="#fbbf24" font-size="10">Ray passing through C strikes mirror along normal (i = 0^{\circ})</text>
</svg>
</div>
Why does a light ray directed through the center of curvature (C) retrace its exact path back after striking point M on the mirror surface?""",
     ["Because any straight line drawn from C to the spherical mirror surface is a radius, making it normal (perpendicular) to the surface (i = 0^{\circ}, r = 0^{\circ})""",
     "Because the center of curvature produces an attractive gravitational pull on photons""",
     "Because C is the point of maximum light absorption""",
     "Because spherical mirrors only reflect light along the radius"],
     "A", "OSC", "medium""",
     "Any line passing through the spherical center of curvature is along a radius of the sphere, meeting the tangent at 90^{\circ}. With normal incidence, i = 0^{\circ}, so r = 0^{\circ} and the ray reflects directly back on itself."),

    # 76: Linear Aperture Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="30" y1="95" x2="290" y2="95" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <path d="M 240,25 A 130,130 0 0,0 240,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Linear Aperture Line XY -->
  <line x1="240" y1="25" x2="240" y2="165" stroke="#ec4899" stroke-width="2" stroke-dasharray="4,3"/>
  <circle cx="240" cy="25" r="4" fill="#ec4899"/>
  <text x="248" y="30" fill="#ec4899" font-size="11" font-weight="bold">X</text>
  <circle cx="240" cy="165" r="4" fill="#ec4899"/>
  <text x="248" y="170" fill="#ec4899" font-size="11" font-weight="bold">Y</text>
  <circle cx="228" cy="95" r="3" fill="#facc15"/>
  <text x="215" y="90" fill="#facc15" font-size="10">P</text>
  <text x="130" y="90" fill="#ec4899" font-size="11" font-weight="bold">Linear Aperture (XY)</text>
</svg>
</div>
What does the dotted vertical line connecting the extreme opposing edges X and Y of the curved mirror represent?""",
     ["The linear aperture of the spherical mirror""",
     "The focal length of the mirror""",
     "The radius of curvature of the mirror""",
     "The principal axis of the mirror"],
     "A", "OSC", "easy""",
     "The straight line distance XY across the circular boundary of the mirror's reflecting surface is defined as the linear aperture."),

    # 77: Ray Incident at Pole Vector Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="300" y2="95" stroke="#94a3b8" stroke-width="2"/>
  <text x="25" y="85" fill="#94a3b8" font-size="10">Principal Axis (Normal)</text>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Pole P -->
  <circle cx="268" cy="95" r="4" fill="#facc15"/>
  <text x="275" y="105" fill="#facc15" font-size="11" font-weight="bold">P</text>
  <!-- Incident ray at P -->
  <line x1="120" y1="35" x2="268" y2="95" stroke="#4ade80" stroke-width="2"/>
  <!-- Reflected ray from P -->
  <line x1="268" y1="95" x2="120" y2="155" stroke="#f87171" stroke-width="2"/>
  <!-- Angle arcs -->
  <path d="M 235,82 A 35,35 0 0,1 245,95" fill="none" stroke="#4ade80" stroke-width="1.5"/>
  <text x="220" y="80" fill="#4ade80" font-size="10">i</text>
  <path d="M 245,95 A 35,35 0 0,1 235,108" fill="none" stroke="#f87171" stroke-width="1.5"/>
  <text x="220" y="115" fill="#f87171" font-size="10">r</text>
  <text x="80" y="180" fill="#cbd5e1" font-size="10">Rays striking Pole P obey law of reflection: i = r</text>
</svg>
</div>
When an incident ray strikes the pole P of a concave mirror at an angle i to the principal axis, how does it reflect?""",
     ["It reflects symmetrically on the other side of the principal axis such that angle of reflection r equals angle of incidence i""",
     "It reflects back along the incident ray""",
     "It emerges parallel to the principal axis""",
     "It turns at 90^{\circ} into the mirror glass"],
     "A", "OSC", "easy""",
     "Because the principal axis is perpendicular to the tangent at pole P, it functions as the normal line. Therefore, the ray reflects obliquely such that r = i on the other side."),

    # 78: Focal Length vs Radius of Curvature Geometry
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="268" cy="95" r="4" fill="#facc15"/>
  <text x="264" y="85" fill="#facc15" font-size="10" font-weight="bold">P</text>
  <circle cx="178" cy="95" r="4" fill="#4ade80"/>
  <text x="174" y="85" fill="#4ade80" font-size="10" font-weight="bold">F</text>
  <circle cx="88" cy="95" r="4" fill="#f87171"/>
  <text x="84" y="85" fill="#f87171" font-size="10" font-weight="bold">C</text>
  <!-- Segment braces -->
  <line x1="88" y1="120" x2="178" y2="120" stroke="#f87171" stroke-width="2"/>
  <text x="125" y="135" fill="#f87171" font-size="10">CF = f</text>
  <line x1="178" y1="120" x2="268" y2="120" stroke="#4ade80" stroke-width="2"/>
  <text x="215" y="135" fill="#4ade80" font-size="10">FP = f</text>
  <text x="90" y="165" fill="#facc15" font-size="10">Focus F is the exact midpoint: CP = 2 * FP (R = 2f)</text>
</svg>
</div>
In the geometry of a spherical mirror with small aperture, which statement accurately describes the location of focus F along the segment CP?""",
     ["F is the exact midpoint between C and P, so CP = 2 * FP (R = 2f)""",
     "F is located one-third of the distance from P to C""",
     "F is located at double the distance of C from P""",
     "F coincides with the center of curvature C"],
     "A", "OSC", "easy""",
     "For small apertures, paraxial ray geometry proves that principal focus F bisects the line segment CP connecting the center of curvature and the pole, yielding R = 2f."),

    # 79: Comparison of Concave vs Convex Reflections
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Concave side -->
  <path d="M 130,40 A 90,90 0 0,0 130,150" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="30" y="30" fill="#38bdf8" font-size="10" font-weight="bold">Concave (Inner reflector)</text>
  <circle cx="60" cy="95" r="3" fill="#facc15"/>
  <text x="55" y="85" fill="#facc15" font-size="9">F (Real)</text>
  <!-- Convex side -->
  <path d="M 220,40 A 90,90 0 0,1 220,150" fill="none" stroke="#ec4899" stroke-width="3"/>
  <text x="190" y="30" fill="#ec4899" font-size="10" font-weight="bold">Convex (Outer reflector)</text>
  <circle cx="280" cy="95" r="3" fill="#4ade80"/>
  <text x="265" y="85" fill="#4ade80" font-size="9">F (Virtual)</text>
</svg>
</div>
Comparing the two spherical mirror configurations shown in the diagram, what is the key difference between their respective principal foci?""",
     ["A concave mirror has a real focus in front of the mirror, while a convex mirror has a virtual focus behind the mirror""",
     "A concave mirror has a virtual focus, while a convex mirror has a real focus""",
     "Both mirrors have real foci located in front of their reflecting surfaces""",
     "Neither mirror has a well-defined focal point"],
     "A", "OSC", "easy""",
     "A concave mirror converges light in real space in front of the mirror (real focus), whereas a convex mirror diverges light so rays only appear to meet behind the mirror (virtual focus)."),

    # 80: Spherical Aberration Illustration
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="300" y2="95" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <path d="M 280,20 A 130,130 0 0,0 280,170" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Paraxial ray & focus -->
  <line x1="40" y1="75" x2="274" y2="75" stroke="#4ade80" stroke-width="1.8"/>
  <line x1="274" y1="75" x2="160" y2="95" stroke="#4ade80" stroke-width="1.8"/>
  <circle cx="160" cy="95" r="3" fill="#4ade80"/>
  <text x="155" y="110" fill="#4ade80" font-size="9">F_paraxial</text>
  <!-- Marginal ray & focus -->
  <line x1="40" y1="30" x2="280" y2="30" stroke="#f87171" stroke-width="1.8"/>
  <line x1="280" y1="30" x2="200" y2="95" stroke="#f87171" stroke-width="1.8"/>
  <circle cx="200" cy="95" r="3" fill="#f87171"/>
  <text x="195" y="110" fill="#f87171" font-size="9">F_marginal</text>
  <text x="70" y="175" fill="#facc15" font-size="10">Spherical Aberration: Wide aperture causes multiple focal points</text>
</svg>
</div>
In a spherical mirror with large aperture as illustrated above, why do marginal rays striking near the edge focus at a different position than paraxial rays near the axis?""",
     ["Because spherical curvature deviates from a true parabola, causing marginal rays to focus closer to the pole (spherical aberration)""",
     "Because marginal rays lose speed in air""",
     "Because the glass has varying density across its rim""",
     "Because the principal axis bends under light pressure"],
     "A", "OSC", "medium""",
     "Spherical aberration arises because the spherical surface reflects outer marginal rays more sharply toward the pole than central paraxial rays, blurring the focal image."),

    # 81: Stainless Steel Spoon Demonstration
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Curved Spoon Bowl -->
  <path d="M 170,30 Q 110,95 170,160 Q 150,95 170,30 Z" fill="#94a3b8"/>
  <text x="60" y="70" fill="#38bdf8" font-size="11" font-weight="bold">Inner curved surface</text>
  <text x="70" y="88" fill="#38bdf8" font-size="9.5">Acts as Concave Mirror</text>
  <text x="190" y="70" fill="#ec4899" font-size="11" font-weight="bold">Outer bulging surface</text>
  <text x="200" y="88" fill="#ec4899" font-size="9.5">Acts as Convex Mirror</text>
  <text x="80" y="180" fill="#facc15" font-size="10">Everyday example: Highly polished stainless steel spoon</text>
</svg>
</div>
When you inspect your reflection in a shiny stainless steel spoon as shown in the diagram, how do the inner hollow surface and the outer bulging surface function optically?""",
     ["The inner hollow surface functions as a concave mirror; the outer bulging surface functions as a convex mirror""",
     "Both surfaces function identically as flat plane mirrors""",
     "The inner surface is convex, and the outer surface is concave""",
     "Both surfaces function as magnifying refracting lenses"],
     "A", "OSC", "easy""",
     "A shiny spoon bowl's hollow inner curve converges light like a concave mirror (producing inverted or enlarged images), while its bulging outer back surface diverges light like a convex mirror (producing erect, diminished images)."),

    # 82: Derivation Geometry for f = R/2
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,40 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Point M on mirror -->
  <circle cx="270" cy="65" r="3" fill="#facc15"/>
  <text x="275" y="65" fill="#facc15" font-size="10">M</text>
  <!-- Parallel incident ray to M -->
  <line x1="40" y1="65" x2="270" y2="65" stroke="#4ade80" stroke-width="2"/>
  <!-- Normal CM -->
  <line x1="90" y1="120" x2="270" y2="65" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Reflected ray MF to axis -->
  <line x1="270" y1="65" x2="180" y2="120" stroke="#f87171" stroke-width="2"/>
  <circle cx="90" cy="120" r="3" fill="#fbbf24"/>
  <text x="85" y="135" fill="#fbbf24" font-size="10">C</text>
  <circle cx="180" cy="120" r="3" fill="#f87171"/>
  <text x="175" y="135" fill="#f87171" font-size="10">F</text>
  <circle cx="270" cy="120" r="3" fill="#38bdf8"/>
  <text x="268" y="135" fill="#38bdf8" font-size="10">P</text>
  <text x="80" y="35" fill="#cbd5e1" font-size="10">Isosceles triangle CFM gives CF = FM \approx FP, so f = R/2</text>
</svg>
</div>
In the geometric derivation of the mirror formula for a concave mirror of small aperture shown above, triangle CFM is an isosceles triangle (angle MCF = angle CMF = i). Why does this prove that f = R / 2?""",
     ["Because for small apertures point M is very close to pole P, making FM \approx FP, which means CF = FP = R / 2""",
     "Because the mirror absorbs paraxial light""",
     "Because triangle CFM has right angles at all vertices""",
     "Because center C moves to infinity"],
     "A", "OSC", "medium""",
     "In triangle CFM, angles MCF and CMF both equal i (alternate interior and reflection angles), so side CF = side FM. For a small aperture, M is near P, so FM \approx FP. Hence CF = FP, proving focus F bisects CP and f = R / 2.")
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

    out_file = "scripts/ch11_topic2.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
