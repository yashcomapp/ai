# -*- coding: utf-8 -*-
"""
Chapter 18 Topics 18.4.1 and 18.4.2 Solution Generator (100 Questions)
Class 9 Science & Technology: Observing Space: Telescopes
Telescopes in Space & Atmospheric Obstacles (18.4.1)
Hubble Space Telescope & Chandra X-ray Observatory (18.4.2)
"""

import json

with open('scripts/t4_dump.json', 'r', encoding='utf-8') as f:
    t4_qs = json.load(f)

solutions = {}

# --- TOPIC 18.4.1: TELESCOPES IN SPACE & ATMOSPHERIC OBSTACLES (50 Qs) ---
# 9 OAR
t4_oar_18_4_1 = {
    "MH-9-SCIT-18-18.4.1-OAR-001": ("""Ground-based telescopes look through Earth's turbulent atmosphere; random fluctuations in air temperature and density alter the refractive index continuously, blurring wavefronts and degrading image resolution.""",
        "True — Images captured by ground-based optical telescopes are frequently blurred and shimmer due to atmospheric seeing.",
        "True — Rapid convective mixing of warm and cool air pockets refracts starlight intermittently along random paths.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-002": ("""Urban artificial illumination scatters off aerosols and air molecules in the troposphere, elevating sky background brightness and masking the faint starlight from distant galaxies.""",
        "True — Major astronomical observatories are established in remote, dark rural regions far from metropolitan areas.",
        "True — City lighting creates diffuse skyglow that drowns out faint, low-contrast astronomical objects.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-003": ("""Atmospheric ozone absorbs ultraviolet radiation, while nitrogen and oxygen molecules absorb X-rays and gamma rays, shielding terrestrial biology but preventing ground observation of these wavelengths.""",
        "True — Ground observatories cannot conduct direct X-ray, gamma-ray, or far-UV astronomical observations.",
        "True — Earth's atmospheric gases are completely opaque to ionizing high-energy electromagnetic radiation.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-004": ("""Space telescopes orbit in the vacuum of low Earth orbit or Lagrange points, completely escaping atmospheric refraction, extinction, weather, and light pollution.""",
        "True — Telescopes in space achieve diffraction-limited resolution without atmospheric degradation.",
        "True — Operating outside Earth's atmosphere eliminates all atmospheric turbulence, seeing blur, and air absorption.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-005": ("""Planets have resolvable angular disk sizes, so refraction fluctuations across multiple points on their disks average out; stars are pinpoint sources whose narrow pencil beams are easily deflected, causing them to twinkle.""",
        "True — Stars appear to twinkle when observed from the ground, whereas planets generally shine with a steady light.",
        "True — Planets subtend larger angular diameters than stars, so atmospheric fluctuations across the disk cancel each other out.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-006": ("""Atmospheric water vapor (\\(\\ce{H2O}\\)) and carbon dioxide (\\(\\ce{CO2}\\)) strongly absorb infrared radiation across major vibrational-rotational molecular bands.""",
        "True — Ground-based infrared astronomy is severely hindered by atmospheric absorption.",
        "True — Triatomic greenhouse molecules like water vapor and carbon dioxide absorb incoming infrared starlight.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-007": ("""High mountaintop observatories (e.g., Mauna Kea, Hanle Ladakh) rise above 4,000 meters, putting them above 40–50% of the atmosphere and nearly all low-level clouds and water vapor.""",
        "True — Placing telescopes on high peaks significantly improves image quality and reduces atmospheric extinction.",
        "True — High elevation places observatories above the dense, moist, and turbulent lower tropospheric inversion layers.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-008": ("""Daytime solar radiation is scattered by air molecules via Rayleigh scattering (proportional to \\(1/\\lambda^4\\)), illuminating the daytime sky with bright diffuse blue light that overpowers faint stars.""",
        "True — Optical telescopes on the Earth's surface cannot observe faint celestial bodies during daylight hours.",
        "True — Rayleigh scattering of sunlight creates bright sky luminance millions of times brighter than distant stars.",
        "A"),
    "MH-9-SCIT-18-18.4.1-OAR-009": ("""Adaptive optics systems use laser guide stars and deformable computer-driven mirrors to measure and correct atmospheric wavefront distortions hundreds of times per second.""",
        "True — Modern ground-based telescopes equipped with adaptive optics achieve image sharpness rivaling space telescopes.",
        "True — High-speed piezoelectric actuators deform thin mirror surfaces to cancel out atmospheric phase distortions in real time.",
        "A")
}

# 11 OTF
t4_otf_18_4_1 = {
    "MH-9-SCIT-18-18.4.1-OTF-001": ("Earth's atmosphere absorbs gamma rays, X-rays, and ultraviolet radiation completely, shielding life while blocking high-energy astronomy.",
        True, "Atmospheric absorption prevents high-energy ionizing radiation (gamma rays, X-rays, far UV) from reaching ground-level telescopes."),
    "MH-9-SCIT-18-18.4.1-OTF-002": ("Placing optical telescopes on mountain peaks reduces atmospheric air mass, but does not completely eliminate turbulence, weather, or daytime solar scattering.",
        False, "Mountaintop observatories still look through several kilometers of atmosphere and cannot eliminate all atmospheric distortion or day/night cycles."),
    "MH-9-SCIT-18-18.4.1-OTF-003": ("Starlight twinkles (scintillates) because light rays pass through turbulent atmospheric cells of differing temperature and refractive index.",
        True, "Atmospheric turbulence causes rapid deflection and intensity fluctuations of starlight, creating the twinkling effect."),
    "MH-9-SCIT-18-18.4.1-OTF-004": ("Space telescopes are immune to clouds, atmospheric turbulence, daytime skyglow, and urban light pollution.",
        True, "Orbiting above the atmosphere provides pristine, uninterrupted viewing conditions in continuous vacuum darkness."),
    "MH-9-SCIT-18-18.4.1-OTF-005": ("Because planets are closer to Earth, they appear as extended disks whose light rays average out, so they rarely twinkle like point-source stars.",
        True, "Planets have measurable angular diameters acting as multiple point sources whose variations cancel out, resulting in steady light."),
    "MH-9-SCIT-18-18.4.1-OTF-006": ("Water vapor in Earth's troposphere strongly absorbs cosmic infrared radiation, making high, arid mountaintops or space essential for IR astronomy.",
        True, "Tropospheric water vapor absorbs infrared photons; dry high-altitude sites (like Atacama or Ladakh) or space satellites are required."),
    "MH-9-SCIT-18-18.4.1-OTF-007": ("Rayleigh scattering of starlight by atmospheric dust causes the night sky in cities to be completely transparent to optical light.",
        False, "Artificial lighting scatters off atmospheric aerosols, causing severe light pollution that obscures faint astronomical bodies."),
    "MH-9-SCIT-18-18.4.1-OTF-008": ("Space telescopes can observe faint stars and distant galaxies continuously without being interrupted by daylight or bad weather.",
        True, "Operating in space eliminates weather delays and atmospheric daylight scattering, allowing extended exposure times."),
    "MH-9-SCIT-18-18.4.1-OTF-009": ("Adaptive optics technology uses flexible mirrors adjusted by computer actuators to cancel out atmospheric turbulence in real time.",
        True, "Adaptive optics measures wavefront distortions using sensor feedback and deforms a flexible mirror to restore sharpness."),
    "MH-9-SCIT-18-18.4.1-OTF-010": ("The term 'astronomical seeing' refers to the degree of optical blur and image jitter caused by atmospheric turbulence.",
        True, "'Seeing' is the standard astronomical metric measuring the angular diameter of a blurred star point caused by atmospheric turbulence."),
    "MH-9-SCIT-18-18.4.1-OTF-011": ("Optical telescopes on the surface of the Earth can easily detect cosmic X-rays and gamma rays on clear, cloudless nights.",
        False, "X-rays and gamma rays are absorbed in the upper atmosphere and never reach the Earth's surface, regardless of cloud cover.")
}

# 21 OSC
t4_osc_18_4_1 = {
    "MH-9-SCIT-18-18.4.1-OSC-001": ("Starlight twinkles because light rays pass through turbulent layers of moving air with continuously fluctuating refractive indices.", {
        "A": "Atmospheric turbulence causes continuous random refraction of narrow starlight rays, resulting in scintillation (twinkling).",
        "B": "Incorrect; stars do not rapidly pulsate in brightness.",
        "C": "Incorrect; interplanetary dust does not flicker starlight.",
        "D": "Incorrect; human blinking is not the cause of stellar twinkling."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-002": ("The primary reason for placing telescopes in space is to completely eliminate atmospheric distortion, absorption, and weather interference.", {
        "A": "Orbiting outside Earth's atmosphere eliminates seeing blur, air absorption, clouds, and light pollution.",
        "B": "Incorrect; space telescopes are much more expensive to construct and launch.",
        "C": "Incorrect; distance to stars is negligible compared to the orbital radius.",
        "D": "Incorrect; space telescopes do not escape the Sun's gravitational field."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-003": ("Atmospheric turbulence blurs point-source starlight into a jittering disc; astronomers quantify this optical distortion as 'seeing'.", {
        "A": "Astronomical 'seeing' describes the blurring of stellar images caused by atmospheric turbulence.",
        "B": "Incorrect; focal length is a telescope design parameter.",
        "C": "Incorrect; chromatic aberration is glass dispersion.",
        "D": "Incorrect; field of view is angular sky coverage."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-004": ("Earth's atmosphere absorbs cosmic X-rays, gamma rays, and ultraviolet radiation completely, shielding life while necessitating space observatories.", {
        "A": "Gamma rays, X-rays, and far UV are completely absorbed by nitrogen, oxygen, and ozone in the atmosphere.",
        "B": "Incorrect; visible light passes through the optical window.",
        "C": "Incorrect; radio waves pass through the radio window.",
        "D": "Incorrect; near-infrared penetrates dry atmospheric bands."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-005": ("High mountaintops place telescopes above the thickest, most humid layers of the troposphere, reducing water vapor absorption and air turbulence.", {
        "A": "High altitude puts the telescope above low-level humidity, fog, dust, and thick atmospheric turbulence.",
        "B": "Incorrect; gravity is essentially identical at mountain heights.",
        "C": "Incorrect; telescopes do not move faster on mountains.",
        "D": "Incorrect; magnetic fields do not alter optical rays."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-006": ("Planets subtend a larger angular size than stars; slight refractions across their disk average out, preventing them from twinkling.", {
        "A": "Planets act as extended sources whose multiple ray paths average out, so they shine with steady, non-twinkling light.",
        "B": "Incorrect; planets reflect starlight from the Sun; they do not emit their own nuclear light.",
        "C": "Incorrect; planetary light passes through the same atmosphere.",
        "D": "Incorrect; planets move slowly relative to starlight."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-007": ("Rayleigh scattering of sunlight by diatomic nitrogen and oxygen molecules illuminates the daytime sky with bright diffuse light, drowning out stars.", {
        "A": "Rayleigh scattering of sunlight creates high sky background brightness that overpowers faint stellar photons.",
        "B": "Incorrect; stars do not turn off during daytime.",
        "C": "Incorrect; the ozone layer does not absorb visible starlight.",
        "D": "Incorrect; Earth's magnetic field does not reflect starlight."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-008": ("Atmospheric water vapor absorbs cosmic infrared wavelengths, making dry, arid high-altitude deserts the premier ground sites for IR astronomy.", {
        "A": "Atmospheric water vapor strongly absorbs incoming infrared radiation.",
        "B": "Incorrect; helium does not absorb infrared.",
        "C": "Incorrect; nitrogen does not have strong IR dipole absorption bands.",
        "D": "Incorrect; argon is an inert monoatomic gas without IR absorption bands."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-009": ("Adaptive optics utilizes high-speed wavefront sensors and computer-controlled deformable mirrors to cancel out atmospheric turbulence in real time.", {
        "A": "Adaptive optics deforms a thin secondary mirror hundreds of times per second to neutralize atmospheric wavefront distortions.",
        "B": "Incorrect; cryogenics cools sensors, it does not correct wavefronts.",
        "C": "Incorrect; spectroscopy splits light into spectra.",
        "D": "Incorrect; polarizing filters only select wave orientation."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-010": ("Artificial urban lighting illuminates aerosols and clouds in the night sky, creating 'light pollution' that prevents observations of faint galaxies.", {
        "A": "Light pollution from urban areas scatters into the sky, drastically reducing the contrast of faint celestial objects.",
        "B": "Incorrect; air pollution refers to chemical particulates, though it often accompanies light pollution.",
        "C": "Incorrect; greenhouse effect refers to thermal heat retention.",
        "D": "Incorrect; thermal inversion is a meteorological temperature layer."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-011": ("Because stars are located light-years away, their angular size as viewed from Earth is practically a single mathematical point.", {
        "A": "Stars are point sources of light, making their narrow ray cones exceptionally susceptible to atmospheric refraction and twinkling.",
        "B": "Incorrect; stars are not flat geometric sheets.",
        "C": "Incorrect; stars are huge spherical plasmas, but appear as points due to immense distance.",
        "D": "Incorrect; stars are not ring-shaped."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-012": ("A major limitation of space telescopes is their extremely high financial cost and the extreme difficulty or impossibility of physical repairs.", {
        "A": "High launch costs and the difficulty of servicing orbital instruments are primary drawbacks of space telescopes.",
        "B": "Incorrect; space telescopes achieve far sharper images than ground telescopes.",
        "C": "Incorrect; they detect UV and X-rays that ground telescopes cannot.",
        "D": "Incorrect; they are immune to bad weather."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-013": ("The stratospheric ozone (\\(\\ce{O3}\\)) layer absorbs solar and stellar ultraviolet radiation (wavelengths below 310 nm), protecting Earth's biosphere.", {
        "A": "The stratospheric ozone layer absorbs harmful ultraviolet radiation, requiring space telescopes for UV astronomy.",
        "B": "Incorrect; tropospheric carbon dioxide absorbs infrared.",
        "C": "Incorrect; nitrogen absorbs extreme UV and X-rays in the thermosphere.",
        "D": "Incorrect; water vapor absorbs infrared."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-014": ("The Hubble Space Telescope was launched into low Earth orbit at an altitude of approximately 540–570 kilometers, well above the dense atmosphere.", {
        "A": "Orbiting at approximately \\(540-570\\text{ km}\\) places Hubble completely above the turbulent troposphere and stratosphere.",
        "B": "Incorrect; \\(10\\text{ km}\\) is within the tropospheric jet stream.",
        "C": "Incorrect; geostationary orbit is at \\(36{,}000\\text{ km}\\).",
        "D": "Incorrect; Moon orbit is at \\(384{,}000\\text{ km}\\)."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-015": ("Laser guide stars are projected into the upper mesosphere (exciting sodium atoms at 90 km) to provide a reference point for adaptive optics systems.", {
        "A": "Laser guide stars create an artificial beacon in the upper atmosphere to measure turbulent phase distortions for adaptive optics.",
        "B": "Incorrect; lasers do not destroy space debris in astronomy.",
        "C": "Incorrect; lasers do not heat telescope mirrors.",
        "D": "Incorrect; lasers do not communicate with aliens."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-016": ("Daylight Rayleigh scattering prevents ground-based optical telescopes from viewing stars; in space, the sky is perpetually black, allowing round-the-clock viewing.", {
        "A": "In the vacuum of space, there are no air molecules to scatter sunlight, keeping the background sky black even in daylight.",
        "B": "Incorrect; space does not lack sunlight.",
        "C": "Incorrect; stars do not move closer to space telescopes.",
        "D": "Incorrect; gravity does not change the sky color."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-017": ("In astronomy, the 'optical window' and 'radio window' are the two primary wavelength intervals where Earth's atmosphere is transparent to cosmic radiation.", {
        "A": "The optical and radio windows allow visible light and certain radio frequencies to reach ground instruments.",
        "B": "Incorrect; the X-ray window does not exist at sea level.",
        "C": "Incorrect; gamma rays do not penetrate to the ground.",
        "D": "Incorrect; ultraviolet is predominantly blocked by ozone."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-018": ("The Indian Astronomical Observatory (IAO) at Hanle, Ladakh, is located at an altitude of 4,500 meters, making it one of the highest optical sites in the world.", {
        "A": "Hanle in Ladakh (elevation \\(4500\\text{ m}\\)) offers exceptionally clear, dry, and dark skies for Indian astronomy.",
        "B": "Incorrect; Mumbai is a humid, sea-level metropolis with severe light pollution.",
        "C": "Incorrect; Chennai is a humid coastal city.",
        "D": "Incorrect; Kolkata is a low-altitude river delta city."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-019": ("Clouds are composed of liquid water droplets or ice crystals that reflect and scatter visible starlight, completely blocking optical astronomical observations.", {
        "A": "Cloud cover reflects and scatters starlight, rendering ground-based optical telescopes completely ineffective during overcast weather.",
        "B": "Incorrect; clouds do not stop radio waves.",
        "C": "Incorrect; clouds do not alter the telescope's focal length.",
        "D": "Incorrect; clouds do not absorb gravity."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-020": ("Atmospheric extinction refers to the attenuation (absorption and scattering) of starlight as it travels through Earth's atmospheric path length.", {
        "A": "Atmospheric extinction reduces the apparent brightness of stars as light is scattered and absorbed by air and dust.",
        "B": "Incorrect; scintillation is the rapid flickering of position and brightness.",
        "C": "Incorrect; chromatic aberration is glass dispersion.",
        "D": "Incorrect; spherical aberration is mirror curvature error."
    }),
    "MH-9-SCIT-18-18.4.1-OSC-021": ("Ground-based optical telescopes are typically housed inside rotatable hemispherical domes with slit openings that shield instruments from wind and dust.", {
        "A": "Observatory domes protect precision telescope mechanics from wind buffeting and precipitation while providing a viewing slit.",
        "B": "Incorrect; domes do not generate oxygen.",
        "C": "Incorrect; domes do not magnify starlight.",
        "D": "Incorrect; domes do not block cosmic rays."
    })
}

# 9 OMC 18.4.1
t4_omc_18_4_1 = {
    "MH-9-SCIT-18-18.4.1-OMC-001": ("Ground-based optical astronomy is hindered by atmospheric turbulence (seeing), atmospheric absorption of UV/X-rays, and urban light pollution.", {
        "Turbulence causing rapid shifts in light direction and blurring images": "Correct; convective cells cause starlight scintillation and optical blur.",
        "Absorption of ultraviolet and X-ray wavelengths by atmospheric gases": "Correct; ozone, oxygen, and nitrogen block high-energy radiation.",
        "City lights causing light pollution that brightens the night sky background": "Correct; scattered artificial illumination masks faint celestial targets.",
        "Gravitational lensing bending starlight inside the telescope tube": "Incorrect; gravitational lensing requires massive cosmic bodies (galaxies), not air inside tubes."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-002": ("To overcome atmospheric degradation, astronomers build observatories on high dry mountaintops, launch space telescopes, and use adaptive optics.", {
        "Building observatories on remote, high mountain peaks above thick cloud layers": "Correct; avoids lower tropospheric moisture, dust, and seeing blur.",
        "Placing telescopes in orbit around the Earth in outer space": "Correct; completely eliminates all atmospheric absorption and turbulence.",
        "Using adaptive optics technology to correct for atmospheric distortion in real time": "Correct; deformable mirrors actively compensate for seeing fluctuations.",
        "Replacing telescope mirrors with ordinary clear window glass": "Incorrect; window glass cannot focus light and introduces severe optical aberrations."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-003": ("Key advantages of orbiting space telescopes include zero atmospheric seeing, full spectral access (UV, X-rays, IR), and absence of weather disruptions.", {
        "Access to electromagnetic wavelengths like ultraviolet and X-rays that never reach Earth's surface": "Correct; enables high-energy astrophysics.",
        "Completely crystal-clear, sharp images free from atmospheric scintillation and seeing blur": "Correct; achieves diffraction-limited optical resolution.",
        "Continuous observations unhindered by cloud cover, rain, or local weather conditions": "Correct; orbital vacuum guarantees uninterrupted operation.",
        "Immediate, zero-cost manual repairs by technicians on bicycles": "Incorrect; orbital repairs require multi-hundred-million-dollar astronaut spacewalk missions."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-004": ("Scintillation (twinkling) affects point-source stars due to atmospheric turbulence; extended planetary disks average out and shine steadily.", {
        "Stars appear as pinpoint light sources whose narrow light beams are easily deflected by turbulent air pockets.": "Correct; point-like starlight flickers rapidly in position and intensity.",
        "Planets appear as extended disks with larger angular sizes, averaging out atmospheric fluctuations.": "Correct; variations across the planetary disc cancel, producing steady light.",
        "Twinkling occurs inside Earth's atmosphere, not in outer space.": "Correct; astronauts in space see steady, non-twinkling stars against a black sky.",
        "Twinkling is caused by rapid nuclear explosions occurring every second in stellar cores.": "Incorrect; stellar nuclear reactions are continuous and steady."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-005": ("High-altitude mountaintop sites are chosen for reduced air mass, low humidity (crucial for infrared), and isolation from urban light pollution.", {
        "A reduced atmospheric column above the observatory decreases light scattering and absorption.": "Correct; high elevation cuts atmospheric air mass significantly.",
        "Lower ambient humidity drastically minimizes infrared absorption by water vapor.": "Correct; dry air opens up critical near-infrared and submillimeter windows.",
        "Remoteness from urban centers ensures exceptionally dark night skies free of light pollution.": "Correct; dark skies provide maximum contrast for faint deep-sky targets.",
        "Mountaintop observatories experience zero gravity, allowing mirrors to float freely.": "Incorrect; gravity is essentially identical at mountaintop elevations."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-006": ("Earth's atmosphere absorbs ionizing radiation (X-rays, gamma rays, far UV) and infrared (via water vapor and CO2), but transmits visible light and radio.", {
        "Gamma rays and X-rays are absorbed high in the upper atmosphere.": "Correct; absorbed by thermospheric and stratospheric gases.",
        "Ultraviolet light below 310 nm is absorbed by the stratospheric ozone layer.": "Correct; ozone photolysis blocks lethal UV-B and UV-C radiation.",
        "Infrared radiation experiences substantial absorption bands due to water vapor and carbon dioxide.": "Correct; molecular vibration modes absorb specific infrared bands.",
        "Radio waves and visible light are completely blocked by clean dry air.": "Incorrect; clean dry air transmits visible light and radio waves freely."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-007": ("Adaptive optics systems combine high-speed wavefront sensors, real-time computer processors, laser guide stars, and deformable secondary mirrors.", {
        "Wavefront sensors to detect atmospheric phase distortions hundreds of times per second": "Correct; monitors instantaneous optical phase errors.",
        "Deformable mirrors with piezoelectric actuators to correct the distorted wavefront": "Correct; physically adjusts surface figure to cancel phase errors.",
        "Laser guide stars projected into the mesosphere to provide a bright artificial reference point": "Correct; creates an artificial beacon when no bright star is nearby.",
        "Massive concrete shields to physically block the wind from touching the clouds": "Incorrect; atmospheric turbulence occurs kilometers above the ground."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-008": ("Daytime astronomy with visible light is prevented by Rayleigh scattering of sunlight, which brightens the sky; radio astronomy is unaffected.", {
        "Sunlight is scattered in all directions by atmospheric molecules (Rayleigh scattering).": "Correct; scattering creates bright blue sky luminance.",
        "Diffuse sky brightness completely overwhelms the faint optical flux from distant stars.": "Correct; astronomical contrast drops to zero in optical wavelengths.",
        "Radio telescopes can operate during daytime because sunlight does not scatter at radio frequencies.": "Correct; solar glare does not impair radio astronomy.",
        "Stars physically cease to emit electromagnetic waves when the Sun rises.": "Incorrect; stars continue radiating uniformly 24 hours a day."
    }),
    "MH-9-SCIT-18-18.4.1-OMC-009": ("Severe operational challenges of space telescopes include enormous construction/launch costs, harsh radiation in space, and servicing constraints.", {
        "Extremely high financial investment required for launch and space qualification": "Correct; space missions cost hundreds of millions to billions of dollars.",
        "Extreme difficulty or impossibility of manned maintenance and instrument upgrades": "Correct; only Hubble was serviceable by the Space Shuttle; JWST is unreachable at L2.",
        "Exposure to harsh space environments, cosmic radiation, and micrometeoroid impacts": "Correct; electronics must be radiation-hardened and optics shielded.",
        "Frequent interruptions caused by rainstorms, fog, and clouds in orbit": "Incorrect; outer space is a vacuum with zero weather or clouds."
    })
}

# --- TOPIC 18.4.2: HUBBLE SPACE TELESCOPE & CHANDRA X-RAY OBSERVATORY (50 Qs) ---
# 10 OAR
t4_oar_18_4_2 = {
    "MH-9-SCIT-18-18.4.2-OAR-001": ("""Earth's atmosphere absorbs cosmic X-rays completely through photoelectric absorption, making ground-based X-ray astronomy impossible and space deployment essential.""",
        "True — The Chandra X-ray Observatory must operate in outer space to detect cosmic X-rays.",
        "True — Atmospheric gases (nitrogen and oxygen) completely absorb X-ray photons before they can reach the surface of the Earth.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-002": ("""The Hubble Space Telescope orbits above the turbulent atmosphere, avoiding seeing blur, skyglow, and cloud cover, allowing it to capture razor-sharp images of ultra-deep space.""",
        "True — Hubble can resolve fainter, more distant galaxies with unprecedented clarity compared to ground telescopes.",
        "True — Operating in the vacuum of space eliminates atmospheric scintillation, light absorption, and weather interference.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-003": ("""X-rays have extremely short wavelengths and high photon energies, causing them to penetrate or be absorbed by conventional glass mirrors at normal incidence rather than reflecting.""",
        "True — Standard perpendicular reflection cannot be used to focus X-rays.",
        "True — High-energy X-ray photons penetrate directly into standard glass or mirror coatings instead of bouncing off.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-004": ("""Chandra utilizes nested cylindrical paraboloid and hyperboloid mirrors where X-rays strike at shallow grazing angles (less than 1 degree), skimming off like stones skipping across water.""",
        "True — Chandra uses grazing-incidence optics to gently deflect and focus X-rays onto electronic detectors.",
        "True — When X-rays strike a polished heavy metal surface (iridium) at grazing angles below the critical angle, total external reflection occurs.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-005": ("""Subrahmanyan Chandrasekhar mathematically proved in 1930 that electron degeneracy pressure cannot support a white dwarf star against gravitational collapse if its mass exceeds 1.44 solar masses.""",
        "True — The maximum mass of a stable white dwarf star is known as the Chandrasekhar limit (\\(\\approx 1.44 M_\\odot\\)).",
        "True — Relativistic electron degeneracy pressure has an upper theoretical limit that fails above \\(1.44 M_\\odot\\), leading to neutron stars or black holes.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-006": ("""The Chandra X-ray Observatory was named in honour of Indian-American Nobel laureate Subrahmanyan Chandrasekhar to celebrate his foundational contributions to relativistic astrophysics.""",
        "True — NASA named its premier X-ray space observatory 'Chandra' in honor of Subrahmanyan Chandrasekhar.",
        "True — Chandrasekhar received the 1983 Nobel Prize in Physics for his theoretical studies of stellar structure and evolution.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-007": ("""Hubble uses a 2.4-meter primary mirror in a Ritchey-Chrétien Cassegrain reflecting configuration, collecting starlight across optical, near-UV, and near-IR bands.""",
        "True — The Hubble Space Telescope is a reflecting telescope equipped with a 2.4-meter primary mirror.",
        "True — The Cassegrain design provides a long focal length (\\(f = 57.6\\text{ m}\\)) inside a compact space-qualifiable tube.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-008": ("""Because Chandra observes million-degree gas in galaxy clusters, accretion disks around black holes, and supernova remnants, it maps the most violent, energetic realms of the cosmos.""",
        "True — Chandra X-ray observations are crucial for studying black hole physics and high-energy cataclysms.",
        "True — Matter heated to millions of Kelvin in intense gravitational and magnetic fields radiates primarily in the X-ray band.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-009": ("""Hubble's high-resolution images of Cepheid variable stars in distant galaxies enabled astronomers to calibrate the cosmic distance ladder and determine the Hubble constant (expansion rate of the universe).""",
        "True — Hubble played a decisive role in measuring the expansion rate and age of our universe (\\(\\sim 13.8\\text{ billion years}\\)).",
        "True — Resolving individual pulsating Cepheids in faraway galaxies provided precise cosmological distance measurements.",
        "A"),
    "MH-9-SCIT-18-18.4.2-OAR-010": ("""Chandra was placed in an elliptical high Earth orbit extending to 133,000 km (more than one-third the distance to the Moon) to spend most of its 64-hour orbit outside Earth's radiation belts.""",
        "True — Chandra's high elliptical orbit allows continuous X-ray observations for up to 55 hours without Earth occultation.",
        "True — Operating above the Van Allen radiation belts prevents intense particle radiation from damaging or blinding sensitive X-ray detectors.",
        "A")
}

# 11 OTF
t4_otf_18_4_2 = {
    "MH-9-SCIT-18-18.4.2-OTF-001": ("The Hubble Space Telescope observes celestial bodies across the near-ultraviolet, visible, and near-infrared regions of the spectrum.",
        True, "Hubble's scientific suite covers near-UV, visible light, and near-IR, providing comprehensive multi-wavelength imaging."),
    "MH-9-SCIT-18-18.4.2-OTF-002": ("Subrahmanyan Chandrasekhar was awarded the 1983 Nobel Prize in Physics for his mathematical theories on the structure and evolution of stars.",
        True, "Chandrasekhar received the Nobel Prize in Physics in 1983 for his foundational work on stellar dynamics and the white dwarf mass limit."),
    "MH-9-SCIT-18-18.4.2-OTF-003": ("The Chandra X-ray Observatory uses conventional thick glass convex lenses to refract incoming cosmic X-rays.",
        False, "X-rays pass right through or are absorbed by glass lenses; Chandra uses specialized grazing-incidence nested cylindrical mirrors."),
    "MH-9-SCIT-18-18.4.2-OTF-004": ("The primary mirror of the Hubble Space Telescope has an optical aperture diameter of approximately 2.4 meters.",
        True, "Hubble features a precision 2.4-meter primary mirror that has delivered revolutionary astronomical discoveries since 1990."),
    "MH-9-SCIT-18-18.4.2-OTF-005": ("The Chandrasekhar limit states that the maximum mass of a stable, non-rotating white dwarf star is approximately 1.44 solar masses.",
        True, "Above \\(1.44 M_\\odot\\), electron degeneracy pressure cannot halt gravitational collapse, resulting in a neutron star or black hole."),
    "MH-9-SCIT-18-18.4.2-OTF-006": ("Chandra X-ray Observatory is deployed on the surface of the Earth at a high-altitude mountain peak in California.",
        False, "Chandra is an orbital space telescope launched by Space Shuttle Columbia in 1999; X-rays cannot reach mountain peaks on Earth."),
    "MH-9-SCIT-18-18.4.2-OTF-007": ("The Hubble Space Telescope was launched into low Earth orbit in 1990 by the Space Shuttle Discovery.",
        True, "NASA and ESA deployed the Hubble Space Telescope in April 1990 via STS-31 aboard Space Shuttle Discovery."),
    "MH-9-SCIT-18-18.4.2-OTF-008": ("In grazing-incidence X-ray mirrors, incoming X-rays strike the reflective metal surface at very shallow, skimming angles.",
        True, "By striking nested cylindrical mirrors at grazing angles of less than 1 degree, X-rays undergo total reflection toward the focal detectors."),
    "MH-9-SCIT-18-18.4.2-OTF-009": ("Chandra primarily studies cold interstellar dust clouds that radiate thermal energy below 50 Kelvin.",
        False, "Chandra studies ultra-hot plasmas (millions of degrees) around black holes, neutron stars, and galaxy clusters; cold dust is studied in infrared/radio."),
    "MH-9-SCIT-18-18.4.2-OTF-010": ("Astronauts on Space Shuttle servicing missions visited the Hubble Space Telescope multiple times to upgrade its cameras and instruments.",
        True, "Five Space Shuttle servicing missions (SM1 to SM4) maintained, repaired, and upgraded Hubble's scientific payload in orbit."),
    "MH-9-SCIT-18-18.4.2-OTF-011": ("Stars with core masses exceeding the Chandrasekhar limit can end their lives as violent core-collapse supernovae leaving neutron stars or black holes.",
        True, "Stellar cores exceeding \\(1.44 M_\\odot\\) undergo catastrophic collapse, generating Type II supernovae and compact relativistic remnants.")
}

# 20 OSC
t4_osc_18_4_2 = {
    "MH-9-SCIT-18-18.4.2-OSC-001": ("The Chandra X-ray Observatory was named in honour of Indian-American astrophysicist and Nobel laureate Subrahmanyan Chandrasekhar.", {
        "A": "Subrahmanyan Chandrasekhar formulated the white dwarf mass limit and won the 1983 Nobel Prize in Physics.",
        "B": "Incorrect; C.V. Raman discovered the Raman effect in light scattering.",
        "C": "Incorrect; Homi Bhabha was the architect of India's nuclear energy program.",
        "D": "Incorrect; Jagadish Chandra Bose was a pioneer of radio and plant physiology."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-002": ("The Chandra observatory was specifically designed to detect and image high-energy cosmic X-ray radiation.", {
        "A": "Chandra is NASA's flagship space telescope dedicated to high-resolution X-ray astronomy.",
        "B": "Incorrect; infrared is observed by Spitzer and JWST.",
        "C": "Incorrect; radio waves are observed by ground arrays like GMRT.",
        "D": "Incorrect; visible light is observed by Hubble."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-003": ("The primary mirror of the Hubble Space Telescope has a diameter of 2.4 meters (approximately 7.9 feet).", {
        "A": "Hubble has a 2.4-meter precision primary reflecting mirror.",
        "B": "Incorrect; 10 meters describes the Keck telescopes.",
        "C": "Incorrect; 45 meters is the diameter of individual GMRT radio dishes.",
        "D": "Incorrect; 1 meter was the limit of historic refracting lenses."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-004": ("Chandra studies extreme high-energy phenomena: black hole accretion disks, supernova remnants, colliding galaxies, and hot gas in galaxy clusters.", {
        "A": "Chandra specializes in observing black holes, supernova remnants, neutron stars, and hot intergalactic gas.",
        "B": "Incorrect; ocean plate tectonics are terrestrial geological processes.",
        "C": "Incorrect; lunar atmospheric variations are studied by lunar orbiters.",
        "D": "Incorrect; Earth vegetation is studied by terrestrial remote sensing satellites."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-005": ("The Chandrasekhar limit defines the maximum possible mass (~1.44 solar masses) of a stable white dwarf supported by electron degeneracy pressure.", {
        "A": "The Chandrasekhar limit establishes the maximum theoretical mass of a stable white dwarf star (\\(\\approx 1.44 M_\\odot\\)).",
        "B": "Incorrect; the expansion rate of the universe is the Hubble constant.",
        "C": "Incorrect; the speed of light is an invariant constant \\(c\\).",
        "D": "Incorrect; solar flare composition is determined by spectroscopy."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-006": ("Standard glass lenses cannot focus X-rays because high-energy X-ray photons pass right through or are absorbed by glass rather than refracting normally.", {
        "A": "X-rays penetrate or are absorbed by standard glass rather than refracting at optical interfaces.",
        "B": "Incorrect; glass weight is not the physical barrier to X-ray refraction.",
        "C": "Incorrect; starlight X-ray flux is too faint to melt glass.",
        "D": "Incorrect; X-rays do not reflect randomly from glass."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-007": ("Chandra focuses X-rays using four pairs of nested, grazing-incidence cylindrical paraboloid and hyperboloid mirrors coated with iridium.", {
        "A": "Specialized grazing-incidence nested cylindrical mirrors reflect X-rays at shallow skimming angles.",
        "B": "Incorrect; plane wooden mirrors absorb or scatter radiation.",
        "C": "Incorrect; rubber coatings do not reflect X-rays.",
        "D": "Incorrect; thick convex glass lenses absorb X-rays."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-008": ("Subrahmanyan Chandrasekhar was awarded the Nobel Prize in Physics in 1983 for his theoretical studies of stellar structure and evolution.", {
        "A": "Chandrasekhar won the Nobel Prize in Physics in 1983.",
        "B": "Incorrect; Fields Medal is awarded in mathematics to researchers under 40.",
        "C": "Incorrect; Bharat Ratna is India's highest civilian honor.",
        "D": "Incorrect; Pulitzer Prize is awarded in journalism and literature."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-009": ("Space telescopes like Hubble and Chandra avoid all atmospheric absorption, turbulence seeing blur, weather, and city light pollution.", {
        "A": "Space deployment avoids atmospheric absorption, seeing turbulence, and light pollution entirely.",
        "B": "Incorrect; space telescopes require solar panels and batteries.",
        "C": "Incorrect; space telescopes cannot be visited by pedestrians.",
        "D": "Incorrect; space telescopes do not generate artificial gravity."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-010": ("Grazing-incidence reflection works because X-rays skim off highly polished metal surfaces at angles less than 1 degree, like stones skipping on water.", {
        "A": "X-rays skim off highly polished curved surfaces at very shallow grazing angles, undergoing total reflection.",
        "B": "Incorrect; 90-degree normal reflection causes absorption.",
        "C": "Incorrect; lead plates absorb X-rays.",
        "D": "Incorrect; X-rays are not converted into sound waves."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-011": ("The Chandrasekhar mass limit (1.44 solar masses) determines the maximum stable mass of a white dwarf star.", {
        "A": "White dwarf stars are supported by electron degeneracy pressure up to a maximum limit of \\(1.44 M_\\odot\\).",
        "B": "Incorrect; main sequence stars are supported by thermal radiation pressure from fusion.",
        "C": "Incorrect; protostars are collapsing pre-stellar gas clouds.",
        "D": "Incorrect; red supergiants are massive evolved stars."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-012": ("The Hubble Space Telescope was built to observe the cosmos in ultraviolet, visible, and near-infrared light.", {
        "A": "Hubble observes across ultraviolet, visible, and near-infrared bands.",
        "B": "Incorrect; Hubble does not observe radio waves or long microwaves.",
        "C": "Incorrect; Hubble does not record acoustic sound waves.",
        "D": "Incorrect; Hubble is not an X-ray or gamma-ray observatory."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-013": ("The mathematical limit of 1.44 solar masses for white dwarfs was derived by Subrahmanyan Chandrasekhar when he was just 19 years old.", {
        "A": "Subrahmanyan Chandrasekhar derived the theoretical limit bearing his name.",
        "B": "Incorrect; Galileo pioneered the refracting telescope.",
        "C": "Incorrect; Albert Einstein formulated the theory of relativity.",
        "D": "Incorrect; Sir Isaac Newton formulated classical mechanics and the reflecting telescope."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-014": ("Earth's atmosphere absorbs cosmic X-rays completely, shielding life from lethal radiation but preventing ground-based X-ray observatories.", {
        "A": "Earth's atmosphere absorbs X-rays completely, preventing them from reaching the ground.",
        "B": "Incorrect; mountain temperature is not the obstacle.",
        "C": "Incorrect; zero gravity is not required for X-ray reflection.",
        "D": "Incorrect; X-ray telescopes can be compact."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-015": ("Chandra's High Resolution Mirror Assembly (HRMA) consists of nested grazing-incidence paraboloid and hyperboloid mirrors.", {
        "A": "Grazing-incidence reflection using nested cylindrical mirrors is the only viable method for focusing cosmic X-rays.",
        "B": "Incorrect; diffraction gratings disperse light, they do not focus X-rays.",
        "C": "Incorrect; quartz prisms do not focus X-rays.",
        "D": "Incorrect; convex glass lenses absorb X-rays."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-016": ("When a massive star's remnant core exceeds the Chandrasekhar limit of 1.44 solar masses, it collapses past the white dwarf stage into a neutron star or black hole.", {
        "A": "A remnant core exceeding the Chandrasekhar limit collapses into a neutron star or black hole.",
        "B": "Incorrect; stable white dwarfs cannot exceed \\(1.44 M_\\odot\\).",
        "C": "Incorrect; it does not remain a main-sequence star.",
        "D": "Incorrect; protostars are early pre-main-sequence objects."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-017": ("Hubble's scientific suite operates across ultraviolet, visible, and near-infrared bands (wavelengths 115 nm to 2500 nm).", {
        "A": "Hubble observes across ultraviolet, visible, and near-infrared wavelengths.",
        "B": "Incorrect; radio waves are observed by ground radio telescopes.",
        "C": "Incorrect; sound waves do not travel through space.",
        "D": "Incorrect; X-rays and gamma rays are observed by Chandra and Fermi."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-018": ("Because X-rays have wavelengths comparable to atomic spacing, they penetrate straight into ordinary glass rather than reflecting or refracting.", {
        "A": "X-rays are absorbed or pass right through conventional glass instead of bending normally.",
        "B": "Incorrect; X-rays do not cause acoustic resonance in glass.",
        "C": "Incorrect; glass does not turn permanently opaque from starlight.",
        "D": "Incorrect; X-rays do not reflect at 180 degrees."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-019": ("A stellar core with mass less than the Chandrasekhar limit ends its life peacefully as a stable white dwarf cooled by radiative emission.", {
        "A": "A stellar core below \\(1.44 M_\\odot\\) forms a stable white dwarf supported by electron degeneracy pressure.",
        "B": "Incorrect; neutron stars form when the core exceeds \\(1.44 M_\\odot\\).",
        "C": "Incorrect; black holes form when the remnant exceeds the Tolman-Oppenheimer-Volkoff limit (\\(\\sim 3 M_\\odot\\)).",
        "D": "Incorrect; asteroids are rocky solar system bodies, not stellar remnants."
    }),
    "MH-9-SCIT-18-18.4.2-OSC-020": ("Hubble achieves extraordinary sharpness because it orbits above Earth's atmosphere, completely avoiding twinkling and air distortion.", {
        "A": "By orbiting above Earth's turbulent atmosphere, Hubble eliminates scintillation and seeing blur completely.",
        "B": "Incorrect; liquid water lenses are not used in space telescopes.",
        "C": "Incorrect; Hubble does not shoot laser beams into the stratosphere.",
        "D": "Incorrect; Hubble uses precision glass mirrors."
    })
}

# 9 OMC 18.4.2
t4_omc_18_4_2 = {
    "MH-9-SCIT-18-18.4.2-OMC-001": ("Subrahmanyan Chandrasekhar determined the 1.44 solar mass limit for white dwarfs, formulated stellar evolution dynamics, and won the 1983 Nobel Prize.", {
        "Determining the upper mass limit for white dwarf stars (Chandrasekhar limit)": "Correct; showed that white dwarfs cannot exceed \\(1.44 M_\\odot\\).",
        "Making fundamental discoveries about the stellar evolution of massive stars": "Correct; formulated mathematical theories of stellar interiors and black hole collapse.",
        "Receiving the Nobel Prize in Physics for his theoretical studies on physical processes important to stellar structure and evolution": "Correct; awarded the 1983 Nobel Prize in Physics.",
        "Inventing the first optical telescope in 1609": "Incorrect; Hans Lippershey and Galileo Galilei pioneered optical telescopes in 1608–1609."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-002": ("The Hubble Space Telescope features a 2.4-meter primary mirror, multi-spectral instruments (UV, visible, IR), and solar power arrays in orbit.", {
        "A primary optical mirror measuring roughly 2.4 meters in diameter": "Correct; precision Ritchey-Chrétien Cassegrain primary mirror.",
        "Cameras and spectrographs operating across ultraviolet, visible, and infrared light": "Correct; payload includes ACS, WFC3, and STIS instruments.",
        "Solar panels to generate electrical power in orbit": "Correct; twin solar arrays convert sunlight into electricity for operations.",
        "A massive nuclear reactor powering rocket propulsion": "Incorrect; Hubble uses solar panels and batteries, not a nuclear reactor."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-003": ("The Chandra X-ray Observatory uses nested grazing-incidence cylindrical mirrors coated with iridium and observes violent high-energy cosmic events.", {
        "It uses specialized grazing-incidence mirrors to focus X-rays.": "Correct; four nested pairs of paraboloid and hyperboloid mirrors.",
        "It detects X-rays emitted by high-energy objects like black holes and supernova remnants.": "Correct; images million-degree gas and relativistic jets.",
        "It operates in space because Earth's atmosphere completely blocks cosmic X-rays.": "Correct; orbital placement is mandatory for X-ray astronomy.",
        "It was built using ordinary thick convex glass lenses like a handheld magnifying glass.": "Incorrect; X-rays pass through or are absorbed by glass lenses."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-004": ("Astronomical milestones achieved by the Hubble Space Telescope include measuring the expansion rate of the universe, deep-field galaxy surveys, and observing protoplanetary disks.", {
        "Accurately measuring the rate of expansion of the universe (Hubble constant)": "Correct; Cepheid observations calibrated cosmic distances.",
        "Capturing the Hubble Deep Field images showing thousands of distant newborn galaxies": "Correct; revealed galaxies formed less than a billion years after the Big Bang.",
        "Observing protoplanetary disks (proplyds) around newborn stars in the Orion Nebula": "Correct; confirmed the birthplaces of planetary systems.",
        "Landing astronauts safely on the surface of Mars": "Incorrect; Hubble is an orbiting astronomical telescope, not a manned spacecraft."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-005": ("High-energy cosmic phenomena that radiate primarily in the X-ray band include black hole accretion disks, neutron star surfaces, and hot gas in galaxy clusters.", {
        "Hot gas in colliding clusters of galaxies (temperatures of millions of Kelvin)": "Correct; intergalactic cluster gas glows brightly in X-rays.",
        "Accretion disks of matter spiraling into supermassive black holes": "Correct; friction and gravitational heating generate intense X-ray radiation.",
        "Remnants of exploded supernova stars containing shock waves and pulsars": "Correct; Crab Nebula and Cas A are brilliant X-ray sources.",
        "Cold interstellar molecular clouds where water and ammonia molecules freeze": "Incorrect; cold molecular gas emits in radio and submillimeter bands."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-006": ("Hubble and Chandra are both flagship space observatories operating in vacuum; Hubble observes optical/UV/IR while Chandra observes X-rays.", {
        "Both operate in orbit above Earth's atmosphere to eliminate atmospheric absorption.": "Correct; orbiting above the atmosphere is essential for both.",
        "Hubble observes primarily in UV, visible, and near-IR light, while Chandra observes in X-rays.": "Correct; complementary multi-wavelength capabilities.",
        "Both have revolutionized our understanding of deep-space astrophysics and cosmology.": "Correct; both are pillars of NASA's Great Observatories program.",
        "Both use the exact same type of standard reflective parabolic glass dish.": "Incorrect; Chandra uses grazing-incidence cylindrical mirrors, not standard dish mirrors."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-007": ("Grazing-incidence reflection in X-ray telescopes relies on very shallow striking angles, highly polished dense metal surfaces (iridium/gold), and nested cylindrical geometry.", {
        "X-rays must strike the metal mirror surface at extremely shallow (grazing) angles of less than 1 degree.": "Correct; avoids penetrating into the mirror substrate.",
        "The mirrors are coated with heavy, dense metals such as iridium or gold.": "Correct; high-density elements maximize total external reflection.",
        "The mirrors are arranged as nested concentric cylinders to increase total collecting area.": "Correct; nested shells maximize the effective aperture.",
        "The mirrors must be transparent glass lenses that bend light by refraction.": "Incorrect; X-rays are not refracted by lenses."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-008": ("Stellar evolution outcomes governed by the Chandrasekhar limit (1.44 solar masses) include white dwarfs (< 1.44 M_sun) and neutron stars/black holes (> 1.44 M_sun).", {
        "Stellar remnant cores with mass less than the Chandrasekhar limit form stable white dwarf stars.": "Correct; supported indefinitely by electron degeneracy pressure.",
        "Stellar remnant cores with mass exceeding the Chandrasekhar limit collapse into neutron stars or black holes.": "Correct; electron degeneracy pressure is overwhelmed by gravity.",
        "The limit demonstrates that quantum mechanical principles (Pauli exclusion principle) govern macroscopic astrophysical bodies.": "Correct; degeneracy pressure arises from the Pauli exclusion principle.",
        "All stars, regardless of initial mass, permanently expand into eternal yellow dwarfs like the Sun.": "Incorrect; stars evolve into white dwarfs, neutron stars, or black holes."
    }),
    "MH-9-SCIT-18-18.4.2-OMC-009": ("Chandra's orbital parameters include an elliptical high Earth orbit reaching 133,000 km, spending over 70% of each 64-hour orbit above Earth's radiation belts.", {
        "Its highly elliptical orbit allows extended uninterrupted observation periods lasting up to 55 hours.": "Correct; avoids frequent Earth occultations experienced in low Earth orbit.",
        "It spends most of its orbit outside Earth's Van Allen radiation belts.": "Correct; avoids intense charged particle interference on sensitive detectors.",
        "Its orbit takes it more than one-third of the distance to the Moon at its apogee.": "Correct; apogee altitude is approximately \\(133{,}000\\text{ km}\\).",
        "It lands in the Pacific Ocean every night for cleaning and battery replacement.": "Incorrect; Chandra remains in permanent outer space orbit."
    })
}

# Process all 100 questions in t4_qs
for q in t4_qs:
    code = q['code']
    qtype = q['type']
    
    # 18.4.1
    if '-18.4.1' in code:
        if qtype == 'OAR' and code in t4_oar_18_4_1:
            concept, a_exp, r_exp, correct_let = t4_oar_18_4_1[code]
            solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical optical and atmospheric principles."""
        elif qtype == 'OTF' and code in t4_otf_18_4_1:
            concept, truth_val, rationale = t4_otf_18_4_1[code]
            correct_choice = "A" if truth_val else "B"
            truth_str = "True" if truth_val else "False"
            solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""
        elif qtype == 'OSC' and code in t4_osc_18_4_1:
            concept, opt_reasons = t4_osc_18_4_1[code]
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
                reason = opt_reasons.get(letter, "Evaluated based on atmospheric and optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
        elif qtype == 'OMC' and code in t4_omc_18_4_1:
            concept, opt_reasons = t4_omc_18_4_1[code]
            correct_list = q.get('cas', [])
            options = q.get('options', [])
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (opt in correct_list)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(opt, "Evaluated based on atmospheric and optical principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

    # 18.4.2
    elif '-18.4.2' in code:
        if qtype == 'OAR' and code in t4_oar_18_4_2:
            concept, a_exp, r_exp, correct_let = t4_oar_18_4_2[code]
            solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical astrophysics principles."""
        elif qtype == 'OTF' and code in t4_otf_18_4_2:
            concept, truth_val, rationale = t4_otf_18_4_2[code]
            correct_choice = "A" if truth_val else "B"
            truth_str = "True" if truth_val else "False"
            solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""
        elif qtype == 'OSC' and code in t4_osc_18_4_2:
            concept, opt_reasons = t4_osc_18_4_2[code]
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
                reason = opt_reasons.get(letter, "Evaluated based on astrophysics principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
        elif qtype == 'OMC' and code in t4_omc_18_4_2:
            concept, opt_reasons = t4_omc_18_4_2[code]
            correct_list = q.get('cas', [])
            options = q.get('options', [])
            lines = []
            for i, opt in enumerate(options):
                letter = chr(65+i)
                is_corr = (opt in correct_list)
                corr_tag = " (Correct)" if is_corr else ""
                reason = opt_reasons.get(opt, "Evaluated based on astrophysics principles.")
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
            solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

print(f"Generated {len(solutions)} / {len(t4_qs)} solutions for Topics 18.4.1 and 18.4.2.")

with open('scripts/ch18_t4_solutions.json', 'w', encoding='utf-8') as f:
    json.dump(solutions, f, indent=2)
print("Saved scripts/ch18_t4_solutions.json")
