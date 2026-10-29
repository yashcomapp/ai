// scripts/ch2_part4.js - Questions 91 to 117 of Chapter 2 (Work and Energy)
module.exports = [
  {
    id: "MH-9-SCIT-2-2.1-OSC-091",
    text: "Which of the following sequences represents the correct chain of energy transformations in a hydroelectric power generating station?",
    options: [
      "Gravitational Potential Energy \\(\\rightarrow\\) Kinetic Energy \\(\\rightarrow\\) Electrical Energy",
      "Chemical Potential Energy \\(\\rightarrow\\) Thermal Energy \\(\\rightarrow\\) Electrical Energy",
      "Electrical Energy \\(\\rightarrow\\) Mechanical Energy \\(\\rightarrow\\) Nuclear Energy",
      "Kinetic Energy \\(\\rightarrow\\) Elastic Potential Energy \\(\\rightarrow\\) Radiant Energy"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a hydroelectric power station:
1. Water stored high in an elevated reservoir holds **Gravitational Potential Energy** (\(E_p = mgh\)).
2. As water descends rapidly through penstocks, potential energy converts into **Kinetic Energy** of rushing fluid (\(\\frac{1}{2}mv^2\)).
3. The rushing water strikes hydraulic turbine runners, transferring kinetic energy into rotating mechanical shafts.
4. The spinning turbines turn electric generators, converting mechanical rotation into **Electrical Energy** via electromagnetic induction.

### 2. Physical Context & Practical Illustration:
Facilities like the Koyna Hydroelectric Project in Maharashtra generate thousands of megawatts of clean electricity by channeling water down steep mountain penstocks.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Potential \\(\\rightarrow\\) Kinetic \\(\\rightarrow\\) Electrical)**: Correct. Accurate scientific progression from reservoir to turbine to electrical grid.
- **Option B**: Incorrect. Describes a coal-fired thermal power station.
- **Option C**: Incorrect. Reversed sequence; power stations produce electricity, not consume it.
- **Option D**: Incorrect. No elastic potential energy is involved.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-092",
    text: "When the speed of a moving object is doubled, by what factor does its kinetic energy increase?",
    options: [
      "It becomes \\(4\\) times its initial kinetic energy",
      "It becomes \\(2\\) times its initial kinetic energy",
      "It decreases to half of its initial kinetic energy",
      "It remains completely unchanged"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Kinetic energy is defined as:
\\[
E_k = \\frac{1}{2} m v^2
\\]
If the speed is doubled (\(v' = 2v\)):
\\[
E_k' = \\frac{1}{2} m (2v)^2 = \\frac{1}{2} m (4v^2) = 4 \\left(\\frac{1}{2} m v^2\\right) = 4 E_k
\\]
The kinetic energy becomes **4 times** (quadruples) its original value.

### 2. Physical Context & Practical Illustration:
This quadratic scaling explains why braking distance quadruples when vehicle speed is doubled under constant braking deceleration (\(v^2 = 2as \\implies s \\propto v^2\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (4 times)**: Correct. Quadratic relationship (\(E_k \\propto v^2 \\implies 2^2 = 4\)).
- **Option B (2 times)**: Incorrect. Linear scaling applies to momentum (\(p = mv\)), not kinetic energy.
- **Option C (Half)**: Incorrect. Kinetic energy increases with speed, never decreases.
- **Option D (Unchanged)**: Incorrect. Kinetic energy depends directly on speed.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-093",
    text: "Which form of energy is stored in the drawn and stretched bowstring of an archer just before the arrow is released?",
    options: [
      "Elastic potential energy",
      "Gravitational potential energy",
      "Translational kinetic energy",
      "Chemical bond energy"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an archer pulls back a bowstring, work is performed against the elastic restoring forces of the flexing bow limbs. This mechanical work is stored in the deformed structure of the bow as **elastic potential energy**:
\\[
E_p = \\frac{1}{2} k x^2
\\]
When the string is released, this stored elastic potential energy is instantaneously transferred into the arrow as **kinetic energy** (\(\\frac{1}{2}mv^2\)).

### 2. Physical Context & Practical Illustration:
Olympic archers use carbon-composite recurve bows that can store over \(50\\text{ Joules}\) of elastic potential energy, propelling an arrow at speeds exceeding \(200\\text{ km/h}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Elastic potential energy)**: Correct. Energy stored through physical elastic deformation.
- **Option B (Gravitational potential energy)**: Incorrect. The bow is not elevated to store gravitational energy.
- **Option C (Translational kinetic energy)**: Incorrect. The held arrow and bow are stationary (\(v = 0\)).
- **Option D (Chemical bond energy)**: Incorrect. Deformation is macroscopic physical strain, not a chemical reaction.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-094",
    text: "A machine performs \\(1200\\text{ J}\\) of mechanical work in \\(2\\text{ minutes}\\). What is its average power output?",
    options: [
      "\\(10\\text{ W}\\)",
      "\\(600\\text{ W}\\)",
      "\\(2400\\text{ W}\\)",
      "\\(24\\text{ W}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Power is the rate of doing work:
\\[
P = \\frac{W}{t}
\\]
Convert the time interval into standard SI seconds:
\\[
t = 2\\text{ minutes} = 2 \\times 60\\text{ s} = 120\\text{ s}
\\]
Given work \(W = 1200\\text{ J}\):
\\[
P = \\frac{1200\\text{ J}}{120\\text{ s}} = 10\\text{ W}
\\]

### 2. Physical Context & Practical Illustration:
A power rating of \(10\\text{ W}\) means the device delivers \(10\\text{ Joules}\) of energy each second, equivalent to the power required to operate a small decorative LED bulb.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (10 W)**: Correct. Exact computation: \(1200 / 120 = 10\\text{ W}\).
- **Option B (600 W)**: Incorrect. Erroneously divides by 2 minutes directly without converting to seconds (\(1200 / 2 = 600\)).
- **Option C (2400 W)**: Incorrect. Multiplies work by time (\(1200 \\times 2\)).
- **Option D (24 W)**: Incorrect. Calculation error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-095",
    text: "While taking a measurement with a Vernier caliper, an observer adds the main scale reading directly to the Vernier scale coincidence division number before multiplying by the least count. What type of experimental error is this?",
    options: [
      "Instrumental zero error",
      "Environmental parallax error",
      "Careless calculation and algorithmic error",
      "Random statistical fluctuation"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The standard formula for total reading (TR) with a Vernier caliper is:
\\[
\\text{TR} = \\text{MSR} + (\\text{VSR} \\times \\text{LC})
\\]
where MSR is Main Scale Reading, VSR is Vernier Scale division coincidence, and LC is Least Count.
If an experimenter erroneously computes:
\\[
\\text{Wrong TR} = (\\text{MSR} + \\text{VSR}) \\times \\text{LC}
\\]
they have violated the mathematical order of operations and algorithmic formula. This is a human **careless calculation error**.

### 2. Physical Context & Practical Illustration:
For example, if \(\\text{MSR} = 2.5\\text{ cm}\), \(\\text{VSR} = 4\), and \(\\text{LC} = 0.01\\text{ cm}\):
- Correct: \(2.5 + (4 \\times 0.01) = 2.54\\text{ cm}\).
- Wrong: \((2.5 + 4) \\times 0.01 = 0.065\\text{ cm}\) (completely absurd result).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Zero error)**: Incorrect. Zero error is an instrumental offset present when jaws are fully closed.
- **Option B (Parallax error)**: Incorrect. Parallax arises from looking at scales at an angle.
- **Option C (Calculation error)**: Correct. Applying an erroneous mathematical formula during data reduction.
- **Option D (Random fluctuation)**: Incorrect. This is a systematic human procedural error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-096",
    text: "In a physical equation \\(a = \\frac{P}{t}\\), if \\(P\\) has SI units of \\(\\text{m/s}\\) and \\(t\\) has SI units of \\(\\text{s}\\), what is the SI unit of \\(a\\)?",
    options: [
      "\\(\\text{m/s}\\)",
      "\\(\\text{m}\\)",
      "\\(\\text{m/s}^2\\)",
      "\\(\\text{s}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Using dimensional analysis:
\\[
[a] = \\frac{[P]}{[t]}
\\]
Given:
- Unit of \(P = \\text{m/s} = \\text{m}\\cdot\\text{s}^{-1}\) (velocity)
- Unit of \(t = \\text{s}\) (time)

Substituting into the quotient:
\\[
[a] = \\frac{\\text{m/s}}{\\text{s}} = \\frac{\\text{m}}{\\text{s} \\times \\text{s}} = \\frac{\\text{m}}{\\text{s}^2} = \\text{m/s}^2
\\]
This represents the standard SI unit of linear **acceleration**.

### 2. Physical Context & Practical Illustration:
Acceleration measures how rapidly velocity changes per unit time:
\\[
a = \\frac{\\Delta v}{\\Delta t} \\implies \\text{Units: } \\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(\\text{m/s}\\))**: Incorrect. This is the unit of speed/velocity (\(P\)), without dividing by time.
- **Option B (\\(\\text{m}\\))**: Incorrect. Unit of length or displacement.
- **Option C (\\(\\text{m/s}^2\\))**: Correct. Exact algebraic quotient: \(\\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2\).
- **Option D (\\(\\text{s}\\))**: Incorrect. Unit of time.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-097",
    text: "Which of the following physical quantities is one of the seven fundamental (base) SI quantities?",
    options: [
      "Density",
      "Mass",
      "Force",
      "Velocity"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the International System of Units (SI), there are **seven fundamental base quantities** that are defined independently and cannot be expressed in terms of other quantities:
1. Length (meter, \(\\text{m}\))
2. **Mass (kilogram, \\(\\text{kg}\\))**
3. Time (second, \(\\text{s}\))
4. Electric Current (Ampere, \(\\text{A}\))
5. Thermodynamic Temperature (Kelvin, \(\\text{K}\))
6. Amount of Substance (mole, \(\\text{mol}\))
7. Luminous Intensity (candela, \(\\text{cd}\))

All other quantities (density \(\\frac{\\text{kg}}{\\text{m}^3}\), velocity \(\\frac{\\text{m}}{\\text{s}}\), force \(\\text{kg}\\cdot\\text{m/s}^2\)) are derived quantities.

### 2. Physical Context & Practical Illustration:
Mass is an intrinsic property of matter that quantifies its inertia (resistance to acceleration) and gravitational attraction, forming one of the core base pillars of classical physics.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Density)**: Derived quantity (\(\\text{mass} / \\text{volume}\)).
- **Option B (Mass)**: Correct. One of the fundamental base quantities of the SI system.
- **Option C (Force)**: Derived quantity (\(\\text{mass} \\times \\text{acceleration}\)).
- **Option D (Velocity)**: Derived quantity (\(\\text{displacement} / \\text{time}\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-098",
    text: "Two identical wooden blocks of equal mass \\(m\\) are placed on two tables of heights \\(h_1\\) and \\(h_2\\) respectively, where \\(h_1 < h_2\\). What is the relationship between their gravitational potential energies \\(U_1\\) and \\(U_2\\) relative to the floor?",
    options: [
      "\\(U_1 < U_2\\)",
      "\\(U_1 > U_2\\)",
      "\\(U_1 = U_2\\)",
      "\\(U_1 + U_2 = 0\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy of an object of mass \(m\) at height \(h\) above a reference datum is:
\\[
U = mgh
\\]
For the two identical blocks:
\\[
U_1 = mgh_1 \\quad \\text{and} \\quad U_2 = mgh_2
\\]
Subtracting the two values:
\\[
U_2 - U_1 = mg(h_2 - h_1)
\\]
Since \(h_2 > h_1\) and \(m, g > 0\):
\\[
h_2 - h_1 > 0 \\implies U_2 - U_1 > 0 \\implies U_1 < U_2
\\]
The block placed on the higher table possesses greater gravitational potential energy.

### 2. Physical Context & Practical Illustration:
Falling from the higher table (\(h_2\)) would allow gravity to do more work on the block (\(W = mgh_2\)), imparting greater kinetic energy upon impact with the floor.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(U_1 < U_2\\))**: Correct. Because \(h_1 < h_2\), \(mgh_1 < mgh_2\).
- **Option B (\\(U_1 > U_2\\))**: Incorrect. Higher elevation increases potential energy, not decreases it.
- **Option C (\\(U_1 = U_2\\))**: Incorrect. Potential energies are equal only if table heights are identical.
- **Option D (\\(U_1 + U_2 = 0\\))**: Incorrect. Both potential energies are strictly positive above the floor.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-099",
    text: "Which of the following energy resources is classified as a conventional, non-renewable source of energy?",
    options: [
      "Flowing water in a mountain stream",
      "Ocean tidal wave energy",
      "Direct solar radiation",
      "Coal and natural gas"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
- **Conventional / Non-renewable resources**: Energy sources that were formed over geological timescales (hundreds of millions of years) from fossilized organic matter. Once extracted and burned, they cannot be replenished on human timescales:
\\[
\\text{Coal, Crude Petroleum, Natural Gas}
\\]
- **Non-conventional / Renewable resources**: Natural flows that replenish cyclically and continuously without exhaustion:
\\[
\\text{Solar, Wind, Hydro, Geothermal, Ocean Tidal}
\\]

### 2. Physical Context & Practical Illustration:
Combustion of fossil fuels releases carbon dioxide and sulfur pollutants. Global energy policy focuses heavily on replacing conventional coal power plants with solar and hydroelectric installations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Flowing water)**: Renewable hydroelectric source.
- **Option B (Ocean tidal waves)**: Renewable gravitational/orbital energy source.
- **Option C (Direct solar radiation)**: Inexhaustible renewable source.
- **Option D (Coal and natural gas)**: Correct. Classical conventional, non-renewable fossil energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-100",
    text: "What is the equivalent value of one commercial unit of electrical energy, \\(1\\text{ kilowatt-hour (kWh)}\\), expressed in Joules?",
    options: [
      "\\(3.6 \\times 10^6\\text{ J}\\)",
      "\\(3.6 \\times 10^5\\text{ J}\\)",
      "\\(1.0 \\times 10^3\\text{ J}\\)",
      "\\(3.6 \\times 10^3\\text{ J}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Recall the definition of electrical units:
\\[
1\\text{ kW} = 1000\\text{ W} = 10^3\\text{ J/s}
\\]
\\[
1\\text{ hour} = 60\\text{ minutes} \\times 60\\text{ seconds} = 3600\\text{ s}
\\]
Multiplying power by time to calculate energy:
\\[
1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3,600,000\\text{ W}\\cdot\\text{s} = 3.6 \\times 10^6\\text{ J}
\\]
Thus, \(1\\text{ unit (kWh)} = 3.6\\text{ Mega-Joules (MJ)}\).

### 2. Physical Context & Practical Illustration:
Electric utility bills meter household consumption in kilowatt-hours. Using a \(1000\\text{ W}\) microwave oven continuously for one hour consumes exactly \(1\\text{ kWh}\), which equals \(3.6\\) million Joules of energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(3.6 \\times 10^6\\text{ J}\\))**: Correct. Exact conversion factor: \(1000 \\times 3600 = 3.6 \\times 10^6\\text{ J}\).
- **Option B (\\(3.6 \\times 10^5\\text{ J}\\))**: Incorrect. Missing a factor of 10.
- **Option C (\\(1.0 \\times 10^3\\text{ J}\\))**: Incorrect. Confuses \(1\\text{ kW}\) with \(1\\text{ kWh}\).
- **Option D (\\(3.6 \\times 10^3\\text{ J}\\))**: Incorrect. Omits the 1000 W factor.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-101",
    text: "How many meters are equal to one nanometer (\\(1\\text{ nm}\\))?",
    options: [
      "\\(10^{-9}\\text{ m}\\) (one-billionth of a meter)",
      "\\(10^{-2}\\text{ m}\\) (one-hundredth of a meter)",
      "\\(10^{-6}\\text{ m}\\) (one-millionth of a meter)",
      "\\(10^{-3}\\text{ m}\\) (one-thousandth of a meter)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the metric system of SI prefixes:
- Centi (\(\\text{c}\)) \(= 10^{-2}\) (one-hundredth)
- Milli (\(\\text{m}\)) \(= 10^{-3}\) (one-thousandth)
- Micro (\(\\mu\)) \(= 10^{-6}\) (one-millionth)
- **Nano (\\(\\text{n}\\)) \\(= 10^{-9}\\) (one-billionth)**
- Pico (\(\\text{p}\)) \(= 10^{-12}\) (one-trillionth)

Therefore:
\\[
1\\text{ nm} = 10^{-9}\\text{ m} = \\frac{1}{1,000,000,000}\\text{ m}
\\]

### 2. Physical Context & Practical Illustration:
Nanotechnology manipulates matter at the scale of atoms and molecules. For instance, the diameter of a DNA double helix is approximately \(2\\text{ nm}\), and modern semiconductor microchip transistors are manufactured with feature sizes under \(5\\text{ nm}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(10^{-9}\\text{ m}\\))**: Correct. Nano corresponds to \(10^{-9}\) (one-billionth).
- **Option B (\\(10^{-2}\\text{ m}\\))**: Incorrect. This is one centimeter (\(\\text{cm}\)).
- **Option C (\\(10^{-6}\\text{ m}\\))**: Incorrect. This is one micrometer/micron (\(\\mu\\text{m}\)).
- **Option D (\\(10^{-3}\\text{ m}\\))**: Incorrect. This is one millimeter (\(\\text{mm}\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-102",
    text: "If the mass of a moving object is increased to \\(4\\) times its original value, what must be the change in its velocity to keep its kinetic energy strictly constant?",
    options: [
      "Double the velocity",
      "Triple the velocity",
      "Half the velocity",
      "No change in velocity"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Initial kinetic energy:
\\[
E_k = \\frac{1}{2} m v^2
\\]
Let the new mass be \(m' = 4m\), and the new velocity be \(v'\).
For kinetic energy to remain constant (\(E_k' = E_k\)):
\\[
\\frac{1}{2} m' (v')^2 = \\frac{1}{2} m v^2
\\]
\\[
\\frac{1}{2} (4m) (v')^2 = \\frac{1}{2} m v^2 \\implies 4(v')^2 = v^2
\\]
Taking the square root on both sides:
\\[
2v' = v \\implies v' = \\frac{v}{2}
\\]
Thus, the velocity must be **halved** (reduced to one-half of its original value).

### 2. Physical Context & Practical Illustration:
Because kinetic energy depends quadratically on velocity (\(v^2\)) but only linearly on mass (\(m\)), doubling mass can be offset by a smaller reduction in speed. A 4-fold increase in mass requires cutting the velocity in half to maintain identical kinetic energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Double)**: Incorrect. Doubling velocity while quadrupling mass would increase kinetic energy by \(4 \\times 2^2 = 16\) times!
- **Option B (Triple)**: Incorrect. Would increase kinetic energy drastically.
- **Option C (Half the velocity)**: Correct. \((1/2)^2 = 1/4\), exactly canceling the factor of 4 from mass: \(4 \\times \\frac{1}{4} = 1\).
- **Option D (No change)**: Incorrect. Kinetic energy would quadruple if velocity were unchanged.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-103",
    text: "An object is dropped from a stationary helicopter hovering at high altitude. In the absence of significant air resistance, which of the following physical quantities of the falling body continuously increases during the descent?",
    options: [
      "Acceleration due to gravity",
      "Kinetic energy",
      "Gravitational potential energy",
      "Total mechanical energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
During free fall from rest (\(u = 0\)):
- Acceleration remains constant: \(a = g = 9.8\\text{ m/s}^2\).
- Total mechanical energy remains constant: \(E = E_k + E_p = \\text{constant}\).
- Vertical downward velocity increases: \(v = gt\).
- Gravitational potential energy decreases: \(E_p = mgy\\) (as height \(y\) drops).
- Kinetic energy:
\\[
E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} m (gt)^2
\\]
Because velocity \(v\) increases with time, the **kinetic energy increases continuously**.

### 2. Physical Context & Practical Illustration:
The falling object converts its initial gravitational potential energy into kinetic energy, gaining speed every second until it impacts the surface (or reaches aerodynamic terminal velocity).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Acceleration)**: Incorrect. Near Earth's surface, \(g \\approx 9.8\\text{ m/s}^2\) is constant.
- **Option B (Kinetic energy)**: Correct. \(E_k = \\frac{1}{2}mv^2\) increases as the falling body accelerates.
- **Option C (Potential energy)**: Incorrect. Height decreases, so \(E_p = mgy\) decreases.
- **Option D (Total mechanical energy)**: Incorrect. Conserved and constant in free fall.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-0104",
    text: "A LASER beam consists of an intense, coherent, and monochromatic stream of which form of energy?",
    options: [
      "Acoustic sound energy",
      "Chemical potential energy",
      "Electromagnetic radiant light energy",
      "Nuclear binding energy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The acronym **LASER** stands for:
*Light Amplification by Stimulated Emission of Radiation*.
A laser operates when excited atoms are stimulated to drop to lower energy states by incoming photons, emitting secondary photons that have identical frequency, phase, and polarization:
\\[
\\Delta E = h\\nu
\\]
This produces a coherent beam of **electromagnetic radiant light energy**.

### 2. Physical Context & Practical Illustration:
Because laser light waves travel in perfect lockstep (coherence) with minimal beam divergence, they can focus extreme energy densities onto microscopic spots for precision laser eye surgery, barcode scanning, and optical fiber telecommunications.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Sound energy)**: Incorrect. Lasers are electromagnetic photons, not acoustic pressure waves.
- **Option B (Chemical energy)**: Incorrect. Lasers emit radiant light photons, not chemical bond changes.
- **Option C (Radiant light energy)**: Correct. Lasers are coherent electromagnetic optical radiation.
- **Option D (Nuclear energy)**: Incorrect. Standard lasers involve atomic orbital electron transitions, not nuclear decay.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-105",
    text: "Two bodies, one light with mass \\(m_1\\) and one heavy with mass \\(m_2\\) (\\(m_1 < m_2\\)), have strictly equal linear momentum (\\(p_1 = p_2\\)). Which body possesses greater kinetic energy?",
    options: [
      "The heavy body",
      "The lighter body",
      "Both possess strictly identical kinetic energy",
      "Cannot be determined without knowing their heights"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The relation between kinetic energy \(E_k\) and momentum \(p\) is:
\\[
E_k = \\frac{p^2}{2m}
\\]
Given that both bodies have the exact same momentum (\(p = \\text{constant}\)):
\\[
E_k \\propto \\frac{1}{m}
\\]
Kinetic energy is **inversely proportional** to mass for a fixed momentum.
Taking the ratio:
\\[
\\frac{E_{k1}}{E_{k2}} = \\frac{m_2}{m_1}
\\]
Since \(m_1 < m_2\) (body 1 is lighter), \(\\frac{m_2}{m_1} > 1\\):
\\[
E_{k1} > E_{k2}
\\]
Therefore, the **lighter body possesses greater kinetic energy**.

### 2. Physical Context & Practical Illustration:
When a rifle fires a bullet, conservation of linear momentum dictates that the bullet and the rifle experience equal and opposite momentum:
\\[
p_{\\text{bullet}} = p_{\\text{rifle}}
\\]
However, because the bullet is thousands of times lighter than the rifle (\(m_{\\text{bullet}} \\ll M_{\\text{rifle}}\)), almost all the explosion's kinetic energy goes into the bullet (\(E_k \\propto 1/m\)), allowing it to penetrate targets while the heavy rifle merely delivers a manageable recoil kick.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Heavy body)**: Incorrect. Inversely proportional; larger mass results in lower kinetic energy for equal momentum.
- **Option B (Lighter body)**: Correct. \(E_k = \\frac{p^2}{2m} \\implies\) smaller mass yields higher kinetic energy.
- **Option C (Identical)**: Incorrect. Equal momentum does not mean equal kinetic energy when masses differ.
- **Option D (Cannot be determined)**: Incorrect. Decisively proven by \(E_k = \\frac{p^2}{2m}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-106",
    text: "By which nuclear reaction is the immense continuous energy output of the Sun produced?",
    options: [
      "Nuclear fusion of light hydrogen nuclei into helium",
      "Nuclear fission of heavy uranium nuclei",
      "Exothermic chemical combustion of hydrocarbons",
      "Gravitational radioactive decay of carbon-14"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the Sun's core, at temperatures exceeding \(15 \\times 10^6\\text{ K}\) and extreme pressures, hydrogen nuclei undergo the **proton-proton chain reaction** of **nuclear fusion**:
\\[
4\\,^1\\text{H} \\longrightarrow \\,^4\\text{He} + 2e^+ + 2\\nu_e + 26.7\\text{ MeV}
\\]
The total mass of the resulting helium nucleus is slightly less than the sum of the four initial protons (\(\\Delta m = 0.0287\\text{ u}\)). By Einstein's equation:
\\[
E = \\Delta m \\cdot c^2
\\]
This mass defect is converted directly into vast quantities of radiant energy.

### 2. Physical Context & Practical Illustration:
Nuclear fusion powers every star in the universe. The Sun fuses approximately \(600\\) million tonnes of hydrogen every second, radiating the energy that sustains life, wind, and water cycles on Earth.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Nuclear fusion)**: Correct. Light hydrogen nuclei fuse into helium at stellar temperatures.
- **Option B (Nuclear fission)**: Incorrect. Fission is the splitting of heavy elements (used in terrestrial reactors), not stellar cores.
- **Option C (Chemical combustion)**: Incorrect. Chemical burning could only power the Sun for a few thousand years; the Sun is over 4.6 billion years old.
- **Option D (Radioactive decay)**: Incorrect. Minor isotopic decay cannot explain stellar luminosities.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-107",
    text: "Which of the following is the primary source of electrical power used to operate onboard scientific instruments in artificial Earth satellites?",
    options: [
      "Internal combustion diesel engines",
      "Photovoltaic solar panels with rechargeable storage batteries",
      "High-pressure hydraulic steam boilers",
      "Disposable lead-acid starter batteries"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In space orbit outside Earth's atmosphere, satellites receive an intense solar flux of approximately \(1361\\text{ W/m}^2\). Satellites deploy large wings of **photovoltaic solar cells** made of crystalline silicon or gallium arsenide.
These cells convert sunlight directly into electricity via the photovoltaic effect:
\\[
\\text{Solar Radiant Photons} \\longrightarrow \\text{Electrical Energy}
\\]
During the illuminated portion of each orbit, solar panels power instruments and charge onboard batteries (e.g., lithium-ion), which sustain satellite operations during orbital eclipse periods when passing through Earth's shadow.

### 2. Physical Context & Practical Illustration:
Communication satellites, weather monitoring satellites, and the International Space Station (ISS) operate continuously for 15+ years without refueling by relying entirely on solar array wings.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Diesel engines)**: Incorrect. Combustion engines require atmospheric oxygen and heavy fuel tanks, impossible in vacuum.
- **Option B (Solar panels + batteries)**: Correct. Clean, lightweight, inexhaustible power source in Earth orbit.
- **Option C (Steam boilers)**: Incorrect. Impractical in zero-gravity space environments.
- **Option D (Disposable batteries)**: Incorrect. Non-rechargeable batteries would deplete within days.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-108",
    text: "Which of the following values represents \\(200\\text{ square centimeters}\\) (\\(200\\text{ cm}^2\\)) converted into square meters (\\(\\text{m}^2\\))?",
    options: [
      "\\(2\\text{ m}^2\\)",
      "\\(0.2\\text{ m}^2\\)",
      "\\(0.02\\text{ m}^2\\) (or \\(2 \\times 10^{-2}\\text{ m}^2\\))",
      "\\(2000\\text{ m}^2\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Recall the basic linear length relation between meters and centimeters:
\\[
1\\text{ m} = 100\\text{ cm} = 10^2\\text{ cm} \\implies 1\\text{ cm} = 10^{-2}\\text{ m}
\\]
Squaring both sides to convert area:
\\[
1\\text{ cm}^2 = (10^{-2}\\text{ m})^2 = 10^{-4}\\text{ m}^2 = \\frac{1}{10,000}\\text{ m}^2
\\]
Now convert \(200\\text{ cm}^2\):
\\[
200\\text{ cm}^2 = 200 \\times 10^{-4}\\text{ m}^2 = \\frac{200}{10,000}\\text{ m}^2 = 0.02\\text{ m}^2 = 2 \\times 10^{-2}\\text{ m}^2
\\]

### 2. Physical Context & Practical Illustration:
A standard sheet of notebook paper has an area of roughly \(600\\text{ cm}^2 = 0.06\\text{ m}^2\). An area of \(200\\text{ cm}^2\) is approximately one-third of a notebook page.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (2 m^2)**: Incorrect. Divides by 100 instead of \(100^2\).
- **Option B (0.2 m^2)**: Incorrect. Divides by 1000.
- **Option C (0.02 m^2)**: Correct. Exact conversion: \(\\frac{200}{10,000} = 0.02\\text{ m}^2\).
- **Option D (2000 m^2)**: Incorrect. Erroneously multiplies instead of dividing.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-109",
    text: "In the MKS (SI) system of units, which of the following physical quantities is measured in Joules?",
    options: [
      "Mechanical Work and Energy",
      "Linear Momentum",
      "Mechanical Power",
      "Gravitational Force"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the MKS (Meter-Kilogram-Second) / SI system:
- Unit of Force: Newton (\(\\text{N} = \\text{kg}\\cdot\\text{m/s}^2\))
- Unit of Work / Energy:
\\[
\\text{Work} = \\text{Force} \\times \\text{Displacement} = \\text{N}\\cdot\\text{m} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2} = \\text{Joule (J)}
\\]
All forms of work (mechanical, electrical) and energy (kinetic, potential, heat) are measured in **Joules**.

### 2. Physical Context & Practical Illustration:
Momentum is measured in \(\\text{kg}\\cdot\\text{m/s}\), power in Watts (\(\\text{J/s}\)), and force in Newtons. Only work and energy share the Joule.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Work and Energy)**: Correct. Both are measured in Joules (\(\\text{J}\)).
- **Option B (Linear Momentum)**: Incorrect. Measured in \(\\text{kg}\\cdot\\text{m/s}\) or \(\\text{N}\\cdot\\text{s}\).
- **Option C (Power)**: Incorrect. Measured in Watts (\(\\text{W}\)).
- **Option D (Force)**: Incorrect. Measured in Newtons (\(\\text{N}\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-110",
    text: "A person fetches water from a deep well using a single fixed pulley. What types of motion do the rotating pulley wheel and the ascending bucket of water undergo?",
    options: [
      "The motion of the bucket is translational (rectilinear), while that of the pulley wheel is rotational",
      "The motion of the pulley wheel is translational, while that of the bucket is rotational",
      "Both the bucket and the pulley wheel undergo purely translational motion",
      "Both the bucket and the pulley wheel undergo purely rotational motion"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the kinematics of both components:
1. **Pulley Wheel**: Mounted on a fixed axle supported by a bracket. Its center of mass does not move linearly; every particle of the wheel rotates about the fixed central axis in a circular path. Hence, it undergoes **rotational motion**.
2. **Bucket of Water**: Suspended from the rope, moving in a straight vertical path upwards from the water surface to the well curb. All particles of the bucket move along parallel straight paths with identical velocity. Hence, it undergoes **translational (rectilinear) motion**.

### 2. Physical Context & Practical Illustration:
This illustrates how simple machines can couple different types of mechanical motion: rotational motion of the wheel guides and converts the pulling motion into vertical translational lift.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Bucket translational, Pulley rotational)**: Correct. Bucket moves straight up; pulley spins on fixed axle.
- **Option B**: Incorrect. Reverses the two motions.
- **Option C**: Incorrect. The pulley wheel spins and does not translate.
- **Option D**: Incorrect. The bucket moves linearly upwards without spinning.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-111",
    text: "At what height above the ground will an object of mass \\(1\\text{ kg}\\) possess a gravitational potential energy of exactly \\(1\\text{ Joule}\\)? (Take \\(g = 9.8\\text{ m/s}^2\\))",
    options: [
      "\\(\\frac{1}{9.8}\\text{ m} \\approx 10.2\\text{ cm}\\)",
      "\\(9.8\\text{ m}\\)",
      "\\(1.0\\text{ m}\\)",
      "\\(98\\text{ cm}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is given by:
\\[
E_p = mgh
\\]
Rearranging to solve for height \(h\):
\\[
h = \\frac{E_p}{mg}
\\]
Substitute the given values:
- \(E_p = 1\\text{ J}\)
- \(m = 1\\text{ kg}\)
- \(g = 9.8\\text{ m/s}^2\)
\\[
h = \\frac{1}{1 \\times 9.8}\\text{ m} = \\frac{1}{9.8}\\text{ m} \\approx 0.10204\\text{ m} = 10.2\\text{ cm}
\\]

### 2. Physical Context & Practical Illustration:
One Joule is a relatively modest unit of mechanical energy: lifting a standard \(1\\text{ kg}\) bag of sugar by just about \(10.2\\text{ cm}\) (roughly 4 inches) stores exactly \(1\\text{ Joule}\) of potential energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(\\frac{1}{9.8}\\text{ m} \\approx 10.2\\text{ cm}\\))**: Correct. Exact algebraic solution of \(h = \\frac{E_p}{mg}\).
- **Option B (9.8 m)**: Incorrect. Multiplies \(g\) instead of dividing (\(h = mg / E_p\)).
- **Option C (1.0 m)**: Incorrect. Completely ignores gravitational acceleration \(g\).
- **Option D (98 cm)**: Incorrect. Decimal calculation error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-112",
    text: "Which of the following groups consists EXCLUSIVELY of scalar physical quantities?",
    options: [
      "Speed, Velocity, Acceleration",
      "Work, Energy, Power",
      "Displacement, Force, Momentum",
      "Velocity, Weight, Kinetic Energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
- **Scalars** have magnitude only:
  - **Work** (\(W = \\vec{F} \\cdot \\vec{s}\), scalar dot product)
  - **Energy** (capacity to do work, scalar)
  - **Power** (\(P = W/t\), scalar rate of energy transfer)
  - Speed, mass, time, temperature
- **Vectors** possess both magnitude and spatial direction:
  - Velocity (\(\\vec{v}\)), Acceleration (\(\\vec{a}\)), Force (\(\\vec{F}\)), Weight (\(\\vec{W}\)), Displacement (\(\\vec{s}\)), Momentum (\(\\vec{p}\)).

### 2. Physical Context & Practical Illustration:
Work, energy, and power add together via ordinary scalar addition without requiring trigonometric decomposition or vector component rules.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. Velocity and acceleration are vectors.
- **Option B (Work, Energy, Power)**: Correct. All three are purely scalar quantities.
- **Option C**: Incorrect. Displacement, force, and momentum are all vectors.
- **Option D**: Incorrect. Velocity and weight are vectors.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-113",
    text: "Einstein's mass-energy equivalence equation, \\(E = mc^2\\), describes the fundamental release of energy in which physical process?",
    options: [
      "Nuclear reactions (fission and fusion)",
      "Hydroelectric water turbine rotation",
      "Frictional braking of a motor car",
      "Stretching of a mechanical spring"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In 1905, Albert Einstein formulated the principle of mass-energy equivalence:
\\[
E = \\Delta m \\cdot c^2
\\]
where \(\\Delta m\) is the **mass defect** (loss of invariant rest mass) and \(c = 3 \\times 10^8\\text{ m/s}\) is the speed of light in vacuum.
Because \(c^2 \\approx 9 \\times 10^{16}\\text{ m}^2/\\text{s}^2\) is immense, even an infinitesimal loss of mass releases colossal energy. This conversion occurs significantly in **nuclear fission** and **nuclear fusion** reactions where nuclear binding energy changes produce a measurable mass defect.

### 2. Physical Context & Practical Illustration:
In the Sun's core, the fusion of hydrogen into helium converts approximately \(4.3\\) million tonnes of mass into radiant solar energy every single second, following \(E = mc^2\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Nuclear reactions)**: Correct. Measurable mass defects convert into binding energy release.
- **Option B (Hydroelectric)**: Incorrect. Involves macroscopic gravitational potential energy, not mass defect.
- **Option C (Frictional braking)**: Incorrect. Mechanical kinetic energy converts into thermal molecular vibration.
- **Option D (Stretching spring)**: Incorrect. Governed by Hooke's law and elastic potential energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-114",
    text: "Which physical quantity is obtained when we multiply the mass, acceleration, and velocity of an object together (\\(m \\times a \\times v\\))?",
    options: [
      "Linear Momentum",
      "Mechanical Work",
      "Mechanical Power (rate of energy transfer)",
      "Gravitational Potential Energy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the product using Newton's laws and definitions:
1. By Newton's second law:
\\[
\\text{Force } F = m \\times a
\\]
2. Multiplying force by velocity:
\\[
(m \\times a) \\times v = F \\times v
\\]
3. The instantaneous rate of doing work (mechanical power) is defined as:
\\[
P = \\frac{dW}{dt} = \\vec{F} \\cdot \\frac{d\\vec{s}}{dt} = F \\cdot v
\\]
Thus:
\\[
m \\times a \\times v = \\text{Power}
\\]

### 2. Physical Context & Practical Illustration:
Checking dimensions:
\\[
[m \\cdot a \\cdot v] = [M^1] \\times [L^1 T^{-2}] \\times [L^1 T^{-1}] = [M^1 L^2 T^{-3}]
\\]
The dimension \([M^1 L^2 T^{-3}]\) is precisely the physical dimension of **Power** (\(\\text{Watts} = \\text{J/s}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Momentum)**: Incorrect. Momentum is \(m \\times v\), without acceleration.
- **Option B (Work)**: Incorrect. Work is \(F \\times s = m \\times a \\times s\), with displacement instead of velocity.
- **Option C (Mechanical Power)**: Correct. \(m \\cdot a \\cdot v = F \\cdot v = P\) (Power).
- **Option D (Potential Energy)**: Incorrect. Potential energy is \(m \\times g \\times h\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-115",
    text: "On the circular dial of a stopwatch, one complete rotation of the second hand corresponds to \\(60\\text{ seconds}\\). If this dial is divided into \\(60\\) equal division markings, what is the least count of the stopwatch?",
    options: [
      "\\(1\\text{ second}\\)",
      "\\(0.1\\text{ second}\\)",
      "\\(0.5\\text{ second}\\)",
      "\\(0.01\\text{ second}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **least count** of any dial instrument is the value of one smallest scale division:
\\[
\\text{Least Count} = \\frac{\\text{Total range of one complete rotation}}{\\text{Total number of scale divisions}}
\\]
Given:
- Total time interval for one rotation = \(60\\text{ seconds}\)
- Total number of divisions = \(60\\)

Calculating least count:
\\[
\\text{Least Count} = \\frac{60\\text{ s}}{60} = 1\\text{ second}
\\]

### 2. Physical Context & Practical Illustration:
An observer using this stopwatch can record time intervals with an accuracy of \(\\pm 1\\text{ s}\). To measure tenths of a second, an electronic digital stopwatch or a dial with 600 subdivisions would be required.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1 second)**: Correct. \(60\\text{ s} / 60\\text{ divisions} = 1\\text{ s}\).
- **Option B (0.1 second)**: Incorrect. Would require 600 divisions on the dial.
- **Option C (0.5 second)**: Incorrect. Would require 120 divisions.
- **Option D (0.01 second)**: Incorrect. Typical of modern digital stopwatches, not a 60-division dial.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-116",
    text: "What modification can be made to the design of a Vernier caliper to increase its measurement accuracy (i.e., make its least count smaller)?",
    options: [
      "Increase the number of divisions on the Vernier scale for the same total length",
      "Decrease the number of divisions on the Vernier scale",
      "Lengthen the main scale without altering graduations",
      "Increase the thickness of the jaws"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The least count (LC) of a Vernier caliper is given by:
\\[
\\text{LC} = 1\\text{ MSD} - 1\\text{ VSD} = \\frac{1\\text{ MSD}}{n}
\\]
where \(1\\text{ MSD}\) is the value of one main scale division, and \(n\) is the total number of divisions on the Vernier scale matching with \((n-1)\) main scale divisions.
From the formula:
\\[
\\text{LC} \\propto \\frac{1}{n}
\\]
To increase measurement accuracy (which means making the least count smaller and more precise), one must **increase the number of Vernier divisions \\(n\\)**. For example, increasing \(n\) from \(10\) to \(50\) reduces least count from \(0.1\\text{ mm}\) to \(0.02\\text{ mm}\).

### 2. Physical Context & Practical Illustration:
High-precision industrial calipers use 50-division Vernier plates, allowing machinists to measure engine cylinder tolerances down to \(0.02\\text{ mm}\) (\(20\\,\\mu\\text{m}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Increase number of divisions)**: Correct. More divisions \(n\) reduce least count (\(\\text{LC} = \\text{MSD}/n\)), improving accuracy.
- **Option B (Decrease divisions)**: Incorrect. Fewer divisions increase least count, worsening precision.
- **Option C (Lengthen main scale)**: Incorrect. Increases measuring range, not accuracy or least count.
- **Option D (Increase jaw thickness)**: Incorrect. Affects durability, not scale graduation precision.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-117",
    text: "What primary chain of energy transformations takes place inside the electromagnetic receiver (earphone / speaker) of a telephone?",
    options: [
      "Electrical energy \\(\\rightarrow\\) Magnetic force / Mechanical vibration \\(\\rightarrow\\) Acoustic sound energy",
      "Sound energy \\(\\rightarrow\\) Electrical energy \\(\\rightarrow\\) Mechanical energy",
      "Chemical energy \\(\\rightarrow\\) Thermal energy \\(\\rightarrow\\) Sound energy",
      "Mechanical energy \\(\\rightarrow\\) Electrical energy \\(\\rightarrow\\) Radiant light energy"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Inside a telephone earphone (audio receiver):
1. Incoming audio signals arrive as fluctuating **Electrical Current**.
2. This current flows through a wire coil wrapped around a permanent magnet, producing a rapidly fluctuating magnetic field.
3. The varying magnetic field exerts mechanical forces on a thin ferromagnetic diaphragm, causing it to vibrate (**Mechanical Kinetic Energy**).
4. The vibrating diaphragm compresses and expands the surrounding air, generating longitudinal acoustic pressure waves (**Sound Energy**).
\\[
\\text{Electrical Energy} \\longrightarrow \\text{Mechanical Vibration} \\longrightarrow \\text{Acoustic Sound Energy}
\\]

### 2. Physical Context & Practical Illustration:
This is the operating principle of all loudspeakers and headphones, converting electrical audio signals into sound waves audible to human ears.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Electrical \\(\\rightarrow\\) Mechanical \\(\\rightarrow\\) Sound)**: Correct. Standard sequence for an earphone/speaker.
- **Option B**: Incorrect. This describes a microphone (transmitter), which converts sound into electrical signals.
- **Option C**: Incorrect. No chemical reactions take place in an earphone.
- **Option D**: Incorrect. Earphones generate sound, not radiant light.`
  }
];
