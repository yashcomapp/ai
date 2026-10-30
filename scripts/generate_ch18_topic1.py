# -*- coding: utf-8 -*-
"""
Generate 82 canonical questions for MH-9-SCIT-18-18.1
Topic: Forms of Light & Electromagnetic Spectrum
Vault: 40 Exam, 30 Practice, 12 Mock (with dark-theme SVGs)
"""

import json
import os

TOPIC_CODE = "MH-9-SCIT-18-18.1"

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
    # 1: Nature of light
    ("What fundamental physical phenomenon is light fundamentally recognized as in modern physics?",
     ["Electromagnetic radiation consisting of synchronized oscillating electric and magnetic fields",
      "A stream of heavy microscopic lead particles",
      "A purely mechanical sound vibration of air molecules",
      "A steady flow of liquid chemical photons"],
     "A", "OSC", "easy",
     "Light is electromagnetic radiation composed of transverse electric and magnetic field vectors oscillating mutually perpendicular to each other and to the direction of wave propagation through space."),

    # 2: Speed of light in vacuum
    ("What is the exact constant propagation speed of all electromagnetic radiation through a vacuum?",
     ["Approximately 3 x 10^8 m/s (300,000 km/s)",
      "Approximately 340 m/s",
      "Approximately 3 x 10^3 m/s",
      "Approximately 1,500 m/s"],
     "A", "OSC", "easy",
     "In a vacuum, all forms of electromagnetic waves (from gamma rays to radio waves) travel at the universal constant velocity c approx 3 x 10^8 m/s (approx 300,000 kilometers per second)."),

    # 3: Wave equation c = nu * lambda
    ("Which mathematical formula correctly connects the speed of light (c), its frequency (nu), and its wavelength (lambda)?",
     ["c = nu * lambda", "c = nu / lambda", "c = lambda / nu", "c = nu^2 * lambda"],
     "A", "OSC", "easy",
     "The universal wave equation states that wave propagation velocity equals the product of its temporal frequency and spatial wavelength (c = nu * lambda). Since c is constant in a vacuum, frequency and wavelength are inversely proportional."),

    # 4: Visible light wavelength window
    ("What is the approximate wavelength range of electromagnetic radiation that human retinas can visually detect?",
     ["400 nm to 800 nm", "1 nm to 10 nm", "10 m to 100 m", "800 nm to 1 mm"],
     "A", "OSC", "easy",
     "Human eye photoreceptors (rods and cones) are biochemically sensitive solely to the narrow visible spectrum spanning wavelengths from approximately 400 nm (violet) to 800 nm (deep red)."),

    # 5: Violet vs Red wavelength
    ("Within the visible light spectrum, which color possesses the shortest wavelength and highest frequency?",
     ["Violet", "Red", "Yellow", "Green"],
     "A", "OSC", "easy",
     "Violet light has the shortest wavelength (~400 nm) and consequently the highest frequency (~7.5 x 10^14 Hz) in the visible band, whereas red light has the longest wavelength (~700-800 nm) and lowest frequency."),

    # 6: Full EM spectrum order by frequency
    ("Which sequence correctly arranges electromagnetic waves in order of INCREASING frequency (and increasing photon energy)?",
     ["Radio waves -> Microwaves -> Infrared -> Visible -> Ultraviolet -> X-rays -> Gamma rays",
      "Gamma rays -> X-rays -> Ultraviolet -> Visible -> Infrared -> Radio waves",
      "Visible -> Infrared -> Ultraviolet -> Radio waves -> X-rays -> Gamma rays",
      "Radio waves -> Gamma rays -> Visible -> Microwaves -> X-rays"],
     "A", "OSC", "medium",
     "Arranged by ascending frequency and photon energy, the spectrum starts with long-wavelength radio waves, progressing through microwaves, infrared, visible, ultraviolet, X-rays, up to extreme high-energy gamma rays."),

    # 7: Longest wavelength in EM spectrum
    ("Which family of electromagnetic waves has the longest wavelengths, typically exceeding 20 centimeters and extending up to kilometers?",
     ["Radio waves", "Gamma rays", "X-rays", "Ultraviolet rays"],
     "A", "OSC", "easy",
     "Radio waves occupy the lowest frequency and longest wavelength regime of the electromagnetic spectrum, with wavelengths ranging from 20 cm to thousands of kilometers, making them ideal for long-distance communication and radio astronomy."),

    # 8: Shortest wavelength in EM spectrum
    ("Which category of electromagnetic radiation possesses the shortest wavelengths (less than 3 picometers) and carries the greatest photon energy?",
     ["Gamma rays", "Microwaves", "Infrared rays", "Radio waves"],
     "A", "OSC", "easy",
     "Gamma rays have sub-picometer wavelengths (lambda < 3 x 10^-12 m) and frequencies exceeding 10^19 Hz, carrying energetic quanta emitted during nuclear transitions, supernovae, and cosmic gamma-ray bursts."),

    # 9: Infrared radiation thermal nature
    ("Why is infrared radiation (wavelengths approx 800 nm to 0.3 mm) commonly known as 'heat radiation'?",
     ["All warm physical bodies, including stars and living organisms, radiate heat primarily in the infrared band due to thermal molecular vibrations",
      "Infrared rays are literally flames of fire traveling in space",
      "Infrared light turns into steam upon touching air",
      "Only boiling water can emit infrared waves"],
     "A", "OSC", "easy",
     "All objects with temperatures above absolute zero radiate thermal energy according to Planck's blackbody law; at everyday terrestrial temperatures (and cool interstellar dust clouds), this thermal blackbody emission peaks squarely within the infrared spectrum."),

    # 10: Ultraviolet radiation hazard and ozone layer
    ("Which atmospheric layer safeguards life on Earth by absorbing hazardous, high-energy solar ultraviolet (UV) radiation?",
     ["The stratospheric Ozone layer (O3)", "The troposphere water clouds", "The ionosphere radio layer", "The mesospheric dust layer"],
     "A", "OSC", "easy",
     "Stratospheric ozone molecules photodissociate upon absorbing lethal solar ultraviolet-B and ultraviolet-C rays (wavelengths 200-315 nm), shielding terrestrial organisms from severe DNA mutagenesis and photochemical tissue burns."),

    # 11: X-rays discovery
    ("Which German physicist discovered X-rays in 1895 while experimenting with high-voltage discharge in cathode ray tubes?",
     ["Wilhelm Conrad Rontgen", "Isaac Newton", "Galileo Galilei", "Heinrich Hertz"],
     "A", "OSC", "easy",
     "Wilhelm Conrad Rontgen discovered penetrating, invisible X-radiation emanating from fluorescent Crookes tubes in November 1895, earning him the inaugural Nobel Prize in Physics in 1901."),

    # 12: Atmospheric optical window
    ("What does the term 'Optical Window' mean in terrestrial astronomical observation?",
     ["The specific wavelength band of visible light (and near-IR) that the Earth's atmosphere allows to pass through to ground level without severe absorption",
      "A glass window cut into an observatory dome roof",
      "A specialized telescope eyepiece lens",
      "The opening in a camera shutter"],
     "A", "OSC", "medium",
     "Earth's atmospheric gases are largely transparent to visible wavelengths between 300 nm and 1,000 nm, allowing ground-based optical telescopes to observe stars directly through this natural atmospheric transmission window."),

    # 13: Atmospheric radio window
    ("Besides visible light, which other broad electromagnetic region penetrates Earth's atmosphere all the way to ground level, enabling giant ground-based telescopes?",
     ["Radio waves (from millimeters up to several meters)", "X-rays", "Extreme ultraviolet rays", "Gamma rays"],
     "A", "OSC", "easy",
     "The Earth's atmosphere features a wide 'radio window' spanning from a few millimeters up to approximately 20 meters, permitting large ground-based parabolic dish radio telescopes (like GMRT) to observe cosmic radio sources uninterruptedly."),

    # 14: Atmospheric absorption of X-rays and Gamma rays
    ("Why is it impossible to operate X-ray and Gamma-ray telescopes directly on the Earth's surface?",
     ["Upper atmospheric nitrogen and oxygen molecules completely absorb high-energy X-ray and gamma-ray photons via photoelectric and Compton scattering",
      "X-ray photons bounce off clouds back into outer space",
      "X-rays only travel during daytime when observatories are closed",
      "Earth's gravitational pull destroys high-frequency photons"],
     "A", "OSC", "medium",
     "The Earth's atmosphere acts as an impenetrable shield equivalent to several meters of solid concrete; dense column densities of atmospheric nitrogen and oxygen absorb all celestial X-rays and gamma rays well before they can reach the ground."),

    # 15: Space telescopes rationale
    ("What is the primary scientific reason for launching space telescopes (like Hubble and Chandra) into orbit above Earth's atmosphere?",
     ["To eliminate atmospheric absorption across UV, X-ray, and IR bands, and to bypass atmospheric turbulence, cloud cover, and city light pollution",
      "To bring the telescope physically closer to distant galaxies by a significant fraction of light-years",
      "Because space has zero gravity, which makes telescope glass completely weightless and free of scratches",
      "To prevent birds and insects from landing on telescope lenses"],
     "A", "OSC", "easy",
     "Placing telescopes in orbit circumvents atmospheric opacity (enabling multi-wavelength observation of UV, X-rays, and IR) and eliminates atmospheric air turbulence ('seeing' jitter), resulting in razor-sharp diffraction-limited astronomical imagery."),

    # 16: Atmospheric turbulence (seeing)
    ("Why do stars appear to 'twinkle' (scintillate) when viewed by human eyes or ground telescopes?",
     ["Pockets of fluctuating atmospheric air densities and temperatures continuously refract light beams along jittering optical paths",
      "Stars rapidly turn their nuclear fusion on and off several times per second",
      "Passing space dust swarms intermittently cover star surfaces",
      "The human eye blinks synchronously with stellar pulses"],
     "A", "OSC", "easy",
     "Turbulent convective currents in Earth's atmosphere cause microscopic refractive index variations that rapidly bend stellar point-source rays in random directions, producing the characteristic twinkling or blurred ground telescopic images."),

    # 17: Light pollution problem
    ("Why are modern professional astronomical observatories intentionally constructed on high, remote mountain peaks far from urban centers?",
     ["To escape urban artificial light pollution, industrial smog, and dense lower-tropospheric atmospheric moisture",
      "To be physically closer to the Moon",
      "Because mountains have less gravity, allowing telescopes to point upward faster",
      "To prevent tourists from asking questions to astronomers"],
     "A", "OSC", "easy",
     "City artificial lighting scatters off airborne aerosols, creating skyglow that drowns out faint celestial objects; remote mountain summits rise above dense inversion fog and light pollution into dry, laminar air."),

    # 18: Photon energy formula E = h*nu
    ("According to Max Planck's quantum formula, how does the energy (E) of a single light photon relate to its frequency (nu)?",
     ["E = h * nu (Energy is directly proportional to frequency)",
      "E = h / nu (Energy is inversely proportional to frequency)",
      "E = h * nu^2",
      "E = nu / h^2"],
     "A", "OSC", "medium",
     "Planck's relation states that photon energy is directly proportional to frequency (E = h*nu, where h is Planck's constant 6.626 x 10^-34 J s). Thus, high-frequency X-rays and gamma rays pack far more energetic punch per photon than low-frequency radio waves."),

    # 19: Microwave wavelength span
    ("What is the approximate wavelength span of microwaves in the electromagnetic spectrum?",
     ["0.3 mm to 20 cm", "400 nm to 800 nm", "3 pm to 300 pm", "10 m to 10 km"],
     "A", "OSC", "medium",
     "Microwaves bridge the boundary between far-infrared and high-frequency radio waves, typically designated between 0.3 millimeters (300 GHz) and 20-30 centimeters (1 GHz), used in radar, satellite links, and cosmic microwave background research."),

    # 20: Cosmic microwave background (CMB)
    ("What cosmic relic radiation filling all of space provides direct empirical evidence for the Big Bang creation of the Universe?",
     ["Cosmic Microwave Background (CMB) radiation with a thermal blackbody temperature of 2.73 Kelvin",
      "Bright green laser beams traversing space",
      "Radio waves broadcast from alien television towers",
      "A steady rain of cosmic ocean water droplets"],
     "A", "OSC", "medium",
     "Discovered by Penzias and Wilson in 1965, the Cosmic Microwave Background is redshifted thermal radiation from the primordial hot Big Bang era (~380,000 years after inception), cooled by cosmic expansion to a uniform 2.73 K microwave glow."),

    # 21: Multi-wavelength astronomy importance
    ("Why cannot astronomers rely solely on visible optical light to comprehend the physical structure of the cosmos?",
     ["Celestial phenomena emit signatures across different EM bands: cold dust radiates infrared, neutral hydrogen emits radio, while superheated accretion disks around black holes radiate X-rays",
      "Visible light is illegal to observe from space satellites",
      "All stars in the universe stop emitting visible light during nighttime",
      "Visible light photons travel much slower than radio waves in space"],
     "A", "OSC", "easy",
     "No single wavelength band reveals the complete universe: cold dark molecular clouds conceal newborn stars observable only in infrared, pulsar magnetic poles emit radio beams, and violent black hole jets blaze in X-rays and gamma rays."),

    # 22: Nanometer unit conversion
    ("How many meters are equivalent to one nanometer (1 nm), the standard SI unit used to quantify visible light wavelengths?",
     ["1 x 10^-9 meters", "1 x 10^-6 meters", "1 x 10^-12 meters", "1 x 10^-3 meters"],
     "A", "OSC", "easy",
     "One nanometer (1 nm) equals one-billionth of a meter (10^-9 m). For instance, green light of wavelength 550 nm equals 5.5 x 10^-7 meters."),

    # 23: Picometer unit conversion
    ("How many meters are equivalent to one picometer (1 pm), the unit commonly used to quantify X-ray and gamma-ray wavelengths?",
     ["1 x 10^-12 meters", "1 x 10^-9 meters", "1 x 10^-15 meters", "1 x 10^-6 meters"],
     "A", "OSC", "easy",
     "One picometer (1 pm) equals one-trillionth of a meter (10^-12 m). X-rays span 3 to 300 picometers, matching atomic electron-shell dimensions."),

    # 24: Heinrich Hertz radio wave confirmation
    ("Which scientist experimentally confirmed James Clerk Maxwell's theoretical prediction of electromagnetic waves by generating and detecting radio waves in a laboratory in 1887?",
     ["Heinrich Hertz", "Thomas Edison", "Albert Einstein", "Niels Bohr"],
     "A", "OSC", "easy",
     "Heinrich Hertz constructed spark-gap transmitters and resonant loop receivers in 1887, proving that electromagnetic sparks produce oscillating waves traveling at the speed of light, inaugurating radio frequency science."),

    # 25: Thermal radiation and infrared telescopes
    ("Why must space-based infrared telescopes (like Spitzer or James Webb Space Telescope) be cryogenically cooled down to temperatures near absolute zero?",
     ["To prevent thermal infrared emission from the telescope's own mirrors and electronics from blinding its ultrasensitive infrared detectors",
      "To prevent the telescope glass from evaporating into gas",
      "Because cold mirrors reflect light faster than warm mirrors",
      "To freeze the cosmic photons into solid crystals"],
     "A", "OSC", "hard",
     "At room temperature, telescope mirrors and instruments glow brightly in the infrared band; without deep cryogenic cooling (using liquid helium or sunshields to reach <50 K), internal instrument heat swamping would drown out faint infrared signals from distant protostars."),

    # 26: 21 cm Neutral Hydrogen radio line
    ("In radio astronomy, what is the significance of the famous '21 cm line' (frequency 1420.4 MHz)?",
     ["It is emitted during hyperfine spin-flip transitions of neutral atomic hydrogen, enabling astronomers to map the spiral arms of our Milky Way through interstellar dust",
      "It is the wavelength used by police speed radars",
      "It is the sound of lightning striking planets",
      "It represents the exact diameter of the Moon"],
     "A", "OSC", "hard",
     "Interstellar dust absorbs visible light completely across the galactic plane, but the 21 cm radio line emitted by neutral hydrogen penetrates interstellar dust unimpeded, allowing radio astronomers to map the Milky Way's massive spiral structure."),

    # 27: Electromagnetic wave components
    ("What are the mutually perpendicular components that propagate together through space in an electromagnetic wave?",
     ["An oscillating Electric field (E) and an oscillating Magnetic field (B)",
      "A gravity wave and a sound wave",
      "A water stream and an air stream",
      "An electron beam and a proton beam"],
     "A", "OSC", "easy",
     "Maxwell demonstrated that an oscillating electric field induces an in-phase oscillating magnetic field, and vice versa; these coupled perpendicular fields sustain each other's propagation through vacuum without requiring a material medium."),

    # 28: Gamma-ray bursts (GRB)
    ("What are Gamma-Ray Bursts (GRBs), observed by space observatories like Swift and Fermi?",
     ["The most energetic cataclysmic cosmic explosions in the universe, triggered by the core-collapse of massive stars into black holes or merging neutron stars",
      "Lightning strikes in Jupiter's atmosphere",
      "Solar flares burning away the Moon's dust",
      "Exploding space station batteries"],
     "A", "OSC", "medium",
     "Gamma-Ray Bursts release more energy in a matter of seconds than our Sun will emit over its entire 10-billion-year lifespan, arising from collimated ultra-relativistic relativistic jets produced during collapsars or neutron star mergers."),

    # 29: Electromagnetic spectrum frequency unit
    ("What is the standard SI unit of frequency, representing one complete oscillation cycle per second?",
     ["Hertz (Hz)", "Joule (J)", "Watt (W)", "Newton (N)"],
     "A", "OSC", "easy",
     "Frequency is measured in Hertz (Hz), named in honor of Heinrich Hertz. One Hertz corresponds to one complete wave cycle or vibration passing a fixed point in one second."),

    # 30: Transverse nature of EM waves
    ("Why are all electromagnetic waves classified as 'Transverse waves' rather than 'Longitudinal waves'?",
     ["Because the electric and magnetic field oscillations occur perpendicular to the direction of wave advance",
      "Because they can only travel horizontally along the ground",
      "Because their speed changes with every second",
      "Because they require air to vibrate back and forth"],
     "A", "OSC", "medium",
     "In transverse waves, the physical disturbances (electric and magnetic vector oscillations) oscillate at right angles to the Poynting vector (wave travel direction), in contrast to longitudinal sound waves where compressions move parallel to propagation."),

    # 31: Reflection and refraction of visible light
    ("What optical phenomenon occurs when visible light transitions from air into a denser medium like glass, causing its speed to decrease and its path to bend?",
     ["Refraction", "Nuclear fission", "Total absorption", "Doppler shift"],
     "A", "OSC", "easy",
     "Refraction is the change in the direction and velocity of a wavefront as it passes obliquely across the boundary between two transparent optical media having different refractive indices."),

    # 32: Dispersion of white light through a prism
    ("When a beam of white sunlight passes through a glass prism, why does it disperse into a continuous spectrum of seven distinct colors (VIBGYOR)?",
     ["Because different wavelengths of light have different refractive indices in glass and refract through slightly different angles",
      "Because the glass prism paints the light with built-in dyes",
      "Because red light is destroyed inside the glass",
      "Because sunlight contains seven different chemical liquids"],
     "A", "OSC", "medium",
     "Glass has normal optical dispersion: shorter wavelengths (violet, ~400 nm) experience a higher refractive index and bend most sharply, while longer wavelengths (red, ~700 nm) experience a lower refractive index and bend least, splitting white light into rainbow colors."),

    # 33: Black hole accretion disks and X-rays
    ("Why do supermassive black holes at the centers of active galaxies emit intense X-ray radiation, even though nothing can escape from beyond their event horizons?",
     ["Gas and stellar matter swirling into the black hole undergo extreme gravitational compression and viscous friction, heating the accretion disk to millions of degrees",
      "The black hole's surface reflects light like a silver mirror",
      "Black holes burn coal and petroleum at their poles",
      "The event horizon radiates green chemical smoke"],
     "A", "OSC", "hard",
     "While nothing escapes beyond the event horizon, infalling plasma outside the horizon in the accretion disk converts gravitational potential energy into scorching thermal friction (temperatures reaching 10^7 Kelvin), emitting furious X-ray photons."),

    # 34: Radio waves penetrating interstellar dust
    ("Why are radio waves uniquely suited for peering deep into the center of our Milky Way galaxy?",
     ["Radio wavelengths (centimeters to meters) are far larger than interstellar dust grains (~0.1 micron), allowing them to pass through dense dust lanes without scattering",
      "Radio waves travel faster than visible light in space",
      "Interstellar dust acts like an antenna that multiplies radio waves",
      "Radio waves destroy all dust clouds they encounter"],
     "A", "OSC", "medium",
     "Rayleigh scattering cross-section is inversely proportional to the fourth power of wavelength (1/lambda^4); because radio waves are millions of times longer than visible light, they glide past microscopic dust grains with zero scattering loss."),

    # 35: Infrared detection of protostars
    ("Why are infrared telescopes essential for discovering 'protostars' (baby stars) inside stellar nurseries like the Orion Nebula?",
     ["Protostars are cloaked inside cold, opaque interstellar molecular gas clouds that completely block visible light, but infrared heat penetrates the dust",
      "Protostars do not emit any light whatsoever",
      "Protostars only exist in universes outside our own",
      "Visible light telescopes are prohibited by law from looking at nebulae"],
     "A", "OSC", "easy",
     "Dense clouds of interstellar gas and dust extinguish visible starlight by up to 30 magnitudes; however, infrared radiation passes freely through the dust shroud, revealing glowing protostellar embryos within."),

    # 36: Ozone photodissociation mechanism
    ("What chemical reaction in the stratosphere protects the biosphere from dangerous solar UV-B radiation?",
     ["Ozone (O3) absorbs high-energy UV photons and dissociates into molecular oxygen (O2) and a free oxygen atom (O)",
      "Ozone freezes into solid nitrogen ice",
      "Ozone converts UV light into liquid water rain",
      "Ozone reflects light like a flat silver mirror"],
     "A", "OSC", "medium",
     "In the Chapman mechanism, stratospheric ozone molecules absorb solar UV-B radiation (240-310 nm), breaking the chemical bond to produce O2 and a highly reactive O atom; these species recombine into ozone, dissipating energetic photons harmlessly as thermal heat."),

    # 37: Electromagnetic spectrum energy ranking
    ("Which of the following forms of electromagnetic radiation carries the LOWEST photon energy?",
     ["Radio waves", "Visible light", "X-rays", "Ultraviolet rays"],
     "A", "OSC", "easy",
     "Because photon energy is directly proportional to frequency (E = h*nu) and inversely proportional to wavelength, radio waves have the lowest frequency and therefore carry the lowest quantum energy of all EM waves."),

    # 38: X-ray wavelength match to atomic spacing
    ("Why are X-rays particularly valuable for crystallographers determining the three-dimensional structures of complex proteins and minerals?",
     ["X-ray wavelengths (0.01 to 10 nm) are comparable to the interatomic spacing in crystal lattices, creating sharp diffraction patterns",
      "X-rays change the color of mineral crystals to gold",
      "X-rays dissolve crystal bonds into water",
      "X-rays make crystals grow ten times larger"],
     "A", "OSC", "medium",
     "Bragg's law of X-ray diffraction requires the probing radiation wavelength to be of the same order of magnitude as the spacing between crystal atomic planes (~0.1-1 nm), enabling crystallographers to reconstruct exact 3D electron density maps."),

    # 39: James Webb Space Telescope (JWST) primary wavelength
    ("In which primary electromagnetic regime does the James Webb Space Telescope (JWST) operate to observe the earliest, highest-redshift galaxies in the universe?",
     ["Infrared (Near-Infrared and Mid-Infrared)", "Gamma rays", "Hard X-rays", "Extreme Ultraviolet"],
     "A", "OSC", "medium",
     "Due to cosmological expansion, ultraviolet and visible light emitted by the earliest stars 13.5 billion years ago has been stretched (cosmologically redshifted) into infrared wavelengths; JWST's gold-coated beryllium mirrors and infrared detectors capture these distant signals."),

    # 40: Earth's atmospheric opacity curve
    ("In summary, which two broad wavelength regimes represent Earth's primary natural atmospheric transmission windows through which ground-based astronomy can operate?",
     ["The Optical Window (visible light) and the Radio Window (radio waves)",
      "The X-ray Window and the Gamma-ray Window",
      "The Ultraviolet Window and the Microwave Window",
      "The Submillimeter Window and the Infrared Window"],
     "A", "OSC", "easy",
     "Ground-based astronomy was historically restricted to the Optical Window (400-800 nm) and the Radio Window (cm to meters), as all intermediate and shorter high-energy wavelengths (UV, X-rays, Gamma rays) are filtered out by atmospheric gases.")
]

