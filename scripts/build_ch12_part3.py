"""
build_ch12_part3.py: Generates enhanced Q77 to Q114 for Chapter 12 (Study of Sound).
"""

import json

def get_part3_enhancements():
    # Return dictionary keyed by question index (76 to 113)
    enhancements = {}

    # Q77: MH-9-SCIT-12-12.1-OSC-077
    enhancements[76] = {
        "text": "Human beings are able to hear sound primarily because incoming acoustic pressure waves cause the mechanical vibration of the:",
        "options": [
            "Pinna",
            "Cochlea",
            "Tympanic membrane (Eardrum)",
            "Auditory canal"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The human ear captures sound waves from the atmosphere and converts acoustic pressure fluctuations into mechanical movements, which are subsequently transduced into neural signals.

### 2. Wave Dynamics & Mathematical Derivation:
Sound enters the external ear and travels down the auditory canal, reaching a delicate, tightly stretched circular membrane called the **tympanic membrane (eardrum)**.
- When an acoustic **compression** (high pressure) strikes the eardrum, the net inward force pushes the membrane inward:
\[
F = \Delta P \times A_{\text{eardrum}}
\]
- When a **rarefaction** (low pressure) arrives, the membrane moves outward.
This sets the eardrum into forced mechanical vibration at the exact frequency of the incoming sound wave. These vibrations are then amplified by the three middle ear ossicles (malleus, incus, stapes) and transferred to the cochlea.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** The pinna collects and channels sound waves into the ear canal, but does not execute the primary sensory vibration.
- **B (Incorrect):** The cochlea is the fluid-filled inner ear organ that converts fluid waves into electrical nerve impulses.
- **C (Correct):** The tympanic membrane (eardrum) directly vibrates in response to sound pressure waves, initiating hearing.
- **D (Incorrect):** The auditory canal is an acoustic channel, not a vibrating membrane."""
    }

    # Q78: MH-9-SCIT-12-12.1-OSC-078
    enhancements[77] = {
        "text": "Pulling and releasing a stretched string on a musical instrument produces sound because:",
        "options": [
            "Its internal mechanical tension increases indefinitely",
            "Its state of rest remains completely unaltered",
            "It is set into rapid mechanical vibration",
            "Applied external force generates thermal radiation"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Every sound in the universe originates from the rapid mechanical vibration of a material body.

### 2. Wave Dynamics & Mathematical Derivation:
When a taut string is pulled laterally and released, elastic restoring tension forces accelerate the displaced string segments toward their equilibrium line. Due to inertia, the segments overshoot equilibrium, initiating periodic transverse oscillation:
\[
y(x,t) = A \sin(kx) \cos(\omega t)
\]
As the string vibrates rapidly back and forth, its physical surface repeatedly collides with adjacent air molecules, creating alternating high-pressure compressions and low-pressure rarefactions that propagate outward as audible longitudinal sound waves. Without vibration, no acoustic pressure waves can be formed.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Tension provides the elastic restoring force; it does not increase indefinitely.
- **B (Incorrect):** The string's state of rest is actively disturbed into oscillatory motion.
- **C (Correct):** Sound generation strictly requires setting the physical medium/string into rapid mechanical vibration.
- **D (Incorrect):** Plucking creates elastic acoustic waves, not thermal radiation."""
    }

    # Q79: MH-9-SCIT-12-12.1-OSC-079
    enhancements[78] = {
        "text": "What is the standard SI unit of wavelength (\\(\\lambda\\))?",
        "options": [
            "Hertz (Hz)",
            "Second (s)",
            "Metre (m)",
            "Decibel (dB)"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Wavelength is a fundamental spatial property of any periodic traveling wave, representing the spatial repeat length of the wave profile.

### 2. Wave Dynamics & Mathematical Derivation:
Wavelength (\(\lambda\)) is defined as the linear physical distance between two consecutive points oscillating in the same phase (such as two consecutive crests, two consecutive troughs, or two consecutive compressions).
Because wavelength measures linear spatial separation or length:
\[
[\lambda] = [L]
\]
In the International System of Units (SI), length is measured in **metres (m)**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Hertz (\(\text{Hz} = \text{s}^{-1}\)) is the SI unit of frequency.
- **B (Incorrect):** Second (\(\text{s}\)) is the SI unit of time period.
- **C (Correct):** Metre (\(\text{m}\)) is the SI unit of wavelength.
- **D (Incorrect):** Decibel (\(\text{dB}\)) is the logarithmic unit of sound intensity level."""
    }

    # Q80: MH-9-SCIT-12-12.1-OSC-080
    enhancements[79] = {
        "text": "Identify the odd one out among the following electro-acoustic devices based on energy conversion:",
        "options": [
            "Microphone",
            "Electric bell",
            "Loudspeaker",
            "Radio speaker"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Acoustic transducers are classified according to whether they convert electrical energy into acoustic sound energy (acoustic emitters/actuators) or acoustic sound energy into electrical signals (acoustic sensors/microphones).

### 2. Wave Dynamics & Mathematical Derivation:
Analyzing the energy transformation in each device:
- **Microphone:** Receives mechanical sound pressure waves on a diaphragm and converts **sound energy into electrical signals**:
\[
\text{Sound Energy} \longrightarrow \text{Electrical Energy}
\]
- **Electric bell:** Uses an electromagnet to move a hammer striking a gong, converting **electrical energy into mechanical sound energy**:
\[
\text{Electrical Energy} \longrightarrow \text{Sound Energy}
\]
- **Loudspeaker & Radio speaker:** Use an electromagnetic voice coil in a permanent magnet field to vibrate a cone, converting **electrical signals into acoustic sound energy**:
\[
\text{Electrical Energy} \longrightarrow \text{Sound Energy}
\]
Hence, the microphone is the unique odd one out because it performs the exact inverse energy conversion.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct / Odd one out):** A microphone converts sound energy into electrical energy, whereas all three other devices convert electrical energy into sound.
- **B, C, D (Incorrect to select):** All three are sound-producing transducers converting electrical input into acoustic output."""
    }

    # Q81: MH-9-SCIT-12-12.1-OSC-081
    enhancements[80] = {
        "text": "Bats navigate through obstacles in pitch darkness by emitting which type of acoustic waves?",
        "options": [
            "Ultrasonic sound waves",
            "Infrasonic sound waves",
            "Ultraviolet electromagnetic waves",
            "Infrared thermal radiation"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Bats utilize acoustic echolocation to perceive spatial geometry and locate airborne prey in the absence of visual cues.

### 2. Wave Dynamics & Mathematical Derivation:
Bats emit high-frequency acoustic squeaks belonging to the **ultrasonic frequency range** (\(\nu > 20\text{ kHz}\), extending up to \(120\text{ kHz}\)).
Ultrasonic frequencies are critical for echolocation because of wave optics principles:
\[
\lambda = \frac{v}{\nu} = \frac{344\text{ m/s}}{50{,}000\text{ Hz}} \approx 6.9\text{ mm}
\]
Wavelengths on the order of millimeters allow the acoustic beam to reflect sharply off small insects (such as moths and mosquitoes) without broad diffraction bending, giving the bat high angular and range resolution.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Bats emit ultrasonic sound waves (\(\nu > 20\text{ kHz}\)) for echolocation.
- **B (Incorrect):** Infrasonic waves (\(< 20\text{ Hz}\)) have wavelengths of many metres, which diffract around small prey without reflecting.
- **C, D (Incorrect):** Bats emit mechanical acoustic vibrations, not electromagnetic ultraviolet or infrared radiation."""
    }

    # Q82: MH-9-SCIT-12-12.1-OSC-082 (Fixed defect: all 4 options were "None of the above")
    enhancements[81] = {
        "text": "Colossal nuclear thermonuclear explosions occur continuously on the Sun. Why is absolutely no sound from these solar explosions heard on Earth?",
        "options": [
            "The sound frequency produced by the Sun is too low for the human ear to detect",
            "Solar radiation pressure reflects all acoustic waves away from Earth's orbital path",
            "Earth's ionosphere reflects all interplanetary sound waves back into space",
            "Interplanetary space is a vacuum and sound mechanical waves cannot propagate without a material medium"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Thermonuclear fusion reactions in the solar core and flare eruptions on the solar surface release colossal amounts of energy, generating immense shockwaves within the Sun's dense plasma.

### 2. Wave Dynamics & Mathematical Derivation:
Sound is a mechanical wave that requires a continuous material medium containing mass density and elastic restoring forces to propagate:
\[
v_{\text{sound}} = \sqrt{\frac{B}{\rho}}
\]
Between the Sun and Earth lies approximately \(1.5 \times 10^8\text{ km}\) of interplanetary outer space, which is an almost perfect vacuum (with particle density negligible for macroscopic acoustic pressure coupling):
\[
\rho_{\text{space}} \approx 0 \implies v_{\text{sound, space}} = 0\text{ m/s}
\]
While electromagnetic radiation (light, heat, radio waves) traverses this vacuum effortlessly at \(c \approx 3 \times 10^8\text{ m/s}\), mechanical sound waves cannot propagate across empty space.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Explosions generate a wide spectrum of frequencies, but none can cross the vacuum regardless of frequency.
- **B, C (Incorrect):** Neither solar radiation pressure nor the ionosphere is the reason; sound cannot even reach the outer magnetosphere.
- **D (Correct):** Interplanetary space is a vacuum, and mechanical sound waves cannot travel without a material medium."""
    }

    # Q83: MH-9-SCIT-12-12.1-OSC-083
    enhancements[82] = {
        "text": "What is the approximate wavelength of the sound wave produced in air by a tuning fork vibrating at a frequency of 330 Hz? (Take speed of sound in air = 330 m/s)",
        "options": [
            "100 cm (1.0 m)",
            "10 cm (0.1 m)",
            "1 cm (0.01 m)",
            "330 cm (3.3 m)"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The fundamental wave relation links wave velocity, frequency, and wavelength across all mechanical and electromagnetic wave systems.

### 2. Wave Dynamics & Mathematical Derivation:
The wave equation states:
\[
v = \nu \lambda \implies \lambda = \frac{v}{\nu}
\]
Given:
- Speed of sound in air, \(v = 330\text{ m/s}\)
- Frequency of tuning fork, \(\nu = 330\text{ Hz}\)

Substitute these values:
\[
\lambda = \frac{330\text{ m/s}}{330\text{ s}^{-1}} = 1.0\text{ m}
\]
Convert metres to centimetres:
\[
1.0\text{ m} = 100\text{ cm}
\]
The wavelength of this sound wave is exactly \(100\text{ cm}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** \(\lambda = \frac{330}{330} = 1\text{ m} = 100\text{ cm}\).
- **B (Incorrect):** \(10\text{ cm}\) corresponds to a tenfold frequency of \(3300\text{ Hz}\).
- **C (Incorrect):** \(1\text{ cm}\) corresponds to an ultrasonic frequency of \(33{,}000\text{ Hz}\).
- **D (Incorrect):** \(330\text{ cm}\) corresponds to a frequency of \(100\text{ Hz}\)."""
    }

    # Q84: MH-9-SCIT-12-12.1-OSC-084
    enhancements[83] = {
        "text": "The perceived loudness of an acoustic sound wave depends fundamentally upon which physical wave parameter?",
        "options": [
            "Amplitude",
            "Frequency",
            "Wave velocity",
            "Wavelength"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Loudness is the sensory perception of sound volume, correlating directly with the mechanical energy transported by the acoustic pressure wave per unit time.

### 2. Wave Dynamics & Mathematical Derivation:
The intensity \(I\) (energy per unit area per second) of a sound wave is directly proportional to the square of its displacement amplitude \(A\):
\[
I \propto A^2
\]
When an object vibrates with greater amplitude, it imparts greater kinetic energy to adjacent air molecules, producing larger pressure amplitudes:
\[
\Delta P_{\text{max}} = \rho v \omega A
\]
Greater pressure deflections on the tympanic membrane cause larger hair-cell displacements in the inner ear, signaling greater loudness to the brain according to the Weber-Fechner logarithmic law (\(L \propto \log I\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Loudness depends directly on the amplitude of vibration (\(I \propto A^2\)).
- **B (Incorrect):** Frequency determines *pitch* (shrillness or bass), not loudness.
- **C (Incorrect):** Velocity is determined by the medium and does not govern loudness.
- **D (Incorrect):** Wavelength is linked to pitch and velocity (\(\lambda = v/\nu\))."""
    }

    # Q85: MH-9-SCIT-12-12.1-OSC-085 (Fixed defect)
    enhancements[84] = {
        "text": "In which of the following states of matter does sound propagate with the HIGHEST velocity?",
        "options": [
            "Gases",
            "Liquids",
            "Solids",
            "Vacuum"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The speed of sound in any material medium is governed by the ratio of its elastic modulus to its inertial density.

### 2. Wave Dynamics & Mathematical Derivation:
The velocity of sound is expressed by:
\[
v = \sqrt{\frac{E}{\rho}}
\]
- In **solids**, atoms are locked in crystalline or closely packed lattice structures with strong chemical bonds, providing enormous elasticity (Young's modulus \(Y \sim 10^{10} - 10^{11}\text{ N/m}^2\)).
- In **liquids**, molecules are loosely bound with lower bulk moduli (\(B \sim 10^9\text{ N/m}^2\)).
- In **gases**, intermolecular forces are negligible (\(\gamma P \sim 10^5\text{ N/m}^2\)).
Consequently, sound velocities follow the universal order:
\[
v_{\text{solids}} (5000-6500\text{ m/s}) > v_{\text{liquids}} (1400-1500\text{ m/s}) > v_{\text{gases}} (330-350\text{ m/s})
\]
Sound propagates fastest in **solids**. In a vacuum, sound cannot propagate at all (\(v = 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Gases have the lowest sound velocity due to weak intermolecular restoring forces.
- **B (Incorrect):** Liquids transmit sound faster than gases, but slower than solids.
- **C (Correct):** Solids exhibit the highest velocity of sound due to high elastic moduli.
- **D (Incorrect):** Vacuum has zero sound velocity."""
    }

    # Q86: MH-9-SCIT-12-12.1-OSC-086 (Fixed defect)
    enhancements[85] = {
        "text": "In which wave form do acoustic sound waves travel through atmospheric air?",
        "options": [
            "Longitudinal waves (compressions and rarefactions)",
            "Transverse waves (crests and troughs)",
            "Electromagnetic waves",
            "Surface capillary waves"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The physical state of a medium dictates the type of mechanical wave motion it can sustain.

### 2. Wave Dynamics & Mathematical Derivation:
A gas like air possesses compressibility (bulk modulus \(B\)) but completely lacks shear rigidity (\(\eta = 0\)).
- Because air particles cannot exert perpendicular restoring forces, transverse waves cannot propagate through the bulk of a gas.
- Air particles can, however, exert longitudinal restoring forces when compressed.
As a source oscillates, it produces alternating high-density/high-pressure regions (**compressions**) and low-density/low-pressure regions (**rarefactions**), wherein particle displacement is parallel to the wave direction:
\[
\vec{v}_{\text{particle}} \parallel \vec{v}_{\text{wave}}
\]
Hence, sound waves in air travel strictly as **longitudinal waves**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sound in air propagates as longitudinal waves consisting of compressions and rarefactions.
- **B (Incorrect):** Transverse waves require shear rigidity, which air lacks.
- **C (Incorrect):** Electromagnetic waves are non-mechanical field vibrations.
- **D (Incorrect):** Surface capillary waves occur at liquid-gas interfaces due to surface tension."""
    }

    # Q87: MH-9-SCIT-12-12.1-OSC-087 (Fixed defect & ans alignment)
    enhancements[86] = {
        "text": "An echo sounder installed on a ship emits an ultrasonic pulse and receives the reflected echo from the seabed after 0.40 seconds. What is the depth of the sea? (Take speed of sound in seawater = 1500 m/s)",
        "options": [
            "150 m",
            "600 m",
            "300 m",
            "750 m"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Echo sounding applies the principle of sound reflection to determine distances to remote or inaccessible reflective boundaries.

### 2. Wave Dynamics & Mathematical Derivation:
The emitted ultrasonic pulse travels downward to the seabed, reflects, and travels upward back to the ship's receiver.
The total distance traversed during the round-trip time \(t\) is twice the water depth (\(2d\)):
\[
2d = v \times t \implies d = \frac{v \times t}{2}
\]
Given:
- Speed of sound in seawater, \(v = 1500\text{ m/s}\)
- Total round-trip time, \(t = 0.40\text{ s}\)

Substitute the values:
\[
2d = 1500 \times 0.40 = 600\text{ m}
\]
\[
d = \frac{600}{2} = 300\text{ m}
\]
The depth of the seabed is exactly \(300\text{ m}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(150\text{ m}\) results from an erroneous division by 4.
- **B (Incorrect):** \(600\text{ m}\) is the total two-way round-trip path length (\(2d\)); forgetting to divide by 2 is a frequent error.
- **C (Correct):** \(d = \frac{1500 \times 0.40}{2} = 300\text{ m}\).
- **D (Incorrect):** \(750\text{ m}\) is \(v/2\) without multiplying by the time interval."""
    }

    # Q88: MH-9-SCIT-12-12.1-OSC-088
    enhancements[87] = {
        "text": "Which of the following natural wave phenomena consists of a physical mixture of both transverse and longitudinal wave modes?",
        "options": [
            "Electromagnetic radiation",
            "Seismic earthquake waves",
            "Sound waves in atmospheric air",
            "Monochromatic laser beams"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Earthquakes release immense stored strain energy through sudden fault slippage within the solid lithosphere, generating diverse seismic wave modes.

### 2. Wave Dynamics & Mathematical Derivation:
Solid planetary rock possesses both bulk elasticity (resisting compression) and shear elasticity (resisting shear stress). Consequently, an earthquake rupture simultaneously generates:
1. **Primary (P) waves:** Longitudinal body waves where rock particles compress and dilate parallel to wave propagation (\(v_P = \sqrt{\frac{K + \frac{4}{3}\mu}{\rho}}\)).
2. **Secondary (S) waves:** Transverse body waves where rock particles shear perpendicularly to wave propagation (\(v_S = \sqrt{\frac{\mu}{\rho}}\)).
3. **Surface waves:** Rayleigh and Love waves propagating along Earth's surface that combine elliptical longitudinal rolling with transverse horizontal shearing.
Therefore, seismic waves are a classic composite mixture of both longitudinal and transverse waves.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, D (Incorrect):** Electromagnetic waves and laser light are strictly transverse electromagnetic oscillations.
- **B (Correct):** Seismic waves comprise longitudinal P-waves, transverse S-waves, and mixed Rayleigh surface waves.
- **C (Incorrect):** Sound waves in atmospheric air are purely longitudinal."""
    }

    # Q89: MH-9-SCIT-12-12.1-OSC-089
    enhancements[88] = {
        "text": "What is the typical frequency range of the acoustic signals emitted by bats during echolocation to navigate and avoid obstacles?",
        "options": [
            "Below 20 Hz (Infrasonic)",
            "Between 20 Hz and 2,000 Hz",
            "Between 2,000 Hz and 10,000 Hz",
            "Above 20,000 Hz (Ultrasonic)"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Bats utilize high-frequency echolocation calls that are specialized for detecting small targets and fine spatial textures in total darkness.

### 2. Wave Dynamics & Mathematical Derivation:
Human hearing terminates at an upper frequency threshold of \(20{,}000\text{ Hz}\) (\(20\text{ kHz}\)).
Bats emit acoustic vocalizations ranging from \(20\text{ kHz}\) up to \(120\text{ kHz}\) (and in some specialized species, over \(150\text{ kHz}\)):
\[
\nu_{\text{bat}} > 20{,}000\text{ Hz}
\]
These frequencies lie deep in the **ultrasonic frequency band**. The short wavelengths associated with ultrasonic frequencies (\(\lambda < 1.7\text{ cm}\)) prevent sound waves from bending around small insects via diffraction, producing sharp acoustic echoes that pinpoint prey coordinates.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Frequencies below \(20\text{ Hz}\) are infrasonic, characterized by wavelengths exceeding \(17\text{ m}\).
- **B, C (Incorrect):** These represent audible frequencies that humans can easily hear; bats do not use low audible frequencies for precision echolocation.
- **D (Correct):** Bats emit ultrasonic sounds with frequencies exceeding \(20{,}000\text{ Hz}\)."""
    }

    # Q90: MH-9-SCIT-12-12.1-OSC-090 (Fixed defect)
    enhancements[89] = {
        "text": "What is the velocity of sound in dry atmospheric air at a temperature of 0 °C?",
        "options": [
            "331 - 332 m/s",
            "346 m/s",
            "1498 m/s",
            "5000 m/s"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The speed of sound in a gas is directly related to its thermodynamic temperature according to Laplace's equation of state for adiabatic acoustic disturbances.

### 2. Wave Dynamics & Mathematical Derivation:
The speed of sound in an ideal diatomic gas is:
\[
v = \sqrt{\frac{\gamma R T}{M}}
\]
At \(0^\circ\text{C}\) (\(T = 273.15\text{ K}\)):
\[
v_0 = \sqrt{\frac{1.4 \times 8.314 \times 273.15}{0.0288}} \approx 332\text{ m/s}
\]
As temperature increases, speed rises approximately as:
\[
v_t \approx v_0 + 0.61 \times t
\]
At \(25^\circ\text{C}\), \(v_{25} \approx 332 + 0.61(25) \approx 347\text{ m/s}\) (standard textbook value \(346\text{ m/s}\)).
Therefore, at \(0^\circ\text{C}\), the speed of sound is **\(331 - 332\text{ m/s}\)**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** The speed of sound in dry air at \(0^\circ\text{C}\) is approximately \(331 - 332\text{ m/s}\).
- **B (Incorrect):** \(346\text{ m/s}\) is the speed of sound at room temperature (\(25^\circ\text{C}\)).
- **C (Incorrect):** \(1498\text{ m/s}\) is the speed of sound in distilled water.
- **D (Incorrect):** \(5000\text{ m/s}\) is the speed of sound in solid steel or glass."""
    }

    # Q91: MH-9-SCIT-12-12.1-OSC-091
    enhancements[90] = {
        "text": "Television signals broadcast from an artificial satellite in space can be received across continents on Earth, whereas terrestrial TV broadcasts from a city tower cannot be received directly beyond approximately 100 km. Why?",
        "options": [
            "Earth has an atmosphere that absorbs all high-energy satellite signals",
            "Satellite signals bend around the Earth's curvature via atmospheric refraction",
            "Gravity pulls terrestrial TV signals down into the ocean",
            "High-frequency TV signals travel in straight line-of-sight paths and cannot follow Earth's curvature or reflect off the ionosphere"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Television transmissions utilize very high frequency (VHF: \(30 - 300\text{ MHz}\)) and ultra-high frequency (UHF: \(300 - 3000\text{ MHz}\)) electromagnetic carrier waves.

### 2. Wave Dynamics & Mathematical Derivation:
Unlike medium-wave (AM) radio signals, VHF and UHF television waves have frequencies too high to be reflected by the ionospheric Kennelly-Heaviside layers; they penetrate directly into space.
- Terrestrial broadcasts propagate via **line-of-sight (space wave propagation)**.
- Due to Earth's spherical curvature, the horizon distance \(d\) from a transmitter tower of height \(h\) is:
\[
d \approx \sqrt{2 R_E h}
\]
Beyond approximately \(80 - 100\text{ km}\), the line of sight is obstructed by Earth's curvature.
- In contrast, a satellite located high above Earth has a direct, unobstructed line of sight to entire continents.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Earth's atmosphere is transparent to satellite TV microwave frequencies.
- **B (Incorrect):** Satellite signals travel in direct straight lines, not curved refraction paths.
- **C (Incorrect):** Gravitational deflection of radio waves over \(100\text{ km}\) is completely negligible.
- **D (Correct):** Terrestrial VHF/UHF TV signals propagate strictly via line-of-sight and cannot bend around Earth's curvature."""
    }

    # Q92: MH-9-SCIT-12-12.1-OSC-092
    enhancements[91] = {
        "text": "Among the materials listed below, in which medium does sound travel with the LARGEST speed?",
        "options": [
            "Solid steel",
            "Water",
            "Solid wood",
            "Air"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The speed of sound in a solid medium depends on Young's modulus of elasticity (\(Y\)) and density (\(\rho\)): \(v = \sqrt{Y/\rho}\).

### 2. Wave Dynamics & Mathematical Derivation:
Comparing sound velocities in the given materials:
- **Air (gas):** \(v \approx 344\text{ m/s}\)
- **Water (liquid):** \(v \approx 1498\text{ m/s}\)
- **Wood (solid composite):** \(v \approx 3300 - 4000\text{ m/s}\) (along the grain)
- **Steel (solid metal alloy):** \(v \approx 5960\text{ m/s}\)

Steel has an exceptionally high Young's modulus of elasticity (\(Y \approx 200\text{ GPa}\)). Although its density is high (\(\rho \approx 7850\text{ kg/m}^3\)), the elastic modulus is proportionally much greater, yielding the highest velocity of sound (\(\approx 5960\text{ m/s}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Steel conducts sound at approximately \(5960\text{ m/s}\), the highest among all listed options.
- **B (Incorrect):** Water conducts sound at \(\approx 1498\text{ m/s}\).
- **C (Incorrect):** Wood conducts sound at \(\approx 3300 - 4000\text{ m/s}\).
- **D (Incorrect):** Air conducts sound at only \(\approx 344\text{ m/s}\)."""
    }

    # Q93: MH-9-SCIT-12-12.1-OSC-093
    enhancements[92] = {
        "text": "During the periodic oscillation of a simple pendulum between extreme positions f and h through central point g, at which position is the linear velocity of the pendulum bob MAXIMUM?",
        "options": [
            "At extreme points f and h",
            "At central equilibrium point g",
            "Somewhere halfway between points f and g",
            "The bob maintains constant uniform velocity throughout"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
A simple pendulum exchanges potential energy and kinetic energy cyclically according to the law of conservation of mechanical energy.

### 2. Wave Dynamics & Mathematical Derivation:
Let:
- \(f\) and \(h\) be the two turning points (maximum displacement / amplitude positions).
- \(g\) be the central vertical equilibrium position (lowest point of the swing).
By energy conservation:
\[
E_{\text{total}} = E_p + E_k = \text{constant}
\]
- At extreme points \(f\) and \(h\), the bob momentarily halts to reverse direction:
\[
v = 0 \implies E_k = 0, \quad E_p = mgh_{\text{max}}
\]
- At the central equilibrium point \(g\), the bob is at its lowest vertical height (\(h = 0 \implies E_p = 0\)). All gravitational potential energy is converted entirely into kinetic energy:
\[
E_{k,\text{max}} = \frac{1}{2} m v_{\text{max}}^2 = mgh_{\text{max}} \implies v_{\text{max}} = \sqrt{2gh_{\text{max}}}
\]
Therefore, the linear velocity of the bob is at its absolute maximum as it passes through the central equilibrium point \(g\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** At extreme points \(f\) and \(h\), velocity is zero (\(v = 0\)).
- **B (Correct):** Velocity is maximum at the central point \(g\) where potential energy is minimum and kinetic energy is maximum.
- **C (Incorrect):** Intermediate points have intermediate velocities between \(0\) and \(v_{\text{max}}\).
- **D (Incorrect):** Pendulum motion is accelerated SHM, not uniform velocity motion."""
    }

    # Q94: MH-9-SCIT-12-12.1-OSC-094
    enhancements[93] = {
        "text": "What is the time period of an acoustic wave whose vibration frequency is 100 Hz?",
        "options": [
            "0.1 s",
            "0.01 s",
            "0.001 s",
            "100 s"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The time period (\(T\)) is the temporal duration of one complete wave cycle, while frequency (\(\nu\)) is the number of cycles per second.

### 2. Wave Dynamics & Mathematical Derivation:
The inverse relationship between time period and frequency is:
\[
T = \frac{1}{\nu}
\]
Given:
\[
\nu = 100\text{ Hz}
\]
Substitute into the formula:
\[
T = \frac{1}{100} = 0.01\text{ s}
\]
Each complete acoustic wave cycle takes exactly \(0.01\text{ s}\) (\(10\text{ ms}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(0.1\text{ s}\) corresponds to \(\nu = 10\text{ Hz}\).
- **B (Correct):** \(T = \frac{1}{100} = 0.01\text{ s}\).
- **C (Incorrect):** \(0.001\text{ s}\) corresponds to \(\nu = 1000\text{ Hz}\).
- **D (Incorrect):** \(100\text{ s}\) confuses the numerical value of frequency with time."""
    }

    # Q95: MH-9-SCIT-12-12.1-OSC-095
    enhancements[94] = {
        "text": "The subjective physiological loudness of a sound depends directly upon which physical property of the wave?",
        "options": [
            "Amplitude of vibration",
            "Pitch of sound",
            "Speed of sound",
            "Wavelength of sound"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Loudness is the auditory sensation by which a listener assesses the strength or energy of a sound wave.

### 2. Wave Dynamics & Mathematical Derivation:
The intensity \(I\) of an acoustic wave is directly proportional to the square of its displacement amplitude \(A\):
\[
I = 2\pi^2 \rho v \nu^2 A^2 \implies I \propto A^2
\]
Larger vibration amplitudes produce larger alternating compressional pressure peaks (\(\Delta P_{\text{max}} \propto A\)). These exert greater force on the eardrum and fluid within the cochlea, resulting in greater neural discharge rates interpreted by the brain as increased **loudness**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Loudness depends directly on the amplitude of vibration.
- **B (Incorrect):** Pitch depends on frequency (\(\nu\)), not amplitude.
- **C (Incorrect):** Speed depends on the elastic properties of the medium.
- **D (Incorrect):** Wavelength is a spatial dimension governed by speed and frequency (\(\lambda = v/\nu\))."""
    }

    # Q96: MH-9-SCIT-12-12.1-OSC-096 (Fixed defect & ans alignment)
    enhancements[95] = {
        "text": "A simple pendulum has a time period of 1.0 s on Earth. If this pendulum is transported to the Moon (where gravity is approximately one-sixth of Earth's gravity, \\(g_{\\text{moon}} = \\frac{g_{\\text{earth}}}{6}\\)), what modification must be made to keep its time period UNCHANGED at 1.0 s?",
        "options": [
            "The length of the pendulum string should be decreased to one-sixth",
            "The bob of the pendulum should be made six times heavier",
            "The length of the pendulum string should be increased by six times",
            "The amplitude of swing should be doubled"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The period of a simple pendulum depends on the ratio of its physical length to local gravitational acceleration.

### 2. Wave Dynamics & Mathematical Derivation:
The time period formula is:
\[
T = 2\pi \sqrt{\frac{L}{g}}
\]
To maintain the same time period \(T_{\text{moon}} = T_{\text{earth}}\):
\[
2\pi \sqrt{\frac{L_{\text{moon}}}{g_{\text{moon}}}} = 2\pi \sqrt{\frac{L_{\text{earth}}}{g_{\text{earth}}}}
\]
Squaring both sides and simplifying:
\[
\frac{L_{\text{moon}}}{g_{\text{moon}}} = \frac{L_{\text{earth}}}{g_{\text{earth}}} \implies L_{\text{moon}} = L_{\text{earth}} \times \left(\frac{g_{\text{moon}}}{g_{\text{earth}}}\right)
\]
Since \(g_{\text{moon}} = \frac{1}{6} g_{\text{earth}}\):
\[
L_{\text{moon}} = \frac{L_{\text{earth}}}{6}
\]
Therefore, the length of the pendulum string must be **decreased to one-sixth of its original length**.
(Note: Changing the bob's mass has zero effect on the period because \(T\) is completely independent of mass).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** To offset a 6-fold reduction in \(g\), the length \(L\) must be reduced 6-fold so that the ratio \(L/g\) remains constant.
- **B (Incorrect):** Pendulum period is strictly independent of the mass of the bob.
- **C (Incorrect):** Increasing length would make the pendulum swing even slower, increasing its time period.
- **D (Incorrect):** For small oscillations, the time period is independent of amplitude."""
    }

    # Q97: MH-9-SCIT-12-12.1-OSC-097
    enhancements[96] = {
        "text": "Among the following atmospheric conditions, in which air medium will the speed of sound be the MINIMUM?",
        "options": [
            "Hot and dry air",
            "Hot and humid air",
            "Cold and humid air",
            "Cold and dry air"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The speed of sound in air is governed by both thermodynamic temperature and moisture content (humidity).

### 2. Wave Dynamics & Mathematical Derivation:
According to Laplace's formula:
\[
v = \sqrt{\frac{\gamma R T}{M}} \propto \sqrt{\frac{T}{\rho}}
\]
1. **Temperature dependence:** Sound speed is directly proportional to the square root of absolute temperature (\(v \propto \sqrt{T}\)). Therefore, sound travels slower in cold air than in hot air:
\[
v_{\text{cold}} < v_{\text{hot}}
\]
2. **Humidity dependence:** Water vapor (\(M_{\text{H}_2\text{O}} \approx 18\text{ g/mol}\)) is lighter than dry air (\(M_{\text{dry}} \approx 28.8\text{ g/mol}\)). Humid air has lower density than dry air at the same temperature and pressure. Since \(v \propto 1/\sqrt{\rho}\), sound travels slower in dry air than in humid air:
\[
v_{\text{dry}} < v_{\text{humid}}
\]
Combining both factors: sound travels slowest in **cold and dry air**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B (Incorrect):** Hot air possesses higher thermal molecular velocities, increasing sound speed.
- **C (Incorrect):** Humid air has lower density than dry air, which increases sound velocity.
- **D (Correct):** Cold temperature reduces molecular kinetic energy and dry conditions maximize air density, combining to produce the minimum speed of sound."""
    }

    # Q98: MH-9-SCIT-12-12.1-OSC-098
    enhancements[97] = {
        "text": "What is the recognized occupational limit of safe sound exposure for humans, above which prolonged exposure causes auditory fatigue and risk of hearing damage?",
        "options": [
            "20 decibels (dB)",
            "85 decibels (dB)",
            "120 decibels (dB)",
            "150 decibels (dB)"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Human auditory health depends on both the intensity level of incoming sound waves and the duration of continuous exposure.

### 2. Wave Dynamics & Mathematical Derivation:
Acoustic exposure standards established by the World Health Organization (WHO) and OSHA designate **\(85\text{ dB}\)** as the critical occupational threshold:
- Below \(80 - 85\text{ dB}\), everyday sound exposure poses no significant risk of permanent sensorineural hearing impairment.
- Continuous exposure to sounds at or above **\(85\text{ dB}\)** (such as heavy industrial machinery, lawnmowers, or loud traffic) for 8 hours daily damages the sensory hair cells of the cochlea over time.
- \(120\text{ dB}\) represents the threshold of discomfort.
- \(130 - 140\text{ dB}\) represents the threshold of acute physical pain and immediate eardrum trauma.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(20\text{ dB}\) is a whisper or quiet rustling of leaves.
- **B (Correct):** \(85\text{ dB}\) is the recognized safe exposure threshold limit for human hearing.
- **C (Incorrect):** \(120\text{ dB}\) is the threshold of severe ear discomfort.
- **D (Incorrect):** \(150\text{ dB}\) causes immediate acoustic trauma and rupture of the eardrum."""
    }

    # Q99: MH-9-SCIT-12-12.1-OSC-099
    enhancements[98] = {
        "text": "When a mechanical wave disturbance passes through a material medium, what type of motion is executed by the individual particles of the medium?",
        "options": [
            "Translational motion across long distances",
            "Vibrational (oscillatory) motion about their mean equilibrium positions",
            "Pure continuous rotational motion",
            "Random, unbounded Brownian displacement"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Wave propagation fundamentally differs from bulk mass transport. A wave is the propagation of a dynamic state of disturbance, not the migration of particles.

### 2. Wave Dynamics & Mathematical Derivation:
When a wave travels through an elastic medium:
- Medium particles undergo simple harmonic **vibrational (oscillatory) motion** about their mean equilibrium positions:
\[
x(t) = x_0 + A \sin(\omega t + \phi)
\]
- Over any integer number of complete cycles, the average position and net displacement of any particle is strictly zero:
\[
\Delta \vec{r}_{\text{net}} = \int_0^{n T} \vec{v}_{\text{particle}} \, dt = 0
\]
The particles merely transfer momentum and energy to adjacent neighbors via elastic intermolecular forces, while remaining anchored in their local equilibrium positions.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Particles do not undergo translational migration across the medium.
- **B (Correct):** Particles execute localized oscillatory/vibrational motion about their equilibrium positions.
- **C, D (Incorrect):** Particles do not undergo continuous rotational motion or unbounded random drift during wave transmission."""
    }

    # Q100: MH-9-SCIT-12-12.1-OSC-100
    enhancements[99] = {
        "text": "Bats locate flying insect prey and navigate in total darkness by detecting reflected:",
        "options": [
            "Infrasonic waves",
            "Radio waves",
            "Electromagnetic microwaves",
            "Ultrasonic waves"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Echolocation (biosonar) allows microbats to fly at high speeds through dense obstacle fields and capture tiny insects in the dark.

### 2. Wave Dynamics & Mathematical Derivation:
1. Bats emit high-frequency acoustic vocal pulses in the **ultrasonic range** (\(\nu > 20\text{ kHz}\), typically \(30 - 100\text{ kHz}\)).
2. Ultrasound provides millimeter-scale wavelengths (\(\lambda \sim 3 - 10\text{ mm}\)), which match the physical dimensions of insects, ensuring strong specular reflections.
3. The returning ultrasonic echoes are captured by the bat's external ears (pinnae) and processed by an enlarged auditory cortex to compute distance (\(d = \frac{v t}{2}\)), angle, size, and relative velocity.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Infrasound (\(< 20\text{ Hz}\)) has wavelengths too large to reflect off small obstacles or prey.
- **B, C (Incorrect):** Bats are biological organisms that emit mechanical sound waves, not electromagnetic radio or microwaves.
- **D (Correct):** Bats detect reflected ultrasonic sound waves."""
    }

    # Q101: MH-9-SCIT-12-12.1-OSC-101
    enhancements[100] = {
        "text": "An acoustic wave travels through a medium with a speed of 500 m/s. If its vibration frequency is 25 Hz, what is its time period?",
        "options": [
            "20 s",
            "0.05 s",
            "25 s",
            "0.04 s"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The time period (\(T\)) of a wave is determined strictly by its vibration frequency (\(\nu\)), and is independent of the wave speed through the medium.

### 2. Wave Dynamics & Mathematical Derivation:
The relationship between time period and frequency is:
\[
T = \frac{1}{\nu}
\]
Given:
- Frequency, \(\nu = 25\text{ Hz}\)
- Speed, \(v = 500\text{ m/s}\) (Note: Speed is provided but is not required to calculate time period; it would be used if calculating wavelength \(\lambda = v/\nu = 500/25 = 20\text{ m}\)).

Substitute the frequency into the time period formula:
\[
T = \frac{1}{25} = \frac{4}{100} = 0.04\text{ s}
\]
The time period of the wave is \(0.04\text{ s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(20\text{ s}\) is the wavelength (\(\lambda = 500/25 = 20\text{ m}\)) mistakenly labeled with units of seconds.
- **B (Incorrect):** \(0.05\text{ s}\) corresponds to a frequency of \(20\text{ Hz}\).
- **C (Incorrect):** \(25\text{ s}\) confuses the numerical value of frequency with time period.
- **D (Correct):** \(T = \frac{1}{25} = 0.04\text{ s}\)."""
    }

    # Q102: MH-9-SCIT-12-12.1-OSC-102
    enhancements[101] = {
        "text": "The amplitude of a traveling wave is formally defined as:",
        "options": [
            "The linear distance traveled by the wave front in one second",
            "The distance advanced by the wave in one complete time period",
            "The maximum displacement of medium particles on either side of their mean equilibrium position",
            "The distance between two consecutive wave compressions"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Wave motion involves two distinct spatial dimensions: the longitudinal or transverse displacement of medium particles, and the propagation distance of the wave front.

### 2. Wave Dynamics & Mathematical Derivation:
In simple harmonic wave motion:
\[
y(x,t) = A \sin(kx - \omega t)
\]
The equilibrium coordinate is \(y = 0\). As the wave passes:
- The maximum positive displacement is \(y_{\text{max}} = +A\).
- The maximum negative displacement is \(y_{\text{min}} = -A\).
The magnitude \(A\) represents the **amplitude** of the wave. It measures the physical magnitude of particle excursion from the resting equilibrium position and determines the wave's total mechanical energy (\(E \propto A^2\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Distance traveled per second is the *wave speed (\(v\))*.
- **B (Incorrect):** Distance traveled in one time period is the *wavelength (\(\lambda\))*.
- **C (Correct):** Amplitude is the maximum displacement of particles from their mean position.
- **D (Incorrect):** Distance between consecutive compressions is the *wavelength (\(\lambda\))*."""
    }

    # Q103: MH-9-SCIT-12-12.1-OSC-103
    enhancements[102] = {
        "text": "Which of the following is NOT one of the three primary subjective characteristics used by the human ear to distinguish musical sounds?",
        "options": [
            "Pitch",
            "Wavelength",
            "Loudness",
            "Quality or Timbre"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
A musical sound produces a pleasing sensation on the human ear and is distinguished from noise by three fundamental subjective perceptual characteristics.

### 2. Wave Dynamics & Mathematical Derivation:
The three recognized musical characteristics of sound are:
1. **Loudness:** Correlates with acoustic intensity and wave amplitude (\(I \propto A^2\)), distinguishing faint sounds from loud sounds.
2. **Pitch:** Correlates with wave frequency (\(\nu\)), distinguishing shrill/high-pitched sounds from deep/grave sounds.
3. **Quality or Timbre:** Correlates with the acoustic waveform and harmonic overtone spectrum, allowing the ear to distinguish between two instruments playing notes of the same pitch and loudness.
In contrast, **wavelength (\(\lambda\))** is an objective physical parameter of the wave in the medium (\(\lambda = v/\nu\)), not a direct sensory characteristic of musical perception.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, C, D (Incorrect choices to select):** Pitch, Loudness, and Quality/Timbre are the three canonical characteristics of musical sound.
- **B (Correct):** Wavelength is a physical wave dimension dependent on the medium, not a perceptual musical sound characteristic."""
    }

    # Q104: MH-9-SCIT-12-12.1-OSC-104
    enhancements[103] = {
        "text": "During the propagation of most mechanical waves, which physical property of the medium particles periodically oscillates about equilibrium?",
        "options": [
            "Rest mass",
            "Molecular chemical identity",
            "Displacement (position)",
            "Total atomic volume"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Mechanical waves transfer energy through the periodic kinematic disturbance of the particles comprising an elastic medium.

### 2. Wave Dynamics & Mathematical Derivation:
When a mechanical wave passes through a medium:
- The rest mass, atomic volume, and chemical composition of the molecules remain strictly unchanged.
- What oscillates periodically is the **positional displacement (\(s\))** of the particles from their resting equilibrium coordinates:
\[
s(t) = A \sin(\omega t + \phi)
\]
In longitudinal waves, particles oscillate along the line of wave motion; in transverse waves, they oscillate perpendicular to it.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, D (Incorrect):** Mass, chemical identity, and atomic volume are invariant intrinsic physical properties that do not oscillate.
- **C (Correct):** Particle displacement (position relative to equilibrium) oscillates periodically during wave propagation."""
    }

    # Q105: MH-9-SCIT-12-12.1-OSC-105
    enhancements[104] = {
        "text": "Which of the following physical quantities will remain completely UNCHANGED when an acoustic sound wave passes from air into water?",
        "options": [
            "Displacement amplitude",
            "Wavelength",
            "Frequency",
            "Speed of sound"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
When an acoustic wave undergoes boundary transmission (refraction) from one medium to another, boundary continuity conditions dictate which properties vary and which remain conserved.

### 2. Wave Dynamics & Mathematical Derivation:
- **Frequency (\(\nu\)):** Governed exclusively by the periodic driving frequency of the original vibrating source. At the interface, air molecules force water molecules to oscillate at the exact same rhythm, keeping frequency invariant:
\[
\nu_{\text{water}} = \nu_{\text{air}}
\]
- **Speed (\(v\)):** Increases from \(\approx 344\text{ m/s}\) in air to \(\approx 1500\text{ m/s}\) in water.
- **Wavelength (\(\lambda\)):** Must expand proportionally since \(\lambda = v/\nu\).
- **Amplitude (\(A\)):** Decreases due to partial reflection at the boundary.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Amplitude decreases due to partial acoustic energy reflection.
- **B (Incorrect):** Wavelength increases by over fourfold in water.
- **C (Correct):** Frequency is an invariant property governed solely by the source.
- **D (Incorrect):** Sound speed changes dramatically between air and water."""
    }

    # Q106: MH-9-SCIT-12-12.1-OSC-106
    enhancements[105] = {
        "text": "A sound source emits acoustic waves at a frequency of 400 Hz. If the measured wavelength of these waves is 2.5 m, what is the propagation velocity of the sound waves?",
        "options": [
            "100 m/s",
            "1000 m/s",
            "10,000 m/s",
            "160 m/s"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The propagation velocity of any wave is mathematically equal to the product of its vibration frequency and its spatial wavelength.

### 2. Wave Dynamics & Mathematical Derivation:
The wave speed formula is:
\[
v = \nu \times \lambda
\]
Given:
- Frequency, \(\nu = 400\text{ Hz} = 400\text{ s}^{-1}\)
- Wavelength, \(\lambda = 2.5\text{ m}\)

Multiply the two quantities:
\[
v = 400 \times 2.5 = 400 \times \frac{5}{2} = 200 \times 5 = 1000\text{ m/s}
\]
The velocity of the sound waves through this medium is \(1000\text{ m/s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(100\text{ m/s}\) represents a decimal calculation error.
- **B (Correct):** \(v = 400 \times 2.5 = 1000\text{ m/s}\).
- **C (Incorrect):** \(10{,}000\text{ m/s}\) has an extra factor of 10.
- **D (Incorrect):** \(160\text{ m/s}\) results from dividing frequency by wavelength (\(400 / 2.5\))."""
    }

    # Q107: MH-9-SCIT-12-12.1-OSC-107
    enhancements[106] = {
        "text": "A sound source vibrating at a frequency of 500 Hz emits waves of wavelength 0.40 m. How long will it take for these waves to travel a distance of 600 m through the medium?",
        "options": [
            "3.0 s",
            "6.0 s",
            "9.0 s",
            "1.2 s"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Determining wave transit time over a macroscopic distance requires first calculating the propagation velocity from the wave's spectral parameters.

### 2. Wave Dynamics & Mathematical Derivation:
Step 1: Calculate the wave velocity \(v\):
\[
v = \nu \times \lambda
\]
Given:
- \(\nu = 500\text{ Hz}\)
- \(\lambda = 0.40\text{ m}\)
\[
v = 500 \times 0.40 = 200\text{ m/s}
\]

Step 2: Calculate the time \(t\) required to travel distance \(d = 600\text{ m}\):
\[
t = \frac{d}{v} = \frac{600\text{ m}}{200\text{ m/s}} = 3.0\text{ s}
\]
It takes exactly \(3.0\text{ seconds}\) for the sound wave to traverse \(600\text{ m}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** \(v = 500 \times 0.4 = 200\text{ m/s}\); \(t = 600 / 200 = 3.0\text{ s}\).
- **B (Incorrect):** \(6.0\text{ s}\) results from dividing 600 by 100.
- **C (Incorrect):** \(9.0\text{ s}\) is an arbitrary multiple.
- **D (Incorrect):** \(1.2\text{ s}\) results from calculating \(600 / 500\)."""
    }

    # Q108: MH-9-SCIT-12-12.1-OSC-108
    enhancements[107] = {
        "text": "Which of the following physical characteristics is shared in common by BOTH sound waves and light waves?",
        "options": [
            "Both have identical wavelengths of the same order of magnitude",
            "Both obey the fundamental laws of reflection",
            "Both propagate through atmospheric air as longitudinal waves",
            "Both can propagate freely across a complete vacuum"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Although sound is a mechanical wave and light is an electromagnetic wave, all wave phenomena follow universal geometric wave reflection principles at planar and curved boundaries.

### 2. Wave Dynamics & Mathematical Derivation:
Both sound waves and light waves strictly obey the **laws of reflection**:
1. The incident wave ray, the reflected wave ray, and the normal to the reflecting surface at the point of incidence all lie in the same plane.
2. The angle of incidence equals the angle of reflection:
\[
\theta_i = \theta_r
\]
This principle is exploited by curved sound reflectors in auditoriums and parabolic satellite dishes/telescopes alike.

Differences:
- Light travels in vacuum (\(c \approx 3 \times 10^8\text{ m/s}\)); sound requires a medium (\(v_{\text{vacuum}} = 0\)).
- Light is transverse; sound in air is longitudinal.
- Audible sound has wavelengths of \(\sim 1.7\text{ cm} - 17\text{ m}\); visible light has wavelengths of \(\sim 400 - 700\text{ nm}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Audible sound wavelengths are millions of times longer than visible light wavelengths.
- **B (Correct):** Both sound and light waves strictly obey the laws of reflection (\(\theta_i = \theta_r\)).
- **C (Incorrect):** Light is a transverse wave, while sound in air is longitudinal.
- **D (Incorrect):** Sound cannot travel through a vacuum."""
    }

    # Q109: MH-9-SCIT-12-12.1-OSC-109
    enhancements[108] = {
        "text": "In a longitudinal sound wave, rarefactions are localized regions of the medium where:",
        "options": [
            "Density and pressure are both at their minimum",
            "Density and pressure are both at their maximum",
            "Density is low while pressure is high",
            "Particles are compressed together at maximum concentration"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Longitudinal waves propagate through alternating spatial fluctuations of particle concentration and pressure.

### 2. Wave Dynamics & Mathematical Derivation:
In a longitudinal acoustic wave:
- **Compressions:** The vibrating source pushes medium particles together, creating high density (\(\rho > \rho_0\)) and high pressure (\(P > P_0\)).
- **Rarefactions:** As the vibrating source retracts, medium particles expand into the vacated space, creating an expanded region where particles are spaced farthest apart:
\[
\rho < \rho_0, \quad P < P_0
\]
Both density and pressure drop to their localized **minimum** values in rarefactions.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Rarefactions are regions where density and pressure are both at their minimum.
- **B (Incorrect):** High density and pressure define *compressions*.
- **C (Incorrect):** Pressure and density fluctuations in an acoustic wave vary in phase.
- **D (Incorrect):** Maximum particle concentration describes compressions."""
    }

    # Q110: MH-9-SCIT-12-12.1-OSC-110 (Fixed catch-all)
    enhancements[109] = {
        "text": "Sound waves in air are classified as longitudinal waves because:",
        "options": [
            "Particles of the medium vibrate parallel to the direction of wave propagation",
            "Particles of the medium vibrate perpendicular to the direction of wave propagation",
            "They propagate exclusively as oscillating electric and magnetic fields",
            "They do not require any physical material medium to travel"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The fundamental classification of mechanical waves into longitudinal and transverse is determined strictly by the orientation of particle oscillation relative to the vector of wave travel.

### 2. Wave Dynamics & Mathematical Derivation:
In atmospheric air, sound propagates by pressure oscillations:
\[
\vec{v}_{\text{particle}} \parallel \vec{v}_{\text{wave}}
\]
Medium particles oscillate back and forth parallel to the direction along which the sound wave advances. This back-and-forth motion creates sequential compressions and rarefactions. By physical definition, any wave where particle oscillation is parallel to wave propagation is a **longitudinal wave**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** In longitudinal waves, particles vibrate parallel to the direction of wave movement.
- **B (Incorrect):** Perpendicular particle vibration defines *transverse waves*.
- **C (Incorrect):** Oscillating electric and magnetic fields define *electromagnetic waves*.
- **D (Incorrect):** Sound is a mechanical wave and requires a material medium."""
    }

    # Q111: MH-9-SCIT-12-12.1-OSC-111
    enhancements[110] = {
        "text": "What is the minimum distance required between an acoustic sound source and a reflecting surface to hear a distinct, separate echo in air at 22 °C?",
        "options": [
            "10.0 m",
            "17.2 m (approximately 17 m)",
            "34.4 m",
            "50.0 m"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
An echo is a reflected sound wave heard separately from the direct original sound. For the human brain to perceive two sounds as distinct, they must arrive separated by a minimum temporal interval.

### 2. Wave Dynamics & Mathematical Derivation:
1. **Persistence of Hearing:** The auditory sensation of an original sound persists in the human brain for approximately \(0.1\text{ s}\) (\(\frac{1}{10}\text{ s}\)). Any reflection arriving sooner than \(0.1\text{ s}\) blends with the original sound, producing reverberation rather than a distinct echo.
2. **Speed of Sound:** At \(22^\circ\text{C}\), the speed of sound in air is \(v \approx 344\text{ m/s}\).
3. **Round-Trip Distance:**
\[
2d = v \times t \implies d = \frac{v \times t}{2}
\]
Substituting \(t = 0.1\text{ s}\) and \(v = 344\text{ m/s}\):
\[
d = \frac{344 \times 0.1}{2} = \frac{34.4}{2} = 17.2\text{ m}
\]
Thus, the reflector must be at least **\(17.2\text{ m}\)** away (approximately \(17\text{ m}\)) for a distinct echo to be heard.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(10.0\text{ m}\) results in an echo arriving in \(0.058\text{ s}\), which blends into reverberation.
- **B (Correct):** The minimum distance to hear a distinct echo at \(22^\circ\text{C}\) is \(17.2\text{ m}\).
- **C (Incorrect):** \(34.4\text{ m}\) is the total round-trip path length (\(2d\)).
- **D (Incorrect):** \(50.0\text{ m}\) is well beyond the minimum threshold distance."""
    }

    # Q112: MH-9-SCIT-12-12.1-OSC-112
    enhancements[111] = {
        "text": "If the speed of an acoustic sound wave in air is 340 m/s and its frequency is 1700 Hz, what is its wavelength (\\(\\lambda\\)) expressed in centimetres?",
        "options": [
            "2 cm",
            "0.2 cm",
            "20 cm",
            "200 cm"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The fundamental wave relation connects velocity, frequency, and wavelength.

### 2. Wave Dynamics & Mathematical Derivation:
The wave equation states:
\[
v = \nu \lambda \implies \lambda = \frac{v}{\nu}
\]
Given:
- Speed of sound, \(v = 340\text{ m/s}\)
- Frequency, \(\nu = 1700\text{ Hz}\)

Calculate wavelength in metres:
\[
\lambda = \frac{340\text{ m/s}}{1700\text{ s}^{-1}} = \frac{34}{170} = \frac{2}{10} = 0.2\text{ m}
\]
Convert metres to centimetres (\(1\text{ m} = 100\text{ cm}\)):
\[
\lambda = 0.2 \times 100 = 20\text{ cm}
\]
The wavelength of this sound wave is \(20\text{ cm}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(2\text{ cm}\) represents a factor-of-10 conversion error.
- **B (Incorrect):** \(0.2\text{ cm}\) is the wavelength in metres, not centimetres.
- **C (Correct):** \(\lambda = \frac{340}{1700}\text{ m} = 0.2\text{ m} = 20\text{ cm}\).
- **D (Incorrect):** \(200\text{ cm} = 2.0\text{ m}\), corresponding to a frequency of \(170\text{ Hz}\)."""
    }

    # Q113: MH-9-SCIT-12-12.1-OSC-113
    enhancements[112] = {
        "text": "In what fundamental physical respect is a sound wave DIFFERENT from a light wave?",
        "options": [
            "Light waves transfer energy while sound waves do not transfer any energy",
            "Sound waves require a material medium and cannot propagate through a vacuum, whereas light waves propagate through a vacuum",
            "Sound waves cannot undergo reflection, whereas light waves can reflect",
            "Sound waves have only a single frequency, whereas light has a wide frequency spectrum"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Understanding the physical boundary between mechanical waves and electromagnetic waves is fundamental to wave physics.

### 2. Wave Dynamics & Mathematical Derivation:
- **Sound waves** are **mechanical waves** that transmit energy via elastic particle collisions in a material medium. In a vacuum, where no particles exist, sound velocity is zero:
\[
v_{\text{sound, vacuum}} = 0\text{ m/s}
\]
- **Light waves** are **electromagnetic waves** consisting of oscillating electric (\(\vec{E}\)) and magnetic (\(\vec{B}\)) fields that do not require any material medium:
\[
c_{\text{light, vacuum}} \approx 3 \times 10^8\text{ m/s}
\]
Both wave types transfer energy, both obey the laws of reflection and refraction, and both exist across continuous frequency spectra.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Both sound and light waves transport energy and momentum across space.
- **B (Correct):** Sound requires a material medium and cannot travel through a vacuum, whereas light propagates freely through a vacuum.
- **C (Incorrect):** Both sound and light undergo regular and diffuse reflection.
- **D (Incorrect):** Both sound and light exist across wide, continuous frequency spectra."""
    }

    # Q114: MH-9-SCIT-12-12.1-OSC-114
    enhancements[113] = {
        "text": "When a guitar string is plucked, what is the wave classification of the vibrations traveling along the string itself, and the sound waves produced in the surrounding air?",
        "options": [
            "Transverse in the string, and Transverse in air",
            "Longitudinal in the string, and Longitudinal in air",
            "Longitudinal in the string, and Transverse in air",
            "Transverse in the string, and Longitudinal in air"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Musical string instruments couple two distinct media: an elastic taut metallic/nylon solid wire and the surrounding compressible fluid atmosphere.

### 2. Wave Dynamics & Mathematical Derivation:
1. **Along the guitar wire:** Plucking pulls the string sideways perpendicular to its length. Elastic tension creates sideways restoring forces, causing string particles to oscillate perpendicular to the string axis (\(\vec{y} \perp \vec{x}\)). Hence, the waves traveling along the wire are **transverse standing waves**.
2. **In the surrounding air:** As the transverse string vibrates laterally, its outer surface repeatedly pushes and pulls adjacent air layers, setting up alternating compressions and rarefactions where air particles oscillate parallel to the outward acoustic radiation:
\[
\vec{v}_{\text{air particle}} \parallel \vec{v}_{\text{wave}}
\]
Hence, the sound waves traveling through the air are **longitudinal waves**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Sound cannot propagate as a transverse wave in bulk air because air has zero shear modulus.
- **B (Incorrect):** Plucking vibrates the string laterally (transverse), not along its length.
- **C (Incorrect):** Reverses the physical mechanisms of the string and air.
- **D (Correct):** The vibrations in the string are transverse, while the sound waves produced in the surrounding air are longitudinal."""
    }

    return enhancements

if __name__ == '__main__':
    data = get_part3_enhancements()
    print(f"Generated {len(data)} enhancements for Part 3 (Q77 to Q114).")
