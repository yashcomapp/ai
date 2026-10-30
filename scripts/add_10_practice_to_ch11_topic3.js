const fs = require('fs');

const extraPractice = `    # 61-70: Additional Practice Questions
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
`;

let content = fs.readFileSync('scripts/generate_ch11_topic3.py', 'utf8');
const target = 'mock_data = [';
const insertPos = content.indexOf(target);
if (insertPos !== -1) {
  const lastBracket = content.lastIndexOf(']', insertPos);
  const newContent = content.slice(0, lastBracket) + ',\n' + extraPractice + content.slice(lastBracket);
  fs.writeFileSync('scripts/generate_ch11_topic3.py', newContent, 'utf8');
  console.log('Inserted 10 additional practice questions into ch11_topic3.');
}