practice_data = [
    # 41: Wavelength calculation c = nu * lambda
    ("A radio transmitter broadcasts electromagnetic waves at a frequency of 100 MHz (10^8 Hz). Given the speed of light is 3 x 10^8 m/s, what is the wavelength of these radio waves?",
     ["3 meters", "0.33 meters", "30 meters", "300 meters"],
     "A", "OSC", "easy",
     "Wavelength lambda = c / nu = (3 x 10^8 m/s) / (100 x 10^6 Hz) = 3 meters. This belongs to the VHF FM radio broadcast band."),

    # 42: Green light frequency calculation
    ("A green laser pointer emits light with a wavelength of 500 nm (5 x 10^-7 m). Given c = 3 x 10^8 m/s, what is the oscillation frequency of this green light?",
     ["6 x 10^14 Hz", "1.5 x 10^15 Hz", "6 x 10^12 Hz", "1.5 x 10^8 Hz"],
     "A", "OSC", "medium",
     "Frequency nu = c / lambda = (3 x 10^8 m/s) / (5 x 10^-7 m) = 6 x 10^14 Hz (600 Terahertz)."),

    # 43: Red vs Violet energy comparison
    ("How does the quantum energy of a violet light photon (lambda = 400 nm) compare to that of a red light photon (lambda = 800 nm)?",
     ["The violet photon carries exactly TWICE the energy of the red photon",
      "The red photon carries twice the energy of the violet photon",
      "Both photons carry the exact same energy",
      "The violet photon carries four times less energy"],
     "A", "OSC", "medium",
     "Photon energy E = hc / lambda. Because the wavelength of violet light (400 nm) is half that of red light (800 nm), its photon energy is precisely double (E_violet = 2 * E_red)."),

    # 44: Electromagnetic nature of X-rays vs Sound
    ("Why can X-rays and visible light traverse the vast vacuum of outer space from distant stars, whereas sound waves cannot travel through space?",
     ["Electromagnetic waves require no material medium to propagate, whereas mechanical sound waves strictly require a material medium of vibrating particles",
      "Sound waves travel too slowly to ever reach Earth",
      "Space is too cold for sound waves to survive",
      "Stars refuse to emit sound waves"],
     "A", "OSC", "easy",
     "Sound is a mechanical disturbance requiring particle collisions in an elastic material medium; electromagnetic waves consist of self-sustaining oscillations of electric and magnetic fields that propagate effortlessly through a vacuum."),

    # 45: Microwaves in household ovens
    ("Why do domestic microwave ovens operate at an electromagnetic frequency of approximately 2.45 GHz (wavelength ~12.2 cm)?",
     ["This frequency is readily absorbed by dipolar water and fat molecules in food, causing rapid molecular rotation that generates frictional heat",
      "This frequency ionizes atomic nuclei to create nuclear reactions",
      "This frequency freezes food instantly",
      "This frequency turns water into pure hydrogen gas"],
     "A", "OSC", "medium",
     "At 2.45 GHz, oscillating electric fields induce dielectric heating: asymmetric polar water molecules in food continuously rotate to align with the alternating field (billions of times per second), dissipating kinetic friction into heat."),

    # 46: Ultraviolet radiation classification (UVA, UVB, UVC)
    ("Which category of solar ultraviolet radiation possesses the shortest wavelength and highest hazard, but is fortunately 100% absorbed by atmospheric oxygen and ozone?",
     ["UV-C (100 to 280 nm)", "UV-A (315 to 400 nm)", "UV-B (280 to 315 nm)", "Visible blue light"],
     "A", "OSC", "medium",
     "UV-C radiation (100-280 nm) is extremely energetic and lethal to living cells, but stratospheric O2 and O3 absorb 100% of extraterrestrial UV-C before it can ever touch the Earth's surface."),

    # 47: Infrared thermography applications
    ("How do thermal night-vision infrared cameras reveal animals or humans moving in total pitch-black darkness?",
     ["By detecting the natural mid- and far-infrared radiation (~10 micron wavelength) emitted by warm living bodies according to their skin temperature",
      "By shining invisible green searchlights on the targets",
      "By detecting the sound of human breathing",
      "By sensing the gravitational pull of the body"],
     "A", "OSC", "easy",
     "Human body temperature (~37°C or 310 K) emits blackbody radiation peaking around 9.3 micrometers in the thermal infrared; bolometer sensor arrays detect these infrared emissions and map them as a false-color visual heat image."),

    # 48: Radio astronomy dish size requirement
    ("Why do radio telescopes require vastly larger apertures (dishes tens or hundreds of meters wide) compared to small optical telescopes to achieve comparable angular resolution?",
     ["Because the angular resolution depends on lambda / D; since radio wavelengths are millions of times longer than visible light, the aperture diameter (D) must be proportionally huge",
      "Because radio waves are heavier than visible photons",
      "Because small dishes break when radio waves hit them",
      "Because radio astronomers like building giant steel statues"],
     "A", "OSC", "hard",
     "Diffraction-limited angular resolution theta is proportional to lambda / D. Because radio wavelengths (centimeters) are roughly 100,000 times longer than visible light (nanometers), an aperture must be massive to distinguish two adjacent point sources in the sky."),

    # 49: Atmospheric absorption of Infrared by greenhouse gases
    ("Which gases in Earth's lower atmosphere are primarily responsible for absorbing extraterrestrial and outgoing terrestrial infrared radiation?",
     ["Water vapor (H2O) and Carbon dioxide (CO2)", "Pure Argon gas", "Helium and Neon", "Solid iron dust"],
     "A", "OSC", "easy",
     "Triatomic molecules such as H2O and CO2 possess vibrational dipole modes that strongly absorb infrared wavelengths, forming the natural greenhouse effect and obscuring much of the infrared universe from sea-level observatories."),

    # 50: Gamma ray telescope mechanism (Scintillation crystals)
    ("Why cannot conventional curved glass lenses or polished optical mirrors focus celestial gamma-ray photons?",
     ["Gamma-ray photons are so energetic that they penetrate directly into glass and mirror atoms without reflecting, interacting instead via pair production and Compton scattering",
      "Gamma rays are too wide to hit telescope mirrors",
      "Glass lenses turn gamma rays into ice",
      "Gamma rays only travel along straight laser guides"],
     "A", "OSC", "hard",
     "Gamma rays have wavelengths shorter than atomic radii; optical reflection cannot occur because the photons pass straight between atoms or ionize electrons. Gamma telescopes must use heavy scintillation crystals, tungsten masks, and silicon tracking detectors to record arrival vectors."),

    # 51: Doppler effect in astronomy (Redshift vs Blueshift)
    ("When a distant star or galaxy is moving rapidly AWAY from Earth, what observable shift occurs in its spectral absorption lines?",
     ["Redshift: the observed wavelengths are stretched toward longer, redder wavelengths",
      "Blueshift: the observed wavelengths are compressed toward shorter, bluer wavelengths",
      "The spectral lines turn into sound waves",
      "The lines disappear into complete darkness"],
     "A", "OSC", "medium",
     "The relativistic Doppler effect stretches light waves emitted by receding celestial sources: spectral absorption lines shift toward the red (longer wavelength) end of the spectrum, providing the foundation for Edwin Hubble's discovery of the expanding universe."),

    # 52: Supernova remnants and X-ray emission
    ("Why do expanding supernova remnants (like the Crab Nebula or Cassiopeia A) glow intensely in X-rays for thousands of years after the explosion?",
     ["Shockwaves from the stellar explosion heat interstellar gas to tens of millions of degrees Kelvin, generating hot thermal bremsstrahlung plasma emission",
      "The exploded star burns like a giant coal bonfire",
      "The supernova remnant is coated in glowing radioactive gold paint",
      "Alien civilizations shine searchlights on the remnant"],
     "A", "OSC", "hard",
     "The hypersonic blast wave from a core-collapse supernova drives shock fronts through the interstellar medium at thousands of km/s, thermalizing gas into million-degree ionized plasma that shines brightly in the X-ray regime."),

    # 53: Polarization of light
    ("What optical property proves conclusively that electromagnetic light is a transverse wave rather than a longitudinal wave?",
     ["Polarization: light can be filtered to oscillate strictly within a single spatial plane",
      "Total internal reflection",
      "Dispersion through water droplets",
      "Color changes at sunset"],
     "A", "OSC", "medium",
     "Only transverse waves can be polarized; longitudinal waves (like sound) vibrate exclusively parallel to propagation and cannot be restricted to an orientation plane. Polaroid filters block electric field vectors oscillating outside a designated transmission axis."),

    # 54: Solar spectrum peak wavelength
    ("According to Wien's displacement law, the surface of our Sun (temperature ~5800 K) radiates electromagnetic energy with its peak intensity in which band?",
     ["Visible green-yellow light (~500 nm)", "Extreme X-rays (~0.1 nm)", "Long radio waves (~100 m)", "Submillimeter microwaves (~1 mm)"],
     "A", "OSC", "medium",
     "Wien's law (lambda_max * T = 2.898 x 10^-3 m K) dictates that for a 5,800 K stellar photosphere, maximum radiative intensity occurs at lambda approx 500 nm, directly in the visible green-yellow band to which human vision evolved maximum sensitivity."),

    # 55: High altitude observatories in Ladakh (Hanle)
    ("Why did the Indian Institute of Astrophysics construct the Indian Astronomical Observatory at Hanle in Ladakh at an elevation of 4,500 meters?",
     ["The extreme altitude provides exceptionally low atmospheric water vapor, cloudless dry skies, low atmospheric pressure, and near-zero light pollution",
      "Hanle is closer to the North Pole than any other place in India",
      "To protect the telescope from ocean tsunamis",
      "Because telescopes can only be operated in freezing snow"],
     "A", "OSC", "easy",
     "Perched high on Mount Saraswati in the cold desert of Ladakh, Hanle rises above 50% of the Earth's atmosphere and almost all water vapor, yielding crystal-clear optical and infrared viewing conditions unmatched in mainland India."),

    # 56: Gravitational waves vs EM waves distinction
    ("How do newly discovered Gravitational Waves (detected by LIGO) fundamentally differ from Electromagnetic Waves?",
     ["Gravitational waves are ripples in the fabric of spacetime itself produced by accelerating massive bodies, whereas EM waves are propagating disturbances in electric and magnetic fields",
      "Gravitational waves travel at double the speed of light",
      "Electromagnetic waves can only travel through solid metals",
      "Gravitational waves are visible to the naked eye as purple light"],
     "A", "OSC", "medium",
     "Gravitational waves represent quadrupolar strain oscillations of spacetime geometry caused by massive binary black hole or neutron star coalescences, whereas electromagnetic waves are dipolar vector oscillations that interact with electric charges."),

    # 57: Ultraviolet water purification
    ("Why is germicidal ultraviolet (UV-C) radiation of wavelength ~254 nm widely used in drinking water purifiers?",
     ["It is absorbed by microbial DNA and RNA, forming thymine dimers that destroy the pathogen's ability to replicate",
      "It boils the water into steam instantly",
      "It filters dirt out of water like a paper sieve",
      "It adds chlorine chemicals to the water"],
     "A", "OSC", "easy",
     "UV-C radiation at 254 nm corresponds to peak DNA absorption; it induces photochemical cross-linking (cyclobutane pyrimidine dimers) between adjacent thymines, jamming bacterial and viral replication and rendering microbes non-infectious without chemicals."),

    # 58: Radio astronomy aperture synthesis
    ("How do radio astronomers achieve pinpoint angular resolution without having to construct a physically impossible 25-kilometer-wide solid metal dish?",
     ["By Aperture Synthesis: combining signals from an array of separate dishes spread across 25 km using interferometry computers to synthesize a giant virtual aperture",
      "By placing magnifying glasses in front of radio dishes",
      "By shining bright lasers onto the radio antennas",
      "By flying radio telescopes on jet airplanes"],
     "A", "OSC", "hard",
     "Aperture synthesis (pioneered by Martin Ryle) links an array of widely separated antennas with microsecond atomic clocks, computationally correlating their phase delays to achieve the angular sharpness of a single monstrous dish spanning the entire baseline."),

    # 59: Cosmic rays vs Gamma rays distinction
    ("Why are primary 'Cosmic Rays' (detected from space) scientifically distinct from 'Gamma Rays'?",
     ["Cosmic rays are high-energy subatomic charged particles (protons and atomic nuclei), whereas gamma rays are electromagnetic photons with zero charge and zero rest mass",
      "Cosmic rays are radio waves while gamma rays are sound waves",
      "Cosmic rays travel faster than light while gamma rays do not",
      "Cosmic rays only come from the Moon"],
     "A", "OSC", "medium",
     "Despite the historical name 'rays', cosmic rays consist of relativistic charged matter (approx 90% protons, 9% alpha particles, 1% heavy nuclei) deflected by magnetic fields, unlike uncharged gamma-ray photons which travel in straight trajectories."),

    # 60: Astronomical unit (AU) and light-year
    ("What astronomical unit of length is defined as the total distance traversed by an electromagnetic light photon through a vacuum in one Julian year (approx 9.46 x 10^12 km)?",
     ["One Light-Year", "One Astronomical Unit (AU)", "One Parsec", "One Kilometer"],
     "A", "OSC", "easy",
     "A light-year is the astronomical measure of distance that light covers in one full year: Distance = c * time = (3 x 10^8 m/s) * (365.25 * 86,400 s) approx 9.46 x 10^12 kilometers (9.46 trillion km)."),

    # 61: Multiple choice OMC on EM spectrum order
    ("Which of the following electromagnetic radiations have HIGHER frequency than visible light? (Select all that apply)",
     ["Ultraviolet rays", "X-rays", "Gamma rays", "Radio waves"],
     "A,B,C", "OMC", "easy",
     "Ultraviolet, X-rays, and gamma rays possess shorter wavelengths and higher frequencies than visible light, making them ionizing and high-energy. Radio waves have much lower frequencies."),

    # 62: Multiple choice OMC on atmospheric transparency
    ("Which electromagnetic wavelength bands are severely BLOCKED or absorbed by the Earth's atmosphere, necessitating space observatories? (Select all that apply)",
     ["X-rays", "Gamma rays", "Extreme Ultraviolet (UV)", "Visible light"],
     "A,B,C", "OMC", "medium",
     "Earth's atmosphere is completely opaque to X-rays, gamma rays, and far-UV, protecting the biosphere. Visible light penetrates freely through the optical window."),

    # 63: Multiple choice OMC on light wave properties
    ("Which of the following physical characteristics are TRUE for all electromagnetic waves in a vacuum? (Select all that apply)",
     ["They all travel at the same velocity (c approx 3 x 10^8 m/s)",
      "They are all transverse waves of oscillating E and B fields",
      "They can propagate through empty vacuum without any material medium",
      "They all carry identical photon energies regardless of frequency"],
     "A,B,C", "OMC", "medium",
     "All EM waves travel at velocity c in a vacuum, require no material medium, and are transverse. However, their photon energy varies with frequency (E = h*nu), so they do NOT carry identical energies."),

    # 64: True or False on speed of different light colors
    ("State whether True or False: In a vacuum, blue light photons travel faster than red light photons because blue light has higher energy.",
     ["True", "False"],
     "B", "OTF", "easy",
     "False. In a vacuum, all electromagnetic waves travel at the exact same invariant speed (c = 300,000 km/s), regardless of their frequency, wavelength, or quantum energy."),

    # 65: True or False on radio waves penetration
    ("State whether True or False: Radio waves from space easily penetrate through rain, clouds, and interstellar dust that completely block optical visible light.",
     ["True", "False"],
     "A", "OTF", "easy",
     "True. Because radio wavelengths (cm to meters) are vastly larger than water droplets, smoke particles, and interstellar dust, they suffer negligible scattering and pass through clouds unimpeded."),

    # 66: True or False on space telescope distance myth
    ("State whether True or False: The primary purpose of space telescopes is to get physically closer to distant stars to view them larger.",
     ["True", "False"],
     "B", "OTF", "easy",
     "False. Orbiting 500 km above Earth brings a telescope insignificantly closer to stars that are trillions of kilometers away. The actual purpose is to escape atmospheric absorption, air turbulence, and light pollution."),

    # 67: Assertion and Reason on Space X-ray Telescopes
    ("Assertion (A): X-ray telescopes like Chandra must be launched into space orbits high above Earth's atmosphere.\nReason (R): Earth's dense atmospheric gases absorb celestial X-rays completely, preventing them from reaching ground-based observatories.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "The nitrogen and oxygen molecules of our atmosphere absorb all cosmic X-ray photons; consequently, X-ray astronomy is physically impossible from the Earth's surface and requires spaceborne observatories."),

    # 68: Assertion and Reason on Frequency and Energy
    ("Assertion (A): Gamma rays cause severe biological radiation sickness and DNA mutations, whereas radio waves do not.\nReason (R): Gamma-ray photons carry orders of magnitude greater quantum energy (E = h*nu) capable of ionizing atoms and breaking molecular bonds.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "High-frequency gamma photons exceed atomic ionization thresholds, stripping orbital electrons and severing DNA phosphodiester backbones, whereas low-frequency radio photons lack the energy to ionize atoms."),

    # 69: Fill in the blank on Visible Spectrum
    ("Fill in the blank: The wavelength of visible light ranges from approximately 400 nm for violet to ________ nm for deep red light.",
     ["800", "100", "2000", "50"],
     "A", "OFB", "easy",
     "The human visible spectrum begins at violet (~400 nm) and terminates at deep red (~750 to 800 nm), beyond which lies the infrared spectrum."),

    # 70: Numerical objective on frequency of red light
    ("Calculate the frequency of red light having a wavelength of 750 nm (7.5 x 10^-7 m) in a vacuum, given c = 3 x 10^8 m/s.",
     ["4 x 10^14 Hz", "2.5 x 10^14 Hz", "5 x 10^8 Hz", "1.5 x 10^15 Hz"],
     "A", "ONE", "easy",
     "Frequency nu = c / lambda = (3 x 10^8 m/s) / (7.5 x 10^-7 m) = 0.4 x 10^15 Hz = 4 x 10^14 Hz (400 Terahertz).")
]

mock_data = [
    # 71: Complete Electromagnetic Spectrum Wavelength Chart
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Frequency Arrow (Left to Right) -->
  <line x1="30" y1="25" x2="370" y2="25" stroke="#facc15" stroke-width="2"/>
  <polygon points="370,25 360,20 360,30" fill="#facc15"/>
  <text x="200" y="18" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">INCREASING FREQUENCY & PHOTON ENERGY (nu ->)</text>
  <!-- Spectrum Bands -->
  <!-- Radio -->
  <rect x="25" y="40" width="50" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="50" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Radio</text>
  <text x="50" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">>20 cm</text>
  <!-- Micro -->
  <rect x="78" y="40" width="50" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="103" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Micro</text>
  <text x="103" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">0.3mm-20cm</text>
  <!-- Infrared -->
  <rect x="131" y="40" width="50" height="50" rx="4" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="156" y="60" fill="#f43f5e" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Infrared</text>
  <text x="156" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">800nm-0.3mm</text>
  <!-- Visible (Highlighted Rainbow) -->
  <rect x="184" y="35" width="55" height="60" rx="5" fill="#047857" stroke="#34d399" stroke-width="2"/>
  <text x="211" y="55" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">VISIBLE</text>
  <text x="211" y="70" fill="#fef08a" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">400-800 nm</text>
  <text x="211" y="82" fill="#bbf7d0" font-size="6" font-family="sans-serif" text-anchor="middle">Human Eye</text>
  <!-- UV -->
  <rect x="242" y="40" width="45" height="50" rx="4" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="264" y="60" fill="#c084fc" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">UV</text>
  <text x="264" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">300pm-400nm</text>
  <!-- X-ray -->
  <rect x="290" y="40" width="45" height="50" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="312" y="60" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">X-rays</text>
  <text x="312" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">3-300 pm</text>
  <!-- Gamma -->
  <rect x="338" y="40" width="45" height="50" rx="4" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
  <text x="360" y="60" fill="#f472b6" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Gamma</text>
  <text x="360" y="75" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle"><3 pm</text>
  <!-- Wavelength Arrow (Right to Left) -->
  <line x1="370" y1="110" x2="30" y2="110" stroke="#4ade80" stroke-width="2"/>
  <polygon points="30,110 40,105 40,115" fill="#4ade80"/>
  <text x="200" y="125" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">(<- lambda) INCREASING WAVELENGTH (Longer Waves)</text>
  <!-- Atmospheric Window Labels below -->
  <rect x="25" y="140" width="105" height="45" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1"/>
  <text x="77" y="158" fill="#93c5fd" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Radio Window</text>
  <text x="77" y="172" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Reaches Ground!</text>
  <rect x="184" y="140" width="55" height="45" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="1"/>
  <text x="211" y="158" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Optical</text>
  <text x="211" y="172" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Ground!</text>
  <rect x="250" y="140" width="130" height="45" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="315" y="158" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Blocked by Atmosphere!</text>
  <text x="315" y="172" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Requires Space Telescopes</text>
</svg>
</div>
Based on the electromagnetic spectrum diagram above, how do wavelength and photon frequency correlate across the spectrum?""",
     ["Wavelength and frequency are inversely proportional: as frequency increases from radio to gamma rays, wavelength progressively shrinks",
      "Wavelength and frequency increase simultaneously together",
      "All electromagnetic waves have the exact same wavelength of 500 nm",
      "Gamma rays have longer wavelengths than radio waves"],
     "A", "OSC", "easy",
     "Because wave speed c is invariant in vacuum (c = nu * lambda), frequency and wavelength exhibit a strict inverse relationship: high-frequency gamma rays have sub-picometer wavelengths, whereas low-frequency radio waves span meters to kilometers."),

    # 72: Electromagnetic Transverse Wave Vector Structure
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Axis -->
  <line x1="40" y1="100" x2="360" y2="100" stroke="#64748b" stroke-width="2"/>
  <polygon points="360,100 350,95 350,105" fill="#64748b"/>
  <text x="340" y="115" fill="#94a3b8" font-size="8" font-family="sans-serif">Propagation (c)</text>
  <!-- Electric Field Curve (Vertical Sine - Red) -->
  <path d="M 50 100 Q 100 20 150 100 T 250 100 T 350 100" stroke="#f43f5e" stroke-width="3" fill="none"/>
  <!-- Magnetic Field Curve (Horizontal Plane - Cyan) -->
  <path d="M 50 100 Q 80 140 150 100 T 220 60 T 250 100" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3" fill="none"/>
  <!-- Field Labels -->
  <line x1="100" y1="50" x2="100" y2="100" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="100" y="40" fill="#f43f5e" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Electric Field (E)</text>
  <text x="100" y="150" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Magnetic Field (B)</text>
  <!-- Info Box -->
  <rect x="200" y="125" width="180" height="60" rx="5" fill="#090d16" stroke="#facc15" stroke-width="1"/>
  <text x="290" y="145" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Key Wave Invariants:</text>
  <text x="290" y="160" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1. E perpendicular to B</text>
  <text x="290" y="174" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">2. Both perpendicular to Propagation (c)</text>
</svg>
</div>
What structural orientation relationship governs the Electric field (E) and Magnetic field (B) in an electromagnetic wave?""",
     ["The electric field vector and magnetic field vector oscillate perpendicular to each other, and both are perpendicular to the direction of wave advance",
      "The electric and magnetic fields point in the exact same direction parallel to travel",
      "The magnetic field is always zero in outer space",
      "The electric field travels in circles while the magnetic field stays stationary"],
     "A", "OSC", "medium",
     "Electromagnetic waves are transverse: the oscillating electric field (E) and magnetic field (B) vectors are perpendicular to each other and mutually perpendicular to the Poynting vector direction of wave propagation."),

    # 73: Atmospheric Opacity vs Altitude Graph
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Altitude Layer Markers -->
  <text x="50" y="30" fill="#38bdf8" font-size="8" font-family="sans-serif">Space (>500 km) -> Hubble & Chandra Orbit</text>
  <line x1="30" y1="35" x2="370" y2="35" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2"/>
  <text x="50" y="70" fill="#c084fc" font-size="8" font-family="sans-serif">Stratosphere (Ozone Layer: Absorbs UV)</text>
  <line x1="30" y1="75" x2="370" y2="75" stroke="#c084fc" stroke-width="1" stroke-dasharray="2"/>
  <text x="50" y="120" fill="#facc15" font-size="8" font-family="sans-serif">High Mountains (Ladakh / Hawaii): Optical & Near-IR</text>
  <line x1="30" y1="125" x2="370" y2="125" stroke="#facc15" stroke-width="1" stroke-dasharray="2"/>
  <!-- Ground level -->
  <rect x="30" y="160" width="340" height="25" fill="#334155"/>
  <text x="200" y="177" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sea Level: Optical Window (400-800nm) & Radio Window (cm-m) ONLY</text>
  <!-- Incoming Beams -->
  <!-- Gamma/X-ray absorbed high -->
  <line x1="330" y1="15" x2="330" y2="55" stroke="#ef4444" stroke-width="3"/>
  <text x="330" y="65" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">X-rays Blocked</text>
  <!-- UV absorbed mid -->
  <line x1="260" y1="15" x2="260" y2="75" stroke="#a855f7" stroke-width="3"/>
  <text x="260" y="85" fill="#c084fc" font-size="7" font-family="sans-serif" text-anchor="middle">UV Absorbed</text>
  <!-- Optical reaches ground -->
  <line x1="180" y1="15" x2="180" y2="160" stroke="#4ade80" stroke-width="3"/>
  <text x="180" y="150" fill="#4ade80" font-size="7" font-family="sans-serif" text-anchor="middle">Visible Hits Ground</text>
  <!-- Radio reaches ground -->
  <line x1="100" y1="15" x2="100" y2="160" stroke="#38bdf8" stroke-width="3"/>
  <text x="100" y="150" fill="#38bdf8" font-size="7" font-family="sans-serif" text-anchor="middle">Radio Hits Ground</text>
</svg>
</div>
Why does high-energy X-ray and Gamma-ray radiation fail to penetrate down to mountain-top observatories on Earth?""",
     ["Atmospheric nitrogen and oxygen molecules high in the upper atmosphere absorb energetic X-rays and gamma rays via photoelectric and Compton scattering",
      "X-rays are repelled by Earth's gravity back into outer space",
      "X-rays turn into water vapor upon entering the solar system",
      "Only the Moon absorbs X-rays, not the Earth"],
     "A", "OSC", "easy",
     "The Earth's atmosphere presents an areal mass density of 10,000 kg/m^2; nitrogen and oxygen atoms absorb all incoming high-energy X-ray and gamma-ray photons above 40-50 km altitude, requiring satellite observatories."),

    # 74: Refraction and Prismatic Dispersion of White Light
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Triangular Glass Prism -->
  <polygon points="120,40 60,160 180,160" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="120" y="140" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Glass Prism</text>
  <!-- Incident White Light Beam -->
  <line x1="20" y1="110" x2="90" y2="100" stroke="#ffffff" stroke-width="4"/>
  <text x="45" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold">White Light</text>
  <!-- Dispersed Rays emerging -->
  <line x1="90" y1="100" x2="140" y2="105" stroke="#f43f5e" stroke-width="1.5"/>
  <line x1="90" y1="100" x2="140" y2="115" stroke="#8b5cf6" stroke-width="1.5"/>
  <!-- Fan out after exit -->
  <line x1="140" y1="105" x2="260" y2="70" stroke="#ef4444" stroke-width="2.5"/>
  <text x="270" y="75" fill="#ef4444" font-size="9" font-family="sans-serif" font-weight="bold">Red (700 nm): Least Bending</text>
  <line x1="140" y1="110" x2="260" y2="100" stroke="#eab308" stroke-width="2"/>
  <text x="270" y="105" fill="#facc15" font-size="9" font-family="sans-serif">Yellow (580 nm)</text>
  <line x1="140" y1="113" x2="260" y2="125" stroke="#22c55e" stroke-width="2"/>
  <text x="270" y="130" fill="#4ade80" font-size="9" font-family="sans-serif">Green (530 nm)</text>
  <line x1="140" y1="115" x2="260" y2="155" stroke="#8b5cf6" stroke-width="2.5"/>
  <text x="270" y="160" fill="#c084fc" font-size="9" font-family="sans-serif" font-weight="bold">Violet (400 nm): Maximum Bending</text>
</svg>
</div>
Why does violet light deviate (bend) more sharply than red light when passing through a dispersive glass prism?""",
     ["Violet light has a shorter wavelength and experiences a higher refractive index in glass, causing it to slow down more and bend at a steeper angle",
      "Violet light is heavier than red light",
      "Red light travels backwards inside glass",
      "Prism glass absorbs all red light completely"],
     "A", "OSC", "medium",
     "In optical dispersion, refractive index n increases as wavelength lambda decreases (Cauchy's equation); short-wavelength violet light (~400 nm) encounters a higher optical density in glass than red light (~700 nm), refracting through a larger angle."),

    # 75: Multi-Wavelength View of the Milky Way
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Optical View Strip -->
  <rect x="25" y="25" width="350" height="35" rx="4" fill="#18181b" stroke="#64748b" stroke-width="1"/>
  <text x="35" y="45" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold">Optical (Visible):</text>
  <text x="140" y="45" fill="#cbd5e1" font-size="8" font-family="sans-serif">Bright stars obscured by dark dust lanes</text>
  <!-- Infrared View Strip -->
  <rect x="25" y="68" width="350" height="35" rx="4" fill="#450a0a" stroke="#f43f5e" stroke-width="1"/>
  <text x="35" y="88" fill="#fca5a5" font-size="8" font-family="sans-serif" font-weight="bold">Infrared (JWST/Spitzer):</text>
  <text x="160" y="88" fill="#fecaca" font-size="8" font-family="sans-serif">Penetrates dust! Reveals warm protostars & galactic core</text>
  <!-- Radio View Strip -->
  <rect x="25" y="111" width="350" height="35" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1"/>
  <text x="35" y="131" fill="#7dd3fc" font-size="8" font-family="sans-serif" font-weight="bold">Radio (21 cm GMRT):</text>
  <text x="160" y="131" fill="#bae6fd" font-size="8" font-family="sans-serif">Maps cold neutral hydrogen gas across entire spiral arms</text>
  <!-- X-ray View Strip -->
  <rect x="25" y="154" width="350" height="35" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="1"/>
  <text x="35" y="174" fill="#e9d5ff" font-size="8" font-family="sans-serif" font-weight="bold">X-ray (Chandra):</text>
  <text x="140" y="174" fill="#f3e8ff" font-size="8" font-family="sans-serif">Shows Sagittarius A* black hole accretion & supernova remnants</text>
</svg>
</div>
What vital astronomical insight is gained by observing our galaxy across multiple electromagnetic bands rather than solely in visible light?""",
     ["Different EM wavelengths reveal distinct astrophysical components: infrared pierces dust to expose stars, radio maps hydrogen gas, and X-rays reveal black holes",
      "Visible light is fake while radio waves are real",
      "Multi-wavelength observation is done only to create colorful pictures for magazines",
      "All stars look exactly identical across all wavelengths"],
     "A", "OSC", "easy",
     "Astrophysical processes operate across the entire EM spectrum: cold atomic gas radiates radio, warm dust shines in infrared, stellar surfaces radiate visible light, and superheated accretion disks around black holes radiate X-rays."),

    # 76: Astronomical Seeing Blur vs Space Diffraction-Limited View
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Ground View Box -->
  <rect x="25" y="25" width="165" height="140" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
  <text x="107" y="48" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">GROUND TELESCOPE VIEW</text>
  <!-- Blurred Star Blob -->
  <circle cx="107" cy="95" r="24" fill="#facc15" opacity="0.3"/>
  <circle cx="107" cy="95" r="14" fill="#facc15" opacity="0.6"/>
  <circle cx="107" cy="95" r="6" fill="#ffffff"/>
  <text x="107" y="135" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Atmospheric 'Seeing' Jitter</text>
  <text x="107" y="150" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Air turbulence blurs point to ~1 arcsec</text>
  <!-- Space View Box -->
  <rect x="210" y="25" width="165" height="140" rx="6" fill="#090d16" stroke="#4ade80" stroke-width="2"/>
  <text x="292" y="48" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">SPACE TELESCOPE VIEW</text>
  <!-- Sharp Airy Disk -->
  <circle cx="292" cy="95" r="4" fill="#ffffff"/>
  <circle cx="292" cy="95" r="10" fill="none" stroke="#38bdf8" stroke-width="1" opacity="0.5"/>
  <text x="292" y="135" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Diffraction-Limited Airy Disk</text>
  <text x="292" y="150" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Zero atmospheric blur: 0.05 arcsec resolution!</text>
</svg>
</div>
Why does a space telescope produce dramatically sharper astronomical images than a ground-based telescope of identical mirror diameter?""",
     ["A space telescope operates outside the turbulent atmosphere, completely eliminating thermal air scintillation (seeing blur) that smears ground star images",
      "Space telescopes are made of pure diamond instead of glass",
      "Light moves three times faster in space than on Earth",
      "Stars are afraid of ground telescopes"],
     "A", "OSC", "easy",
     "Thermal convection in Earth's atmosphere continuously modulates refractive indices, blurring stellar points into jittering seeing disks (~1 arcsecond wide); space telescopes operate in a vacuum, achieving true theoretical diffraction limits (e.g. 0.05 arcsec for Hubble)."),

    # 77: Wien's Displacement Law Stellar Temperature Spectrum
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#090d16"/>
  <!-- Axis -->
  <line x1="40" y1="160" x2="360" y2="160" stroke="#64748b" stroke-width="2"/>
  <line x1="40" y1="160" x2="40" y2="20" stroke="#64748b" stroke-width="2"/>
  <text x="340" y="175" fill="#94a3b8" font-size="8" font-family="sans-serif">Wavelength (lambda)</text>
  <text x="30" y="15" fill="#94a3b8" font-size="8" font-family="sans-serif">Intensity</text>
  <!-- Hot Star Curve (Blue - 10,000 K) -->
  <path d="M 40 160 Q 80 30 140 120 T 360 160" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
  <text x="90" y="45" fill="#38bdf8" font-size="8" font-family="sans-serif" font-weight="bold">Hot Star (10,000 K): Peaks in UV/Blue</text>
  <!-- Medium Star Curve (Sun - 6,000 K - Yellow) -->
  <path d="M 40 160 Q 140 70 200 130 T 360 160" stroke="#facc15" stroke-width="2.5" fill="none"/>
  <text x="150" y="80" fill="#facc15" font-size="8" font-family="sans-serif" font-weight="bold">Sun (5,800 K): Peaks in Visible (500 nm)</text>
  <!-- Cool Star Curve (Red Dwarf - 3,000 K) -->
  <path d="M 40 160 Q 220 110 270 145 T 360 160" stroke="#ef4444" stroke-width="2.5" fill="none"/>
  <text x="250" y="115" fill="#f87171" font-size="8" font-family="sans-serif" font-weight="bold">Cool Star (3,000 K): Peaks in Infrared</text>
