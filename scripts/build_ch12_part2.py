"""
build_ch12_part2.py: Generates enhanced Q39 to Q76 for Chapter 12 (Study of Sound).
"""

import json

def get_part2_enhancements():
    # Return dictionary keyed by question index (38 to 75)
    enhancements = {}

    # Q39: MH-9-SCIT-12-12.1-OSC-039
    enhancements[38] = {
        "text": "Identify the acoustic technology: 'I am used for underwater communication between ships, detecting internal cracks in metal castings, destroying pathogens in milk, and ultrasonic plastic welding.'",
        "options": [
            "Thermal radiation",
            "Ultrasound (Ultrasonic waves)",
            "Audible reverberation",
            "Infrasonic waves"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Ultrasound refers to acoustic waves with frequencies exceeding \(20{,}000\text{ Hz}\) (\(20\text{ kHz}\)). Because of their high frequency and correspondingly short wavelength (\(\lambda = v/\nu\)), ultrasonic waves can carry high energy in focused, narrow beams without significant diffraction spreading.

### 2. Wave Dynamics & Mathematical Derivation:
Key practical applications of ultrasound:
1. **Marine Communication & Ranging:** Exploited in SONAR systems to transmit directional acoustic pulses between naval vessels and map submarine obstacles.
2. **Industrial Non-Destructive Testing (NDT):** Ultrasonic pulses sent through metal blocks reflect off internal flaws, voids, or micro-cracks before reaching the opposite boundary, revealing internal defects.
3. **Sterilization of Liquids (Milk):** Intense ultrasound creates acoustic cavitation—rapid formation and violent collapse of microscopic vapor bubbles generating localized shockwaves and extreme shear stress that rupture bacterial cell membranes.
4. **Plastic Welding:** High-frequency ultrasonic vibrations generate localized frictional heat at joint seams, melting and fusing thermoplastic components cleanly.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Thermal radiation consists of electromagnetic infrared waves, not directional acoustic mechanical vibrations.
- **B (Correct):** Ultrasound (\(\nu > 20\text{ kHz}\)) possesses the energetic and directional properties required for all four listed applications.
- **C (Incorrect):** Audible reverberation is the prolonged persistence of sound in an auditorium due to multiple wall reflections.
- **D (Incorrect):** Infrasound consists of low-frequency vibrations below \(20\text{ Hz}\), which spread with large diffraction and cannot focus into narrow beams."""
    }

    # Q40: MH-9-SCIT-12-12.1-OSC-040
    enhancements[39] = {
        "text": "In which of the following states of matter is the speed of sound generally MAXIMUM?",
        "options": [
            "Vacuum",
            "Solids",
            "Liquids",
            "Gases"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Sound is a mechanical wave whose propagation speed depends directly on the restoring elasticity of the medium and inversely on its inertial density.

### 2. Wave Dynamics & Mathematical Derivation:
In Newton-Laplace wave mechanics, the velocity of longitudinal sound waves is:
\[
v = \sqrt{\frac{E}{\rho}}
\]
where \(E\) is the relevant elastic modulus (Young's modulus \(Y\) in solids, bulk modulus \(B\) in fluids) and \(\rho\) is the mass density.
Although solids are denser than liquids and gases, their elastic moduli are thousands of times greater (\(Y_{\text{solid}} \gg B_{\text{liquid}} \gg \gamma P_{\text{gas}}\)) due to strong intermolecular chemical bonds. As a result:
\[
v_{\text{solid}} > v_{\text{liquid}} > v_{\text{gas}}
\]
- In solids (e.g., steel, aluminium): \(v \approx 5000 - 6420\text{ m/s}\)
- In liquids (e.g., water): \(v \approx 1400 - 1500\text{ m/s}\)
- In gases (e.g., air): \(v \approx 330 - 346\text{ m/s}\)
In a vacuum, sound cannot propagate at all (\(v = 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Sound cannot travel through a vacuum because it requires material particles.
- **B (Correct):** Sound travels fastest in solids due to their exceptionally high elastic restoring forces (Young's modulus).
- **C, D (Incorrect):** Liquids and gases have much lower bulk moduli, resulting in significantly lower sound velocities."""
    }

    # Q41: MH-9-SCIT-12-12.1-OSC-041 (Fixed defect)
    enhancements[40] = {
        "text": "The time period \\(T\\) of a simple pendulum executing small-amplitude oscillations is given by the formula:",
        "options": [
            "\\(T = 2\\pi \\sqrt{\\frac{g}{L}}\\)",
            "\\(T = \\frac{1}{2\\pi} \\sqrt{\\frac{L}{g}}\\)",
            "\\(T = 2\\pi \\sqrt{\\frac{L}{g}}\\)",
            "\\(T = 2\\pi \\sqrt{L \\cdot g}\\)"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
A simple pendulum undergoing small-angle displacement exhibits simple harmonic motion (SHM). Its restoring torque is provided by the tangential component of gravity.

### 2. Wave Dynamics & Mathematical Derivation:
For an angular displacement \(\theta\), the restoring torque is:
\[
\tau = - m g L \sin\theta \approx - m g L \theta \quad (\text{for small } \theta, \, \sin\theta \approx \theta)
\]
Applying Newton's second law for rotation:
\[
I \ddot{\theta} = - m g L \theta \implies (m L^2) \ddot{\theta} + m g L \theta = 0
\]
\[
\ddot{\theta} + \frac{g}{L} \theta = 0
\]
This is the standard equation of simple harmonic motion \(\ddot{\theta} + \omega^2 \theta = 0\), where angular frequency is:
\[
\omega = \sqrt{\frac{g}{L}}
\]
The time period \(T = \frac{2\pi}{\omega}\) is therefore:
\[
T = 2\pi \sqrt{\frac{L}{g}}
\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Inverts the fraction to \(\sqrt{g/L}\), which has units of \(\text{s}^{-1}\) (frequency), not time period.
- **B (Incorrect):** Incorrectly places \(2\pi\) in the denominator.
- **C (Correct):** \(T = 2\pi \sqrt{\frac{L}{g}}\) is the exact formula for the time period of a simple pendulum.
- **D (Incorrect):** Multiplies \(L \cdot g\), which yields dimensions of velocity, not time."""
    }

    # Q42: MH-9-SCIT-12-12.1-OSC-042
    enhancements[41] = {
        "text": "What is the time period of an acoustic wave having a vibration frequency of 50 Hz?",
        "options": [
            "0.2 s",
            "0.02 s",
            "0.5 s",
            "0.05 s"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The time period (\(T\)) represents the time taken by any particle of the medium to complete one full cycle of vibration. Frequency (\(\nu\)) is the number of complete vibration cycles occurring per second.

### 2. Wave Dynamics & Mathematical Derivation:
The relationship between time period and frequency is:
\[
T = \frac{1}{\nu}
\]
Given:
\[
\nu = 50\text{ Hz}
\]
Substitute into the relation:
\[
T = \frac{1}{50} = \frac{2}{100} = 0.02\text{ s}
\]
Each complete acoustic wave cycle takes exactly \(0.02\text{ seconds}\) (\(20\text{ milliseconds}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(0.2\text{ s}\) corresponds to a frequency of \(\nu = 1/0.2 = 5\text{ Hz}\).
- **B (Correct):** \(T = 1/50 = 0.02\text{ s}\).
- **C (Incorrect):** \(0.5\text{ s}\) corresponds to \(\nu = 2\text{ Hz}\).
- **D (Incorrect):** \(0.05\text{ s}\) corresponds to \(\nu = 1/0.05 = 20\text{ Hz}\)."""
    }

    # Q43: MH-9-SCIT-12-12.1-OSC-043
    enhancements[42] = {
        "text": "Which internal structure of the human ear discriminates and encodes the specific auditory qualities of loudness and pitch?",
        "options": [
            "Tympanic membrane (Eardrum)",
            "Cochlea",
            "Auditory canal",
            "Eustachian tube"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The human ear receives external mechanical sound pressure vibrations, magnifies them mechanically via ossicles, and transduces them into biological neural action potentials in the inner ear.

### 2. Wave Dynamics & Mathematical Derivation:
- The **cochlea** is a fluid-filled coiled structure in the inner ear. It contains the **basilar membrane**, which varies continuously in width and stiffness along its length.
- **Pitch Discrimination (Frequency):** High-frequency sound waves cause maximal resonance near the narrow, stiff base of the cochlea, while low-frequency sounds travel further to stimulate the wide, flexible apex (Helmholtz's place theory of hearing).
- **Loudness Discrimination (Intensity):** Louder sounds carry greater wave amplitude, causing greater mechanical displacement of stereocilia on the hair cells, triggering a higher firing frequency of nerve impulses.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** The eardrum vibrates mechanically in response to incoming pressure waves, but cannot perform frequency/spectral analysis.
- **B (Correct):** The cochlea contains the sensory hair cells along the basilar membrane that distinguish frequency (pitch) and amplitude (loudness).
- **C (Incorrect):** The auditory canal is an acoustic passageway directing sound waves inward.
- **D (Incorrect):** The Eustachian tube equalizes air pressure between the middle ear cavity and the nasopharynx."""
    }

    # Q44: MH-9-SCIT-12-12.1-OSC-044
    enhancements[43] = {
        "text": "Which of the following physical quantities represents the linear distance between two successive compressions in a longitudinal sound wave?",
        "options": [
            "\\(\\frac{\\lambda}{4}\\)",
            "\\(\\lambda\\) (Wavelength)",
            "\\(2\\lambda\\)",
            "\\(\\frac{\\lambda}{2}\\)"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
In a longitudinal acoustic wave, compressions are regions where medium particles are crowded together at maximum density and pressure, while rarefactions are regions where particles are spaced farthest apart at minimum density.

### 2. Wave Dynamics & Mathematical Derivation:
A complete wave cycle in a longitudinal wave consists of one full compression and one full rarefaction.
Therefore, the spatial distance between:
- The centers of two successive compressions \(= \lambda\)
- The centers of two successive rarefactions \(= \lambda\)
- The center of a compression and the center of the immediately adjacent rarefaction \(= \frac{\lambda}{2}\)
Hence, the linear distance between two consecutive compressions is precisely one full **wavelength (\(\lambda\))**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(\frac{\lambda}{4}\) is the distance from a node to an adjacent antinode in a standing wave.
- **B (Correct):** The distance between two consecutive compressions represents one full periodic cycle, which is wavelength \(\lambda\).
- **C (Incorrect):** \(2\lambda\) is the distance spanning across three successive compressions.
- **D (Incorrect):** \(\frac{\lambda}{2}\) is the distance between a compression and its immediately adjacent rarefaction."""
    }

    # Q45: MH-9-SCIT-12-12.1-OSC-045
    enhancements[44] = {
        "text": "Identify the odd one out in the context of acoustic wave phenomena:",
        "options": [
            "RADAR",
            "SONAR",
            "Medical Ultrasonography",
            "Echolocation in bats"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Technological detection systems rely either on mechanical acoustic waves or on electromagnetic waves, which differ fundamentally in their physical nature and propagation requirements.

### 2. Wave Dynamics & Mathematical Derivation:
- **SONAR (B), Ultrasonography (C), and Bat Echolocation (D)** all operate strictly on high-frequency **ultrasonic mechanical waves** (\(\nu > 20\text{ kHz}\)). They require a material medium (water, biological tissue, or air) and detect reflected acoustic pressure pulses.
- **RADAR (A)** (Radio Detection and Ranging) operates on **electromagnetic waves** (microwaves or radio waves, \(\nu \approx 10^8 - 10^{11}\text{ Hz}\)) propagating at the speed of light (\(c \approx 3 \times 10^8\text{ m/s}\)) through air or vacuum.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct / Odd one out):** RADAR uses electromagnetic radio/microwaves, whereas the other three rely strictly on mechanical ultrasound waves.
- **B, C, D (Incorrect to select):** All three utilize acoustic ultrasound reflections (echoes)."""
    }

    # Q46: MH-9-SCIT-12-12.1-OSC-046
    enhancements[45] = {
        "text": "A person standing in a valley between two parallel vertical cliff walls fires a gun. He hears the first echo after 0.5 s and the second echo after 0.9 s. What is the total distance between the two cliffs? (Take speed of sound in air = 340 m/s)",
        "options": [
            "228 m",
            "238 m",
            "248 m",
            "476 m"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
When sound is produced between two reflective cliffs, echoes are heard separately from both walls. The sound travels from the person to each cliff and reflects back, covering twice the distance to that cliff.

### 2. Wave Dynamics & Mathematical Derivation:
Let \(d_1\) be the distance to the closer cliff and \(d_2\) be the distance to the farther cliff.
The total distance between the two cliffs is:
\[
D = d_1 + d_2
\]
For the first cliff (echo time \(t_1 = 0.5\text{ s}\)):
\[
2d_1 = v \times t_1 \implies d_1 = \frac{v \times t_1}{2} = \frac{340 \times 0.5}{2} = \frac{170}{2} = 85\text{ m}
\]
For the second cliff (echo time \(t_2 = 0.9\text{ s}\)):
\[
2d_2 = v \times t_2 \implies d_2 = \frac{v \times t_2}{2} = \frac{340 \times 0.9}{2} = \frac{306}{2} = 153\text{ m}
\]
The total distance between the two cliff faces is:
\[
D = d_1 + d_2 = 85 + 153 = 238\text{ m}
\]
(Alternatively: \(D = \frac{v(t_1 + t_2)}{2} = \frac{340 \times (0.5 + 0.9)}{2} = \frac{340 \times 1.4}{2} = 238\text{ m}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(228\text{ m}\) is an arithmetic miscalculation.
- **B (Correct):** \(D = d_1 + d_2 = 85\text{ m} + 153\text{ m} = 238\text{ m}\).
- **C (Incorrect):** \(248\text{ m}\) uses an incorrect speed of \(354\text{ m/s}\).
- **D (Incorrect):** \(476\text{ m}\) is the sum of the two round-trip distances (\(2d_1 + 2d_2\)) without dividing by 2."""
    }

    # Q47: MH-9-SCIT-12-12.1-OSC-047
    enhancements[46] = {
        "text": "An oscillating pendulum takes 2.0 seconds to complete one full oscillation from its extreme position, through the mean position to the opposite extreme, and back. What is its frequency of oscillation?",
        "options": [
            "1 Hz",
            "2 Hz",
            "0.5 Hz",
            "4 Hz"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
One complete oscillation of a pendulum comprises the entire round-trip motion: starting from one extreme, passing through the equilibrium point to the other extreme, and returning back to the starting extreme.

### 2. Wave Dynamics & Mathematical Derivation:
The time period \(T\) is the duration of one complete oscillation:
\[
T = 2.0\text{ s}
\]
Frequency (\(\nu\)) is the reciprocal of the time period:
\[
\nu = \frac{1}{T} = \frac{1}{2.0\text{ s}} = 0.5\text{ Hz}
\]
The pendulum completes \(0.5\) oscillations per second (or 1 full oscillation every 2 seconds).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(1\text{ Hz}\) corresponds to \(T = 1.0\text{ s}\).
- **B (Incorrect):** \(2\text{ Hz}\) incorrectly equates frequency to the time period value.
- **C (Correct):** \(\nu = \frac{1}{T} = \frac{1}{2.0} = 0.5\text{ Hz}\).
- **D (Incorrect):** \(4\text{ Hz}\) corresponds to a quarter-period calculation."""
    }

    # Q48: MH-9-SCIT-12-12.1-OSC-048
    enhancements[47] = {
        "text": "Which of the following wave phenomena consists naturally of a mixture of both longitudinal and transverse wave components?",
        "options": [
            "Seismic earthquake waves",
            "Microwave radiation",
            "X-ray radiation",
            "Visible light waves"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Seismic disturbances inside planetary bodies generate complex wave trains classified into body waves (traveling through the interior) and surface waves (traveling along the crust).

### 2. Wave Dynamics & Mathematical Derivation:
Earthquake seismic waves consist of:
1. **Primary waves (P-waves):** Fast longitudinal compressional waves where rock particles compress and dilate parallel to wave propagation (\(v_p \approx 6 - 8\text{ km/s}\)).
2. **Secondary waves (S-waves):** Slower transverse shear waves where rock particles vibrate perpendicular to wave propagation (\(v_s \approx 3.5 - 4.5\text{ km/s}\)).
3. **Surface waves (Rayleigh & Love waves):** Complex retrograde elliptical rolling motions combining vertical transverse and horizontal longitudinal motions.
Hence, seismic waves are a physical mixture of both longitudinal and transverse waves.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Seismic waves comprise longitudinal P-waves, transverse S-waves, and mixed Rayleigh/Love surface waves.
- **B, C, D (Incorrect):** Microwaves, X-rays, and visible light are pure transverse electromagnetic waves with no longitudinal component."""
    }

    # Q49: MH-9-SCIT-12-12.1-OSC-049 (Fixed teacher note & catch-alls)
    enhancements[48] = {
        "text": "What is the propagation velocity of sound waves in a vacuum?",
        "options": [
            "0 m/s (Sound cannot propagate in a vacuum)",
            "332 m/s",
            "3 × 10⁸ m/s",
            "1500 m/s"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Sound is a mechanical wave that propagates via sequential elastic collisions between atoms or molecules in a material medium.

### 2. Wave Dynamics & Mathematical Derivation:
The velocity of a mechanical wave is given by:
\[
v = \sqrt{\frac{\text{Elasticity}}{\text{Density}}}
\]
A vacuum is a region devoid of matter. Because there are no material particles to oscillate, compress, or exert restoring elastic forces, acoustic disturbances cannot be transmitted across empty space:
\[
v_{\text{sound, vacuum}} = 0\text{ m/s}
\]
(This was famously demonstrated by Robert Boyle's electric bell-in-a-bell-jar experiment: as air is evacuated with a vacuum pump, the ringing bell becomes fainter until no sound is audible, even though the hammer continues striking).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sound velocity in vacuum is strictly \(0\text{ m/s}\) because sound cannot travel without a material medium.
- **B (Incorrect):** \(332\text{ m/s}\) is the speed of sound in dry air at \(0^\circ\text{C}\).
- **C (Incorrect):** \(3 \times 10^8\text{ m/s}\) is the speed of electromagnetic light waves in vacuum.
- **D (Incorrect):** \(1500\text{ m/s}\) is the approximate speed of sound in liquid water."""
    }

    # Q50: MH-9-SCIT-12-12.1-OSC-050 (Fixed teacher note & catch-alls)
    enhancements[49] = {
        "text": "Sound level (or sound intensity level relative to the human hearing threshold) is commonly measured in units of:",
        "options": [
            "Decibels (dB)",
            "Hertz (Hz)",
            "Metres per second (m/s)",
            "Coulombs (C)"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Because the human ear responds to sound intensities over a vast range spanning twelve orders of magnitude (from the threshold of hearing at \(10^{-12}\text{ W/m}^2\) to the threshold of pain at \(1\text{ W/m}^2\)), acoustic intensity level is expressed on a logarithmic scale.

### 2. Wave Dynamics & Mathematical Derivation:
The sound level \(\beta\) in decibels (\(\text{dB}\)) is defined relative to the reference threshold intensity \(I_0 = 10^{-12}\text{ W/m}^2\):
\[
\beta = 10 \log_{10} \left(\frac{I}{I_0}\right) \text{ dB}
\]
The physical intensity \(I\) is measured in Watts per square metre (\(\text{W/m}^2\)), while the dimensionless logarithmic unit representing sound intensity level is the **decibel (dB)**, named in honor of Alexander Graham Bell.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sound intensity level is measured in decibels (\(\text{dB}\)).
- **B (Incorrect):** Hertz (\(\text{Hz}\)) is the SI unit of frequency (cycles per second), not intensity level.
- **C (Incorrect):** Metres per second (\(\text{m/s}\)) is the unit of wave velocity.
- **D (Incorrect):** Coulomb (\(\text{C}\)) is the unit of electric charge."""
    }

    # Q51: MH-9-SCIT-12-12.1-OSC-051 (Fixed defect)
    enhancements[50] = {
        "text": "When a sound wave travels from air into water, which of the following wave characteristics remains UNCHANGED?",
        "options": [
            "Amplitude",
            "Wave velocity",
            "Frequency",
            "Wavelength"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
When an acoustic wave crosses the boundary separating two different media, its propagation environment changes abruptly, but the fundamental periodicity of the source remains invariant.

### 2. Wave Dynamics & Mathematical Derivation:
- **Frequency (\(\nu\))** represents the number of wave cycles generated per second by the source. As wave fronts pass across an interface, each boundary particle must oscillate at the exact driving frequency of the preceding particle to maintain boundary continuity:
\[
\nu_{\text{water}} = \nu_{\text{air}} = \nu_{\text{source}}
\]
- **Speed (\(v\))** increases drastically from \(\approx 344\text{ m/s}\) in air to \(\approx 1500\text{ m/s}\) in water due to water's higher bulk modulus.
- **Wavelength (\(\lambda\))** must stretch proportionally according to \(v = \nu \lambda\):
\[
\lambda_{\text{water}} = \frac{v_{\text{water}}}{\nu} \approx 4.36 \times \lambda_{\text{air}}
\]
- **Amplitude (\(A\))** decreases because part of the incident wave energy is reflected back into the air.
Therefore, only **frequency** remains strictly unchanged.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Amplitude changes due to partial acoustic reflection and impedance mismatch.
- **B (Incorrect):** Velocity increases by over fourfold in water.
- **C (Correct):** Frequency is source-dependent and remains strictly constant during refraction.
- **D (Incorrect):** Wavelength increases in direct proportion to wave speed."""
    }

    # Q52: MH-9-SCIT-12-12.1-OSC-052
    enhancements[51] = {
        "text": "An explosion occurs at the water surface of a calm lake. A boatman located 100 m away on the water and a diver submerged 100 m directly beneath the explosion both listen for the blast. Who will hear the sound first?",
        "options": [
            "The boatman will hear the sound first",
            "The diver will hear the sound first",
            "Both will hear the sound at the exact same instant",
            "Neither will hear the sound because water absorbs all acoustic energy"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The time required for an acoustic pulse to traverse a given distance depends inversely on the speed of sound in the transmitting medium: \(t = d/v\).

### 2. Wave Dynamics & Mathematical Derivation:
Both observers are equidistant from the explosion: \(d = 100\text{ m}\).
- For the boatman, sound travels through **air** at:
\[
v_{\text{air}} \approx 344\text{ m/s} \implies t_{\text{boatman}} = \frac{100\text{ m}}{344\text{ m/s}} \approx 0.291\text{ s}
\]
- For the submerged diver, sound travels through **water** at:
\[
v_{\text{water}} \approx 1500\text{ m/s} \implies t_{\text{diver}} = \frac{100\text{ m}}{1500\text{ m/s}} \approx 0.067\text{ s}
\]
Comparing transit times:
\[
t_{\text{diver}} \approx 0.067\text{ s} \ll t_{\text{boatman}} \approx 0.291\text{ s}
\]
Because sound travels over four times faster in water than in air, the submerged diver will hear the sound first.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Sound travels significantly slower in air (\(\sim 344\text{ m/s}\)) than in liquid water.
- **B (Correct):** Sound travels at \(\sim 1500\text{ m/s}\) in water, reaching the diver in less than one-fourth the time taken to reach the boatman.
- **C (Incorrect):** Equal distance does not yield equal transit time when wave velocities differ.
- **D (Incorrect):** Water is an excellent conductor of acoustic waves."""
    }

    # Q53: MH-9-SCIT-12-12.1-OSC-053
    enhancements[52] = {
        "text": "In atmospheric air, sound propagates exclusively in the form of:",
        "options": [
            "Longitudinal mechanical waves",
            "Transverse mechanical waves",
            "Electromagnetic waves",
            "Torsional waves"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Fluids (liquids and gases) lack shear elasticity; they deform continuously under shear stress without generating an elastic restoring force.

### 2. Wave Dynamics & Mathematical Derivation:
Because air cannot resist shear, transverse waves (which require sideways restoring forces) cannot propagate in the bulk of a gas.
Air does, however, possess volume elasticity (bulk modulus \(B = \gamma P\)), resisting changes in volume and pressure. When a vibrating source oscillates, it compresses and decompresses adjacent air layers:
\[
\vec{s}_{\text{particle}} \parallel \vec{v}_{\text{wave}}
\]
Medium particles vibrate back and forth along the direction of propagation, transmitting sound strictly as **longitudinal waves** of alternating compressions and rarefactions.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sound propagates in gases exclusively as longitudinal mechanical waves.
- **B (Incorrect):** Transverse mechanical waves cannot propagate through bulk air because gases have zero shear modulus.
- **C (Incorrect):** Sound is an elastic pressure disturbance, not an electromagnetic field disturbance.
- **D (Incorrect):** Torsional waves require twisting rigidity, which gases lack entirely."""
    }

    # Q54: MH-9-SCIT-12-12.1-OSC-054
    enhancements[53] = {
        "text": "The persistent continuation of sound in an enclosed hall resulting from repeated, multiple reflections from walls, ceiling, and floor is known as:",
        "options": [
            "Single echo",
            "Acoustic scanning",
            "Reverberation",
            "Acoustic refraction"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
In an enclosed architectural space (auditorium, concert hall, or classroom), sound waves radiate outward and strike hard boundary surfaces repeatedly, generating a dense sequence of overlapping reflections.

### 2. Wave Dynamics & Mathematical Derivation:
- An **echo** is the discrete perception of a single, distinct reflected sound arriving at least \(0.1\text{ s}\) after the direct sound.
- If multiple reflected sound waves arrive at the listener's ear in rapid, continuous succession at intervals shorter than the persistence of hearing (\(< 0.1\text{ s}\)), the individual reflections blend together. This produces a continuous, decaying prolongation of the original sound known as **reverberation**.
- The time required for the acoustic sound pressure level to decay by \(60\text{ dB}\) after the source ceases is termed the **reverberation time (\(T_r\))**, modeled by Sabine's formula:
\[
T_r = \frac{0.161 \, V}{A_{\text{total}}}
\]
Excessive reverberation causes speech syllables to overlap, blurring words and making them unintelligible.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** A single echo is a distinct, separated reflection heard with a perceptible delay (\(\ge 0.1\text{ s}\)).
- **B (Incorrect):** Scanning refers to ultrasound medical or sonar imaging, not hall acoustics.
- **C (Correct):** The persistence of sound due to repeated reflections is defined as reverberation.
- **D (Incorrect):** Refraction is the bending of waves due to spatial velocity gradients."""
    }

    # Q55: MH-9-SCIT-12-12.1-OSC-055
    enhancements[54] = {
        "text": "The speed of sound in dry atmospheric air at 0 °C is approximately:",
        "options": [
            "1540 m/s",
            "450 m/s",
            "5100 m/s",
            "331 - 332 m/s"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The speed of sound in air was first derived theoretically by Isaac Newton and later corrected by Pierre-Simon Laplace to account for adiabatic compression and rarefaction.

### 2. Wave Dynamics & Mathematical Derivation:
According to Laplace's formula for an ideal gas:
\[
v = \sqrt{\frac{\gamma R T}{M}}
\]
At \(0^\circ\text{C}\) (\(T = 273.15\text{ K}\)):
- Ratio of specific heats for diatomic air: \(\gamma \approx 1.40\)
- Universal gas constant: \(R \approx 8.314\text{ J/(mol}\cdot\text{K)}\)
- Average molar mass of dry air: \(M \approx 0.0288\text{ kg/mol}\)

Substituting these values:
\[
v = \sqrt{\frac{1.40 \times 8.314 \times 273.15}{0.0288}} \approx \sqrt{110375} \approx 332.2\text{ m/s}
\]
Hence, the speed of sound in dry air at \(0^\circ\text{C}\) is approximately **\(331 - 332\text{ m/s}\)** (often approximated as \(330\text{ m/s}\) or \(332\text{ m/s}\) in standard textbook problems).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(\approx 1540\text{ m/s}\) is the speed of sound in human soft tissue or seawater.
- **B (Incorrect):** \(450\text{ m/s}\) is unrealistically high for cold air.
- **C (Incorrect):** \(5100\text{ m/s}\) is the speed of sound in solid aluminium or steel rods.
- **D (Correct):** Sound travels at approximately \(331 - 332\text{ m/s}\) in dry air at \(0^\circ\text{C}\)."""
    }

    # Q56: MH-9-SCIT-12-12.1-OSC-056
    enhancements[55] = {
        "text": "The time period of a simple pendulum is 2.0 s. What is its frequency of oscillation?",
        "options": [
            "2 Hz",
            "1 Hz",
            "0.5 Hz",
            "4 Hz"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
A simple pendulum with a time period of exactly \(2\text{ seconds}\) (taking \(1\text{ second}\) for each single swing in one direction) is historically known as a **seconds pendulum**.

### 2. Wave Dynamics & Mathematical Derivation:
The frequency of an oscillating system is defined as the reciprocal of its time period:
\[
\nu = \frac{1}{T}
\]
Given:
\[
T = 2.0\text{ s}
\]
Substitute into the formula:
\[
\nu = \frac{1}{2.0} = 0.5\text{ Hz}
\]
A seconds pendulum completes half an oscillation (\(0.5\text{ cycles}\)) per second.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Confuses time period with frequency; \(\nu = 1/T\), not \(T\).
- **B (Incorrect):** \(1\text{ Hz}\) corresponds to a time period of \(1.0\text{ s}\).
- **C (Correct):** \(\nu = \frac{1}{2} = 0.5\text{ Hz}\).
- **D (Incorrect):** \(4\text{ Hz}\) is an arbitrary square of the period."""
    }

    # Q57: MH-9-SCIT-12-12.1-OSC-057
    enhancements[56] = {
        "text": "SONAR navigation and depth-sounding equipment exclusively utilizes which category of waves?",
        "options": [
            "Infrasonic sound waves",
            "Ultrasonic sound waves",
            "Audible musical notes",
            "Visible laser light"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
SONAR operates underwater where light and electromagnetic radio waves suffer severe absorption and attenuation. Sound waves, however, propagate efficiently through water.

### 2. Wave Dynamics & Mathematical Derivation:
SONAR systems specifically employ **ultrasonic waves** (frequencies \(\nu > 20\text{ kHz}\), typically \(20\text{ kHz} - 100\text{ kHz}\)) rather than audible sound or infrasound for several compelling physical reasons:
1. **Short Wavelength:** Because \(\lambda = v/\nu\), high frequencies yield wavelengths of only a few centimeters or millimeters in water.
2. **Minimal Diffraction:** According to wave diffraction theory, waves bend around obstacles comparable to their wavelength. Shorter wavelengths produce sharply focused, pencil-like directional beams with negligible spreading.
3. **High Penetration & Reflection:** Ultrasound carries high acoustic power and reflects sharply off small obstacles without being obscured by background ocean noise.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Infrasonic waves have very long wavelengths that diffract heavily and cannot form directional ranging beams.
- **B (Correct):** SONAR uses ultrasonic sound because its short wavelength enables sharp directional beaming and high spatial resolution.
- **C (Incorrect):** Audible sound would cause nuisance noise and scatters widely.
- **D (Incorrect):** Light waves attenuate within tens of meters in turbid seawater."""
    }

    # Q58: MH-9-SCIT-12-12.1-OSC-058
    enhancements[57] = {
        "text": "What is the standard frequency range of audible sound waves for a healthy human ear?",
        "options": [
            "Between 20 Hz and 2,000 Hz",
            "Between 200 Hz and 20,000 Hz",
            "Between 20 Hz and 20,000 Hz",
            "Between 2,000 Hz and 20,000 Hz"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Human auditory perception is physiologically bounded by the biomechanical properties of the tympanic membrane, middle ear ossicles, and the resonance spectrum of the cochlear basilar membrane.

### 2. Wave Dynamics & Mathematical Derivation:
The acoustic spectrum relative to human hearing is divided into three distinct bands:
1. **Infrasonic range:** Frequencies below the lower threshold of audibility:
\[
\nu < 20\text{ Hz}
\]
2. **Audible range (Sonic range):** The band detectable by a healthy young human ear:
\[
20\text{ Hz} \le \nu \le 20{,}000\text{ Hz} \quad (20\text{ Hz} - 20\text{ kHz})
\]
3. **Ultrasonic range:** Frequencies above the upper limit of human hearing:
\[
\nu > 20{,}000\text{ Hz} \quad (> 20\text{ kHz})
\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Truncates the upper limit at \(2{,}000\text{ Hz}\), excluding high-pitched speech and musical overtones.
- **B (Incorrect):** Omits the deep bass frequencies between \(20\text{ Hz}\) and \(200\text{ Hz}\).
- **C (Correct):** The standard human audible range spans from \(20\text{ Hz}\) to \(20{,}000\text{ Hz}\).
- **D (Incorrect):** Omits all low and midrange frequencies."""
    }

    # Q59: MH-9-SCIT-12-12.1-OSC-059
    enhancements[58] = {
        "text": "At what continuous sound intensity level does acoustic exposure become hazardous noise pollution capable of causing hearing impairment?",
        "options": [
            "At and above 80 decibels (dB)",
            "At exactly 40 decibels (dB)",
            "At 20 decibels (dB)",
            "Only above 180 decibels (dB)"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Sound is categorized as musical/pleasant or as noise (unpleasant, irregular, or hazardous sound). Above specific exposure thresholds, acoustic sound pressure can permanently damage the stereocilia of hair cells in the cochlea.

### 2. Wave Dynamics & Mathematical Derivation:
According to the World Health Organization (WHO) and environmental safety standards:
- Normal conversational speech: \(\approx 60\text{ dB}\)
- Busy city traffic / threshold of hazardous noise: \(\approx 80 - 85\text{ dB}\)
- Heavy machinery / lawn mower: \(\approx 90\text{ dB}\)
- Threshold of physical ear pain: \(\approx 120 - 130\text{ dB}\)
Continuous or occupational exposure to sound levels exceeding **\(80\text{ dB}\)** causes auditory fatigue, elevated stress levels, sleep disturbance, and gradual sensorineural hearing loss.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sustained exposure at and above \(80\text{ dB}\) constitutes harmful noise pollution damaging to the human auditory system.
- **B (Incorrect):** \(40\text{ dB}\) represents a quiet residential room or library, well within safe limits.
- **C (Incorrect):** \(20\text{ dB}\) is a faint whisper.
- **D (Incorrect):** \(180\text{ dB}\) is the blast level of a rocket launch; hearing damage occurs at vastly lower levels (\(\ge 80\text{ dB}\))."""
    }

    # Q60: MH-9-SCIT-12-12.1-OSC-060 (Fixed teacher note & catch-alls)
    enhancements[59] = {
        "text": "When a sound wave refracts from air into water, which of the following physical quantities remains completely UNCHANGED?",
        "options": [
            "Frequency",
            "Speed of sound",
            "Wavelength",
            "Displacement amplitude"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
When an acoustic wave crosses from one medium to another, boundary conditions dictate how the kinematic and dynamic properties of the wave transform.

### 2. Wave Dynamics & Mathematical Derivation:
The three wave parameters are linked by:
\[
v = \nu \lambda
\]
1. **Frequency (\(\nu\)):** Governed solely by the driving source. Particles at the air-water boundary must oscillate at the exact same rhythm as the driving incident wave, so frequency remains invariant:
\[
\nu_{\text{water}} = \nu_{\text{air}}
\]
2. **Speed (\(v\)):** Increases from \(\approx 344\text{ m/s}\) in air to \(\approx 1500\text{ m/s}\) in water.
3. **Wavelength (\(\lambda\)):** Since \(v\) increases while \(\nu\) is constant, \(\lambda = v/\nu\) increases proportionally:
\[
\frac{\lambda_{\text{water}}}{\lambda_{\text{air}}} = \frac{v_{\text{water}}}{v_{\text{air}}} \approx 4.36
\]
4. **Amplitude:** Changes due to partial acoustic reflection at the boundary.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Frequency depends strictly on the vibrating source and remains unchanged across media boundaries.
- **B (Incorrect):** Speed changes dramatically from air to liquid.
- **C (Incorrect):** Wavelength expands in direct proportion to the velocity increase.
- **D (Incorrect):** Amplitude decreases due to partial reflection of acoustic energy."""
    }

    # Q61: MH-9-SCIT-12-12.1-OSC-061 (Fixed defect)
    enhancements[60] = {
        "text": "If two students are conversing inside an airtight room and all the air is suddenly evacuated using a powerful vacuum pump, what happens to the propagation of sound between them?",
        "options": [
            "Sound velocity increases because there is no air resistance",
            "Sound velocity remains unchanged at 344 m/s",
            "The sound becomes shriller with a higher pitch",
            "Sound propagation drops to zero because sound cannot travel in a vacuum"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Sound waves are mechanical vibrations of matter that transmit energy through alternating compressions and rarefactions of an elastic medium.

### 2. Wave Dynamics & Mathematical Derivation:
A mechanical wave requires material particles to exert restoring forces on adjacent particles:
\[
v = \sqrt{\frac{B}{\rho}}
\]
When all air molecules are evacuated from the room:
\[
\rho \rightarrow 0, \quad \text{Number of gas molecules } N \rightarrow 0
\]
Without a material medium, vocal cord vibrations cannot compress any particles. No pressure disturbance can be generated or transmitted across the intervening space. The velocity of sound effectively drops to zero:
\[
v_{\text{vacuum}} = 0\text{ m/s}
\]
The students will see each other's lips moving, but no sound whatsoever can be heard.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Eliminating air removes the medium itself; sound is not an object moving against resistance.
- **B (Incorrect):** Sound cannot travel at \(344\text{ m/s}\) without air molecules.
- **C (Incorrect):** Pitch requires sound waves to reach the ear, which is impossible in a vacuum.
- **D (Correct):** Sound propagation ceases completely because mechanical waves cannot travel through a vacuum."""
    }

    # Q62: MH-9-SCIT-12-12.1-OSC-062
    enhancements[61] = {
        "text": "An ultrasonic wave pulse is transmitted vertically downward from a ship toward the seabed. The time interval between transmission and reception of the reflected echo is 1.6 s. If the speed of sound in seawater is 1400 m/s, what is the depth of the sea?",
        "options": [
            "1120 m",
            "560 m",
            "1400 m",
            "2240 m"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
SONAR echo sounding measures underwater distances by timing the two-way transit of an acoustic wave reflected off the seabed.

### 2. Wave Dynamics & Mathematical Derivation:
Let \(d\) be the depth of the sea. The ultrasonic wave travels down to the seabed and returns to the ship, traversing a total path distance of \(2d\):
\[
2d = v \times t \implies d = \frac{v \times t}{2}
\]
Given:
- Speed of sound in seawater, \(v = 1400\text{ m/s}\)
- Round-trip echo time, \(t = 1.6\text{ s}\)

Substitute the values:
\[
2d = 1400 \times 1.6 = 2240\text{ m}
\]
\[
d = \frac{2240}{2} = 1120\text{ m}
\]
The sea is exactly \(1120\text{ m}\) deep at this location.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** \(d = \frac{1400 \times 1.6}{2} = 1120\text{ m}\).
- **B (Incorrect):** \(560\text{ m}\) results from dividing the correct answer by 2 again.
- **C (Incorrect):** \(1400\text{ m}\) is the speed of sound, not the depth.
- **D (Incorrect):** \(2240\text{ m}\) is the total two-way round-trip path length (\(2d\))."""
    }

    # Q63: MH-9-SCIT-12-12.1-OSC-063
    enhancements[62] = {
        "text": "Which of the following statements best provides the formal scientific definition of wave frequency?",
        "options": [
            "The maximum displacement of a particle from its mean equilibrium position",
            "The number of complete vibrations or wave cycles executed per unit time",
            "The linear distance between one wave crest and the immediately next crest",
            "The distance traveled by a wave front in one second"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Wave motion is characterized by three fundamental parameters: spatial period (wavelength), temporal period (time period), and temporal repetition rate (frequency).

### 2. Wave Dynamics & Mathematical Derivation:
- **Frequency (\(\nu\) or \(f\))** is formally defined as the number of complete oscillations, cycles, or vibrations completed per unit time (per second):
\[
\nu = \frac{N}{\Delta t} = \frac{1}{T}
\]
The SI unit of frequency is Hertz (\(\text{Hz}\)), where \(1\text{ Hz} = 1\text{ cycle per second}\) (\(\text{s}^{-1}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Maximum displacement from equilibrium defines the *amplitude (\(A\))*.
- **B (Correct):** The number of complete vibrations per second is the definition of *frequency (\(\nu\))*.
- **C (Incorrect):** Distance between consecutive crests defines the *wavelength (\(\lambda\))*.
- **D (Incorrect):** Distance traveled per second defines the *wave speed (\(v\))*."""
    }

    # Q64: MH-9-SCIT-12-12.1-OSC-064
    enhancements[63] = {
        "text": "Why can sound waves NOT be heard or transmitted across a perfect vacuum?",
        "options": [
            "Sound energy is immediately absorbed by dark matter",
            "A vacuum lacks material particles capable of vibrating and transmitting elastic restoring forces",
            "The intensity of sound attenuates due to lack of gravity",
            "Temperature in a vacuum is too low for sound waves to form"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Waves are classified into electromagnetic waves (which travel as self-sustaining field disturbances) and mechanical waves (which require the physical deformation and elastic recovery of a material medium).

### 2. Wave Dynamics & Mathematical Derivation:
Sound is a mechanical pressure wave. When a source vibrates, it initiates a series of collisions: particle 1 collides with particle 2, passing momentum and kinetic energy, which in turn collides with particle 3.
In a vacuum:
\[
\text{Particle Density } n = 0, \quad \text{Mass Density } \rho = 0
\]
Because there are zero atoms or molecules to collide, compress, or exert elastic restoring forces, mechanical waves cannot exist:
\[
v_{\text{sound}} = 0\text{ m/s}
\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Sound is not absorbed by dark matter; it simply cannot initiate without physical matter.
- **B (Correct):** Sound requires material particles to oscillate; a vacuum has no particles to transmit mechanical vibrations.
- **C (Incorrect):** Gravity plays no role in acoustic wave transmission.
- **D (Incorrect):** Medium presence—not temperature—is the prerequisite for mechanical wave propagation."""
    }

    # Q65: MH-9-SCIT-12-12.1-OSC-065
    enhancements[64] = {
        "text": "The measured velocities of sound in four media P, Q, R, and S are 1800 km/h, 900 km/h, 0 km/h, and 5400 km/h respectively. Which medium represents a liquid medium?",
        "options": [
            "Medium P (1800 km/h)",
            "Medium Q (900 km/h)",
            "Medium R (0 km/h)",
            "Medium S (5400 km/h)"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Comparing sound velocities across media requires converting values into standard SI units (\(\text{m/s}\)) and applying the acoustic ordering principle: \(v_{\text{vacuum}} = 0 < v_{\text{gas}} < v_{\text{liquid}} < v_{\text{solid}}\).

### 2. Wave Dynamics & Mathematical Derivation:
Convert each velocity from \(\text{km/h}\) to \(\text{m/s}\) using the conversion factor \(\frac{5}{18}\):
- **Medium R:** \(0\text{ km/h} = 0\text{ m/s}\) \(\rightarrow\) **Vacuum** (sound cannot propagate).
- **Medium Q:** \(900 \times \frac{5}{18} = 250\text{ m/s}\) \(\rightarrow\) **Gas at cold temperature** (e.g., air at high altitude).
- **Medium P:** \(1800 \times \frac{5}{18} = 500\text{ m/s}\) \(\rightarrow\) **Light gas** (e.g., hydrogen/helium).
- **Medium S:** \(5400 \times \frac{5}{18} = 1500\text{ m/s}\) \(\rightarrow\) **Liquid** (matches the speed of sound in water, \(\approx 1500\text{ m/s}\)).
Therefore, Medium S corresponds to a liquid medium.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Medium P has \(v = 500\text{ m/s}\), typical of hydrogen gas.
- **B (Incorrect):** Medium Q has \(v = 250\text{ m/s}\), typical of cold gases.
- **C (Incorrect):** Medium R has \(v = 0\text{ m/s}\), representing a vacuum.
- **D (Correct):** Medium S has \(v = 5400\text{ km/h} = 1500\text{ m/s}\), precisely matching liquid water."""
    }

    # Q66: MH-9-SCIT-12-12.1-OSC-066
    enhancements[65] = {
        "text": "A SONAR apparatus on a submarine emits an ultrasonic signal and detects its echo after 5.0 s. If the submerged obstacle is at a distance of 3625 m from the submarine, what is the speed of sound in the water?",
        "options": [
            "725 m/s",
            "362.5 m/s",
            "7250 m/s",
            "1450 m/s"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
SONAR operates via the reflection of sound pulses. The round-trip path traversed by the acoustic pulse is twice the one-way separation distance between the vessel and the target.

### 2. Wave Dynamics & Mathematical Derivation:
Let \(d\) be the distance to the obstacle, \(t\) be the echo time, and \(v\) be the speed of sound:
\[
2d = v \times t \implies v = \frac{2d}{t}
\]
Given:
- One-way distance, \(d = 3625\text{ m}\)
- Total round-trip distance, \(2d = 2 \times 3625 = 7250\text{ m}\)
- Time interval, \(t = 5.0\text{ s}\)

Substitute into the formula:
\[
v = \frac{7250\text{ m}}{5.0\text{ s}} = 1450\text{ m/s}
\]
The speed of sound in this body of water is \(1450\text{ m/s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(725\text{ m/s}\) is obtained by forgetting to double the distance (\(3625 / 5\)).
- **B (Incorrect):** \(362.5\text{ m/s}\) represents a decimal placement error.
- **C (Incorrect):** \(7250\text{ m}\) is the total distance traveled, not the velocity.
- **D (Correct):** \(v = \frac{2 \times 3625}{5} = 1450\text{ m/s}\)."""
    }

    # Q67: MH-9-SCIT-12-12.1-OSC-067
    enhancements[66] = {
        "text": "For a sound wave propagating with a constant velocity through a given medium, if its frequency is doubled, its wavelength:",
        "options": [
            "Becomes doubled",
            "Remains completely unchanged",
            "Becomes half of the original value",
            "Becomes four times greater"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Wave velocity in a homogeneous medium at constant temperature and pressure is a fixed physical property. When an acoustic source vibrates faster, it alters the spatial spacing of wave fronts.

### 2. Wave Dynamics & Mathematical Derivation:
The fundamental wave relation is:
\[
v = \nu \lambda \implies \lambda = \frac{v}{\nu}
\]
Because the medium is unchanged, the wave speed \(v\) is constant (\(v = \text{constant}\)).
Therefore, wavelength is inversely proportional to frequency:
\[
\lambda \propto \frac{1}{\nu}
\]
If the initial frequency \(\nu_1\) is doubled to \(\nu_2 = 2\nu_1\):
\[
\lambda_2 = \frac{v}{\nu_2} = \frac{v}{2\nu_1} = \frac{1}{2}\lambda_1
\]
The wavelength is halved. The wave crests are compressed twice as close together in space.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Doubling wavelength would require wave velocity to quadruple, violating medium constancy.
- **B (Incorrect):** Wavelength must adjust to maintain \(v = \nu \lambda\).
- **C (Correct):** At constant speed, wavelength is inversely proportional to frequency; doubling frequency halves the wavelength.
- **D (Incorrect):** Fourfold increase represents a false quadratic proportionality."""
    }

    # Q68: MH-9-SCIT-12-12.1-OSC-068
    enhancements[67] = {
        "text": "Among the following media, in which material will sound vibrations travel with the HIGHEST speed?",
        "options": [
            "Dry air",
            "Seawater",
            "Ground glass (Solid glass)",
            "Pure oxygen gas"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Sound velocity depends on the elastic modulus (\(E\)) and mass density (\(\rho\)) of the medium: \(v = \sqrt{E/\rho}\). In general, sound travels fastest in solids, intermediate in liquids, and slowest in gases.

### 2. Wave Dynamics & Mathematical Derivation:
Comparing sound velocities in the given media:
- **Dry air (gas):** \(v \approx 344\text{ m/s}\)
- **Pure oxygen (gas):** \(v \approx 316\text{ m/s}\) (heavier molar mass than air reduces velocity)
- **Seawater (liquid):** \(v \approx 1530\text{ m/s}\)
- **Ground glass (solid silicate glass):** \(v \approx 5000 - 5640\text{ m/s}\)

Solid glass possesses covalent/ionic tetrahedral silicate network bonding, imparting an exceptionally high Young's modulus of elasticity (\(Y \approx 70\text{ GPa}\)) relative to its moderate density (\(\rho \approx 2500\text{ kg/m}^3\)), resulting in a sound speed exceeding \(5000\text{ m/s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A, D (Incorrect):** Gases have very low elastic bulk moduli, yielding the slowest speeds (\(\sim 316 - 344\text{ m/s}\)).
- **B (Incorrect):** Seawater transmits sound at \(\sim 1530\text{ m/s}\), much slower than a solid.
- **C (Correct):** Solid glass transmits sound at over \(5000\text{ m/s}\) due to its high Young's modulus."""
    }

    # Q69: MH-9-SCIT-12-12.1-OSC-069
    enhancements[68] = {
        "text": "A musical bell produces a continuous acoustic tone within an audible frequency range, but cannot be heard by an observer standing nearby. The sound must be traveling through:",
        "options": [
            "Liquid water",
            "Solid wax",
            "A vacuum enclosure",
            "An empty open vessel"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Hearing sound requires three continuous elements: a vibrating source, a transmitting material medium, and an auditory receiver.

### 2. Wave Dynamics & Mathematical Derivation:
Mechanical waves require an elastic material medium containing mass and elasticity to propagate:
- Liquid water transmits sound effectively at \(v \approx 1500\text{ m/s}\).
- Solid wax conducts sound at \(v \approx 1500 - 2000\text{ m/s}\).
- An empty open vessel is filled with air, which transmits sound at \(v \approx 344\text{ m/s}\).
- In a **vacuum**, there are zero particles. Even though the source vibrates continuously, it cannot impart mechanical energy to adjacent space because there is no medium. Sound cannot travel through a vacuum:
\[
v_{\text{vacuum}} = 0\text{ m/s}
\]
Hence, the bell cannot be heard if isolated within a vacuum.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, D (Incorrect):** Water, wax, and air in an empty vessel are all material media that readily transmit sound waves to an observer.
- **C (Correct):** A vacuum completely blocks mechanical sound waves because it has no material medium."""
    }

    # Q70: MH-9-SCIT-12-12.1-OSC-070
    enhancements[69] = {
        "text": "What is the standard SI unit for the speed of sound?",
        "options": [
            "Decibels (dB)",
            "Hertz (Hz)",
            "Metres (m)",
            "Metres per second (m/s)"
        ],
        "correctAnswer": "D",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Speed is defined in classical kinematics as the rate of change of distance with respect to time.

### 2. Wave Dynamics & Mathematical Derivation:
Wave speed \(v\) is distance traversed (\(\Delta x\)) per unit time interval (\(\Delta t\)):
\[
v = \frac{\Delta x}{\Delta t} = \nu \lambda
\]
In SI base units:
- Distance / Wavelength \([\lambda]\) is measured in **metres (m)**.
- Time \([t]\) is measured in **seconds (s)**.
Therefore:
\[
[v] = \frac{\text{m}}{\text{s}} = \text{m/s} \quad (\text{or m}\cdot\text{s}^{-1})
\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Decibel (\(\text{dB}\)) is the logarithmic unit of sound intensity level.
- **B (Incorrect):** Hertz (\(\text{Hz}\)) is the unit of frequency.
- **C (Incorrect):** Metre (\(\text{m}\)) is the unit of distance and wavelength.
- **D (Correct):** Metres per second (\(\text{m/s}\)) is the SI unit for wave speed."""
    }

    # Q71: MH-9-SCIT-12-12.1-OSC-071
    enhancements[70] = {
        "text": "How do bats navigate and detect flying prey in total darkness without colliding with obstacles?",
        "options": [
            "By emitting and detecting reflected ultrasonic sound waves (Echolocation)",
            "By emitting faint pulses of visible bioluminescent light",
            "By sensing infrared laser beams emitted by obstacles",
            "By following radioactive magnetic field lines"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Bats are nocturnal mammals that rely on a biological bio-sonar system known as **echolocation** to map three-dimensional spatial environments in pitch darkness.

### 2. Wave Dynamics & Mathematical Derivation:
1. While flying, bats emit high-frequency ultrasonic squeaks through their mouth or nose, with frequencies typically ranging from \(20\text{ kHz}\) to over \(100\text{ kHz}\).
2. Because ultrasonic waves have exceptionally small wavelengths (\(\lambda = v/\nu \approx 344 / 50{,}000 \approx 7\text{ mm}\)), they reflect sharply off tiny flying insects and obstacles with minimal diffraction.
3. The bat's specialized ears receive the returning echo. By measuring:
   - The time delay \(\Delta t\) between emission and echo (\(d = \frac{v \Delta t}{2}\)), the bat computes obstacle distance.
   - The slight Doppler shift in frequency (\(\Delta \nu\)), the bat determines the prey's flight speed and direction.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Bats use echolocation via ultrasonic acoustic wave reflections.
- **B (Incorrect):** Bats do not produce bioluminescent light.
- **C, D (Incorrect):** Bats do not use laser beams or radioactivity; they use mechanical ultrasonic waves."""
    }

    # Q72: MH-9-SCIT-12-12.1-OSC-072
    enhancements[71] = {
        "text": "Among the following liquids at 25 °C, in which will the speed of sound be the HIGHEST?",
        "options": [
            "Distilled water",
            "Seawater",
            "Ethanol",
            "Methanol"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
In liquid media, the speed of sound is determined by the adiabatic bulk modulus of elasticity (\(B\)) and mass density (\(\rho\)): \(v = \sqrt{B/\rho}\).

### 2. Wave Dynamics & Mathematical Derivation:
Comparing sound velocities in liquids at \(25^\circ\text{C}\) (from Maharashtra State Board textbook data):
- **Methanol:** \(v \approx 1103\text{ m/s}\)
- **Ethanol:** \(v \approx 1207\text{ m/s}\)
- **Distilled water:** \(v \approx 1498\text{ m/s}\)
- **Seawater:** \(v \approx 1531\text{ m/s}\)

Seawater contains dissolved mineral salts (predominantly \(\text{NaCl}\), \(\text{MgCl}_2\), \(\approx 3.5\%\) salinity). The presence of dissolved ionic salts structures water molecules more tightly via electrostatic hydration shells, significantly increasing the bulk modulus \(B\) relative to density. As a result, sound travels faster in seawater (\(1531\text{ m/s}\)) than in pure distilled water (\(1498\text{ m/s}\)) or organic alcohols.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Distilled water has \(v \approx 1498\text{ m/s}\), slightly lower than seawater.
- **B (Correct):** Seawater has the highest sound speed (\(\approx 1531\text{ m/s}\)) due to dissolved salts increasing its elastic bulk modulus.
- **C, D (Incorrect):** Alcohols have weaker intermolecular hydrogen bonds and much lower bulk moduli, resulting in lower sound speeds (\(\sim 1100 - 1200\text{ m/s}\))."""
    }

    # Q73: MH-9-SCIT-12-12.1-OSC-073
    enhancements[72] = {
        "text": "In a longitudinal acoustic wave, compressions are localized regions of the medium where:",
        "options": [
            "Density and pressure are both at their minimum",
            "Density and pressure are both at their maximum",
            "Density is low while pressure is high",
            "Density is high while pressure is zero"
        ],
        "correctAnswer": "B",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Longitudinal waves propagate through alternating spatial fluctuations of particle concentration and pressure.

### 2. Wave Dynamics & Mathematical Derivation:
In a longitudinal sound wave:
- As the vibrating source moves forward, it pushes medium particles closer together. This crowding creates a region of increased particle concentration:
\[
\rho > \rho_0, \quad P > P_0
\]
This state of elevated density and elevated pressure is defined as a **compression** (or condensation).
- When the vibrating source pulls back, particles expand into the vacated space, creating a region of decreased concentration:
\[
\rho < \rho_0, \quad P < P_0
\]
This state of reduced density and reduced pressure is defined as a **rarefaction**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Low density and low pressure define *rarefactions*.
- **B (Correct):** Compressions are characterized by both maximum density and maximum pressure.
- **C, D (Incorrect):** According to the equation of state for elastic gases (\(\Delta P = B \frac{\Delta \rho}{\rho_0}\)), pressure and density changes are directly coupled in phase."""
    }

    # Q74: MH-9-SCIT-12-12.1-OSC-074
    enhancements[73] = {
        "text": "Sound waves traveling through air are physically classified as:",
        "options": [
            "Longitudinal mechanical waves",
            "Transverse mechanical waves",
            "Transverse electromagnetic waves",
            "Stationary thermal waves"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
The classification of waves depends on two physical criteria: whether they require a medium (mechanical vs. electromagnetic) and the relative orientation of particle oscillation to wave travel (longitudinal vs. transverse).

### 2. Wave Dynamics & Mathematical Derivation:
1. **Mechanical:** Sound requires an elastic material medium (air molecules) to transfer kinetic and potential energy through molecular collisions; it cannot propagate in a vacuum.
2. **Longitudinal:** Air has volume elasticity (bulk modulus) but lacks shear elasticity (rigidity). Therefore, medium particles oscillate back and forth parallel to the direction of energy propagation:
\[
\vec{v}_{\text{particle}} \parallel \vec{v}_{\text{wave}}
\]
Forming sequential compressions and rarefactions, sound waves in air are strictly **longitudinal mechanical waves**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Sound in air is a longitudinal mechanical wave.
- **B (Incorrect):** Transverse mechanical waves require shear rigidity, which gases do not possess.
- **C (Incorrect):** Electromagnetic waves (light, radio) consist of oscillating electric and magnetic fields, not air pressure fluctuations.
- **D (Incorrect):** Thermal waves describe non-oscillatory heat conduction."""
    }

    # Q75: MH-9-SCIT-12-12.1-OSC-075
    enhancements[74] = {
        "text": "The maximum displacement of an oscillating particle of the medium from its central equilibrium position is called its:",
        "options": [
            "Amplitude",
            "Wavelength",
            "Wave number",
            "Frequency"
        ],
        "correctAnswer": "A",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Simple harmonic motion and traveling waves are mathematically modeled by sinusoidal functions where displacement varies continuously between positive and negative extremes.

### 2. Wave Dynamics & Mathematical Derivation:
The particle displacement in a sinusoidal wave is expressed as:
\[
y(x,t) = A \sin(kx - \omega t + \phi)
\]
Because the sine function has a maximum magnitude of \(|\sin(\dots)| \le 1\):
\[
|y|_{\text{max}} = A
\]
This peak distance \(A\) from the central equilibrium line to either the crest or trough is defined as the **amplitude**. In acoustics, displacement amplitude directly determines wave energy and perceived loudness (\(I \propto A^2\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Amplitude is defined as the maximum displacement from the equilibrium position.
- **B (Incorrect):** Wavelength (\(\lambda\)) is the spatial length of one complete wave cycle.
- **C (Incorrect):** Wave number (\(k = 2\pi/\lambda\)) is the spatial frequency in radians per metre.
- **D (Incorrect):** Frequency (\(\nu\)) is the number of cycles executed per second."""
    }

    # Q76: MH-9-SCIT-12-12.1-OSC-076
    enhancements[75] = {
        "text": "A bat emits an ultrasonic squeak and detects its reflected echo from an obstacle after 0.10 s. If the speed of sound in air is 344 m/s, how far away is the obstacle from the bat?",
        "options": [
            "34.4 m",
            "170 m",
            "17.2 m",
            "180 m"
        ],
        "correctAnswer": "C",
        "solution": r"""### 1. Scientific Principle & Acoustic / Physical Context:
Echolocation in animals relies on the reflection of acoustic waves. The sound pulse travels to the reflective object and returns to the emitter over a total two-way round-trip path.

### 2. Wave Dynamics & Mathematical Derivation:
Let \(d\) be the distance from the bat to the obstacle.
The total distance traveled by the sound pulse is \(2d\):
\[
2d = v \times t \implies d = \frac{v \times t}{2}
\]
Given:
- Speed of sound in air, \(v = 344\text{ m/s}\)
- Echo round-trip time, \(t = 0.10\text{ s}\)

Substitute the values:
\[
2d = 344 \times 0.10 = 34.4\text{ m}
\]
\[
d = \frac{34.4}{2} = 17.2\text{ m}
\]
The obstacle is situated at a distance of \(17.2\text{ m}\).
(Note: \(17.2\text{ m}\) is also the standard minimum distance required for human ears to distinguish an echo in air at \(22^\circ\text{C}\), because the persistence of human hearing is \(\approx 0.1\text{ s}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(34.4\text{ m}\) is the total round-trip distance (\(2d\)); forgetting to divide by 2 is a classic error.
- **B, D (Incorrect):** Factually incorrect orders of magnitude.
- **C (Correct):** \(d = \frac{344 \times 0.10}{2} = 17.2\text{ m}\)."""
    }

    return enhancements

if __name__ == '__main__':
    data = get_part2_enhancements()
    print(f"Generated {len(data)} enhancements for Part 2 (Q39 to Q76).")
