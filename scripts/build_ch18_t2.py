# -*- coding: utf-8 -*-
"""
Chapter 18 Topics 18.2.1 and 18.2.2 Solution Generator (100 Questions)
Class 9 Science & Technology: Observing Space: Telescopes
Refracting Telescopes (18.2.1) & Reflecting Telescopes (18.2.2)
"""

import json

with open('scripts/t2_dump.json', 'r', encoding='utf-8') as f:
    t2_qs = json.load(f)

solutions = {}

# --- TOPIC 18.2.1: REFRACTING TELESCOPES (50 Qs) ---
# 9 OAR
t2_oar_18_2_1 = {
    "MH-9-SCIT-18-18.2.1-OAR-001": ("""Refracting telescopes use glass lenses that refract light; because glass has different refractive indices for different wavelengths, dispersion causes different colors to focus at different points (chromatic aberration).""",
        "True — Glass lenses produce chromatic aberration, causing color fringes around bright celestial images.",
        "True — Dispersion inside glass causes violet light to bend more than red light, focusing them at different focal points.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-002": ("""Large optical lenses are extremely heavy and can only be mechanically supported along their thin outer rims, causing them to sag and distort under their own weight.""",
        "True — Manufacturing very large glass lenses (over 1 meter diameter) is practically impossible due to mechanical sagging.",
        "True — Heavy glass lenses can only be clamped around their circumferences, leading to gravitational deformation.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-003": ("""The objective lens of an astronomical telescope must have a large aperture to gather sufficient light from faint, distant celestial bodies and provide high resolving power.""",
        "True — Astronomical refracting telescopes require large objective lenses to collect abundant light from distant stars.",
        "True — Light gathering power is proportional to the square of the objective's diameter (\\(D^2\\)).",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-004": ("""Magnification of a standard astronomical telescope is given by \\(M = f_o / f_e\\), where \\(f_o\\) is the focal length of the objective lens and \\(f_e\\) is the focal length of the eyepiece.""",
        "True — High magnification requires a long focal length objective and a short focal length eyepiece.",
        "True — Magnification is the ratio of the focal length of the objective to that of the eyepiece.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-005": ("""A simple convex lens bends violet light more sharply than red light because the refractive index of optical glass is higher for shorter wavelengths (\\(n_{\\text{violet}} > n_{\\text{red}}\\)).""",
        "True — The focal length for violet light is shorter than the focal length for red light in a simple convex lens.",
        "True — Higher refractive index causes greater angular deviation according to Snell's law.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-006": ("""Thick glass objective lenses absorb a noticeable fraction of incoming starlight, reducing image brightness and distorting astronomical color measurements.""",
        "True — Massive glass objective lenses suffer from significant optical transmission losses.",
        "True — Starlight passing through inches of optical glass experiences absorption and internal scattering.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-007": ("""Galileo Galilei improved the refracting telescope in 1609 to discover Jupiter's four largest moons, lunar craters, and the phases of Venus.""",
        "True — Galileo used a refracting telescope with a convex objective and concave eyepiece to pioneer observational astronomy.",
        "True — Galileo's optical observations provided revolutionary empirical evidence supporting the heliocentric Copernican model.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-008": ("""Achromatic doublet lenses combine two glass elements with opposite dispersive powers (crown glass and flint glass) to bring two primary wavelengths to a common focus.""",
        "True — Achromatic doublets significantly minimize chromatic aberration in refracting telescopes.",
        "True — The convergent crown lens and divergent flint lens cancel out chromatic dispersion for red and blue light.",
        "A"),
    "MH-9-SCIT-18-18.2.1-OAR-009": ("""A long telescope tube is physically required for refracting telescopes because the length of the tube equals the sum of the focal lengths (\\(L \\approx f_o + f_e\\)).""",
        "True — High-magnification refracting telescopes require extremely long, unwieldy physical tubes.",
        "True — The image formed at the objective's focal plane must be magnified by an eyepiece positioned at its focal distance.",
        "A")
}

# 11 OTF
t2_otf_18_2_1 = {
    "MH-9-SCIT-18-18.2.1-OTF-001": ("In an astronomical telescope, the objective lens must have a large diameter (aperture) and long focal length to gather maximum starlight.",
        False, "The objective lens has a large diameter and long focal length to collect abundant starlight, while the eyepiece has a small diameter and short focal length."),
    "MH-9-SCIT-18-18.2.1-OTF-002": ("Because glass has a higher refractive index for shorter wavelengths, violet light refracts more strongly than red light, focusing closer to the lens.",
        True, "Violet light has a shorter wavelength and refracts more sharply than red light, resulting in chromatic aberration in simple lenses."),
    "MH-9-SCIT-18-18.2.1-OTF-003": ("Galileo Galilei was the first to use a telescope for systematic astronomical observations in 1609.",
        True, "Galileo pointed his telescope toward the heavens in 1609, discovering Jupiter's moons, lunar mountains, and sunspots."),
    "MH-9-SCIT-18-18.2.1-OTF-004": ("Chromatic aberration occurs exclusively in lenses due to refraction and dispersion; it never occurs in reflective mirrors.",
        True, "Reflection obeys \\(i = r\\) identically for all wavelengths, making mirrors completely immune to chromatic aberration."),
    "MH-9-SCIT-18-18.2.1-OTF-005": ("The total tube length of a standard astronomical refractor focused at infinity is approximately the sum of focal lengths, \\(L \\approx f_o + f_e\\).",
        True, "The objective forms a real image at its focal plane \\(f_o\\), which is viewed by an eyepiece located at distance \\(f_e\\), making tube length \\(f_o + f_e\\)."),
    "MH-9-SCIT-18-18.2.1-OTF-006": ("The Yerkes Observatory 40-inch (1.02 m) refractor remains the largest operational astronomical refracting telescope ever built.",
        True, "Built in 1897 at Yerkes Observatory, the 40-inch refractor is the largest refracting telescope ever constructed due to structural glass limits."),
    "MH-9-SCIT-18-18.2.1-OTF-007": ("A concave lens diverges light rays and cannot form a real image by itself; convex lenses are used as objectives.",
        False, "Refracting telescope objectives must be converging (convex) lenses to collect and focus parallel starlight into a real image."),
    "MH-9-SCIT-18-18.2.1-OTF-008": ("Large glass lenses can only be supported along their perimeter rims, causing them to sag gravitationally under their own weight.",
        True, "Because starlight must pass through the lens body, glass lenses cannot be supported from behind, causing physical sagging in large apertures."),
    "MH-9-SCIT-18-18.2.1-OTF-009": ("Refracting telescopes form an inverted real image of distant astronomical objects at the primary focal plane.",
        True, "A convex objective lens forms a real, inverted, and diminished image of distant astronomical targets at its focus."),
    "MH-9-SCIT-18-18.2.1-OTF-010": ("Refracting telescopes use lenses that refract light, while reflecting telescopes use mirrors that reflect light.",
        True, "Refraction through glass lenses is the defining mechanism of refracting telescopes."),
    "MH-9-SCIT-18-18.2.1-OTF-011": ("Thick optical glass absorbs starlight and can contain internal bubbles and impurities that degrade image clarity.",
        True, "Light passing through massive glass lenses experiences optical absorption and internal scatter from residual defects.")
}

# 21 OSC
t2_osc_18_2_1 = {
    "MH-9-SCIT-18-18.2.1-OSC-001": ("A refracting telescope consists of two primary convex lenses: an objective lens of large aperture and an eyepiece of short focal length.", {
        "A": "A refracting telescope consists of an objective lens to collect light and an eyepiece lens to magnify the image.",
        "B": "Incorrect; plane mirrors do not refract light.",
        "C": "Incorrect; concave mirrors are used in reflecting telescopes.",
        "D": "Incorrect; diffraction gratings are used in spectrometers."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-002": ("The objective lens collects starlight from distant objects and focuses it to form a real, inverted image at its focal plane.", {
        "A": "The objective lens collects light from distant celestial bodies and focuses it into a real, inverted image.",
        "B": "Incorrect; the eyepiece magnifies the image for the observer's eye.",
        "C": "Incorrect; dispersing light into a rainbow is chromatic aberration, not the primary goal.",
        "D": "Incorrect; polarization is not the primary function."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-003": ("Chromatic aberration is the optical defect where a lens fails to focus all colors to the same convergence point due to dispersion.", {
        "A": "Chromatic aberration is caused by the dispersion of light in glass lenses, producing colored fringes around images.",
        "B": "Incorrect; spherical aberration is due to spherical mirror/lens curvature.",
        "C": "Incorrect; astigmatism is an off-axis curvature error.",
        "D": "Incorrect; coma is an off-axis comet-shaped distortion."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-004": ("Galileo Galilei constructed his refracting telescope in 1609 and made pioneering discoveries including the Galilean moons of Jupiter.", {
        "A": "Galileo Galilei made the first recorded astronomical observations with a telescope in 1609.",
        "B": "Incorrect; Sir Isaac Newton invented the reflecting telescope in 1668.",
        "C": "Incorrect; Johannes Kepler designed the Keplerian refractor with two convex lenses.",
        "D": "Incorrect; Edwin Hubble discovered the expansion of the universe in the 20th century."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-005": ("Magnification in an astronomical telescope is calculated as \\(M = f_o / f_e\\), the ratio of objective focal length to eyepiece focal length.", {
        "A": "Magnification equals \\(f_o / f_e\\), the focal length of the objective divided by the focal length of the eyepiece.",
        "B": "Incorrect; \\(f_e / f_o\\) is the inverse of magnification.",
        "C": "Incorrect; focal lengths are divided, not multiplied.",
        "D": "Incorrect; \\(f_o + f_e\\) gives the approximate tube length."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-006": ("In glass, violet light has a higher refractive index than red light (\\(n_v > n_r\\)), causing it to bend more strongly and have a shorter focal length.", {
        "A": "Violet light refracts the most and has the shortest focal length in a simple convex lens.",
        "B": "Incorrect; red light has the longest wavelength and refracts the least.",
        "C": "Incorrect; green light has an intermediate focal length.",
        "D": "Incorrect; yellow light has an intermediate focal length."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-007": ("The largest operational astronomical refracting telescope is the 40-inch (1.02 m) refractor at Yerkes Observatory in Wisconsin.", {
        "A": "The 40-inch (1.02 m) refractor at Yerkes Observatory is the largest refracting telescope ever built for astronomy.",
        "B": "Incorrect; Mount Palomar houses the 200-inch Hale reflecting telescope.",
        "C": "Incorrect; Mauna Kea houses giant 10-meter Keck reflecting telescopes.",
        "D": "Incorrect; La Silla houses large reflecting telescopes."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-008": ("A larger aperture (diameter) increases the telescope's light-gathering area in proportion to the square of its diameter (\\(A \\propto D^2\\)).", {
        "A": "A larger objective lens diameter collects more light, allowing faint and distant stars to be detected clearly.",
        "B": "Incorrect; diameter does not change the speed of light.",
        "C": "Incorrect; lens diameter does not eliminate chromatic aberration.",
        "D": "Incorrect; larger lenses increase weight and cost."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-009": ("An achromatic doublet combines a convex crown glass lens with a concave flint glass lens to bring two primary wavelengths to the same focal point.", {
        "A": "An achromatic doublet combines two different glass lenses (crown and flint) to cancel chromatic aberration.",
        "B": "Incorrect; parabolic mirrors are used in reflecting telescopes.",
        "C": "Incorrect; color filters block light rather than correcting focus.",
        "D": "Incorrect; periscopes do not correct chromatic aberration."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-010": ("Because starlight must pass through a lens, large lenses can only be mounted at their rim edges, causing them to sag under their own weight.", {
        "A": "Large glass lenses can only be supported along their outer edges, leading to structural sagging and image distortion.",
        "B": "Incorrect; lenses do not produce radio interference.",
        "C": "Incorrect; glass does not vaporize in open air.",
        "D": "Incorrect; glass does not attract static charge from starlight."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-011": ("The eyepiece of an astronomical telescope functions as a simple magnifier, enlarging the real image formed by the objective into a virtual image.", {
        "A": "The eyepiece acts as a magnifying lens to enlarge the intermediate real image formed by the objective.",
        "B": "Incorrect; collecting primary starlight is the objective's job.",
        "C": "Incorrect; the eyepiece does not reflect light back to space.",
        "D": "Incorrect; the eyepiece does not filter X-rays."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-012": ("The tube length of a two-lens astronomical telescope adjusted for normal view (infinity) is given by \\(L = f_o + f_e\\).", {
        "A": "The tube length is approximately equal to the sum of the focal lengths of the objective and eyepiece (\\(f_o + f_e\\)).",
        "B": "Incorrect; subtracting focal lengths applies to Galilean terrestrial telescopes.",
        "C": "Incorrect; focal lengths are added, not multiplied.",
        "D": "Incorrect; division calculates magnification, not tube length."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-013": ("A standard Keplerian astronomical refracting telescope produces an inverted (upside down) image, which is acceptable in astronomy.", {
        "A": "Astronomical refracting telescopes form an inverted image of celestial objects.",
        "B": "Incorrect; erecting lenses are only added in terrestrial telescopes for upright terrestrial viewing.",
        "C": "Incorrect; astronomical images are inverted.",
        "D": "Incorrect; lateral displacement applies to glass slabs."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-014": ("Light gathering power of an optical instrument is directly proportional to the area of the objective aperture: \\(\\text{LGP} \\propto D^2\\).", {
        "A": "Light gathering power is directly proportional to the square of the objective's diameter (\\(D^2\\)).",
        "B": "Incorrect; it depends on the square of diameter, not linear diameter.",
        "C": "Incorrect; it does not depend inversely on diameter.",
        "D": "Incorrect; it does not depend on tube length."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-015": ("Johannes Kepler improved the refracting telescope in 1611 by replacing Galileo's concave eyepiece with a convex eyepiece, giving a wider field of view.", {
        "A": "Johannes Kepler designed the astronomical refractor using two convex lenses.",
        "B": "Incorrect; Galileo used a concave eyepiece.",
        "C": "Incorrect; Newton invented reflecting telescopes.",
        "D": "Incorrect; Cassegrain designed a reflecting telescope."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-016": ("A major limitation of large refracting telescopes is that massive glass lenses absorb and scatter light, especially in UV and blue wavelengths.", {
        "A": "Thick glass absorbs a significant fraction of starlight and suffers from internal bubbles or defects.",
        "B": "Incorrect; lenses do not generate magnetic fields.",
        "C": "Incorrect; lenses do not reflect all light away.",
        "D": "Incorrect; lenses do not emit ionizing radiation."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-017": ("In an astronomical telescope with \\(f_o = 100\\text{ cm}\\) and \\(f_e = 5\\text{ cm}\\), the magnification is \\(M = 100 / 5 = 20\\).", {
        "A": "Magnification is \\(M = f_o / f_e = 100 / 5 = 20\\).",
        "B": "Incorrect; 500 is the product, not the ratio.",
        "C": "Incorrect; 105 is the tube length in cm.",
        "D": "Incorrect; 0.05 is the inverse ratio."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-018": ("Refracting telescopes use glass lenses that refract light rays according to Snell's law of refraction: \\(n_1 \\sin i = n_2 \\sin r\\).", {
        "A": "Refraction of light through curved glass lenses is the optical basis of refracting telescopes.",
        "B": "Incorrect; reflection operates in reflecting telescopes.",
        "C": "Incorrect; diffraction is a wave-spreading limitation, not the primary focusing mechanism.",
        "D": "Incorrect; polarization is not the primary focusing mechanism."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-019": ("The primary factor that prevented astronomers from building refracting telescopes larger than 1 meter was the mechanical sagging of heavy glass lenses.", {
        "A": "Mechanical distortion and sagging under gravity of large lenses supported only at rims prevented larger refractors.",
        "B": "Incorrect; sand and silica to make glass are abundant.",
        "C": "Incorrect; mountaintops had ample space.",
        "D": "Incorrect; astronomical funding was not the physical barrier."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-020": ("Terrestrial telescopes add an erecting lens or prism system to flip the inverted astronomical image upright for viewing earthbound objects.", {
        "A": "Terrestrial telescopes include an erecting lens or Porro prism to produce an upright image.",
        "B": "Incorrect; astronomical refractors show inverted images.",
        "C": "Incorrect; radio telescopes do not produce optical images.",
        "D": "Incorrect; spectrographs produce spectral lines, not upright views."
    }),
    "MH-9-SCIT-18-18.2.1-OSC-021": ("In an achromatic doublet, the converging lens is typically made of crown glass (lower dispersion) and the diverging lens of flint glass (higher dispersion).", {
        "A": "Crown glass has lower dispersion, while flint glass has higher dispersion, canceling chromatic aberration when paired.",
        "B": "Incorrect; both elements cannot have identical dispersion.",
        "C": "Incorrect; flint glass alone does not eliminate aberration.",
        "D": "Incorrect; plastic lenses degrade under environmental conditions."
    })
}

# 9 OMC 18.2.1
t2_omc_18_2_1 = {
    "MH-9-SCIT-18-18.2.1-OMC-001": ("The eyepiece of an astronomical refractor has a short focal length, magnifies the intermediate real image, and forms a comfortable virtual image.", {
        "It acts as a simple magnifying glass to enlarge the image formed by the objective lens.": "Correct; the eyepiece magnifies the real intermediate image.",
        "It has a shorter focal length than the objective lens.": "Correct; \\(f_e < f_o\\) ensures magnification \\(M = f_o / f_e > 1\\).",
        "It helps the human eye comfortably view the magnified virtual image.": "Correct; it projects parallel rays to the eye at infinity.",
        "It is always a diverging concave lens in modern astronomical refractors.": "Incorrect; modern Keplerian refractors use convex eyepieces."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-002": ("Large refracting telescopes suffer from chromatic aberration, glass absorption of light, and gravitational sagging of heavy rim-supported lenses.", {
        "Chromatic aberration causing distorted or colored image borders": "Correct; dispersion inside glass splits white light into colored fringes.",
        "Sagging of heavy objective lenses supported only at their rims": "Correct; gravity deforms heavy lenses supported only by perimeter edges.",
        "Absorption of light passing through the thick glass of the objective lens": "Correct; starlight is absorbed and scattered inside inches of optical glass.",
        "Complete inability to view celestial objects at night": "Incorrect; refractors operate perfectly at night."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-003": ("The objective lens of an astronomical refractor is a converging convex lens with a large aperture to maximize light collection.", {
        "It is a convex lens that converges incoming parallel light rays.": "Correct; convex lenses focus light into a real image.",
        "It has a relatively large diameter to maximize light gathering power.": "Correct; large diameter gathers more light from faint stars.",
        "It has a longer focal length compared to the eyepiece.": "Correct; long focal length increases overall magnification.",
        "It produces a virtual, erect image of the distant celestial object.": "Incorrect; it forms a real, inverted image at its focal plane."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-004": ("Galileo's 1609 refracting telescope revealed Jupiter's four large moons, craters on the Moon, and the phases of Venus.", {
        "Moons orbiting Jupiter (the Galilean moons)": "Correct; Io, Europa, Ganymede, and Callisto were discovered by Galileo.",
        "Craters and mountains on the surface of the Moon": "Correct; showed that the Moon was a rugged, imperfect world.",
        "Phases of the planet Venus": "Correct; proved Venus orbits the Sun, supporting Copernicus.",
        "The spiral arms and central black hole of the Andromeda Galaxy": "Incorrect; resolving galactic structures required 20th-century telescopes."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-005": ("To increase telescope magnification (\\(M = f_o / f_e\\)), one can increase the objective's focal length \\(f_o\\) or decrease the eyepiece focal length \\(f_e\\).", {
        "Increase the focal length of the objective lens.": "Correct; higher \\(f_o\\) in \\(M = f_o / f_e\\) increases magnification.",
        "Decrease the focal length of the eyepiece lens.": "Correct; smaller \\(f_e\\) in the denominator increases magnification.",
        "Use an eyepiece with a very large focal length.": "Incorrect; larger \\(f_e\\) reduces magnification.",
        "Shorten the focal length of the objective lens.": "Incorrect; smaller \\(f_o\\) reduces magnification."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-006": ("Chromatic aberration occurs because different wavelengths of light experience different refractive indices in glass, focusing at different distances.", {
        "Different colors of light have different wavelengths.": "Correct; white light contains wavelengths from 400 nm to 700 nm.",
        "The refractive index of glass varies with the wavelength of light.": "Correct; shorter wavelengths experience higher refractive indices.",
        "Violet light refracts more than red light.": "Correct; violet light has a shorter focal length than red light.",
        "Light rays reflect off the outer lens surface at differing angles.": "Incorrect; chromatic aberration is caused by refraction and dispersion inside glass, not reflection."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-007": ("Refracting telescopes use lenses that bend light, whereas reflecting telescopes use mirrors that reflect light, avoiding chromatic aberration.", {
        "Refracting telescopes use lenses to focus light, while reflecting telescopes use mirrors.": "Correct; this is the core optical distinction.",
        "Reflecting telescopes are immune to chromatic aberration.": "Correct; reflection angles do not depend on wavelength.",
        "Refracting telescopes can achieve far larger apertures than reflecting telescopes.": "Incorrect; reflecting telescopes reach 10+ meters, whereas refractors max out at 1 meter.",
        "Refracting telescopes generally require longer and heavier tubes for high magnification.": "Correct; \\(L \\approx f_o + f_e\\) necessitates long tubes."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-008": ("Achromatic doublets combine two lens elements of different glass types (crown and flint) to cancel chromatic dispersion for two colors.", {
        "It uses a combination of crown glass and flint glass lenses.": "Correct; combining positive and negative dispersions eliminates color fringes.",
        "It brings at least two wavelengths (usually red and blue) to a common focal point.": "Correct; this minimizes chromatic aberration.",
        "It completely eliminates all physical weight limitations of glass lenses.": "Incorrect; adding a second lens actually increases total weight.",
        "It helps produce sharper images free of heavy color fringes.": "Correct; color blur is drastically reduced."
    }),
    "MH-9-SCIT-18-18.2.1-OMC-009": ("Refracting telescopes are widely used for planetary and double-star observation, small amateur spotting scopes, and camera telephoto lenses.", {
        "Amateur astronomy for observing planets and the Moon": "Correct; sharp contrast makes refractors excellent for lunar and planetary viewing.",
        "Terrestrial spotting scopes and bird watching binoculars": "Correct; portable refractors with erecting prisms are standard for field optics.",
        "Telephoto lenses in photography": "Correct; camera lenses use multi-element refractive optics.",
        "Deep-sky surveys of ultra-faint distant galaxies": "Incorrect; deep-sky survey instruments are massive reflecting telescopes."
    })
}

# --- TOPIC 18.2.2: REFLECTING TELESCOPES (50 Qs) ---
# 9 OAR
t2_oar_18_2_2 = {
    "MH-9-SCIT-18-18.2.2-OAR-001": ("""Modern research telescopes are exclusively reflectors because mirrors can be supported from behind across their entire back surface and are completely free from chromatic aberration.""",
        "True — All modern giant astronomical telescopes (e.g. Keck, VLT, Subaru) use reflective primary mirrors.",
        "True — Primary mirrors do not suffer from chromatic aberration and can be solidly supported across their entire back face.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-002": ("""Spherical mirrors suffer from spherical aberration because marginal rays focus closer to the mirror than paraxial rays; parabolic mirrors eliminate this by focusing all parallel rays to a single point.""",
        "True — Spherical mirrors produce blurred focal spots because parallel rays at different distances from the axis do not meet at a single point.",
        "True — A parabolic curvature brings all parallel light rays to an exact single focal point regardless of aperture distance.",
        "B"),
    "MH-9-SCIT-18-18.2.2-OAR-003": ("""Sir Isaac Newton invented the reflecting telescope in 1668 specifically to overcome the chromatic aberration inherent to glass lenses.""",
        "True — Newton constructed the first functional reflecting telescope using a speculum metal concave mirror and a diagonal flat mirror.",
        "True — Newton discovered that light reflection follows \\(i = r\\) identically for all colors, eliminating chromatic dispersion.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-004": ("""In a Cassegrain telescope, starlight reflected from the primary parabolic mirror converges toward a secondary convex mirror, which reflects light back through a hole in the primary mirror.""",
        "True — The Cassegrain design places the eyepiece and heavy instruments conveniently behind the primary mirror.",
        "True — Folding the optical path between the primary and secondary mirrors allows a long effective focal length inside a compact tube.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-005": ("""Reflective mirrors reflect light from a thin aluminum or silver coating on their front surface; starlight does not pass through the glass body.""",
        "True — Mirror glass does not absorb starlight and does not require optical purity inside the glass bulk.",
        "True — Reflection occurs entirely at the front reflective metallic boundary.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-006": ("""Newtonian reflecting telescopes use a small flat secondary mirror tilted at 45 degrees to deflect the focused beam out through the side of the tube to the eyepiece.""",
        "True — The observer looks through an eyepiece located on the side near the open front end of a Newtonian telescope.",
        "True — The 45-degree flat mirror diverts the convergent ray cone at a right angle (90 degrees) to the optical axis.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-007": ("""Giant segmented mirror telescopes (like Keck and Thirty Meter Telescope) combine dozens of computer-controlled hexagonal mirror segments to form a single massive collecting surface.""",
        "True — Segmented mirrors enable building primary mirrors far exceeding the 8.4-meter limit of monolithic glass casting.",
        "True — Active optics and computer actuators precisely align each hexagonal segment to sub-wavelength tolerances.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-008": ("""Cassegrain telescopes offer a much more compact physical tube length than Newtonian telescopes for an equivalent effective focal length.""",
        "True — Cassegrain telescopes fold the light path back and forth, reducing tube length by more than half.",
        "True — The secondary convex mirror increases the effective focal length while shortening physical tube dimensions.",
        "A"),
    "MH-9-SCIT-18-18.2.2-OAR-009": ("""A parabolic mirror avoids spherical aberration for parallel rays parallel to the principal axis, whereas spherical mirrors produce a longitudinal focal blur.""",
        "True — Parabolic concave mirrors are standard for astronomical reflectors because they focus all parallel starlight to a sharp point.",
        "True — By geometry, any ray parallel to the axis of a parabola reflects directly through its focus.",
        "A")
}

# 11 OTF
t2_otf_18_2_2 = {
    "MH-9-SCIT-18-18.2.2-OTF-001": ("Reflecting telescopes are completely free from chromatic aberration because reflection angles do not depend on wavelength.",
        True, "The law of reflection (\\(i = r\\)) holds identically for all wavelengths, so mirrors never suffer from chromatic aberration."),
    "MH-9-SCIT-18-18.2.2-OTF-002": ("In a Cassegrain reflecting telescope, the secondary mirror is a convex mirror that reflects light back through a central hole in the primary mirror.",
        True, "The Cassegrain design uses a primary parabolic concave mirror and a secondary hyperbolic/convex mirror reflecting through a central hole."),
    "MH-9-SCIT-18-18.2.2-OTF-003": ("Sir Isaac Newton invented the first reflecting telescope in 1668 to eliminate chromatic aberration.",
        True, "Newton designed the Newtonian reflecting telescope using a concave primary mirror and a 45-degree flat secondary mirror."),
    "MH-9-SCIT-18-18.2.2-OTF-004": ("Parabolic concave mirrors bring all incoming parallel starlight to a single sharp focus, completely eliminating spherical aberration.",
        True, "A parabolic profile focuses all rays parallel to its axis to an exact point, avoiding the spherical aberration of spherical mirrors."),
    "MH-9-SCIT-18-18.2.2-OTF-005": ("In a Newtonian telescope, the eyepiece is located on the side of the telescope tube near the front open end.",
        True, "The 45-degree flat diagonal mirror deflects focused light 90 degrees out through the side of the tube near the open front."),
    "MH-9-SCIT-18-18.2.2-OTF-006": ("Reflecting telescope primary mirrors can be supported from behind across their entire rear surface, preventing gravitational sagging.",
        True, "Because light reflects off the front surface, the entire back of the mirror can be mechanically supported by steel trusses and actuators."),
    "MH-9-SCIT-18-18.2.2-OTF-007": ("Light passes directly through the glass substrate of the primary mirror in a reflecting telescope.",
        False, "Starlight reflects off the front metallic (aluminum) coating; it does not pass through the glass body of the mirror."),
    "MH-9-SCIT-18-18.2.2-OTF-008": ("A Cassegrain telescope has a shorter physical tube length than a Newtonian telescope of the same effective focal length.",
        True, "The light path folds back on itself between primary and secondary mirrors, allowing a very compact tube design."),
    "MH-9-SCIT-18-18.2.2-OTF-009": ("Modern giant telescopes with apertures of 8 to 10 meters (like Keck and Subaru) are all reflecting telescopes.",
        True, "All modern giant research telescopes are reflectors because lenses cannot be built or supported at that scale."),
    "MH-9-SCIT-18-18.2.2-OTF-010": ("Spherical mirrors focus light from edge rays and central rays at the exact same focal point.",
        False, "Spherical mirrors suffer from spherical aberration; rays reflecting from the mirror edge focus closer than rays from the center."),
    "MH-9-SCIT-18-18.2.2-OTF-011": ("The secondary mirror in a Newtonian telescope is a flat plane mirror mounted at an angle of 45 degrees.",
        True, "A small diagonal flat mirror mounted at 45 degrees directs light to the eyepiece on the side of the tube.")
}

# 21 OSC
t2_osc_18_2_2 = {
    "MH-9-SCIT-18-18.2.2-OSC-001": ("A reflecting telescope uses a large concave mirror as its primary optical element to collect and focus starlight.", {
        "A": "A concave mirror (parabolic or spherical) serves as the primary objective in a reflecting telescope.",
        "B": "Incorrect; convex mirrors diverge light.",
        "C": "Incorrect; plane mirrors do not focus parallel rays.",
        "D": "Incorrect; convex lenses are used in refracting telescopes."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-002": ("Parabolic concave mirrors focus all incoming parallel rays to a single focal point, eliminating spherical aberration.", {
        "A": "Parabolic concave mirrors bring all parallel starlight to a single sharp focus without spherical aberration.",
        "B": "Incorrect; mirrors do not produce chromatic aberration anyway.",
        "C": "Incorrect; parabolic shape does not alter glass weight.",
        "D": "Incorrect; parabolic mirrors do not disperse starlight."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-003": ("Sir Isaac Newton invented the reflecting telescope in 1668 to eliminate the chromatic aberration that plagued lenses.", {
        "A": "Sir Isaac Newton invented the reflecting telescope in 1668.",
        "B": "Incorrect; Galileo built refracting telescopes.",
        "C": "Incorrect; Kepler designed refracting telescopes with convex eyepieces.",
        "D": "Incorrect; Edwin Hubble used reflecting telescopes in the 20th century."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-004": ("A Newtonian telescope uses a small flat plane mirror angled at 45 degrees to deflect light 90 degrees out through the tube wall to the eyepiece.", {
        "A": "A small flat plane mirror tilted at 45 degrees reflects light to a side-mounted eyepiece.",
        "B": "Incorrect; Cassegrain uses a convex secondary mirror.",
        "C": "Incorrect; prisms are not used as secondary mirrors in standard Newtonians.",
        "D": "Incorrect; a concave secondary mirror would focus light incorrectly."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-005": ("In a Cassegrain telescope, a secondary convex mirror reflects convergent rays back through a hole in the center of the primary mirror.", {
        "A": "A Cassegrain telescope directs light through a central hole in the primary mirror to an eyepiece behind it.",
        "B": "Incorrect; Newtonian telescopes place the eyepiece on the side near the top.",
        "C": "Incorrect; Galilean refractors place the eyepiece directly in line without mirrors.",
        "D": "Incorrect; Keplerian refractors do not have holes in lenses."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-006": ("Reflecting telescopes are completely immune to chromatic aberration because light reflection follows the law \\(i = r\\) for all colors.", {
        "A": "Reflecting telescopes are completely free from chromatic aberration because reflection does not depend on wavelength.",
        "B": "Incorrect; mirrors still suffer from atmospheric seeing on Earth.",
        "C": "Incorrect; diffraction limits still apply based on aperture.",
        "D": "Incorrect; mirrors can suffer from coma and spherical aberration if not parabolic."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-007": ("The secondary mirror in a Cassegrain reflecting telescope has a convex curved reflective surface.", {
        "A": "The secondary mirror in a Cassegrain telescope is a small convex mirror.",
        "B": "Incorrect; flat plane mirrors are used in Newtonian telescopes.",
        "C": "Incorrect; concave secondary mirrors are used in Gregorian telescopes.",
        "D": "Incorrect; lenses are not used as secondary mirrors."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-008": ("Primary mirrors reflect light from a thin front-surface metallic coating (usually aluminum), meaning starlight never passes through the glass substrate.", {
        "A": "Light reflects from a thin reflective metallic layer on the front surface of the mirror, never penetrating the glass.",
        "B": "Incorrect; starlight does not pass through the back.",
        "C": "Incorrect; household mirrors are back-silvered, but astronomical mirrors are front-aluminized.",
        "D": "Incorrect; light is reflected, not refracted."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-009": ("Because starlight reflects from the front surface, primary mirrors can be supported from behind across their entire back face, avoiding gravitational sagging.", {
        "A": "Primary mirrors can be fully supported across their rear surface, preventing gravitational sagging in large apertures.",
        "B": "Incorrect; mirrors can be made far larger than lenses (10+ m vs 1 m).",
        "C": "Incorrect; mirrors are not immune to dust.",
        "D": "Incorrect; mirrors do not produce their own light."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-010": ("Spherical aberration in a spherical mirror occurs because rays hitting the outer edge focus closer to the mirror than rays hitting near the center.", {
        "A": "Spherical aberration occurs when light rays striking different zones of a spherical mirror do not meet at a common focus.",
        "B": "Incorrect; chromatic aberration is dispersion in lenses.",
        "C": "Incorrect; diffraction is a wave-aperture phenomenon.",
        "D": "Incorrect; atmospheric turbulence is external seeing."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-011": ("In a Newtonian telescope, the eyepiece is located on the side of the telescope tube near the top open aperture.", {
        "A": "The eyepiece is positioned on the side of the tube near the open front end.",
        "B": "Incorrect; behind the primary mirror describes the Cassegrain configuration.",
        "C": "Incorrect; inside the tube would block the light path.",
        "D": "Incorrect; directly on the primary mirror would obstruct the mirror."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-012": ("The primary mirror of a Cassegrain telescope has a hole drilled through its center to allow reflected light to reach the eyepiece behind it.", {
        "A": "The primary mirror has a central hole allowing light reflected by the secondary mirror to reach instruments behind it.",
        "B": "Incorrect; Newtonian primary mirrors do not have central holes.",
        "C": "Incorrect; Keplerian lenses do not have holes.",
        "D": "Incorrect; Galilean lenses do not have holes."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-013": ("Reflecting telescopes fold the optical path between primary and secondary mirrors, allowing a long effective focal length inside a compact tube.", {
        "A": "Folding the optical path allows a long focal length and high magnification within a short, rigid tube.",
        "B": "Incorrect; folding does not eliminate the need for an eyepiece.",
        "C": "Incorrect; folding does not reduce the mirror aperture.",
        "D": "Incorrect; folding does not make the telescope heavier."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-014": ("The Hubble Space Telescope utilizes a Ritchey-Chrétien Cassegrain reflecting design with a 2.4-meter primary mirror.", {
        "A": "The Hubble Space Telescope is a Cassegrain reflecting telescope with a 2.4-meter primary mirror.",
        "B": "Incorrect; Hubble is not a refractor.",
        "C": "Incorrect; Hubble is not a Newtonian reflector.",
        "D": "Incorrect; Hubble is not a radio telescope."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-015": ("The Keck telescopes in Hawaii use segmented primary mirrors consisting of 36 hexagonal mirror tiles acting as a single 10-meter mirror.", {
        "A": "The Keck telescopes use 36 hexagonal segmented mirror tiles to form a 10-meter primary mirror.",
        "B": "Incorrect; they do not use a single monolithic glass lens.",
        "C": "Incorrect; they do not use liquid mercury exclusively.",
        "D": "Incorrect; they are optical and infrared, not radio dishes."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-016": ("A flat plane mirror reflects starlight without changing the convergence or focal distance of the ray cone.", {
        "A": "A flat plane mirror redirects the light beam without introducing optical power or altering focal length.",
        "B": "Incorrect; convex mirrors diverge light.",
        "C": "Incorrect; concave mirrors converge light.",
        "D": "Incorrect; cylindrical mirrors introduce astigmatism."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-017": ("In a reflecting telescope, starlight does not pass through the glass body of the mirror, meaning the glass substrate does not need optical homogeneity.", {
        "A": "The glass only serves as a mechanical support for the reflective coating; internal bubbles or color do not affect image quality.",
        "B": "Incorrect; glass purity is critical for refracting lenses.",
        "C": "Incorrect; mirrors must still have an accurate surface figure.",
        "D": "Incorrect; thermal expansion must still be controlled."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-018": ("The angle of incidence of the flat secondary mirror in a Newtonian telescope relative to the primary axis is 45 degrees.", {
        "A": "The flat secondary mirror is positioned at 45 degrees to divert the beam by 90 degrees.",
        "B": "Incorrect; 30 degrees would deflect light at an inconvenient 60-degree angle.",
        "C": "Incorrect; 60 degrees would deflect light backward.",
        "D": "Incorrect; 90 degrees would reflect light directly back into the tube."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-019": ("The primary concave mirror of a reflecting telescope forms a real, inverted image at its focal plane.", {
        "A": "The primary concave mirror forms a real, inverted image of distant celestial objects.",
        "B": "Incorrect; concave mirrors form virtual images only when the object is within the focal distance.",
        "C": "Incorrect; starlight originates from infinity, forming a real image at the focus.",
        "D": "Incorrect; a dispersed rainbow is chromatic dispersion."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-020": ("Astronomical primary mirrors are coated on the front surface with an ultra-thin layer of aluminum and protective silicon dioxide.", {
        "A": "Aluminum vapor deposition creates a front-surface reflective coating with high reflectivity across optical and UV bands.",
        "B": "Incorrect; copper oxidizes and has poor blue reflectivity.",
        "C": "Incorrect; lead is toxic and poorly reflective.",
        "D": "Incorrect; iron rusts and has poor reflectivity."
    }),
    "MH-9-SCIT-18-18.2.2-OSC-021": ("The primary mirror in an astronomical telescope collects starlight; a larger diameter enables the telescope to see fainter stars with higher resolution.", {
        "A": "A larger primary mirror collects more light and provides higher angular resolution according to Rayleigh's criterion (\\(\\theta \\propto \\lambda / D\\)).",
        "B": "Incorrect; mirror diameter does not change the speed of light.",
        "C": "Incorrect; mirror diameter does not increase atmospheric turbulence.",
        "D": "Incorrect; mirror diameter does not alter the star's actual distance."
    })
}

# 9 OMC 18.2.2
t2_omc_18_2_2 = {
    "MH-9-SCIT-18-18.2.2-OMC-001": ("Reflecting telescopes avoid chromatic aberration, can be solidly supported across their entire rear face, and avoid internal glass absorption.", {
        "They do not suffer from chromatic aberration.": "Correct; reflection angles are independent of wavelength.",
        "Large mirrors can be supported from behind, preventing sagging under their own weight.": "Correct; full back support enables apertures of 8 to 10+ meters.",
        "Light does not pass through the glass body of the primary mirror, avoiding internal absorption.": "Correct; reflection occurs strictly at the front aluminum surface.",
        "They are completely unaffected by Earth's atmosphere when operated from the ground.": "Incorrect; ground reflectors still suffer from atmospheric seeing."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-002": ("A Newtonian reflecting telescope consists of a primary parabolic concave mirror, a small flat secondary mirror at 45 degrees, and an eyepiece.", {
        "A primary parabolic concave mirror": "Correct; gathers starlight and focuses it toward the front.",
        "A small flat diagonal secondary mirror": "Correct; redirects light 90 degrees out through the tube side.",
        "An eyepiece lens": "Correct; magnifies the intermediate real image for the observer.",
        "A large convex glass objective lens": "Incorrect; convex objective lenses are used in refracting telescopes."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-003": ("A Cassegrain reflecting telescope features a concave primary mirror with a central hole, a convex secondary mirror, and an eyepiece mounted behind the primary.", {
        "A concave primary mirror with a hole in its center": "Correct; allows light to exit through the back of the telescope.",
        "A secondary convex mirror": "Correct; reflects light back through the hole in the primary mirror.",
        "An eyepiece located behind the primary mirror": "Correct; allows convenient rear mounting of heavy instruments.",
        "A large flat plane mirror mounted at a 45-degree angle": "Incorrect; 45-degree flat mirrors are used in Newtonian telescopes."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-004": ("Parabolic mirrors focus all rays parallel to their axis to a single focus, eliminating spherical aberration without chromatic aberration.", {
        "They eliminate spherical aberration for parallel on-axis light rays.": "Correct; parabolic geometry brings all parallel rays to a single focal point.",
        "They bring all colors of light to the same focus without chromatic dispersion.": "Correct; mirrors reflect all wavelengths identically.",
        "They allow sharper astronomical images than spherical mirrors of the same size.": "Correct; avoidance of spherical aberration yields point-like star images.",
        "They allow starlight to pass through the mirror without reflection.": "Incorrect; starlight reflects off the front surface."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-005": ("Newtonian telescopes have the eyepiece on the side near the open front, whereas Cassegrain telescopes place the eyepiece behind the primary mirror.", {
        "Newtonian telescopes use a flat secondary mirror, while Cassegrain telescopes use a curved convex secondary mirror.": "Correct; flat diagonal in Newtonian vs convex in Cassegrain.",
        "In a Newtonian telescope, the eyepiece is on the side of the tube; in a Cassegrain, it is behind the primary mirror.": "Correct; side viewing vs rear viewing.",
        "Cassegrain telescopes provide a more compact tube length for the same focal length.": "Correct; folded optical path shortens the physical tube.",
        "Newtonian telescopes suffer from severe chromatic aberration, while Cassegrain telescopes do not.": "Incorrect; both are reflectors and completely free of chromatic aberration."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-006": ("Modern research telescopes use reflecting optics, active computer actuators, front-surface aluminum coatings, and segmented mirrors.", {
        "Primary mirrors are coated on the front surface with a reflective metallic layer.": "Correct; aluminum deposition provides high optical reflectivity.",
        "Active optics and computer-controlled actuators maintain ideal mirror curvature.": "Correct; actuators continuously correct for gravitational and thermal sag.",
        "Many giant telescopes use segmented hexagonal mirrors aligned precisely as one mirror.": "Correct; Keck, TMT, and ELT use segmented architectures.",
        "They use thick convex glass objective lenses to collect the initial starlight.": "Incorrect; giant telescopes use reflective primary mirrors, not lenses."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-007": ("Reflecting telescopes are used in giant mountaintop observatories, space telescopes (Hubble, JWST), and amateur astronomical photography.", {
        "Giant mountaintop observatories (e.g., Keck, Subaru, VLT)": "Correct; all 8-10 meter ground telescopes are reflectors.",
        "Space telescopes like the Hubble Space Telescope and James Webb Space Telescope": "Correct; Hubble (2.4 m) and JWST (6.5 m) are Cassegrain-style reflectors.",
        "Amateur deep-sky astrophotography (Dobsonian and Newtonian setups)": "Correct; Dobsonians are popular, affordable large-aperture Newtonian reflectors.",
        "Simple handheld pocket magnifying glasses": "Incorrect; magnifying glasses are simple convex lenses."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-008": ("Primary mirrors in reflecting telescopes can be made from low-expansion glass-ceramics (Zerodur, Pyrex) because internal optical purity is not required.", {
        "The glass substrate needs to have low thermal expansion to maintain shape during temperature changes.": "Correct; Zerodur and Pyrex minimize thermal focus drift.",
        "The glass substrate does not require internal optical clarity since light does not travel through it.": "Correct; internal bubbles or opacity do not impair front-surface reflection.",
        "The mirror surface must be polished to extreme precision (fractions of a wavelength of light).": "Correct; optical surface accuracy must be within \\(\\lambda / 10\\).",
        "The mirror must be made of transparent diamond to refract starlight properly.": "Incorrect; primary mirrors reflect light, they do not refract through diamond."
    }),
    "MH-9-SCIT-18-18.2.2-OMC-009": ("Reflecting telescopes offer several advantages: no chromatic aberration, structural back support, front reflection, and compact folded tubes.", {
        "Elimination of chromatic aberration": "Correct; reflection angles are independent of wavelength.",
        "Ability to support giant mirrors firmly across the entire back surface": "Correct; avoids the rim-sagging limitation of heavy lenses.",
        "Compact tube construction through folded optical paths (Cassegrain)": "Correct; reduces observatory dome size and cost.",
        "Automatic elimination of atmospheric turbulence and starlight twinkling": "Incorrect; ground-based reflectors still suffer from atmospheric seeing."
    })
}

# Process all 100 questions in t2_qs
for q in t2_qs:
    code = q['code']
    qtype = q['type']
    
    # 18.2.1
    if '-18.2.1' in code:
        if qtype == 'OAR' and code in t2_oar_18_2_1:
            concept, a_exp, r_exp, correct_let = t2_oar_18_2_1[code]
            solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical optical principles."""
        elif qtype == 'OTF' and code in t2_otf_18_2_1:
            concept, truth_val, rationale = t2_otf_18_2_1[code]
            correct_choice = "A" if truth_val else "B"
            truth_str = "True" if truth_val else "False"
            solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""
        elif qtype == 'OSC' and code in t2_osc_18_2_1:
            concept, opt_reasons = t2_osc_18_2_1[code]
            correct_ans = q.get('ca')
            options = q.get('options', [])
            corr_idx = -1
            for i, opt in enumerate(options):
                if opt == correct_ans or (len(str(correct_ans)) == 1 and chr(65+i) == str(correct_ans)):
                    corr_idx = i
                    break
            if corr_idx == -1 and correct_ans in ['A', 'B', 'C', 'D']:
                corr_idx = ord(correct_ans) - 65
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (i == corr_idx)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(letter, "Evaluated based on optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
        elif qtype == 'OMC' and code in t2_omc_18_2_1:
            concept, opt_reasons = t2_omc_18_2_1[code]
            correct_list = q.get('cas', [])
            options = q.get('options', [])
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (opt in correct_list)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(opt, "Evaluated based on optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

    # 18.2.2
    elif '-18.2.2' in code:
        if qtype == 'OAR' and code in t2_oar_18_2_2:
            concept, a_exp, r_exp, correct_let = t2_oar_18_2_2[code]
            solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical optical principles."""
        elif qtype == 'OTF' and code in t2_otf_18_2_2:
            concept, truth_val, rationale = t2_otf_18_2_2[code]
            correct_choice = "A" if truth_val else "B"
            truth_str = "True" if truth_val else "False"
            solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""
        elif qtype == 'OSC' and code in t2_osc_18_2_2:
            concept, opt_reasons = t2_osc_18_2_2[code]
            correct_ans = q.get('ca')
            options = q.get('options', [])
            corr_idx = -1
            for i, opt in enumerate(options):
                if opt == correct_ans or (len(str(correct_ans)) == 1 and chr(65+i) == str(correct_ans)):
                    corr_idx = i
                    break
            if corr_idx == -1 and correct_ans in ['A', 'B', 'C', 'D']:
                corr_idx = ord(correct_ans) - 65
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (i == corr_idx)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(letter, "Evaluated based on optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
        elif qtype == 'OMC' and code in t2_omc_18_2_2:
            concept, opt_reasons = t2_omc_18_2_2[code]
            correct_list = q.get('cas', [])
            options = q.get('options', [])
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (opt in correct_list)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(opt, "Evaluated based on optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

print(f"Generated {len(solutions)} / {len(t2_qs)} solutions for Topics 18.2.1 and 18.2.2.")

with open('scripts/ch18_t2_solutions.json', 'w', encoding='utf-8') as f:
    json.dump(solutions, f, indent=2)
print("Saved scripts/ch18_t2_solutions.json")