</svg>
</div>
According to the blackbody radiation curves shown above, what happens to the peak emission wavelength (lambda_max) as a star's surface temperature increases?""",
     ["The peak emission wavelength shifts toward shorter wavelengths (higher frequencies and higher photon energies)",
      "The peak emission wavelength shifts toward longer radio wavelengths",
      "The star stops radiating energy completely",
      "The wavelength remains constant at exactly 1 meter"],
     "A", "OSC", "medium",
     "Wien's displacement law (lambda_max = b / T) establishes that peak emission wavelength is inversely proportional to surface temperature: scorching 10,000 K stars peak in blue/UV, the 5,800 K Sun peaks in green-yellow visible, and cool 3,000 K red stars peak in the infrared."),

    # 78: 21 cm Hydrogen Line Spin-Flip Transition
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Parallel Spins (Higher Energy) -->
  <rect x="25" y="25" width="160" height="140" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="75" cy="70" r="16" fill="#38bdf8"/>
  <text x="75" y="74" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Proton</text>
  <line x1="75" y1="50" x2="75" y2="35" stroke="#facc15" stroke-width="2"/>
  <circle cx="135" cy="70" r="10" fill="#f43f5e"/>
  <text x="135" y="74" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Electron</text>
  <line x1="135" y1="55" x2="135" y2="40" stroke="#facc15" stroke-width="2"/>
  <text x="105" y="115" fill="#fca5a5" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Parallel Spins (Parallel)</text>
  <text x="105" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Higher Energy State</text>
  <!-- Flip Transition Arrow -->
  <line x1="190" y1="95" x2="225" y2="95" stroke="#facc15" stroke-width="3"/>
  <!-- Anti-Parallel Spins (Lower Energy) -->
  <rect x="230" y="25" width="150" height="140" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <circle cx="275" cy="70" r="16" fill="#38bdf8"/>
  <text x="275" y="74" fill="#000000" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Proton</text>
  <line x1="275" y1="50" x2="275" y2="35" stroke="#facc15" stroke-width="2"/>
  <circle cx="335" cy="70" r="10" fill="#f43f5e"/>
  <text x="335" y="74" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Electron</text>
  <line x1="335" y1="85" x2="335" y2="100" stroke="#facc15" stroke-width="2"/>
  <text x="305" y="115" fill="#86efac" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Opposite Spins (Anti-parallel)</text>
  <text x="305" y="130" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Lower Energy Ground State</text>
  <!-- Emitted Photon -->
  <text x="200" y="180" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">EMITS: 21 cm Radio Photon (nu = 1420.4 MHz)</text>
