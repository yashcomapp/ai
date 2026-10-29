# -*- coding: utf-8 -*-
"""
Chapter 18 Topic 18.1.1 Solution Generator (87 Questions)
Class 9 Science & Technology: Observing Space: Telescopes
Forms of Light, Electromagnetic Spectrum, and Atmospheric Transmission
"""

import json
import re

# Load raw questions
with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

t1_qs = [q for q in all_qs if '-18.1.1' in q['questionCode']]

solutions = {}

# --- 16 OAR QUESTIONS ---
oar_data = {
    "MH-9-SCIT-18-18.1.1-OAR-001": ("""Earth's atmosphere has an optical transmission window that allows visible light wavelengths (400–800 nm) to penetrate with minimal absorption, making ground-based optical astronomy possible.""",
        "True — Optical telescopes can operate effectively on the Earth's surface because visible wavelengths pass freely through the atmosphere.",
        "True — Nitrogen and oxygen molecules in the atmosphere do not absorb visible light frequencies, providing a clear optical window.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-002": ("""Gamma rays have extremely short wavelengths (< 0.001 nm) and high photon energy, causing them to interact with atmospheric gas molecules and be completely absorbed in the upper atmosphere.""",
        "True — High-energy gamma ray photons cannot reach the Earth's surface, so ground-based direct gamma observatories are impossible.",
        "True — The atmosphere is completely opaque to gamma radiation due to Compton scattering and pair production in upper atmospheric layers.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-003": ("""Radio waves have long wavelengths (millimeters to meters) that easily diffract around and pass through cloud droplets and atmospheric moisture without significant scattering or absorption.""",
        "True — Radio telescopes can operate continuously during cloudy weather and daytime without interference from sunlight glare.",
        "True — Cloud water droplets are vastly smaller than radio wavelengths, producing negligible scattering, and solar optical glare does not affect radio frequencies.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-004": ("""Space telescopes orbit outside the Earth's atmosphere, completely avoiding atmospheric scintillation (twinkling), air currents, light pollution, and atmospheric absorption.""",
        "True — Telescopes in space capture significantly sharper images because wavefronts are not degraded by air turbulence.",
        "True — Operating in a vacuum eliminates all atmospheric distortion, weather interruptions, and light pollution.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-005": ("""Celestial bodies emit electromagnetic radiation across multiple bands (from radio waves to gamma rays) depending on their surface temperatures, magnetic fields, and nuclear processes.""",
        "True — Stars and galaxies are multi-wavelength emitters whose radiation spans the entire electromagnetic spectrum.",
        "True — Thermal radiation, nuclear fusion, relativistic accretion disks, and synchrotron emissions produce photons across diverse energy bands.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-006": ("""Rayleigh scattering of sunlight by atmospheric gas molecules creates bright diffuse sky luminance that overpowers the faint light of distant celestial bodies during daytime.""",
        "True — Optical telescopes cannot observe faint starlight during the daytime from the Earth's surface.",
        "True — Rayleigh scattering of blue wavelengths illuminates the atmosphere, completely drowning out faint starlight.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-007": ("""The stratospheric ozone (\\(\\ce{O3}\\)) layer absorbs solar and stellar ultraviolet radiation (wavelengths below 310 nm), necessitating space telescopes for UV astronomy.""",
        "True — Ultraviolet astronomy must be conducted from orbital space platforms because celestial UV rays cannot reach the ground.",
        "True — Photodissociation of ozone molecules effectively shields Earth's surface by absorbing high-energy UV-B and UV-C wavelengths.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-008": ("""The electromagnetic spectrum is arranged continuously by wavelength; radio waves occupy the longest wavelengths (meters to kilometers), whereas visible light is restricted to 400–800 nm.""",
        "True — Radio waves possess significantly longer wavelengths than visible light waves.",
        "True — Astronomical radio wavelengths span from millimeters up to hundreds of meters, far exceeding the sub-micron scale of visible light.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-009": ("""Liquid water droplets in dense clouds reflect and scatter optical photons (Mie scattering), making Earth's atmosphere opaque to visible light during overcast weather.""",
        "True — Cloudy and overcast skies obstruct optical telescope observations from the surface of the Earth.",
        "True — Cloud water droplets randomly scatter and attenuate visible light waves, preventing starlight from reaching ground instruments.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-010": ("""Multi-wavelength astronomy combines data across all electromagnetic bands (radio to gamma rays) to construct complete physical models of celestial structures and energetic events.""",
        "True — Multi-wavelength observations reveal physical phenomena that are completely invisible in optical frequencies alone.",
        "True — Cold interstellar gas emits in radio/IR, warm stellar photospheres emit in visible light, and high-energy accretion discs emit in X-rays/gamma rays.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-011": ("""Because radio wavelengths are thousands of times longer than optical wavelengths, the surface tolerance required for radio dishes is on the order of millimeters rather than nanometers.""",
        "True — Ground radio telescope dishes can be constructed with diameters exceeding 45–100 meters, far larger than optical mirror diameters.",
        "True — Rayleigh's criterion requires surface precision of \\(\\sim \\lambda / 16\\); larger wavelengths permit coarser mechanical tolerances.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-012": ("""Earth's atmospheric column provides an effective radiation barrier equivalent to 10 meters of water, shielding terrestrial life while requiring space satellites for high-energy astrophysics.""",
        "True — High-energy X-ray and gamma-ray astronomy was impossible before orbital space observatories were launched.",
        "True — The Earth's atmospheric mass completely blocks and absorbs cosmic X-rays and gamma rays.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-013": ("""Atmospheric dust and rain particles have sizes comparable to optical wavelengths (causing scattering), but are vastly smaller than radio wavelengths, which pass through unhindered.""",
        "True — Radio telescopes can observe celestial targets through rain, fog, and interstellar dust clouds.",
        "True — When wavelength is much larger than particle diameter (\\(\\lambda \\gg d\\)), scattering is negligible.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-014": ("""According to Wien's displacement law (\\(\\lambda_{\\text{max}} T = b\\)), the peak emission wavelength of a star's thermal spectrum is inversely proportional to its surface temperature.""",
        "True — Hot stars (\\(\\sim 30{,}000\\text{ K}\\)) appear blue/UV, while cooler stars (\\(\\sim 3{,}000\\text{ K}\\)) appear reddish/IR.",
        "True — Increasing thermal temperature shifts the blackbody emission curve toward shorter, higher-energy wavelengths.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-015": ("""Directly observing the Sun through an unfiltered optical telescope focuses intense concentrated solar flux onto the retina, causing instantaneous and irreversible blindness.""",
        "False — Viewing the Sun through an optical telescope without specialized solar filters is extremely dangerous and strictly prohibited.",
        "True — Concentrated solar visible and infrared radiation causes thermal and photochemical retinal burns.",
        "D"),
    "MH-9-SCIT-18-18.1.1-OAR-016": ("""Positioning observatories on high mountaintops places them above the densest, most humid, and turbulent lower atmospheric layers, reducing optical distortion and seeing blur.""",
        "True — High-altitude observatories (e.g. Mauna Kea, Hanle Ladakh) achieve superior resolution and optical transparency.",
        "True — High elevation avoids lower atmospheric water vapor, clouds, and thermal turbulence cells.",
        "A")
}

for code, (concept, a_exp, r_exp, correct_let) in oar_data.items():
    solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical optical and atmospheric principles."""

# --- 18 OTF QUESTIONS ---
otf_data = {
    "MH-9-SCIT-18-18.1.1-OTF-001": ("All electromagnetic waves travel at the speed of light in vacuum, \\(c = 3 \\times 10^8\\text{ m/s}\\).",
        True, "In a vacuum, all electromagnetic radiation—from radio waves to gamma rays—propagates at the identical universal speed of light \\(c = 3 \\times 10^8\\text{ m/s}\\)."),
    "MH-9-SCIT-18-18.1.1-OTF-002": ("Earth's atmosphere absorbs cosmic X-rays completely, preventing them from reaching ground-level telescopes.",
        True, "Nitrogen, oxygen, and other atmospheric gases absorb X-rays through photoelectric absorption, making space-based satellites mandatory for X-ray astronomy."),
    "MH-9-SCIT-18-18.1.1-OTF-003": ("Infrared radiation spans wavelengths longer than visible light (\\(> 800\\text{ nm}\\)) and is perceived as thermal heat.",
        True, "Infrared rays have wavelengths from \\(800\\text{ nm}\\) to \\(1\\text{ mm}\\) and are emitted by warm objects as thermal radiation."),
    "MH-9-SCIT-18-18.1.1-OTF-004": ("Photon energy is inversely proportional to wavelength (\\(E = hc/\\lambda\\)), so shorter UV rays possess higher energy than longer IR rays.",
        True, "Ultraviolet radiation has wavelengths between \\(10\\text{ nm}\\) and \\(400\\text{ nm}\\), giving UV photons substantially higher frequencies and energy than infrared photons (\\(800\\text{ nm} - 1\\text{ mm}\\))."),
    "MH-9-SCIT-18-18.1.1-OTF-005": ("In the visible spectrum (\\(400-800\\text{ nm}\\)), green light has a shorter wavelength (\\(\\sim 520\\text{ nm}\\)) than red light (\\(\\sim 700\\text{ nm}\\)).",
        True, "Across the visible spectrum (VIBGYOR), wavelength increases from violet (\\(\\sim 400\\text{ nm}\\)) to red (\\(\\sim 700\\text{ nm}\\)), meaning green light has a shorter wavelength than red light."),
    "MH-9-SCIT-18-18.1.1-OTF-006": ("In the electromagnetic spectrum, microwaves have shorter wavelengths and higher frequencies than radio waves.",
        False, "Radio waves possess the lowest frequencies and longest wavelengths in the electromagnetic spectrum; microwaves have higher frequencies than radio waves."),
    "MH-9-SCIT-18-18.1.1-OTF-007": ("Earth's atmosphere acts as a protective shield absorbing ionizing cosmic radiation (gamma rays, X-rays, and far UV).",
        True, "The upper atmospheric layers absorb lethal high-energy ionizing photons (UV-C, X-rays, gamma rays), protecting terrestrial living organisms."),
    "MH-9-SCIT-18-18.1.1-OTF-008": ("Radio waves penetrate clouds and are unaffected by daylight solar glare, allowing 24-hour operation.",
        True, "Because solar glare is predominantly optical and radio waves pass through clouds without scattering, radio telescopes operate seamlessly day and night."),
    "MH-9-SCIT-18-18.1.1-OTF-009": ("Infrared detectors must be cryogenically cooled to prevent thermal emission from the instrument itself from blinding the sensor.",
        True, "Any object at room temperature radiates ambient infrared thermal noise; cooling telescope instruments with liquid helium/nitrogen eliminates background thermal glow."),
    "MH-9-SCIT-18-18.1.1-OTF-010": ("Visible light constitutes an extremely narrow fraction of the total electromagnetic spectrum (only 400 to 800 nm).",
        False, "Visible light spans only \\(400-800\\text{ nm}\\), representing a microscopic fraction of the continuous electromagnetic spectrum that extends across dozens of orders of magnitude."),
    "MH-9-SCIT-18-18.1.1-OTF-011": ("The stratospheric ozone layer absorbs UV radiation below 310 nm, meaning the atmosphere is not completely transparent to UV.",
        False, "Earth's atmosphere absorbs almost all UV-C and most UV-B radiation via the ozone layer, allowing only a small window of near-UV (UV-A) to reach the ground."),
    "MH-9-SCIT-18-18.1.1-OTF-012": ("Electromagnetic waves (including radio waves) are transverse waves composed of oscillating electric and magnetic fields requiring no medium.",
        True, "Radio waves propagate freely across the vacuum of interstellar space without requiring any material medium, as mutually perpendicular electric and magnetic vectors."),
    "MH-9-SCIT-18-18.1.1-OTF-013": ("In a vacuum, all electromagnetic waves travel at the identical speed \\(c = 3 \\times 10^8\\text{ m/s}\\) regardless of frequency.",
        False, "Ultraviolet radiation and radio waves propagate at the exact same invariant speed of light in a vacuum (\\(c = 3 \\times 10^8\\text{ m/s}\\))."),
    "MH-9-SCIT-18-18.1.1-OTF-014": ("Cool celestial objects (planets, interstellar dust, protostars) radiate primarily in the infrared band according to Wien's law.",
        True, "Cool cosmic gas and dust clouds (temperatures from \\(10\\text{ K}\\) to a few hundred Kelvin) emit thermal radiation peaking in the infrared region."),
    "MH-9-SCIT-18-18.1.1-OTF-015": ("Optical telescopes collect visible light photons using lenses or mirrors, whereas radio telescopes collect radio waves using metal antennas.",
        False, "Optical telescopes detect visible light (wavelengths \\(400-800\\text{ nm}\\)); radio waves are collected by radio telescopes using parabolic dish reflectors and receivers."),
    "MH-9-SCIT-18-18.1.1-OTF-016": ("The electromagnetic spectrum comprises seven distinct bands: radio, microwave, infrared, visible, ultraviolet, X-ray, and gamma-ray.",
        False, "The electromagnetic spectrum includes radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, and gamma rays."),
    "MH-9-SCIT-18-18.1.1-OTF-017": ("Gamma rays have the shortest wavelengths (< 0.001 nm) and highest photon frequencies in the electromagnetic spectrum.",
        False, "Gamma rays have the shortest wavelengths and highest frequencies in the entire electromagnetic spectrum, whereas optical telescopes observe much longer wavelengths (\\(400-800\\text{ nm}\\))."),
    "MH-9-SCIT-18-18.1.1-OTF-018": ("In the electromagnetic spectrum, X-rays have shorter wavelengths (0.01–10 nm) than ultraviolet radiation (10–400 nm).",
        False, "X-rays possess higher energy and shorter wavelengths (\\(0.01-10\\text{ nm}\\)) than ultraviolet rays (\\(10-400\\text{ nm}\\)).")
}

for q in t1_qs:
    code = q['questionCode']
    if q['type'] == 'OTF' and code in otf_data:
        concept, truth_val, rationale = otf_data[code]
        correct_choice = "A" if truth_val else "B"
        truth_str = "True" if truth_val else "False"
        solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""

# --- 36 OSC QUESTIONS ---
osc_data = {
    "MH-9-SCIT-18-18.1.1-OSC-001": ("Human photoreceptors in the retina are sensitive only to visible light wavelengths spanning approximately 400 nm (violet) to 800 nm (red).", {
        "A": "Incorrect; does not match the biological detection range.",
        "B": "Incorrect; infra-optical band.",
        "C": "Incorrect; radio wavelength range.",
        "D": "The visible spectrum detectable by the human eye spans from approximately \\(400\\text{ nm}\\) (violet) to \\(800\\text{ nm}\\) (red)."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-002": ("In the electromagnetic spectrum, wavelength is inversely proportional to frequency (\\(c = \\nu \\lambda\\)), making radio waves the longest.", {
        "A": "Radio waves have the longest wavelengths in the electromagnetic spectrum, ranging from millimeters to kilometers.",
        "B": "Incorrect; X-rays have short sub-nanometer wavelengths.",
        "C": "Incorrect; gamma rays have the shortest wavelengths in the spectrum.",
        "D": "Incorrect; ultraviolet wavelengths are much shorter than radio."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-003": ("Microwaves have wavelengths spanning from approximately 1 mm to 30 cm and are widely used in radar, satellite links, and microwave ovens.", {
        "A": "Incorrect; X-rays are used for medical radiography, not microwave ovens.",
        "B": "Microwaves (wavelengths \\(1\\text{ mm} - 30\\text{ cm}\\)) are used in radar and cooking due to water molecule absorption.",
        "C": "Incorrect; UV rays are ionizing and cause photochemical reactions.",
        "D": "Incorrect; gamma rays are high-energy nuclear emissions."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-004": ("Gamma rays are produced by nuclear reactions and cosmic cataclysms, possessing the highest frequencies (> 10^19 Hz) and greatest photon energy.", {
        "A": "Incorrect; radio waves have the lowest frequencies.",
        "B": "Incorrect; visible light has moderate frequencies (\\(\\sim 10^{14}\\text{ Hz}\\)).",
        "C": "Gamma rays possess the shortest wavelengths and the highest frequencies (and energy) in the electromagnetic spectrum.",
        "D": "Incorrect; infrared has frequencies below visible light."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-005": ("Radio astronomy uses parabolic dish reflectors and sensitive radio receivers to detect cosmic radio frequency emissions.", {
        "A": "Radio telescopes are designed with metallic dishes or antennas to collect and focus radio waves from space.",
        "B": "Incorrect; optical telescopes collect visible light photons.",
        "C": "Incorrect; electron microscopes use electron beams for microscopic imaging.",
        "D": "Incorrect; periscopes use flat mirrors for submarine line-of-sight."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-006": ("In order of decreasing wavelength, ultraviolet radiation lies directly between visible light (400–800 nm) and X-rays (0.01–10 nm).", {
        "A": "Incorrect; infrared lies on the longer wavelength side of visible light.",
        "B": "Ultraviolet (UV) radiation lies directly between visible light (violet end at \\(400\\text{ nm}\\)) and X-rays (\\(< 10\\text{ nm}\\)).",
        "C": "Incorrect; microwaves lie between radio and infrared.",
        "D": "Incorrect; gamma rays lie beyond X-rays at the extreme high-frequency end."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-007": ("High mountaintops place optical observatories above the thickest, dustiest atmospheric layers and far from city light pollution.", {
        "A": "Incorrect; mountain elevation does not alter gravity's effect on light.",
        "B": "Mountaintop observatories avoid urban light pollution and thick lower atmospheric dust and thermal turbulence.",
        "C": "Incorrect; temperature differences do not improve mirror quality.",
        "D": "Incorrect; distance to stars is negligible compared to interstellar distances."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-008": ("Electromagnetic waves are classified into distinct bands purely based on their physical wavelength and oscillation frequency (\\(c = \\nu \\lambda\\)).", {
        "A": "Wavelength and frequency fundamentally classify electromagnetic waves into radio, infrared, optical, UV, X-ray, and gamma-ray bands.",
        "B": "Incorrect; all EM waves propagate at the same speed \\(c\\) in vacuum.",
        "C": "Incorrect; brightness determines intensity, not spectral classification.",
        "D": "Incorrect; polarization describes vector orientation, not spectral category."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-009": ("X-rays and gamma rays are emitted during violent high-energy astrophysical events such as accretion onto black holes and supernova explosions.", {
        "A": "High-energy phenomena like supernova remnants, neutron stars, and black holes emit intense X-rays and gamma rays.",
        "B": "Incorrect; cool interstellar dust radiates primarily in the infrared.",
        "C": "Incorrect; planetary atmospheres radiate primarily in visible and infrared.",
        "D": "Incorrect; calm molecular clouds emit low-energy radio spectral lines."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-010": ("Warm dust grains and cool celestial bodies emit thermal blackbody radiation peaking in the infrared region (0.8–1000 µm).", {
        "A": "Incorrect; X-rays originate from million-degree gases.",
        "B": "Infrared telescopes are ideal for detecting cool dust clouds and protostellar nebulae that emit thermal radiation.",
        "C": "Incorrect; gamma rays are emitted in nuclear cataclysms.",
        "D": "Incorrect; UV rays are emitted by extremely hot young stars."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-011": ("The human visible spectrum terminates on the short-wavelength (high-frequency) violet side at approximately 400 nm (\\(4000\\text{ \\AA}\\)).", {
        "A": "The lower wavelength limit of the visible spectrum corresponds to violet light at approximately \\(400\\text{ nm}\\).",
        "B": "Incorrect; \\(100\\text{ nm}\\) is in the far ultraviolet region.",
        "C": "Incorrect; \\(800\\text{ nm}\\) is the upper limit (red end).",
        "D": "Incorrect; \\(1\\text{ nm}\\) is in the soft X-ray band."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-012": ("The cosmic microwave background (CMB), the relic thermal radiation from the Big Bang, has cooled to 2.73 K and peaks in the microwave spectrum.", {
        "A": "Incorrect; gamma rays are emitted by energetic localized sources.",
        "B": "Microwaves (millimeter to centimeter wavelengths) are used to study the Cosmic Microwave Background radiation from the early universe.",
        "C": "Incorrect; UV radiation does not represent relic cosmological radiation.",
        "D": "Incorrect; X-rays represent hot relativistic accretion phenomena."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-013": ("The Hubble Space Telescope (HST), launched in 1990 into low Earth orbit, observes celestial targets in optical, near-UV, and near-IR bands.", {
        "A": "The Hubble Space Telescope is the world's most famous orbital optical and ultraviolet observatory.",
        "B": "Incorrect; Chandra is dedicated exclusively to X-ray astronomy.",
        "C": "Incorrect; GMRT is a ground-based radio telescope array in Pune.",
        "D": "Incorrect; VLA is a ground-based radio array in New Mexico."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-014": ("Radio waves reflect off metallic conductors, allowing large parabolic metal mesh or sheet dishes to focus incoming radio waves onto an antenna receiver.", {
        "A": "Incorrect; glass convex lenses refract visible light, not radio waves.",
        "B": "A curved metallic parabolic dish focuses incoming radio waves onto a central receiver horn.",
        "C": "Incorrect; optical prisms disperse visible light, not radio.",
        "D": "Incorrect; flat wooden boards absorb or scatter radio waves."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-015": ("In the electromagnetic spectrum, infrared radiation has wavelengths spanning immediately longer than the red end of visible light (> 800 nm).", {
        "A": "Incorrect; ultraviolet has wavelengths shorter than violet light.",
        "B": "Infrared radiation occupies the wavelength band immediately longer than visible red light (\\(800\\text{ nm} - 1\\text{ mm}\\)).",
        "C": "Incorrect; X-rays have sub-nanometer wavelengths.",
        "D": "Incorrect; gamma rays have the shortest wavelengths."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-016": ("At higher altitudes, atmospheric pressure and density decrease, reducing light scattering, dust, and thermal turbulence.", {
        "A": "Thinner, cleaner air at mountain peaks reduces atmospheric scattering and seeing distortions.",
        "B": "Incorrect; mountain elevation does not alter celestial distances.",
        "C": "Incorrect; telescopes do not absorb more gravity on mountains.",
        "D": "Incorrect; clouds often gather below high mountain peaks, improving visibility."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-017": ("The development of liquid-fuel rocketry and orbital launch vehicles in the 20th century enabled humanity to place telescopes into space.", {
        "A": "The development of rocketry and artificial satellites allowed telescopes to orbit above Earth's atmosphere.",
        "B": "Incorrect; bronze age navigation predated modern telescopes by millennia.",
        "C": "Incorrect; incandescent bulbs contributed to urban light pollution.",
        "D": "Incorrect; steam locomotives did not launch orbital satellites."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-018": ("X-rays possess wavelengths ranging from 0.01 nm to 10 nm, which are shorter than ultraviolet radiation (10–400 nm).", {
        "A": "Incorrect; radio waves have the longest wavelengths.",
        "B": "X-rays have wavelengths shorter than ultraviolet radiation and longer than gamma rays.",
        "C": "Incorrect; microwaves have millimeter wavelengths.",
        "D": "Incorrect; infrared has wavelengths longer than visible light."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-019": ("The atmosphere's optical and radio windows allow visible light and certain radio frequencies to reach ground observatories.", {
        "A": "The optical window refers to the atmospheric transparency band that permits visible light to pass to the Earth's surface.",
        "B": "Incorrect; greenhouse effect refers to thermal heat trapping.",
        "C": "Incorrect; solar eclipse is the occultation of the Sun by the Moon.",
        "D": "Incorrect; Doppler effect describes frequency shifts due to relative motion."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-020": ("Earth's atmosphere is transparent to visible light but completely opaque to X-rays, requiring space satellites for X-ray observation.", {
        "A": "Visible light easily reaches ground telescopes through the optical window, while X-rays are completely absorbed and require space observatories.",
        "B": "Incorrect; neither can pass through solid planetary cores.",
        "C": "Incorrect; ground telescopes cannot detect celestial X-rays.",
        "D": "Incorrect; space telescopes can detect both bands."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-021": ("In increasing order of frequency (or decreasing order of wavelength), the sequence is: Radio waves -> Infrared -> Visible light -> X-rays.", {
        "A": "Radio waves have the lowest frequency, followed by infrared, visible light, and X-rays in increasing order of frequency.",
        "B": "Incorrect; inverted sequence.",
        "C": "Incorrect; visible light has higher frequency than infrared.",
        "D": "Incorrect; X-rays have far higher frequency than visible light."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-022": ("Cool astronomical bodies (temperatures below 1000 K) emit predominantly in the infrared band as thermal radiation.", {
        "A": "Incorrect; gamma-ray telescopes detect multi-million Kelvin violent reactions.",
        "B": "Infrared telescopes are specialized for observing cooler astronomical bodies like brown dwarfs and interstellar clouds.",
        "C": "Incorrect; X-ray telescopes observe ultra-hot plasmas.",
        "D": "Incorrect; UV telescopes detect hot O and B stars."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-023": ("Cosmic X-rays interact with nitrogen and oxygen atoms in the upper atmosphere via the photoelectric effect, being completely absorbed.", {
        "A": "Atmospheric gases absorb X-rays completely before they can reach the ground, requiring satellites in orbit.",
        "B": "Incorrect; mountain elevation does not bypass the absorbing atmospheric column.",
        "C": "Incorrect; zero gravity is not required for X-ray reflection.",
        "D": "Incorrect; X-ray telescopes can be compact."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-024": ("In the visible spectrum (VIBGYOR), violet light has the shortest wavelength (~400 nm) and consequently the highest frequency.", {
        "A": "Violet light has the shortest wavelength (\\(\\sim 400\\text{ nm}\\)) and highest frequency in the visible spectrum.",
        "B": "Incorrect; red light has the longest wavelength (\\(\\sim 700\\text{ nm}\\)).",
        "C": "Incorrect; yellow occupies an intermediate wavelength (\\(\\sim 580\\text{ nm}\\)).",
        "D": "Incorrect; green occupies an intermediate wavelength (\\(\\sim 530\\text{ nm}\\))."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-025": ("In the electromagnetic spectrum, infrared radiation bridges the gap between microwaves (shorter wavelength side of radio) and visible light.", {
        "A": "Incorrect; gamma rays lie beyond X-rays.",
        "B": "Infrared radiation is situated directly between microwaves and visible light.",
        "C": "Incorrect; ultraviolet lies between visible light and X-rays.",
        "D": "Incorrect; X-rays lie between UV and gamma rays."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-026": ("Gamma rays are emitted only by the most violent nuclear and relativistic processes, such as gamma-ray bursts (GRBs) and supernova collapse.", {
        "A": "Gamma-ray bursts, pulsars, and violent nuclear interactions in deep space produce gamma-ray emissions.",
        "B": "Incorrect; rocky planets emit thermal infrared.",
        "C": "Incorrect; main-sequence photospheres radiate mainly visible light.",
        "D": "Incorrect; cometary ice sublimation emits neutral gas molecules."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-027": ("Among radio, microwaves, infrared, and ultraviolet, ultraviolet radiation has the shortest wavelength (10–400 nm).", {
        "A": "Incorrect; radio waves have the longest wavelengths.",
        "B": "Incorrect; microwaves have millimeter wavelengths.",
        "C": "Incorrect; infrared has micrometer wavelengths.",
        "D": "Ultraviolet radiation has the shortest wavelength (\\(10-400\\text{ nm}\\)) among the listed options."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-028": ("Microwaves have wavelengths spanning from approximately 1 mm to 30 cm, bridging infrared and standard radio wavelengths.", {
        "A": "Microwaves typically span wavelengths from \\(1\\text{ mm}\\) to \\(30\\text{ cm}\\).",
        "B": "Incorrect; \\(400-800\\text{ nm}\\) is visible light.",
        "C": "Incorrect; kilometers are long-wave radio.",
        "D": "Incorrect; sub-nanometers are X-rays."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-029": ("Immediately above ultraviolet frequencies lie X-rays, with frequencies ranging from 30 petahertz to 30 exahertz.", {
        "A": "X-rays have frequencies immediately higher than ultraviolet radiation.",
        "B": "Incorrect; infrared has lower frequencies than visible light.",
        "C": "Incorrect; radio waves have the lowest frequencies.",
        "D": "Incorrect; microwaves have lower frequencies than infrared."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-030": ("Radio astronomy uses large curved parabolic metal antennas or dishes to reflect and focus long radio waves.", {
        "A": "Radio waves are focused using parabolic metal dish antennas.",
        "B": "Incorrect; X-rays pass through glass lenses instead of refracting.",
        "C": "Incorrect; gamma rays cannot be refracted by prisms.",
        "D": "Incorrect; infrared is not collected with wooden tubes."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-031": ("Interferometric arrays combine signals from widely separated radio dishes, simulating a giant telescope with resolution proportional to the baseline distance.", {
        "A": "Arraying radio telescopes across kilometers dramatically enhances angular resolution through synthetic aperture interferometry.",
        "B": "Incorrect; arrays do not change the weather.",
        "C": "Incorrect; arraying does not convert radio to visible light.",
        "D": "Incorrect; arraying does not decrease construction costs."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-032": ("Photon energy is governed by \\(E = h\\nu = hc/\\lambda\\); radio waves have the longest wavelengths and thus the lowest energy per photon.", {
        "A": "Radio waves possess the lowest frequencies and longest wavelengths, corresponding to the lowest energy per photon.",
        "B": "Incorrect; visible light has higher energy photons.",
        "C": "Incorrect; X-rays carry high photon energies.",
        "D": "Incorrect; gamma rays carry the highest photon energy."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-033": ("Variations in atmospheric temperature and air currents cause fluctuations in optical refractive index, making starlight twinkle (scintillation).", {
        "A": "Atmospheric turbulence and rapid refractive index changes cause stellar twinkling (scintillation).",
        "B": "Incorrect; stars emit steady light; the twinkling occurs inside Earth's atmosphere.",
        "C": "Incorrect; orbital motion does not cause twinkling.",
        "D": "Incorrect; lunar gravity does not flicker starlight."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-034": ("The long-wavelength boundary of the visible spectrum corresponds to red light at approximately 800 nm (\\(8000\\text{ \\AA}\\)).", {
        "A": "The upper limit of the human visible wavelength spectrum is approximately \\(800\\text{ nm}\\) (red light).",
        "B": "Incorrect; \\(400\\text{ nm}\\) is the violet lower limit.",
        "C": "Incorrect; \\(1\\text{ cm}\\) is in the microwave band.",
        "D": "Incorrect; \\(1\\text{ m}\\) is in the radio band."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-035": ("The Giant Metrewave Radio Telescope (GMRT), located at Narayangaon near Pune, operates 30 parabolic dishes of 45 m diameter for radio astronomy.", {
        "A": "GMRT near Pune is India's world-renowned low-frequency radio observatory.",
        "B": "Incorrect; Hubble is an American/European orbital telescope.",
        "C": "Incorrect; Chandra is a NASA X-ray space telescope.",
        "D": "Incorrect; Keck is an optical observatory in Hawaii."
    }),
    "MH-9-SCIT-18-18.1.1-OSC-036": ("Warm bodies around 300 K emit peak thermal radiation in the infrared band (~10 µm) in accordance with Planck's radiation law.", {
        "A": "Warm bodies (such as humans and room-temperature matter) emit peak blackbody radiation in the infrared spectrum.",
        "B": "Incorrect; X-rays require million-degree temperatures.",
        "C": "Incorrect; gamma rays require nuclear reactions.",
        "D": "Incorrect; UV requires high-temperature stellar photospheres."
    })
}

# Map OSC answers correctly
for q in t1_qs:
    code = q['questionCode']
    if q['type'] == 'OSC' and code in osc_data:
        concept, opt_reasons = osc_data[code]
        correct_ans = q.get('correctAnswer')
        options = q.get('options', [])
        
        # Match correct answer
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
            reason = opt_reasons.get(letter, "Evaluated based on physical principles.")
            lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")

        solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

# --- 17 OMC QUESTIONS ---
omc_data = {
    "MH-9-SCIT-18-18.1.1-OMC-001": ("Electromagnetic radiations with wavelengths shorter than visible light (400 nm) include ultraviolet rays, X-rays, and gamma rays.", {
        "Ultraviolet rays": "Correct; UV wavelengths (\\(10-400\\text{ nm}\\)) are shorter than visible light.",
        "X-rays": "Correct; X-ray wavelengths (\\(0.01-10\\text{ nm}\\)) are much shorter than visible light.",
        "Gamma rays": "Correct; gamma rays have the shortest wavelengths in the entire spectrum.",
        "Radio waves": "Incorrect; radio waves have the longest wavelengths, far longer than visible light."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-002": ("Radio waves have low frequencies, penetrate Earth's atmosphere easily, and are unaffected by daylight, allowing continuous observation.", {
        "They have frequencies lower than infrared waves.": "Correct; radio waves occupy the lowest frequency band in the spectrum.",
        "They can pass through Earth's atmosphere easily.": "Correct; the atmospheric radio window transmits radio waves freely to the ground.",
        "They are used to study celestial objects day and night.": "Correct; radio telescopes are immune to daylight solar glare and cloud cover.",
        "They have shorter wavelengths than gamma rays.": "Incorrect; radio waves have the longest wavelengths, not shorter than gamma rays."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-003": ("Earth's atmosphere features two primary transmission windows: the optical window (visible light) and the radio window.", {
        "Visible light": "Correct; passes directly through the optical window to ground telescopes.",
        "Radio waves": "Correct; passes directly through the radio window to ground dishes.",
        "X-rays": "Incorrect; completely absorbed by nitrogen and oxygen in the upper atmosphere.",
        "Gamma rays": "Incorrect; completely absorbed by atmospheric gas molecules."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-004": ("All electromagnetic waves propagate at the invariant speed of light in vacuum, consist of oscillating orthogonal electric and magnetic fields, and transport energy.", {
        "They travel at the speed of light in a vacuum.": "Correct; all EM radiation travels at \\(c = 3 \\times 10^8\\text{ m/s}\\) in vacuum.",
        "They consist of oscillating electric and magnetic fields.": "Correct; EM waves are coupled transverse oscillations of electric and magnetic vectors.",
        "They carry energy through space.": "Correct; electromagnetic waves transport radiant energy and momentum.",
        "They require a physical medium to travel through.": "Incorrect; EM waves propagate freely through vacuum without any medium."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-005": ("High-energy ionizing radiation (X-rays, gamma rays, and ultraviolet) is absorbed by the atmosphere and requires orbital space observatories.", {
        "X-rays": "Correct; absorbed by atmospheric nitrogen and oxygen; requires satellites like Chandra.",
        "Gamma rays": "Correct; absorbed in the stratosphere and mesosphere; requires space observatories.",
        "Ultraviolet rays": "Correct; absorbed predominantly by stratospheric ozone; requires space telescopes.",
        "Radio waves": "Incorrect; radio waves reach the ground freely through the atmospheric radio window."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-006": ("Multi-wavelength astrophysics uses different instruments to observe phenomena spanning low-energy radio gas to ultra-hot stars emitting UV.", {
        "Different celestial objects emit different types of electromagnetic waves depending on their temperature and physical processes.": "Correct; radiation peaks correspond to physical temperatures and emission mechanisms.",
        "Radio telescopes can be linked together to form giant interferometers.": "Correct; synthetic aperture interferometry combines multiple dishes to achieve high resolution.",
        "Ultraviolet astronomy helps study young, hot stars.": "Correct; massive O and B stars emit peak radiation in ultraviolet wavelengths.",
        "Ground-based telescopes can detect all wavelengths of the electromagnetic spectrum equally well.": "Incorrect; the atmosphere blocks gamma rays, X-rays, and far UV."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-007": ("Ionizing radiation carries sufficient photon energy to liberate electrons from atoms, encompassing high-energy UV, X-rays, and gamma rays.", {
        "X-rays": "Correct; X-ray photons possess high energy (\\(100\\text{ eV} - 100\\text{ keV}\\)) and readily ionize matter.",
        "Gamma rays": "Correct; gamma rays have megaelectronvolt energies and are strongly ionizing.",
        "Ultraviolet rays (higher energy bands)": "Correct; UV-C and extreme UV have sufficient energy to ionize atoms and break molecular bonds.",
        "Radio waves": "Incorrect; radio photons carry negligible energy (micro-eV) and cannot cause ionization."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-008": ("Space telescopes operate outside Earth's atmosphere, avoiding weather, scintillation blurring, and atmospheric absorption of UV and X-rays.", {
        "They are unaffected by weather, clouds, or atmospheric turbulence.": "Correct; vacuum orbit guarantees continuous, diffraction-limited clarity.",
        "They can detect wavelengths like X-rays and UV that are blocked by the atmosphere.": "Correct; orbital location permits full-spectrum astronomical observation.",
        "They have an unobstructed view of the night sky 24 hours a day for polar-orbiting satellites.": "Incorrect; orbital geometry and Earth/Sun occultation require scheduling constraints.",
        "They are much cheaper and easier to maintain than ground telescopes.": "Incorrect; space missions cost billions and are exceedingly difficult or impossible to service."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-009": ("Radio observatories detect meter and centimeter wavelength cosmic emissions using parabolic dishes or antenna arrays.", {
        "Giant Metrewave Radio Telescope (GMRT) in India": "Correct; premier 30-dish radio interferometer located in Pune, India.",
        "Very Large Array (VLA)": "Correct; world-famous radio telescope array located in New Mexico, USA.",
        "Chandra X-ray Observatory": "Incorrect; Chandra is a space-based X-ray telescope.",
        "Hubble Space Telescope": "Incorrect; Hubble is an optical, UV, and near-IR telescope."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-010": ("Radio telescopes use parabolic metal dishes to focus radio waves, functioning day and night regardless of cloudy weather.", {
        "They can be used during the daytime.": "Correct; solar optical glare does not drown out radio-frequency cosmic signals.",
        "They are unaffected by cloudy weather.": "Correct; radio waves easily penetrate water droplets in clouds without scattering.",
        "They use parabolic metal dishes instead of glass lenses.": "Correct; metallic surfaces reflect radio waves to focus them on receivers.",
        "They detect very high-frequency gamma radiation.": "Incorrect; gamma radiation is high-frequency nuclear radiation detected by space satellites."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-011": ("The electromagnetic spectrum extends from long radio waves to ultra-energetic gamma rays, with visible light spanning 400–800 nm.", {
        "Radio waves have the longest wavelengths in the spectrum.": "Correct; radio wavelengths range from millimeters to thousands of meters.",
        "Gamma rays have the highest energy per photon.": "Correct; \\(E = h\\nu\\) gives gamma rays the maximum photon energy.",
        "Visible light spans wavelengths from roughly \\(400\\text{ nm}\\) to \\(800\\text{ nm}\\).": "Correct; this represents the visible optical band.",
        "X-rays can easily pass through the Earth's atmosphere to reach ground-level instruments.": "Incorrect; X-rays are completely blocked by the atmosphere."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-012": ("Space telescopes orbit outside the atmosphere, including Hubble (optical/UV), Chandra (X-ray), and JWST (infrared).", {
        "Hubble Space Telescope": "Correct; launched in 1990 into low Earth orbit.",
        "Chandra X-ray Observatory": "Correct; launched in 1999 to observe X-rays from space.",
        "James Webb Space Telescope": "Correct; launched in 2021 to observe infrared radiation at L2.",
        "Giant Metrewave Radio Telescope": "Incorrect; GMRT is a ground-based facility in Narayangaon, Pune."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-013": ("Ground-based optical astronomy suffers from atmospheric turbulence (twinkling), weather/clouds, and urban light pollution.", {
        "Turbulence in Earth's atmosphere": "Correct; fluctuating temperature and density cause atmospheric seeing blur.",
        "Presence of clouds and water vapor": "Correct; clouds scatter visible light and water vapor absorbs infrared.",
        "City lights causing light pollution": "Correct; artificial illumination brightens the night sky background.",
        "Interplanetary magnetic fields": "Incorrect; magnetic fields do not alter the straight propagation of optical photons."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-014": ("High mountaintops offer thinner air, lower humidity, clearer skies, and avoidance of urban light pollution for observatories.", {
        "A smaller amount of air mass lies above the telescope, reducing atmospheric absorption.": "Correct; higher altitude reduces optical and infrared extinction.",
        "Lower humidity reduces water vapor interference, especially for infrared observations.": "Correct; dry mountain air minimizes infrared absorption bands.",
        "Skies are frequently clearer and free from low cloud cover.": "Correct; observatory peaks frequently sit above low inversion cloud layers.",
        "The telescope is located outside Earth's gravitational field.": "Incorrect; gravity is essentially identical on mountaintops compared to sea level."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-015": ("Ultraviolet radiation has shorter wavelengths and higher photon energy than infrared, driving photochemical rather than thermal effects.", {
        "Ultraviolet has shorter wavelengths than infrared.": "Correct; UV (\\(10-400\\text{ nm}\\)) is much shorter than IR (\\(800\\text{ nm} - 1\\text{ mm}\\)).",
        "Ultraviolet carries higher energy per photon than infrared.": "Correct; photon energy \\(E = hc/\\lambda\\) is significantly higher for UV.",
        "Infrared radiation is commonly associated with thermal heat, while UV causes chemical and ionization effects.": "Correct; IR excites molecular vibrations, whereas UV drives electron transitions and chemical damage.",
        "Ultraviolet rays easily penetrate human skin, while infrared cannot.": "Incorrect; far UV is absorbed superficially in the epidermis, whereas near-IR penetrates deeper."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-016": ("Radio astronomy investigates non-thermal synchrotron emission from pulsars, cold 21-cm hydrogen gas, and distant active galactic nuclei.", {
        "Pulsars and neutron stars": "Correct; pulsars emit periodic beams of radio waves generated by relativistic magnetospheres.",
        "Hydrogen gas clouds in the interstellar medium": "Correct; neutral hydrogen emits the ubiquitous \\(21\\text{-cm}\\) radio line.",
        "Quasars and distant radio galaxies": "Correct; relativistic plasma jets in active galaxies produce powerful radio emission.",
        "Atmospheres of exoplanets in visible detail": "Incorrect; exoplanet atmospheric transit spectroscopy requires optical/infrared telescopes."
    }),
    "MH-9-SCIT-18-18.1.1-OMC-017": ("Electromagnetic waves are transverse disturbances of coupled electric and magnetic vectors propagating through vacuum without any medium.", {
        "They transfer momentum and energy across interplanetary and interstellar distances.": "Correct; EM waves carry radiant flux, momentum, and radiation pressure.",
        "They can travel through the vacuum of space without any physical conduit.": "Correct; self-sustaining electric and magnetic field oscillations require no material medium.",
        "Their electric and magnetic field oscillations are perpendicular to each other and to the direction of wave propagation.": "Correct; this defines the transverse nature of electromagnetic waves.",
        "Their speed increases directly as their frequency increases in a vacuum.": "Incorrect; all EM waves travel at the constant speed \\(c\\) in vacuum regardless of frequency."
    })
}

for q in t1_qs:
    code = q['questionCode']
    if q['type'] == 'OMC' and code in omc_data:
        concept, opt_reasons = omc_data[code]
        correct_list = q.get('correctAnswers', [])
        options = q.get('options', [])
        
        lines = []
        for i, opt in enumerate(options):
            letter = chr(65+i)
            is_corr = (opt in correct_list)
            corr_tag = " (Correct)" if is_corr else ""
            reason = opt_reasons.get(opt, "Evaluated based on physical principles.")
            lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            
        solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

print(f"Generated {len(solutions)} / {len(t1_qs)} solutions for Topic 18.1.1.")

# Save Topic 1 solutions
with open('scripts/ch18_t1_solutions.json', 'w', encoding='utf-8') as f:
    json.dump(solutions, f, indent=2)
print("Saved scripts/ch18_t1_solutions.json")
