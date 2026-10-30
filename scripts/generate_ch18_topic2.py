# -*- coding: utf-8 -*-
"""
Generate 82 canonical questions for MH-9-SCIT-18-18.2
Topic: Optical Telescopes: Refracting & Reflecting (Newtonian, Cassegrain)
Vault: 40 Exam, 30 Practice, 12 Mock (with dark-theme SVGs)
"""

import json
import os

TOPIC_CODE = "MH-9-SCIT-18-18.2"

def make_q(qcode, topic_code, text, options, correct_key, qtype, difficulty, vault, exam_cat, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic_code,
        "text": text,
        "options": options,
        "correctAnswer": correct_key,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": exam_cat,
        "explanation": explanation,
        "requiresFigure": bool(vault == "mock" and "<svg" in text),
        "chapterNumber": 18,
        "class": "Class 9",
        "board": "MH",
        "subject": "Science and Technology",
        "bloomsTaxonomy": "Application" if difficulty == "hard" else ("Comprehension" if difficulty == "medium" else "Knowledge"),
        "usageCount": 0,
        "used": False
    }

exam_data = [
    # 1: Refracting telescope definition
    ("What optical components are fundamentally employed by a Refracting Telescope to collect and focus visible starlight?",
     ["Lenses that bend (refract) incoming light rays toward a focal point",
      "Curved silver-coated mirrors that reflect light rays",
      "Radio dish antennas and electronic receivers",
      "Rotating magnetic coils and electric grids"],
     "A", "OSC", "easy",
     "A refracting telescope (dioptric system) utilizes transparent glass lenses; incoming parallel light rays pass through a large objective lens, refracting to form a real focal image that is magnified by an eyepiece lens."),

    # 2: Galileo's astronomical telescope (1609)
    ("Who constructed the first astronomical refracting telescope in 1609 and directed it toward the night sky, discovering Jupiter's four largest moons?",
     ["Galileo Galilei", "Isaac Newton", "Johannes Kepler", "Albert Einstein"],
     "A", "OSC", "easy",
     "Galileo Galilei built an improved 30x spyglass in 1609, revolutionizing astronomy by observing mountains on the Moon, the four satellites of Jupiter (Io, Europa, Ganymede, Callisto), sunspots, and Venus phases."),

    # 3: Objective vs Eyepiece lenses in refractor
    ("In a standard astronomical refracting telescope, what are the respective roles and optical specifications of the Objective and Eyepiece lenses?",
     ["Objective has a large aperture and long focal length to gather light; Eyepiece has a small aperture and short focal length to magnify the focal image",
      "Objective has a small aperture to block light; Eyepiece has a giant lens to focus starlight",
      "Both lenses have identical focal lengths and flat surfaces",
      "The objective is a mirror while the eyepiece is a laser"],
     "A", "OSC", "easy",
     "The objective lens requires a wide clear aperture to gather maximum photon flux from faint stars and a long focal length (f_o) to produce a large primary image; the eyepiece lens has a short focal length (f_e) to provide high angular magnification."),

    # 4: Angular magnification formula M = fo / fe
    ("Which mathematical formula expresses the angular magnification (M) of an astronomical refracting telescope in normal adjustment?",
     ["M = f_o / f_e", "M = f_e / f_o", "M = f_o * f_e", "M = f_o + f_e"],
     "A", "OSC", "easy",
     "Telescope angular magnification in normal adjustment is given by the ratio of the objective focal length to the eyepiece focal length (M = f_o / f_e). A longer objective paired with a shorter eyepiece yields greater magnification."),

    # 5: Chromatic aberration defect
    ("What optical defect inherent to glass lenses causes colored rainbow halos to blur star images in refracting telescopes?",
     ["Chromatic Aberration", "Doppler Shift", "Total Internal Reflection", "Polarization"],
     "A", "OSC", "easy",
     "Chromatic aberration arises because glass exhibits optical dispersion: shorter blue/violet wavelengths refract more sharply than longer red wavelengths, focusing at different points along the optical axis and creating colored fringes."),

    # 6: Newton's invention of reflecting telescope (1668)
    ("Why did Sir Isaac Newton design and construct the first Reflecting Telescope in 1668?",
     ["To completely eliminate chromatic aberration by substituting curved mirrors for glass lenses",
      "Because glass was completely unavailable in England",
      "To make the telescope heavier and more expensive",
      "To prevent starlight from reaching the astronomer's eye"],
     "A", "OSC", "medium",
     "Newton recognized that reflection is completely achromatic: the law of reflection (theta_i = theta_r) applies equally to all wavelengths of light without dispersion, eliminating colored chromatic halos entirely."),

    # 7: Law of reflection wavelength independence
    ("Why do curved optical mirrors suffer zero chromatic aberration across all wavelengths of visible light?",
     ["The angle of reflection equals the angle of incidence regardless of light frequency or wavelength",
      "Mirrors absorb all blue light completely",
      "Mirrors convert all colors of light into yellow light",
      "Mirrors only reflect light in total darkness"],
     "A", "OSC", "easy",
     "Reflection is an angle-conserving boundary phenomenon occurring at a reflective metal surface; unlike refraction inside a dense medium, no wavelength-dependent velocity changes occur, ensuring all colors converge at the exact same focal point."),

    # 8: Newtonian telescope design components
    ("In a Newtonian reflecting telescope, what optical elements redirect the converging light beam out to the side of the telescope tube?",
     ["A primary concave mirror paired with a small flat plane mirror tilted at 45 degrees",
      "Two convex glass lenses glued together",
      "A rotating triangular prism and a water basin",
      "A giant concave lens at the front"],
     "A", "OSC", "medium",
     "In Newton's arrangement, incoming starlight reflects off a primary concave mirror toward a focal point; before reaching focus, a small plane secondary mirror tilted at 45 degrees reflects the cone of light out through a hole in the tube side to the eyepiece."),

    # 9: Cassegrain telescope design components
    ("In a Cassegrain reflecting telescope, how is the secondary reflection routed to the observer's eyepiece?",
     ["A convex secondary mirror reflects starlight straight back through a central hole drilled in the primary concave mirror to an eyepiece behind it",
      "Light is directed out of the front of the telescope tube",
      "Light is bounced through five separate glass prisms",
      "Light is focused inside the astronomer's pocket"],
     "A", "OSC", "medium",
     "Designed by Laurent Cassegrain (1672), incoming starlight hits a primary concave mirror, reflects toward a small convex secondary mirror, which folds the optical beam back through a central aperture in the primary mirror to an eyepiece located conveniently behind the telescope."),

    # 10: Compact tube length of Cassegrain
    ("What practical mechanical advantage does the folded optical path of a Cassegrain telescope offer over a refracting telescope of equal focal length?",
     ["It provides a very long effective focal length inside a short, compact, easily maneuverable telescope tube",
      "It makes the telescope ten times longer than a football field",
      "It eliminates the need for an eyepiece lens",
      "It allows the telescope to operate without any starlight"],
     "A", "OSC", "easy",
     "By folding the optical cone back and forth between primary and secondary mirrors, a Cassegrain telescope achieves an immense effective focal length (e.g. 5 to 10 meters) inside a compact physical tube only 1 to 2 meters long, minimizing observatory dome size."),

    # 11: Support advantage of mirrors vs lenses
    ("Why can telescope mirrors be built with massive diameters (8 to 10 meters), whereas refracting glass lenses cannot exceed approximately 1 meter in diameter?",
     ["Mirrors can be supported securely across their entire rear surface, whereas transparent lenses can only be supported around their thin perimeter rims and sag under gravity",
      "Lenses turn into water when they exceed 1 meter",
      "Mirrors are much lighter than feather down",
      "Glass cannot be cut into circular shapes larger than 1 meter"],
     "A", "OSC", "medium",
     "Transparent lenses must allow light to pass through their full body, restricting structural mounting solely to the rim; massive lenses sag under gravity, warping optical figures. In contrast, opaque mirrors reflect off their front surface and can be supported rigidly across their entire back."),

    # 12: Optical absorption and bubbles in large lenses
    ("What manufacturing defect severely degrades optical performance when attempting to cast giant glass lenses thicker than 10 centimeters?",
     ["Internal air bubbles, thermal strain birefringence, and absorption of light within the thick glass volume",
      "The glass spontaneously catches fire in sunlight",
      "The lens starts emitting toxic radioactive gases",
      "The glass turns opaque black overnight"],
     "A", "OSC", "medium",
     "Casting enormous homogeneous optical blanks without micro-bubbles, striae, or cooling stress is nearly impossible; furthermore, light traveling through several inches of dense glass suffers significant absorption, especially in blue and UV wavelengths."),

    # 13: Yerkes Observatory 40-inch refractor limit
    ("The world's largest successful astronomical refracting telescope, built in 1897 at Yerkes Observatory (Wisconsin, USA), has an objective lens diameter of:",
     ["40 inches (approx 1.02 meters)", "10 meters", "200 inches (5 meters)", "6 inches (15 cm)"],
     "A", "OSC", "easy",
     "The 40-inch (1.02 m) refractor at Yerkes Observatory represents the absolute historical engineering limit for refracting lenses; larger lenses suffered unacceptable gravitational sag and chromatic aberrations."),

    # 14: Spherical aberration in curved mirrors
    ("What optical defect occurs when a spherical concave mirror reflects rays, causing peripheral edge rays to focus closer to the mirror than central paraxial rays?",
     ["Spherical Aberration", "Chromatic Aberration", "Astigmatism", "Diffraction Spikes"],
     "A", "OSC", "medium",
     "A simple spherical mirror fails to bring all parallel rays to a single point: marginal rays reflect more steeply than central rays, creating a blurry blur circle. This spherical aberration is eliminated by figuring the mirror into a true parabola."),

    # 15: Parabolic mirror eliminates spherical aberration
    ("Which geometrical surface shape must an astronomical primary mirror possess to focus ALL parallel incoming starlight rays to a single, aberration-free focal point?",
     ["Paraboloid (Parabolic concave surface)", "Flat plane surface", "Hyperbolic convex surface", "Cylindrical surface"],
     "A", "OSC", "medium",
     "A paraboloid is mathematically unique: all rays entering parallel to its principal axis reflect to converge at precisely the exact same geometric focus regardless of their distance from the center, eliminating spherical aberration."),

    # 16: Modern segmented mirror technology
    ("How do modern mega-telescopes (like Keck, Gran Telescopio Canarias, and Thirty Meter Telescope) construct primary mirrors exceeding 10 meters in diameter?",
     ["By tiling dozens of smaller, computer-aligned hexagonal mirror segments into a single unified parabolic reflective surface",
      "By casting a single giant solid glass block weighing 1,000 tons",
      "By using liquid mercury pools that spin in outer space",
      "By gluing thousands of flat bathroom mirrors together"],
     "A", "OSC", "medium",
     "Pioneered by Jerry Nelson on the 10-meter Keck telescopes, segmented mirror design joins 36 or more thin hexagonal mirror blanks controlled by nanometer-precision computerized actuators to mimic a monolithic parabolic aperture."),

    # 17: Light-gathering power dependence on aperture
    ("How does the light-gathering power of an astronomical telescope scale with the diameter (D) of its primary objective mirror or lens?",
     ["Directly proportional to the SQUARE of the diameter (Area proportional to D^2)",
      "Directly proportional to the diameter (D)",
      "Inversely proportional to the diameter (1/D)",
      "Independent of diameter"],
     "A", "OSC", "medium",
     "Light-gathering power depends directly on the photon-collecting surface area (Area = pi * (D/2)^2). Doubling the aperture diameter multiplies its photon-collecting capacity by four (2^2 = 4), revealing far fainter stars."),

    # 18: Resolving power of telescope
    ("What does the 'Resolving Power' of an astronomical telescope define?",
     ["Its ability to distinguish two closely spaced celestial point sources as distinct, separate objects",
      "The total electrical power consumed by the telescope motor",
      "How heavy a camera the telescope can physically lift",
      "The brightness of the optical laser used to clean the mirror"],
     "A", "OSC", "easy",
     "Resolving power measures angular detail resolution: according to Rayleigh's criterion (theta = 1.22 * lambda / D), a larger aperture diameter (D) yields a smaller diffraction limit theta, enabling the telescope to separate tightly orbiting binary stars."),

    # 19: Eyepiece swap and magnification control
    ("How does an astronomer conveniently change the magnification of an optical telescope without replacing the heavy primary mirror?",
     ["By swapping the eyepiece lens with another eyepiece of a different focal length (fe)",
      "By moving the telescope closer to the star",
      "By painting the telescope tube with reflective paint",
      "By heating the primary mirror with a hair dryer"],
     "A", "OSC", "easy",
     "Because magnification M = f_o / f_e, where the objective focal length f_o is fixed by the telescope tube geometry, the astronomer simply replaces the modular eyepiece: an eyepiece with a shorter focal length delivers higher magnification."),

    # 20: Inverted image in Keplerian telescope
    ("Why does an astronomical refracting telescope (Keplerian design) produce an upside-down (inverted) image, and why is this acceptable in astronomy?",
     ["Two convex lenses produce an inverted real image, which is completely acceptable because celestial objects in space have no terrestrial 'up' or 'down'",
      "Because stars are actually upside down in reality",
      "To save electrical power inside the observatory",
      "Because Earth's gravity inverts starlight before it enters the telescope"],
     "A", "OSC", "easy",
     "A simple two-element astronomical refractor inverts images; while confusing for terrestrial terrestrial landscapes, orientation is irrelevant for symmetrical spherical stars, planets, and nebulae in outer space, avoiding extra erecting lenses that would absorb starlight."),

    # 21: Galilean telescope optical arrangement
    ("How did Galileo Galilei's original 1609 telescope arrangement differ optically from Johannes Kepler's 1611 telescope design?",
     ["Galileo used a convex objective lens paired with a CONCAVE eyepiece lens to produce an upright image, whereas Kepler used two convex lenses",
      "Galileo used mirrors while Kepler used water lenses",
      "Galileo used an electric camera while Kepler used photographic film",
      "Galileo's telescope was 50 meters long while Kepler's was 1 cm"],
     "A", "OSC", "medium",
     "Galileo's refractor combined a positive (convex) objective with a negative (diverging concave) eyepiece placed before the focal point, producing an erect image with a narrow field of view; Kepler substituted a positive convex eyepiece, widening the field of view with an inverted image."),

    # 22: Achromatic doublet lens invention
    ("How did John Dollond significantly reduce chromatic aberration in refracting telescopes in 1758?",
     ["By cementing an 'Achromatic Doublet' combining a crown glass convex lens with a flint glass concave lens having opposing dispersions",
      "By dipping lenses in liquid red dye",
      "By making lenses out of solid silver metal",
      "By viewing stars strictly through green sunglasses"],
     "A", "OSC", "medium",
     "An achromatic doublet unites a low-dispersion crown glass convex lens with a high-dispersion flint glass concave lens; the diverging flint lens cancels the chromatic spread of the crown lens while preserving net positive converging power for red and blue light."),

    # 23: Thin aluminium coating on telescope mirrors
    ("What reflective material is vacuum-evaporated as a microscopic layer onto the polished glass surface of modern astronomical telescope mirrors?",
     ["A microscopic reflective coating of pure Aluminium (or Silver) with a protective silicon dioxide overcoat",
      "A thick layer of white lead paint",
      "Solid diamond sheets glued with epoxy",
      "Liquid mercury brushed with a paintbrush"],
     "A", "OSC", "easy",
     "Telescope mirrors are made of low-thermal-expansion glass-ceramic (like Zerodur or Pyrex) that serves strictly as a rigid substrate; the actual optical reflection occurs off a 100-nanometer thin film of evaporated pure aluminum deposited on the front surface."),

    # 24: Front-surface (first-surface) mirror principle
    ("Why do astronomical telescopes strictly use 'Front-surface' (first-surface) mirrors rather than household second-surface back-silvered mirrors?",
     ["To prevent starlight from passing through glass where it would suffer reflection loss, refraction, and ghost double-images",
      "Because front surfaces are cheaper to clean with soap",
      "Because back surfaces are too cold to reflect light",
      "To allow the mirror to be used as a solar panel"],
     "A", "OSC", "medium",
     "Household mirrors have silvering on the rear of a glass plate, generating a faint ghost reflection from the front glass surface and refractive distortion; astronomical mirrors reflect light directly off the front metallic surface, avoiding glass transmission completely."),

    # 25: Focal ratio (f-number) meaning
    ("What does the 'Focal Ratio' (f-number = f / D) of an optical telescope indicate regarding its photographic performance?",
     ["A lower f-number (e.g. f/3) indicates a 'fast' telescope delivering bright, wide-field images of faint nebulae with shorter camera exposure times",
      "A higher f-number makes the telescope travel faster across the sky",
      "Focal ratio measures the temperature of the telescope tube",
      "Focal ratio indicates how many lenses are glued together"],
     "A", "OSC", "medium",
     "The focal ratio (f/D) measures optical speed: just like in camera lenses, smaller f-ratios concentrate starlight onto smaller image areas, reducing required CCD exposure times for diffuse deep-sky targets like galaxies and nebulae."),

    # 26: Adaptive optics (AO) technology
    ("How does modern 'Adaptive Optics' (AO) technology allow large ground-based optical telescopes to overcome atmospheric air turbulence blurring?",
     ["Deformable thin mirrors continuously flex their surface hundreds of times per second driven by computer actuators to cancel out incoming atmospheric wavefront distortions",
      "By blasting high-powered air cannons into the sky to freeze the wind",
      "By sucking all the air out of the sky with vacuum pumps",
      "By moving the entire mountain up and down synchronously"],
     "A", "OSC", "hard",
     "Adaptive optics measures atmospheric wavefront distortion using a sodium laser guide star high in the mesosphere; a real-time computer calculates phase corrections and commands piezo-actuators to deform a thin secondary mirror up to 1,000 times per second, restoring razor-sharp diffraction-limited images."),

    # 27: Liquid mirror telescope (ILMT at Devasthal, India)
    ("India's International Liquid Mirror Telescope (ILMT) at Devasthal (Nainital) uses which rotating liquid as its primary reflecting surface?",
     ["A rotating 4-meter pool of liquid Mercury (Hg) that naturally assumes a perfect parabolic surface under gravity and centripetal acceleration",
      "Liquid liquid nitrogen",
      "Liquid cooking sunflower oil",
      "Pure distilled mineral water with blue dye"],
     "A", "OSC", "hard",
     "When a container of liquid rotates at a constant angular velocity, the equilibrium between gravity and centrifugal inertia forces the liquid surface into an optically flawless paraboloid; ILMT uses a rotating 4-meter pool of liquid mercury at Devasthal at a fraction of the cost of glass mirrors."),

    # 28: Vena Cava in Cassegrain mirror
    ("In a Cassegrain telescope, what happens to the starlight that strikes the small central area occupied by the secondary mirror?",
     ["It represents a small central obstruction (typically 10-20% of area) causing a minor shadow that slightly reduces contrast without creating a dark spot in the final focused image",
      "It completely blocks all starlight from forming any image whatsoever",
      "It makes the image appear with a giant black hole in the exact center",
      "It causes the secondary mirror to explode under light pressure"],
     "A", "OSC", "medium",
     "Because light from every point source is distributed across the entire unobstructed aperture, central obstructions (the secondary mirror and its spider support vanes) merely produce minor diffraction rings and slightly diminish contrast, without creating a hole in the image."),

    # 29: Spider vanes and diffraction spikes
    ("Why do bright stars photographed by Newtonian and Cassegrain reflecting telescopes display characteristic cross-shaped 'diffraction spikes'?",
     ["Starlight diffracts around the thin metal spider vanes that hold the secondary mirror suspended in the telescope tube",
      "Stars naturally shoot four laser beams into space",
      "The camera sensor has four cracked corners",
      "Diffraction spikes are optical artifacts added by Photoshop software"],
     "A", "OSC", "medium",
     "Light diffracts perpendicular to straight edges: the four thin metallic support struts (spider vanes) holding the secondary mirror scatter light perpendicularly, generating the iconic cross-shaped diffraction spikes visible around bright stellar points in astronomical photographs."),

    # 30: Ritchey-Chretien advanced Cassegrain
    ("What specialized optical surface design is utilized by the Hubble Space Telescope and many professional observatories (the Ritchey-Chretien variant of Cassegrain)?",
     ["Hyperbolic primary and Hyperbolic secondary mirrors, which completely eliminate both spherical aberration and off-axis coma across a wide field of view",
      "Flat window glass primary and spherical secondary",
      "Two plastic lenses and one rubber mirror",
      "Parabolic primary and flat secondary mirror"],
     "A", "OSC", "hard",
     "The Ritchey-Chretien Cassegrain system employs two hyperbolic mirrors; this two-degree-of-freedom optical design eliminates both spherical aberration and third-order off-axis coma, yielding pristine pinpoint star images across an extraordinarily wide photographic focal plane."),

    # 31: Primary mirror thermal equilibrium
    ("Why must astronomical telescope mirrors be cooled to match the ambient nighttime air temperature before observations commence?",
     ["If the mirror is warmer than the surrounding air, convective heat plumes rise off the mirror face, creating internal optical turbulence that severely blurs star images",
      "Warm mirrors attract nocturnal moths and bats",
      "Warm mirrors reflect infrared light backwards into the stars",
      "Cold mirrors weigh 50% less than warm mirrors"],
     "A", "OSC", "medium",
     "A mirror that is warmer than surrounding ambient air sheds heat via convective boundary-layer currents directly across its optical surface; this 'mirror seeing' turbulence severely degrades angular resolution unless high-velocity fans flush the mirror to thermal equilibrium."),

    # 32: Catadioptric telescopes (Schmidt-Cassegrain)
    ("What is a 'Catadioptric' telescope (such as the widely used Schmidt-Cassegrain or Maksutov-Cassegrain)?",
     ["An optical system combining both curved mirrors (reflection) and thin correcting glass lenses (refraction) to produce compact, wide-field, aberration-free imaging",
      "A telescope made strictly out of wooden parts",
      "A radio antenna connected to an optical camera",
      "A telescope that operates strictly underwater"],
     "A", "OSC", "easy",
     "Catadioptric telescopes harmonize reflection and refraction: a spherical primary mirror provides easy manufacturing, while a thin aspheric glass corrector plate (Schmidt corrector) at the tube entrance completely neutralizes the mirror's spherical aberration."),

    # 33: Telescope mount types (Equatorial vs Alt-Azimuth)
    ("Why do astronomical telescopes require precision motorized tracking mounts?",
     ["To continuously counteract the Earth's west-to-east axial rotation, keeping celestial objects centered in the optical field during long exposures",
      "To prevent the telescope from falling over under wind pressure",
      "To spin the telescope around to keep the mirrors cool",
      "To search for shooting stars automatically across the entire sky"],
     "A", "OSC", "easy",
     "Because the Earth rotates once every 24 hours from west to east, stars appear to move across the night sky at 15 degrees per hour; motorized equatorial or altitude-azimuth mounts continuously track celestial coordinates to freeze star images on camera sensors."),

    # 34: Light-gathering power comparison calculation
    ("A 10-meter giant reflecting telescope has an aperture diameter 100 times larger than a 10-centimeter amateur telescope. How many times more starlight does the giant telescope gather in one second?",
     ["10,000 times more light (100^2)", "100 times more light", "1,000 times more light", "200 times more light"],
     "A", "OSC", "easy",
     "Light-gathering power scales with the square of the diameter ratio: (D_large / D_small)^2 = (10 m / 0.1 m)^2 = (100)^2 = 10,000 times more photon collecting capability."),

    # 35: Eyepiece field of view
    ("In telescope optics, what is the 'Apparent Field of View' (AFOV) of an eyepiece?",
     ["The angular diameter of the circular light field visible to the observer's eye when looking through the eyepiece alone",
      "The total weight of the glass inside the eyepiece",
      "The physical length of the eyepiece metal barrel",
      "The distance between the telescope and the observer's foot"],
     "A", "OSC", "easy",
     "Apparent field of view (AFOV) is the angular span perceived by the human eye looking into the eyepiece (typically 50° for Plossl eyepieces and 82° to 100° for ultra-wide eyepieces); dividing AFOV by magnification yields true sky field of view."),

    # 36: Diffraction limit Rayleigh criterion
    ("According to Lord Rayleigh's diffraction criterion, the minimum angular separation (theta) resolvable by a circular telescope aperture of diameter D is given by:",
     ["theta = 1.22 * lambda / D", "theta = D / lambda", "theta = 1.22 * D * lambda", "theta = lambda^2 / D"],
     "A", "OSC", "medium",
     "Diffraction through a circular entrance aperture of diameter D spreads light into a central Airy disk surrounded by faint concentric rings; two point sources are barely resolved when the central maximum of one falls upon the first minimum of the other (theta = 1.22 * lambda / D radians)."),

    # 37: Zerodur and Pyrex glass ceramics
    ("Why are astronomical primary mirrors manufactured from specialized glass-ceramics like Zerodur or fused silica rather than ordinary window glass?",
     ["They have near-zero coefficients of thermal expansion, preventing the mirror surface from warping when ambient nighttime temperatures drop",
      "They are transparent to X-rays and gamma rays",
      "They are lighter than air and float inside the telescope",
      "They are unbreakable even when struck by hammers"],
     "A", "OSC", "medium",
     "Ordinary glass expands and contracts significantly with temperature swings, distorting optical tolerances; Zerodur glass-ceramic features a thermal expansion coefficient near zero (alpha approx 0 +/- 0.05 x 10^-6 /K), maintaining nanometer-level parabolic curvature under changing ambient temperatures."),

    # 38: Barlow lens function
    ("What optical function is performed by inserting an auxiliary 'Barlow Lens' between the telescope focuser and the eyepiece?",
     ["It diverges the converging light cone, effectively doubling or tripling the telescope's focal length and magnification",
      "It reduces magnification to make the image wider",
      "It turns the telescope into a microscope for examining dust",
      "It reverses the color of the stars from yellow to blue"],
     "A", "OSC", "medium",
     "A Barlow lens is an achromatic diverging lens system placed just before the focal point; it diverges the focal cone, multiplying effective focal length by a factor of 2x or 3x, thereby doubling or tripling magnification without changing eyepieces."),

    # 39: Giant Metrewave Radio Telescope contrast
    ("How does the optical surface smoothness tolerance required for a visible-light telescope mirror compare to the wire-mesh surface of a radio telescope dish?",
     ["Visible light mirrors require surface precision within a fraction of a light wavelength (~50 nanometers), whereas radio dishes only require accuracy within millimeters",
      "Radio dishes require a billion times smoother surfaces than optical mirrors",
      "Both require identical precision down to atomic dimensions",
      "Optical mirrors can have huge holes while radio dishes cannot"],
     "A", "OSC", "hard",
     "A reflector must maintain surface deviations less than lambda/16 to form coherent reflections: for visible light (lambda ~ 500 nm), this demands nanometer polishing; for 21 cm radio waves, a coarse wire mesh with millimeter tolerances acts as a solid reflective mirror."),

    # 40: Summary contrast between Refractors and Reflectors
    ("In modern research astronomy, why have reflecting telescopes completely replaced refracting telescopes for all major observatories worldwide?",
     ["Reflectors eliminate chromatic aberration, can be supported from behind across giant diameters (up to 30 m), and cost far less per unit aperture area than massive glass lenses",
      "Refractors were banned by international astronomy treaties",
      "Reflecting telescopes can only see nearby planets",
      "Lenses are no longer manufactured anywhere in the world"],
     "A", "OSC", "easy",
     "Reflecting telescopes possess decisive physical advantages: complete absence of chromatic aberration, structural support across the entire mirror back, feasibility of segmented mirrors exceeding 10 meters, and compact folded optical paths.")
]

