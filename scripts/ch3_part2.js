// scripts/ch3_part2.js - Chapter 3 (Current Electricity) Questions 31-60 Gold Standard Enhancements
const ch3_part2 = [
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-031",
    text: "Which of the following physical fields exist in the space surrounding an electron moving with a steady velocity?",
    options: [
      "Only an electrostatic field",
      "Only a magnetic field",
      "Both an electric field and a magnetic field",
      "Neither electric nor magnetic field"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electron possesses an intrinsic negative electric charge (\\(q_e = -1.6 \\times 10^{-19}\\text{ C}\\)).
1. **Electric Field (\\(\\mathbf{E}\\))**: Because the electron carries electric charge, it always establishes a radial Coulomb electric field around itself:
\\[
\\mathbf{E} = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q}{r^2} \\hat{r}
\\]
2. **Magnetic Field (\\(\\mathbf{B}\\))**: When the electron moves with velocity \\(\\mathbf{v}\\), this motion constitutes a microscopic electric current element (\\(I d\\mathbf{l} = q \\mathbf{v}\\)), generating a surrounding magnetic field according to the Biot-Savart Law:
\\[
\\mathbf{B} = \\frac{\\mu_0}{4\\pi} \\frac{q (\\mathbf{v} \\times \\hat{r})}{r^2}
\\]
Therefore, a moving charge carrier produces **both an electric field and a magnetic field**.

### 2. Physical Context & Practical Illustration:
A stationary charge produces only an electric field. The moment it accelerates or drifts (such as conduction electrons flowing through a copper wire), its motion creates a surrounding magnetic field that can deflect a magnetic compass needle while maintaining its electric force interactions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: An electric field exists, but a moving charge also generates a magnetic field.
- **Option B is incorrect**: The intrinsic charge does not disappear during motion; the electric field persists.
- **Option C is correct**: A moving electron generates both an electric field (due to charge) and a magnetic field (due to motion).
- **Option D is incorrect**: Both fundamental electromagnetic fields are present.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-032",
    text: "How does the intensity of the magnetic field vary around a permanent bar magnet?",
    options: [
      "It is maximum at the poles and minimum at the neutral center",
      "It is completely uniform at all points around the magnet",
      "It is maximum at the geometric center and zero at the poles",
      "It is stronger along the broadside than near the pole tips"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The strength of a magnetic field is directly proportional to the spatial density of magnetic lines of force (magnetic flux density, \\(B = \\Phi / A\\)):
- At the **poles** of a bar magnet, magnetic field lines converge densely as they emerge from the North pole and enter the South pole, producing maximum field intensity:
\\[
B_{\\text{pole}} \\approx \\frac{\\mu_0}{4\\pi} \\frac{2M}{r^3} \\quad (\\text{axial maximum})
\\]
- At the **center** between the two opposite poles, the magnetic fields created by the North and South poles oppose each other, resulting in a neutral zone with minimum field strength.

### 2. Physical Context & Practical Illustration:
When a bar magnet is dipped into a tray of iron filings, dense bushy clusters of filings cling to the two ends (poles), while virtually no filings stick to the middle section, visually proving field concentration at the poles.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The magnetic field is strongest at the poles where field lines are most concentrated, and weakest at the neutral center.
- **Option B is incorrect**: The field is non-uniform; field density drops sharply with distance.
- **Option C is incorrect**: Inverts the physical reality; the center is the neutral zone.
- **Option D is incorrect**: The axial field at the poles is twice as strong as the equatorial broadside field for the same distance.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-033",
    text: "In an open electrical circuit where no current flows, which component is intentionally placed in the open state?",
    options: [
      "The switch (or plug key)",
      "The chemical cell (battery)",
      "The connecting copper wire",
      "The electric load (lamp)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric circuit requires a continuous, unbroken conducting loop for electrons to circulate under a potential difference. According to Ohm's Law:
\\[
I = \\frac{V}{R_{\\text{circuit}}}
\\]
When the **switch (key)** is open:
- An air gap of very high dielectric resistance (\\(R_{\\text{switch}} \\to \\infty\\)) is introduced into the circuit.
- The total loop resistance approaches infinity, reducing the current to zero (\\(I = 0\\)).
The switch is specifically designed to safely make (close) or break (open) the conducting path on demand.

### 2. Physical Context & Practical Illustration:
A wall switch operates by physically separating two spring-loaded metal contacts. When turned 'OFF', the contacts separate, creating an air gap that halts current to appliances without disconnecting the internal wiring.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The switch or plug key is the control element kept open to prevent current flow in an open circuit.
- **Option B is incorrect**: The cell remains chemically active; opening a cell would mean physically destroying it.
- **Option C is incorrect**: Wires remain physically connected to terminals.
- **Option D is incorrect**: The load remains intact; it simply cannot operate without current.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-034",
    text: "On which fundamental physical principle is the operation of an electric generator (dynamo) based?",
    options: [
      "Electromagnetic induction",
      "Magnetic effect of electric current",
      "Joule's heating effect of current",
      "Chemical effect of electric current"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric generator (dynamo) converts mechanical energy into electrical energy based on **Faraday's Law of Electromagnetic Induction**:
\\[
\\mathcal{E} = -N \\frac{d\\Phi_B}{dt} = -N \\frac{d}{dt}(B A \\cos\\omega t) = N B A \\omega \\sin\\omega t
\\]
When a conducting armature coil rotates within a uniform magnetic field, the magnetic flux (\\(\\Phi_B\\)) linking the coil changes continuously over time, inducing an alternating electromotive force (EMF) that drives an electric current through the external circuit.

### 2. Physical Context & Practical Illustration:
In hydroelectric and thermal power stations, massive turbines rotate coils inside powerful electromagnets. Bicycle dynamos use the same principle on a small scale: rotating a permanent magnet near a stationary coil to generate electricity for the bicycle headlamp.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Dynamos operate via electromagnetic induction, generating electric current from changing magnetic flux.
- **Option B is incorrect**: The magnetic effect of current (Oersted's principle) is the basis of electric motors and electromagnets, converting electrical energy into mechanical force.
- **Option C is incorrect**: The heating effect is used in heaters and toasters.
- **Option D is incorrect**: The chemical effect is used in electroplating and batteries.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-035",
    text: "Which of the following statements is NOT TRUE regarding static electricity?",
    options: [
      "Static electric charges are localized and do not flow continuously like current electricity",
      "Static charges are generated through friction, conduction, or induction",
      "Accumulated static charges on insulators dissipate over time due to atmospheric humidity",
      "Static electricity cannot establish an electric field in the surrounding space"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Static electricity involves stationary electric charges accumulated on the surface of dielectric insulators or isolated conductors:
1. **Coulomb's Law & Electric Field**: Any stationary electric charge \\(Q\\) fundamentally establishes an electrostatic field \\(\\mathbf{E}\\) in its surrounding space:
\\[
\\mathbf{E} = \\frac{1}{4\\pi\\varepsilon_0} \\frac{Q}{r^2} \\hat{r} \\neq 0
\\]
Therefore, claiming static electricity cannot produce an electric field is fundamentally false!
2. Static charges produce observable electrostatic forces (attracting bits of paper) precisely because of the electric field they create.

### 2. Physical Context & Practical Illustration:
When a plastic comb is rubbed through dry hair, it acquires static charge. Holding it near small scraps of paper exerts an electrostatic attractive force across empty air, proving the active presence of an surrounding electric field.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a true statement**: Static electricity consists of stationary, non-circulating charges.
- **Option B is a true statement**: Charges are transferred by triboelectric friction, direct contact, or induction.
- **Option C is a true statement**: Airborne moisture film conducts static charges away.
- **Option D is incorrect (the correct answer to the question)**: Asserting that static electricity cannot create an electric field is false; all charges generate electric fields.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-036",
    text: "Which of the following descriptions accurately defines the phenomenon of electromagnetic induction?",
    options: [
      "The generation of a static electric charge on an insulator through mechanical friction",
      "The alignment of magnetic domains inside soft iron by a steady direct current",
      "The generation of an electromotive force and electric current in a conductor due to changing magnetic flux",
      "The heating of a conductor due to resistance when an electric current passes through it"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electromagnetic induction is the physical phenomenon discovered by Michael Faraday in 1831:
- Whenever the magnetic flux (\\(\\Phi_B\\)) linking an electric circuit changes with time, an induced electromotive force (EMF, \\(\\mathcal{E}\\)) is produced in the circuit:
\\[
\\mathcal{E} = -\\frac{d\\Phi_B}{dt}
\\]
- If the circuit is closed, this induced EMF causes an induced electric current to circulate, whose direction opposes the change in flux according to Lenz's Law.

### 2. Physical Context & Practical Illustration:
Moving a bar magnet rapidly into and out of a wire coil connected to a galvanometer causes the needle to deflect back and forth. No battery is present; the relative motion between the magnetic field and the coil directly induces current.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: This describes triboelectric charging (static electricity).
- **Option B is incorrect**: This describes magnetization (electromagnetism).
- **Option C is correct**: Electromagnetic induction is the production of electric current by changing magnetic flux.
- **Option D is incorrect**: This describes Joule heating.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-037",
    text: "The operational lifespan and energy capacity of an electrochemical cell (battery) primarily depends upon:",
    options: [
      "The physical external color and packaging of the cell",
      "The atmospheric pressure of the surrounding room",
      "The quantity of active chemical reactants and the rate of internal chemical reactions",
      "The length of connecting wires attached to the battery terminals"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electrochemical cell stores electrical energy in the form of chemical potential energy:
\\[
\\text{Total Charge Capacity } Q = \\int I dt = n F \\left(\\frac{m}{M}\\right)
\\]
where:
- \\(n\\) = number of electrons transferred per reaction
- \\(F\\) = Faraday's constant (\\(\\approx 96485\\text{ C/mol}\\))
- \\(m\\) = mass of active electrochemical material (e.g., Zinc, \\(\\text{MnO}_2\\))
- \\(M\\) = molar mass of active reactant
The operating life depends strictly on the mass of active reactants available and the rate at which redox reactions proceed to exhaustion.

### 2. Physical Context & Practical Illustration:
A larger D-size cell lasts much longer than a AAA-size cell even though both deliver the same open-circuit potential of \\(1.5\\text{ V}\\). The D cell contains a much greater quantity of active zinc and manganese dioxide paste, allowing it to supply current for far more hours.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Packaging and casing color are superficial and do not affect electrochemical capacity.
- **Option B is incorrect**: Standard atmospheric pressure variations have negligible impact on sealed cells.
- **Option C is correct**: Lifespan is governed by the mass of chemical reactants and their redox reaction rates.
- **Option D is incorrect**: Wire length affects external resistance, not internal chemical capacity.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-038",
    text: "In which of the following advanced medical diagnostic instruments are powerful superconducting magnets utilized?",
    options: [
      "Stethoscope",
      "Electrocardiogram (ECG)",
      "Ultrasound sonography machine",
      "Magnetic Resonance Imaging (MRI) machine"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic Resonance Imaging (MRI) relies on nuclear magnetic resonance (NMR) of hydrogen nuclei (protons):
1. A powerful uniform magnetic field (typically \\(1.5\\text{ T to } 3.0\\text{ T}\\)) generated by superconducting electromagnet coils aligns the magnetic dipoles of protons in water molecules throughout the human body.
2. Radiofrequency (RF) pulses are applied at the Larmor precession frequency:
\\[
\\omega_0 = \\gamma B_0
\\]
3. When the RF pulse terminates, protons relax back to alignment, emitting radio signals picked up by receiver coils to reconstruct high-resolution cross-sectional anatomical images.

### 2. Physical Context & Practical Illustration:
Superconducting electromagnets in MRI scanners are cooled by liquid helium to \\(-269^\\circ\\text{C}\\) (\\(4\\text{ K}\\)) to eliminate electrical resistance, allowing thousands of Amperes to circulate without power dissipation, sustaining intense magnetic fields.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A stethoscope is a purely acoustic instrument for listening to internal heart and lung sounds.
- **Option B is incorrect**: An ECG records natural electrical bio-potentials of heart contractions using surface skin electrodes.
- **Option C is incorrect**: Ultrasound sonography utilizes high-frequency acoustic waves and piezoelectric transducers.
- **Option D is correct**: MRI scanners employ powerful magnets to align nuclear spins for medical diagnostic imaging.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-039",
    text: "An electromagnet is an essential operating component in which of the following everyday devices?",
    options: [
      "Magnetic compass needle",
      "Electric toaster heating element",
      "Audio loudspeaker",
      "Mercury glass thermometer"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An audio loudspeaker converts electrical audio signals into mechanical sound waves using the interaction between a permanent magnet and an electromagnet (voice coil):
\\[
\\mathbf{F} = I (\\mathbf{l} \\times \\mathbf{B})
\\]
1. An alternating audio signal current \\(I(t)\\) passes through a light wire coil (electromagnet) suspended in the cylindrical magnetic gap of a permanent magnet.
2. The Lorentz force causes the coil to oscillate rapidly backward and forward in synchrony with the audio frequency.
3. The coil is attached to a flexible paper/polypropylene cone that vibrates the surrounding air, producing acoustic sound waves.

### 2. Physical Context & Practical Illustration:
Electromagnets are indispensable wherever variable, controllable mechanical motion must be driven by an electric signal—such as loudspeakers, relays, electric bells, and maglev trains.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A compass needle uses a permanent magnet, not an electromagnet.
- **Option B is incorrect**: An electric toaster relies on resistive Joule heating (Nichrome), not magnetic fields.
- **Option C is correct**: Loudspeakers utilize an electromagnet voice-coil to vibrate the speaker diaphragm.
- **Option D is incorrect**: A glass thermometer operates on thermal volumetric expansion of liquid mercury.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-040",
    text: "Which of the following electrical appliances does NOT contain a high-resistance heating filament?",
    options: [
      "Incandescent light bulb",
      "Electric iron",
      "Electric geyser (water heater)",
      "Electromagnetic doorbell"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Appliances designed to generate heat or light through Joule heating (\\(H = I^2 R t\\)) require high-resistance filaments or heating elements:
- **Incandescent bulb**: Contains a coiled fine tungsten filament heated to \\(> 2500^\\circ\\text{C}\\) to glow white-hot.
- **Electric iron & Geyser**: Contain thick Nichrome heating elements that convert electrical power into thermal energy.
In contrast, an **electromagnetic doorbell** operates on the magnetic effect of electric current. It contains an electromagnet coil made of low-resistance insulated copper wire wound around a soft iron core to maximize magnetic flux while minimizing heat generation.

### 2. Physical Context & Practical Illustration:
A doorbell's coil is designed to avoid heating; generating significant heat would waste energy and risk melting the coil insulation. Its sole purpose is to produce a magnetic field that moves the striker hammer.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Incandescent bulbs contain a tungsten filament.
- **Option B is incorrect**: Electric irons contain a Nichrome heating element.
- **Option C is incorrect**: Electric geysers contain an immersed Nichrome heating element.
- **Option D is correct**: An electromagnetic doorbell has an electromagnet coil, not a heating filament.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-041",
    text: "Which of the following household devices utilizes an active magnetic mechanism to function?",
    options: [
      "Electric doorbell",
      "Wax candle",
      "Wooden matchstick",
      "Kerosene lantern"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric doorbell relies on an **electromagnet** operating via the magnetic effect of electric current. When the circuit closes, current circulates through copper coils wound on a soft iron core, creating an attractive magnetic field:
\\[
B = \\mu n I
\\]
This magnetic force attracts a spring-loaded soft iron armature, causing the striker to strike the chime bar or gong.

### 2. Physical Context & Practical Illustration:
Candles, matchsticks, and kerosene lamps are combustion-based lighting devices operating through chemical oxidation reactions (hydrocarbons combining with oxygen). None contain magnetic materials or generate magnetic fields.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The electric doorbell employs an electromagnet to mechanically actuate the hammer.
- **Option B is incorrect**: A candle produces light via paraffin wax combustion.
- **Option C is incorrect**: A matchstick ignites phosphorus/sulfur via friction.
- **Option D is incorrect**: A kerosene lantern produces flame through fuel combustion.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-042",
    text: "In an electric circuit schematic diagram, which component is represented by parallel lines of unequal lengths (a longer thin line and a shorter thicker line)?",
    options: [
      "An electric bulb",
      "An electric cell (or battery)",
      "A closed plug key",
      "A fixed resistor"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In standard electrical schematic diagrams:
- **Electric Cell**: Represented by two parallel vertical lines of unequal lengths and thicknesses:
  - The **longer, thinner line** represents the **positive terminal** (higher potential, \\(V_+\\)).
  - The **shorter, thicker line** represents the **negative terminal** (lower potential, \\(V_-\\)).
- A combination of multiple such pairs connected in series represents a **battery**.

### 2. Physical Context & Practical Illustration:
Standard circuit schematic symbols provide a universal blueprint language across electrical engineering: a zigzag line represents a resistor, a circle with an encircled cross represents an incandescent lamp, and bracketed dots represent keys/switches.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: An electric bulb is represented by a circle containing a looped filament wire or an 'X'.
- **Option B is correct**: An electric cell is represented by two parallel lines of different heights (long positive, short negative).
- **Option C is incorrect**: A closed plug key is represented by parentheses with a central dot: \\((\\cdot)\\).
- **Option D is incorrect**: A resistor is represented by a continuous zigzag line.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-043",
    text: "In a gold leaf electroscope, the divergence between the gold leaves increases when a positively charged rod is brought close to the brass disc without touching it. What is the nature of the charge originally present on the electroscope?",
    options: [
      "Negative charge",
      "Zero charge (neutral)",
      "Charge of any arbitrary polarity",
      "Positive charge"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Consider an electroscope that is already charged:
1. **Electrostatic Induction**: Bringing a positively charged rod (+ve) near the brass cap attracts negative conduction electrons from the leaves up toward the cap:
\\[
\\mathbf{F}_e = -e \\mathbf{E}_{\\text{rod}} \\quad (\\text{directed upward toward the positive rod})
\\]
2. **Deficit at the Leaves**: This upward electron migration leaves the gold leaves with an increased deficit of electrons, making the leaves **more positively charged**:
\\[
Q_{\\text{leaves}}' = Q_{\\text{leaves}} + \\Delta Q_+
\\]
3. **Leaf Divergence**:
   - If the electroscope was originally **positive**, adding more positive charge increases electrostatic repulsion, causing the leaves to **diverge further**.
   - If it had been negative, the positive deficit would neutralize the negative charge, causing the leaves to collapse.
Therefore, increased divergence confirms the electroscope was originally **positively charged**.

### 2. Physical Context & Practical Illustration:
This test is the standard electrostatic diagnostic method: an increase in divergence when like polarity approaches proves that the electroscope and the inducing rod share identical charge polarities.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: If the electroscope were negative, bringing a positive rod would draw electrons to the top, reducing leaf charge and causing the leaves to collapse.
- **Option B is incorrect**: On a neutral electroscope, divergence occurs from zero, but the question specifies the divergence *increases* from an existing spread.
- **Option C is incorrect**: The response is strictly polarity-dependent.
- **Option D is correct**: The leaves diverge further only if the electroscope already carried like positive charge.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-044",
    text: "What type of electric current is delivered by a standard dry pencil cell (AA / AAA battery)?",
    options: [
      "Alternating current (AC) with variable frequency",
      "Direct current (DC) flowing unidirectionally",
      "High-frequency radio pulse current",
      "Neutral oscillating current"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electrochemical cell generates electrical energy from spontaneous internal chemical redox reactions:
- The chemical potential difference between the cathode (+ve terminal) and anode (-ve terminal) maintains a steady, fixed polarity:
\\[
V(t) = V_0 = \\text{constant}
\\]
- In an external closed circuit, charge carriers move unidirectionally from the negative terminal to the positive terminal (conventional current from + to -).
Current whose magnitude and direction remain unidirectional over time is called **Direct Current (DC)**.

### 2. Physical Context & Practical Illustration:
Household wall outlets provide Alternating Current (AC) at \\(50\\text{ Hz}\\) (where current reverses direction 100 times per second). In contrast, chemical batteries (pencil cells, coin cells, lead-acid batteries) supply pure, steady Direct Current (DC).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Alternating current periodically reverses direction; batteries produce unidirectional current.
- **Option B is correct**: Chemical cells produce Direct Current (DC) with fixed polarity and unidirectional flow.
- **Option C is incorrect**: Radio pulse currents are generated by high-frequency electronic oscillators, not dry cells.
- **Option D is incorrect**: 'Neutral oscillating current' is a non-existent physical concept.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-045",
    text: "What information does the Right-Hand Thumb Rule provide for a straight current-carrying conductor?",
    options: [
      "The magnitude of gravitational pull on the wire",
      "The frequency of alternating current in the circuit",
      "The direction of circular magnetic field lines around the conductor",
      "The electrical resistance of the conducting material"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Maxwell's Right-Hand Thumb Rule (corkscrew rule) defines the spatial orientation of magnetic field lines produced by electric current:
\\[
\\mathbf{B} = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\phi}
\\]
- **Rule Statement**: Imagine holding a straight current-carrying conductor in your right hand such that the outstretched thumb points in the direction of conventional electric current (\\(I\\)).
- Then, the curled fingers encircling the conductor point in the direction of the concentric **magnetic lines of force**.

### 2. Physical Context & Practical Illustration:
If current flows vertically upward through a straight vertical wire, pointing your right thumb upward causes your fingers to encircle the wire in an anticlockwise direction as viewed from above, precisely matching the deflection direction of compass needles placed around the wire.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Gravitational forces are unrelated to the right-hand thumb rule.
- **Option B is incorrect**: Frequency is a temporal property of AC sources, not determined by hand rules.
- **Option C is correct**: The right-hand thumb rule determines the direction of magnetic field lines around a current-carrying wire.
- **Option D is incorrect**: Resistance is determined by material resistivity and dimensions (\\(R = \\rho l / A\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-046",
    text: "The magnetic field strength of an electromagnet depends upon which of the following physical factors?",
    options: [
      "The number of turns per unit length in the coil",
      "The magnitude of electric current circulating through the coil",
      "The magnetic permeability of the core material placed inside the coil",
      "All of the above factors"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The magnetic flux density (\\(B\\)) inside an electromagnet solenoid is governed by:
\\[
B = \\mu n I = \\mu_0 \\mu_r \\left(\\frac{N}{L}\\right) I
\\]
where:
1. \\(n = N/L\\): Number of turns of wire per unit length (\\(B \\propto n\\)).
2. \\(I\\): Current flowing through the winding (\\(B \\propto I\\)).
3. \\(\\mu = \\mu_0 \\mu_r\\): Magnetic permeability of the core material. Inserting a soft iron core (\\(\\mu_r > 1000\\)) multiplies the field intensity by several thousand times compared to an air core.

### 2. Physical Context & Practical Illustration:
To build a powerful industrial scrap-metal lifting electromagnet, engineers maximize all three factors: they wind thousands of copper turns, supply heavy direct currents (hundreds of Amperes), and employ high-permeability soft iron alloy cores.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is partially correct**: Field strength increases with turn density, but it also depends on current and core material.
- **Option B is partially correct**: Field strength increases with current, but turn count and core are also critical.
- **Option C is partially correct**: High permeability boosts field strength, but turns and current are equally required.
- **Option D is correct**: The magnetic field strength depends comprehensively on the number of turns, current magnitude, and core material.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-047",
    text: "What is the net effective magnetic strength (flux density) at the exact geometric center of a uniformly magnetized bar magnet?",
    options: [
      "Equal to 100% of the pole strength",
      "Equal to 50% of the pole strength",
      "Practically zero (neutral zone)",
      "Twice the magnetic pole strength"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A bar magnet comprises two equal and opposite magnetic poles separated by magnetic length \\(2l\\):
- At the exact center midway between the poles (\\(x = 0\\)), the magnetic field lines emerging from the North pole and those returning to the South pole run internally parallel to the magnet's axis:
- The external surface magnetic force is zero because opposite pole influences balance each other out:
\\[
F_{\\text{ext}} \\approx 0
\\]
This mid-plane is called the **neutral region** or neutral zone of the magnet.

### 2. Physical Context & Practical Illustration:
If an iron nail or paper clip is brought near the exact middle of a bar magnet, it experiences no noticeable magnetic attraction and fails to stick. All attraction is concentrated at the two extreme ends (poles).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The magnetic strength at the center is nowhere near 100% of the poles.
- **Option B is incorrect**: It is not 50%; external attractive force drops to zero.
- **Option C is correct**: The center of a bar magnet is a neutral zone where external magnetism is practically zero.
- **Option D is incorrect**: The center cannot have greater field strength than the poles.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-048",
    text: "In domestic electricity billing, what exact quantity of electrical energy corresponds to '1 unit' of consumption?",
    options: [
      "\\(1\\text{ Watt-hour (Wh)}\\)",
      "\\(1\\text{ Kilowatt-hour (kWh)}\\)",
      "\\(1\\text{ Joule (J)}\\)",
      "\\(1\\text{ Megawatt-second (MW}\\cdot\\text{s)}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In commercial and domestic power distribution, the billing unit is the Board of Trade Unit (B.O.T.U.), universally referred to as **1 unit**:
\\[
1\\text{ commercial unit} = 1\\text{ kilowatt-hour (kWh)}
\\]
Converting to SI base units of energy (Joules):
\\[
1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6\\text{ Joules} = 3.6\\text{ MJ}
\\]
Because domestic appliances consume millions of Joules each day, electric utility meters measure energy in kilowatt-hours rather than Joules.

### 2. Physical Context & Practical Illustration:
Operating a \\(100\\text{ W}\\) television for \\(10\\text{ hours}\\) consumes:
\\[
E = 100\\text{ W} \\times 10\\text{ h} = 1000\\text{ Wh} = 1\\text{ kWh} = 1\\text{ unit}
\\]
If the electricity tariff is ₹6.00 per unit, the cost to run the television for 10 hours is exactly ₹6.00.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A watt-hour is only \\(1/1000\\) of a commercial unit (\\(3600\\text{ J}\\)).
- **Option B is correct**: One unit of electricity is defined as one kilowatt-hour (\\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}\\)).
- **Option C is incorrect**: One Joule is an extremely tiny amount of energy (1 watt-second).
- **Option D is incorrect**: Megawatt-second is an unconventional non-commercial unit.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-049",
    text: "Which of the following electrochemical cells is a secondary (rechargeable) cell?",
    options: [
      "Standard Leclanché dry cell",
      "Alkaline zinc-manganese dioxide cell",
      "Nickel-Cadmium (Ni-Cd) cell",
      "Daniell copper-zinc cell"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrochemical cells are categorized into two classes based on thermodynamic reversibility:
1. **Primary Cells**: Internal redox reactions are non-reversible; once reactants (e.g. Zinc anode) are chemically consumed, the cell is exhausted and cannot be recharged (e.g., Dry cell, Daniell cell).
2. **Secondary Cells**: The electrode reactions are chemically reversible. Passing a direct current in the reverse direction restores the original chemical reactants:
\\[
\\text{Cd} + 2\\text{NiO(OH)} + 2\\text{H}_2\\text{O} \\underset{\\text{Charge}}{\\overset{\\text{Discharge}}{\\rightleftharpoons}} \\text{Cd(OH)}_2 + 2\\text{Ni(OH)}_2
\\]
The **Nickel-Cadmium (Ni-Cd) cell** is a classic rechargeable secondary cell capable of hundreds of charge-discharge cycles.

### 2. Physical Context & Practical Illustration:
Ni-Cd, Nickel-Metal Hydride (NiMH), and Lithium-ion batteries power smartphones, laptops, and electric power tools because their chemical energy can be replenished repeatedly from mains power.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Leclanché dry cells are non-rechargeable primary cells.
- **Option B is incorrect**: Standard alkaline cells are primary cells designed for single use.
- **Option C is correct**: Nickel-Cadmium (Ni-Cd) cells are rechargeable secondary batteries.
- **Option D is incorrect**: Daniell cells are non-rechargeable primary laboratory cells.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-050",
    text: "For industrial, automotive, and heavy mechanical engineering purposes, which traditional non-SI unit of power is widely used?",
    options: [
      "Newton (N)",
      "Joule per second (J/s)",
      "Horsepower (hp)",
      "Kilowatt-hour (kWh)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In mechanical and industrial engineering, mechanical output of engines, pumps, and electric motors is traditionally rated in **Horsepower (hp)**:
- In the imperial/British engineering system:
\\[
1\\text{ Horsepower (hp)} = 550\\text{ foot-pounds per second} \\approx 746\\text{ Watts}
\\]
- In the metric system:
\\[
1\\text{ metric hp (PS)} \\approx 735.5\\text{ Watts}
\\]
The unit was introduced by James Watt to benchmark the power output of his steam engines against working draft horses.

### 2. Physical Context & Practical Illustration:
Agricultural water pumps and tractor engines are commercially rated in horsepower (e.g., a \\(5\\text{ hp}\\) submersible pump draws roughly \\(5 \\times 746\\text{ W} = 3730\\text{ W} \\approx 3.73\\text{ kW}\\) of electrical power).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Newton (\\(\\text{N}\\)) is the SI unit of force, not power.
- **Option B is incorrect**: Joule per second is the SI unit Watt, but the traditional industrial standard cited is horsepower.
- **Option C is correct**: Horsepower (\\(1\\text{ hp} = 746\\text{ W}\\)) is widely used in commercial and automotive ratings.
- **Option D is incorrect**: Kilowatt-hour is a unit of energy, not power.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-051",
    text: "Identify the types of electrochemical cells represented by: (A) A primary non-rechargeable cell, and (B) A secondary rechargeable accumulator cell, respectively:",
    options: [
      "A - Zinc-carbon dry cell, B - Nickel-Cadmium cell",
      "A - Lead-acid storage battery, B - Daniell cell",
      "A - Lithium-ion phone battery, B - Simple voltaic cell",
      "A - Nickel-metal hydride cell, B - Dry Leclanché cell"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
- **Primary Cell (A)**: Converts chemical energy to electrical energy via irreversible spontaneous redox reactions. Once exhausted, it cannot be recharged (e.g., **Zinc-carbon dry cell**, \\(\\mathcal{E} \\approx 1.5\\text{ V}\\)).
- **Secondary Cell (B)**: Functions reversibly as both a galvanic cell (during discharge) and an electrolytic cell (during recharge). Electrical energy is stored as chemical potential energy and can be recharged repeatedly (e.g., **Nickel-Cadmium cell**, \\(\\mathcal{E} \\approx 1.2\\text{ V}\\)).

### 2. Physical Context & Practical Illustration:
Zinc-carbon dry cells are discarded after depletion in TV remote controls, whereas Nickel-Cadmium or Lithium-ion battery packs are recharged hundreds of times in power tools and cordless devices.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Zinc-carbon is a primary cell (A) and Nickel-Cadmium is a secondary cell (B).
- **Option B is incorrect**: Reverses the roles; Lead-acid is secondary and Daniell is primary.
- **Option C is incorrect**: Lithium-ion is secondary, not primary.
- **Option D is incorrect**: Reverses the order.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-052",
    text: "In a miniature alkaline button cell (used in wristwatches and calculators), which material serves as the negative electrode (anode)?",
    options: [
      "Powdered Zinc (Zn)",
      "Silver oxide (Ag₂O)",
      "Mercuric oxide (HgO)",
      "Nickel hydroxide"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In miniature button cells (silver oxide or alkaline button cells):
- **Negative Electrode (Anode)**: Consists of finely powdered **Zinc metal (Zn)** mixed with a gelling agent. At this terminal, zinc undergoes oxidation, releasing electrons:
\\[
\\text{Zn}_{(s)} + 2\\text{OH}^-_{(aq)} \\longrightarrow \\text{ZnO}_{(s)} + \\text{H}_2\\text{O}_{(l)} + 2e^-
\\]
- **Positive Electrode (Cathode)**: Consists of silver oxide (\\(\\text{Ag}_2\\text{O}\\)) or manganese dioxide (\\(\\text{MnO}_2\\)), where reduction occurs.
- **Electrolyte**: Potassium hydroxide (\\(\\text{KOH}\\)) or sodium hydroxide (\\(\\text{NaOH}\\)) paste.

### 2. Physical Context & Practical Illustration:
Powdered zinc provides a large effective surface area in a tiny disc volume, enabling stable low-current discharge over several years to power quartz wristwatches.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Powdered Zinc acts as the electron donor (negative electrode/anode).
- **Option B is incorrect**: Silver oxide is the cathode material where reduction takes place.
- **Option C is incorrect**: Mercuric oxide is a cathode material used in older mercury cells.
- **Option D is incorrect**: Nickel hydroxide is used in secondary alkaline batteries.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-053",
    text: "What will be the total heat generated in a heating coil of resistance \\(50\\,\\Omega\\) when an electric current of \\(6\\text{ A}\\) flows through it continuously for \\(2\\text{ minutes}\\)?",
    options: [
      "\\(2.16 \\times 10^5\\text{ Joules}\\)",
      "\\(21.6 \\times 10^5\\text{ Joules}\\)",
      "\\(3.6 \\times 10^3\\text{ Joules}\\)",
      "\\(0.216 \\times 10^5\\text{ Joules}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Joule's Law of Heating:
\\[
H = I^2 R t
\\]
Given:
- Electric current \\(I = 6\\text{ A}\\)
- Resistance \\(R = 50\\,\\Omega\\)
- Time duration \\(t = 2\\text{ minutes} = 2 \\times 60\\text{ seconds} = 120\\text{ s}\\)

Substitute the values:
\\[
H = (6\\text{ A})^2 \\times 50\\,\\Omega \\times 120\\text{ s}
\\]
\\[
H = 36 \\times 50 \\times 120
\\]
\\[
H = 1800 \\times 120 = 216,000\\text{ Joules} = 2.16 \\times 10^5\\text{ Joules}
\\]

### 2. Physical Context & Practical Illustration:
This calculation determines the thermal rating of an electric water heater element. In two minutes, \\(2.16 \\times 10^5\\text{ Joules}\\) of thermal energy is transferred into the water, raising its temperature by a predictable amount via \\(H = m c \\Delta T\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(H = 6^2 \\times 50 \\times 120 = 216,000\\text{ J} = 2.16 \\times 10^5\\text{ J}\\).
- **Option B is incorrect**: \\(21.6 \\times 10^5\\text{ J}\\) is an order of magnitude too large (factor of 10 error).
- **Option C is incorrect**: \\(3.6 \\times 10^3\\text{ J}\\) forgets to square the current or use proper time.
- **Option D is incorrect**: \\(0.216 \\times 10^5\\text{ J}\\) represents a decimal place error.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-054",
    text: "According to traditional Indian and British electrical safety standards, what is the standard colour coding for the insulation of Live, Neutral, and Earth wires, respectively?",
    options: [
      "Live: Green, Neutral: Black, Earth: Red",
      "Live: Black, Neutral: Red, Earth: Green",
      "Live: Red, Neutral: Black, Earth: Green",
      "Live: Yellow, Neutral: Blue, Earth: White"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In household three-pin single-phase alternating current wiring (IS 694 / traditional British code):
1. **Live Wire (L)**: Colored **Red** (or Brown in new international IEC standard). It carries high potential alternating voltage (\\(230\\text{ V}\\)) relative to earth.
2. **Neutral Wire (N)**: Colored **Black** (or Light Blue in new IEC standard). It completes the electric circuit, held near ground potential (\\(0\\text{ V}\\)).
3. **Earth Wire (E)**: Colored **Green** (or Green-with-Yellow stripe in new IEC standard). It connects the metal chassis of appliances directly to a copper earthing plate in the ground for shock protection.

### 2. Physical Context & Practical Illustration:
Colour coding ensures electrical safety during installation and repair. An electrician knows immediately that the red wire is live and dangerous to touch, while the green wire is the safety earth lead that directs fault leakage current into the ground.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Green is earthing, never live.
- **Option B is incorrect**: Inverts live and neutral colors.
- **Option C is correct**: Live is Red, Neutral is Black, and Earth is Green.
- **Option D is incorrect**: Used for three-phase line phases, not standard single-phase live-neutral-earth.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-055",
    text: "Which of the following chemical compounds is NOT used in the internal composition of a standard dry Leclanché cell?",
    options: [
      "Ammonium chloride (NH₄Cl)",
      "Manganese dioxide (MnO₂)",
      "Zinc chloride (ZnCl₂)",
      "Copper oxide (CuO)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A standard dry Leclanché cell consists of:
1. **Zinc (Zn) outer container**: Acts as the negative anode.
2. **Graphite rod**: Central cathode.
3. **Electrolyte paste**: A moist paste of Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) and Zinc chloride (\\(\\text{ZnCl}_2\\)), which provides mobile ions for conduction.
4. **Depolarizer**: Manganese dioxide (\\(\\text{MnO}_2\\)) mixed with powdered carbon, which oxidizes hydrogen gas bubbles to water to prevent polarization.
**Copper oxide (CuO)** is not part of a dry cell (it was used in historical Edison-Lalande wet cells).

### 2. Physical Context & Practical Illustration:
Without the depolarizer (\\(\\text{MnO}_2\\)), hydrogen gas bubbles would accumulate on the carbon rod, creating an insulating gas sheath that halts current flow within minutes of operation.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Ammonium chloride is the primary conducting electrolyte paste.
- **Option B is incorrect**: Manganese dioxide is the depolarizer surrounding the cathode.
- **Option C is incorrect**: Zinc chloride is added to maintain electrolyte moisture and reduce local action.
- **Option D is correct**: Copper oxide is not used in a dry cell.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-056",
    text: "Which chemical substance serves as the primary moist electrolyte in a standard dry Leclanché cell?",
    options: [
      "Ammonium chloride (NH₄Cl)",
      "Copper sulfate (CuSO₄)",
      "Dilute hydrochloric acid (HCl)",
      "Sodium hydroxide (NaOH)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a dry Leclanché cell, the electrolyte must provide mobile ions without being in liquid form:
- A moist paste containing **Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\))** mixed with zinc chloride and starch/plaster of Paris fills the space between the zinc casing and the cathode depolarizer bag:
\\[
\\text{NH}_4\\text{Cl} \\rightleftharpoons \\text{NH}_4^+ + \\text{Cl}^-
\\]
- The \\(\\text{Cl}^-\\) ions react with the zinc container to release electrons, while \\(\\text{NH}_4^+\\) ions migrate toward the cathode to participate in depolarizing reduction.

### 2. Physical Context & Practical Illustration:
The term 'dry' cell is slightly misleading: the electrolyte is not completely dry, but a moist paste. If it dries out completely, ionic conduction ceases and the internal resistance becomes infinite, rendering the cell dead.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) is the primary electrolyte in standard dry cells.
- **Option B is incorrect**: Copper sulfate is the catholyte in a Daniell wet cell.
- **Option C is incorrect**: Liquid hydrochloric acid would violently corrode the zinc container and cause acid spills.
- **Option D is incorrect**: Sodium hydroxide is used in alkaline cells, not standard dry Leclanché cells.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-057",
    text: "According to Ohm's Law, how is the electric current (I) flowing through a metallic conductor related to the potential difference (V) maintained across its ends at constant temperature?",
    options: [
      "Current is inversely proportional to the potential difference",
      "Current is directly proportional to the square of the potential difference",
      "Current is completely independent of the potential difference",
      "Current is directly proportional to the potential difference"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Ohm's Law states that at constant temperature and physical dimensions, the electric current (\\(I\\)) flowing through a metallic conductor is directly proportional to the electric potential difference (\\(V\\)) applied across its ends:
\\[
I \\propto V \\implies V = I R \\implies I = \\frac{1}{R} V
\\]
where \\(R\\) is the constant electrical resistance of the conductor.
A graph plotted between potential difference \\(V\\) on the y-axis and current \\(I\\) on the x-axis yields a straight line passing through the origin with slope equal to \\(R\\).

### 2. Physical Context & Practical Illustration:
If you double the battery voltage across a fixed resistor from \\(6\\text{ V}\\) to \\(12\\text{ V}\\), the current flowing through the circuit doubles proportionally from \\(1\\text{ A}\\) to \\(2\\text{ A}\\), confirming the linear relationship \\(V \\propto I\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Current is inversely proportional to resistance, not potential difference.
- **Option B is incorrect**: Power is proportional to \\(V^2\\), but current is linearly proportional to \\(V\\).
- **Option C is incorrect**: Current directly depends on potential difference.
- **Option D is correct**: Current is directly proportional to potential difference (\\(I \\propto V\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-058",
    text: "Which of the following electrical measuring instruments is designed to have the LOWEST electrical resistance?",
    options: [
      "An ideal Ammeter",
      "An ideal Voltmeter",
      "A sensitive Galvanometer",
      "A high-range Ohmmeter"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrical instruments are engineered to minimize disturbance to the circuit being tested:
1. **Ammeter**: Connected in **series** to measure current \\(I\\). Total resistance becomes \\(R_{\\text{circuit}} + R_A\\). To prevent reducing the actual circuit current:
\\[
R_A \\longrightarrow 0 \\quad (\\text{Ideal Ammeter has zero resistance})
\\]
An ammeter has a very low-resistance shunt wire (\\(S \\ll 1\\,\\Omega\\)) connected in parallel with its moving coil.
2. **Voltmeter**: Connected in **parallel** to measure voltage. To avoid drawing current away from the circuit branch:
\\[
R_V \\longrightarrow \\infty \\quad (\\text{Ideal Voltmeter has infinite resistance})
\\]

### 2. Physical Context & Practical Illustration:
If an ammeter had high resistance, inserting it into a circuit would significantly throttle the current, giving an inaccurately low reading. Therefore, ammeter shunts have resistances of milliohms (\\(10^{-3}\\,\\Omega\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: An ammeter is designed to have the lowest possible resistance (ideally zero) to avoid impeding current.
- **Option B is incorrect**: A voltmeter has extremely high resistance (ideally infinite).
- **Option C is incorrect**: A galvanometer has moderate coil resistance (\\(10\\,\\Omega\\text{ to } 100\\,\\Omega\\)).
- **Option D is incorrect**: An ohmmeter incorporates substantial internal reference resistance.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-059",
    text: "Which electrical circuit component is used to adjust and regulate the magnitude of electric current by varying resistance without interrupting the circuit?",
    options: [
      "Fixed carbon resistor",
      "Electric fuse wire",
      "Rheostat (variable resistor)",
      "Galvanometer"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Ohm's Law:
\\[
I = \\frac{V}{R}
\\]
To control or vary the current \\(I\\) in a circuit powered by a constant voltage source \\(V\\), one must vary the circuit resistance \\(R\\).
A **rheostat** (variable resistor) consists of a high-resistivity oxidized Nichrome wire coil wound on an insulating ceramic tube with a sliding metallic contact rider:
\\[
R = \\rho \\frac{l}{A}
\\]
Sliding the rider adjusts the effective length \\(l\\) of wire included in the circuit, smoothly controlling the resistance and the resulting electric current.

### 2. Physical Context & Practical Illustration:
Laboratory rheostats and rotary dimmer switches on ceiling fans use this exact principle: rotating the knob changes the resistance in series with the motor, smoothly controlling fan speed.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A fixed resistor provides a single permanent resistance value and cannot be adjusted.
- **Option B is incorrect**: A fuse wire melts to break the circuit under fault overcurrent; it cannot regulate current.
- **Option C is correct**: A rheostat (variable resistor) smoothly regulates current by varying circuit resistance.
- **Option D is incorrect**: A galvanometer detects the presence of tiny currents; it does not control them.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-060",
    text: "On which fundamental physical principle does an industrial electromagnetic crane operate to lift and transport heavy scrap iron?",
    options: [
      "Atmospheric suction pressure",
      "Electrostatic attraction of charged plates",
      "Hydraulic Archimedes buoyancy",
      "Magnetic effect of electric current (Electromagnetism)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An industrial scrap crane operates on the **magnetic effect of electric current**:
1. It features a massive disk of soft iron wound with heavy insulated electrical conductor cables.
2. When energized with a strong direct current (\\(I\\)), a tremendous magnetic field is generated:
\\[
B = \\mu n I
\\]
3. The magnetized iron core attracts ferromagnetic scrap materials (iron and steel) with a force proportional to \\(B^2 A / (2\\mu_0)\\), lifting tons of metal effortlessly.
4. When the crane operator cuts off the electric current (\\(I = 0\\)), the soft iron core immediately demagnetizes due to low coercivity, instantly dropping the scrap at the target location.

### 2. Physical Context & Practical Illustration:
Using a permanent magnet on a scrap crane would make releasing the metal impossible! The controllable nature of electromagnets (turning magnetic force ON and OFF via an electric switch) makes them indispensable in junkyards and steel foundries.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Suction cranes work on smooth non-porous glass or tiles, not jagged heavy scrap metal.
- **Option B is incorrect**: Electrostatic forces are far too weak to lift tons of dense steel.
- **Option C is incorrect**: Hydraulic buoyancy operates in fluids, not crane hoists.
- **Option D is correct**: The crane operates via the magnetic effect of electric current, creating a switchable electromagnet.`
  }
];

module.exports = { ch3_part2 };