</svg>
</div>
What fundamental atomic event produces the 21 cm cosmic radio wave line used by radio astronomers to map the Milky Way galaxy?""",
     ["A hyperfine spin-flip transition wherein the electron's spin flips from parallel to anti-parallel relative to the proton's nuclear spin in a neutral hydrogen atom",
      "A hydrogen atom colliding with an iron meteor",
      "Nuclear fusion of two hydrogen atoms into helium",
      "An electron escaping completely from the atom into space"],
     "A", "OSC", "hard",
     "In ground-state neutral hydrogen (HI), parallel electron-proton magnetic dipole moments represent a slightly higher hyperfine energy level; when the electron spontaneously flips to anti-parallel alignment, a tiny energy quantum (5.87 micro-eV) is emitted as a 21.1 cm (1420.4 MHz) radio photon."),

    # 79: Radio Waves vs Visible Light Penetration of Dust
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Interstellar Dust Cloud -->
  <rect x="130" y="30" width="140" height="130" rx="10" fill="#292524" stroke="#78716c" stroke-width="2"/>
  <text x="200" y="90" fill="#d6d3d1" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Interstellar Dust Cloud</text>
  <text x="200" y="105" fill="#a8a29e" font-size="8" font-family="sans-serif" text-anchor="middle">(Grain size approx 0.1-1 micron)</text>
  <!-- Visible light beam blocked -->
  <line x1="20" y1="60" x2="130" y2="60" stroke="#4ade80" stroke-width="3"/>
  <circle cx="130" cy="60" r="4" fill="#ef4444"/>
  <text x="75" y="50" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Visible Light (0.5 micron)</text>
  <text x="145" y="50" fill="#ef4444" font-size="7" font-family="sans-serif">SCATTERED & BLOCKED!</text>
  <!-- Radio wave passing through -->
  <line x1="20" y1="130" x2="380" y2="130" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6"/>
  <text x="75" y="120" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Radio Wave (21 cm)</text>
  <text x="320" y="120" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Passes Unimpeded!</text>
  <text x="200" y="178" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Physics: lambda_radio >> dust grain diameter -> Zero Rayleigh scattering!</text>
</svg>
</div>
Why can long radio waves pass through dense interstellar dust clouds that completely block visible light?""",
     ["Radio wavelengths (centimeters) are hundreds of thousands of times larger than dust grains (~0.1 micron), causing negligible scattering",
      "Radio waves evaporate the dust grains upon contact",
      "Dust grains are transparent to visible light but opaque to radio",
      "Radio waves travel along optical fibers in space"],
     "A", "OSC", "easy",
     "Rayleigh scattering occurs when particles are comparable in size to the probing wavelength; because microscopic interstellar dust grains (~0.1-0.5 micron) match visible light wavelengths, they scatter visible light strongly, but are far too small to scatter long radio waves."),

    # 80: Gravitational Redshift near Dense Objects
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Dense White Dwarf / Neutron Star -->
  <circle cx="80" cy="95" r="35" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="80" y="92" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Super-Dense</text>
  <text x="80" y="104" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">Massive Star</text>
  <!-- Emitted Blue Photon Climbing out -->
  <path d="M 120 95 Q 160 70 200 95 T 280 95 T 360 95" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <!-- Transition to Red -->
  <path d="M 240 95 Q 290 60 340 95" stroke="#ef4444" stroke-width="3" fill="none"/>
  <text x="160" y="70" fill="#38bdf8" font-size="8" font-family="sans-serif">Initial High Frequency (Blue)</text>
  <text x="310" y="60" fill="#ef4444" font-size="8" font-family="sans-serif" font-weight="bold">Redshifted (Lower Energy)</text>
  <!-- Explanatory Box -->
  <rect x="60" y="145" width="280" height="35" rx="5" fill="#090d16" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="166" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Gravitational Potential Energy Loss: h*nu_obs < h*nu_emit</text>
