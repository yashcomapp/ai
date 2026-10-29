"""
build_ch12_part1.py: Generates enhanced Q1 to Q38 for Chapter 12 (Study of Sound).
"""

import json

def get_part1_enhancements():
    # Return dictionary keyed by question index (0 to 37)
    enhancements = {}

    # Q1: MH-9-SCIT-12-12.1-OSC-001
    enhancements[0] = {
        "text": "Through which of the following media can transverse mechanical waves propagate?",
        "options": [
            "Solids",
            "Gases only",
            "Liquids only",
            "Any fluid or vacuum"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Transverse mechanical waves are waves in which the particles of the medium vibrate perpendicular to the direction of wave propagation, forming alternating crests and troughs. Propagation of transverse waves requires the medium to possess shear elasticity (rigidity) so that a restoring force can act when layers of the medium are displaced sideways relative to each other.

### 2. Wave Dynamics & Mathematical Derivation:
The velocity of a transverse mechanical wave in an elastic solid medium depends on the shear modulus of rigidity (\(\\eta\)) and mass density (\(\\rho\)):
\\[
v_{\\text{transverse}} = \\sqrt{\\frac{\\eta}{\\rho}}
\\]
Fluids (liquids and gases) have zero shear rigidity (\(\\eta = 0\)) in their bulk volume; they can sustain volume compression (bulk modulus) but cannot support shearing strain. Therefore, mechanical transverse waves can propagate exclusively through **solids** (and as surface tension capillary waves on the surface of liquids), but never through bulk fluids or gases.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Solids possess significant shear rigidity (\(\\eta > 0\)), allowing transverse vibrations to generate restoring forces that propagate crests and troughs.
- **B (Incorrect):** Gases lack shear rigidity entirely (\(\\eta = 0\)); particles cannot exert sideways restoring forces, so only longitudinal compressions and rarefactions can propagate.
- **C (Incorrect):** Liquids lack volume shear rigidity; bulk transverse waves cannot travel through liquid interiors.
- **D (Incorrect):** Mechanical waves cannot propagate in a vacuum because they require material particles to transmit elastic strain energy."""
    }

    # Q2: MH-9-SCIT-12-12.1-OSC-002
    enhancements[1] = {
        "text": "When a sound wave travels through air, the air particles:",
        "options": [
            "Vibrate parallel to the direction of wave propagation",
            "Vibrate perpendicular to the direction of wave propagation",
            "Move permanently from the source to the listener",
            "Remain completely stationary without any oscillation"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Sound in a gaseous medium like air propagates strictly as a longitudinal mechanical wave. When a vibrating source (such as a tuning fork or vocal cord) pushes forward, it compresses adjacent air particles into a region of high density and pressure (compression). When it retracts, air expands into a region of low density and pressure (rarefaction).

### 2. Wave Dynamics & Mathematical Derivation:
In a longitudinal wave, the displacement vector of medium particles \(\\vec{s}(x,t)\) is collinear with the wave propagation velocity vector \(\\vec{v}\):
\\[
s(x,t) = s_0 \\sin(kx - \\omega t)
\\]
Particles oscillate back and forth about their mean equilibrium positions parallel to the wave vector \(\\vec{k}\). There is zero net transport of mass; only acoustic energy and momentum are transferred through sequential molecular collisions.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Air particles execute simple harmonic oscillations parallel (along) the line of sound propagation, creating alternating compressions and rarefactions.
- **B (Incorrect):** Perpendicular oscillations characterize transverse waves (e.g., waves along a plucked guitar string or light waves), not sound waves in air.
- **C (Incorrect):** Particles do not travel across space with the wave; they oscillate locally around stationary equilibrium positions.
- **D (Incorrect):** Particles must vibrate to transfer acoustic energy via elastic collisions; static particles cannot transmit sound."""
    }

    # Q3: MH-9-SCIT-12-12.1-OSC-003
    enhancements[2] = {
        "text": "When a sound wave travels through a material medium:",
        "options": [
            "Medium particles are permanently transported from one location to another",
            "Energy is transferred at a constant speed characteristic of the medium",
            "Energy is transferred with continuously accelerating speed",
            "Particles travel along with the wave at the speed of sound"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
A mechanical wave is a self-sustaining disturbance that transports energy and momentum through a material medium without causing any permanent displacement or bulk transport of matter.

### 2. Wave Dynamics & Mathematical Derivation:
In a uniform, isotropic medium under constant ambient conditions (temperature, pressure, and density), the acoustic wave speed \(v\) is a constant physical property:
\\[
v = \\nu \\lambda = \\sqrt{\\frac{B}{\\rho}}
\\]
where \(B\) is the bulk modulus and \(\\rho\) is the mass density. Acoustic energy flows continuously through the medium at this constant propagation velocity \(v\), while individual medium molecules merely execute microscopic oscillations with zero net drift velocity (\(\\langle \\vec{v}_{\\text{particle}} \\rangle = 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Mass is not transported across macroscopic distances during wave propagation; only acoustic energy moves forward.
- **B (Correct):** Energy is transferred at a constant speed determined exclusively by the elastic and inertial properties of the medium.
- **C (Incorrect):** The wave does not accelerate in a homogeneous medium; speed remains strictly constant unless ambient physical properties (like temperature or density) change.
- **D (Incorrect):** Particles execute local periodic oscillations with maximum particle velocity \(v_{\\text{max}} = \\omega A\), which is completely decoupled from the wave speed \(v\)."""
    }

    # Q4: MH-9-SCIT-12-12.1-OSC-004
    enhancements[3] = {
        "text": "The technique of detecting the presence, position, and depth of submerged distant objects using reflected sound waves is known as:",
        "options": [
            "RADAR",
            "SONAR",
            "MRI",
            "CRO"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
SONAR stands for **SO**und **N**avigation **A**nd **R**anging. It is an acoustic technique that exploits the reflection of high-frequency ultrasonic waves underwater to detect obstacles, map the seabed, or locate underwater vessels and shoals of fish.

### 2. Wave Dynamics & Mathematical Derivation:
A SONAR apparatus consists of an ultrasonic transmitter and an acoustic detector installed on the bottom of a ship. The transmitter emits high-frequency ultrasonic pulses that travel through seawater at speed \(v\), reflect off a submerged object, and return to the receiver after a total two-way transit time \(t\):
\\[
2d = v \\times t \\implies d = \\frac{v \\times t}{2}
\\]
where \(d\) is the one-way distance (depth) to the submerged target.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** RADAR (Radio Detection and Ranging) utilizes high-frequency electromagnetic radio/microwaves in the atmosphere, which are rapidly attenuated in water.
- **B (Correct):** SONAR utilizes reflected ultrasound waves in water to measure underwater distances, velocities, and topographical depth.
- **C (Incorrect):** MRI (Magnetic Resonance Imaging) is a medical diagnostic tool utilizing strong magnetic fields and radiofrequency pulses to image internal organs.
- **D (Incorrect):** CRO (Cathode Ray Oscilloscope) is an electronic laboratory instrument used to display and analyze electrical waveforms."""
    }

    # Q5: MH-9-SCIT-12-12.1-OSC-005
    enhancements[4] = {
        "text": "If the tension (stretching force) on a guitar wire is increased, the fundamental frequency of the sound produced:",
        "options": [
            "Increases",
            "Decreases",
            "Remains unchanged",
            "First decreases and then drops to zero"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
When a stretched string or guitar wire is plucked, standing transverse waves are established with nodes at the fixed endpoints. The frequency of vibration dictates the musical pitch heard by the human ear.

### 2. Wave Dynamics & Mathematical Derivation:
According to Mersenne's laws for vibrating strings, the fundamental frequency \(\\nu\) of a stretched wire of length \(L\), linear mass density \(m\), and tension \(T\) is given by:
\\[
\\nu = \\frac{1}{2L} \\sqrt{\\frac{T}{m}}
\\]
This directly establishes that frequency is proportional to the square root of tension:
\\[
\\nu \\propto \\sqrt{T}
\\]
Increasing the tension \(T\) by tightening the tuning peg increases the transverse wave velocity on the wire (\(v = \\sqrt{T/m}\)), directly increasing the vibration frequency \(\\nu\), producing a higher-pitched sound.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** As stretching force (tension \(T\)) increases, the restoring force accelerates string particles faster, directly increasing frequency (\(\\nu \\propto \\sqrt{T}\)).
- **B (Incorrect):** Frequency decreases only if tension is loosened or string length/thickness is increased.
- **C (Incorrect):** Frequency is directly dependent on string tension; it cannot remain unchanged when tuning pegs are turned.
- **D (Incorrect):** The relationship is strictly monotonic increasing; frequency never drops to zero under positive tension."""
    }

    # Q6: MH-9-SCIT-12-12.1-OSC-006
    enhancements[5] = {
        "text": "Among the following physical properties of a traveling wave, which property is independent of the others?",
        "options": [
            "Frequency",
            "Wavelength",
            "Wave speed",
            "Amplitude"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
In wave physics, kinematic wave properties are divided into those governed by source vibration, those determined by the medium, and those representing wave energy.

### 2. Wave Dynamics & Mathematical Derivation:
The wave equation links speed (\(v\)), frequency (\(\\nu\)), and wavelength (\(\\lambda\)):
\\[
v = \\nu \\lambda
\\]
Here, frequency \(\\nu\) is fixed by the source, speed \(v\) is governed strictly by the elastic and inertial properties of the medium, and wavelength \(\\lambda = v/\\nu\) is mutually dependent on both.
In contrast, **amplitude (\(A\))** represents the maximum displacement of particles from equilibrium and is governed solely by the mechanical energy supplied by the source:
\\[
E \\propto A^2, \\quad I = 2\\pi^2 \\rho v \\nu^2 A^2
\\]
Amplitude can be varied arbitrarily (by plucking harder or softer) without altering the wave speed \(v\), wavelength \(\\lambda\), or frequency \(\\nu\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, C (Incorrect):** Frequency, wavelength, and speed are interdependent through the fundamental wave relation \(v = \\nu \\lambda\). Modifying medium alters \(\\lambda\) for a given \(\\nu\).
- **D (Correct):** Amplitude depends strictly on the energy imparted to the wave and is independent of wave speed, frequency, and wavelength in linear acoustic systems."""
    }

    # Q7: MH-9-SCIT-12-12.1-OSC-007
    enhancements[6] = {
        "text": "The amplitude of a sound wave primarily determines its:",
        "options": [
            "Loudness",
            "Pitch",
            "Speed",
            "Quality or Timbre"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Loudness is the physiological sensation by which the ear distinguishes between faint and loud sounds. The physical quantity underlying loudness is the acoustic intensity, which depends directly on the amplitude of vibration.

### 2. Wave Dynamics & Mathematical Derivation:
The acoustic intensity \(I\) of a sound wave is proportional to the square of its amplitude \(A\):
\\[
I \\propto A^2
\\]
When the vibrating body oscillates with a larger amplitude, it strikes air particles with greater force, producing larger pressure fluctuations (\(\\Delta P_{\\text{max}} = \\rho v \\omega A\)). According to Weber-Fechner's law, loudness \(L\) is proportional to the logarithm of sound intensity:
\\[
L \\propto \\log_{10}\\left(\\frac{I}{I_0}\\right)
\\]
Thus, doubling the vibration amplitude quadruples the acoustic intensity, resulting in a noticeably louder sound.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Amplitude directly governs sound intensity (\(I \\propto A^2\)), which determines perceived loudness.
- **B (Incorrect):** Pitch is governed by the frequency (\(\\nu\)) of the wave, not its amplitude.
- **C (Incorrect):** Wave speed is determined by the properties of the transmitting medium (density and elasticity).
- **D (Incorrect):** Quality or timbre is determined by the waveform and the presence of harmonic overtones."""
    }

    # Q8: MH-9-SCIT-12-12.1-OSC-008
    enhancements[7] = {
        "text": "Which of the following physical quantities is transported across the medium during wave propagation?",
        "options": [
            "Mass of medium particles",
            "Matter",
            "Gravitational charge",
            "Energy and Momentum"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Wave motion is a mechanism of energy transfer across space without the physical transport of matter. A wave originates when an external disturbance transfers energy to the particles of an elastic medium.

### 2. Wave Dynamics & Mathematical Derivation:
As the wave propagates through an elastic medium, each particle executes simple harmonic oscillation about its mean position, transferring kinetic energy (\(E_k = \\frac{1}{2} m v^2\)) and elastic potential energy (\(E_p = \\frac{1}{2} k x^2\)) to adjacent particles via intermolecular forces:
\\[
\\text{Net Mass Transport: } \\Delta M = \\int_{t_1}^{t_2} \\vec{v}_{\\text{particle}} \\, dt = 0
\\]
\\[
\\text{Energy Transport Rate: } P = \\frac{dE}{dt} = \\frac{1}{2} \\rho v \\omega^2 A^2 S
\\]
Energy and momentum travel forward with wave velocity \(v\), while the medium as a whole undergoes zero net displacement.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B (Incorrect):** Medium particles merely oscillate locally around their equilibrium coordinates; they do not travel with the wave.
- **C (Incorrect):** Gravitational charge (mass) is not transported through acoustic waves.
- **D (Correct):** Waves are defined physically by the progressive transmission of energy and momentum through space."""
    }

    # Q9: MH-9-SCIT-12-12.1-OSC-009
    enhancements[8] = {
        "text": "When the wire of a sitar is plucked, what type of waves are generated within the wire itself?",
        "options": [
            "Longitudinal mechanical waves",
            "Transverse mechanical waves",
            "Electromagnetic waves",
            "Stationary torsional waves"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
When a musical string (such as in a sitar, guitar, or violin) is pulled sideways and released, its particles oscillate perpendicular to the string's length, setting up standing waves between the fixed ends.

### 2. Wave Dynamics & Mathematical Derivation:
The displacement of the wire particles \(\\vec{y}(x,t)\) is perpendicular to the string axis (\(x\)-axis), which is the direction along which the disturbance travels:
\\[
\\vec{y} \\perp \\vec{v}_{\\text{wave}}
\\]
Therefore, the waves inside the wire are **transverse mechanical waves** with alternating crests and troughs. (Note: These vibrating strings subsequently push and pull on ambient air molecules, generating **longitudinal** sound waves in the surrounding air).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Longitudinal waves in the wire would require particles to oscillate along the string length; plucking pulls the string sideways.
- **B (Correct):** The plucked string particles vibrate perpendicular to the wire length, forming transverse standing waves.
- **C (Incorrect):** Mechanical vibrating wires generate elastic mechanical waves, not electromagnetic waves (like radio or light).
- **D (Incorrect):** Torsional waves involve twisting vibrations around the axis, not lateral transverse plucking."""
    }

    # Q10: MH-9-SCIT-12-12.1-OSC-010
    enhancements[9] = {
        "text": "Which of the following statements is INCORRECT regarding the propagation of sound waves in air?",
        "options": [
            "Sound waves travel through different parts of the medium via elastic interactions",
            "Sound waves travel with a constant velocity in a homogeneous medium at uniform temperature",
            "Vibrating air particles travel forward across space along with the sound wave",
            "Particles of the medium simply vibrate about their mean equilibrium positions"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Sound propagation in air occurs by pressure waves that alternately compress and expand air layers. Understanding the distinction between wave velocity and particle oscillation velocity is central to wave mechanics.

### 2. Wave Dynamics & Mathematical Derivation:
When sound travels through air:
- The disturbance moves forward at wave velocity \(v = \\sqrt{\\frac{\\gamma P}{\\rho}}\) (\(\\approx 344\\text{ m/s}\) at \(22^\\circ\\text{C}\)).
- Air molecules do **not** travel with this speed. They execute simple harmonic motion about stationary equilibrium points:
\\[
x(t) = x_0 + A \\sin(\\omega t)
\\]
The mean net displacement of any air particle over complete cycles is strictly zero:
\\[
\\Delta x_{\\text{net}} = 0
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (True statement / Incorrect choice):** Sound transmits through sequential molecular collisions in an elastic medium.
- **B (True statement / Incorrect choice):** In a uniform isotropic medium at constant temperature, wave speed remains strictly constant.
- **C (Correct / False statement):** Air particles do NOT travel with the sound wave across space; believing that air particles travel from speaker to listener is a major student misconception.
- **D (True statement / Incorrect choice):** Medium particles undergo simple harmonic oscillation about their mean coordinates."""
    }

    # Q11: MH-9-SCIT-12-12.1-OSC-011
    enhancements[10] = {
        "text": "A stone is dropped into a calm pond, producing circular ripples. A leaf floating on the water surface bobs up and down without moving outward. This occurs because the ripples are:",
        "options": [
            "Purely longitudinal waves",
            "Gravitational body waves",
            "Transverse surface waves",
            "Electromagnetic radiation"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Disturbances created on a water surface produce ripples (ripples/waves) that travel radially outward from the point of impact. Floating objects act as markers that trace the motion of the water particles beneath them.

### 2. Wave Dynamics & Mathematical Derivation:
In transverse surface waves, the water particles oscillate vertically (up and down) about their mean equilibrium positions, while the wave disturbance moves horizontally across the surface:
\\[
\\vec{v}_{\\text{particle}} \\perp \\vec{v}_{\\text{wave}}
\\]
As crests and troughs pass beneath the floating leaf, it is lifted to the crest and drops into the trough, experiencing zero net horizontal displacement. This demonstrates that mechanical waves transfer energy across the surface while the medium itself merely oscillates locally.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Longitudinal waves involve oscillations parallel to wave propagation (back-and-forth horizontally), which would push the leaf laterally.
- **B (Incorrect):** Gravitational body waves are astronomical spacetime perturbations, not water surface ripples.
- **C (Correct):** The leaf bobs up and down perpendicular to the outward horizontal wave propagation, confirming transverse surface wave motion.
- **D (Incorrect):** Water ripples are mechanical elastic/surface-tension waves, not electromagnetic radiation."""
    }

    # Q12: MH-9-SCIT-12-12.1-OSC-012
    enhancements[11] = {
        "text": "Why is the velocity of sound in moist (humid) air greater than in dry air at the same temperature and pressure?",
        "options": [
            "The density of moist air is less than that of dry air",
            "The temperature of moist air is naturally higher than that of dry air",
            "Atmospheric pressure increases substantially in the presence of water vapor",
            "The frequency of the sound wave increases in humid conditions"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
According to Laplace's formula, the speed of sound in a gaseous medium depends on the ratio of heat capacities (\(\\gamma\)), atmospheric pressure (\(P\)), and gas density (\(\\rho\)).

### 2. Wave Dynamics & Mathematical Derivation:
The velocity of sound in a gas is given by:
\\[
v = \\sqrt{\\frac{\\gamma P}{\\rho}} \\implies v \\propto \\frac{1}{\\sqrt{\\rho}}
\\]
Water vapor has a molar mass of \(M_{\\text{H}_2\\text{O}} \\approx 18\\text{ g/mol}\), whereas dry air consists predominantly of nitrogen (\(N_2\), \(28\\text{ g/mol}\)) and oxygen (\(O_2\), \(32\\text{ g/mol}\)), giving an effective average molar mass of \(M_{\\text{dry}} \\approx 28.8\\text{ g/mol}\).
When dry air becomes moist, lighter water vapor molecules displace heavier nitrogen and oxygen molecules at equal temperature and pressure. Consequently:
\\[
\\rho_{\\text{moist}} < \\rho_{\\text{dry}} \\implies v_{\\text{moist}} > v_{\\text{dry}}
\\]
Since sound velocity is inversely proportional to the square root of gas density, sound travels faster through less dense moist air.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Moist air is less dense than dry air due to the lower molecular mass of \(\\text{H}_2\\text{O}\) compared to \(N_2\) and \(O_2\); lower density directly increases sound speed (\(v \\propto 1/\\sqrt{\\rho}\)).
- **B (Incorrect):** The comparison is defined at identical temperatures; temperature difference is not the cause.
- **C (Incorrect):** Ambient total atmospheric pressure remains constant; partial pressures shift according to Dalton's law.
- **D (Incorrect):** Wave frequency is governed exclusively by the vibrating source and does not change with humidity."""
    }

    # Q13: MH-9-SCIT-12-12.1-OSC-013
    enhancements[12] = {
        "text": "Which of the following is an example of a mechanical wave?",
        "options": [
            "Radio wave",
            "Light wave",
            "Infrared radiation",
            "Sound wave"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Waves are broadly classified into mechanical waves and electromagnetic waves based on whether they require a physical material medium for propagation.

### 2. Wave Dynamics & Mathematical Derivation:
- **Mechanical waves** require an elastic material medium (solid, liquid, or gas) containing mass and restoring elasticity to transmit vibrational energy:
\\[
v = \\sqrt{\\frac{\\text{Elastic Property}}{\\text{Inertial Property}}}
\\]
Sound waves propagate via mechanical oscillations of atoms/molecules and cannot travel through a vacuum (\(v_{\\text{vacuum}} = 0\)).
- **Electromagnetic waves** consist of oscillating, mutually perpendicular electric (\(\\vec{E}\)) and magnetic (\(\\vec{B}\)) fields and propagate freely through vacuum at speed \(c \\approx 3 \\times 10^8\\text{ m/s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, C (Incorrect):** Radio waves, visible light, and infrared radiation are non-mechanical electromagnetic waves capable of traversing empty space.
- **D (Correct):** Sound waves require an elastic material medium (air, water, steel) to propagate compressions and rarefactions, making them mechanical waves."""
    }

    # Q14: MH-9-SCIT-12-12.1-OSC-014
    enhancements[13] = {
        "text": "Crests and troughs are characteristic structural features formed in:",
        "options": [
            "Longitudinal waves only",
            "Transverse waves",
            "Both longitudinal and transverse waves identically",
            "Stationary pressure waves only"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Mechanical waves create distinct geometrical profile patterns based on whether particle displacements are parallel or perpendicular to the direction of wave travel.

### 2. Wave Dynamics & Mathematical Derivation:
- In a **transverse wave**, particles oscillate perpendicular to the axis of wave propagation. The point of maximum positive displacement above the mean equilibrium position is termed a **crest**, while the point of maximum negative displacement below the mean position is termed a **trough**.
- In contrast, a **longitudinal wave** (such as sound in air) consists of alternating regions of increased particle density and pressure called **compressions**, and regions of decreased density and pressure called **rarefactions**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Longitudinal waves form compressions and rarefactions, not crests and troughs.
- **B (Correct):** Transverse waves are structurally defined by alternating elevations (crests) and depressions (troughs).
- **C (Incorrect):** The two wave types have distinct physical profiles; longitudinal waves cannot form physical crests and troughs.
- **D (Incorrect):** Stationary pressure waves in gas columns form pressure nodes and antinodes."""
    }

    # Q15: MH-9-SCIT-12-12.1-OSC-015
    enhancements[14] = {
        "text": "Match the musical instrument vibration source correctly:\\n(A) String vibration - (I) Tabla\\n(B) Membrane vibration - (II) Bicycle bell\\n(C) Air column vibration - (III) Sitar\\n(D) Plate/Metal vibration - (IV) Flute",
        "options": [
            "A-(I), B-(II), C-(III), D-(IV)",
            "A-(II), B-(I), C-(IV), D-(III)",
            "A-(III), B-(I), C-(IV), D-(II)",
            "A-(IV), B-(III), C-(II), D-(I)"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Musical instruments produce sound through the vibration of specific physical components, classified into chordophones (strings), membranophones (stretched membranes), aerophones (air columns), and idiophones (solid resonant plates/bells).

### 2. Wave Dynamics & Mathematical Derivation:
Analyzing each category:
1. **String Vibration (A):** Sitar uses taut metal strings plucked to generate transverse standing waves \(\\rightarrow\) **(III)**.
2. **Membrane Vibration (B):** Tabla uses a stretched leather membrane struck by hands to set up 2D vibrational modes \(\\rightarrow\) **(I)**.
3. **Air Column Vibration (C):** Flute uses an open/closed cylindrical column of air vibrating in longitudinal standing acoustic modes \(\\rightarrow\) **(IV)**.
4. **Plate / Metal Body Vibration (D):** Bicycle bell uses a metallic cup/disc struck by a clapper to produce surface vibrations \(\\rightarrow\) **(II)**.
Thus, the correct matching is **A-(III), B-(I), C-(IV), D-(II)**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Inaccurately pairs sitar with air vibration and tabla with string vibration.
- **B (Incorrect):** Fails to match the sitar to string vibration.
- **C (Correct):** Accurately correlates A-(III) Sitar, B-(I) Tabla, C-(IV) Flute, and D-(II) Bicycle bell.
- **D (Incorrect):** Reverses the essential acoustic classifications."""
    }

    # Q16: MH-9-SCIT-12-12.1-OSC-016
    enhancements[15] = {
        "text": "The frequency of a sound source is 20 kHz. When the sound waves produced by it pass from air into water, their frequency will be:",
        "options": [
            "Exactly 20 kHz (same as the source)",
            "Significantly higher than 20 kHz",
            "Significantly lower than 20 kHz",
            "Directly proportional to the ratio of sound velocities"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
When a mechanical or electromagnetic wave crosses an interface between two different media (refraction), some wave parameters change while others remain invariant.

### 2. Wave Dynamics & Mathematical Derivation:
Frequency (\(\\nu\)) represents the number of complete oscillations or wave cycles emitted per second. It is determined **strictly by the vibrating source** (such as a piezoelectric crystal or tuning fork):
\\[
\\nu_{\\text{water}} = \\nu_{\\text{air}} = \\nu_{\\text{source}} = 20\\text{ kHz}
\\]
When sound enters water from air, its speed increases markedly from \(v_{\\text{air}} \\approx 344\\text{ m/s}\) to \(v_{\\text{water}} \\approx 1500\\text{ m/s}\). Because the relation \(v = \\nu \\lambda\) must hold in both media:
\\[
\\lambda_{\\text{water}} = \\frac{v_{\\text{water}}}{\\nu} > \\lambda_{\\text{air}}
\\]
Wavelength increases by the same factor as velocity, keeping frequency \(\\nu\) strictly unchanged.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Frequency is an intrinsic property of the emitting source; it remains invariant across boundary transitions.
- **B, C (Incorrect):** Frequency does not increase or decrease when crossing media interfaces.
- **D (Incorrect):** Wavelength—not frequency—is directly proportional to the sound velocity in the medium."""
    }

    # Q17: MH-9-SCIT-12-12.1-OSC-017
    enhancements[16] = {
        "text": "The time period of an oscillating simple pendulum is 0.2 s. What is its frequency of oscillation?",
        "options": [
            "0.5 Hz",
            "5 Hz",
            "50 Hz",
            "1 Hz"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
The time period (\(T\)) is the duration required for one complete oscillation. Frequency (\(\\nu\) or \(f\)) is defined as the number of complete oscillations executed per unit time (per second).

### 2. Wave Dynamics & Mathematical Derivation:
Frequency and time period are inversely related by the fundamental formula:
\\[
\\nu = \\frac{1}{T}
\\]
Given:
\\[
T = 0.2\\text{ s} = \\frac{2}{10}\\text{ s} = \\frac{1}{5}\\text{ s}
\\]
Substituting into the formula:
\\[
\\nu = \\frac{1}{0.2} = \\frac{10}{2} = 5\\text{ Hz}
\\]
The pendulum completes 5 full back-and-forth oscillations every second.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(0.5\\text{ Hz}\) corresponds to a time period of \(T = 1/0.5 = 2.0\\text{ s}\).
- **B (Correct):** \(\\nu = 1/0.2 = 5\\text{ Hz}\), exactly 5 cycles per second.
- **C (Incorrect):** \(50\\text{ Hz}\) corresponds to \(T = 0.02\\text{ s}\), a tenfold error.
- **D (Incorrect):** \(1\\text{ Hz}\) corresponds to a period of \(T = 1.0\\text{ s}\)."""
    }

    # Q18: MH-9-SCIT-12-12.1-OSC-018 (Sanitized endocrine gland defect)
    enhancements[17] = {
        "text": "Which of the following is NOT an endocrine gland in the human body?",
        "options": [
            "Pituitary gland",
            "Thyroid gland",
            "Adrenal gland",
            "Salivary gland"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
In human biology, glands are categorized into endocrine glands (ductless glands that secrete hormones directly into the bloodstream) and exocrine glands (glands possessing ducts that discharge their secretions onto epithelial surfaces or body cavities).

### 2. Wave Dynamics & Mathematical Derivation:
- **Pituitary gland, Thyroid gland, and Adrenal gland** are classical endocrine glands. They produce chemical messengers (such as growth hormone, thyroxine, and adrenaline) released directly into blood capillaries without ducts.
- **Salivary glands** (parotid, submandibular, and sublingual) possess dedicated salivary ducts (such as Stensen's duct and Wharton's duct) that secrete saliva and digestive enzymes (salivary amylase) into the oral cavity. Hence, they are **exocrine glands**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Pituitary is the master endocrine gland situated at the base of the brain.
- **B (Incorrect):** Thyroid is an endocrine gland located in the neck secreting thyroxine.
- **C (Incorrect):** Adrenal glands are endocrine glands located atop the kidneys secreting adrenaline and corticosteroids.
- **D (Correct):** Salivary glands secrete through ducts into the mouth, making them exocrine (duct) glands, NOT endocrine glands."""
    }

    # Q19: MH-9-SCIT-12-12.1-OSC-019
    enhancements[18] = {
        "text": "In a transverse wave, a crest represents the point of:",
        "options": [
            "Zero displacement from the mean equilibrium position",
            "Maximum positive displacement above the mean equilibrium position",
            "Minimum pressure and density in the medium",
            "Maximum particle velocity in the downward direction"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
A transverse wave is geometrically mapped as an undulating sine or cosine curve representing the displacement of medium particles as a function of position and time.

### 2. Wave Dynamics & Mathematical Derivation:
The displacement of a particle in a transverse sinusoidal wave is given by:
\\[
y(x,t) = A \\sin(kx - \\omega t)
\\]
- A **crest** is formed where displacement reaches its maximum positive peak value:
\\[
y_{\\text{crest}} = +A
\\]
- At this peak, the instantaneous particle velocity momentarily drops to zero (\(v_y = dy/dt = 0\)) as particles reverse direction.
- A **trough** corresponds to the maximum negative excursion: \(y_{\\text{trough}} = -A\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Zero displacement points are nodes or zero-crossings, not crests.
- **B (Correct):** A crest is defined as the point of maximum upward (positive) displacement (\(+A\)) above the baseline.
- **C (Incorrect):** Pressure and density fluctuations describe longitudinal waves (rarefactions), not transverse crests.
- **D (Incorrect):** At the crest peak, instantaneous particle velocity is zero before downward motion begins."""
    }

    # Q20: MH-9-SCIT-12-12.1-OSC-020
    enhancements[19] = {
        "text": "When a sitar wire is plucked, what is the nature of the wave traveling along the wire?",
        "options": [
            "Longitudinal mechanical wave",
            "Transverse mechanical wave",
            "Electromagnetic radio wave",
            "Non-mechanical wave"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
When a musical instrument's taut string is pulled laterally and released, elastic restoring tension forces pull the displaced segments back toward equilibrium, initiating wave motion along the string.

### 2. Wave Dynamics & Mathematical Derivation:
Since the string displacement is perpendicular to the string length along which the disturbance propagates:
\\[
\\vec{y} \\perp \\vec{x}
\\]
the waves propagating along the wire are **transverse mechanical waves**. The speed of these transverse waves depends on string tension \(T\) and linear mass density \(m\):
\\[
v = \\sqrt{\\frac{T}{m}}
\\]
Reflections at both clamped endpoints establish stationary transverse standing waves with fixed nodes at the ends and antinodes in between.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Longitudinal waves have particle oscillations parallel to wave travel; plucking vibrates the wire laterally.
- **B (Correct):** Displaced segments move perpendicular to the wire length, forming transverse mechanical waves.
- **C, D (Incorrect):** String vibrations are mechanical elastic waves requiring mass and tension, not electromagnetic fields."""
    }

    # Q21: MH-9-SCIT-12-12.1-OSC-021
    enhancements[20] = {
        "text": "If a periodic wave of time period \\(T\\) travels through a medium with velocity \\(V\\), its wavelength \\(\\lambda\\) is given by:",
        "options": [
            "\\(\\lambda = \\frac{V}{T}\\)",
            "\\(\\lambda = V \\times T\\)",
            "\\(\\lambda = \\frac{1}{V \\times T}\\)",
            "\\(\\lambda = \\frac{T}{V}\\)"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Wavelength (\(\\lambda\)) is the spatial distance traversed by a wave during the time interval in which a medium particle completes one full cycle of oscillation (the time period \(T\)).

### 2. Wave Dynamics & Mathematical Derivation:
By definition, wave velocity \(V\) is distance traveled per unit time:
\\[
V = \\frac{\\text{Distance}}{\\text{Time}} = \\frac{\\lambda}{T}
\\]
Multiplying both sides by the time period \(T\):
\\[
\\lambda = V \\times T
\\]
Alternatively, since frequency \(\\nu = 1/T\), substituting \(\\nu\) yields the familiar wave equation:
\\[
V = \\nu \\lambda \\implies \\lambda = \\frac{V}{\\nu} = V \\times T
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(\\frac{V}{T}\) has dimensional units of acceleration (\(\\text{m/s}^2\)), not wavelength (\(\\text{m}\)).
- **B (Correct):** \(\\lambda = V \\times T\), with dimension \([\\text{m/s}] \\times [\\text{s}] = [\\text{m}]\).
- **C (Incorrect):** \(\\frac{1}{VT}\) has units of inverse distance (\(\\text{m}^{-1}\)).
- **D (Incorrect):** \(\\frac{T}{V}\) has units of inverse velocity/slowness (\(\\text{s}^2\\text{/m}\))."""
    }

    # Q22: MH-9-SCIT-12-12.1-OSC-022
    enhancements[21] = {
        "text": "SONAR (Sound Navigation and Ranging) operates on the physical principle of:",
        "options": [
            "Echo (reflection of ultrasonic waves)",
            "Acoustic resonance",
            "Reverberation of audible sound",
            "Diffraction around obstacles"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
SONAR utilizes high-frequency ultrasound pulses (frequency \(> 20\\text{ kHz}\)) to probe underwater environments. Ultrasound is preferred because its short wavelength allows it to travel in narrow, directional beams over long underwater distances without significant spreading.

### 2. Wave Dynamics & Mathematical Derivation:
The core operating principle of SONAR is **echo**, which is the regular reflection of sound waves from an obstacle back to the observer.
A transmitter emits an ultrasonic pulse that travels through water, strikes a reflective boundary (such as the ocean floor, a submarine, or an underwater reef), and reflects back to an acoustic receiver. Measuring the round-trip travel time \(t\) gives:
\\[
2d = v \\times t \\implies d = \\frac{v t}{2}
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** SONAR relies directly on the echo (reflection) of ultrasonic waves to determine distance and target topography.
- **B (Incorrect):** Resonance involves matching natural frequencies to amplify vibrations, which is not how target ranging operates.
- **C (Incorrect):** Reverberation is the persistence of sound due to multiple confused reflections in an enclosure, which SONAR avoids.
- **D (Incorrect):** Diffraction causes wave spreading around corners, which reduces targeting resolution."""
    }

    # Q23: MH-9-SCIT-12-12.1-OSC-023
    enhancements[22] = {
        "text": "An echo sounder installed on a fishing boat receives an echo from a shoal of fish 0.4 s after transmission. If the speed of sound in seawater is 1500 m/s, how deep is the shoal?",
        "options": [
            "150 m",
            "7500 m",
            "300 m",
            "600 m"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Echo sounding measures one-way distance to a submerged target by recording the two-way transit time of an ultrasonic signal that travels to the target and reflects back to the source.

### 2. Wave Dynamics & Mathematical Derivation:
Let \(d\) be the depth of the shoal of fish, \(v\) be the speed of sound in water, and \(t\) be the total round-trip time.
The ultrasonic pulse traverses the depth twice:
\\[
2d = v \\times t
\\]
Given:
- Speed of sound in seawater, \(v = 1500\\text{ m/s}\)
- Total echo time, \(t = 0.4\\text{ s}\)

Substitute the values:
\\[
2d = 1500 \\times 0.4 = 600\\text{ m}
\\]
\\[
d = \\frac{600}{2} = 300\\text{ m}
\\]
The shoal of fish is located at a depth of \(300\\text{ m}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** \(150\\text{ m}\) results from dividing the correct answer by 2 again.
- **B (Incorrect):** \(7500\\text{ m}\) results from dividing \(1500\) by \(0.4 / 2\).
- **C (Correct):** \(d = (1500 \\times 0.4) / 2 = 300\\text{ m}\).
- **D (Incorrect):** \(600\\text{ m}\) is the total two-way round-trip path length (\(2d\)); forgetting to divide by 2 is a common error."""
    }

    # Q24: MH-9-SCIT-12-12.1-OSC-024
    enhancements[23] = {
        "text": "Arrange the speed of sound in the following media in ascending (increasing) order:\\n(a) Air at 0 °C\\n(b) Iron\\n(c) Blood\\n(d) Distilled water",
        "options": [
            "d < a < c < b",
            "b < c < d < a",
            "a < d < c < b",
            "a < c < d < b"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Sound velocity depends on the elastic modulus (\(E\)) and density (\(\\rho\)) of the medium: \(v = \\sqrt{E/\\rho}\). In general, sound travels slowest in gases, faster in liquids, and fastest in solids due to the vastly higher bulk and Young's moduli of solids and liquids:
\\[
v_{\\text{gas}} < v_{\\text{liquid}} < v_{\\text{solid}}
\\]

### 2. Wave Dynamics & Mathematical Derivation:
Representative sound velocities at standard conditions:
- **(a) Air at 0 °C:** \(v \\approx 331\\text{--}332\\text{ m/s}\) (gas)
- **(d) Distilled water (25 °C):** \(v \\approx 1498\\text{ m/s}\) (pure liquid)
- **(c) Blood (37 °C):** \(v \\approx 1570\\text{ m/s}\) (dense biological fluid with dissolved proteins and cells)
- **(b) Iron (solid):** \(v \\approx 5950\\text{ m/s}\) (solid metal with high Young's modulus)

Arranging in ascending order (lowest to highest):
\\[
a (332\\text{ m/s}) < d (1498\\text{ m/s}) < c (1570\\text{ m/s}) < b (5950\\text{ m/s})
\\]
Hence, the sequence is **a < d < c < b**.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Places distilled water as having a lower sound speed than air, which is physically false.
- **B (Incorrect):** Reverses the order into descending sequence.
- **C (Correct):** Correctly orders gas (air, 332 m/s) < liquid (distilled water, 1498 m/s) < biological liquid (blood, 1570 m/s) < solid (iron, 5950 m/s).
- **D (Incorrect):** Inaccurately ranks blood below distilled water; blood has higher density and bulk modulus."""
    }

    # Q25: MH-9-SCIT-12-12.1-OSC-025
    enhancements[24] = {
        "text": "Which of the following is NOT an example of a transverse wave?",
        "options": [
            "Light emitted by a CFL lamp",
            "TV signals transmitted from a satellite",
            "Ripples spreading across the surface of a pond",
            "Musical notes produced by an orchestra traveling through air"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Transverse waves feature particle or field oscillations perpendicular to the direction of propagation, whereas longitudinal waves feature oscillations parallel to the direction of propagation.

### 2. Wave Dynamics & Mathematical Derivation:
- **Light from a CFL lamp (A)** and **satellite TV signals (B)** are electromagnetic waves consisting of transverse electric (\(\\vec{E}\)) and magnetic (\(\\vec{B}\)) fields perpendicular to the propagation vector (\(\\vec{k}\)).
- **Ripples on a pond (C)** are transverse surface waves where water molecules bob up and down vertically as the wave spreads horizontally.
- **Musical notes in air (D)** are acoustic sound waves. In air (a fluid with zero shear modulus), sound can propagate **only as a longitudinal wave** consisting of alternating compressions and rarefactions parallel to the wave direction.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B (Incorrect choices):** Both are electromagnetic waves and therefore genuinely transverse.
- **C (Incorrect choice):** Surface water waves exhibit vertical transverse oscillations.
- **D (Correct):** Musical sound waves traveling through air are strictly longitudinal mechanical waves, NOT transverse."""
    }

    # Q26: MH-9-SCIT-12-12.1-OSC-026
    enhancements[25] = {
        "text": "Which type of wave propagates via alternating regions of compressions and rarefactions?",
        "options": [
            "Transverse wave",
            "Light wave",
            "Longitudinal wave",
            "X-ray radiation"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Mechanical waves transmit energy by inducing cyclical spatial density and pressure variations in the medium.

### 2. Wave Dynamics & Mathematical Derivation:
In a **longitudinal wave**, particles of the medium oscillate parallel to the direction of wave travel.
- When particles crowd together, they form a region of high density and high pressure known as a **compression** (\(C\)).
- When particles spread apart, they create a region of low density and low pressure known as a **rarefaction** (\(R\)).
The spatial distance between two consecutive compressions or two consecutive rarefactions equals one wavelength (\(\\lambda\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Transverse waves propagate through crests and troughs, not compressions and rarefactions.
- **B, D (Incorrect):** Light waves and X-rays are transverse electromagnetic waves consisting of oscillating field vectors.
- **C (Correct):** Longitudinal waves propagate through alternating compressions and rarefactions parallel to the wave vector."""
    }

    # Q27: MH-9-SCIT-12-12.1-OSC-027
    enhancements[26] = {
        "text": "The acoustic intensity of a sound wave is defined as:",
        "options": [
            "The subjective physiological response of the human ear",
            "The pitch or highness of the musical sound",
            "The amount of sound energy passing per second through unit area perpendicular to propagation",
            "The total acoustic volume enclosed within a listening room"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Acoustic intensity is an objective, measurable physical property of a sound wave that quantifies the rate of energy transmission through space.

### 2. Wave Dynamics & Mathematical Derivation:
Sound intensity (\(I\)) is defined as the acoustic power (\(P\)) transmitted per unit area (\(A\)) oriented perpendicular to the direction of wave propagation:
\\[
I = \\frac{\\text{Energy}}{\\text{Time} \\times \\text{Area}} = \\frac{P}{A}
\\]
Expressed in terms of medium density (\(\\rho\)), wave velocity (\(v\)), angular frequency (\(\\omega = 2\\pi \\nu\)), and displacement amplitude (\(A_0\)):
\\[
I = \\frac{1}{2} \\rho v \\omega^2 A_0^2 = 2\\pi^2 \\rho v \\nu^2 A_0^2
\\]
The SI unit of sound intensity is Watts per square metre (\(\\text{W/m}^2\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Physiological response to intensity is termed *loudness*, which is a subjective psychological perception.
- **B (Incorrect):** Pitch is determined by frequency (\(\\nu\)), not energy flux per unit area.
- **C (Correct):** Acoustic intensity is quantitatively defined as energy per second per unit area perpendicular to wave flow (\(\\text{W/m}^2\)).
- **D (Incorrect):** Enclosed spatial volume is a geometric measure (\(\\text{m}^3\)), unrelated to acoustic wave flux."""
    }

    # Q28: MH-9-SCIT-12-12.1-OSC-028
    enhancements[27] = {
        "text": "Among the following metallic solids, in which material will the speed of sound be the HIGHEST at 25 °C?",
        "options": [
            "Nickel (Ni)",
            "Iron (Fe)",
            "Aluminium (Al)",
            "Brass"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
In solid elastic rods, the speed of longitudinal sound waves is determined by Young's modulus of elasticity (\(Y\)) and the mass density (\(\\rho\)):
\\[
v = \\sqrt{\\frac{Y}{\\rho}}
\\]

### 2. Wave Dynamics & Mathematical Derivation:
Comparing the experimental speed of sound values in metallic elements at \(25^\\circ\\text{C}\) (as cataloged in the Maharashtra State Board Class 9 Science textbook):
- **Aluminium (Al):** \(v \\approx 6420\\text{ m/s}\)
- **Nickel (Ni):** \(v \\approx 6040\\text{ m/s}\)
- **Iron (Fe):** \(v \\approx 5950\\text{ m/s}\)
- **Brass (Cu-Zn alloy):** \(v \\approx 4700\\text{ m/s}\)

Even though Aluminium has a lower Young's modulus than iron or nickel, its density (\(\\rho_{\\text{Al}} \\approx 2700\\text{ kg/m}^3\)) is almost one-third that of iron (\(\\rho_{\\text{Fe}} \\approx 7870\\text{ kg/m}^3\)). The very low density in the denominator produces a exceptionally high \(Y/\\rho\) ratio, yielding the highest speed of sound (\(6420\\text{ m/s}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Sound travels at \(6040\\text{ m/s}\) in nickel, which is lower than in aluminium.
- **B (Incorrect):** Sound travels at \(5950\\text{ m/s}\) in iron.
- **C (Correct):** Sound travels fastest in Aluminium (\(6420\\text{ m/s}\)) due to its remarkably low mass density.
- **D (Incorrect):** Sound travels at approximately \(4700\\text{ m/s}\) in brass."""
    }

    # Q29: MH-9-SCIT-12-12.1-OSC-029
    enhancements[28] = {
        "text": "A sound consisting of only a single, pure frequency is scientifically referred to as a:",
        "options": [
            "Note",
            "Tone",
            "Tune",
            "Node"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Acoustic waveforms are classified according to their spectral composition into pure single-frequency sinusoidal vibrations and composite harmonic vibrations.

### 2. Wave Dynamics & Mathematical Derivation:
- A sound wave of a **single frequency** is called a **tone**. It is represented mathematically by a pure sinusoid:
\\[
y(t) = A \\sin(2\\pi \\nu t)
\\]
A tuning fork vibrating cleanly produces an almost pure tone.
- A sound produced by a mixture of several different frequencies (a fundamental frequency plus higher harmonic overtones) is termed a **note**. Notes produced by musical instruments have rich acoustic timbre and are pleasant to hear.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** A *note* is composed of a mixture of multiple harmonic frequencies.
- **B (Correct):** A *tone* is strictly defined as a sound having only one distinct frequency.
- **C (Incorrect):** A *tune* refers to a musical melody consisting of a sequence of notes.
- **D (Incorrect):** A *node* is a spatial point of zero displacement amplitude in a stationary standing wave."""
    }

    # Q30: MH-9-SCIT-12-12.1-OSC-030
    enhancements[29] = {
        "text": "At which of the following temperatures will sound travel FASTEST in air?",
        "options": [
            "0 °C",
            "-20 °C",
            "30 °C",
            "50 °C"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Temperature affects the kinetic energy and average thermal velocity of gas molecules, which directly dictates how rapidly momentum and pressure pulses are transferred between colliding molecules.

### 2. Wave Dynamics & Mathematical Derivation:
According to Laplace's formula for the speed of sound in an ideal gas:
\\[
v = \\sqrt{\\frac{\\gamma R T}{M}} \\implies v \\propto \\sqrt{T}
\\]
where \(T\) is the absolute temperature in Kelvin (\(T = \\theta + 273.15\\text{ K}\)).
Converting each temperature to Kelvin:
- \(-20^\\circ\\text{C} = 253.15\\text{ K}\)
- \(0^\\circ\\text{C} = 273.15\\text{ K}\)
- \(30^\\circ\\text{C} = 303.15\\text{ K}\)
- \(50^\\circ\\text{C} = 323.15\\text{ K}\)
Since \(323.15\\text{ K}\) is the highest absolute temperature:
\\[
v_{50^\\circ\\text{C}} > v_{30^\\circ\\text{C}} > v_{0^\\circ\\text{C}} > v_{-20^\\circ\\text{C}}
\\]
(Approximately, sound speed increases by \(0.61\\text{ m/s}\) for each \(1^\\circ\\text{C}\) rise in temperature: \(v_t \\approx v_0 + 0.61 t\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, C (Incorrect):** These represent lower temperatures, resulting in slower molecular collisions and lower sound velocities.
- **D (Correct):** Sound travels fastest at \(50^\\circ\\text{C}\) because velocity is directly proportional to the square root of absolute temperature (\(v \\propto \\sqrt{T}\))."""
    }

    # Q31: MH-9-SCIT-12-12.1-OSC-031
    enhancements[30] = {
        "text": "In the human ear, which sensory organ is responsible for identifying the pitch and loudness of incoming sound waves?",
        "options": [
            "Pinna",
            "Auditory canal",
            "Cochlea",
            "Malleus (Hammer)"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
The human ear is divided into outer, middle, and inner sections. While the outer and middle ear collect and amplify mechanical vibrations, the inner ear performs acoustic sensory transduction.

### 2. Wave Dynamics & Mathematical Derivation:
- The **cochlea** is a snail-shaped, fluid-filled spiral organ located in the inner ear.
- Within the cochlea lies the **basilar membrane** lined with thousands of microscopic sensory hair cells (the organ of Corti).
- Different frequencies vibrate different regions along the tapered basilar membrane (high frequencies resonate near the stiff base, low frequencies near the flexible apex), allowing precise detection of **pitch** (tonotopic mapping).
- The degree of hair cell deflection reflects the vibration amplitude, encoding perceived **loudness**.
- These mechanical deflections trigger neurochemical depolarizations that generate nerve impulses sent along the auditory nerve to the brain.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** The pinna collects and directs ambient sound waves into the auditory canal.
- **B (Incorrect):** The auditory canal simply channels sound waves to the tympanic membrane.
- **C (Correct):** The cochlea contains the sensory basilar membrane and hair cells that transduce and discriminate sound pitch and loudness.
- **D (Incorrect):** The malleus (hammer) is a middle-ear bone that mechanically magnifies pressure."""
    }

    # Q32: MH-9-SCIT-12-12.1-OSC-032
    enhancements[31] = {
        "text": "Low-frequency sound waves produced within Earth's crust before the main shockwaves of an earthquake belong to which frequency domain?",
        "options": [
            "Ultrasonic sound (> 20,000 Hz)",
            "Infrasonic sound (< 20 Hz)",
            "Audible sound (20 Hz - 20,000 Hz)",
            "Electromagnetic radiation"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Acoustic waves are categorized by their vibration frequency relative to normal human auditory perception:
- Infrasound: \(\\nu < 20\\text{ Hz}\)
- Audible sound: \(20\\text{ Hz} \\le \\nu \\le 20{,}000\\text{ Hz}\)
- Ultrasound: \(\\nu > 20{,}000\\text{ Hz}\)

### 2. Wave Dynamics & Mathematical Derivation:
Before destructive earthquake shockwaves rupture the surface, massive subterranean rock strata undergo initial micro-fracturing and slow tectonic slippage. These large-scale crustal movements generate very low frequency vibrations below \(20\\text{ Hz}\), which are **infrasonic waves**:
\\[
\\nu_{\\text{seismic precursor}} < 20\\text{ Hz}
\\]
While inaudible to human ears, certain animals (such as dogs, elephants, and birds) can detect these infrasonic precursors and display noticeable distress before humans feel the earthquake.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Ultrasonic sound has frequencies above \(20\\text{ kHz}\); earthquakes do not generate primary ultrasound waves.
- **B (Correct):** Subterranean rock tremors generate low-frequency infrasonic waves below \(20\\text{ Hz}\).
- **C (Incorrect):** Humans cannot hear these precursor tremors because they lie below the audible limit of \(20\\text{ Hz}\).
- **D (Incorrect):** Earthquake tremors are mechanical elastic waves, not electromagnetic radiation."""
    }

    # Q33: MH-9-SCIT-12-12.1-OSC-033
    enhancements[32] = {
        "text": "Identical strings of the same length and under equal tension in a guitar and a violin sound distinct when plucked. This difference in sound character is due to their:",
        "options": [
            "Different harmonic overtones and acoustic body resonance (Timbre)",
            "Different speeds of sound through ambient air",
            "Different fundamental frequencies of the strings",
            "Different gravitational pull acting on the instruments"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
When two different musical instruments play a note of the exact same pitch (frequency) and loudness (intensity), the human ear effortlessly distinguishes between them. This distinct subjective acoustic characteristic is called **quality** or **timbre**.

### 2. Wave Dynamics & Mathematical Derivation:
A musical string does not vibrate exclusively at its fundamental frequency (\(\\nu_1\)); it vibrates simultaneously in higher harmonic modes (\(2\\nu_1, 3\\nu_1, 4\\nu_1, \\dots\)).
The overall acoustic waveform is a Fourier superposition:
\\[
y(t) = \\sum_{n=1}^{\\infty} A_n \\sin(n \\omega_1 t + \\phi_n)
\\]
The hollow wooden soundbox of a guitar and the curved resonance chamber of a violin amplify different harmonic overtones (\(A_n\)) with distinct relative amplitudes. This creates unique, complex waveforms that our brain perceives as the distinctive timbre of each instrument.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Differences in the mixture of harmonic overtones and the acoustic resonance of the wooden body shape produce different timbres.
- **B (Incorrect):** Sound travels through the ambient air at the same constant speed regardless of the instrument.
- **C (Incorrect):** For identical string length, tension, and linear density, fundamental frequency \(\\nu = \\frac{1}{2L}\\sqrt{T/m}\) is identical.
- **D (Incorrect):** Gravity plays no role in determining musical timbre."""
    }

    # Q34: MH-9-SCIT-12-12.1-OSC-034
    enhancements[33] = {
        "text": "A sound wave possessing a frequency of 5000 Hz falls into which frequency classification?",
        "options": [
            "Ultrasound",
            "Infrasound",
            "Audible sound",
            "Sub-audible whisper"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
The human ear is sensitive to acoustic vibrations over a specific frequency band termed the audible spectrum.

### 2. Wave Dynamics & Mathematical Derivation:
Acoustic classifications are strictly defined as:
\\[
\\text{Infrasound: } \\nu < 20\\text{ Hz}
\\]
\\[
\\text{Audible range: } 20\\text{ Hz} \\le \\nu \\le 20{,}000\\text{ Hz}
\\]
\\[
\\text{Ultrasound: } \\nu > 20{,}000\\text{ Hz}
\\]
Given \(\\nu = 5000\\text{ Hz} = 5\\text{ kHz}\):
\\[
20\\text{ Hz} < 5000\\text{ Hz} < 20{,}000\\text{ Hz}
\\]
Since \(5000\\text{ Hz}\) lies comfortably between the lower and upper auditory thresholds, it is an **audible sound** (perceived as a high-pitched whistle or tone).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Ultrasound requires frequencies exceeding \(20{,}000\\text{ Hz}\).
- **B (Incorrect):** Infrasound consists of vibrations below \(20\\text{ Hz}\).
- **C (Correct):** \(5000\\text{ Hz}\) falls within the human audible band of \(20\\text{ Hz} - 20{,}000\\text{ Hz}\).
- **D (Incorrect):** Sub-audible sounds are below \(20\\text{ Hz}\); whispers are audible sounds with low amplitude, not a frequency band."""
    }

    # Q35: MH-9-SCIT-12-12.1-OSC-035
    enhancements[34] = {
        "text": "Which of the following is classified as a percussion musical instrument?",
        "options": [
            "Mridangam",
            "Flute",
            "Guitar",
            "Harmonium"
        ],
        "correctAnswer": "A",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Musical instruments are classified according to their mechanism of sound excitation:
1. **Percussion instruments (Avanaddha/Ghana vadya):** Sound is produced by striking, beating, or scraping a stretched membrane or solid resonator.
2. **Wind instruments (Sushira vadya):** Sound is produced by vibrating air columns.
3. **Stringed instruments (Tata vadya):** Sound is produced by plucking or bowing taut strings.

### 2. Wave Dynamics & Mathematical Derivation:
- The **Mridangam** is a classical Indian double-sided drum featuring stretched leather membranes. When struck by the musician's hands, 2D transverse vibrational modes are excited in the membrane, producing resonant rhythmic percussive sounds.
- A flute is a wind instrument (air column).
- A guitar is a string instrument.
- A harmonium is a reed-based keyboard instrument.

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Correct):** Mridangam is a membranophone / percussion instrument played by striking stretched membranes.
- **B (Incorrect):** Flute produces sound via air column resonance (aerophone).
- **C (Incorrect):** Guitar produces sound via vibrating strings (chordophone).
- **D (Incorrect):** Harmonium utilizes vibrating metallic reeds actuated by air bellows."""
    }

    # Q36: MH-9-SCIT-12-12.1-OSC-036
    enhancements[35] = {
        "text": "Sound waves can propagate through which of the following media?",
        "options": [
            "Solids only",
            "Liquids only",
            "Gases only",
            "Solids, liquids, and gases"
        ],
        "correctAnswer": "D",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
Sound is a mechanical wave that requires an elastic material medium possessing mass and inertia to propagate.

### 2. Wave Dynamics & Mathematical Derivation:
Acoustic waves transmit through material media via intermolecular interactions:
- In **solids**, tight lattice bonding supports both longitudinal and transverse waves (\(v \\approx 5000\\text{--}6500\\text{ m/s}\)).
- In **liquids**, bulk modulus allows longitudinal wave propagation (\(v \\approx 1400\\text{--}1550\\text{ m/s}\)).
- In **gases**, compressibility allows longitudinal compressions and rarefactions (\(v \\approx 330\\text{--}350\\text{ m/s}\)).
Sound propagates through all three states of matter, but cannot propagate through a vacuum where no particles exist (\(v_{\\text{vacuum}} = 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A, B, C (Incorrect):** Sound is not restricted to any single state of matter; it travels effectively through all three.
- **D (Correct):** Sound can propagate through solids, liquids, and gases."""
    }

    # Q37: MH-9-SCIT-12-12.1-OSC-037
    enhancements[36] = {
        "text": "The pitch (shrillness) of a musical sound:",
        "options": [
            "Depends directly on the amplitude of vibration",
            "Is independent of the amplitude of vibration",
            "Varies inversely with the frequency of vibration",
            "Increases exponentially with sound intensity"
        ],
        "correctAnswer": "B",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
In acoustics, pitch and loudness represent two entirely independent perceptual dimensions of sound.

### 2. Wave Dynamics & Mathematical Derivation:
- **Pitch (shrillness)** is governed strictly by the **frequency (\(\\nu\))** of the sound wave. Higher frequency means more wave cycles per second, yielding a higher pitch / shriller sound:
\\[
\\text{Pitch} \\propto \\nu
\\]
- **Loudness** is governed by the **amplitude (\(A\))** of the wave, with intensity \(I \\propto A^2\).
Varying the amplitude alters the sound's volume from soft to loud, but leaves the vibration frequency and pitch completely unaltered. Thus, pitch is physically independent of amplitude.

### 3. Step-by-Step Option & Misconception Analysis:
- **A, D (Incorrect):** Amplitude governs loudness and sound intensity, not pitch or shrillness.
- **B (Correct):** Pitch is determined solely by frequency and is independent of the vibration amplitude.
- **C (Incorrect):** Pitch varies directly—not inversely—with vibration frequency."""
    }

    # Q38: MH-9-SCIT-12-12.1-OSC-038 (Fixed defect)
    enhancements[37] = {
        "text": "The time period of an oscillating simple pendulum is independent of which of the following physical quantities?",
        "options": [
            "Length of the pendulum",
            "Acceleration due to gravity",
            "Mass of the pendulum bob",
            "Geographic location on Earth"
        ],
        "correctAnswer": "C",
        "solution": """### 1. Scientific Principle & Acoustic / Physical Context:
A simple pendulum consists of a point mass (bob) suspended from a frictionless pivot by a light, inextensible string executing small-angle harmonic oscillations.

### 2. Wave Dynamics & Mathematical Derivation:
The time period \(T\) of a simple pendulum for small oscillations (\(\\theta < 10^\\circ\)) is given by:
\\[
T = 2\\pi \\sqrt{\\frac{L}{g}}
\\]
where:
- \(L\) is the effective length of the pendulum.
- \(g\) is the acceleration due to gravity at the location.
Notice that the mass of the bob \(m\) does **not** appear anywhere in this formula.
This independence arises because gravitational force (weight \(F_g = mg\)) is directly proportional to mass, while inertial resistance to acceleration (\(F_{\\text{inertial}} = ma\)) is also directly proportional to mass. The mass terms cancel out identically (\(mg \\sin\\theta \\approx m L \\ddot{\\theta} \\implies \\ddot{\\theta} + \\frac{g}{L}\\theta = 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **A (Incorrect):** Period is directly proportional to the square root of pendulum length (\(T \\propto \\sqrt{L}\)).
- **B, D (Incorrect):** Period depends inversely on the square root of gravity (\(T \\propto 1/\\sqrt{g}\)), which varies with geographic latitude and altitude.
- **C (Correct):** The time period is completely independent of the mass of the bob."""
    }

    return enhancements

if __name__ == '__main__':
    data = get_part1_enhancements()
    print(f"Generated {len(data)} enhancements for Part 1 (Q1 to Q38).")