practice_data = [
    # 41: Magnification calculation M = fo / fe
    ("An astronomical refracting telescope has an objective lens with a focal length of 120 cm (1200 mm) and an eyepiece lens with a focal length of 10 mm. What is the magnifying power of this telescope?",
     ["120x", "12x", "1200x", "0.08x"],
     "A", "OSC", "easy",
     "Magnification M = f_o / f_e = 1200 mm / 10 mm = 120x. Celestial objects appear 120 times larger in angular diameter."),

    # 42: Tube length of Keplerian telescope
    ("In a simple Keplerian astronomical refracting telescope in normal adjustment (with the image formed at infinity), what is the total physical length (L) of the telescope tube?",
     ["L = f_o + f_e", "L = f_o - f_e", "L = f_o * f_e", "L = f_o / f_e"],
     "A", "OSC", "easy",
     "In normal adjustment, the real focal plane of the objective coincides with the focal point of the eyepiece; therefore, the physical separation between objective and eyepiece lenses equals the sum of their focal lengths (L = f_o + f_e)."),

    # 43: Tube length calculation
    ("A refracting telescope has an objective of focal length 150 cm and an eyepiece of focal length 5 cm. What is the distance between the two lenses in normal adjustment?",
     ["155 cm", "145 cm", "750 cm", "30 cm"],
     "A", "OSC", "easy",
     "Distance between lenses L = f_o + f_e = 150 cm + 5 cm = 155 cm (1.55 meters)."),

    # 44: Eyepiece swap to increase magnification
    ("An astronomer observing Saturn with a telescope having an objective focal length of 1000 mm switches from a 25 mm eyepiece to a 5 mm eyepiece. How does the magnification change?",
     ["Magnification increases from 40x to 200x (a 5-fold increase)",
      "Magnification decreases from 200x to 40x",
      "Magnification remains unchanged at 40x",
      "Magnification drops to zero"],
     "A", "OSC", "easy",
     "Initial magnification M_1 = 1000 / 25 = 40x. With the 5 mm eyepiece, M_2 = 1000 / 5 = 200x. Smaller focal length eyepieces deliver proportionally higher magnification."),

    # 45: Light gathering comparison: 20 cm vs 5 cm
    ("How does the light-gathering power of an 20 cm amateur telescope compare to that of a small 5 cm spotting scope?",
     ["The 20 cm telescope gathers 16 times more light than the 5 cm scope",
      "The 20 cm telescope gathers 4 times more light",
      "The 20 cm telescope gathers 2 times more light",
      "The 20 cm telescope gathers 20 times more light"],
     "A", "OSC", "easy",
     "Light gathering ratio = (D_1 / D_2)^2 = (20 cm / 5 cm)^2 = (4)^2 = 16 times more photons collected per second."),

    # 46: Newtonian 45-degree flat mirror function
    ("Why is the flat secondary mirror in a Newtonian telescope positioned precisely at a 45-degree angle to the primary optical axis?",
     ["To deflect the converging cone of starlight at a right angle (90 degrees) through the side of the telescope tube into the eyepiece",
      "To reflect light back out into space",
      "To split starlight into seven rainbow colors",
      "To prevent starlight from being absorbed by the primary mirror"],
     "A", "OSC", "easy",
     "A flat mirror tilted at 45 degrees reflects incoming axial rays by 2 * 45° = 90°, cleanly diverting the focal plane out of the tube barrel where an observer or camera can access it without blocking incoming starlight."),

    # 47: Cassegrain convex secondary mirror divergence
    ("What optical effect does the convex secondary mirror have on the cone of starlight reflected from the primary concave mirror in a Cassegrain telescope?",
     ["It slightly decreases the convergence angle of the rays, effectively increasing the focal length while folding the path back through the primary central hole",
      "It scatters starlight in random directions inside the tube",
      "It turns the starlight into parallel radio waves",
      "It absorbs all starlight to keep the telescope cool"],
     "A", "OSC", "medium",
     "A convex secondary mirror has negative optical power: it slows the convergence of the incoming cone of rays, multiplying effective focal length (by a magnification factor of 3x to 5x) before passing through the primary mirror hole."),

    # 48: Chromatic aberration absence in mirrors demonstration
    ("A beam of mixed red light (700 nm) and blue light (400 nm) strikes a concave parabolic mirror in a vacuum. What are the respective focal points of the red and blue rays?",
     ["Both red and blue light converge at the EXACT SAME focal point",
      "Blue light focuses closer to the mirror than red light",
      "Red light focuses closer to the mirror than blue light",
      "Red light reflects but blue light is completely absorbed"],
     "A", "OSC", "easy",
     "Reflection obeys the law of reflection (angle of incidence = angle of reflection) identically for all electromagnetic wavelengths; therefore, concave mirrors focus all colors of light to the identical focal point with zero chromatic aberration."),

    # 49: Resolving power Rayleigh calculation
    ("If an astronomer desires to double the resolving power of an optical telescope (reducing the resolvable angular separation by half), how must the aperture diameter (D) be modified?",
     ["The aperture diameter (D) must be DOUBLED (2 * D)",
      "The aperture diameter must be halved (D / 2)",
      "The aperture diameter must be quadrupled (4 * D)",
      "The focal length must be multiplied by ten"],
     "A", "OSC", "medium",
     "Rayleigh's criterion states that angular resolution theta = 1.22 * lambda / D. Because angular separation theta is inversely proportional to aperture diameter D, doubling D cuts the minimum resolvable angle in half, doubling resolving power."),

    # 50: Human eye aperture vs 20 cm telescope
    ("The pupil of a dark-adapted human eye has a diameter of approximately 5 mm (0.005 m). How many times more light does a 200 mm (20 cm) telescope collect compared to the human naked eye?",
     ["1,600 times more light", "40 times more light", "400 times more light", "160 times more light"],
     "A", "OSC", "medium",
     "Light gathering ratio = (D_telescope / D_pupil)^2 = (200 mm / 5 mm)^2 = (40)^2 = 1,600 times more photon collecting area than the human eye."),

    # 51: Secondary mirror spider diffraction spikes
    ("If an astronomer photographs a star using a telescope whose secondary mirror is held by a 3-vane spider instead of a 4-vane spider, how many diffraction spikes will radiate from the star image?",
     ["6 diffraction spikes (each vane diffracts in two opposite directions: 3 * 2 = 6)",
      "3 diffraction spikes",
      "4 diffraction spikes",
      "Zero diffraction spikes"],
     "A", "OSC", "hard",
     "Each straight spider strut creates a pair of diffraction spikes radiating in opposite directions (180° apart). In a 4-vane spider with orthogonal vanes, the 4 pairs overlap into 4 visible spikes; with a 3-vane spider (120° apart), the pairs do not overlap, producing 6 distinct diffraction spikes."),

    # 52: Maksutov-Cassegrain corrector meniscus
    ("What optical component distinguishes a Maksutov-Cassegrain telescope from a standard Cassegrain telescope?",
     ["A deeply curved spherical meniscus glass corrector lens at the front of the tube that corrects spherical aberration",
      "A laser beam pointed at the Moon",
      "A water filter inside the eyepiece",
      "A diamond mirror at the back"],
     "A", "OSC", "medium",
     "Invented by Dmitri Maksutov in 1941, this catadioptric design places a thick, deeply curved negative meniscus lens at the entrance pupil; the negative spherical aberration of the meniscus perfectly cancels the positive spherical aberration of the primary mirror."),

    # 53: Primary mirror collimation
    ("What is meant by optical 'Collimation' in reflecting telescopes, and why must it be checked regularly?",
     ["The precise mechanical alignment of the optical axes of the primary mirror, secondary mirror, and eyepiece focuser",
      "Polishing the mirror with sand every week",
      "Painting the outside of the telescope white",
      "Replacing the batteries in the telescope mount"],
     "A", "OSC", "easy",
     "Collimation is the alignment of all optical centerlines; if the primary mirror tilts even fractions of a millimeter out of true alignment with the secondary mirror and focuser, star images suffer severe coma and astigmatism."),

    # 54: Keck telescopes location on Mauna Kea
    ("Why were the twin 10-meter Keck reflecting telescopes constructed on top of the dormant Mauna Kea volcano in Hawaii at an elevation of 4,205 meters?",
     ["The summit rises above 40% of Earth's atmosphere, experiencing minimal cloud cover, low humidity, laminar oceanic airflow, and very dark skies",
      "Because Hawaii is closer to the Moon than any other place on Earth",
      "To harness volcanic geothermal energy to power the telescope mirrors",
      "To prevent earthquakes from affecting the telescopes"],
     "A", "OSC", "easy",
     "Mauna Kea's high altitude and steady inversion layer keep cloud cover below the summit; isolated in the Pacific Ocean, winds blow in smooth laminar layers without convective mountain turbulence, yielding world-class astronomical seeing."),

    # 55: Focal length and image scale on camera sensor
    ("How does the focal length of a telescope's objective mirror affect the physical size (in millimeters) of the Moon's image formed on an astronomical camera sensor?",
     ["Physical image size is directly proportional to focal length: a longer focal length creates a larger image on the sensor",
      "Physical image size is inversely proportional to focal length",
      "Physical image size is completely independent of focal length",
      "Image size depends only on the color of the Moon"],
     "A", "OSC", "medium",
     "The linear image scale at the prime focus is given by Size = focal_length * tan(angular_diameter). A telescope with a 2000 mm focal length produces an image of the Moon (angular size ~0.5°) approximately 17.5 mm across, twice the size produced by a 1000 mm focal length telescope."),

    # 56: Segmented mirror hexagonal geometry
    ("Why are the 36 mirror segments of the Keck telescopes manufactured in hexagonal shapes rather than circular or square shapes?",
     ["Hexagons tile together seamlessly across a curved surface with zero gaps, while providing near-circular symmetry for smooth edge actuators",
      "Because bees build honeycombs and astronomers wanted to honor bees",
      "Because glass can only be cut into hexagons",
      "Because circular mirrors cannot reflect starlight"],
     "A", "OSC", "medium",
     "Regular hexagons provide maximum area per perimeter and tile Euclidean surfaces without interstices or wasted space; furthermore, three-point edge sensor actuators placed between adjacent hexagonal flats maintain precise phasing across the entire composite aperture."),

    # 57: Dew shield function on catadioptric telescopes
    ("Why do astronomers attach an extended cylindrical 'Dew Shield' to the front of a Schmidt-Cassegrain telescope during damp nights?",
     ["To delay radiative cooling of the exposed front corrector glass to the cold night sky, preventing atmospheric moisture from condensing into dew",
      "To block all starlight from entering the telescope",
      "To act as a megaphone so astronomers can hear stars",
      "To protect the telescope from falling meteorites"],
     "A", "OSC", "easy",
     "Exposed glass corrector plates radiate thermal heat directly toward the cold zenith night sky, dropping below ambient dew point temperature; an extended dew shield restricts the clear sky angle, slowing radiative heat loss and keeping the glass clear."),

    # 58: Diagonal mirror minor axis sizing
    ("In a Newtonian reflector, what optical compromise dictates the diameter of the small flat secondary diagonal mirror?",
     ["It must be large enough to intercept the full converging light cone without vignetting, but small enough to minimize central obstruction diffraction",
      "It must be exactly as large as the primary mirror",
      "It must be microscopic so light cannot hit it",
      "It must be made of solid lead"],
     "A", "OSC", "hard",
     "An oversized diagonal mirror obstructs too much incoming starlight and degrades image contrast through increased diffraction; an undersized diagonal cuts off the outer perimeter of the converging light cone, causing severe edge vignetting (darkening)."),

    # 59: Astigmatism off-axis aberration
    ("What optical aberration causes an off-axis star point to focus into two mutually perpendicular focal line segments at slightly different distances rather than a sharp circular point?",
     ["Astigmatism", "Chromatic aberration", "Atmospheric scintillation", "Doppler broadening"],
     "A", "OSC", "medium",
     "Astigmatism occurs when rays in the sagittal and tangential planes of a tilted optical wavefront encounter different curvatures, focusing at different longitudinal planes and smearing star points into cross-shaped ellipses."),

    # 60: Coma aberration in parabolic mirrors
    ("What is 'Coma' aberration, which characteristically flares star images near the outer edges of a parabolic Newtonian reflector into tiny comet-like fan shapes?",
     ["An off-axis geometric aberration where rays from off-axis stars focus at different magnifications across different annular zones of the mirror",
      "A real comet flying into the telescope tube",
      "Dust accumulated on the secondary mirror",
      "Refraction through cold air inside the eyepiece"],
     "A", "OSC", "hard",
     "While a parabolic mirror has zero spherical aberration on-axis, incoming oblique rays from stars off the optical axis focus into overlapping circular zones with varying transverse magnifications, distorting pinpoint stars into distinctive comet-like flares called coma."),

    # 61: Multiple choice OMC on reflecting telescope advantages
    ("Which of the following represent genuine physical advantages of Reflecting telescopes over Refracting telescopes? (Select all that apply)",
     ["Complete freedom from chromatic aberration",
      "Primary mirror can be supported rigidly across its entire back",
      "Can achieve massive aperture diameters (>10 meters) using segmented mirrors",
      "They do not require any glass or optical coatings"],
     "A,B,C", "OMC", "easy",
     "Reflectors are completely achromatic, can be supported across their entire rear substrate, and scale to giant segmented apertures. However, their mirror substrates are still made of glass-ceramics coated with reflective aluminum films."),

    # 62: Multiple choice OMC on telescope optical components
    ("Which optical elements are present in a standard Newtonian reflecting telescope? (Select all that apply)",
     ["A primary concave parabolic mirror",
      "A secondary flat plane mirror tilted at 45 degrees",
      "An eyepiece lens mounted on the side of the tube",
      "A large convex glass objective lens at the tube entrance"],
     "A,B,C", "OMC", "easy",
     "A Newtonian reflector consists of a primary concave mirror, a 45° secondary flat mirror, and an eyepiece mounted on the side. A convex objective lens belongs to refracting telescopes."),

    # 63: Multiple choice OMC on telescope magnification and light
    ("Which of the following statements regarding optical telescopes are TRUE? (Select all that apply)",
     ["Magnification equals objective focal length divided by eyepiece focal length (M = fo / fe)",
      "Light-gathering power is proportional to the square of aperture diameter (D^2)",
      "Larger aperture diameter provides finer angular resolution (smaller diffraction limit theta)",
      "Increasing magnification increases the total amount of light entering the telescope"],
     "A,B,C", "OMC", "medium",
     "Magnification (fo/fe), light gathering (D^2), and angular resolution (lambda/D) are correct. Increasing magnification spreads the existing collected light over a larger angular area, making extended objects appear dimmer, NOT brighter."),

    # 64: True or False on chromatic aberration in mirrors
    ("State whether True or False: Reflecting telescopes using front-surface curved mirrors suffer from severe chromatic aberration.",
     ["True", "False"],
     "B", "OTF", "easy",
     "False. Reflection is completely achromatic because the angle of reflection equals the angle of incidence for all wavelengths of light; mirrors exhibit zero chromatic aberration."),

    # 65: True or False on primary mirror support
    ("State whether True or False: Large telescope mirrors can be supported firmly across their entire rear surface, preventing gravitational sagging.",
     ["True", "False"],
     "A", "OTF", "easy",
     "True. Because starlight reflects off the front surface of an opaque mirror, the entire back and sides of the glass-ceramic blank can be supported by computer-controlled flotation whiffletrees and pneumatic actuators."),

    # 66: True or False on Cassegrain central hole
    ("State whether True or False: In a Cassegrain telescope, drilling a central hole through the primary mirror causes a black circular hole to appear in the center of every star image.",
     ["True", "False"],
     "B", "OTF", "easy",
     "False. Light from every point of a celestial object is collected across the entire surface of the mirror; the central hole simply reduces total photon collecting area slightly without punching a hole in the resulting image."),

    # 67: Assertion and Reason on Newtonian 45-degree mirror
    ("Assertion (A): In a Newtonian telescope, a secondary flat mirror is inclined at an angle of 45 degrees to the principal axis.\nReason (R): This redirects the converging starlight cone sideways out of the telescope tube, allowing comfortable viewing without the observer blocking incoming starlight.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "Without the 45° secondary mirror, the focal point would lie inside the incoming light beam along the tube axis, forcing the astronomer's head to block the telescope aperture."),

    # 68: Assertion and Reason on Reflecting Telescope Superiority
    ("Assertion (A): All modern mega-telescopes constructed for astrophysical research are reflecting telescopes rather than refracting telescopes.\nReason (R): Giant lenses cannot be supported from behind, sag under gravity, and produce chromatic aberration, whereas mirrors avoid all these defects.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "Reflectors eliminate chromatic aberration and permit rear-surface flotation support, making 8- to 30-meter apertures mechanically feasible, whereas refractors max out at approximately 1 meter."),

    # 69: Fill in the blank on Magnification formula
    ("Fill in the blank: The angular magnification of an astronomical telescope is calculated as M = ________ / f_e, where f_e is the focal length of the eyepiece.",
     ["f_o", "D", "lambda", "c"],
     "A", "OFB", "easy",
     "The magnification formula is M = f_o / f_e, where f_o represents the focal length of the objective mirror or lens and f_e represents the focal length of the eyepiece."),

    # 70: Numerical objective on telescope magnification
    ("An astronomical telescope possesses a primary parabolic mirror with a focal length of 2000 mm. If an astronomer attaches a 10 mm eyepiece, calculate the resulting magnifying power.",
     ["200", "20", "2000", "100"],
     "A", "ONE", "easy",
     "Magnification M = f_o / f_e = 2000 mm / 10 mm = 200x.")
]

mock_data = [
    # 71: Refracting Telescope Optical Ray Diagram (Keplerian)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Optical Axis -->
  <line x1="20" y1="100" x2="380" y2="100" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4"/>
  <!-- Objective Lens (Large Convex) -->
  <ellipse cx="80" cy="100" rx="8" ry="65" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
  <text x="80" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Objective Lens (fo)</text>
  <text x="80" y="180" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Large Aperture, Long fo</text>
  <!-- Incoming Parallel Starlight Rays -->
  <line x1="20" y1="50" x2="80" y2="50" stroke="#facc15" stroke-width="1.5"/>
  <line x1="20" y1="150" x2="80" y2="150" stroke="#facc15" stroke-width="1.5"/>
  <!-- Converging to Intermediate Focus F_o -->
  <line x1="80" y1="50" x2="250" y2="115" stroke="#facc15" stroke-width="1.5"/>
  <line x1="80" y1="150" x2="250" y2="85" stroke="#facc15" stroke-width="1.5"/>
  <!-- Intermediate Inverted Real Image -->
  <line x1="250" y1="85" x2="250" y2="115" stroke="#ef4444" stroke-width="2.5"/>
  <polygon points="250,115 247,107 253,107" fill="#ef4444"/>
  <text x="250" y="75" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Intermediate Inverted Image</text>
  <!-- Eyepiece Lens (Small Convex) -->
  <ellipse cx="320" cy="100" rx="5" ry="30" fill="#4ade80" opacity="0.4" stroke="#4ade80" stroke-width="2"/>
  <text x="320" y="55" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Eyepiece (fe)</text>
  <!-- Rays exiting Eyepiece parallel to eye -->
  <line x1="250" y1="115" x2="320" y2="85" stroke="#facc15" stroke-width="1.5"/>
  <line x1="250" y1="85" x2="320" y2="115" stroke="#facc15" stroke-width="1.5"/>
  <line x1="320" y1="85" x2="375" y2="70" stroke="#facc15" stroke-width="1.5"/>
  <line x1="320" y1="115" x2="375" y2="130" stroke="#facc15" stroke-width="1.5"/>
  <text x="365" y="105" fill="#ffffff" font-size="8" font-family="sans-serif">Observer's Eye</text>
</svg>
</div>
In the Keplerian astronomical refracting telescope ray diagram shown above, what are the properties of the intermediate image formed at the focal point of the objective lens?""",
     ["Real, inverted, and located between the objective and eyepiece lenses",
      "Virtual, upright, and located behind the astronomer",
      "Infinitely large and colored green",
      "A rainbow laser beam without any image"],
     "A", "OSC", "easy",
     "The convex objective lens collects distant parallel starlight rays and converges them to form an intermediate real, inverted image at its focal plane (f_o); this image is subsequently magnified by the convex eyepiece lens acting as a magnifying glass."),

    # 72: Chromatic Aberration in Lens Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Optical Axis -->
  <line x1="20" y1="95" x2="380" y2="95" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4"/>
  <!-- Convex Glass Lens -->
  <ellipse cx="90" cy="95" rx="12" ry="60" fill="#38bdf8" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <text x="90" y="25" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Single Convex Lens</text>
  <!-- Incident White Light -->
  <line x1="20" y1="55" x2="90" y2="55" stroke="#ffffff" stroke-width="3"/>
  <line x1="20" y1="135" x2="90" y2="135" stroke="#ffffff" stroke-width="3"/>
  <text x="45" y="45" fill="#ffffff" font-size="8" font-family="sans-serif">White Starlight</text>
  <!-- Blue Rays (Sharper Bending -> F_blue) -->
  <line x1="90" y1="55" x2="220" y2="95" stroke="#38bdf8" stroke-width="2"/>
  <line x1="90" y1="135" x2="220" y2="95" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="220" cy="95" r="4" fill="#38bdf8"/>
  <text x="220" y="80" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">F_blue</text>
  <!-- Red Rays (Gentler Bending -> F_red) -->
  <line x1="90" y1="55" x2="320" y2="95" stroke="#ef4444" stroke-width="2"/>
  <line x1="90" y1="135" x2="320" y2="95" stroke="#ef4444" stroke-width="2"/>
  <circle cx="320" cy="95" r="4" fill="#ef4444"/>
  <text x="320" y="80" fill="#ef4444" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">F_red</text>
  <!-- Defect Label -->
  <rect x="130" y="140" width="220" height="35" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="240" y="162" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">CHROMATIC ABERRATION: Different Focus for Each Color!</text>
</svg>
</div>
Why does a single convex glass lens cause chromatic aberration, as demonstrated in the ray diagram above?""",
     ["Glass exhibits optical dispersion, bending shorter-wavelength blue light more sharply than red light, causing them to converge at different focal points",
      "Because red light cannot travel through glass",
      "Because blue light moves backward inside lenses",
      "Because glass lenses absorb 100% of starlight"],
     "A", "OSC", "easy",
     "Due to dispersion, the refractive index of glass is higher for blue light than for red light. Consequently, blue rays bend more acutely and focus closer to the lens (F_blue) than red rays (F_red), smearing stellar points with colored rainbow rings."),

    # 73: Newtonian Reflecting Telescope Ray Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Telescope Tube Outline -->
  <rect x="40" y="30" width="310" height="130" fill="none" stroke="#475569" stroke-width="2" rx="4"/>
  <text x="180" y="25" fill="#94a3b8" font-size="8" font-family="sans-serif">Telescope Tube</text>
  <!-- Primary Concave Mirror (Right End) -->
  <path d="M 350 40 Q 330 95 350 150" stroke="#38bdf8" stroke-width="6" fill="none"/>
  <text x="345" y="175" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Primary Concave Mirror</text>
  <!-- Incoming Starlight -->
  <line x1="40" y1="50" x2="335" y2="50" stroke="#facc15" stroke-width="1.5"/>
  <line x1="40" y1="140" x2="335" y2="140" stroke="#facc15" stroke-width="1.5"/>
  <!-- Converging to 45 degree secondary flat mirror -->
  <line x1="335" y1="50" x2="130" y2="85" stroke="#facc15" stroke-width="1.5"/>
  <line x1="335" y1="140" x2="130" y2="105" stroke="#facc15" stroke-width="1.5"/>
  <!-- Flat Secondary Mirror at 45 deg -->
  <line x1="120" y1="80" x2="140" y2="110" stroke="#ec4899" stroke-width="4"/>
  <text x="110" y="70" fill="#f472b6" font-size="8" font-family="sans-serif">Flat 45° Mirror</text>
  <!-- Deflected 90 degrees out through tube top to Eyepiece -->
  <line x1="130" y1="85" x2="130" y2="5" stroke="#facc15" stroke-width="1.5"/>
  <line x1="130" y1="105" x2="130" y2="5" stroke="#facc15" stroke-width="1.5"/>
  <!-- Eyepiece mounted on top -->
  <rect x="115" y="5" width="30" height="20" rx="3" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="130" y="-2" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Eyepiece</text>
</svg>
</div>
In the Newtonian reflecting telescope depicted above, what is the specific role of the small flat secondary mirror tilted at 45 degrees?""",
     ["It reflects the converging cone of starlight at 90 degrees out through the side of the tube into the observer's eyepiece",
      "It magnifies the starlight by 500 times",
      "It separates starlight into its component colors",
      "It closes the telescope tube to keep out rain"],
     "A", "OSC", "easy",
     "Newton placed a flat diagonal mirror angled at 45° in the converging path; this reflects the optical focus 90° sideways out of the tube wall to an eyepiece, allowing the observer to view stars comfortably without obstructing incoming light."),

    # 74: Cassegrain Reflecting Telescope Ray Diagram
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Telescope Tube -->
  <rect x="50" y="30" width="280" height="130" fill="none" stroke="#475569" stroke-width="2" rx="4"/>
  <!-- Primary Concave Mirror with Central Hole (Right) -->
  <path d="M 330 40 Q 315 65 330 85" stroke="#38bdf8" stroke-width="6" fill="none"/>
  <path d="M 330 105 Q 315 125 330 150" stroke="#38bdf8" stroke-width="6" fill="none"/>
  <text x="350" y="100" fill="#38bdf8" font-size="8" font-family="sans-serif">Hole</text>
  <text x="330" y="175" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Primary Concave Mirror</text>
  <!-- Incoming Starlight -->
  <line x1="50" y1="50" x2="320" y2="50" stroke="#facc15" stroke-width="1.5"/>
  <line x1="50" y1="140" x2="320" y2="140" stroke="#facc15" stroke-width="1.5"/>
  <!-- Reflection toward Secondary Convex Mirror (Left) -->
  <line x1="320" y1="50" x2="100" y2="85" stroke="#facc15" stroke-width="1.5"/>
  <line x1="320" y1="140" x2="100" y2="105" stroke="#facc15" stroke-width="1.5"/>
  <!-- Small Convex Secondary Mirror -->
  <path d="M 95 80 Q 105 95 95 110" stroke="#f43f5e" stroke-width="5" fill="none"/>
  <text x="85" y="70" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Convex Secondary</text>
  <!-- Reflected straight back through central hole to Eyepiece -->
  <line x1="100" y1="85" x2="360" y2="92" stroke="#facc15" stroke-width="1.5"/>
  <line x1="100" y1="105" x2="360" y2="98" stroke="#facc15" stroke-width="1.5"/>
  <!-- Eyepiece behind primary mirror -->
  <rect x="360" y="85" width="25" height="20" rx="3" fill="#14532d" stroke="#4ade80" stroke-width="1.5"/>
  <text x="372" y="125" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Eyepiece</text>
</svg>
</div>
How does the Cassegrain telescope design route starlight to the observer's eyepiece located behind the main structure?""",
     ["A small convex secondary mirror reflects starlight straight back through a central hole drilled in the primary concave mirror to an eyepiece behind it",
      "Light is sent out through the front opening of the telescope",
      "Light is piped through flexible plastic hoses into the ground",
      "Light reflects sideways out of the tube like a Newtonian telescope"],
     "A", "OSC", "easy",
     "In Laurent Cassegrain's system, starlight converging from the parabolic primary mirror strikes a convex secondary mirror, which reflects the light cone straight back along the central axis through a circular perforation in the primary mirror to an eyepiece located behind."),

    # 75: Mirror Support Flotation vs Thin Lens Sagging
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Lens Box (Left) -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="107" y="48" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">LARGE GLASS LENS</text>
  <ellipse cx="107" cy="85" rx="8" ry="35" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
  <!-- Rim support only -->
  <circle cx="107" cy="50" r="5" fill="#facc15"/>
  <circle cx="107" cy="120" r="5" fill="#facc15"/>
  <text x="107" y="140" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">- Supported ONLY at rims!</text>
  <text x="107" y="155" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Sags & warps under own weight</text>
  <text x="107" y="168" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">MAX SIZE ~ 1 METER</text>
  <!-- Mirror Box (Right) -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="292" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">LARGE MIRROR SUBSTRATE</text>
  <path d="M 285 60 Q 275 85 285 110" stroke="#38bdf8" stroke-width="5" fill="none"/>
  <!-- Multi-point rear actuators -->
  <rect x="295" y="65" width="15" height="10" fill="#facc15"/>
  <rect x="295" y="80" width="15" height="10" fill="#facc15"/>
  <rect x="295" y="95" width="15" height="10" fill="#facc15"/>
  <text x="292" y="140" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">- Supported across ENTIRE back!</text>
  <text x="292" y="155" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">- Active computer flotation control</text>
  <text x="292" y="168" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">SCALES TO 10-30 METERS!</text>
</svg>
</div>
Why can primary mirrors be constructed with diameters exceeding 10 meters, while refracting lenses cannot exceed approximately 1 meter?""",
     ["Opaque mirrors can be supported firmly across their entire rear surface by computer actuators, whereas transparent lenses can only be held around their rims and sag under gravity",
      "Mirrors are made of indestructible plastic while lenses are made of ice",
      "Lenses reflect light backwards while mirrors refract light",
      "Lenses dissolve when exposed to open night air"],
     "A", "OSC", "easy",
     "Transparent lenses must permit light to pass completely through, meaning structural mounts can only clamp around their thin perimeter; massive glass lenses sag under their own colossal weight. Mirrors reflect off the front and can be supported uniformly across their entire back by hundreds of actuators."),

    # 76: Segmented Primary Mirror Array (Keck / TMT)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Central Hexagon -->
  <polygon points="200,80 215,90 215,110 200,120 185,110 185,90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Ring 1 Hexagons around center -->
  <polygon points="200,50 215,60 215,80 200,90 185,80 185,60" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="200,110 215,120 215,140 200,150 185,140 185,120" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="226,65 241,75 241,95 226,105 211,95 211,75" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="226,95 241,105 241,125 226,135 211,125 211,105" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="174,65 189,75 189,95 174,105 159,95 159,75" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="174,95 189,105 189,125 174,135 159,125 159,105" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Info Text -->
  <text x="200" y="30" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Segmented Hexagonal Mirror Architecture (Keck 10m / JWST 6.5m)</text>
  <text x="200" y="175" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">36+ Hexagonal segments tiled with zero gaps -> Actuators align them to nanometer precision!</text>
</svg>
</div>
How does the segmented hexagonal mirror architecture depicted above revolutionize mega-telescope engineering?""",
     ["Multiple smaller, lightweight hexagonal mirror segments tile seamlessly without gaps, controlled by computer actuators to function as a single giant aperture",
      "It makes the telescope look like a giant honeybee hive to attract tourists",
      "It allows astronomers to remove mirrors and use them as serving trays",
      "It completely stops the telescope from needing any focus adjustments"],
     "A", "OSC", "easy",
     "Casting a single 10- or 30-meter glass monolith is technically impossible; tiling dozens of smaller, thinner hexagonal segments aligned in real time by nanometer-precision computerized edge sensors synthesizes a single colossal, lightweight parabolic aperture."),

    # 77: Parabolic vs Spherical Mirror Aberration Comparison
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Spherical Mirror (Left) -->
  <rect x="25" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="107" y="45" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">SPHERICAL MIRROR</text>
  <path d="M 50 60 Q 35 95 50 130" stroke="#38bdf8" stroke-width="4" fill="none"/>
  <!-- Rays crossing at different foci -->
  <line x1="170" y1="65" x2="45" y2="65" stroke="#facc15" stroke-width="1"/>
  <line x1="45" y1="65" x2="110" y2="95" stroke="#facc15" stroke-width="1"/>
  <line x1="170" y1="85" x2="45" y2="85" stroke="#facc15" stroke-width="1"/>
  <line x1="45" y1="85" x2="140" y2="95" stroke="#facc15" stroke-width="1"/>
  <text x="107" y="150" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Spherical Aberration Blur!</text>
  <text x="107" y="162" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Marginal rays focus too close</text>
  <!-- Parabolic Mirror (Right) -->
  <rect x="210" y="25" width="165" height="150" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="292" y="45" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">PARABOLIC MIRROR</text>
  <path d="M 235 60 Q 215 95 235 130" stroke="#38bdf8" stroke-width="4" fill="none"/>
  <!-- All rays converging to single focus -->
  <line x1="355" y1="65" x2="230" y2="65" stroke="#facc15" stroke-width="1"/>
  <line x1="230" y1="65" x2="310" y2="95" stroke="#facc15" stroke-width="1"/>
  <line x1="355" y1="85" x2="225" y2="85" stroke="#facc15" stroke-width="1"/>
  <line x1="225" y1="85" x2="310" y2="95" stroke="#facc15" stroke-width="1"/>
  <circle cx="310" cy="95" r="3" fill="#4ade80"/>
  <text x="292" y="150" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Single Sharp Focus Point!</text>
  <text x="292" y="162" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Zero Spherical Aberration</text>
