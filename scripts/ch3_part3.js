// scripts/ch3_part3.js - Chapter 3 (Current Electricity) Questions 61-90 Gold Standard Enhancements
const ch3_part3 = [
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-061",
    text: "A bar magnet with North pole at end A and South pole at end B is cut transversely into two equal pieces. What poles are formed at the newly created cut surfaces?",
    options: [
      "Both cut surfaces become unmagnetized neutral ends",
      "Opposite poles: South pole opposite end A, and North pole opposite end B",
      "Both cut surfaces become North poles",
      "Both cut surfaces become South poles"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic monopoles do not exist in nature. Every magnet is composed of microscopic atomic magnetic dipoles aligned in domains:
\\[
\\nabla \\cdot \\mathbf{B} = 0
\\]
When a bar magnet is severed transversely into two halves, each severed piece independently establishes its own pair of equal and opposite poles. The piece retaining original North pole \\(A\\) develops a new South pole at its cut edge, while the piece retaining original South pole \\(B\\) develops a new North pole at its cut edge.

### 2. Physical Context & Practical Illustration:
Imagine a chain of compass needles aligned head-to-tail (North to South). If the chain is snapped anywhere in the middle, the exposed tail of the first segment is South, and the exposed head of the second segment is North. Breaking a magnet creates two smaller, fully functional dipole magnets with identical pole strength per unit cross-sectional area.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The cut edges do not lose magnetism; breaking the physical boundary exposes newly uncompensated magnetic pole domains.
- **Option B is correct**: By dipole conservation, the piece containing end \\(A\\) (North) forms a South pole at its cut surface, and the piece containing end \\(B\\) (South) forms a North pole at its cut surface.
- **Option C is incorrect**: Both ends becoming North poles would violate magnetic flux conservation (isolated magnetic monopoles).
- **Option D is incorrect**: Both ends cannot be South poles without corresponding North poles on the same physical pieces.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-062",
    text: "At which geographical location will a freely suspended magnetic needle rest perfectly horizontally?",
    options: [
      "At the Magnetic Equator",
      "At the Magnetic North Pole",
      "At the Magnetic South Pole",
      "At latitude 45° North"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The angle between the direction of the total magnetic field of the Earth \\(\\mathbf{B}_E\\) and the horizontal plane is the magnetic dip (or angle of inclination, \\(\\delta\\)):
\\[
\\tan \\delta = \\frac{B_V}{B_H}
\\]
- At the **Magnetic Equator**, Earth's magnetic lines of force run strictly parallel to the terrestrial surface. Thus, the vertical component is zero (\\(B_V = 0\\)), yielding:
\\[
\\tan \\delta = 0 \\implies \\delta = 0^\\circ
\\]
The needle rests completely horizontal.
- At the **Magnetic Poles**, the field lines are perpendicular to the surface (\\(B_H = 0\\)), yielding \\(\\delta = 90^\\circ\\) (vertical dip).

### 2. Physical Context & Practical Illustration:
Earth behaves like an enormous tilted bar magnet buried near its center. Near the equator, field lines emerge from the southern hemisphere and travel northwards hugging the spherical curvature. A dip needle pivoted on a horizontal axle aligns tangentially to the ground at the equator with zero inclination.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: At the magnetic equator, the angle of dip is \\(0^\\circ\\), so a freely suspended magnet aligns parallel to the horizontal ground.
- **Option B is incorrect**: At the magnetic North Pole, the angle of dip is \\(90^\\circ\\), causing the needle to point vertically downwards.
- **Option C is incorrect**: At the magnetic South Pole, the angle of dip is \\(90^\\circ\\), causing the needle to point vertically upwards.
- **Option D is incorrect**: At \\(45^\\circ\\) latitude, \\(B_V = B_H\\) and the dip angle is \\(45^\\circ\\), so the needle rests tilted, not horizontal.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-063",
    text: "Who was the first scientist to experimentally observe that an electric current produces a magnetic field?",
    options: [
      "Michael Faraday",
      "James Prescott Joule",
      "Hans Christian Oersted",
      "Alessandro Volta"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1820, Danish physicist Hans Christian Oersted discovered electromagnetism. He observed that when a steady direct current passes through a conducting wire, a nearby pivoted magnetic compass needle experiences a torque and deflects:
\\[
\\mathbf{B} = \\frac{\\mu_0 I}{2\\pi r} \\hat{\\phi}
\\]
This landmark discovery established the fundamental physical link connecting electricity and magnetism, laying the foundation for modern electrodynamics.

### 2. Physical Context & Practical Illustration:
During a lecture demonstration, Oersted placed a wire connected to a voltaic battery directly above a magnetic compass needle aligned in the North-South direction. When the circuit switch closed, the compass needle deflected perpendicularly to the wire, proving that electric charges in motion generate a surrounding magnetic field.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Michael Faraday discovered electromagnetic induction (generating electric current from changing magnetic fields) in 1831, eleven years after Oersted.
- **Option B is incorrect**: James Prescott Joule formulated the heating effect of electric current (\\(H = I^2 R t\\)).
- **Option C is correct**: Hans Christian Oersted first observed the deflection of a magnetic needle by an electric current in 1820.
- **Option D is incorrect**: Alessandro Volta invented the primary electrochemical cell (Voltaic pile) in 1800.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-064",
    text: "Which of the following alloys is widely used to manufacture strong permanent magnets?",
    options: [
      "Alnico",
      "Aluminium Bronze",
      "Solder metal",
      "Duralumin"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Permanent magnets require ferromagnetic materials characterized by:
1. **High Magnetic Retentivity (Remanence, \\(B_r\\))**: Capacity to retain a large fraction of magnetic flux density after the external magnetizing field is removed.
2. **High Coercivity (\\(H_c\\))**: Resistance to demagnetization under stray magnetic fields, physical mechanical shocks, or moderate temperature variations:
\\[
\\text{Energy Product} = (BH)_{\\text{max}}
\\]
**Alnico** is a specialized ferromagnetic alloy composed primarily of Aluminium (Al), Nickel (Ni), Cobalt (Co), and Iron (Fe), offering exceptionally high retentivity and coercivity.

### 2. Physical Context & Practical Illustration:
Alnico alloys are cast or sintered into permanent magnets utilized in loudspeaker voice-coil assemblies, electric guitar pickups, electric meters, and microwave magnetrons because their magnetic alignment persists reliably over decades.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Alnico is an alloy of aluminium, nickel, and cobalt possessing high retentivity and coercivity, making it an ideal permanent magnet.
- **Option B is incorrect**: Aluminium bronze is a copper-aluminium alloy used for corrosion-resistant marine hardware, not for permanent magnets.
- **Option C is incorrect**: Solder (tin-lead or tin-copper) is a low-melting-point alloy used for joining electrical connections.
- **Option D is incorrect**: Duralumin (aluminium, copper, magnesium, manganese) is a lightweight structural alloy used in aircraft construction.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-065",
    text: "Which material is used as 'magnetic keepers' to protect permanent bar magnets from losing their magnetism over time?",
    options: [
      "Cast Iron",
      "Brass plates",
      "Soft Iron",
      "Hardened Steel"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An isolated bar magnet undergoes slow self-demagnetization because its free uncompensated magnetic poles create an internal demagnetizing field (\\(\\mathbf{H}_d\\)) opposing the internal magnetization (\\(\\mathbf{M}\\)):
\\[
\\mathbf{B}_{\\text{internal}} = \\mu_0 (\\mathbf{M} - N \\mathbf{M})
\\]
When pairs of bar magnets are stored with unlike poles adjacent and bridged across their ends by strips of **soft iron** (magnetic keepers), the high magnetic permeability (\\(\\mu_r \\gg 1\\)) of soft iron channels the magnetic flux into continuous, closed continuous loops, eliminating free surface poles and neutralizing the demagnetizing field.

### 2. Physical Context & Practical Illustration:
In science laboratories, bar magnets are stored in pairs in wooden boxes separated by a wooden spacer with two soft iron pieces placed across their opposite poles. Because soft iron is easily magnetized and has high permeability, the magnetic lines of force circulate continuously within the magnetic circuit.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Cast iron has high carbon content, significant hysteresis, and lower permeability than pure soft iron.
- **Option B is incorrect**: Brass is a non-magnetic copper-zinc alloy; it cannot conduct magnetic flux lines and cannot prevent demagnetization.
- **Option C is correct**: Soft iron has high magnetic permeability and low coercivity, easily forming closed magnetic flux loops that prevent self-demagnetization.
- **Option D is incorrect**: Hardened steel retains permanent magnetism itself and is difficult to magnetize/demagnetize quickly, making it unsuitable as a keeper.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-066",
    text: "Which of the following physical quantities has its SI unit expressed in Coulomb (C)?",
    options: [
      "Electric charge",
      "Electric current",
      "Electrical resistance",
      "Electric potential difference"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electric charge (\\(Q\\)) represents the fundamental intrinsic property of subatomic particles that causes them to experience electromagnetic forces. By definition:
\\[
Q = I \\times t
\\]
In SI units, current \\(I\\) is in Amperes (\\(\\text{A}\\)) and time \\(t\\) is in seconds (\\(\\text{s}\\)):
\\[
1\\text{ Coulomb (C)} = 1\\text{ Ampere-second (A}\\cdot\\text{s)}
\\]
One Coulomb corresponds to the collective charge of approximately \\(6.25 \\times 10^{18}\\) electrons.

### 2. Physical Context & Practical Illustration:
When a steady electric current of \\(1\\text{ A}\\) flows through a copper conductor for \\(1\\text{ s}\\), exactly \\(1\\text{ C}\\) of electric charge traverses any given cross-section of the wire.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The SI unit of electric charge is the Coulomb (\\(\\text{C}\\)).
- **Option B is incorrect**: The SI unit of electric current is the Ampere (\\(\\text{A} = \\text{C/s}\\)).
- **Option C is incorrect**: The SI unit of electrical resistance is the Ohm (\\(\\Omega = \\text{V/A}\\)).
- **Option D is incorrect**: The SI unit of electric potential difference is the Volt (\\(\\text{V} = \\text{J/C}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-067",
    text: "Which information is provided by drawing the lines of force of a magnetic field?",
    options: [
      "The relative strength of the field only",
      "The direction of the field at any point only",
      "The presence of electrical charges in the magnet",
      "Both the magnitude (relative strength) and the direction of the magnetic field"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic field lines (lines of magnetic induction) are imaginary continuous curves used to visually represent a vector magnetic field \\(\\mathbf{B}\\):
1. **Direction**: The tangent drawn to a magnetic line of force at any point gives the vector direction of the magnetic field \\(\\mathbf{B}\\) at that location (the direction in which a free North magnetic pole would move).
2. **Magnitude (Strength)**: The degree of closeness (spatial density or flux density) of the lines represents the field's magnitude:
\\[
B \\propto \\frac{\\Phi}{A}
\\]
Where lines are crowded (near poles), the field is strong; where lines are spaced apart, the field is weak.

### 2. Physical Context & Practical Illustration:
Sprinkling iron filings around a bar magnet maps out the lines of force. Close to the North and South pole tips, filings form dense clusters (indicating maximum field intensity), while further away, the curved lines spread out (indicating diminished field strength).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The field lines provide direction in addition to relative strength.
- **Option B is incorrect**: The field lines provide relative field intensity (via line density) in addition to direction.
- **Option C is incorrect**: Magnetic field lines represent magnetic flux, not static electrostatic charge distributions.
- **Option D is correct**: Magnetic lines of force convey both vector direction (via tangents) and field strength/magnitude (via line crowding).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-068",
    text: "What functions can be performed using a Gold Leaf Electroscope?",
    options: [
      "Only detect the presence of static electric charge",
      "Only identify whether an unknown charge is positive or negative",
      "Measure high-frequency alternating current in a circuit",
      "Both detect the presence of electric charge and identify its nature (positive or negative)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A Gold Leaf Electroscope (GLE) operates on the electrostatic principle that like charges repel each other:
1. **Detection of Charge**: When an uncharged GLE is touched by a charged body, charge conducts through the metal disc and brass rod to the two thin gold leaves. The leaves acquire like charges and diverge due to electrostatic repulsion.
2. **Identification of Charge Nature**: If the GLE is pre-charged with a known charge (e.g., positive):
   - Bringing a similarly charged (+ve) body near the disc induces further like charge onto the leaves, increasing divergence.
   - Bringing an oppositely charged (-ve) body near attracts positive charge upward toward the disc, decreasing leaf divergence.

### 2. Physical Context & Practical Illustration:
Gold leaf is used because gold can be beaten into microscopic, extremely light, highly conductive foils. Even tiny static charges generate sufficient electrostatic repulsion to overcome gravity, causing visible mechanical divergence.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The electroscope is not limited to mere detection; it can also determine the polarity of an unknown charge when pre-charged.
- **Option B is incorrect**: It can detect charge on an uncharged electroscope before identifying its nature.
- **Option C is incorrect**: An electroscope is a sensitive electrostatic device, not an ammeter for measuring alternating current.
- **Option D is correct**: A gold leaf electroscope both detects the presence of electric charge and determines whether it is positive or negative.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-069",
    text: "In a gold leaf electroscope, the vertical central stem connecting the brass disc to the gold leaves is made of:",
    options: [
      "Ebonite",
      "Brass",
      "Glass",
      "Rubber"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electroscope requires an electrical conductor to transfer static charge freely from the external top terminal disc down to the suspended gold leaves. The vertical central stem is fabricated from **brass** (a copper-zinc alloy) because of its:
- High electrical conductivity (low resistivity, \\(\\rho \\approx 6 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)).
- Rigidity and corrosion resistance.
The brass rod is insulated from the metal casing using an ebonite or rubber stopper to prevent charge leakage to the ground.

### 2. Physical Context & Practical Illustration:
When a charged glass rod touches the upper brass disc, mobile conduction electrons instantaneously redistribute along the conductive brass stem, ensuring both gold leaves immediately acquire identical electric charge and diverge.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Ebonite is an electrical insulator; if the stem were ebonite, electric charge could not conduct to the gold leaves.
- **Option B is correct**: Brass is a metallic conductor that efficiently conducts charge from the top disc to the leaves.
- **Option C is incorrect**: Glass is an electrical insulator used for the protective transparent housing.
- **Option D is incorrect**: Rubber is an insulator used only for the insulating collar supporting the stem.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-070",
    text: "A lightning conductor installed on tall buildings to protect them from lightning strikes is made of:",
    options: [
      "Plastic",
      "Carbon rods",
      "Copper strip",
      "Ebonite"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A lightning strike transfers an enormous electric charge (tens of thousands of Amperes) in microseconds. To safely dissipate this energy into the Earth without causing thermal or structural damage, the lightning conductor must offer negligible electrical resistance:
\\[
R = \\rho \\frac{l}{A} \\implies \\text{Joule Heat } H = I^2 R t
\\]
**Copper** is chosen because of its exceptional electrical conductivity (low resistivity \\(\\rho = 1.68 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)), high melting point (\\(1085^\\circ\\text{C}\\)), and excellent corrosion resistance.

### 2. Physical Context & Practical Illustration:
A lightning conductor consists of sharp pointed copper spikes at the roof summit connected to a thick, heavy-gauge copper strip running down the outside wall into a copper earthing plate buried deep in moist, salted soil. When lightning strikes, the huge surge current flows directly into the ground rather than through the building's concrete and wiring.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Plastic is an electrical insulator; lightning would bypass it and blast through the building structure.
- **Option B is incorrect**: Carbon has much higher electrical resistance and brittle mechanical properties compared to copper.
- **Option C is correct**: Copper provides the low-resistance conductive path required to safely route lightning discharge into the ground.
- **Option D is incorrect**: Ebonite is a hard rubber insulator that cannot conduct electric current.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-071",
    text: "In an external closed electric circuit, the conventional electric current flows:",
    options: [
      "From the positive terminal (higher potential) to the negative terminal (lower potential)",
      "From the negative terminal (lower potential) to the positive terminal (higher potential)",
      "In the exact same direction as the drift velocity of free electrons",
      "Randomly in both directions simultaneously"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By historical convention established before the discovery of the electron:
- **Conventional Current**: Defined as the direction of motion of hypothetical positive charges, which move from higher electric potential (positive terminal, \\(V_+\\)) to lower electric potential (negative terminal, \\(V_-\\)):
\\[
\\mathbf{J} = n_e q_e \\mathbf{v}_d \\quad (\\text{where } q_e = -e)
\\]
- **Electronic Current**: Metallic conduction is carried exclusively by free electrons (negative charges) drifting from low potential (-ve terminal) to high potential (+ve terminal).
Thus, conventional current flows in the direction **opposite** to the physical electron drift.

### 2. Physical Context & Practical Illustration:
Just as water naturally flows from a region of higher gravitational potential (elevated tank) to lower gravitational potential (ground), conventional electric current flows externally from the higher potential positive battery terminal through the load to the lower potential negative terminal.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: In the external circuit, conventional current flows from higher potential (+ve) to lower potential (-ve).
- **Option B is incorrect**: This is the direction of electron flow, or the internal current path inside the battery, not external conventional current.
- **Option C is incorrect**: Conventional current flows opposite to the direction of electron drift.
- **Option D is incorrect**: Direct current in a closed circuit has a definite, unidirectional flow.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-072",
    text: "What is the SI unit of electric potential difference?",
    options: [
      "Ampere (A)",
      "Volt (V)",
      "Ohm (Ω)",
      "Coulomb (C)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electric potential difference (\\(V\\)) between two points is defined as the work done (\\(W\\)) in moving a unit positive charge (\\(Q\\)) from one point to the other against electrostatic forces:
\\[
V = \\frac{W}{Q}
\\]
In SI units, work is measured in Joules (\\(\\text{J}\\)) and charge in Coulombs (\\(\\text{C}\\)):
\\[
1\\text{ Volt (V)} = 1\\text{ Joule per Coulomb (J/C)} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}
\\]
The unit is named in honor of Alessandro Volta.

### 2. Physical Context & Practical Illustration:
If a battery does \\(1\\text{ Joule}\\) of work to move \\(1\\text{ Coulomb}\\) of charge from its negative terminal to its positive terminal, the potential difference across the battery terminals is exactly \\(1\\text{ Volt}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Ampere (\\(\\text{A}\\)) is the SI unit of electric current (\\(I = Q/t\\)).
- **Option B is correct**: The Volt (\\(\\text{V}\\)) is the SI unit of electric potential difference (\\(V = W/Q\\)).
- **Option C is incorrect**: The Ohm (\\(\\Omega\\)) is the SI unit of electrical resistance (\\(R = V/I\\)).
- **Option D is incorrect**: The Coulomb (\\(\\text{C}\\)) is the SI unit of electric charge.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-073",
    text: "In an electric circuit connected to a constant voltage source, what happens to the electric current if the resistance of the circuit is increased?",
    options: [
      "The electric current decreases",
      "The electric current increases proportionally",
      "The electric current remains completely unchanged",
      "The electric current reverses its direction of flow"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Ohm's Law, at constant temperature and physical dimensions, the current (\\(I\\)) flowing through a conductor is inversely proportional to its electrical resistance (\\(R\\)) for a constant applied potential difference (\\(V\\)):
\\[
I = \\frac{V}{R}
\\]
Differentiating with respect to resistance at constant \\(V\\):
\\[
\\frac{dI}{dR} = -\\frac{V}{R^2} < 0
\\]
Therefore, increasing circuit resistance directly reduces the rate of charge flow, decreasing the electric current.

### 2. Physical Context & Practical Illustration:
Consider a dimmable lamp circuit. Turning the rheostat dial increases the resistance in the path of electrons. More frequent collisions between conduction electrons and vibrating lattice ions impede electron drift, reducing current and dimming the lamp.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: By Ohm's law (\\(I = V/R\\)), current is inversely proportional to resistance; increasing resistance causes current to decrease.
- **Option B is incorrect**: Current increases only if voltage increases or resistance decreases.
- **Option C is incorrect**: Current cannot remain constant when resistance changes under fixed potential difference.
- **Option D is incorrect**: Changing resistance alters current magnitude, never its polarity or direction.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-074",
    text: "When two resistors of resistances \\(4\\,\\Omega\\) and \\(6\\,\\Omega\\) are connected in series across a \\(20\\text{ V}\\) battery, what is the electric current flowing through the circuit?",
    options: [
      "\\(2\\text{ A}\\)",
      "\\(5\\text{ A}\\)",
      "\\(10\\text{ A}\\)",
      "\\(0.5\\text{ A}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For resistors connected in series, the same current flows sequentially through each resistor, and the equivalent resistance (\\(R_s\\)) is the algebraic sum of individual resistances:
\\[
R_s = R_1 + R_2 = 4\\,\\Omega + 6\\,\\Omega = 10\\,\\Omega
\\]
Applying Ohm's law to the complete circuit:
\\[
I = \\frac{V}{R_s} = \\frac{20\\text{ V}}{10\\,\\Omega} = 2\\text{ A}
\\]

### 2. Physical Context & Practical Illustration:
In a series circuit, charge cannot branch or accumulate anywhere along the single continuous pathway. The total impedance offered to electron flow is simply the cumulative resistance of all connected components, yielding an overall current of \\(2\\text{ A}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: \\(R_s = 4 + 6 = 10\\,\\Omega\\), and \\(I = V / R_s = 20 / 10 = 2\\text{ A}\\).
- **Option B is incorrect**: \\(5\\text{ A}\\) corresponds to \\(20\\text{ V} / 4\\,\\Omega\\), ignoring the second resistor.
- **Option C is incorrect**: \\(10\\text{ A}\\) confuses the equivalent resistance (\\(10\\,\\Omega\\)) with current.
- **Option D is incorrect**: \\(0.5\\text{ A}\\) inverts the Ohm's law ratio as \\(R_s / V = 10 / 20 = 0.5\\).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-075",
    text: "Which of the following statements is INCORRECT regarding resistors connected in parallel across a common voltage source?",
    options: [
      "The potential difference across each parallel branch is identical",
      "The total current entering the combination equals the sum of branch currents",
      "The effective resistance of the combination is greater than the largest individual resistance",
      "If one electrical component fails or is disconnected, other parallel branches continue to operate"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For \\(n\\) resistors connected in parallel across potential difference \\(V\\):
1. **Common Voltage**: \\(V_1 = V_2 = \\dots = V_n = V\\).
2. **Current Conservation**: \\(I = I_1 + I_2 + \\dots + I_n\\).
3. **Equivalent Resistance (\\(R_p\\))**:
\\[
\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\dots + \\frac{1}{R_n}
\\]
Since each term \\(\\frac{1}{R_i} > 0\\), it follows mathematically that:
\\[
\\frac{1}{R_p} > \\frac{1}{R_{\\text{min}}} \\implies R_p < R_{\\text{min}}
\\]
The equivalent resistance of a parallel circuit is strictly **less than the smallest individual resistance**, never greater!

### 2. Physical Context & Practical Illustration:
Adding parallel branches creates additional parallel conduction channels for electrons, widening the total available cross-sectional path and reducing the overall resistance to charge flow. This is why household appliances are wired in parallel: each receives full mains voltage (230 V) and operates independently.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a true statement**: Each parallel branch connects directly between the same two nodes, maintaining equal potential difference.
- **Option B is a true statement**: By Kirchhoff's Current Law, total current equals the sum of branch currents.
- **Option C is incorrect (the correct answer to the question)**: Effective resistance in parallel is smaller than the smallest individual branch resistance; being greater than the largest is characteristic of series connections.
- **Option D is a true statement**: Parallel branches provide independent current paths, ensuring unbroken operation if one branch opens.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-076",
    text: "In which of the following physical states do ionic compounds conduct electric current most effectively?",
    options: [
      "Solid crystalline state at room temperature",
      "Compressed dry powder state",
      "Molten (liquid) state or dissolved in aqueous solution",
      "Frozen solid state at very low temperature"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrical conduction in matter requires mobile charge carriers. In ionic compounds (e.g., \\(\\text{NaCl}\\)):
- **Solid State**: Positive cations (\\(\\text{Na}^+\\)) and negative anions (\\(\\text{Cl}^-\\)) are held rigidly in fixed positions by strong electrostatic lattice forces. They can only vibrate in place and cannot migrate; hence, solid ionic crystals are electrical insulators (\\(\\sigma \\approx 0\\)).
- **Molten or Aqueous State**: Melting or dissolution breaks the rigid crystal lattice, liberating ions:
\\[
\\text{NaCl}_{(s)} \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+_{(aq)} + \\text{Cl}^-_{(aq)}
\\]
These free mobile ions migrate under an electric field toward oppositely charged electrodes, conducting electricity readily.

### 2. Physical Context & Practical Illustration:
Dry table salt crystals cannot conduct electricity and will not light up a bulb in an open circuit. However, once dissolved in water or heated to melting point (above \\(801^\\circ\\text{C}\\)), the solution becomes an excellent electrolytic conductor, causing the bulb to glow brightly.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: In the solid state, ions are locked into fixed lattice points and cannot carry charge.
- **Option B is incorrect**: Compressing dry powder does not release free mobile ions.
- **Option C is correct**: In the molten or aqueous state, the lattice is broken, releasing free mobile cations and anions that conduct electricity.
- **Option D is incorrect**: Freezing locks particles even more rigidly in place, preventing conduction.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-077",
    text: "During the electrolysis of a dilute aqueous solution of sodium chloride (NaCl), which gas is liberated at the cathode?",
    options: [
      "Oxygen gas (\\(\\text{O}_2\\))",
      "Chlorine gas (\\(\\text{Cl}_2\\))",
      "Hydrogen gas (\\(\\text{H}_2\\))",
      "Nitrogen gas (\\(\\text{N}_2\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In dilute aqueous \\(\\text{NaCl}\\), the solution contains \\(\\text{Na}^+\\), \\(\\text{Cl}^-\\), \\(\\text{H}^+\\), and \\(\\text{OH}^-\\) ions:
- **At the Cathode (negative electrode)**, reduction occurs. Water molecules / \\(\\text{H}^+\\) ions have a substantially higher reduction potential (\\(E^\\circ = -0.83\\text{ V}\\)) than sodium ions \\(\\text{Na}^+\\) (\\(E^\\circ = -2.71\\text{ V}\\)):
\\[
2\\text{H}_2\\text{O}_{(l)} + 2e^- \\longrightarrow \\text{H}_{2(g)} + 2\\text{OH}^-_{(aq)}
\\]
Hydrogen gas is preferentially evolved at the cathode.
- **At the Anode (positive electrode)**, oxidation occurs, discharging \\(\\text{Cl}_2\\) gas.

### 2. Physical Context & Practical Illustration:
This process is the basis of the industrial chlor-alkali process. At the cathode, brisk effervescence of hydrogen gas bubbles is collected, leaving sodium hydroxide (\\(\\text{NaOH}\\)) in the surrounding solution.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Oxygen is evolved during electrolysis of dilute sulfuric acid, not at the cathode.
- **Option B is incorrect**: Chlorine gas is liberated at the anode (positive electrode) via oxidation of chloride ions.
- **Option C is correct**: Hydrogen gas is liberated at the cathode via reduction of hydrogen ions / water.
- **Option D is incorrect**: Nitrogen is not present in sodium chloride or water.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-078",
    text: "Pure distilled water is a very poor conductor of electricity. Which of the following substances should be added to water to make it conduct electricity effectively?",
    options: [
      "Granulated sugar",
      "Kerosene oil",
      "Ethyl alcohol",
      "A few drops of dilute sulfuric acid"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Pure water self-ionizes to an extremely minuscule degree at \\(25^\\circ\\text{C}\\):
\\[
K_w = [\\text{H}^+][\\text{OH}^-] = 1.0 \\times 10^{-14}
\\]
With only \\(10^{-7}\\text{ mol/L}\\) of \\(\\text{H}^+\\) and \\(\\text{OH}^-\\) ions, pure water lacks sufficient charge carrier density to conduct noticeable electric current.
Adding a strong electrolyte like dilute sulfuric acid (\\(\\text{H}_2\\text{SO}_4\\)) introduces a high concentration of mobile ions via complete dissociation:
\\[
\\text{H}_2\\text{SO}_4 \\longrightarrow 2\\text{H}^+ + \\text{SO}_4^{2-}
\\]
These abundant ions carry current under an applied electric field.

### 2. Physical Context & Practical Illustration:
In the electrolysis of water (Hoffmann voltameter), pure water does not decompose because current cannot flow. When a few drops of acid (acidulated water) or salt are added, current immediately flows, and bubbles of hydrogen and oxygen gas form briskly at the electrodes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Sugar is a covalent compound; it dissolves as neutral sugar molecules (\\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}\\)) without producing ions.
- **Option B is incorrect**: Kerosene is a non-polar hydrocarbon liquid that does not dissolve in water or ionize.
- **Option C is incorrect**: Alcohol is a covalent molecular liquid that does not dissociate into conducting ions.
- **Option D is correct**: Dilute acid dissociates completely into mobile \\(\\text{H}^+\\) and \\(\\text{SO}_4^{2-}\\) ions, transforming water into a good electrolytic conductor.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-079",
    text: "What will happen if cold water droplets accidentally fall onto the glass envelope of a glowing, very hot incandescent electric bulb?",
    options: [
      "The glass envelope will crack or shatter due to sudden uneven thermal contraction",
      "The internal tungsten filament will immediately fuse without damaging the glass",
      "The bulb will glow significantly brighter due to external cooling",
      "The electrical resistance of the filament will instantly drop to zero"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An incandescent electric bulb operating at rated voltage heats its internal filament to over \\(2500^\\circ\\text{C}\\), heating the surrounding glass envelope to upwards of \\(150^\\circ\\text{C} - 200^\\circ\\text{C}\\) via radiation and gas convection.
Glass is a poor thermal conductor with a finite coefficient of thermal expansion (\\(\\alpha\\)). When cold water hits the localized surface:
\\[
\\sigma_{\\text{thermal}} = E \\alpha \\Delta T
\\]
The outer contacted surface cools and contracts rapidly while the inner surface remains expanded and hot. The resulting severe differential thermal stress exceeds the ultimate tensile strength of glass, producing rapid fracture (thermal shock shattering).

### 2. Physical Context & Practical Illustration:
Pouring cold water into a hot baking dish or onto hot glassware causes violent thermal cracking for the exact same physical reason. The brittle nature and low thermal conductivity of standard soda-lime glass cannot withstand steep temperature gradients across its thickness.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The localized rapid cooling creates intense tensile thermal stress across the glass wall, causing it to crack or shatter.
- **Option B is incorrect**: The filament inside is protected by inert gas/vacuum until the glass envelope fractures and admits atmospheric oxygen.
- **Option C is incorrect**: Cooling the outer glass does not increase the filament's light emission.
- **Option D is incorrect**: The filament resistance depends on its internal temperature, which remains high until oxygen enters.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-080",
    text: "On which fundamental effect of electric current does a household electric iron operate?",
    options: [
      "Magnetic effect of electric current",
      "Chemical effect of electric current",
      "Heating effect of electric current",
      "Sound effect of electric current"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric iron operates on the **Joule heating effect of electric current**. When current \\(I\\) flows through a conductor of resistance \\(R\\) for duration \\(t\\), electrical potential energy is converted into thermal energy due to frequent inelastic collisions between drifting electrons and lattice atoms:
\\[
H = I^2 R t = V I t = \\frac{V^2}{R} t
\\]
The heating element is made of high-resistivity Nichrome wire wound around a mica sheet, transferring heat conductionally to the heavy soleplate.

### 2. Physical Context & Practical Illustration:
The mica sheet acts as an electrical insulator to prevent electric shocks while conducting heat efficiently to the smooth metallic base. A built-in bimetallic thermostat automatically switches off the circuit when the iron reaches the set temperature.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The magnetic effect is utilized in electric motors, relays, and electric bells, not irons.
- **Option B is incorrect**: The chemical effect is utilized in electroplating, electrorefining, and battery charging.
- **Option C is correct**: Electric irons convert electrical energy into heat energy via Joule heating (\\(H = I^2 R t\\)).
- **Option D is incorrect**: Sound effect is utilized in buzzers, loudspeakers, and piezoelectric transducers.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-081",
    text: "Which versatile electrical measuring instrument can measure electric current, potential difference, and electrical resistance in a circuit?",
    options: [
      "Potentiometer",
      "Electrometer",
      "Micrometer",
      "Multimeter (AVO meter)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **multimeter** (also termed an AVO meter: Ampere-Volt-Ohm meter) is a multi-purpose electronic instrument combining several measurement capabilities in a single unit:
1. **Ammeter function**: Measures direct or alternating current (\\(I\\)) connected in series (low internal impedance).
2. **Voltmeter function**: Measures DC/AC potential difference (\\(V\\)) connected in parallel (high internal impedance).
3. **Ohmmeter function**: Measures resistance (\\(R\\)) across unpowered components by applying a known internal test current:
\\[
R = \\frac{V_{\\text{test}}}{I_{\\text{measured}}}
\\]

### 2. Physical Context & Practical Illustration:
Electronic technicians and electricians carry digital multimeters (DMMs) equipped with rotary function dials and dual probe leads. By rotating the dial selector, one can test battery voltages, verify circuit continuity, and measure motor winding resistances using one portable device.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A potentiometer is used primarily for precise comparison of electromotive forces (EMFs) using null deflection.
- **Option B is incorrect**: An electrometer measures electrostatic charge and high electrical potential.
- **Option C is incorrect**: A micrometer is a mechanical precision tool used to measure physical thickness/diameter, not electrical quantities.
- **Option D is correct**: A multimeter combines the functions of ammeter, voltmeter, and ohmmeter to measure current, voltage, and resistance.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-082",
    text: "Two resistors of resistances \\(6\\,\\Omega\\) and \\(3\\,\\Omega\\) are connected in parallel. What is their effective (equivalent) resistance?",
    options: [
      "\\(9\\,\\Omega\\)",
      "\\(2\\,\\Omega\\)",
      "\\(0.5\\,\\Omega\\)",
      "\\(18\\,\\Omega\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For two resistors \\(R_1\\) and \\(R_2\\) connected in parallel, the reciprocal of the equivalent resistance (\\(R_p\\)) is the sum of the reciprocals of individual resistances:
\\[
\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} = \\frac{1}{6} + \\frac{1}{3}
\\]
Taking the common denominator of \\(6\\):
\\[
\\frac{1}{R_p} = \\frac{1 + 2}{6} = \\frac{3}{6} = \\frac{1}{2\\,\\Omega}
\\]
Inverting gives:
\\[
R_p = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{6 \\times 3}{6 + 3} = \\frac{18}{9} = 2\\,\\Omega
\\]

### 2. Physical Context & Practical Illustration:
Connecting resistors in parallel provides alternate parallel pathways for electric charges. Even though one branch has a \\(6\\,\\Omega\\) resistor, the presence of the parallel \\(3\\,\\Omega\\) path increases the overall conductance of the circuit, dropping the net equivalent resistance to \\(2\\,\\Omega\\) (less than the smallest branch resistance).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(9\\,\\Omega\\) is the series combination (\\(R_s = 6 + 3 = 9\\,\\Omega\\)).
- **Option B is correct**: \\(R_p = (6 \\times 3) / (6 + 3) = 18 / 9 = 2\\,\\Omega\\).
- **Option C is incorrect**: \\(0.5\\,\\Omega\\) is the reciprocal \\(1/R_p = 1/2\\).
- **Option D is incorrect**: \\(18\\,\\Omega\\) is merely the product \\(R_1 \\times R_2\\) without dividing by their sum.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-083",
    text: "An electric current of \\(0.5\\text{ A}\\) flows through an electric lamp for \\(10\\text{ minutes}\\). What is the total electric charge that passes through the circuit?",
    options: [
      "\\(5\\text{ C}\\)",
      "\\(50\\text{ C}\\)",
      "\\(300\\text{ C}\\)",
      "\\(600\\text{ C}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electric current (\\(I\\)) is defined as the rate of flow of electric charge (\\(Q\\)) across any cross-section of a conductor:
\\[
I = \\frac{Q}{t} \\implies Q = I \\times t
\\]
Given:
- Current \\(I = 0.5\\text{ A}\\)
- Time \\(t = 10\\text{ minutes} = 10 \\times 60\\text{ s} = 600\\text{ s}\\)

Substitute the SI values:
\\[
Q = 0.5\\text{ A} \\times 600\\text{ s} = 300\\text{ C}
\\]

### 2. Physical Context & Practical Illustration:
Electric charge calculations require time to be expressed strictly in seconds (the SI base unit). Operating the lamp for ten minutes allows \\(300\\text{ Coulombs}\\) of charge, representing \\(300 \\times 6.25 \\times 10^{18} \\approx 1.875 \\times 10^{21}\\) electrons, to pass through the filament.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(5\\text{ C}\\) results from forgetting to convert minutes to seconds (\\(0.5 \\times 10 = 5\\)).
- **Option B is incorrect**: \\(50\\text{ C}\\) is an arbitrary arithmetic error.
- **Option C is correct**: \\(Q = I \\times t = 0.5\\text{ A} \\times 600\\text{ s} = 300\\text{ C}\\).
- **Option D is incorrect**: \\(600\\text{ C}\\) is the elapsed time in seconds, not the charge.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-084",
    text: "What is the SI unit of electric current?",
    options: [
      "Volt (V)",
      "Ohm (Ω)",
      "Ampere (A)",
      "Coulomb (C)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electric current (\\(I\\)) is one of the seven base physical quantities in the International System of Units (SI). It is defined as the rate of transfer of electric charge past a point in a circuit:
\\[
I = \\frac{\\Delta Q}{\\Delta t}
\\]
Its SI unit is the **Ampere (A)**, named after French physicist André-Marie Ampère:
\\[
1\\text{ Ampere} = 1\\text{ Coulomb per second } (1\\text{ A} = 1\\text{ C/s})
\\]
A current of \\(1\\text{ A}\\) corresponds to the flow of \\(6.25 \\times 10^{18}\\) elementary electronic charges per second.

### 2. Physical Context & Practical Illustration:
Typical household electrical appliances draw currents measured in Amperes: an LED lamp draws about \\(0.05\\text{ A}\\), an electric ceiling fan draws about \\(0.3\\text{ A}\\), and an electric toaster or iron draws about \\(5\\text{ A} - 8\\text{ A}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Volt (\\(\\text{V}\\)) is the unit of electric potential difference and electromotive force.
- **Option B is incorrect**: The Ohm (\\(\\Omega\\)) is the unit of electrical resistance.
- **Option C is correct**: The Ampere (\\(\\text{A}\\)) is the SI unit of electric current.
- **Option D is incorrect**: The Coulomb (\\(\\text{C}\\)) is the unit of electric charge.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-085",
    text: "In a standard dry Leclanché cell, what material serves as the negative terminal (anode)?",
    options: [
      "Carbon (graphite) rod",
      "Outer Zinc container",
      "Manganese dioxide paste",
      "Copper metal cap"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A standard dry cell (Leclanché cell) is a primary electrochemical galvanic cell:
- **Negative Terminal (Anode / Zinc Casing)**: The outer cylindrical container is made of metallic Zinc (\\(\\text{Zn}\\)). At this electrode, oxidation occurs:
\\[
\\text{Zn}_{(s)} \\longrightarrow \\text{Zn}^{2+}_{(aq)} + 2e^-
\\]
Releasing electrons into the external circuit makes the zinc container the negative terminal.
- **Positive Terminal (Cathode / Carbon Rod)**: A central graphite rod surrounded by a depolarizer mixture of manganese dioxide (\\(\\text{MnO}_2\\)) and carbon powder.

### 2. Physical Context & Practical Illustration:
The outer zinc can serves a dual purpose: it acts as the chemical container housing the moist electrolyte paste (ammonium chloride, \\(\\text{NH}_4\\text{Cl}\\)) and functions as the active electron donor that powers connected devices like wall clocks and flashlights.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The carbon (graphite) rod is the inert positive terminal (cathode) where reduction occurs.
- **Option B is correct**: The outer zinc container undergoes oxidation (\\(\\text{Zn} \\to \\text{Zn}^{2+} + 2e^-\\)) and functions as the negative terminal.
- **Option C is incorrect**: Manganese dioxide acts as a chemical depolarizer to oxidize hydrogen gas formed during discharge.
- **Option D is incorrect**: The brass/copper cap merely protects the tip of the positive carbon rod.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-086",
    text: "When two point positive charges are separated by a distance \\(r\\), the electrostatic repulsive force between them is \\(16\\text{ units}\\). If the distance between the two charges is doubled, what will be the new repulsive force?",
    options: [
      "\\(4\\text{ units}\\)",
      "\\(8\\text{ units}\\)",
      "\\(16\\text{ units}\\)",
      "\\(1\\text{ unit}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to Coulomb's Law of electrostatics, the electrostatic force (\\(F\\)) between two stationary point charges is inversely proportional to the square of the distance (\\(r\\)) between them:
\\[
F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2} \\implies F \\propto \\frac{1}{r^2}
\\]
When the distance is doubled, \\(r' = 2r\\):
\\[
F' = \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{(2r)^2} = \\frac{1}{4} \\left( \\frac{1}{4\\pi\\varepsilon_0} \\frac{q_1 q_2}{r^2} \\right) = \\frac{F}{4}
\\]
Given the initial force \\(F = 16\\text{ units}\\):
\\[
F' = \\frac{16\\text{ units}}{4} = 4\\text{ units}
\\]

### 2. Physical Context & Practical Illustration:
The inverse square law causes electrostatic interactions to drop off rapidly with distance. Doubling separation cuts the force to one-fourth (\\(2^2 = 4\\)); tripling separation would diminish the force to one-ninth (\\(3^2 = 9\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: By the inverse-square law, \\(F' = F / 2^2 = 16 / 4 = 4\\text{ units}\\).
- **Option B is incorrect**: \\(8\\text{ units}\\) assumes an inverse linear relationship (\\(F \\propto 1/r\\)), forgetting the square term.
- **Option C is incorrect**: \\(16\\text{ units}\\) implies electrostatic force is independent of distance.
- **Option D is incorrect**: \\(1\\text{ unit}\\) corresponds to quadrupling distance (\\(r' = 4r \\implies F / 16 = 1\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-087",
    text: "Which type of magnet is used in the operational mechanism of an electric bell?",
    options: [
      "Permanent Alnico magnet",
      "Temporary electromagnet (soft iron core)",
      "Magnetic compass needle",
      "Naturally occurring lodestone"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric bell requires a magnet that can be energized and de-energized rapidly in fractions of a second:
- It employs an **electromagnet** consisting of insulated copper wire wound around a U-shaped soft iron core.
- When current flows, the soft iron core magnetizes instantaneously via the magnetic effect of electric current (\\(B = \\mu n I\\)), attracting the spring-loaded soft iron armature to strike the gong.
- Movement of the armature breaks contact with the contact screw, opening the circuit (\\(I = 0\\)). The soft iron core loses its magnetism instantly due to its very low coercivity and retentivity, allowing the spring to snap the armature back and repeat the cycle.

### 2. Physical Context & Practical Illustration:
If a permanent magnet were used instead of an electromagnet, the armature would remain permanently clamped against the magnet once attracted, preventing the rapid reciprocating ringing motion of the striker hammer.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: A permanent magnet cannot be switched on and off to create the automatic make-and-break cycle.
- **Option B is correct**: An electromagnet with a soft iron core provides rapid, controllable magnetization and demagnetization.
- **Option C is incorrect**: A magnetic needle is a delicate pointer used for field direction sensing, not mechanical actuation.
- **Option D is incorrect**: Lodestone is a weak natural permanent magnet (magnetite).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-088",
    text: "What is the electric charge density and electric field inside the hollow interior cavity of a charged spherical conductor?",
    options: [
      "It increases progressively toward the center",
      "It decreases progressively toward the center",
      "It is strictly zero throughout the internal cavity",
      "It is uniform and equal to the surface charge density"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Gauss's Law of electrostatics, the net electric flux through any closed Gaussian surface enclosing volume \\(V\\) is proportional to the enclosed charge \\(q_{\\text{enc}}\\):
\\[
\\oint \\mathbf{E} \\cdot d\\mathbf{A} = \\frac{q_{\\text{enc}}}{\\varepsilon_0}
\\]
For a conducting hollow sphere in electrostatic equilibrium:
1. Like charges on the conductor mutually repel to the maximum distance possible, residing exclusively on the **outer surface**.
2. Any Gaussian surface constructed entirely inside the internal cavity encloses zero net charge (\\(q_{\\text{enc}} = 0\\)).
3. Hence, the electric field is zero (\\(\\mathbf{E} = 0\\)), and the internal charge density is strictly zero (\\(\\rho = 0\\)).

### 2. Physical Context & Practical Illustration:
This phenomenon is called **electrostatic shielding** (Faraday cage effect). During a thunderstorm, a metal car or airplane cabin forms a closed hollow conductor; any lightning charge resides strictly on the outer metal skin, leaving the inside completely safe from electric fields and shocks.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Charge does not concentrate at the center; electrostatic repulsion forces all mobile charges to the outer boundary.
- **Option B is incorrect**: It does not vary with radius; it is identically zero everywhere inside.
- **Option C is correct**: Charge density and electric field inside a hollow charged conductor are strictly zero.
- **Option D is incorrect**: Charge density is non-zero exclusively on the external surface.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-089",
    text: "Which of the following materials is most suitable for manufacturing strong permanent magnets?",
    options: [
      "Soft iron",
      "Steel / Alnico alloy",
      "Pure copper",
      "Pure lead"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Materials suitable for permanent magnets must possess a wide magnetic hysteresis loop characterized by:
1. **High Retentivity (Remanence, \\(B_r\\))**: Retains strong magnetic flux density after removal of the external field.
2. **High Coercivity (\\(H_c\\))**: Resists demagnetization from external fields, thermal agitation, or mechanical vibration.
Hardened carbon steel and alloys like **Alnico** (Al-Ni-Co-Fe) have very high coercivity, making it difficult for magnetic domains to revert to random orientations once magnetized.
In contrast, soft iron has high retentivity but extremely low coercivity (it demagnetizes immediately when the external field is removed).

### 2. Physical Context & Practical Illustration:
Soft iron is used where temporary magnetization is desired (electromagnets, transformer cores). Steel and Alnico are used where permanent magnetization is required (compass needles, electric guitar pickups, permanent magnet motors).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Soft iron loses almost all magnetism once the magnetizing field ceases; it is used for electromagnets, not permanent magnets.
- **Option B is correct**: Steel and Alnico have high coercivity, permanently locking aligned magnetic domains in place.
- **Option C is incorrect**: Copper is a diamagnetic metal that cannot be magnetized.
- **Option D is incorrect**: Lead is diamagnetic and non-magnetic.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-090",
    text: "Which of the following metal alloy wires is used to make the heating element in an electric room heater or geyser?",
    options: [
      "Aluminium",
      "Pure copper",
      "Nichrome (Nickel-Chromium alloy)",
      "Tungsten"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A heating element converts electrical energy into heat energy via Joule's heating law:
\\[
H = I^2 R t = I^2 \\left(\\rho \\frac{l}{A}\\right) t
\\]
To function effectively, the heating element wire must satisfy four criteria:
1. **High Electrical Resistivity (\\(\\rho\\))**: \\(\\rho_{\\text{Nichrome}} \\approx 1.1 \\times 10^{-6}\\,\\Omega\\cdot\\text{m}\\) (about 60 times higher than copper), producing intense heating in a compact length.
2. **High Melting Point**: Approximately \\(1400^\\circ\\text{C}\\), preventing melting at red-hot operating temperatures.
3. **High Resistance to Oxidation**: Does not oxidize (burn out) even when glowing red-hot in air.
4. **Low Temperature Coefficient of Resistance**: Resistance remains relatively stable over a wide temperature range.
**Nichrome** (an alloy of \\(80\\%\\) Nickel and \\(20\\%\\) Chromium) uniquely fulfills all these criteria.

### 2. Physical Context & Practical Illustration:
When an electric room heater is turned on, the connecting copper power cord remains cool because copper has very low resistance. In contrast, the Nichrome coil element heats up and glows red-hot within seconds because of its high resistivity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Aluminium has low resistivity and a low melting point (\\(660^\\circ\\text{C}\\)); it would quickly oxidize and melt.
- **Option B is incorrect**: Copper has very low resistivity (\\(\\approx 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)); it is used for connecting cables to minimize heat loss.
- **Option C is correct**: Nichrome possesses high electrical resistivity, high melting point, and does not oxidize at high operating temperatures.
- **Option D is incorrect**: Tungsten has a very high melting point but oxidizes rapidly in open air; it is used in evacuated/inert gas light bulbs, not open room heaters.`
  }
];

module.exports = { ch3_part3 };
