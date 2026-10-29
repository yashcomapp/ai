// scripts/ch3_part1.js - Questions 1 to 30 of Chapter 3 (Current Electricity)
module.exports = [
  {
    id: "MH-9-SCIT-3-3.1-OSC-001",
    text: "The electric power supplied to our homes for operating domestic electrical appliances is distributed in which form?",
    options: [
      "High-voltage direct current (HVDC)",
      "Low-voltage pulsating direct current (DC)",
      "Alternating current (AC mains at \\(220\\text{ V}, 50\\text{ Hz}\\))",
      "Static electricity"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In domestic electricity distribution grids, electrical power is transmitted and supplied as **Alternating Current (AC)**:
\\[
V(t) = V_0 \\sin(2\\pi f t)
\\]
In India and Maharashtra State Electricity Board (MSEB / MSEDCL) standards:
- Root-Mean-Square (RMS) voltage: \\(V_{\\text{rms}} = 220\\text{ V}\\)
- Frequency: \\(f = 50\\text{ Hz}\\) (the direction of current reverses 100 times per second).
AC is chosen over DC because AC voltages can be efficiently stepped up or stepped down with minimal power loss using electromagnetic transformers (\\(P_{\\text{loss}} = I^2 R\\)).

### 2. Physical Context & Practical Illustration:
Power stations generate electricity at high voltage and transmit it over hundreds of kilometers. Step-down substation transformers then lower the voltage to \\(220\\text{ V}\\) AC before it enters domestic consumer households to safely run fans, refrigerators, and lighting.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (HVDC)**: Incorrect. HVDC is utilized only for long-distance bulk inter-regional transmission, not domestic wall outlets.
- **Option B (Direct current DC)**: Incorrect. Chemical batteries provide DC; grid wall outlets provide AC.
- **Option C (AC mains)**: Correct. Standard household domestic supply is \\(220\\text{ V}, 50\\text{ Hz}\\) alternating current.
- **Option D (Static electricity)**: Incorrect. Static electricity involves stationary charges and cannot sustain continuous appliance operation.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-002",
    text: "When a cylindrical bar magnet is cut into two halves across its transverse midpoint, what happens to the two resulting pieces?",
    options: [
      "Each piece becomes a complete, independent magnet possessing both a North and a South pole",
      "Each piece loses its magnetism completely",
      "One piece becomes an isolated North pole and the other an isolated South pole",
      "Both pieces lose their ability to attract ferromagnetic substances"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In classical electromagnetism and Gauss's Law for Magnetism:
\\[
\\nabla \\cdot \\vec{B} = 0 \\implies \\oint \\vec{B} \\cdot d\\vec{A} = 0
\\]
This fundamental law dictates that **isolated magnetic monopoles do not exist** in nature.
At the microscopic level, ferromagnetism is caused by atomic electron spin dipoles aligned in localized magnetic domains. When a magnet is cut in two, the aligned domains within each piece remain intact, automatically forming a new South pole at the cut face of the northern segment, and a new North pole at the cut face of the southern segment.

### 2. Physical Context & Practical Illustration:
No matter how many times you divide a magnet—even down to the microscopic atomic scale—every single fragment retains a paired North and South pole.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Two complete magnets)**: Correct. Cutting a magnet produces two complete dipole magnets.
- **Option B (Loses magnetism)**: Incorrect. Mechanical cutting does not randomize internal domain alignment.
- **Option C (Isolated poles)**: Incorrect. Magnetic monopoles do not exist.
- **Option D (Will not attract iron)**: Incorrect. Both new magnets actively attract iron filings.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-003",
    text: "Which type of magnetic instrument is specifically designed to detect geographic and navigational directions on Earth's surface?",
    options: [
      "A cylindrical bar magnet",
      "A horseshoe (U-shaped) magnet",
      "A pivoted magnetic compass needle",
      "An electromagnetic solenoid"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Earth behaves as a giant magnetic dipole whose magnetic South pole is situated near the geographic North pole.
When a lightweight, slender magnetic needle is balanced horizontally on a low-friction jewel bearing, the horizontal component of Earth's magnetic field (\\(B_H\\)) exerts a restoring magnetic torque:
\\[
\\vec{\\tau} = \\vec{M} \\times \\vec{B}_H
\\]
This torque rotates the needle until its magnetic dipole moment \\(\\vec{M}\\) aligns parallel to the local magnetic meridian, pointing directly North-South.

### 2. Physical Context & Practical Illustration:
Mariners, aviators, and hikers rely on magnetic compasses to establish directional orientation across open oceans and wilderness where geographic landmarks are absent.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Bar magnet)**: Incorrect. Heavy and lacks a low-friction pivot for sensitive field detection.
- **Option B (Horseshoe magnet)**: Incorrect. Horseshoe magnets have closely spaced poles designed for concentrated lifting, not directional sensing.
- **Option C (Magnetic compass needle)**: Correct. Lightweight, pivoted needle freely aligns with Earth's magnetic meridian.
- **Option D (Electromagnetic solenoid)**: Incorrect. Requires external electric current and is not a portable directional instrument.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-004",
    text: "Which of the following metallic elements is classified as a ferromagnetic substance?",
    options: [
      "Gold (\\(\\text{Au}\\))",
      "Cobalt (\\(\\text{Co}\\))",
      "Aluminium (\\(\\text{Al}\\))",
      "Silver (\\(\\text{Ag}\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic materials are classified into three primary categories based on magnetic susceptibility \\(\\chi_m\\):
1. **Ferromagnetic**: Exhibit strong positive susceptibility (\\(\\chi_m \\gg 1\\)) and form spontaneous aligned magnetic domains. The three classic ferromagnetic transition metals at room temperature are:
\\[
\\text{Iron (Fe), Cobalt (Co), Nickel (Ni)}
\\]
2. **Paramagnetic**: Weakly attracted (e.g. Aluminium, Platinum).
3. **Diamagnetic**: Weakly repelled (e.g. Gold, Silver, Copper, Bismuth).

### 2. Physical Context & Practical Illustration:
Cobalt is alloyed with iron, nickel, and aluminium to produce **Alnico** magnets, which possess exceptionally high coercivity and are widely used in guitar pickups and industrial loudspeakers.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Gold)**: Incorrect. Diamagnetic metal; weakly repelled by magnetic fields.
- **Option B (Cobalt)**: Correct. Canonical ferromagnetic metal that strongly attracts to magnets.
- **Option C (Aluminium)**: Incorrect. Paramagnetic substance with negligible room-temperature attraction.
- **Option D (Silver)**: Incorrect. Diamagnetic metal.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-005",
    text: "Which of the following safety protective devices is installed in domestic electric circuits to safeguard appliances from overcurrent and electrical overloading?",
    options: [
      "An electric fuse (or miniature circuit breaker - MCB)",
      "A single-pole toggle switch",
      "A fan step regulator",
      "A three-pin wall plug"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric fuse functions on the **Joule heating effect of electric current**:
\\[
H = I^2 R t
\\]
A fuse wire is manufactured from a low-melting-point alloy (such as lead-tin alloy, \\(\\text{Pb-Sn}\\)).
When excessive current flows due to overloading or a short circuit (\\(I > I_{\\text{rated}}\\)):
1. Excessive heat \\(H\\) is generated rapidly.
2. The fuse wire exceeds its melting temperature, melts, and breaks the continuity of the circuit.
3. Current drops to zero instantly (\\(I = 0\\)), preventing fire hazards and appliance damage.

### 2. Physical Context & Practical Illustration:
In modern household electrical distribution boards, sacrificial fuse wires are largely replaced by reusable **Miniature Circuit Breakers (MCBs)**, which automatically trip an electromechanical switch during overcurrent conditions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Electric fuse / MCB)**: Correct. Designed specifically to break the circuit during overcurrent/short circuits.
- **Option B (Toggle switch)**: Incorrect. Manual on/off controller; does not provide automatic overload protection.
- **Option C (Fan regulator)**: Incorrect. Regulates resistance to alter motor speed, not an overcurrent safety device.
- **Option D (Three-pin plug)**: Incorrect. Passive connector; contains an earthing pin but does not break current automatically.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-006",
    text: "An electric immersion water heater primarily converts electrical energy into which form of energy?",
    options: [
      "Light radiant energy",
      "Thermal (heat) energy",
      "Chemical potential energy",
      "Mechanical kinetic energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric water heater operates according to **Joule's Law of Heating**:
\\[
H = I^2 R t = V I t = \\frac{V^2}{R} t
\\]
The heating element is made of high-resistivity **Nichrome wire** (an alloy of nickel and chromium). When electric current \\(I\\) flows through the element, the kinetic energy of colliding conduction electrons is transferred into lattice vibrational energy of the metal ions, releasing **thermal (heat) energy**.

### 2. Physical Context & Practical Illustration:
The Nichrome heating coil is encased within a copper or stainless steel tube insulated by magnesium oxide (\\(\\text{MgO}\\)) powder, transferring heat directly to the surrounding water while maintaining electrical insulation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Light energy)**: Incorrect. Incandescent bulbs emit light; immersion heaters emit minimal light.
- **Option B (Heat energy)**: Correct. Converts electrical energy into thermal heat to raise water temperature.
- **Option C (Chemical energy)**: Incorrect. Recharging batteries converts electrical to chemical, not heaters.
- **Option D (Mechanical energy)**: Incorrect. Electric motors produce mechanical energy.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-007",
    text: "What is the most effective traditional laboratory method to magnetize a sewing needle or steel pin using a permanent bar magnet?",
    options: [
      "Heating the steel pin to red hot and cooling it in ice water",
      "Stroking the pin repeatedly in a single direction from one end to the other with one pole of the bar magnet",
      "Vigorously hammering the pin with the bar magnet",
      "Immersing the pin in boiling water"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In unmagnetized steel, magnetic domains (clusters of aligned atomic dipoles) are oriented in random directions, resulting in zero net magnetic field:
\\[
\\sum \\vec{m}_i = 0
\\]
In the **single-touch method**:
1. One pole of a strong bar magnet (e.g., North pole) is placed at one end of the steel pin and stroked along its length to the other end.
2. The magnet is lifted clear into the air and returned to the starting end.
3. Repeating this process \\(20\\) to \\(30\\) times in the **exact same direction** exerts a magnetic torque that systematically rotates the random domains into parallel alignment:
\\[
\\sum \\vec{m}_i \\gg 0
\\]

### 2. Physical Context & Practical Illustration:
Heating or hammering a magnet randomizes domain alignment via thermal agitation and mechanical shock, destroying magnetism. Single-direction stroking is the canonical method for creating a permanent magnetic needle.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Heating)**: Incorrect. Destroys magnetic domain alignment (demagnetization).
- **Option B (Single-touch stroking)**: Correct. Methodical stroking aligns domains along the pin's axis.
- **Option C (Hammering)**: Incorrect. Mechanical shock randomizes dipoles and causes demagnetization.
- **Option D (Boiling water)**: Incorrect. Heating impairs magnetic properties.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-008",
    text: "Which of the following metallic substances is classified as a non-magnetic material?",
    options: [
      "Iron",
      "Nickel",
      "Aluminium",
      "Cobalt"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Substances are categorized as magnetic (strongly attracted to magnets) or non-magnetic:
- **Ferromagnetic (Magnetic)**: Iron (\\(\\text{Fe}\\)), Nickel (\\(\\text{Ni}\\)), Cobalt (\\(\\text{Co}\\)), and their alloys (steel, Alnico). They have unpaired electron spins that lock into macroscopic magnetic domains.
- **Non-magnetic**: Materials that experience no noticeable attraction to ordinary permanent magnets, such as **Aluminium**, Copper, Brass, Gold, and Wood.

### 2. Physical Context & Practical Illustration:
Scrap metal sorting yards use giant lifting electromagnets to separate ferrous metals (iron and steel) from non-ferrous non-magnetic metals (aluminium beverage cans and copper wiring).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Iron)**: Magnetic ferromagnetic substance.
- **Option B (Nickel)**: Magnetic ferromagnetic substance.
- **Option C (Aluminium)**: Correct. Non-magnetic (paramagnetic) metal with no everyday magnetic attraction.
- **Option D (Cobalt)**: Magnetic ferromagnetic substance.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-009",
    text: "In a standard gold-leaf electroscope, why are the delicate leaves attached to the bottom of the brass rod manufactured from gold (\\(\\text{Au}\\)) foil?",
    options: [
      "Because gold is the cheapest available metal",
      "Because gold can be beaten into extremely thin, lightweight, and highly conductive foils",
      "Because gold is naturally radioactive",
      "Because gold acts as an electrical insulator"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In an electroscope, like charges conducted down the central rod distribute across the two leaves. The electrostatic repulsive force between the leaves is:
\\[
F_e = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2}
\\]
This electrostatic force must overcome the downward gravitational force (weight \\(W = mg\\)) of the leaves to produce visible angular divergence \\(\\theta\\):
\\[
\\tan\\theta = \\frac{F_e}{mg}
\\]
To maximize sensitivity to minute quantities of charge \\(q\\), the mass \\(m\\) must be as small as possible. Gold possesses the highest **malleability** of all metals, allowing it to be hammered into leaves just \\(0.0001\\text{ mm}\\) thick while remaining an excellent electrical conductor.

### 2. Physical Context & Practical Illustration:
Thin gold foil leaves weigh only a few milligrams, allowing even tiny electrostatic charges from a rubbed plastic comb to cause a clear, dramatic leaf divergence.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Cheapest metal)**: Incorrect. Gold is a precious metal, but very little mass is required.
- **Option B (Thin, lightweight, conductive)**: Correct. Superb malleability yields featherweight conductive leaves for maximum sensitivity.
- **Option C (Radioactive)**: Incorrect. Natural gold is non-radioactive.
- **Option D (Insulator)**: Incorrect. Gold is an exceptional conductor.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-010",
    text: "Which of the following physical processes is utilized to produce static electric charges by transfer of electrons between two insulating bodies?",
    options: [
      "Thermal conduction",
      "Fluid convection",
      "Triboelectric friction (rubbing)",
      "Electromagnetic radiation"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Static electricity is generated via **frictional charging (triboelectric effect)**.
When two different insulating materials (such as glass and silk, or amber and fur) are rubbed together:
1. Mechanical friction brings microscopic surface asperities into intimate atomic contact.
2. The material with lower electron work function releases valence electrons to the material with higher electron affinity.
3. Conservation of electric charge:
\\[
q_{\\text{lost}} = -q_{\\text{gained}} \\implies Q_{\\text{total}} = 0
\\]
One body becomes positively charged and the other becomes equally negatively charged.

### 2. Physical Context & Practical Illustration:
Running a plastic comb through dry hair transfers electrons from the hair to the comb. The negatively charged comb can then pick up tiny pieces of paper via electrostatic induction.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Conduction)**: Incorrect. Conduction transfers heat or electric current across conductors, not static charges on dry insulators.
- **Option B (Convection)**: Incorrect. Heat transfer mechanism in moving fluids.
- **Option C (Triboelectric friction)**: Correct. Rubbing insulators transfers electrons and generates static charge.
- **Option D (Radiation)**: Incorrect. Energy transfer via electromagnetic photons.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-011",
    text: "In electrical utility billing, domestic electricity consumption is measured and charged per 'unit'. What is the exact scientific definition of one commercial unit of electricity?",
    options: [
      "One Watt-hour (\\(1\\text{ Wh}\\))",
      "One Kilowatt-hour (\\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}\\))",
      "One Megawatt-second (\\(1\\text{ MWs}\\))",
      "One Ampere-hour (\\(1\\text{ Ah}\\))"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In commercial and domestic electric power distribution:
\\[
\\text{Energy} = \\text{Power} \\times \\text{Time}
\\]
One commercial 'Board of Trade Unit' (or simply 'unit') is defined as **one Kilowatt-hour (kWh)**:
\\[
1\\text{ unit} = 1\\text{ kWh} = 1000\\text{ Watts} \\times 3600\\text{ seconds}
\\]
\\[
1\\text{ unit} = 3,600,000\\text{ Joules} = 3.6 \\times 10^6\\text{ J} = 3.6\\text{ MJ}
\\]

### 2. Physical Context & Practical Illustration:
Operating an electric iron rated at \\(1000\\text{ W}\\) (\\(1\\text{ kW}\\)) for exactly one hour consumes \\(1\\text{ unit}\\) of electricity on the household digital energy meter.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1 Wh)**: Incorrect. A Watt-hour is only \\(3600\\text{ J}\\), which is \\(1/1000\\)th of a commercial unit.
- **Option B (1 kWh)**: Correct. Commercial unit of electricity equals \\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}\\).
- **Option C (1 MWs)**: Incorrect. Not standard commercial terminology.
- **Option D (1 Ah)**: Incorrect. Ampere-hour measures electric charge capacity in chemical batteries, not electrical energy.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-012",
    text: "For a standard rectangular bar magnet, at which location along its body is the magnetic attractive force on iron filings greatest?",
    options: [
      "Concentrated near the two magnetic poles located near the ends",
      "Uniformly distributed along the outer surface",
      "At the geometric center midpoint",
      "Equal in all directions around the magnet"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic field lines of a bar magnet emerge from the North pole and curve around to re-enter at the South pole, forming closed continuous loops.
The magnetic flux density \\(\\vec{B}\\) is directly proportional to the spatial concentration (density) of magnetic field lines:
\\[
B \\propto \\frac{d\\Phi}{dA}
\\]
Field lines crowd together most densely near the **poles** located slightly inside the physical ends of the bar magnet. Hence, magnetic field intensity and attractive force on ferromagnetic filings are **maximum at the poles** and minimum at the neutral center.

### 2. Physical Context & Practical Illustration:
When a bar magnet is rolled in a tray of iron filings, dense clusters of filings cling to the two ends (poles), while virtually no filings adhere to the center of the bar.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Near the poles)**: Correct. Magnetic flux density is highest near the poles.
- **Option B (Uniformly distributed)**: Incorrect. Magnetic strength varies drastically along the bar's length.
- **Option C (At the center)**: Incorrect. The center represents the neutral region where opposing pole influences cancel.
- **Option D (Equal in all directions)**: Incorrect. Bar magnets are anisotropic dipoles.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-013",
    text: "Which metallic material is primarily used to construct lightning protection conductors mounted on the rooftops of tall buildings?",
    options: [
      "Cast Iron",
      "Lead",
      "Copper (\\(\\text{Cu}\\))",
      "Cobalt"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A lightning conductor protects structures by providing a very low-resistance path to safely discharge atmospheric lightning strikes into the earth:
\\[
R = \\rho \\frac{l}{A}
\\]
During a lightning discharge, peak currents can exceed \\(50,000\\text{ Amperes}\\). To prevent violent resistive heating (\\(H = I^2 R t\\)) from melting the conductor or igniting building materials, the electrical resistivity \\(\\rho\\) must be exceptionally low. **Copper** has one of the highest electrical conductivities (lowest resistivities, \\(\\rho \\approx 1.68 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)) and excellent corrosion resistance.

### 2. Physical Context & Practical Illustration:
Invented by Benjamin Franklin, a copper lightning rod features sharp spikes at the top to facilitate corona discharge and is connected to a thick copper strip that extends down to a grounding copper plate buried deep in moist soil.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Cast Iron)**: Incorrect. Much higher electrical resistivity and prone to rusting.
- **Option B (Lead)**: Incorrect. Poor conductor with low melting point.
- **Option C (Copper)**: Correct. High electrical conductivity, high melting point, and durable corrosion resistance.
- **Option D (Cobalt)**: Incorrect. Magnetic metal with high resistance; unsuited for lightning grounding.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-014",
    text: "Why do fine airborne dust particles rapidly accumulate on the glass screen of a cathode-ray tube (CRT) or television set after it has been switched on?",
    options: [
      "Due to atmospheric air pressure differences",
      "Due to radiant heating of the glass",
      "Due to condensation of ambient water vapor",
      "Due to electrostatic attraction from static electric charges accumulated on the glass"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a television screen, high-energy electron beams strike the phosphor-coated interior of the glass screen. This electron bombardment induces a static electric charge on the exterior glass face.
When uncharged neutral airborne dust particles drift near the charged screen:
1. The electric field \\(\\vec{E}\\) of the screen induces dipole polarization in the dust particles.
2. The side of the dust particle with opposite charge is pulled closer than the side with like charge.
3. By Coulomb's law (\\(F \\propto 1/r^2\\)), the attractive electrostatic force exceeds the repulsive force, pulling the dust firmly against the glass screen.

### 2. Physical Context & Practical Illustration:
This is the exact same electrostatic phenomenon where a charged plastic ruler attracts tiny uncharged bits of paper.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Air pressure)**: Incorrect. Air pressure is uniform across the screen face.
- **Option B (Radiant heat)**: Incorrect. Heat creates convective updrafts that would tend to blow dust away.
- **Option C (Water vapor)**: Incorrect. Dust accumulation occurs even in completely dry environments.
- **Option D (Electrostatic attraction)**: Correct. Static charges on the screen attract polarized neutral dust particles.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-015",
    text: "Which of the following common metal wires will NOT be attracted by a strong permanent magnet?",
    options: [
      "Pure copper wire",
      "Soft iron wire",
      "High-carbon steel wire",
      "Nickel wire"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Materials exhibit different magnetic behaviors based on atomic electron shell configurations:
- **Ferromagnetic materials** (Iron, Steel, Nickel, Cobalt): Strongly attracted to magnets due to permanent atomic magnetic dipole moments and spontaneous domain alignment.
- **Diamagnetic materials** (Copper, Bismuth, Gold): Have all paired electrons with zero net atomic dipole moments. In external magnetic fields, they develop a tiny opposing induced magnetic moment and are slightly repelled, exhibiting **zero attraction**.

### 2. Physical Context & Practical Illustration:
Electric motors and transformers use copper wire for windings specifically because copper is an outstanding electrical conductor that will not magnetically stick to or distort the iron stator core.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Pure copper)**: Correct. Non-magnetic (diamagnetic) metal that is not attracted to magnets.
- **Option B (Soft iron)**: Incorrect. Classic ferromagnetic metal that strongly attracts.
- **Option C (Steel)**: Incorrect. Iron-carbon alloy that strongly attracts.
- **Option D (Nickel)**: Incorrect. Ferromagnetic element that strongly attracts.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-016",
    text: "Which of the following statements correctly describes the distribution of magnetic field strength along the length of a bar magnet?",
    options: [
      "Magnetic strength is maximum at the geometric center and decreases toward the ends",
      "Magnetic strength is strictly uniform across the entire length of the magnet",
      "Magnetic strength is maximum near the ends (poles) and minimum at the central neutral region",
      "Magnetic strength exists exclusively at the sharp corner edges"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A bar magnet acts as a magnetic dipole with two opposite poles (+m and -m) separated by magnetic length \\(2l\\).
The magnetic field lines emerge from the North pole and re-enter at the South pole:
- At the ends, field lines are intensely concentrated (high flux density \\(B = \\frac{\\Phi}{A}\\)), resulting in **maximum magnetic force**.
- At the central midpoint, the outward field from the North pole and the inward field from the South pole oppose each other along the surface, creating a **neutral zone** where net surface magnetic attraction drops to near zero.

### 2. Physical Context & Practical Illustration:
Sprinkling iron filings evenly over a bar magnet clearly demonstrates heavy filings clinging to the two ends (poles) and an empty neutral gap in the middle.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. The center has minimum strength, not maximum.
- **Option B**: Incorrect. Magnetic field strength is non-uniform along the axis.
- **Option C (Maximum at ends, minimum at center)**: Correct. Accurately describes dipole field geometry.
- **Option D**: Incorrect. The entire polar surface exerts strong attraction.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-017",
    text: "Atmospheric lightning during thunderstorms is scientifically caused by which electrical phenomenon?",
    options: [
      "Thermal combustion of atmospheric nitrogen",
      "Chemical electrolysis of airborne rain clouds",
      "Massive electric discharge of accumulated static electricity between clouds or between cloud and ground",
      "Nuclear fusion in storm cloud centers"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Inside cumulonimbus storm clouds, turbulent convection currents cause violent collisions between rising water droplets and falling ice crystals (graupel).
1. Frictional charge separation leaves the upper cloud positively charged and the cloud base strongly negatively charged.
2. The negative cloud base induces a dense positive charge on Earth's surface directly beneath it.
3. When the electric field exceeds the dielectric breakdown strength of air (\\(E > 3 \\times 10^6\\text{ V/m}\\)), air ionizes into conductive plasma.
4. An avalanche of electrons rushes through this ionized channel in a fraction of a millisecond as a massive **static electric spark discharge**.

### 2. Physical Context & Practical Illustration:
A typical lightning flash carries electrical currents of \\(30,000\\text{ Amperes}\\) at potentials of over \\(100\\) million Volts, heating the surrounding air to \\(30,000\\text{ K}\\) (hotter than the surface of the Sun), creating explosive acoustic shockwaves (thunder).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Nitrogen combustion)**: Incorrect. Nitrogen does not burn spontaneously.
- **Option B (Electrolysis)**: Incorrect. Electrolysis occurs in liquid ionic solutions, not vapor sparks.
- **Option C (Static electricity discharge)**: Correct. Gigantic dielectric breakdown discharge of static charge.
- **Option D (Nuclear fusion)**: Incorrect. Thunderstorms involve electrostatic forces, not nuclear reactions.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-018",
    text: "What happens to the magnetic properties of a permanent magnet when it is heated strongly above its Curie temperature?",
    options: [
      "It loses its permanent magnetism completely",
      "Its magnetic strength increases significantly",
      "Its magnetic poles invert directions",
      "Its magnetic field remains strictly unaffected"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In ferromagnetic materials, neighboring atomic magnetic moments are locked into parallel alignment within domains by quantum mechanical exchange forces.
Thermal energy increases the random thermal vibrations of the crystal lattice:
\\[
E_{\\text{thermal}} \\sim k_B T
\\]
When the temperature reaches and exceeds the **Curie temperature** (\\(T_C\\), which is \\(770^\\circ\\text{C}\\) for iron):
1. Thermal agitation completely overpowers the exchange coupling.
2. Domain structures collapse into completely randomized magnetic dipoles.
3. The material undergoes a phase transition from **ferromagnetic to paramagnetic**, losing its permanent remanent magnetism.

### 2. Physical Context & Practical Illustration:
Heating a magnetized steel needle over a candle flame to a dull red glow and letting it cool causes it to completely lose its ability to attract paperclips.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Loses magnetism)**: Correct. Thermal agitation destroys domain alignment.
- **Option B (Increases)**: Incorrect. Thermal agitation always degrades magnetic ordering.
- **Option C (Poles invert)**: Incorrect. Dipoles become random, not inverted.
- **Option D (Unaffected)**: Incorrect. Magnetism is highly temperature-dependent.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-019",
    text: "What is the primary function of a laboratory gold-leaf electroscope?",
    options: [
      "To measure electrical power in Watts",
      "To detect the presence and nature (sign) of electric charge on a body",
      "To generate high-voltage alternating current",
      "To measure electrical resistance in Ohms"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electroscope is an electrostatic instrument consisting of a metal terminal knob, conductive vertical rod, and two delicate metal leaves inside a glass enclosure.
- **Detecting Charge**: When a charged body touches the brass knob, charge conducts to the leaves. Because like charges repel (\\(F_e \\propto q_1 q_2\\)), the leaves diverge apart, proving the presence of charge.
- **Identifying Polarity**: If the electroscope is given a known positive charge (leaves diverge), bringing an unknown object near the knob will cause:
  - Greater divergence \\(\\implies\\) unknown object has **positive charge**.
  - Decreased divergence \\(\\implies\\) unknown object has **negative charge**.

### 2. Physical Context & Practical Illustration:
Electroscopes were the foundational instruments used by Michael Faraday and Marie Curie to detect ionizing radiation and discover electrostatic induction.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Power in Watts)**: Incorrect. Power is measured with a Wattmeter.
- **Option B (Detect presence and nature of charge)**: Correct. Standard physical purpose of an electroscope.
- **Option C (Generate AC)**: Incorrect. Dynamos/alternators generate AC.
- **Option D (Resistance in Ohms)**: Incorrect. Resistance is measured with an Ohmmeter.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-020",
    text: "Why does a freely suspended bar magnet always align itself in a geographic North-South direction when brought to rest?",
    options: [
      "Because the Sun's gravitational field pulls on magnetic poles",
      "Because cosmic solar winds push the magnet northward",
      "Because the Earth itself behaves like an enormous natural magnetic dipole",
      "Because the Earth's spherical shape forces mechanical alignment"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Earth possesses an internal geomagnetic field generated by the geodynamo effect—convection currents of molten iron and nickel in the outer core:
- Earth's magnetic dipole axis is inclined at approximately \\(11.3^\\circ\\) to its rotational axis.
- Near the geographic North Pole lies the Earth's **magnetic South pole**.
- Near the geographic South Pole lies the Earth's **magnetic North pole**.
By the fundamental law of magnetism, *unlike poles attract*:
- The North-seeking pole of a suspended bar magnet is attracted towards Earth's magnetic South pole (geographic North).
- The South-seeking pole is attracted towards Earth's magnetic North pole (geographic South).

### 2. Physical Context & Practical Illustration:
This directional behavior is the foundation of compass navigation, used by travelers for over a thousand years to navigate across Earth.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Sun's gravity)**: Incorrect. Gravity attracts mass, not magnetic polarity.
- **Option B (Solar winds)**: Incorrect. Solar winds are deflected by the magnetosphere and do not align needles.
- **Option C (Earth behaves as a magnet)**: Correct. Earth's geomagnetic field aligns the dipole needle.
- **Option D (Spherical shape)**: Incorrect. Geometry does not produce magnetic torque.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-021",
    text: "A magnetic substance that retains a high degree of remanent magnetization for a prolonged period after the external field is removed is called a:",
    options: [
      "Diamagnetic substance",
      "Temporary magnet",
      "Paramagnetic substance",
      "Permanent magnet"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic materials are characterized by their **magnetic hysteresis loop**:
- **Retentivity (Remanence, \\(B_r\\))**: The magnetic flux density remaining in the material when the magnetizing field \\(H\\) is reduced to zero.
- **Coercivity (\\(H_c\\))**: The reverse magnetic field required to demagnetize the material.
Materials with **high retentivity and high coercivity** (such as hardened carbon steel, Alnico, and neodymium alloys) resist demagnetization and retain their magnetic field indefinitely as **permanent magnets**.

### 2. Physical Context & Practical Illustration:
Permanent magnets are essential components in electric DC motors, bicycle dynamos, magnetic cabinet latches, and computer hard drives.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Diamagnetic)**: Incorrect. Diamagnetic substances develop zero remanent magnetism.
- **Option B (Temporary magnet)**: Incorrect. Temporary magnets (soft iron) lose their magnetism immediately when the field is removed.
- **Option C (Paramagnetic)**: Incorrect. Paramagnetic materials have zero remanence at room temperature.
- **Option D (Permanent magnet)**: Correct. Retains high magnetization and coercivity over long periods.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-022",
    text: "When an ebonite rod is vigorously rubbed with a dry woolen cloth, what type of electric charge is developed on the ebonite rod?",
    options: [
      "Positive charge",
      "Negative charge",
      "Neutral (zero charge)",
      "Alternating sinusoidal charge"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the **triboelectric series**, materials are ranked by their relative tendency to gain or lose electrons:
- Wool has a lower electron affinity and tends to lose electrons easily.
- Ebonite (vulcanized hard rubber) has a higher electron affinity and attracts electrons strongly.
When rubbed together:
1. Electrons are transferred from the outer atomic shells of wool molecules onto the ebonite rod.
2. Because electrons carry negative elementary charge (\\(e = -1.6 \\times 10^{-19}\\text{ C}\\)), the ebonite rod gains excess electrons, acquiring a net **negative charge**.
3. The woolen cloth loses electrons, acquiring an equal and opposite **positive charge**.

### 2. Physical Context & Practical Illustration:
In contrast, rubbing a smooth glass rod with silk causes electrons to transfer from glass to silk, leaving the glass rod with a *positive* charge.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Positive charge)**: Incorrect. Developed on glass rubbed with silk or on the woolen cloth.
- **Option B (Negative charge)**: Correct. Ebonite gains electrons from wool, becoming negatively charged.
- **Option C (Neutral)**: Incorrect. Frictional rubbing causes significant charge separation.
- **Option D (Alternating charge)**: Incorrect. Static charge is unidirectional DC.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-023",
    text: "What term is used in physics to describe the spatial region surrounding a magnet where its magnetic forces can be experienced by other magnets or moving charges?",
    options: [
      "Electric field",
      "Gravitational field",
      "Nuclear field",
      "Magnetic field"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **magnetic field** is a vector field \\(\\vec{B}\\) that surrounds magnetic dipoles and moving electric charges.
The magnetic Lorentz force exerted on a test charge \\(q\\) moving with velocity \\(\\vec{v}\\) within this region is:
\\[
\\vec{F}_m = q (\\vec{v} \\times \\vec{B})
\\]
The SI unit of magnetic field strength (magnetic flux density) is the **Tesla (\\(\\text{T}\\))** or \\(\\text{Weber/m}^2\\).

### 2. Physical Context & Practical Illustration:
Although invisible to the naked eye, the magnetic field can be mapped visually by spreading iron filings on a sheet of paper placed over a magnet. The filings align with magnetic field lines.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Electric field)**: Incorrect. Region of electrostatic force produced by electric charges (\\(\\vec{F} = q\\vec{E}\\)).
- **Option B (Gravitational field)**: Incorrect. Region of gravitational mass attraction (\\(\\vec{F} = m\\vec{g}\\)).
- **Option C (Nuclear field)**: Incorrect. Short-range subatomic interaction inside nuclei.
- **Option D (Magnetic field)**: Correct. Region of magnetic influence surrounding a magnet.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-024",
    text: "What is electrostatic induction?",
    options: [
      "The continuous flow of electric current through a closed circuit",
      "The magnetic attraction between unlike magnetic poles",
      "The redistribution of electric charges on a conductor caused by the nearby presence of a charged object without physical contact",
      "The chemical reaction occurring inside an electric battery"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
**Electrostatic induction** is the phenomenon where a charged object induces temporary charge separation in a nearby neutral conducting body without touching it:
1. When a negatively charged rod is brought close to a neutral metal sphere, free conduction electrons inside the metal are repelled to the far side.
2. The near surface is left with a deficiency of electrons (net positive bound charge).
3. The far surface accumulates excess electrons (net negative free charge).
4. Total net charge on the sphere remains strictly zero:
\\[
Q_{\\text{total}} = q_{\\text{near}} + q_{\\text{far}} = (+q) + (-q) = 0
\\]

### 2. Physical Context & Practical Illustration:
Electrostatic induction is how charged objects attract neutral objects (e.g., a charged comb attracting neutral bits of paper) and how photocopiers and electrostatic precipitators function.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Current flow)**: Incorrect. That is dynamic conduction, not static induction.
- **Option B (Magnetic attraction)**: Incorrect. That is magnetism.
- **Option C (Charge redistribution without contact)**: Correct. Exact definition of electrostatic induction.
- **Option D (Chemical reaction)**: Incorrect. That is electrochemical action.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-025",
    text: "Which of the following statements correctly characterizes the operation of an electromagnet?",
    options: [
      "It is a permanent magnet that cannot be switched off",
      "It behaves as a magnet only when there is zero electric current",
      "It behaves as a strong magnet exclusively while electric current flows through its coil",
      "It generates a magnetic field using nuclear decay"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An **electromagnet** consists of an insulated wire coil (solenoid) wound around a soft iron core.
By Ampere's Law, the magnetic field \\(B\\) generated inside an ideal solenoid is:
\\[
B = \\mu_r \\mu_0 n I
\\]
where \\(n\\) is turns per meter, \\(I\\) is current, and \\(\\mu_r\\) is the relative permeability of the iron core.
- When current \\(I > 0\\), a powerful magnetic field is generated instantly.
- Because soft iron has low magnetic retentivity, when current is switched off (\\(I = 0\\)), the magnetic field vanishes almost immediately.
Thus, it is a controllable **temporary magnet**.

### 2. Physical Context & Practical Illustration:
Industrial junkyard cranes use massive electromagnets to lift several tons of scrap steel, then drop the scrap instantly simply by flipping a switch to shut off the electric current.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Permanent magnet)**: Incorrect. Electromagnets lose magnetism when current ceases.
- **Option B (Magnet when current is zero)**: Incorrect. Magnetic field requires current flow.
- **Option C (Magnet while current flows)**: Correct. Magnetic field is directly produced and controlled by the flowing electric current.
- **Option D (Nuclear decay)**: Incorrect. Electromagnets are driven by electrical current, not radioactivity.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-026",
    text: "A commercial dry cell (Leclanché dry cell) used in torches and wall clocks consists of which terminal configuration?",
    options: [
      "Two positive terminals and zero negative terminals",
      "Two negative terminals and zero positive terminals",
      "One positive terminal (carbon/brass cap) and one negative terminal (zinc metal base)",
      "Three separate alternating current terminals"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A standard 1.5 V Leclanché dry cell is an electrochemical cell consisting of:
- **Cathode (Positive terminal)**: A central carbon (graphite) rod capped with a brass contact at the top, surrounded by a paste of manganese dioxide (\\(\\text{MnO}_2\\)) and carbon powder.
- **Anode (Negative terminal)**: The outer cylindrical zinc (\\(\\text{Zn}\\)) metal container forming the base.
- **Electrolyte**: A moist ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) and zinc chloride (\\(\\text{ZnCl}_2\\)) paste.
During spontaneous chemical oxidation-reduction, electrons flow externally from the zinc negative terminal to the carbon positive terminal:
\\[
\\text{EMF} \\approx 1.5\\text{ Volts}
\\]

### 2. Physical Context & Practical Illustration:
Standard AA and AAA dry cells power remote controls, clocks, and flashlights with a reliable direct-current (DC) voltage of \\(1.5\\text{ V}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A & B**: Incorrect. Every functional DC electrochemical cell requires both a positive and a negative pole.
- **Option C (One positive, one negative)**: Correct. Carbon rod is positive, zinc casing is negative.
- **Option D**: Incorrect. Dry cells produce single-voltage DC, not multi-phase AC.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-027",
    text: "Small, disc-shaped electrochemical cells commonly used to power wristwatches, hearing aids, and calculators are widely known as:",
    options: [
      "Solar photovoltaic cells",
      "Button cells (coin cells)",
      "Lead-acid wet cells",
      "Industrial dynamos"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **button cell** (also known as a **coin cell**) is a compact, miniature single-cell electrochemical battery shaped like a flat button or coin:
- Typically utilize lithium chemistry (e.g. \\(\\text{CR2032}\\), \\(3.0\\text{ V}\\)) or silver oxide / zinc-air chemistry (\\(1.55\\text{ V}\\)).
- The top stainless steel cap is usually connected to the negative electrode, while the outer can forms the positive terminal.
- Offer high energy density, extremely low self-discharge rates, and long shelf life for low-drain miniature electronics.

### 2. Physical Context & Practical Illustration:
Because of their tiny footprint and light weight, button cells power electronic car key fobs, computer BIOS memory, digital clinical thermometers, and wristwatches for years without replacement.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Solar cells)**: Incorrect. Solar cells convert light into electricity; button cells are chemical batteries.
- **Option B (Button cells)**: Correct. Common commercial name for compact disc/coin-shaped cells.
- **Option C (Lead-acid cells)**: Incorrect. Heavy, liquid-electrolyte automotive batteries.
- **Option D (Dynamos)**: Incorrect. Rotating mechanical electromagnetic generators.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-028",
    text: "In standard electrical circuit schematic diagrams, a symbol consisting of two bracket curves enclosing a central dot \\((\\cdot)\\) represents which component?",
    options: [
      "An open switch / plug key",
      "An incandescent electric bulb",
      "A closed switch / plug key",
      "A variable resistor (rheostat)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In electrical engineering schematic standards:
- **Open Plug Key / Switch**: Represented by empty brackets without a dot:
\\[
---(\\quad)---
\\]
Because the circuit is open (broken), resistance is infinite and current is zero (\\(I = 0\\)).
- **Closed Plug Key / Switch**: Represented by brackets containing a central dot:
\\[
---(\\cdot)---
\\]
The dot symbolizes the insertion of the brass contact plug, completing the conducting path and allowing electric current to flow through the circuit.

### 2. Physical Context & Practical Illustration:
Laboratory physics experiments with Ohm's law apparatus use brass plug keys where inserting the metal plug closes the circuit, enabling current to pass through the ammeter and test resistor.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Open switch)**: Incorrect. An open switch has empty brackets \\(---(\\quad)---\\).
- **Option B (Bulb)**: Incorrect. An electric bulb is symbolized by a looped filament inside a circle.
- **Option C (Closed switch / plug key)**: Correct. Brackets with a dot denote a closed conducting key.
- **Option D (Variable resistor)**: Incorrect. A zigzag line with a crossing diagonal arrow.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-029",
    text: "In electrical physics, electric current in a metallic wire is fundamentally defined as the rate of flow of:",
    options: [
      "Atomic mass",
      "Free conduction electrons (electric charge)",
      "Stationary atomic nuclei",
      "Thermal phonons"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electric current \\(I\\) is defined as the net rate of flow of electric charge \\(Q\\) through a cross-section of a conductor per unit time:
\\[
I = \\frac{\\Delta Q}{\\Delta t} = \\frac{n e A v_d}{\\Delta t}
\\]
In solid metallic conductors:
1. Positive atomic nuclei are anchored rigidly in the crystal lattice.
2. The outer valence electrons are delocalized and form a 'sea' of **free conduction electrons**.
3. Applying an electric potential difference creates an electric field that causes these free electrons to drift with drift velocity \\(v_d\\), constituting the electric current.

### 2. Physical Context & Practical Illustration:
By historical convention, conventional current is defined in the direction positive charges would move (from positive to negative potential), which is directly opposite to the physical drift direction of negatively charged electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Atomic mass)**: Incorrect. Matter does not transfer along wires; only electrons drift.
- **Option B (Free conduction electrons)**: Correct. The mobile charge carriers in metals are free electrons.
- **Option C (Stationary nuclei)**: Incorrect. Heavy protons are fixed in the metallic lattice.
- **Option D (Thermal phonons)**: Incorrect. Phonons are quantized lattice vibrations governing heat conduction.`
  },
  {
    id: "MH-9-SCIT-3-3.1-OSC-030",
    text: "Which of the following physical characteristics is essential for a domestic electric fuse wire?",
    options: [
      "High melting point and high electrical resistivity",
      "Low melting point and low electrical resistance",
      "High melting point and zero electrical resistance",
      "Low melting point and relatively high electrical resistivity compared to copper supply cables"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A fuse wire serves as the sacrificial weak link in an electric circuit.
1. **Low Melting Point**: Made of an alloy of tin and lead (\\(63\\%\\,\\text{Sn} + 37\\%\\,\\text{Pb}\\)), having a low melting temperature (\\(\\approx 183^\\circ\\text{C}\\) to \\(200^\\circ\\text{C}\\)).
2. **Relatively High Resistivity**: Its resistance per unit length is higher than the heavy copper house wiring:
\\[
H = I^2 R t
\\]
During a fault or overcurrent surge, heat generation \\(H\\) in the fuse wire rapidly exceeds heat dissipation, safely melting the fuse wire and interrupting the circuit *before* the copper supply cables heat up or catch fire.

### 2. Physical Context & Practical Illustration:
If an amateur electrician dangerously replaces a blown fuse with a thick copper wire, the copper wire will not melt during a short circuit; instead, the wiring inside the walls will overheat and ignite building fires.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. A high melting point would prevent the fuse from melting during an overload.
- **Option B**: Incorrect. The fuse wire needs enough resistance to heat up before the copper feed lines.
- **Option C**: Incorrect. Zero resistance produces zero Joule heating (\\(I^2 R = 0\\)), so it would never melt.
- **Option D (Low melting point, appropriate resistivity)**: Correct. Ensures fast, safe thermal melting under overcurrent.`
  }
];
