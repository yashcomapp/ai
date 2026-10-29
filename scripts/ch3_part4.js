// scripts/ch3_part4.js - Chapter 3 (Current Electricity) Questions 91-114 Gold Standard Enhancements
const ch3_part4 = [
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-091",
    text: "What is the SI unit of Electromotive Force (EMF) of an electric cell?",
    options: [
      "Ampere (A)",
      "Coulomb (C)",
      "Joule (J)",
      "Volt (V)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electromotive Force (EMF, denoted by \\(\\mathcal{E}\\)) is not a mechanical force, but the total electrical energy provided by a source per unit charge that flows through it when the circuit is open (zero current):
\\[
\\mathcal{E} = \\frac{W}{Q} = \\frac{d W}{d Q}
\\]
In SI units, work (\\(W\\)) is measured in Joules (\\(\\text{J}\\)) and charge (\\(Q\\)) in Coulombs (\\(\\text{C}\\)):
\\[
1\\text{ Volt (V)} = 1\\text{ Joule per Coulomb (J/C)} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}
\\]
Therefore, the SI unit of EMF is identical to that of electric potential difference: the **Volt (V)**.

### 2. Physical Context & Practical Illustration:
When a standard alkaline AA cell is rated at \\(1.5\\text{ V}\\), it means the chemical reactions inside the cell supply \\(1.5\\text{ Joules}\\) of electrical energy for every \\(1\\text{ Coulomb}\\) of charge transported between its terminals in an open circuit.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Ampere (\\(\\text{A}\\)) is the SI unit of electric current.
- **Option B is incorrect**: The Coulomb (\\(\\text{C}\\)) is the SI unit of electric charge.
- **Option C is incorrect**: The Joule (\\(\\text{J}\\)) is the SI unit of energy or work, not energy per unit charge.
- **Option D is correct**: The Volt (\\(\\text{V} = \\text{J/C}\\)) is the SI unit of Electromotive Force (EMF).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-092",
    text: "On which fundamental effect of electric current does an electric bell operate?",
    options: [
      "Chemical effect of electric current",
      "Heating effect of electric current",
      "Magnetic effect of electric current",
      "Thermoelectric effect"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric bell operates on the **magnetic effect of electric current** (electromagnetism). When the push-button switch is depressed:
1. Current flows through the coil wound around a soft iron U-core, generating an electromagnet:
\\[
B = \\mu n I
\\]
2. The magnetized core attracts the soft iron armature, causing the hammer to strike the metallic gong.
3. As the armature moves forward, it breaks contact with the contact screw, opening the circuit (\\(I = 0\\)).
4. The magnetic field collapses instantly, allowing the spring to pull the armature back to re-establish contact and repeat the cycle automatically.

### 2. Physical Context & Practical Illustration:
The soft iron core must possess high magnetic permeability and near-zero retentivity so that the magnetic field is created and quenched instantly, enabling rapid hammer vibrations of dozens of cycles per second.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The chemical effect is utilized in electroplating and electrochemical storage cells.
- **Option B is incorrect**: The heating effect is utilized in heaters, toasters, and thermal fuses.
- **Option C is correct**: The electric bell utilizes the magnetic effect of electric current to actuate an electromagnet.
- **Option D is incorrect**: The thermoelectric (Seebeck/Peltier) effect involves temperature differences generating EMF, not electromagnetic actuation.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-093",
    text: "A bar magnet is cut transversely in the middle into two pieces. Which of the following statements is INCORRECT regarding the two resulting pieces?",
    options: [
      "Each piece becomes a complete, independent dipole magnet with its own North and South poles",
      "The newly formed cut surfaces develop opposite magnetic poles",
      "The newly formed cut surfaces develop identical magnetic poles and repel each other",
      "The magnetic pole strength of each piece remains approximately equal to that of the original magnet"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetism originates from aligned microscopic atomic magnetic dipoles. According to Maxwell's equation for magnetism:
\\[
\\oint \\mathbf{B} \\cdot d\\mathbf{A} = 0
\\]
Isolated magnetic monopoles cannot exist. Severing a bar magnet with original poles \\(N\\) (left) and \\(S\\) (right) exposes:
- A new South pole at the cut face of the left piece.
- A new North pole at the cut face of the right piece.
Because the two newly exposed adjacent cut faces have **opposite poles** (one South, one North), they mutually attract each other if placed back together, never repel!

### 2. Physical Context & Practical Illustration:
If you break a brittle ceramic bar magnet in half and attempt to put the two broken halves back together at the fracture line, they snap back together with strong magnetic attraction because opposite poles developed on the mating fracture faces.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is a true statement**: Each severed segment functions as a complete independent magnet with a North and a South pole.
- **Option B is a true statement**: The two mating cut surfaces acquire opposite polarities.
- **Option C is incorrect (the correct answer to the question)**: The cut faces develop opposite poles (attracting each other), so asserting they develop identical repelling poles is false.
- **Option D is a true statement**: Transverse cutting preserves the cross-sectional area, maintaining identical pole strength.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-094",
    text: "Which of the following expressions represents the SI derived base unit of electric power (Watt)?",
    options: [
      "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\)",
      "\\(\\text{g}\\cdot\\text{cm}^3\\cdot\\text{s}^{-1}\\)",
      "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}\\)",
      "\\(\\text{g}\\cdot\\text{cm}\\cdot\\text{s}^{-3}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Power (\\(P\\)) is defined as the rate at which work is done or energy is transformed per unit time:
\\[
P = \\frac{W}{t} = \\frac{\\text{Force} \\times \\text{Displacement}}{\\text{Time}}
\\]
Expressing in SI base units:
\\[
\\text{Force} = \\text{mass} \\times \\text{acceleration} = \\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}
\\]
\\[
\\text{Work} = (\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}) \\times \\text{m} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}
\\]
Dividing by time (\\(\\text{s}\\)):
\\[
1\\text{ Watt (W)} = \\frac{1\\text{ Joule}}{1\\text{ second}} = \\frac{\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}}{\\text{s}} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}
\\]