</svg>
</div>
What happens to electromagnetic radiation as it climbs upward out of an intense gravitational field (such as near a neutron star or white dwarf)?""",
     ["Gravitational Redshift: photons lose energy climbing out of the gravitational well, causing their frequency to decrease and wavelength to stretch",
      "The photons accelerate to triple the speed of light",
      "The photons turn into heavy lead atoms",
      "The light turns into pure mechanical sound"],
     "A", "OSC", "hard",
     "According to Einstein's General Relativity, photons must expend energy to climb out of a deep gravitational potential well; because photon velocity c is constant, energy loss is manifested as a reduction in frequency (E = h*nu), causing gravitational redshift."),

    # 81: Atmospheric Windows for Space Missions
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Title -->
  <text x="200" y="25" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Observatory Deployment Strategy by EM Band</text>
  <!-- Ground Observatories -->
  <rect x="25" y="40" width="165" height="135" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="107" y="60" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">GROUND-BASED</text>
  <text x="107" y="78" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1. Optical Telescopes (400-800 nm)</text>
  <text x="107" y="93" fill="#cbd5e1" font-size="8" font-family="sans-serif">   Located on high mountains</text>
  <text x="107" y="112" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2. Radio Arrays (cm to meters)</text>
  <text x="107" y="127" fill="#cbd5e1" font-size="8" font-family="sans-serif">   GMRT at Narayangaon, Pune</text>
  <text x="107" y="155" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Atmosphere is 100% Transparent!</text>
  <!-- Space Observatories -->
  <rect x="210" y="40" width="165" height="135" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="292" y="60" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">SPACE-BASED ONLY</text>
  <text x="292" y="78" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">1. Gamma-ray: Fermi & Swift</text>
  <text x="292" y="95" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">2. X-ray: Chandra & Astrosat</text>
  <text x="292" y="112" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">3. Far-UV: Hubble & Astrosat</text>
  <text x="292" y="129" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">4. Mid-Infrared: JWST</text>
  <text x="292" y="155" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Atmosphere is Opaque!</text>
</svg>
</div>
Which fundamental physical criterion determines whether an astronomical observatory can be built on the ground or MUST be launched into space?""",
     ["The atmospheric absorption opacity of Earth's atmosphere for that specific electromagnetic wavelength band",
      "The total construction cost of the telescope mirror",
      "Whether the stars being observed are located north or south of the equator",
      "The weight of the astronomers operating the controls"],
     "A", "OSC", "easy",
     "Atmospheric opacity dictates observatory deployment: bands where the atmosphere is transparent (visible light and radio waves) allow economical ground-based mega-telescopes, whereas opaque bands (gamma, X-ray, far-UV, far-IR) require orbital space platforms."),

    # 82: Cosmic Distance and Light Travel Time
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Distant Star (Left) -->
  <circle cx="60" cy="95" r="25" fill="#facc15" stroke="#eab308" stroke-width="2"/>
  <text x="60" y="92" fill="#000000" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Distant Star</text>
  <text x="60" y="104" fill="#000000" font-size="7" font-family="sans-serif" text-anchor="middle">(100 Light-Yrs Away)</text>
  <!-- Light Beam Traveling Through Space -->
  <line x1="90" y1="95" x2="295" y2="95" stroke="#38bdf8" stroke-width="3" stroke-dasharray="8"/>
  <text x="195" y="80" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Light travels at c = 300,000 km/s</text>
  <text x="195" y="115" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Travel Time = 100 Years</text>
  <!-- Earth Observer (Right) -->
  <circle cx="330" cy="95" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="330" y="92" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Earth</text>
  <text x="330" y="104" fill="#bbf7d0" font-size="7" font-family="sans-serif" text-anchor="middle">Year 2026</text>
  <!-- Core Takeaway -->
  <rect x="40" y="140" width="320" height="35" rx="5" fill="#090d16" stroke="#4ade80" stroke-width="1"/>
  <text x="200" y="162" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">"Looking out into space is literally looking back in time!"</text>
</svg>
</div>
When an astronomer on Earth looks at a star situated 100 light-years away, what state of the star are they actually observing?""",
     ["The physical state and appearance of the star as it existed exactly 100 years ago in the past",
      "The physical state of the star as it will exist 100 years into the future",
      "The instantaneous current state of the star in real time today",
      "An imaginary mirage that does not exist"],
     "A", "OSC", "easy",
     "Because light travels at a finite velocity (c approx 300,000 km/s), the photons reaching our telescopes today departed the star 100 years ago; observing distant cosmic objects is equivalent to looking directly into deep historical time.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch18_topic1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