</svg>
</div>
Why are astronomical primary mirrors figured into a paraboloid rather than a simple spherical concave surface?""",
     ["A parabolic surface reflects all parallel incoming starlight rays to a single, identical geometric focus, eliminating spherical aberration",
      "Parabolic mirrors are easier to clean with water",
      "Spherical mirrors absorb all starlight and turn it into heat",
      "Parabolic mirrors only reflect green light"],
     "A", "OSC", "medium",
     "A spherical mirror reflects outer marginal rays to a shorter focus than central paraxial rays, producing spherical aberration blur; a paraboloid possesses the exact geometric curvature required to converge all parallel rays to a single, infinitely sharp focal point."),

    # 78: Adaptive Optics Real-Time Correction Loop
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Distorted incoming wavefront -->
  <path d="M 40 40 Q 60 55 80 40 T 120 40" stroke="#ef4444" stroke-width="3" fill="none"/>
  <text x="80" y="25" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Distorted Wavefront (Turbulent Air)</text>
  <!-- Deformable Mirror -->
  <path d="M 120 70 Q 140 85 160 70" stroke="#facc15" stroke-width="5" fill="none"/>
  <text x="140" y="60" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Deformable Mirror</text>
  <!-- Actuator array pushing mirror -->
  <rect x="125" y="80" width="6" height="15" fill="#38bdf8"/>
  <rect x="137" y="80" width="6" height="15" fill="#38bdf8"/>
  <rect x="149" y="80" width="6" height="15" fill="#38bdf8"/>
  <text x="140" y="110" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">Piezo-Actuators (1000 Hz)</text>
  <!-- Wavefront sensor & computer loop -->
  <rect x="220" y="120" width="130" height="60" rx="5" fill="#090d16" stroke="#4ade80" stroke-width="1.5"/>
  <text x="285" y="140" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Real-Time Computer</text>
  <text x="285" y="155" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Measures phase errors 1000x/sec</text>
  <text x="285" y="168" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Commands mirror to counter-flex</text>
  <!-- Corrected Flat Wavefront to Science Camera -->
  <line x1="200" y1="70" x2="350" y2="70" stroke="#4ade80" stroke-width="3"/>
  <text x="280" y="60" fill="#4ade80" font-size="8" font-family="sans-serif" font-weight="bold">Corrected Flat Wavefront -> Pinpoint Star!</text>
</svg>
</div>
How does an Adaptive Optics (AO) system restore diffraction-limited resolution to giant ground-based optical telescopes?""",
     ["A wavefront sensor and high-speed computer detect atmospheric distortions and command piezo-actuators to rapidly deform a flexible mirror, canceling phase errors in real time",
      "By warming the air around the telescope with giant electric heaters",
      "By replacing the telescope mirrors with photographic film",
      "By spinning the telescope in reverse to match the Earth's orbit"],
     "A", "OSC", "hard",
     "Adaptive optics samples incoming distorted wavefronts hundreds of times per second using a laser guide star; a dedicated computer commands piezoelectric actuators behind a thin deformable mirror to deform in exact anti-phase, canceling atmospheric turbulence."),

    # 79: First-Surface Mirror vs Second-Surface Mirror
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- First Surface Mirror (Telescope) -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="48" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">TELESCOPE (First-Surface)</text>
  <rect x="40" y="65" width="135" height="30" fill="#334155" stroke="#64748b" stroke-width="1"/>
  <text x="107" y="85" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Glass Substrate</text>
  <!-- Reflective film on FRONT -->
  <line x1="40" y1="65" x2="175" y2="65" stroke="#facc15" stroke-width="4"/>
  <text x="107" y="60" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Aluminium Film on FRONT</text>
  <text x="107" y="125" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Light reflects instantly!</text>
  <text x="107" y="145" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Zero ghost images or dispersion</text>
  <!-- Second Surface Mirror (Household) -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="292" y="48" fill="#f87171" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">HOUSEHOLD (Second-Surface)</text>
  <rect x="225" y="65" width="135" height="30" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="1"/>
  <text x="292" y="85" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">Thick Window Glass</text>
  <!-- Reflective silver on BACK -->
  <line x1="225" y1="95" x2="360" y2="95" stroke="#94a3b8" stroke-width="4"/>
  <text x="292" y="112" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Silver on REAR</text>
  <text x="292" y="130" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Front glass reflection creates GHOSTS!</text>
  <text x="292" y="145" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle">Unacceptable for astronomy</text>