### 2. Physical Context & Practical Illustration:
In electrical terms, power is also \\(P = V \\times I\\). Since \\(1\\text{ V} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}\\) and \\(1\\text{ A} = 1\\text{ A}\\), multiplying yields \\(1\\text{ W} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\), demonstrating exact dimensional consistency.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: The base unit derivation for Watt is \\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\).
- **Option B is incorrect**: Dimensionally inconsistent with power.
- **Option C is incorrect**: \\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}\\) is the unit of work or energy (Joule), not power.
- **Option D is incorrect**: Dimensionally represents force per unit time, not power.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-095",
    text: "Why do electrostatic experiments (such as charging glass rods or using gold leaf electroscopes) frequently fail or show poor results during the rainy season?",
    options: [
      "Because the ambient air temperature is excessively cold",
      "Because high atmospheric humidity forms a conducting moisture film that leaks static charges",
      "Because distant atmospheric lightning neutralizes the charges wirelessly",
      "Because ambient atmospheric pressure decreases significantly"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Dry air is an excellent electrical insulator with a very high breakdown dielectric strength (\\(\\sim 3 \\times 10^6\\text{ V/m}\\)), allowing static charges deposited on insulators (ebonite, glass, silk) to remain localized for long periods.
During the rainy season, the relative humidity of the atmosphere approaches \\(80\\% - 100\\%\\):
1. A microscopic, invisible film of moisture (water molecules with dissolved atmospheric ions) condenses onto all apparatus surfaces.
2. Water is a polar solvent that facilitates electrolytic surface conduction (\\(\\sigma_{\\text{film}} \\gg \\sigma_{\\text{air}}\\)).
3. Accumulated static charges rapidly leak away to the surroundings via surface conduction before electrostatic effects can be observed.

### 2. Physical Context & Practical Illustration:
In electrostatic laboratories, demonstrator teachers use electric hair-dryers or heating lamps to warm and dry the insulating stands, electroscope stoppers, and glass rods on humid days to disperse the conductive moisture layer.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Moderate temperature changes do not alter dielectric properties of insulators significantly.
- **Option B is correct**: High humidity creates a thin conductive water film on apparatus surfaces, rapidly discharging static electricity to the surroundings.
- **Option C is incorrect**: Distant lightning does not discharge benchtop electrostatic equipment.
- **Option D is incorrect**: Small variations in atmospheric pressure have negligible effect on static charge retention.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-096",
    text: "How can a permanent magnet be completely demagnetized?",
    options: [
      "By placing it inside a solenoid carrying an alternating current and gradually reducing the current to zero, or heating it above its Curie temperature",
      "By breaking it into several smaller pieces with a copper chisel",
      "By applying heavy uniform hydrostatic pressure on it",
      "By immersing it in freezing cold water for several hours"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Ferromagnetism depends on the parallel spontaneous alignment of magnetic dipoles within magnetic domains held together by quantum mechanical exchange interactions.
Demagnetization requires randomizing these ordered domain vectors so that the net vector sum vanishes:
\\[
\\mathbf{M} = \\frac{1}{V} \\sum \\mathbf{m}_i = 0
\\]
This can be achieved by:
1. **Thermal agitation**: Heating the ferromagnetic material above its **Curie temperature** (\\(T_C\\)), where thermal kinetic energy overwhelms exchange forces, transforming it into a paramagnet.
2. **Alternating Demagnetizing Field**: Placing the magnet inside a solenoid carrying alternating current (AC) and slowly decreasing the amplitude to zero, tracing successively smaller hysteresis loops until remanence reaches zero.

### 2. Physical Context & Practical Illustration:
Professional degaussing coils used for demagnetizing ship hulls, magnetic recording heads, and steel tools employ strong AC magnetic fields that are slowly withdrawn, leaving the magnetic domains randomly oriented with zero net external magnetic field.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Thermal agitation above the Curie temperature or cycling through a decaying alternating magnetic field completely randomizes magnetic domains.
- **Option B is incorrect**: Breaking a magnet simply creates smaller dipole magnets; it does not randomize the domain orientations.
- **Option C is incorrect**: Hydrostatic pressure does not disrupt atomic exchange coupling.
- **Option D is incorrect**: Cooling actually stabilizes magnetic domain alignment and enhances magnetization.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-097",
    text: "How must an ammeter be connected in an electrical circuit to accurately measure the electric current flowing through a component?",
    options: [
      "In parallel with the component, because it has extremely high resistance",
      "In series with the component, because it has very low internal resistance",
      "In parallel with the power source, because it draws minimum current",
      "In series with the voltmeter, connected across the terminals"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An ammeter measures the rate of charge flow (\\(I\\)) traversing a branch of a circuit:
1. **Series Connection**: To ensure that the entirety of the current flowing through the component passes through the measuring instrument, the ammeter must be inserted directly into the same single conductive path (in series):
\\[
I_{\\text{circuit}} = I_{\\text{ammeter}}
\\]
2. **Low Internal Resistance (\\(R_A \\to 0\\))**: The total circuit resistance becomes \\(R_{\\text{total}} = R + R_A\\). An ideal ammeter has zero internal resistance so that its introduction does not reduce the circuit current:
\\[
I' = \\frac{V}{R + R_A} \\approx \\frac{V}{R} \\quad (\\text{when } R_A \\ll R)
\\]

### 2. Physical Context & Practical Illustration:
If an ammeter were accidentally connected in parallel across a load or power source, its extremely low resistance would form a dead short circuit, drawing a massive fault current that would burn out the meter coil or blow the protective fuse instantly.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Connecting an ammeter in parallel creates a short circuit and damages the instrument; high resistance is a property of voltmeters.
- **Option B is correct**: An ammeter is connected in series and has very low internal resistance so it does not alter the circuit current.
- **Option C is incorrect**: Connecting directly across the source produces an immediate short circuit.
- **Option D is incorrect**: Connecting in series with a high-resistance voltmeter prevents current from flowing through the circuit.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-098",
    text: "Which of the following metal alloys is chosen for making heating coils in household electric appliances like toasters and water heaters?",
    options: [
      "Pure Aluminium",
      "Pure Copper",
      "Nichrome (Nickel-Chromium alloy)",
      "Brass (Copper-Zinc alloy)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Heating elements operate by converting electrical energy into heat through Joule heating:
\\[
P = I^2 R = I^2 \\left(\\rho \\frac{l}{A}\\right)
\\]
An optimal heating alloy must exhibit:
1. **High Electrical Resistivity (\\(\\rho\\))**: Allows compact element design while generating substantial thermal power.
2. **High Melting Point (\\(\\approx 1400^\\circ\\text{C}\\))**: Withstands intense red heat without softening or melting.
3. **High Oxidation Resistance**: Forms a protective, adherent chromium oxide (\\(\\text{Cr}_2\\text{O}_3\\)) surface layer that prevents further oxidation even at \\(1000^\\circ\\text{C}\\).
**Nichrome** (an alloy of \\(80\\%\\) Nickel and \\(20\\%\\) Chromium) perfectly satisfies all these engineering criteria.

### 2. Physical Context & Practical Illustration:
If copper or aluminium were used as a heating element, their low melting points and rapid oxidation in air would cause the element to melt or burn out within seconds of turning on the power.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Aluminium has low resistivity and a low melting point (\\(660^\\circ\\text{C}\\)).
- **Option B is incorrect**: Copper has extremely low resistivity; it is used for connecting leads to prevent heating.
- **Option C is correct**: Nichrome has high resistivity, high melting point, and excellent resistance to oxidation at high temperatures.
- **Option D is incorrect**: Brass has relatively low resistivity and oxidizes readily at elevated temperatures.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-099",
    text: "Which of the following physical quantities has its SI unit expressed in Volt (V)?",
    options: [
      "Electric charge",
      "Electric current",
      "Electromotive force (EMF)",
      "Electrical resistivity (specific resistance)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Both electric potential difference (\\(V\\)) and Electromotive Force (\\(\\mathcal{E}\\)) represent energy per unit electric charge:
\\[
\\mathcal{E} = \\frac{W}{Q}
\\]
In SI units, \\(1\\text{ Joule}\\) of work done per \\(1\\text{ Coulomb}\\) of charge transported equals \\(1\\text{ Volt}\\):
\\[
1\\text{ Volt (V)} = 1\\text{ J/C} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}
\\]
Thus, Electromotive Force is measured in **Volts**.

### 2. Physical Context & Practical Illustration:
The electromotive force of a dry cell is \\(1.5\\text{ V}\\), a lead-acid car battery cell is \\(2.1\\text{ V}\\), and a lithium-ion cell is \\(3.7\\text{ V}\\). All specify the maximum potential difference between cell terminals under open-circuit conditions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Electric charge is measured in Coulombs (\\(\\text{C}\\)).
- **Option B is incorrect**: Electric current is measured in Amperes (\\(\\text{A}\\)).
- **Option C is correct**: Electromotive force (EMF) is measured in Volts (\\(\\text{V}\\)).
- **Option D is incorrect**: Electrical resistivity is measured in Ohm-meters (\\(\\Omega\\cdot\\text{m}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-100",
    text: "In fair-weather atmospheric electricity, what is the net electric charge of the Earth's surface relative to the upper atmosphere?",
    options: [
      "Strongly positive",
      "Completely neutral and uncharged",
      "Negative",
      "Constantly oscillating between positive and negative"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In global atmospheric electricity, the Earth and the ionosphere form a giant spherical capacitor:
1. The Earth's conducting surface carries a net **negative charge** of approximately \\(-5 \\times 10^5\\text{ C}\\) (surface charge density \\(\\sigma \\approx -1.1\\text{ nC/m}^2\\)).
2. The upper conducting atmospheric layer (the electrosphere / ionosphere) carries an equal and opposite net positive charge.
3. This charge separation establishes a downward-directed vertical electric field in fair-weather regions:
\\[
E = -\\frac{dV}{dz} \\approx 100\\text{ to } 130\\text{ V/m} \\quad (\\text{directed toward Earth})
\\]
Global thunderstorm activity acts as a global battery, continuously pumping negative charge down to the ground via lightning and rain to maintain this negative equilibrium.

### 2. Physical Context & Practical Illustration:
Standing in an open flat field, there is an electric potential difference of over \\(200\\text{ V}\\) between your feet on the ground and your head \\(1.8\\text{ m}\\) above, but you do not feel a shock because human skin and air have very low current flow under fair-weather conditions.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The upper atmosphere is positive; Earth's surface carries negative charge relative to it.
- **Option B is incorrect**: The Earth's surface is not neutral; it holds an ongoing negative surface charge density.
- **Option C is correct**: Relative to the positive upper atmosphere, the Earth's surface is negatively charged.
- **Option D is incorrect**: In fair weather, the polarity is stable and does not oscillate.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-101",
    text: "A solenoid consists of a long helical coil of insulated copper wire. On which fundamental effect is its operation based?",
    options: [
      "Heating effect of electric current",
      "Chemical effect of electric current",
      "Magnetic effect of electric current",
      "Photoelectric effect"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A solenoid operates on the **magnetic effect of electric current**. When an electric current \\(I\\) circulates through the \\(N\\) closely wound turns of a helical coil:
1. Each individual circular loop generates a magnetic dipole field.
2. Inside the core, the individual magnetic fields superimpose constructively along the central axis, producing a strong, uniform magnetic field:
\\[
B = \\mu_0 n I = \\mu_0 \\left(\\frac{N}{L}\\right) I
\\]
3. The magnetic field outside the solenoid resembles that of an equivalent permanent bar magnet, with distinct North and South magnetic poles at opposite ends.

### 2. Physical Context & Practical Illustration:
Solenoids are the driving component in automotive starter relays, industrial valve actuators, electric door chimes, and MRI medical scanners, converting electric current directly into controllable magnetic attraction and mechanical linear motion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The heating effect causes unwanted resistive losses in a solenoid, not its intended operational mechanism.
- **Option B is incorrect**: The chemical effect relates to electrochemical reactions, not coil magnetic fields.
- **Option C is correct**: A solenoid functions by generating a strong magnetic field from an electric current (\\(B = \\mu_0 n I\\)).
- **Option D is incorrect**: The photoelectric effect involves electron emission triggered by incident light photons.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-102",
    text: "Which of the following statements regarding soft iron are CORRECT?\\n(a) Soft iron conducts electricity\\n(b) Soft iron is a ferromagnetic material\\n(c) Soft iron is an alloy of iron and copper\\n(d) Soft iron is preferred for making permanent magnets",
    options: [
      "Statements (a) and (c) only",
      "Statements (a) and (b) only",
      "Statements (b) and (d) only",
      "Statements (c) and (d) only"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing the properties of soft iron:
- **Statement (a) is correct**: Soft iron is a metallic element with free conduction electrons, having a low electrical resistivity (\\(\\rho \\approx 10^{-7}\\,\\Omega\\cdot\\text{m}\\)); hence it conducts electricity readily.
- **Statement (b) is correct**: Soft iron is a ferromagnetic material with high magnetic permeability (\\(\\mu_r > 1000\\)), easily magnetized in the presence of an external magnetic field.
- **Statement (c) is incorrect**: Soft iron is nearly pure elemental iron with very low carbon content (\\(< 0.1\\%\\)), not an alloy of copper.
- **Statement (d) is incorrect**: Soft iron has very low coercivity and loses its magnetism almost immediately when the magnetizing field is removed; hence it is used for **temporary electromagnets and transformer cores**, not permanent magnets!

### 2. Physical Context & Practical Illustration:
Soft iron is chosen for electromagnets because its magnetic domains align readily under low applied magnetic fields and randomize immediately when current ceases, preventing residual magnetic sticking.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Statement (c) is false because soft iron is pure iron, not a copper alloy.
- **Option B is correct**: Statements (a) and (b) are both factually accurate.
- **Option C is incorrect**: Statement (d) is false; soft iron is unsuitable for permanent magnets.
- **Option D is incorrect**: Both (c) and (d) are false.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-103",
    text: "A glass tube AB is filled with loose iron filings. The North pole of a strong bar magnet is repeatedly stroked along the tube from end A to end B. What magnetic polarity develops across the ends of the tube?",
    options: [
      "North pole at A and South pole at B",
      "South pole at A and North pole at B",
      "North poles at both ends A and B",
      "South poles at both ends A and B"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
This single-touch method of magnetization aligns the molecular magnetic domains of the iron filings:
1. When the North (N) pole of the magnet touches end \\(A\\), it attracts opposite South (S) poles of the nearby domain dipoles toward end \\(A\\).
2. As the North pole is stroked toward end \\(B\\), the South poles of the filings are drawn along behind it, leaving the North poles of the filings pointing toward end \\(B\\).
3. At end \\(B\\), as the North pole of the magnet is lifted away, the newly aligned North poles of the filings remain pointing toward \\(B\\).
Therefore, end \\(A\\) develops a **South pole**, and end \\(B\\) develops a **North pole**.

### 2. Physical Context & Practical Illustration:
Each tiny filing acts like a microscopic compass needle. Stroking with the North pole pulls the needle tails (South) toward the starting point \\(A\\) while repelling the needle tips (North) toward the destination point \\(B\\), creating a coherent macro-dipole along the tube.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The starting end develops the opposite polarity to the stroking pole, which is South, not North.
- **Option B is correct**: Stroking with a North pole from A to B leaves a South pole at starting point A and a North pole at exit point B.
- **Option C is incorrect**: A magnet must have opposite poles at opposite ends to conserve magnetic flux.
- **Option D is incorrect**: Cannot form identical poles at both extremities.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-104",
    text: "Which electrical physical quantity is measured in the SI unit 'Ohm' (Ω)?",
    options: [
      "Electric charge",
      "Electric current",
      "Electrical resistance",
      "Electric potential difference"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrical resistance (\\(R\\)) represents the opposition offered by a conductor to the flow of electric charge. According to Ohm's Law:
\\[
R = \\frac{V}{I}
\\]
In SI units, potential difference \\(V\\) is in Volts and current \\(I\\) is in Amperes:
\\[
1\\text{ Ohm (}\\Omega\\text{)} = 1\\text{ Volt per Ampere (V/A)} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-2}
\\]
The unit is named in honor of German physicist Georg Simon Ohm.

### 2. Physical Context & Practical Illustration:
A component with a resistance of \\(1\\,\\Omega\\) permits an electric current of exactly \\(1\\text{ Ampere}\\) to flow through it when an electromotive potential difference of \\(1\\text{ Volt}\\) is maintained across its ends.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Electric charge is measured in Coulombs (\\(\\text{C}\\)).
- **Option B is incorrect**: Electric current is measured in Amperes (\\(\\text{A}\\)).
- **Option C is correct**: Electrical resistance is measured in Ohms (\\(\\Omega\\)).
- **Option D is incorrect**: Electric potential difference is measured in Volts (\\(\\text{V}\\)).`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-105",
    text: "Two soft iron pins A and B are suspended by magnetic induction from the North pole of a strong bar magnet. Which statement correctly describes their magnetic behavior?",
    options: [
      "The attached tops of both pins become North poles, and their free hanging tips attract each other",
      "The attached tops of both pins become South poles, while their lower free hanging tips acquire North polarity and repel each other",
      "Both pins become unmagnetized and fall off immediately",
      "Pin A becomes a complete North magnet and Pin B becomes a complete South magnet"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When soft iron pins are brought in contact with or near the North pole of a bar magnet:
1. **Magnetic Induction**: The North pole of the magnet induces an opposite **South pole** at the contact head of each pin:
\\[
\\text{Head } \\longrightarrow \\text{South pole (attracted to magnet's North)}
\\]
2. **Induced Distal Pole**: By dipole conservation, the lower pointed tips of both pins acquire like **North poles**:
\\[
\\text{Tip } \\longrightarrow \\text{North pole}
\\]
3. **Repulsion Between Tips**: Because both hanging tips carry identical North poles, they exert mutual electrostatic/magnetic repulsion on each other, causing the pins to splay outward in a V-shape.

### 2. Physical Context & Practical Illustration:
Suspending several steel sewing needles or paper clips from the pole of a neodymium magnet visibly demonstrates this effect: their free hanging ends push away from one another because like induced poles mutually repel.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The attached tops must be South poles (attracted to the North pole), and like tips repel rather than attract.
- **Option B is correct**: Magnetic induction creates South poles at the attached ends and like North poles at the hanging tips, causing mutual repulsion.
- **Option C is incorrect**: Soft iron is ferromagnetic and remains strongly magnetized while in contact with the magnet.
- **Option D is incorrect**: Both pins undergo identical induction symmetry.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-106",
    text: "Which of the following statements is a fundamental, verified property of magnetic lines of force?",
    options: [
      "Magnetic lines of force frequently cross and intersect each other near strong poles",
      "Two magnetic lines of force never intersect each other at any point",
      "Magnetic lines of force begin on negative electric charges and terminate on positive charges",
      "Magnetic lines of force exist only in a vacuum and cannot penetrate matter"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition, the tangent to a magnetic line of force at any point gives the unique vector direction of the resultant magnetic field (\\(\\mathbf{B}\\)) at that location:
\\[
\\mathbf{B}(\\mathbf{r}) = B_x \\hat{i} + B_y \\hat{j} + B_z \\hat{k}
\\]
If two field lines were to intersect at a common point:
1. Two distinct tangents could be drawn at the point of intersection.
2. This would imply that the magnetic field has two simultaneous, conflicting directions at a single physical point in space.
Because a physical vector field can have only one unique resultant direction at any given point, **magnetic lines of force can never intersect**.

### 2. Physical Context & Practical Illustration:
If you place a magnetic compass needle at any location in a magnetic field, the needle points in exactly one definite direction. It cannot point in two directions at once. Therefore, magnetic field lines never cross.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Field lines crowd together where the field is strong, but they never cross or touch.
- **Option B is correct**: Magnetic lines of force never intersect, ensuring a unique field direction at every point in space.
- **Option C is incorrect**: Magnetic field lines form continuous closed loops without start or end points; electric field lines originate on positive charges and end on negative charges.
- **Option D is incorrect**: Magnetic fields penetrate freely through air, water, vacuum, and most non-magnetic materials.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-107",
    text: "Which of the following types of waves is NOT electromagnetic in nature?",
    options: [
      "Sound waves",
      "Ultraviolet rays",
      "X-rays",
      "Radio waves"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electromagnetic waves consist of time-varying, mutually perpendicular oscillating electric (\\(\\mathbf{E}\\)) and magnetic (\\(\\mathbf{B}\\)) fields propagating through space at the speed of light (\\(c = 3 \\times 10^8\\text{ m/s}\\)) without requiring a material medium:
\\[
c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}}
\\]
- Ultraviolet rays, X-rays, and Radio waves are all parts of the electromagnetic spectrum.
- **Sound waves**, by contrast, are **mechanical longitudinal waves** consisting of compressions and rarefactions of material particles (molecules), requiring a material medium (solid, liquid, or gas) to propagate:
\\[
v_{\\text{sound}} = \\sqrt{\\frac{B}{\\rho}}
\\]
Sound waves cannot travel through a vacuum and are not electromagnetic in nature.

### 2. Physical Context & Practical Illustration:
Radio communications travel freely from satellites through the vacuum of outer space to Earth because radio waves are electromagnetic. In contrast, the enormous acoustic roar of solar explosions cannot reach Earth because empty space has no air particles to transmit mechanical sound waves.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is correct**: Sound is a mechanical longitudinal wave requiring a physical material medium, not an electromagnetic wave.
- **Option B is incorrect**: Ultraviolet rays are high-frequency electromagnetic waves.
- **Option C is incorrect**: X-rays are electromagnetic radiation with wavelengths of \\(0.01\\text{ to } 10\\text{ nm}\\).
- **Option D is incorrect**: Radio waves are long-wavelength electromagnetic waves.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-108",
    text: "One watt-hour (Wh) of electrical energy is equivalent to how many Joules?",
    options: [
      "\\(6.3 \\times 10^3\\text{ J}\\)",
      "\\(6.3 \\times 10^{-7}\\text{ J}\\)",
      "\\(3.6 \\times 10^3\\text{ J}\\)",
      "\\(3.6 \\times 10^{-3}\\text{ J}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrical energy (\\(E\\)) is the product of power (\\(P\\)) and time (\\(t\\)):
\\[
E = P \\times t
\\]
By definition:
\\[
1\\text{ Watt (W)} = 1\\text{ Joule per second (J/s)}
\\]
\\[
1\\text{ hour (h)} = 60\\text{ minutes} \\times 60\\text{ seconds} = 3600\\text{ seconds}
\\]
Substituting into the energy relation:
\\[
1\\text{ Wh} = 1\\text{ W} \\times 3600\\text{ s} = 1\\left(\\frac{\\text{J}}{\\text{s}}\\right) \\times 3600\\text{ s} = 3600\\text{ J} = 3.6 \\times 10^3\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
If a \\(1\\text{ W}\\) LED indicator remains illuminated for exactly one hour, it consumes \\(1\\text{ watt-hour}\\) of electrical energy, corresponding to \\(3,600\\text{ Joules}\\). Similarly, \\(1\\text{ kilowatt-hour (kWh)} = 1000\\text{ Wh} = 3.6 \\times 10^6\\text{ J}\\), which forms the commercial billing unit of electricity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: \\(6.3 \\times 10^3\\text{ J}\\) transposes the digits \\(3\\) and \\(6\\).
- **Option B is incorrect**: \\(6.3 \\times 10^{-7}\\text{ J}\\) involves an erroneous negative exponent.
- **Option C is correct**: \\(1\\text{ Wh} = 1\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^3\\text{ J}\\).
- **Option D is incorrect**: \\(3.6 \\times 10^{-3}\\text{ J}\\) incorrectly uses a negative exponent.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-109",
    text: "During an experiment, it is observed that end B of metal rod X repels end C of metal rod Y. Which of the following conclusions is undeniably true?",
    options: [
      "Rod X is a magnet and rod Y is an unmagnetized magnetic material",
      "Rod Y is a magnet and rod X is an unmagnetized magnetic material",
      "Both rod X and rod Y are magnets",
      "Neither rod X nor rod Y is a magnet"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In magnetostatics:
1. **Attraction is not a definitive test**: A permanent magnet attracts both opposite magnetic poles AND unmagnetized ferromagnetic materials (via induced magnetism):
\\[
F_{\\text{attraction}} \\text{ can occur between a magnet and unmagnetized iron}
\\]
2. **Repulsion is the sure test of magnetism**: Electrostatic and magnetic repulsion occurs strictly and exclusively between two bodies carrying **like poles** (North repelling North, or South repelling South):
\\[
F_{\\text{repulsion}} > 0 \\iff \\text{Both bodies possess independent intrinsic magnetic dipoles}
\\]
Because end \\(B\\) repels end \\(C\\), both ends must possess like magnetic poles, proving definitively that **both rod X and rod Y are magnets**.

### 2. Physical Context & Practical Illustration:
If you bring an unmagnetized iron nail near either pole of a bar magnet, it will always be attracted, never repelled. The moment you observe two objects actively repelling each other, both must be magnetized.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: If rod Y were unmagnetized, it would be attracted to rod X, not repelled.
- **Option B is incorrect**: An unmagnetized rod X would be attracted to magnet Y, not repelled.
- **Option C is correct**: Repulsion is the definitive test of magnetism; therefore, both rods must be permanent magnets.
- **Option D is incorrect**: Non-magnetic rods exhibit no magnetic force between each other.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-110",
    text: "Two identical uncharged metal spheres X and Y supported on insulating stands are placed in physical contact. A negatively charged ebonite rod is brought near sphere X (without touching it). While the rod is held in position, sphere Y is separated from sphere X, and then the rod is removed. What are the resulting charges on spheres X and Y?",
    options: [
      "Sphere X is negative and Sphere Y is positive",
      "Both spheres X and Y acquire equal negative charges",
      "Sphere X is positive and Sphere Y is negative",
      "Both spheres X and Y remain completely neutral"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
This process is **charging by electrostatic induction**:
1. When the two metal spheres touch, they form a single continuous conductor.
2. Bringing a negatively charged rod near sphere \\(X\\) exerts an electrostatic repulsive force on free conduction electrons:
\\[
\\mathbf{F}_e = -e \\mathbf{E}
\\]
Free electrons are driven away from sphere \\(X\\) across the contact junction into sphere \\(Y\\).
3. Sphere \\(X\\) now has a deficit of electrons (net positive charge), while sphere \\(Y\\) has an excess of electrons (net negative charge).
4. Separating sphere \\(Y\\) from sphere \\(X\\) traps the transferred electrons on sphere \\(Y\\).
5. Removing the inducing negative rod allows the trapped charges to redistribute uniformly over each isolated sphere: sphere \\(X\\) remains **positively charged** and sphere \\(Y\\) remains **negatively charged**.

### 2. Physical Context & Practical Illustration:
Total charge is strictly conserved: \\(Q_{\\text{total}} = Q_X + Q_Y = 0\\). Charging by induction allows conductors to be charged with opposite polarities without transferring any charge from the inducing rod itself.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The near sphere \\(X\\) acquires the opposite (positive) charge, not negative.
- **Option B is incorrect**: Electrons are displaced from one sphere to the other, creating opposite charges, not identical like charges.
- **Option C is correct**: Sphere \\(X\\) acquires a positive charge and sphere \\(Y\\) acquires an equal negative charge.
- **Option D is incorrect**: Separating the spheres before removing the rod permanently isolates the induced charges.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-111",
    text: "What occurs at the microscopic level when a neutral glass rod is rubbed vigorously with a dry silk cloth?",
    options: [
      "Positive protons transfer from the silk cloth to the surface of the glass rod",
      "Loosely bound electrons transfer from the glass rod to the silk cloth, leaving the glass positively charged",
      "Frictional energy creates brand-new positive charges on the glass rod",
      "Frictional heat destroys all negative charges originally residing on the glass rod"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Charging by friction (triboelectric charging) is governed by differences in electronic work functions between contacting materials:
1. Glass has a lower electronic work function than silk; its valence electrons are less tightly bound to the atomic nuclei.
2. Mechanical friction brings atoms of both surfaces into intimate contact:
\\[
\\text{Glass} + \\text{Silk} \\xrightarrow{\\text{friction}} \\text{Glass}^{+q} + \\text{Silk}^{-q}
\\]
3. Mobile electrons are transferred from the surface of the glass rod to the silk cloth.
4. Glass loses electrons and acquires a net **positive charge**, while silk gains an equal number of electrons, acquiring an equal **negative charge**.
Protons remain tightly bound within atomic nuclei and do not move.

### 2. Physical Context & Practical Illustration:
Charge is conserved throughout the interaction: \\(\\Delta Q_{\\text{glass}} + \\Delta Q_{\\text{silk}} = 0\\). No new charges are created or destroyed; triboelectricity is strictly a transfer of existing subatomic electrons.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Protons are bound by strong nuclear forces inside the nucleus and never transfer during electrostatic rubbing.
- **Option B is correct**: Electrons transfer from the glass rod to the silk cloth, leaving the glass with a net positive charge.
- **Option C is incorrect**: Electric charge is universally conserved; friction transfers electrons, it does not create new charges.
- **Option D is incorrect**: Friction does not destroy electrons.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-112",
    text: "Domestic electricity consumption is billed based on units consumed (e.g., Rs. 3.36 per unit). What standard commercial electrical unit corresponds to '1 unit' of electrical energy?",
    options: [
      "Watt (W)",
      "Kilowatt-hour (kWh)",
      "Joule-second (J·s)",
      "Ampere-hour (Ah)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The commercial unit of electrical energy is the **Board of Trade Unit (B.O.T.U.)**, colloquially termed '1 unit' of electricity:
\\[
1\\text{ commercial unit} = 1\\text{ kilowatt-hour (kWh)}
\\]
Mathematically:
\\[
1\\text{ kWh} = 1\\text{ kilowatt} \\times 1\\text{ hour} = (1000\\text{ W}) \\times (3600\\text{ s}) = 3.6 \\times 10^6\\text{ Joules}
\\]
The Joule is too small for practical billing; a single household uses billions of Joules monthly. Hence, power utilities measure energy in kilowatt-hours (kWh).

### 2. Physical Context & Practical Illustration:
Running a \\(1000\\text{ W}\\) electric immersion water heater continuously for \\(1\\text{ hour}\\) consumes exactly \\(1\\text{ kWh}\\) (1 unit) of electrical energy on the household energy meter.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Watt is a unit of power (rate of energy consumption), not energy consumed over time.
- **Option B is correct**: 1 commercial unit of electricity equals 1 kilowatt-hour (\\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}\\)).
- **Option C is incorrect**: Joule-second is the unit of angular momentum or Planck's constant, not energy.
- **Option D is incorrect**: Ampere-hour is a unit of battery electric charge capacity (\\(1\\text{ Ah} = 3600\\text{ C}\\)), not energy.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-113",
    text: "Which of the following is the SI unit for measuring electrical resistance?",
    options: [
      "Watt (W)",
      "Ampere (A)",
      "Ohm (Ω)",
      "Coulomb (C)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Electrical resistance (\\(R\\)) is the physical property of a conductor that quantifies its opposition to the passage of electric current:
\\[
R = \\frac{V}{I}
\\]
In SI units:
\\[
1\\text{ Ohm (}\\Omega\\text{)} = \\frac{1\\text{ Volt}}{1\\text{ Ampere}} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-2}
\\]
The unit is named after German physicist Georg Simon Ohm, who formulated Ohm's law.

### 2. Physical Context & Practical Illustration:
A good conductor such as a heavy copper wire has a resistance of less than \\(0.01\\,\\Omega\\), whereas a human body's dry skin resistance is about \\(100,000\\,\\Omega\\) (\\(100\\text{ k}\\Omega\\)), and good glass or rubber insulators exceed \\(10^{12}\\,\\Omega\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: The Watt (\\(\\text{W}\\)) is the unit of electric power.
- **Option B is incorrect**: The Ampere (\\(\\text{A}\\)) is the unit of electric current.
- **Option C is correct**: The Ohm (\\(\\Omega\\)) is the SI unit of electrical resistance.
- **Option D is incorrect**: The Coulomb (\\(\\text{C}\\)) is the unit of electric charge.`
  },
  {
    questionCode: "MH-9-SCIT-3-3.1-OSC-114",
    text: "Which of the following metallic elements is strongly attracted by a permanent magnet?",
    options: [
      "Copper",
      "Cobalt",
      "Zinc",
      "Aluminium"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Magnetic materials are classified into three primary categories based on magnetic susceptibility (\\(\\chi_m\\)):
1. **Ferromagnetic Materials**: Possess permanent atomic magnetic dipole moments and strong quantum exchange interactions that align dipoles into domains, causing them to be strongly attracted toward regions of high magnetic fields (\\(\\chi_m \\gg 1\\)). The classic ferromagnetic elements are **Iron (Fe)**, **Cobalt (Co)**, and **Nickel (Ni)**.
2. **Paramagnetic Materials**: Weakly attracted (e.g., Aluminium, \\(\\chi_m \\approx +2 \\times 10^{-5}\\)).
3. **Diamagnetic Materials**: Weakly repelled (e.g., Copper, Zinc, \\(\\chi_m < 0\\)).

### 2. Physical Context & Practical Illustration:
Cobalt retains its ferromagnetism up to an exceptionally high Curie temperature of \\(1115^\\circ\\text{C}\\) (\\(1388\\text{ K}\\)), which is why cobalt is alloyed with iron, nickel, and aluminium (Alnico) to create powerful, heat-resistant permanent magnets.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A is incorrect**: Copper is diamagnetic and is very weakly repelled by a magnetic field.
- **Option B is correct**: Cobalt is one of the three primary ferromagnetic transition metals (along with iron and nickel) and is strongly attracted by magnets.
- **Option C is incorrect**: Zinc is diamagnetic and is weakly repelled by magnets.
- **Option D is incorrect**: Aluminium is weakly paramagnetic; its attraction is minuscule and imperceptible to hand-held magnets.`
  }
];

module.exports = { ch3_part4 };
