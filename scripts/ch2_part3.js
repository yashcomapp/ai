// scripts/ch2_part3.js - Questions 61 to 90 of Chapter 2 (Work and Energy)
module.exports = [
  {
    id: "MH-9-SCIT-2-2.1-OSC-061",
    text: "When a sound wave propagates through an elastic medium, what is physically transported from one place to another?",
    options: [
      "The physical mass of the medium particles",
      "Energy and momentum",
      "Gravitational potential force",
      "Electric charge carriers"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A mechanical wave is an oscillatory disturbance traveling through a medium. The constituent particles of the medium oscillate back and forth about their mean equilibrium positions without any net bulk displacement of matter:
\\[
\\Delta x_{\\text{matter}} = 0
\\]
However, the kinetic and elastic potential energies of vibrating particles are continuously transferred to adjacent particles via intermolecular forces. Thus, waves transport **energy and momentum** across space.

### 2. Physical Context & Practical Illustration:
When a loudspeaker produces a sound, air molecules do not travel from the speaker cone all the way across the room into the listener's ear. Instead, alternating compressions and rarefactions pass through the air, delivering energy that vibrates the listener's eardrum.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Physical mass)**: Incorrect. Matter does not travel with the wave; particles only oscillate locally.
- **Option B (Energy and momentum)**: Correct. Waves transport energy and momentum without bulk transport of matter.
- **Option C (Gravitational force)**: Incorrect. Sound is an acoustic pressure disturbance, not gravitational.
- **Option D (Electric charge)**: Incorrect. Sound in air does not involve net electric current.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-062",
    text: "What happens to the elastic potential energy stored in a compressed mechanical spring when it is allowed to expand back to its natural unstrained equilibrium length?",
    options: [
      "It continuously increases",
      "It remains completely unchanged",
      "It is converted into other forms of energy and reduces to zero",
      "It doubles in magnitude"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The elastic potential energy stored in a spring compressed by displacement \(x\) is given by:
\\[
E_p = \\frac{1}{2} k x^2
\\]
where \(k\) is the spring stiffness constant.
When the spring rebounds and returns to its natural uncompressed length, the deformation displacement becomes:
\\[
x = 0 \\implies E_p = \\frac{1}{2} k (0)^2 = 0\\text{ J}
\\]
The stored elastic potential energy reduces to zero as it does work, converting into kinetic energy of the attached mass or projectile.

### 2. Physical Context & Practical Illustration:
In a pinball launcher or spring-powered dart gun, pulling back compresses the spring, storing potential energy. When released, the spring relaxes to \(x = 0\), releasing all its stored potential energy to shoot the ball forward at high velocity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Increases)**: Incorrect. Relaxing the spring releases energy, decreasing stored potential energy.
- **Option B (Remains unchanged)**: Incorrect. Potential energy depends directly on deformation \(x^2\).
- **Option C (Reduces to zero)**: Correct. At the natural equilibrium position (\(x = 0\)), stored elastic potential energy is zero.
- **Option D (Doubles)**: Incorrect. No deformation means no stored elastic energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-063",
    text: "Which of the following physical quantities is a scalar quantity?",
    options: [
      "Displacement",
      "Acceleration",
      "Energy",
      "Weight (gravitational force)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Physical quantities are classified into scalars and vectors:
- **Scalars**: Possess magnitude only and combine according to ordinary algebraic addition. Examples include **energy**, work, mass, temperature, and speed.
- **Vectors**: Possess both magnitude and a specific spatial direction, obeying vector addition rules. Examples include displacement (\(\\vec{s}\)), acceleration (\(\\vec{a}\)), velocity (\(\\vec{v}\)), and weight (\(\\vec{W} = m\\vec{g}\)).

### 2. Physical Context & Practical Illustration:
Saying an object has \(500\\text{ Joules}\) of kinetic energy completely specifies the physical state without needing a directional heading (north, south, up, down).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Displacement)**: Vector quantity (directed straight-line distance).
- **Option B (Acceleration)**: Vector quantity (rate of change of velocity).
- **Option C (Energy)**: Correct. Energy is an invariant scalar quantity.
- **Option D (Weight)**: Vector quantity (gravitational force directed downward towards Earth's center).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-064",
    text: "According to the kinetic theory of matter, what microscopic physical quantity determines the thermodynamic temperature of an object?",
    options: [
      "The total mass of the object",
      "The average speed of macroscopic center-of-mass motion",
      "The total internal potential energy only",
      "The average kinetic energy of the constituent molecules"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In kinetic theory, the absolute temperature \(T\) of a substance in Kelvins is directly proportional to the mean translational kinetic energy of its constituent particles:
\\[
\\langle E_k \\rangle = \\frac{1}{2} m \\langle v^2 \\rangle = \\frac{3}{2} k_B T
\\]
where \(k_B = 1.38 \\times 10^{-23}\\text{ J/K}\) is Boltzmann's constant.
Thus:
\\[
T \\propto \\langle E_k \\rangle
\\]
Temperature is a statistical measure of the **average kinetic energy** of random molecular vibrations and collisions.

### 2. Physical Context & Practical Illustration:
A tiny cup of boiling water at \(100^\\circ\\text{C}\) has a higher temperature than a vast iceberg at \(0^\\circ\\text{C}\), because the average kinetic energy of individual water molecules in the cup is greater, even though the massive iceberg contains vastly more total internal thermal energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Total mass)**: Incorrect. Mass determines extensive heat capacity, not intensive temperature.
- **Option B (Center-of-mass speed)**: Incorrect. Throwing a warm rock fast does not change its internal temperature.
- **Option C (Total potential energy)**: Incorrect. Intermolecular potential energy governs phase changes (latent heat), not temperature.
- **Option D (Average kinetic energy of molecules)**: Correct. Fundamental definition from the kinetic theory of gases and matter.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-065",
    text: "A constant horizontal force of \\(20\\text{ N}\\) acts on a cart, displacing it horizontally across a floor by a distance of \\(5\\text{ m}\\) in the direction of the force. How much mechanical work is performed on the cart?",
    options: [
      "\\(4\\text{ J}\\)",
      "\\(25\\text{ J}\\)",
      "\\(100\\text{ J}\\)",
      "\\(400\\text{ J}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done by a constant force acting along the line of displacement is:
\\[
W = F \\cdot s \\cdot \\cos\\theta
\\]
Given:
- Force \(F = 20\\text{ N}\)
- Displacement \(s = 5\\text{ m}\)
- Since force is in the direction of motion, \(\\theta = 0^\\circ \\implies \\cos 0^\\circ = 1\)

Calculation:
\\[
W = 20\\text{ N} \\times 5\\text{ m} \\times 1 = 100\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
This \(100\\text{ Joules}\) of mechanical work represents the energy transferred to the cart. If the surface is frictionless, the cart's kinetic energy increases by exactly \(100\\text{ J}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (4 J)**: Incorrect. Divides force by displacement (\(20 / 5 = 4\)).
- **Option B (25 J)**: Incorrect. Adds force and displacement.
- **Option C (100 J)**: Correct. Exact product \(20 \\times 5 = 100\\text{ J}\).
- **Option D (400 J)**: Incorrect. Multiplies \(F^2\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-066",
    text: "Convert a speed of \\(54\\text{ km/h}\\) into CGS units (\\(\\text{cm/s}\\)).",
    options: [
      "\\(1.5 \\times 10^3\\text{ cm/s}\\)",
      "\\(15\\text{ cm/s}\\)",
      "\\(150\\text{ cm/s}\\)",
      "\\(1.5 \\times 10^4\\text{ cm/s}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Step 1: Convert kilometers per hour to meters per second:
\\[
v = 54\\text{ km/h} = 54 \\times \\frac{5}{18}\\text{ m/s} = 3 \\times 5 = 15\\text{ m/s}
\\]
Step 2: Convert meters per second to centimeters per second (\(1\\text{ m} = 100\\text{ cm} = 10^2\\text{ cm}\)):
\\[
v = 15\\text{ m/s} = 15 \\times 100\\text{ cm/s} = 1500\\text{ cm/s} = 1.5 \\times 10^3\\text{ cm/s}
\\]

### 2. Physical Context & Practical Illustration:
\(54\\text{ km/h}\) is the typical legal speed limit for passenger cars on suburban roads. In scientific scientific notation, \(1500\\text{ cm/s}\) is written cleanly as \(1.5 \\times 10^3\\text{ cm/s}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(1.5 \\times 10^3\\text{ cm/s}\\))**: Correct. \(1500\\text{ cm/s} = 1.5 \\times 10^3\\text{ cm/s}\).
- **Option B (15 cm/s)**: Incorrect. Forgets to multiply the \(15\\text{ m/s}\) by 100.
- **Option C (150 cm/s)**: Incorrect. Multiplies by 10 instead of 100.
- **Option D (\\(1.5 \\times 10^4\\text{ cm/s}\\))**: Incorrect. Erroneous extra power of 10.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-067",
    text: "If we wish to double the kinetic energy of a moving object while maintaining constant mass, by what factor must its velocity be multiplied?",
    options: [
      "\\(2\\) times",
      "\\(\\frac{1}{2}\\) times",
      "\\(4\\) times",
      "\\(\\sqrt{2}\\) times"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Kinetic energy is given by:
\\[
E_k = \\frac{1}{2} m v^2 \\implies v = \\sqrt{\\frac{2E_k}{m}}
\\]
If the new kinetic energy is doubled (\(E_k' = 2E_k\)):
\\[
v' = \\sqrt{\\frac{2(2E_k)}{m}} = \\sqrt{2} \\times \\sqrt{\\frac{2E_k}{m}} = \\sqrt{2} \\, v
\\]
Thus, the velocity must be increased by a factor of \(\\sqrt{2} \\approx 1.414\) (an increase of approximately \(41.4\\%\)).

### 2. Physical Context & Practical Illustration:
Because kinetic energy grows with the square of velocity, you do not need to double the vehicle's speed to double its kinetic energy. Accelerating from \(50\\text{ km/h}\) to approximately \(70.7\\text{ km/h}\) (\(50 \\times \\sqrt{2}\)) doubles the car's kinetic energy and required braking work.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (2 times)**: Incorrect. Doubling velocity quadruples kinetic energy (\(2^2 = 4\)).
- **Option B (1/2 times)**: Incorrect. Halving velocity reduces kinetic energy to one-fourth.
- **Option C (4 times)**: Incorrect. Multiplying velocity by 4 increases kinetic energy by \(4^2 = 16\) times.
- **Option D (\\(\\sqrt{2}\\) times)**: Correct. \((\\sqrt{2})^2 = 2\), exactly doubling kinetic energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-068",
    text: "Two displacement vectors \\(\\vec{AB}\\) and \\(\\vec{BC}\\) are mutually perpendicular (\\(\\theta = 90^\\circ\\)) and have equal magnitude \\(a\\). What is the magnitude of the resultant displacement vector \\(\\vec{AC}\\)?",
    options: [
      "\\(a\\sqrt{2}\\)",
      "\\(2a\\)",
      "\\(a\\)",
      "\\(\\frac{a}{\\sqrt{2}}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By vector addition (triangle law):
\\[
\\vec{AC} = \\vec{AB} + \\vec{BC}
\\]
The magnitude of the resultant of two vectors inclined at angle \(\\theta\) is:
\\[
|\\vec{AC}| = \\sqrt{|\\vec{AB}|^2 + |\\vec{BC}|^2 + 2|\\vec{AB}||\\vec{BC}|\\cos\\theta}
\\]
Since \(\\vec{AB} \\perp \\vec{BC}\\), \(\\theta = 90^\\circ \\implies \\cos 90^\\circ = 0\). Given \(|\\vec{AB}| = |\\vec{BC}| = a\):
\\[
|\\vec{AC}| = \\sqrt{a^2 + a^2 + 0} = \\sqrt{2a^2} = a\\sqrt{2}
\\]

### 2. Physical Context & Practical Illustration:
This is equivalent to finding the length of the diagonal of a square of side \(a\) using the Pythagorean theorem (\(c^2 = a^2 + b^2\)). If a person walks \(10\\text{ m}\) East and then \(10\\text{ m}\) North, the net straight-line displacement is \(10\\sqrt{2} \\approx 14.14\\text{ m}\) North-East.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(a\\sqrt{2}\\))**: Correct. By Pythagoras' theorem, \(\\sqrt{a^2 + a^2} = a\\sqrt{2}\).
- **Option B (2a)**: Incorrect. Simple scalar addition (\(a + a = 2a\)), which is valid only if vectors are parallel (\(\\theta = 0^\\circ\)).
- **Option C (a)**: Incorrect. Valid only if \(\\theta = 120^\\circ\).
- **Option D (\\(a/\\sqrt{2}\\))**: Incorrect. Inverts the geometric ratio.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-069",
    text: "What is the least count of a standard classroom metric ruler calibrated in centimeters and millimeters?",
    options: [
      "\\(1\\text{ cm}\\)",
      "\\(1\\text{ m}\\)",
      "\\(0.1\\text{ cm}\\) (or \\(1\\text{ mm}\\))",
      "\\(0.01\\text{ cm}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **least count** of any measuring instrument is the smallest measurement that can be measured directly and accurately using that instrument.
On a standard metric laboratory ruler:
- Each major centimeter mark is subdivided into \(10\) equal parts.
- Value of one smallest division:
\\[
\\text{Least Count} = \\frac{1\\text{ cm}}{10} = 0.1\\text{ cm} = 1\\text{ mm}
\\]

### 2. Physical Context & Practical Illustration:
When measuring the length of a pencil with a standard plastic ruler, you can measure down to \(1\\text{ mm}\) directly (e.g. \(14.3\\text{ cm}\)), but any fractional division between marks is an estimate.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1 cm)**: Incorrect. This is the major division, not the smallest graduation.
- **Option B (1 m)**: Incorrect. Represents the total length of a meter stick.
- **Option C (0.1 cm)**: Correct. \(1\\text{ mm} = 0.1\\text{ cm}\) is the smallest physical division.
- **Option D (0.01 cm)**: Incorrect. \(0.01\\text{ cm} = 0.1\\text{ mm}\) is the least count of a standard Vernier caliper, not a ruler.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-070",
    text: "How much will the kinetic energy of a moving ball change if its velocity is doubled while its mass remains constant?",
    options: [
      "It will be doubled (increase 2 times)",
      "It will remain unchanged",
      "It will quadruple (increase to 4 times its original value)",
      "It will increase to 8 times"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The formula for kinetic energy is:
\\[
E_k = \\frac{1}{2} m v^2
\\]
When velocity is doubled, \(v' = 2v\):
\\[
E_k' = \\frac{1}{2} m (2v)^2 = \\frac{1}{2} m (4v^2) = 4 \\left(\\frac{1}{2} m v^2\\right) = 4 E_k
\\]
Hence, the kinetic energy quadruples (increases by a factor of 4).

### 2. Physical Context & Practical Illustration:
This rapid non-linear increase is why highway speed limits are strictly enforced. A car traveling at \(80\\text{ km/h}\) has \(4\) times the kinetic energy of a car at \(40\\text{ km/h}\), requiring \(4\) times the braking distance under identical tire traction forces.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Doubled)**: Incorrect. Linear scaling applies to momentum (\(p = mv\)), not kinetic energy (\(E_k \\propto v^2\)).
- **Option B (Remains unchanged)**: Incorrect. Kinetic energy depends dynamically on velocity.
- **Option C (Quadruple / 4 times)**: Correct. Since \(E_k \\propto v^2\), \((2)^2 = 4\).
- **Option D (8 times)**: Incorrect. Cubed scaling applies to wind power (\(v^3\)), not kinetic energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-071",
    text: "Which of the following values is equal to \\(1\\text{ square meter}\\) (\\(1\\text{ m}^2\\))?",
    options: [
      "\\(100\\text{ mm}^2\\)",
      "\\(1000\\text{ mm}^2\\)",
      "\\(10^4\\text{ mm}^2\\)",
      "\\(10^6\\text{ mm}^2\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Recall the basic linear conversion between meters and millimeters:
\\[
1\\text{ m} = 1000\\text{ mm} = 10^3\\text{ mm}
\\]
Squaring both sides to find area:
\\[
1\\text{ m}^2 = (10^3\\text{ mm})^2 = 10^{3 \\times 2}\\text{ mm}^2 = 10^6\\text{ mm}^2 = 1,000,000\\text{ mm}^2
\\]

### 2. Physical Context & Practical Illustration:
In surface area calculations (e.g. pressure \(P = \\frac{F}{A}\)), unit conversions must account for the square of the conversion factor:
- \(1\\text{ m}^2 = 10^4\\text{ cm}^2 = 10^6\\text{ mm}^2\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(100\\text{ mm}^2\\))**: Incorrect. This is \((10\\text{ mm})^2 = 1\\text{ cm}^2\).
- **Option B (\\(1000\\text{ mm}^2\\))**: Incorrect. Confuses linear millimeters (\(1000\\text{ mm} = 1\\text{ m}\)) with area.
- **Option C (\\(10^4\\text{ mm}^2\\))**: Incorrect. \(1\\text{ m}^2 = 10^4\\text{ cm}^2\), not \(\\text{mm}^2\).
- **Option D (\\(10^6\\text{ mm}^2\\))**: Correct. Exact mathematical conversion: \((10^3)^2 = 10^6\\text{ mm}^2\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-072",
    text: "The kilowatt-hour (\\(\\text{kWh}\\)) is the commercial unit of which physical quantity?",
    options: [
      "Electric power",
      "Electric force",
      "Electrical energy",
      "Electric current"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Power is defined as energy per unit time (\(P = \\frac{E}{t}\)).
Therefore:
\\[
\\text{Energy} = \\text{Power} \\times \\text{time}
\\]
In commercial electricity billing:
- Power is measured in kilowatts (\(1\\text{ kW} = 1000\\text{ W}\)).
- Time is measured in hours (\(1\\text{ h} = 3600\\text{ s}\)).

Multiplying them gives energy:
\\[
1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6\\text{ W}\\cdot\\text{s} = 3.6 \\times 10^6\\text{ Joules (J)}
\\]
Hence, the kilowatt-hour is a commercial unit of **electrical energy**.

### 2. Physical Context & Practical Illustration:
When an electricity utility meter reads that a household consumed "1 unit" of electricity, it corresponds precisely to \(1\\text{ kWh}\) (\(3.6\\text{ MJ}\)) of energy, which can power a \(100\\text{ W}\) incandescent bulb continuously for 10 hours.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Electric power)**: Incorrect. Power is measured in Watts (\(\\text{W}\)) or Kilowatts (\(\\text{kW}\)), without the time factor.
- **Option B (Electric force)**: Incorrect. Force is measured in Newtons (\(\\text{N}\)).
- **Option C (Electrical energy)**: Correct. Power \(\\times\) time = Energy.
- **Option D (Electric current)**: Incorrect. Current is measured in Amperes (\(\\text{A}\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-073",
    text: "A stationary body placed at an elevation \\(h\\) above the ground possesses which form of mechanical energy?",
    options: [
      "Kinetic energy",
      "Gravitational potential energy",
      "Solar radiant energy",
      "Nuclear binding energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy \(E_p\) is the energy possessed by an object due to its position in a gravitational field:
\\[
E_p = mgh
\\]
Since the body is stationary (\(v = 0\\text{ m/s}\)), its kinetic energy is zero:
\\[
E_k = \\frac{1}{2}mv^2 = 0
\\]
All of its mechanical energy exists purely as **gravitational potential energy**.

### 2. Physical Context & Practical Illustration:
A brick resting on top of a 5-story building possesses substantial potential energy. If it is knocked off, that potential energy converts into kinetic energy as it accelerates downward under gravity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Kinetic energy)**: Incorrect. Velocity is zero, so \(E_k = 0\).
- **Option B (Gravitational potential energy)**: Correct. Elevated position gives it \(E_p = mgh\).
- **Option C (Solar energy)**: Incorrect. Elevation is mechanical, not radiant.
- **Option D (Nuclear energy)**: Incorrect. Raising an object does not alter nuclear forces.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-074",
    text: "In an electrochemical cell (battery) while discharging to power a circuit, what primary energy transformation takes place?",
    options: [
      "Electrical energy to mechanical energy",
      "Electrical energy to chemical energy",
      "Chemical energy to mechanical energy",
      "Chemical energy to electrical energy"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electrochemical cell contains an anode, a cathode, and an electrolyte solution. During discharge:
1. Spontaneous redox (reduction-oxidation) chemical reactions occur at the electrodes.
2. The Gibbs free energy (\(\\Delta G < 0\)) released by these chemical bond transformations drives the migration of electrons through the external circuit:
\\[
\\text{Chemical Energy} \\longrightarrow \\text{Electrical Energy}
\\]

### 2. Physical Context & Practical Illustration:
In flashlights, smartphones, and remote controls, chemical reactions inside dry cells or lithium-ion batteries generate continuous electric current to power electronic components.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Electrical to mechanical)**: Incorrect. This occurs in electric motors.
- **Option B (Electrical to chemical)**: Incorrect. This occurs during battery *recharging* or electrolysis.
- **Option C (Chemical to mechanical)**: Incorrect. This occurs in internal combustion engines or human muscles.
- **Option D (Chemical to electrical)**: Correct. Discharging cells convert stored chemical energy into electric current.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-075",
    text: "A ball of mass \\(m\\) is thrown vertically upwards with an initial velocity so that it reaches a maximum height \\(h\\). Which of the following statements is correct regarding its energy state?",
    options: [
      "Potential energy of the ball at the launch point on the ground is \\(mgh\\)",
      "Kinetic energy imparted to the ball at the ground is zero",
      "Kinetic energy of the ball at the highest point is \\(mgh\\)",
      "Potential energy of the ball at the highest point is \\(mgh\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the mechanical energy at both extremes (neglecting air resistance):
1. **At the ground (\\(y = 0\\))**:
   - Potential energy: \(E_p = mg(0) = 0\).
   - Kinetic energy: \(E_k = \\frac{1}{2}mu^2 = mgh\) (where \(u = \\sqrt{2gh}\)).
2. **At the highest point (\\(y = h\\))**:
   - The ball momentarily comes to a complete stop: \(v = 0 \\implies E_k = 0\).
   - Potential energy: \(E_p = mgh\).
By conservation of mechanical energy:
\\[
E = E_p + E_k = mgh + 0 = mgh
\\]
Thus, the potential energy of the ball at its highest point is **\\(mgh\\)**.

### 2. Physical Context & Practical Illustration:
All the kinetic energy provided by the thrower's hand at ground level is gradually converted into gravitational potential energy as the ball rises against gravity, peaking at \(mgh\) at the top of the arc.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. At the ground datum (\(h = 0\)), \(E_p = 0\).
- **Option B**: Incorrect. The ball must have maximum kinetic energy (\(E_k = mgh\)) to reach height \(h\).
- **Option C**: Incorrect. At the highest point, velocity is zero, so \(E_k = 0\).
- **Option D**: Correct. At the peak, all mechanical energy resides as potential energy \(E_p = mgh\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-076",
    text: "A simple pendulum oscillates to and fro about its central equilibrium position. Which of the following statements is strictly correct regarding its mechanical energy (neglecting friction)?",
    options: [
      "It possesses only kinetic energy throughout its entire motion",
      "It possesses maximum kinetic energy at its extreme angular positions",
      "It possesses maximum potential energy at its central rest position",
      "The sum of its kinetic and potential energies remains constant throughout the oscillation"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In an ideal simple pendulum governed solely by conservative gravity:
\\[
E_{\\text{total}} = E_k + E_p = \\text{constant}
\\]
- **At extreme positions**: The pendulum bob momentarily stops (\(v = 0 \\implies E_k = 0\)) at maximum elevation \(h_{\\text{max}}\), so potential energy is maximum (\(E_p = mgh_{\\text{max}}\)).
- **At mean (rest) position**: Height is minimum (\(h = 0 \\implies E_p = 0\)), and velocity is maximum (\(v_{\\text{max}} = \\sqrt{2gh_{\\text{max}}}\)), so kinetic energy is maximum.
- **At intermediate points**: Energy is divided between \(E_k\) and \(E_p\), with their sum remaining strictly constant.

### 2. Physical Context & Practical Illustration:
The continuous cyclic exchange between potential energy at the extremes and kinetic energy at the bottom center illustrates the Law of Conservation of Mechanical Energy in periodic motion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. It has potential energy whenever it is elevated above the mean position.
- **Option B**: Incorrect. Velocity is zero at extreme turning points, so \(E_k = 0\).
- **Option C**: Incorrect. Elevation is zero at the mean rest position, so \(E_p = 0\) (minimum, not maximum).
- **Option D**: Correct. Total mechanical energy (\(E_k + E_p\)) is conserved throughout.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-077",
    text: "Calculate the kinetic energy of a body of mass \\(0.1\\text{ kg}\\) having a linear momentum of \\(20\\text{ kg}\\cdot\\text{m/s}\\).",
    options: [
      "\\(2500\\text{ J}\\)",
      "\\(2000\\text{ J}\\)",
      "\\(200\\text{ J}\\)",
      "\\(400\\text{ J}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Recall the fundamental relationship between kinetic energy \(E_k\) and linear momentum \(p = mv\):
\\[
E_k = \\frac{1}{2} m v^2 = \\frac{m^2 v^2}{2m} = \\frac{p^2}{2m}
\\]
Given:
- Mass \(m = 0.1\\text{ kg}\)
- Momentum \(p = 20\\text{ kg}\\cdot\\text{m/s}\)

Substitute the values:
\\[
E_k = \\frac{(20)^2}{2 \\times 0.1} = \\frac{400}{0.2} = \\frac{4000}{2} = 2000\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
A light projectile (\(100\\text{ g}\)) carrying a substantial momentum of \(20\\text{ kg}\\cdot\\text{m/s}\) must be traveling at a very high velocity:
\\[
v = \\frac{p}{m} = \\frac{20}{0.1} = 200\\text{ m/s}
\\]
Consequently, its kinetic energy is large: \(E_k = \\frac{1}{2}(0.1)(200)^2 = 2000\\text{ Joules}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (2500 J)**: Incorrect. Arithmetic miscalculation.
- **Option B (2000 J)**: Correct. Exact computation: \(\\frac{400}{0.2} = 2000\\text{ J}\).
- **Option C (200 J)**: Incorrect. Omits squaring the momentum (\(p / 2m = 20 / 0.2 = 100\)) or decimal error.
- **Option D (400 J)**: Incorrect. Forgets to divide by \(2m\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-078",
    text: "One Angstrom unit (\\(1\\text{ \\AA}\\)) is equal to how many nanometers (\\(\\text{nm}\\))?",
    options: [
      "\\(0.1\\text{ nm}\\)",
      "\\(10\\text{ nm}\\)",
      "\\(1\\text{ nm}\\)",
      "\\(0.01\\text{ nm}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition:
- \(1\\text{ \\AA} = 10^{-10}\\text{ m}\)
- \(1\\text{ nm} = 10^{-9}\\text{ m}\)

Expressing Angstrom in terms of nanometers:
\\[
1\\text{ \\AA} = 10^{-10}\\text{ m} = 10^{-1} \\times 10^{-9}\\text{ m} = 0.1\\text{ nm}
\\]
Conversely, \(1\\text{ nm} = 10\\text{ \\AA}\).

### 2. Physical Context & Practical Illustration:
The Angstrom is widely used in atomic physics and crystallography because atomic radii (such as the Bohr radius of hydrogen, \(a_0 \\approx 0.53\\text{ \\AA}\)) and chemical bond lengths are typically on the order of \(1\\) to \(2\\text{ \\AA}\) (\(0.1\\) to \(0.2\\text{ nm}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (0.1 nm)**: Correct. \(10^{-10}\\text{ m} = 0.1 \\times 10^{-9}\\text{ m} = 0.1\\text{ nm}\).
- **Option B (10 nm)**: Incorrect. Inverts the ratio (\(1\\text{ nm} = 10\\text{ \\AA}\)).
- **Option C (1 nm)**: Incorrect. Equal to \(10\\text{ \\AA}\).
- **Option D (0.01 nm)**: Incorrect. Equal to \(1\\text{ pm} \\times 10\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-079",
    text: "Which of the following units is an authentic unit of time?",
    options: [
      "Light-year",
      "Parsec",
      "Leap year",
      "Angstrom"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us examine the physical dimensions of each listed unit:
- **Light-year**: The distance that light travels in vacuum in one Julian year (\(\\approx 9.46 \\times 10^{15}\\text{ m}\)). Unit of **distance/length**.
- **Parsec**: Parallax of one arcsecond (\(\\approx 3.08 \\times 10^{16}\\text{ m} \\approx 3.26\\text{ light-years}\)). Unit of astronomical **distance/length**.
- **Leap year**: A calendar year containing \(366\\text{ days}\) (\(31,622,400\\text{ seconds}\)) to adjust for Earth's orbital period. Unit of **time**.
- **Angstrom**: \(10^{-10}\\text{ m}\). Unit of **atomic length**.

### 2. Physical Context & Practical Illustration:
Students often mistakenly assume that because "light-year" contains the word "year", it measures time. In reality, light-year measures astronomical distance, whereas a leap year measures time.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Light-year)**: Incorrect. Unit of distance, not time.
- **Option B (Parsec)**: Incorrect. Unit of astronomical distance.
- **Option C (Leap year)**: Correct. Measures a time interval of 366 days.
- **Option D (Angstrom)**: Incorrect. Unit of atomic length.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-080",
    text: "What is the least count of a standard one-meter wooden or plastic measuring rule?",
    options: [
      "\\(1\\text{ cm}\\)",
      "\\(1\\text{ m}\\)",
      "\\(0.1\\text{ cm}\\) (or \\(1\\text{ mm}\\))",
      "\\(0.01\\text{ cm}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A standard meter rule has a total length of \(1\\text{ meter} = 100\\text{ cm}\).
- Each centimeter is divided into \(10\) millimeter subdivisions.
- The minimum distance between two consecutive graduation marks is:
\\[
\\text{Least Count} = 1\\text{ mm} = 0.1\\text{ cm} = 10^{-3}\\text{ m}
\\]

### 2. Physical Context & Practical Illustration:
Any measurement taken with a standard meter rule must be reported with an instrumental uncertainty of \(\\pm 0.1\\text{ cm}\) (\(\\pm 1\\text{ mm}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1 cm)**: Incorrect. This is the main numbered graduation.
- **Option B (1 m)**: Incorrect. This is the total scale span.
- **Option C (0.1 cm)**: Correct. \(1\\text{ mm} = 0.1\\text{ cm}\) is the smallest graduated division.
- **Option D (0.01 cm)**: Incorrect. This requires a Vernier caliper.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-081",
    text: "A Torricellian mercury barometer column stands at \\(76\\text{ cm}\\) of Hg under normal atmospheric pressure. What happens to the mercury column if a small pinhole is pierced at the closed glass top above the column?",
    options: [
      "The mercury level will fall completely into the trough until levels equalize (reading \\(0\\text{ cm}\\))",
      "The reading will remain unchanged at \\(76\\text{ cm}\\)",
      "The mercury level will rise and shoot out of the top",
      "The reading will drop to exactly half (\\(38\\text{ cm}\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In an intact barometer, the space above the mercury column is a **Torricellian vacuum** (\(P_{\\text{top}} \\approx 0\)). The atmospheric pressure \(P_0\) acting on the open trough supports the weight of the mercury column:
\\[
P_0 = P_{\\text{top}} + h\\rho g = 0 + h\\rho g \\implies h = \\frac{P_0}{\\rho g} = 76\\text{ cm}
\\]
If a hole is made at the top:
1. Air rushes into the vacuum, establishing atmospheric pressure \(P_0\) on top of the liquid column inside the tube.
2. Net pressure difference:
\\[
\\Delta P = P_0 - P_0 = 0 \\implies h\\rho g = 0 \\implies h = 0\\text{ cm}
\\]
The mercury column falls completely until its level matches the mercury level in the trough.

### 2. Physical Context & Practical Illustration:
The vacuum at the top is crucial; without it, the downward air pressure balances the upward atmospheric support pressure, rendering the barometer unable to sustain any elevated liquid column.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Falls completely to trough level / 0 cm)**: Correct. Equal atmospheric pressure acts at both ends, destroying the hydrostatic column.
- **Option B (Remains unchanged)**: Incorrect. Ignores incoming air pressure.
- **Option C (Shoots out of the top)**: Incorrect. Air pressure pushes downward into the tube, not upward.
- **Option D (Drops to half)**: Incorrect. No physical mechanism balances a half column.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-082",
    text: "An iron sphere of mass \\(30\\text{ kg}\\) and an aluminum sphere of mass \\(10.5\\text{ kg}\\), both having identical external diameter, are simultaneously dropped from rest from the top of a tall tower. Neglecting air resistance, what physical property will they have strictly identical when they are \\(10\\text{ m}\\) above the ground?",
    options: [
      "Acceleration and downward velocity",
      "Linear momentum",
      "Kinetic energy",
      "Gravitational potential energy"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's second law and universal gravitation:
\\[
F = \\frac{GMm}{R^2} = ma \\implies a = g = \\frac{GM}{R^2}
\\]
The gravitational acceleration \(g = 9.8\\text{ m/s}^2\) is independent of the falling object's mass \(m\).
Since both spheres fall from the same initial height \(H\) starting from rest (\(u = 0\)), at any height \(y = 10\\text{ m}\), the distance fallen is \(\\Delta h = H - 10\\text{ m}\).
Their downward speed is:
\\[
v = \\sqrt{2g\\Delta h}
\\]
Because \(g\) and \(\\Delta h\) are identical, their **acceleration** and **speed/velocity** are strictly identical.

### 2. Physical Context & Practical Illustration:
Mass-dependent quantities differ significantly:
- Momentum: \(p = mv \\implies p_{\\text{iron}} > p_{\\text{aluminum}}\)
- Kinetic energy: \(E_k = \\frac{1}{2}mv^2 \\implies E_{k,\\text{iron}} > E_{k,\\text{aluminum}}\)
- Potential energy: \(E_p = mgy \\implies E_{p,\\text{iron}} > E_{p,\\text{aluminum}}\)
Only kinematic quantities (acceleration and velocity) are identical.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Acceleration and velocity)**: Correct. Galileo's principle of equivalence: all masses fall with identical acceleration \(g\) and speed in free fall.
- **Option B (Linear momentum)**: Incorrect. \(p = mv\); the heavier iron sphere has nearly 3 times more momentum.
- **Option C (Kinetic energy)**: Incorrect. \(E_k = \\frac{1}{2}mv^2\); scales with mass.
- **Option D (Potential energy)**: Incorrect. \(E_p = mgy\); scales with mass.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-083",
    text: "A pair of household scissors used for cutting paper belongs to which class of lever?",
    options: [
      "Class I lever",
      "Class II lever",
      "Class III lever",
      "Class IV lever"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a pair of scissors:
- The central pivot pin acts as the **Fulcrum (F)**.
- The user's fingers apply **Effort (E)** on the handles.
- The blades exert force to cut the paper, which represents the **Load (L)**.
Since the fulcrum is situated in between the effort and the load (\(E - F - L\)), scissors are a canonical **Class I lever**.

### 2. Physical Context & Practical Illustration:
In metal-cutting shears, the effort handles are very long while the blades are very short, resulting in a large mechanical advantage (\(MA = \\frac{d_E}{d_L} > 1\)). In tailor scissors, the blades are long to cut long strips of fabric rapidly in one stroke.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Class I lever)**: Correct. The pivot screw (fulcrum) sits in between the load blades and effort loops.
- **Option B (Class II lever)**: Incorrect. In Class II levers, load sits between fulcrum and effort.
- **Option C (Class III lever)**: Incorrect. In Class III levers, effort sits in the middle.
- **Option D (Class IV lever)**: Incorrect. There is no fourth class of levers.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-084",
    text: "A simple pendulum suspended from a rigid ceiling swings to and fro without friction. Which of the following statements is true regarding its total mechanical energy during the swing?",
    options: [
      "Potential energy is maximum at the lowest midpoint of the swing",
      "Kinetic energy is minimum at the lowest midpoint of the swing",
      "The sum of Kinetic Energy and Potential Energy remains constant throughout the swing",
      "The sum of Kinetic Energy and Potential Energy is zero throughout the swing"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By the Law of Conservation of Mechanical Energy:
\\[
E_{\\text{total}} = E_k + E_p = \\frac{1}{2}mv^2 + mgh = \\text{constant}
\\]
- At extreme points (\(h = h_{\\text{max}}\)): Bob stops momentarily (\(v = 0\)), so \(E_k = 0\) and \(E_p = mgh_{\\text{max}}\).
- At equilibrium center (\(h = 0\)): \(E_p = 0\) and \(v = v_{\\text{max}}\), so \(E_k = \\frac{1}{2}mv_{\\text{max}}^2 = mgh_{\\text{max}}\).
The sum of kinetic and potential energies remains invariant at every point of the trajectory.

### 2. Physical Context & Practical Illustration:
As the pendulum swings back and forth, energy constantly sloshes between potential and kinetic forms without any loss in an ideal frictionless environment.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. Potential energy is *minimum* at the lowest midpoint (\(h = 0\)).
- **Option B**: Incorrect. Kinetic energy is *maximum* at the lowest midpoint (\(v = v_{\\text{max}}\)).
- **Option C**: Correct. Total mechanical energy (\(E_k + E_p\)) is conserved and constant.
- **Option D**: Incorrect. The total energy is positive (\(mgh_{\\text{max}}\)), not zero.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-085",
    text: "Why do mechanical work and energy share the exact same physical unit (the Joule)?",
    options: [
      "Because energy is the capacity to do work, and work done measures the energy transferred",
      "Because both work and energy are fundamental vector quantities",
      "Because work can only be performed when power is zero",
      "Because energy equals force divided by displacement"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work and energy are dimensionally equivalent physical quantities:
\\[
[\\text{Work}] = [\\text{Force} \\times \\text{Displacement}] = [M^1 L^1 T^{-2}] \\times [L^1] = [M^1 L^2 T^{-2}]
\\]
\\[
[\\text{Energy}] = [\\text{Kinetic Energy}] = [\\text{Mass} \\times \\text{Velocity}^2] = [M^1] \\times [L^1 T^{-1}]^2 = [M^1 L^2 T^{-2}]
\\]
According to the **Work-Energy Theorem**:
\\[
W = \\Delta E
\\]
Work is energy in transit. Doing work on a body increases its energy by an amount equal to the work done. Hence, they share the exact same SI unit: the **Joule (\\(\\text{J}\\))**.

### 2. Physical Context & Practical Illustration:
If an athlete expends \(500\\text{ Joules}\) of chemical energy from metabolic processes to lift a barbell, exactly \(500\\text{ Joules}\) of work is performed on the barbell, storing \(500\\text{ Joules}\) of gravitational potential energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Energy is capacity to do work)**: Correct. Work measures energy transfer; both have dimensions \([M^1 L^2 T^{-2}]\) and unit Joule.
- **Option B (Vector quantities)**: Incorrect. Both work and energy are scalars, not vectors.
- **Option C (Power is zero)**: Incorrect. Power is the rate of doing work (\(P = W/t\)).
- **Option D (Force divided by displacement)**: Incorrect. Work is force *multiplied* by displacement.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-086",
    text: "Which of the following statements correctly describes the primary energy transformation in an electric dynamo (generator)?",
    options: [
      "Electrical energy is converted into light energy",
      "Electrical energy is converted into mechanical kinetic energy",
      "Thermal energy is converted into chemical energy",
      "Mechanical energy is converted into electrical energy"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
An electric dynamo operates on Michael Faraday's law of **electromagnetic induction**:
\\[
\\mathcal{E} = -\\frac{d\\Phi_B}{dt}
\\]
When an external mechanical torque rotates a coil of wire inside a magnetic field, the magnetic flux \(\\Phi_B\) passing through the coil changes with time, inducing an electromotive force (voltage) that drives an electric current:
\\[
\\text{Mechanical Energy (Rotation)} \\longrightarrow \\text{Electrical Energy}
\\]

### 2. Physical Context & Practical Illustration:
Bicycle dynamos rubbing against tires power headlights when cycling, and giant turbine dynamos in power plants generate megawatts of electricity for national grids.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. Dynamos produce electricity, not light directly.
- **Option B**: Incorrect. This describes an electric **motor**, which is the reverse of a dynamo.
- **Option C**: Incorrect. Dynamos do not involve chemical transformations.
- **Option D (Mechanical to electrical)**: Correct. Mechanical rotation is converted into electrical current.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-087",
    text: "What is the mechanical work done by the gravitational force on an object of mass \\(m\\) when it is pushed horizontally across a frictionless horizontal table over a distance \\(s\\)?",
    options: [
      "\\(0\\text{ J}\\)",
      "\\(mgs\\)",
      "\\(-mgs\\)",
      "\\(\\frac{1}{2}mv^2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done by gravity is:
\\[
W_g = \\vec{F}_g \\cdot \\vec{s} = F_g \\cdot s \\cdot \\cos\\theta
\\]
The force of gravity \(\\vec{F}_g = mg\\hat{j}\) acts vertically downwards towards the center of Earth.
The displacement \(\\vec{s} = s\\hat{i}\) is purely horizontal.
The angle between gravity and horizontal displacement is:
\\[
\\theta = 90^\\circ \\implies \\cos 90^\\circ = 0
\\]
\\[
W_g = mg \\times s \\times 0 = 0\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Because the object does not change its vertical elevation (\(\\Delta h = 0\)), its gravitational potential energy remains strictly constant (\(\\Delta E_p = 0\)). Gravity performs zero work on horizontally moving objects.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (0 J)**: Correct. Force and displacement are perpendicular (\(\\cos 90^\\circ = 0\\)).
- **Option B (mgs)**: Incorrect. Valid only if the object were falling vertically downwards.
- **Option C (-mgs)**: Incorrect. Valid only if the object were lifted vertically upwards.
- **Option D (\\(1/2 mv^2\\))**: Incorrect. This is the horizontal kinetic energy imparted by the external pushing force, not gravitational work.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-088",
    text: "Which of the following is categorized as a conventional (traditional fossil) source of energy?",
    options: [
      "Biogas from agricultural waste",
      "Solar photovoltaic radiation",
      "Coal and petroleum",
      "Geothermal steam energy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Energy sources are classified into two broad historical/technological categories:
- **Conventional Sources**: Energy sources that have been traditionally utilized by human civilization on a massive commercial scale for generations, primarily fossil fuels (coal, petroleum, natural gas). They are finite, non-renewable, and major carbon emitters.
- **Non-Conventional (Renewable) Sources**: Alternative modern sources harnessed more recently, such as solar, wind, tidal, geothermal, and biogas.

### 2. Physical Context & Practical Illustration:
Coal thermal power plants still supply a large baseline percentage of electricity in India and worldwide, representing the quintessential conventional energy source.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Biogas)**: Non-conventional renewable source.
- **Option B (Solar radiation)**: Non-conventional renewable source.
- **Option C (Coal and petroleum)**: Correct. Canonical conventional fossil energy sources.
- **Option D (Geothermal)**: Non-conventional renewable source.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-089",
    text: "Two bodies, a light body of mass \\(m_1\\) and a heavy body of mass \\(m_2\\) (\\(m_1 < m_2\\)), possess identical kinetic energy (\\(E_{k1} = E_{k2}\\)). Which body has a greater magnitude of linear momentum?",
    options: [
      "The heavy body",
      "The light body",
      "Both have strictly equal linear momentum",
      "Cannot be determined without knowing their velocities"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The relationship between linear momentum \(p\) and kinetic energy \(E_k\) is:
\\[
E_k = \\frac{p^2}{2m} \\implies p = \\sqrt{2m E_k}
\\]
Given that both bodies have the exact same kinetic energy \(E_k\):
\\[
p \\propto \\sqrt{m}
\\]
Taking the ratio of their momenta:
\\[
\\frac{p_2}{p_1} = \\sqrt{\\frac{m_2}{m_1}}
\\]
Since \(m_2 > m_1\):
\\[
\\frac{p_2}{p_1} > 1 \\implies p_2 > p_1
\\]
Therefore, the **heavier body possesses greater linear momentum**.

### 2. Physical Context & Practical Illustration:
Consider a loaded truck (\(5000\\text{ kg}\)) and a light scooter (\(100\\text{ kg}\)) possessing the same kinetic energy of \(50,000\\text{ J}\):
- Scooter velocity: \(v_1 = \\sqrt{\\frac{2 \\times 50000}{100}} = \\sqrt{1000} \\approx 31.6\\text{ m/s} \\implies p_1 = 100 \\times 31.6 = 3162\\text{ kg}\\cdot\\text{m/s}\).
- Truck velocity: \(v_2 = \\sqrt{\\frac{2 \\times 50000}{5000}} = \\sqrt{20} \\approx 4.47\\text{ m/s} \\implies p_2 = 5000 \\times 4.47 = 22,360\\text{ kg}\\cdot\\text{m/s}\).
The truck carries over 7 times more momentum despite moving much slower!

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (The heavy body)**: Correct. For constant \(E_k\), \(p \\propto \\sqrt{m}\), so the heavier mass has greater momentum.
- **Option B (The light body)**: Incorrect. The light body has higher velocity, but less momentum.
- **Option C (Both equal)**: Incorrect. Equal \(E_k\) does not mean equal momentum when masses differ.
- **Option D (Cannot be determined)**: Incorrect. Completely determined by \(p = \\sqrt{2mE_k}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-090",
    text: "Which of the following statements is scientifically correct regarding the work done by kinetic friction when an object slides across a rough horizontal floor?",
    options: [
      "Kinetic friction always does negative work on the sliding object because it opposes the relative displacement",
      "Kinetic friction always does positive work on the sliding object",
      "Kinetic friction cannot do work because it is a non-conservative force",
      "Kinetic friction always does zero work because normal reaction is perpendicular"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an object slides horizontally with velocity \(\\vec{v}\), the force of kinetic friction \(\\vec{f}_k\) acts along the contact interface in the direction directly opposite to the relative motion:
\\[
\\vec{f}_k = -\\mu_k N \\hat{v}
\\]
The angle between frictional force and displacement is \(\\theta = 180^\\circ\).
Work done by friction over displacement \(s\):
\\[
W_f = f_k \\cdot s \\cdot \\cos 180^\\circ = -f_k s < 0
\\]
The work done by kinetic friction on the sliding body is **negative**, converting mechanical kinetic energy into dissipative thermal energy (heat).

### 2. Physical Context & Practical Illustration:
When a book slides across a desk and comes to rest, friction removes all its kinetic energy (\(W_{\\text{net}} = \\Delta E_k < 0\)). Feeling the contact surface immediately afterwards reveals slight warming due to dissipated frictional heat.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Negative work)**: Correct. \(\\cos 180^\\circ = -1\), so friction removes mechanical energy.
- **Option B (Positive work)**: Incorrect. Kinetic friction opposes sliding, it does not accelerate the sliding object forward.
- **Option C (Cannot do work)**: Incorrect. Non-conservative forces do work; their work simply depends on the path.
- **Option D (Zero work)**: Incorrect. Friction is parallel to displacement, not perpendicular.`
  }
];