</svg>
</div>
Why must astronomical telescope mirrors be strictly 'First-Surface' (front-coated) mirrors rather than ordinary household back-silvered mirrors?""",
     ["To reflect starlight directly off the front metallic surface without light passing through glass, which would cause refractive absorption and faint ghost double-images",
      "Because front-surface mirrors do not reflect light at night",
      "Because back-silvered mirrors are illegal to purchase",
      "Because household mirrors only work in bathrooms"],
     "A", "OSC", "easy",
     "Back-silvered household mirrors cause light to pass through glass twice, producing secondary reflections (ghosting) from the front glass boundary and chromatic attenuation; astronomical mirrors deposit aluminum on the front face, completely avoiding glass transmission."),

    # 80: Diffraction Spikes from Spider Vanes
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Secondary Spider Hardware (Left) -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="107" y="45" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Spider Support Vanes</text>
  <circle cx="107" cy="95" r="45" fill="none" stroke="#64748b" stroke-width="2"/>
  <line x1="107" y1="50" x2="107" y2="140" stroke="#facc15" stroke-width="2"/>
  <line x1="62" y1="95" x2="152" y2="95" stroke="#facc15" stroke-width="2"/>
  <circle cx="107" cy="95" r="10" fill="#e2e8f0"/>
  <text x="107" y="155" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">4 Thin Metallic Struts</text>
  <!-- Resulting Star Photograph with Spikes (Right) -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#090d16" stroke="#facc15" stroke-width="1.5"/>
  <text x="292" y="45" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Star Image (Diffraction Spikes)</text>
  <!-- Central Star -->
  <circle cx="292" cy="95" r="8" fill="#ffffff"/>
  <!-- 4 Perpendicular Diffraction Spikes -->
  <line x1="292" y1="55" x2="292" y2="135" stroke="#ffffff" stroke-width="1.5" opacity="0.8"/>
  <line x1="252" y1="95" x2="332" y2="95" stroke="#ffffff" stroke-width="1.5" opacity="0.8"/>
  <text x="292" y="155" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">Starlight diffracts off straight vanes!</text>
</svg>
</div>
What causes the prominent cross-shaped 'diffraction spikes' seen radiating from bright stars in photographs taken by reflecting telescopes?""",
     ["Diffraction of incoming starlight waves around the straight metallic spider struts that physically hold the secondary mirror in the center of the tube",
      "Nuclear explosions occurring on the surface of the star",
      "Scratches on the astronomer's camera lens",
      "Atmospheric lightning striking the telescope dome"],
     "A", "OSC", "easy",
     "Whenever light encounters a straight linear edge, it diffracts perpendicularly; the thin orthogonal metallic spider vanes suspending the secondary mirror scatter starlight into four characteristic symmetrical cross-shaped spikes around bright stellar points."),

    # 81: Light-Gathering Power Area Scaling (D1 vs D2)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Small Telescope Aperture -->
  <circle cx="80" cy="95" r="25" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="80" y="92" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">D = 10 cm</text>
  <text x="80" y="105" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Area = 1x</text>
  <!-- Giant Telescope Aperture -->
  <circle cx="260" cy="95" r="65" fill="#1e293b" stroke="#4ade80" stroke-width="3"/>
  <text x="260" y="92" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">D = 100 cm (1 m)</text>
  <text x="260" y="108" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Diameter = 10x larger</text>
  <text x="260" y="125" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Area = 100x larger!</text>
  <!-- Summary Box -->
  <rect x="40" y="150" width="320" height="30" rx="4" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="170" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Light Gathering Power scales with (D2 / D1)^2 = (100 / 10)^2 = 100x!</text>
