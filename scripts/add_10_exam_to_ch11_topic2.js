const fs = require('fs');

const extraExam = `    # 31-40: Additional Exam Questions
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
      "The total 360° circular angle of the parent sphere"],
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

    ("Assertion (A): For a spherical mirror of small aperture, R = 2f is valid.\nReason (R): For small apertures, paraxial rays obey the small-angle approximation tan(theta) ≈ sin(theta) ≈ theta.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "The geometric proof of R = 2f relies on the paraxial condition where angles are small, allowing the arc and chord approximations.")
`;

let content = fs.readFileSync('scripts/generate_ch11_topic2.py', 'utf8');
const target = 'practice_data = [';
const insertPos = content.indexOf(target);
if (insertPos !== -1) {
  // Find the end of exam_data before practice_data
  const lastBracket = content.lastIndexOf(']', insertPos);
  const newContent = content.slice(0, lastBracket) + ',\n' + extraExam + content.slice(lastBracket);
  fs.writeFileSync('scripts/generate_ch11_topic2.py', newContent, 'utf8');
  console.log('Inserted 10 additional exam questions into ch11_topic2.');
}