</svg>
</div>
If a 1-meter observatory telescope has an aperture diameter 10 times larger than a 10-centimeter backyard telescope, how much more starlight does it collect per second?""",
     ["100 times more starlight (10^2 = 100)", "10 times more starlight", "1,000 times more starlight", "20 times more starlight"],
     "A", "OSC", "easy",
     "Light gathering power depends on the circular collecting surface area (pi * r^2). Because area scales with the square of the diameter, increasing aperture diameter by a factor of 10 increases photon collecting capacity by 10^2 = 100 times."),

    # 82: Liquid Mirror Telescope (ILMT Devasthal)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Rotating Basin -->
  <rect x="80" y="120" width="240" height="40" rx="6" fill="#334155" stroke="#64748b" stroke-width="2"/>
  <text x="200" y="145" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">Air Bearing Rotating Turn-table</text>
  <!-- Liquid Mercury Pool (Parabolic Curve) -->
  <path d="M 90 120 Q 200 135 310 120" stroke="#38bdf8" stroke-width="8" fill="#0284c7" opacity="0.6"/>
  <text x="200" y="112" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Rotating Liquid Mercury (Hg) Surface</text>
  <!-- Title and physics note -->
  <text x="200" y="25" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">India's International Liquid Mirror Telescope (ILMT, Devasthal)</text>
  <!-- Rotation arrows -->
  <text x="200" y="55" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Rotation + Gravity -> Natural Perfect Parabola!</text>
  <text x="200" y="75" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">4-meter aperture scanning zenith sky continuously</text>
</svg>
</div>
How does India's 4-meter International Liquid Mirror Telescope (ILMT) at Devasthal create an optically perfect parabolic primary mirror without expensive glass grinding?""",
     ["Spinning a circular container of liquid mercury at a constant speed naturally forms a flawless reflective paraboloid through the balance of gravity and centripetal acceleration",
      "Liquid mercury freezes into solid glass at night",
      "The mercury is hammered into a curved plate every morning",
      "Magnets pull the mercury into a curved shape"],
     "A", "OSC", "medium",
     "According to fluid mechanics, the free surface of a liquid in a container rotating at constant angular velocity omega under gravity assumes an exact paraboloid of revolution (z = omega^2 * r^2 / (2g)), creating a perfect 4-meter optical mirror at a tiny fraction of the cost of glass.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch18_topic2.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
