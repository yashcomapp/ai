// scripts/ch2_part1.js - Questions 1 to 30 of Chapter 2 (Work and Energy)
module.exports = [
  {
    id: "MH-9-SCIT-2-2.1-OSC-001",
    text: "A lemon squeezer belongs to which class of lever?",
    options: [
      "Class I lever",
      "Class II lever",
      "Class III lever",
      "Compound lever"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In simple machines, levers are classified into three orders based on the relative positions of the **Fulcrum (F)**, **Load (L)**, and **Effort (E)**:
- **Class I**: Fulcrum lies between Effort and Load (\(E - F - L\)).
- **Class II**: Load lies between Fulcrum and Effort (\(F - L - E\)).
- **Class III**: Effort lies between Fulcrum and Load (\(F - E - L\)).

In a lemon squeezer, the hinge acts as the fulcrum at one end, the lemon being squeezed represents the load in the middle, and the user's hand applies effort at the free ends. Hence, it is a **Class II (second-order) lever**.

### 2. Physical Context & Practical Illustration:
A Class II lever always has a mechanical advantage greater than 1 (\(MA = \\frac{\\text{Effort Arm}}{\\text{Load Arm}} > 1\)) because the effort arm is always longer than the load arm. This enables a person to crush a tough lemon rind using a modest manual grip force. Other common examples include a wheelbarrow, paper cutter, and nutcracker.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Class I lever)**: Incorrect. In Class I levers (like scissors or a crowbar), the fulcrum is located between the effort and the load.
- **Option B (Class II lever)**: Correct. The load (lemon) is positioned between the fulcrum (pivot hinge) and the effort (handles).
- **Option C (Class III lever)**: Incorrect. In Class III levers (such as tongs or a fishing rod), the effort is applied between the fulcrum and the load (\(MA < 1\)).
- **Option D (Compound lever)**: Incorrect. A lemon squeezer is a single simple lever mechanism, not a combination of multiple interconnected lever arms.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-002",
    text: "Work done on a body by a force is categorized as which type of physical quantity?",
    options: [
      "A vector quantity having both magnitude and direction",
      "A scalar quantity having magnitude only",
      "A tensor quantity depending on the frame of reference",
      "A dimensionless quantity"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Mechanically, work done \(W\) is defined as the scalar (dot) product of the force vector \(\\vec{F}\) and the displacement vector \(\\vec{s}\):
\\[
W = \\vec{F} \\cdot \\vec{s} = F s \\cos\\theta
\\]
where \(F\) is the magnitude of force, \(s\) is the magnitude of displacement, and \(\\theta\) is the angle between \(\\vec{F}\) and \(\\vec{s}\). The dot product of two vector quantities always yields a **scalar quantity**.

### 2. Physical Context & Practical Illustration:
Although work can take positive, negative, or zero values, the algebraic sign indicates whether energy was transferred into the system (\(W > 0\)) or extracted from the system (\(W < 0\), such as by friction), NOT a spatial direction in three-dimensional space. Work obeys the rules of ordinary scalar arithmetic.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (A vector quantity)**: Incorrect. While force and displacement are both vectors, their dot product is an invariant scalar quantity.
- **Option B (A scalar quantity)**: Correct. Work has magnitude and algebraic sign, but no spatial direction.
- **Option C (A tensor quantity)**: Incorrect. Work does not require higher-order tensor rank descriptions; it is a rank-0 tensor (scalar).
- **Option D (A dimensionless quantity)**: Incorrect. Work has dimensions of energy, namely \([M^1 L^2 T^{-2}]\), and SI units of Joules (\(\\text{J}\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-003",
    text: "If the speed of a motor car becomes \(6\) times its initial value, how many times will its kinetic energy become?",
    options: [
      "\\(6\\) times",
      "\\(36\\) times",
      "\\(12\\) times",
      "\\(24\\) times"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The kinetic energy \(E_k\) of an object of mass \(m\) moving with velocity \(v\) is given by:
\\[
E_k = \\frac{1}{2} m v^2
\\]
If the speed becomes \(v' = 6v\), the new kinetic energy \(E_k'\) is:
\\[
E_k' = \\frac{1}{2} m (6v)^2 = \\frac{1}{2} m (36 v^2) = 36 \\left(\\frac{1}{2} m v^2\\right) = 36 E_k
\\]
Thus, the kinetic energy increases by a factor of \(6^2 = 36\).

### 2. Physical Context & Practical Illustration:
This quadratic dependence of kinetic energy on speed is the primary reason why high-speed traffic collisions cause exponentially catastrophic damage. A car traveling at \(120\\text{ km/h}\) possesses \(4\) times the destructive kinetic energy of the same car at \(60\\text{ km/h}\), requiring drastically longer braking distances.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (6 times)**: Incorrect. This assumes linear proportionality (\(E_k \\propto v\)), which applies to momentum (\(p = mv\)), not kinetic energy.
- **Option B (36 times)**: Correct. Kinetic energy scales quadratically with speed (\(E_k \\propto v^2\)), so \((6)^2 = 36\).
- **Option C (12 times)**: Incorrect. Confuses squaring \(6^2\) with multiplying by 2 (\(6 \\times 2 = 12\)).
- **Option D (24 times)**: Incorrect. Arises from an erroneous algebraic calculation.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-004",
    text: "At what angle \\(\\theta\\) between the applied force and the displacement is the work done on an object equal to zero?",
    options: [
      "\\(0^\\circ\\)",
      "\\(90^\\circ\\)",
      "\\(180^\\circ\\)",
      "\\(45^\\circ\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The work done by a constant force \(F\) causing a displacement \(s\) is given by:
\\[
W = F s \\cos\\theta
\\]
For the work done to be zero (\(W = 0\)) when both force and displacement are non-zero:
\\[
\\cos\\theta = 0 \\implies \\theta = 90^\\circ
\\]
Therefore, zero work is performed whenever the applied force is perpendicular to the direction of displacement.

### 2. Physical Context & Practical Illustration:
1. **Coolie carrying luggage**: A porter carrying a load on his head while walking along a horizontal platform does zero work against gravity, because the gravitational force acts vertically downwards while displacement is horizontal (\(\\theta = 90^\\circ\\)).
2. **Satellite in circular orbit**: The gravitational pull of Earth acts towards the center (centripetal force), perpendicular to the instantaneous tangential velocity of the satellite, resulting in zero work done over any orbital arc.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(0^\\circ\\))**: Incorrect. When \(\\theta = 0^\\circ\), \(\\cos 0^\\circ = 1\), giving maximum positive work (\(W = +Fs\)).
- **Option B (\\(90^\\circ\\))**: Correct. When \(\\theta = 90^\\circ\), \(\\cos 90^\\circ = 0\), so \(W = 0\\text{ J}\).
- **Option C (\\(180^\\circ\\))**: Incorrect. When \(\\theta = 180^\\circ\), \(\\cos 180^\\circ = -1\), yielding negative work (\(W = -Fs\), like friction).
- **Option D (\\(45^\\circ\\))**: Incorrect. When \(\\theta = 45^\\circ\), \(\\cos 45^\\circ = \\frac{1}{\\sqrt{2}} \\approx 0.707\), producing positive work.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-005",
    text: "When a constant force \\(F\\) acts along the direction of displacement \\(s\\), the mechanical work done \\(W\\) is given by which formula?",
    options: [
      "\\(W = \\frac{F}{s}\\)",
      "\\(W = F \\times s\\)",
      "\\(W = F + s\\)",
      "\\(W = F - s\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition, mechanical work is the product of the magnitude of the force and the displacement in the direction of the force:
\\[
W = F \\cdot s \\cdot \\cos\\theta
\\]
When the force and displacement act in the exact same direction, the angle between them is \(\\theta = 0^\\circ\). Since \(\\cos 0^\\circ = 1\):
\\[
W = F \\times s
\\]

### 2. Physical Context & Practical Illustration:
When a child pushes a toy car across the floor with a horizontal force of \(5\\text{ N}\) through a distance of \(3\\text{ m}\) in the same direction, the work done on the car is:
\\[
W = 5\\text{ N} \\times 3\\text{ m} = 15\\text{ N}\\cdot\\text{m} = 15\\text{ J}
\\]
This energy is transferred into the kinetic energy of the car.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(W = F/s\\))**: Incorrect. Dividing force by displacement does not yield work; its unit would be \(\\text{N/m}\) (stiffness constant).
- **Option B (\\(W = F \\times s\\))**: Correct. Work is the product of force and displacement along the line of action.
- **Option C (\\(W = F + s\\))**: Incorrect. Force (\(\\text{N}\)) and displacement (\(\\text{m}\)) have completely different physical dimensions and cannot be added.
- **Option D (\\(W = F - s\\))**: Incorrect. Incompatible dimensional quantities cannot be subtracted.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-006",
    text: "A stationary body at rest can possess which of the following physical quantities?",
    options: [
      "Speed",
      "Potential energy",
      "Linear momentum",
      "Velocity"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For a body at rest, its velocity \(v = 0\\text{ m/s}\).
Consequently:
- Speed: \(|v| = 0\)
- Momentum: \(p = m v = m(0) = 0\)
- Kinetic energy: \(E_k = \\frac{1}{2}mv^2 = 0\)

However, **potential energy** \(E_p = mgh\) (gravitational) or \(E_p = \\frac{1}{2}kx^2\) (elastic) depends strictly on the body's **position, configuration, or state of strain**, and is completely independent of velocity. Hence, a resting body can store substantial potential energy.

### 2. Physical Context & Practical Illustration:
Water stored behind a high hydroelectric dam is completely stationary, yet it possesses immense gravitational potential energy due to its elevated height above the turbines. When released, this stored potential energy rapidly converts into kinetic energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Speed)**: Incorrect. By definition, a body at rest has zero speed.
- **Option B (Potential energy)**: Correct. Potential energy is energy possessed due to position or shape, requiring no motion.
- **Option C (Linear momentum)**: Incorrect. Momentum is the product of mass and velocity (\(p = mv\)); if \(v = 0\), momentum is strictly zero.
- **Option D (Velocity)**: Incorrect. A body at rest has zero velocity.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-007",
    text: "A photoelectric cell (photocell) directly converts which form of energy into electrical energy?",
    options: [
      "Chemical energy",
      "Light (radiant) energy",
      "Heat (thermal) energy",
      "Mechanical energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A photocell operates on the principle of the **photoelectric effect** or the **photovoltaic effect**. When photons of light with energy \(E = h\\nu\) (where \(h\) is Planck's constant and \(\\nu\) is frequency) strike a photosensitive material, electrons are ejected or charge carriers are mobilized across a p-n junction, creating an electric current. Thus:
\\[
\\text{Light (Radiant) Energy} \\longrightarrow \\text{Electrical Energy}
\\]

### 2. Physical Context & Practical Illustration:
Photocells and solar panels installed on rooftops, satellites, and solar calculators convert incoming sunlight directly into usable electric current to charge batteries and power electrical circuits without any moving mechanical parts.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Chemical energy)**: Incorrect. Chemical cells and batteries convert chemical energy to electrical energy, not photocells.
- **Option B (Light energy)**: Correct. Photocells harness radiant light photons directly to generate electrical potential and current.
- **Option C (Heat energy)**: Incorrect. Thermocouples or thermoelectric generators convert thermal gradients into electricity.
- **Option D (Mechanical energy)**: Incorrect. Dynamos and electric generators convert mechanical energy into electrical energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-008",
    text: "Two spherical balls of identical radius but different masses are simultaneously dropped from the top of a \\(20\\text{ m}\\) high tower. When they reach \\(16\\text{ m}\\) above the ground, both balls possess the same:",
    options: [
      "Kinetic energy",
      "Potential energy",
      "Linear momentum",
      "Speed and acceleration"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When dropped from rest (\(u = 0\)) under gravity in the absence of air resistance, the acceleration of both bodies is identical and independent of mass:
\\[
a = g = 9.8\\text{ m/s}^2
\\]
After falling through a vertical distance \\(\\Delta h = 20\\text{ m} - 16\\text{ m} = 4\\text{ m}\\), the speed \(v\) of each ball is given by the third kinematic equation:
\\[
v = \\sqrt{2g\\Delta h} = \\sqrt{2 \\times 9.8 \\times 4} = \\sqrt{78.4}\\text{ m/s}
\\]
Since both balls experience the same acceleration \(g\) and fall through the same height, their **speed** and **acceleration** are strictly identical.

### 2. Physical Context & Practical Illustration:
As demonstrated by Galileo's legendary Leaning Tower of Pisa thought experiment, gravity accelerates all objects at the exact same rate regardless of their mass. In a vacuum, a heavy cannonball and a light ball dropped from the same height reach the exact same speed at every point along their fall.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Kinetic energy)**: Incorrect. Kinetic energy is \(E_k = \\frac{1}{2} m v^2\); since the masses \(m_1 \\neq m_2\), their kinetic energies are different.
- **Option B (Potential energy)**: Incorrect. Potential energy is \(E_p = mgh\); different masses produce different potential energies at the same height.
- **Option C (Linear momentum)**: Incorrect. Momentum is \(p = mv\); the heavier ball possesses greater momentum.
- **Option D (Speed and acceleration)**: Correct. Both acceleration (\(g\)) and instantaneous speed (\(v = \\sqrt{2g\\Delta h}\)) are independent of mass.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-009",
    text: "When the applied force and the displacement of a body are inclined at an angle of \\(90^\\circ\\), the work done is:",
    options: [
      "Maximum positive",
      "Maximum negative",
      "Zero",
      "Equal to unity (\\(1\\text{ J}\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The work done by a force \(F\) resulting in displacement \(s\) is:
\\[
W = F s \\cos\\theta
\\]
For \(\\theta = 90^\\circ\):
\\[
\\cos 90^\\circ = 0 \\implies W = F \\times s \\times 0 = 0\\text{ J}
\\]
Because no component of force acts along the direction of displacement, no work is performed on the body by that force.

### 2. Physical Context & Practical Illustration:
A person walking horizontally while holding a bucket of water applies an upward vertical force equal to the bucket's weight. Because this upward force is perpendicular (\(90^\\circ\)) to the horizontal walking displacement, the work done by the lifting force on the bucket is zero.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Maximum positive)**: Incorrect. Maximum work occurs at \(\\theta = 0^\\circ\) where \(\\cos 0^\\circ = 1\).
- **Option B (Maximum negative)**: Incorrect. Maximum negative work occurs at \(\\theta = 180^\\circ\) where \(\\cos 180^\\circ = -1\).
- **Option C (Zero)**: Correct. \(\\cos 90^\\circ = 0\), making the work done strictly zero.
- **Option D (Equal to unity)**: Incorrect. Work is zero, not \(1\\text{ J}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-010",
    text: "When a stone tied to a string is whirled in a horizontal circle at constant speed, the work done on the stone by the tension force is:",
    options: [
      "Positive and maximum",
      "Negative and equal to kinetic energy",
      "Infinite",
      "Zero"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In uniform circular motion, the tension in the string provides the **centripetal force** directed radially inwards towards the center of the circle:
\\[
F_c = \\frac{m v^2}{r}
\\]
At any instantaneous moment, the stone's displacement vector \(\\vec{s}\) is tangential to the circular path. Since radius is always perpendicular to tangent:
\\[
\\theta = 90^\\circ \\implies W = F_c s \\cos 90^\\circ = 0\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Because the centripetal force does zero work on the revolving stone, the kinetic energy of the stone remains constant throughout uniform circular motion. The force only continuously alters the direction of velocity, not its magnitude (speed).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Positive and maximum)**: Incorrect. Centripetal force acts perpendicularly to tangential velocity, never parallel.
- **Option B (Negative)**: Incorrect. Tension does not oppose the tangential displacement; it is strictly perpendicular.
- **Option C (Infinite)**: Incorrect. Work done is zero, not infinite.
- **Option D (Zero)**: Correct. The force acts at \(90^\\circ\) to the instantaneous displacement, so \(\\cos 90^\\circ = 0\\implies W = 0\\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-011",
    text: "A spherical boulder rolling down a hill possesses which form of mechanical energy?",
    options: [
      "Kinetic energy only",
      "Potential energy only",
      "Neither kinetic nor potential energy",
      "Both kinetic energy and potential energy"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Total mechanical energy \(E\) of a body is the sum of its kinetic energy and potential energy:
\\[
E = E_k + E_p = \\frac{1}{2} m v^2 + mgh
\\]
As the boulder rolls down the hill:
1. It is in motion with linear velocity \(v > 0\) (and rotational angular velocity \(\\omega\)), so it possesses **kinetic energy** (\(E_k > 0\)).
2. It is still at an elevated height \(h > 0\) above the bottom of the hill, so it possesses **gravitational potential energy** (\(E_p > 0\)).
Therefore, at any intermediate point during its descent, it possesses **both kinetic and potential energy**.

### 2. Physical Context & Practical Illustration:
According to the law of conservation of energy, as the boulder rolls downward, its potential energy gradually transforms into translational and rotational kinetic energy. At the top of the hill, energy is purely potential; halfway down, it is a mixture of both; and at the bottom datum, it is purely kinetic.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Kinetic energy only)**: Incorrect. This is true only when the boulder reaches the very bottom base of the hill where \(h = 0\).
- **Option B (Potential energy only)**: Incorrect. This describes the boulder when stationary at the peak before release (\(v = 0\)).
- **Option C (Neither)**: Incorrect. A moving mass at a height possesses substantial mechanical energy.
- **Option D (Both kinetic and potential energy)**: Correct. The rolling boulder has velocity (\(E_k\)) and elevation (\(E_p\)) simultaneously.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-012",
    text: "A stretched elastic spring possesses which type of energy?",
    options: [
      "Kinetic energy",
      "Elastic potential energy",
      "Electrical energy",
      "Magnetic energy"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an external force stretches or compresses an ideal spring by a displacement \(x\) from its natural equilibrium length, work is performed against the internal restoring force \(F = -kx\). This mechanical work is stored in the deformed configuration of the spring as **elastic potential energy**:
\\[
E_p = \\frac{1}{2} k x^2
\\]
where \(k\) is the spring constant (stiffness) in \(\\text{N/m}\).

### 2. Physical Context & Practical Illustration:
In mechanical clockwork toys, wind-up watches, and car suspension shock absorbers, energy is temporarily stored by compressing or stretching steel springs and then released progressively to perform useful mechanical work.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Kinetic energy)**: Incorrect. The held stretched spring is stationary (\(v = 0\)), so kinetic energy is zero.
- **Option B (Elastic potential energy)**: Correct. Energy is stored in the altered molecular lattice configuration of the stretched spring.
- **Option C (Electrical energy)**: Incorrect. No electric charges or electrical potentials are generated.
- **Option D (Magnetic energy)**: Incorrect. Elastic deformation involves mechanical restoring forces, not magnetism.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-013",
    text: "In the International System of Units (SI), what is the unit of potential energy?",
    options: [
      "Erg",
      "Dyne-centimeter",
      "Joule (\\(\\text{J}\\))",
      "Watt (\\(\\text{W}\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is defined as:
\\[
E_p = m \\cdot g \\cdot h
\\]
Expressing the SI base units for each quantity:
\\[
[E_p] = \\text{kg} \\times \\left(\\frac{\\text{m}}{\\text{s}^2}\\right) \\times \\text{m} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2} = \\text{N}\\cdot\\text{m} = \\text{Joule (J)}
\\]
All forms of energy (kinetic, potential, thermal, electrical) and work share the exact same SI unit: the **Joule**.

### 2. Physical Context & Practical Illustration:
One Joule is the work done (or potential energy gained) when a force of \(1\\text{ Newton}\) raises an object vertically by \(1\\text{ meter}\). For example, lifting an average apple (\(\\approx 100\\text{ g}\)) upward by \(1\\text{ m}\) imparts approximately \(1\\text{ Joule}\) of gravitational potential energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Erg)**: Incorrect. The erg is the CGS unit of energy (\(1\\text{ J} = 10^7\\text{ erg}\)), not SI.
- **Option B (Dyne-centimeter)**: Incorrect. This is the base CGS equivalent unit of work/energy (\(1\\text{ dyne}\\cdot\\text{cm} = 1\\text{ erg}\)).
- **Option C (Joule)**: Correct. The Joule (\(\\text{J}\)) is the official standard SI unit for all forms of energy and work.
- **Option D (Watt)**: Incorrect. The Watt (\(\\text{W} = \\text{J/s}\)) is the SI unit of **power** (rate of doing work), not energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-014",
    text: "What is the SI unit of power?",
    options: [
      "Watt per second (\\(\\text{W/s}\\))",
      "Joule (\\(\\text{J}\\))",
      "Kilojoule (\\(\\text{kJ}\\))",
      "Watt (\\(\\text{W}\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Power \(P\) is defined as the time rate of doing work or transferring energy:
\\[
P = \\frac{W}{t} = \\frac{\\text{Energy}}{\\text{time}}
\\]
In SI units, work is measured in Joules (\(\\text{J}\)) and time in seconds (\(\\text{s}\)). Therefore:
\\[
[P] = \\frac{\\text{Joule}}{\\text{second}} = \\text{J}\\cdot\\text{s}^{-1} = \\text{Watt (W)}
\\]
Named in honor of Scottish engineer James Watt, \(1\\text{ Watt} = 1\\text{ J/s}\).

### 2. Physical Context & Practical Illustration:
A typical \(10\\text{ W}\) LED bulb consumes \(10\\text{ Joules}\) of electrical energy every second, while a high-power electric kettle rated at \(2000\\text{ W}\) (\(2\\text{ kW}\)) transfers \(2000\\text{ Joules}\) of energy per second to boil water rapidly.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Watt per second)**: Incorrect. Dividing power by time has no standard physical meaning in basic mechanics.
- **Option B (Joule)**: Incorrect. Joule is the unit of work and energy, not power.
- **Option C (Kilojoule)**: Incorrect. Kilojoule (\(10^3\\text{ J}\)) is a multiple unit of energy.
- **Option D (Watt)**: Correct. The Watt (\(\\text{W}\)) is the official SI unit of power.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-015",
    text: "A crowbar used to pry up heavy rocks is an example of which class of lever?",
    options: [
      "Class I lever",
      "Class II lever",
      "Class III lever",
      "Rotary wheel lever"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a crowbar:
1. The fulcrum (pivot block or ground fulcrum) is placed near the stone.
2. The heavy rock represents the **load** at the short end.
3. The human applies **effort** downwards at the long opposite handle.
Since the fulcrum lies **between** the effort and the load (\(E - F - L\)), the crowbar operates as a **Class I lever**.

### 2. Physical Context & Practical Illustration:
Because the effort arm is much longer than the load arm (\(d_E \\gg d_L\)), the mechanical advantage is substantially greater than 1:
\\[
MA = \\frac{d_E}{d_L} > 1
\\]
This mechanical multiplier enables a worker exerting a force of only \(200\\text{ N}\) to lift a boulder weighing \(2000\\text{ N}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Class I lever)**: Correct. The pivot/fulcrum lies directly between the applied effort and the load.
- **Option B (Class II lever)**: Incorrect. In Class II levers (e.g. nutcracker), the load is between the fulcrum and effort.
- **Option C (Class III lever)**: Incorrect. In Class III levers (e.g. tweezers), effort is applied in the middle.
- **Option D (Rotary wheel lever)**: Incorrect. A crowbar is a straight rigid bar, not a wheel-and-axle.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-016",
    text: "Which of the following simple tools represents a Class III lever?",
    options: [
      "A bottle opener",
      "A wheelbarrow",
      "A pair of scissors",
      "A fishing rod (or pair of tweezers)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a **Class III lever**, the effort is applied **between** the fulcrum and the load (\(F - E - L\)):
- Load arm is longer than the effort arm (\(d_L > d_E\)).
- Mechanical advantage is always less than 1:
\\[
MA = \\frac{d_E}{d_L} < 1
\\]
In a fishing rod, one hand anchors the base of the rod acting as the **fulcrum**, the second hand applies the **effort** on the grip in the middle, and the hook holding the fish at the tip is the **load**.

### 2. Physical Context & Practical Illustration:
Although Class III levers provide an \(MA < 1\) (requiring more input force than the load weight), they provide a high **speed advantage** and displacement magnification. A small movement of the angler's hand produces a wide, rapid sweep at the tip of the rod to reel in fish swiftly.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Bottle opener)**: Incorrect. A bottle opener is a Class II lever (load is between fulcrum and effort).
- **Option B (Wheelbarrow)**: Incorrect. A wheelbarrow is a Class II lever (wheel is fulcrum, load in bucket, effort at handles).
- **Option C (Pair of scissors)**: Incorrect. Scissors are a Class I lever (fulcrum at the center pivot pin).
- **Option D (Fishing rod)**: Correct. The effort is applied between the anchored fulcrum and the line/load.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-017",
    text: "What is the primary practical advantage of using a single fixed pulley to draw water from a well?",
    options: [
      "It reduces the magnitude of force required to half",
      "It changes the direction of the applied force to a more convenient downward direction",
      "It multiplies the total mechanical work performed",
      "It increases the velocity ratio beyond 2"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For an ideal single fixed pulley (neglecting friction and rope mass):
\\[
\\text{Mechanical Advantage (MA)} = \\frac{\\text{Load}}{\\text{Effort}} = 1
\\]
Because \(MA = 1\), a single fixed pulley does **not** reduce the magnitude of effort required to lift the load. However, it changes the direction of the applied force from pulling upwards to pulling downwards.

### 2. Physical Context & Practical Illustration:
Pulling downwards is ergonomically far more advantageous for human workers because they can utilize their own body weight to assist the pulling effort against gravity, rather than straining back muscles by hauling a heavy bucket directly upwards.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Reduces force to half)**: Incorrect. A single *movable* pulley halves the required force (\(MA = 2\)), but a single *fixed* pulley has \(MA = 1\).
- **Option B (Changes direction)**: Correct. Its sole mechanical advantage is redirecting upward lifting effort into convenient downward pulling.
- **Option C (Multiplies work)**: Incorrect. No machine can create energy or multiply work (Law of Conservation of Energy).
- **Option D (Increases velocity ratio)**: Incorrect. For a single fixed pulley, the velocity ratio \(VR = 1\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-018",
    text: "A traditional beam balance used for weighing masses operates as which class of lever?",
    options: [
      "Class I lever",
      "Class II lever",
      "Class III lever",
      "Class IV lever"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A beam balance consists of a rigid horizontal beam supported at its central midpoint on a knife-edge pivot. 
- The central pivot serves as the **Fulcrum (F)**.
- The standard weights placed in one pan represent the **Effort (E)**.
- The object being weighed in the other pan represents the **Load (L)**.
Since the fulcrum is situated centrally between the load and effort (\(L - F - E\)), it is a classic **Class I lever**.

### 2. Physical Context & Practical Illustration:
Because the two arm lengths are designed to be strictly equal (\(d_L = d_E\)), the principle of moments dictates:
\\[
\\text{Load} \\times d_L = \\text{Effort} \\times d_E \\implies \\text{Load} = \\text{Effort}
\\]
When the beam is balanced horizontally, the unknown mass exactly equals the standard reference mass.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Class I lever)**: Correct. The pivot/fulcrum is positioned in the center between the two scale pans.
- **Option B (Class II lever)**: Incorrect. In Class II levers, the load is in the center.
- **Option C (Class III lever)**: Incorrect. In Class III levers, effort is applied in the center.
- **Option D (Class IV lever)**: Incorrect. Classical mechanics recognizes only three classes of levers.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-019",
    text: "Which of the following household implements is an example of a Class II lever?",
    options: [
      "A spoon used to pry open a tight tin lid",
      "A nutcracker",
      "A long-handled broom",
      "A pair of pliers"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a **Class II lever**, the **Load (L)** is located between the **Fulcrum (F)** and the **Effort (E)**:
\\[
\\text{Fulcrum} \\longleftrightarrow \\text{Load} \\longleftrightarrow \\text{Effort}
\\]
In a nutcracker:
1. The pivot hinge at the front end is the **fulcrum**.
2. The hard nut positioned in the central cavity is the **load**.
3. The user squeezes the handles at the outer ends applying the **effort**.

### 2. Physical Context & Practical Illustration:
Because the effort arm extends from the fulcrum all the way to the end of the handles (\(d_E > d_L\)), the mechanical advantage is always greater than 1:
\\[
MA = \\frac{d_E}{d_L} > 1
\\]
This allows a human hand to generate the high crushing forces needed to crack open hard nutshells with minimal effort.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Spoon prying open a lid)**: Incorrect. The rim of the tin acts as a central fulcrum between the hand and the lid, functioning as a Class I lever.
- **Option B (Nutcracker)**: Correct. The load (nut) sits between the pivot hinge (fulcrum) and the handles (effort).
- **Option C (Broom)**: Incorrect. A sweeping broom is a Class III lever (the lower hand provides effort in the middle).
- **Option D (Pair of pliers)**: Incorrect. Pliers are double Class I levers with a central pivot pin.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-020",
    text: "Which of the following statements accurately describes the physical construction of a pulley?",
    options: [
      "A rigid bar free to rotate about a fixed pivot point",
      "An inclined plane wrapped helically around a central cylinder",
      "A wedge consisting of two inclined planes placed back to back",
      "A wheel with a grooved rim mounted on an axle, carrying a rope or cable"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **pulley** is one of the six classical simple machines. It consists of a disc or circular wheel mounted on an axle that rotates within a frame (block). The outer rim of the wheel features a circumferential groove designed to guide and prevent slipping of a rope, cable, or belt running over it.

### 2. Physical Context & Practical Illustration:
Pulleys are widely used in construction cranes, elevator hoisting systems, flagpoles, and sailing rigging to lift heavy loads or transmit rotational power smoothly between axes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Rigid bar about a fixed pivot)**: Incorrect. This is the definition of a **lever**.
- **Option B (Inclined plane wrapped helically)**: Incorrect. This defines a **screw**.
- **Option C (Two inclined planes back to back)**: Incorrect. This defines a **wedge**.
- **Option D (Wheel with a grooved rim)**: Correct. This is the exact definition of a **pulley**.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-021",
    text: "When a book accidentally slips and falls freely from a high shelf to the floor, what energy transformation takes place during the descent?",
    options: [
      "Gravitational potential energy transforms into kinetic energy",
      "Kinetic energy transforms into gravitational potential energy",
      "Chemical potential energy transforms into thermal energy",
      "Thermal energy transforms into mechanical kinetic energy"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
At the top shelf at height \(h\), the stationary book possesses maximum gravitational potential energy and zero kinetic energy:
\\[
E = E_p + E_k = mgh + 0 = mgh
\\]
As it falls under the conservative force of gravity, its height \(h\) decreases while its speed \(v = \\sqrt{2g(h - y)}\) increases. By the law of conservation of mechanical energy:
\\[
-\\Delta E_p = +\\Delta E_k
\\]
The loss in gravitational potential energy is converted directly into an equivalent gain in **kinetic energy**.

### 2. Physical Context & Practical Illustration:
Just before impacting the floor, the potential energy reaches zero (relative to floor level) and all initial mechanical energy exists as kinetic energy. Upon impact with the floor, this kinetic energy transforms into sound waves (thud sound) and thermal energy (heating the book and floor slightly).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Potential to kinetic)**: Correct. Gravitational potential energy continuously converts into kinetic energy as the book accelerates downward.
- **Option B (Kinetic to potential)**: Incorrect. This happens when an object is thrown *upward*, not when falling downward.
- **Option C (Chemical to thermal)**: Incorrect. Falling involves gravitational mechanical energy, not chemical reactions.
- **Option D (Thermal to kinetic)**: Incorrect. Thermal energy is not driving the falling motion.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-022",
    text: "Which two primary physical parameters determine the amount of gravitational potential energy possessed by an object near Earth's surface?",
    options: [
      "Its mass and horizontal speed",
      "Its mass and vertical height above the reference level",
      "Its volume and surface area",
      "Its velocity and atmospheric pressure"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The gravitational potential energy \(E_p\) of an object of mass \(m\) elevated to a vertical height \(h\) in a uniform gravitational field of acceleration \(g\) is given by:
\\[
E_p = m \\cdot g \\cdot h
\\]
Since \(g \\approx 9.8\\text{ m/s}^2\) is constant near the Earth's surface:
\\[
E_p \\propto m \\quad \\text{and} \\quad E_p \\propto h
\\]
Thus, the magnitude of gravitational potential energy depends directly on the **mass of the object** and its **vertical height** above the chosen reference ground datum.

### 2. Physical Context & Practical Illustration:
A \(10\\text{ kg}\) boulder placed on a \(2\\text{ m}\) table stores twice the gravitational potential energy of a \(5\\text{ kg}\) boulder on the same table (\(E_p \\propto m\)). Similarly, raising the same \(10\\text{ kg}\) boulder to \(4\\text{ m}\) doubles its stored potential energy (\(E_p \\propto h\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Mass and horizontal speed)**: Incorrect. Horizontal speed determines kinetic energy (\(E_k = \\frac{1}{2}mv^2\)), not potential energy.
- **Option B (Mass and vertical height)**: Correct. \(E_p = mgh\) depends directly on mass \(m\) and elevation \(h\).
- **Option C (Volume and surface area)**: Incorrect. Geometry and surface area do not govern gravitational potential energy.
- **Option D (Velocity and pressure)**: Incorrect. Velocity relates to kinetic energy and pressure to fluid mechanics.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-023",
    text: "Calculate the kinetic energy of a ball of mass \\(200\\text{ g}\\) rolling horizontally with a speed of \\(50\\text{ m/s}\\).",
    options: [
      "\\(200\\text{ J}\\)",
      "\\(250\\text{ J}\\)",
      "\\(500\\text{ J}\\)",
      "\\(50\\text{ J}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
First, convert the given mass into standard SI units:
\\[
m = 200\\text{ g} = \\frac{200}{1000}\\text{ kg} = 0.2\\text{ kg}
\\]
Given velocity \(v = 50\\text{ m/s}\).
Using the formula for kinetic energy:
\\[
E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} \\times 0.2\\text{ kg} \\times (50\\text{ m/s})^2
\\]
\\[
E_k = 0.1 \\times 2500 = 250\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
A \(200\\text{ g}\) ball moving at \(50\\text{ m/s}\) (\(180\\text{ km/h}\), comparable to a fast cricket delivery) carries \(250\\text{ Joules}\) of kinetic energy. To bring this ball to a complete stop, an opposing catching glove must perform \(250\\text{ Joules}\) of negative work.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (200 J)**: Incorrect. Forgets to square the velocity or miscalculates \(0.5 \\times 0.2 \\times 50 = 5\).
- **Option B (250 J)**: Correct. Standard SI evaluation yields \(E_k = \\frac{1}{2}(0.2)(50^2) = 250\\text{ J}\).
- **Option C (500 J)**: Incorrect. Omits the factor of \(\\frac{1}{2}\) (\(m v^2 = 0.2 \\times 2500 = 500\\text{ J}\)).
- **Option D (50 J)**: Incorrect. Arises from failing to convert grams to kilograms correctly.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-024",
    text: "An object of mass \\(4\\text{ kg}\\) is raised to a vertical height of \\(20\\text{ m}\\) above the ground. Taking \\(g = 9.8\\text{ m/s}^2\\), what is the gravitational potential energy stored in the object?",
    options: [
      "\\(776\\text{ J}\\)",
      "\\(780\\text{ J}\\)",
      "\\(784\\text{ J}\\)",
      "\\(790\\text{ J}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is calculated using:
\\[
E_p = m \\cdot g \\cdot h
\\]
Given data:
- Mass \(m = 4\\text{ kg}\)
- Height \(h = 20\\text{ m}\)
- Acceleration due to gravity \(g = 9.8\\text{ m/s}^2\)

Substituting the values:
\\[
E_p = 4\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 20\\text{ m}
\\]
\\[
E_p = 80 \\times 9.8 = 784\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
The \(784\\text{ Joules}\) of potential energy stored in this elevated \(4\\text{ kg}\) mass represents the exact external mechanical work done against gravity in lifting it. If dropped, it will release precisely \(784\\text{ Joules}\) of kinetic energy immediately before reaching the ground.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (776 J)**: Incorrect. Arithmetic subtraction error.
- **Option B (780 J)**: Incorrect. Approximation error.
- **Option C (784 J)**: Correct. Exact computation gives \(4 \\times 9.8 \\times 20 = 784\\text{ J}\).
- **Option D (790 J)**: Incorrect. Overshoot caused by rounding errors.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-025",
    text: "Which of the following statements is INCORRECT regarding nuclear energy?",
    options: [
      "It is a non-conventional source of energy",
      "It provides exceptionally high energy output per unit mass of fuel",
      "It produces zero greenhouse gas emissions during electricity generation",
      "It is classified as a renewable source of energy"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Nuclear energy is harnessed through controlled nuclear fission of heavy radioactive isotopes such as Uranium-235 (\(^{235}\\text{U}\)) or Plutonium-239 (\(^{239}\\text{Pu}\)). Because the natural terrestrial deposits of uranium ores in the Earth's crust are finite and non-replenishable on human timescales, nuclear fuel is strictly a **non-renewable** resource.

### 2. Physical Context & Practical Illustration:
Nuclear power releases immense energy per reaction via Einstein's mass-energy equivalence (\(E = \\Delta m c^2\)). Just \(1\\text{ kg}\) of Uranium-235 yields as much thermal energy as burning approximately \(1,500,000\\text{ kg}\) of high-grade coal without emitting carbon dioxide smoke. However, fuel reserves remain exhaustible.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Non-conventional source)**: True statement. Modern commercial nuclear power developed in the mid-20th century, making it non-conventional.
- **Option B (Exceptionally high energy output)**: True statement. Nuclear binding energy density is millions of times higher than chemical combustion.
- **Option C (Zero greenhouse gas emissions)**: True statement. Fission reactions produce heat without burning carbon, emitting no \(\\text{CO}_2\) exhaust.
- **Option D (It is classified as a renewable source)**: Incorrect statement (and hence the correct answer). Nuclear fuels are finite mineral ores that cannot regenerate, making them non-renewable.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-026",
    text: "What is the standard formula used to compute gravitational potential energy \\(E_p\\) near Earth's surface?",
    options: [
      "\\(E_p = mgh\\)",
      "\\(E_p = \\frac{1}{2}mv^2\\)",
      "\\(E_p = mgs^2\\)",
      "\\(E_p = \\frac{mg}{h}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done against the constant force of gravity \(F_g = mg\) to lift a body of mass \(m\) vertically through height \(h\) without acceleration is:
\\[
W = F_g \\cdot h = (mg) \\cdot h = mgh
\\]
This work is stored as gravitational potential energy:
\\[
E_p = mgh
\\]
where \(m\) is mass in \(\\text{kg}\), \(g\) is gravitational acceleration in \(\\text{m/s}^2\), and \(h\) is vertical elevation in \(\\text{m}\).

### 2. Physical Context & Practical Illustration:
Whether an object is carried straight up vertically or rolled up a gentle winding ramp, because gravity is a **conservative force**, the total potential energy gained depends purely on the net vertical elevation \(h\), completely independent of the path taken.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(E_p = mgh\\))**: Correct. Standard formula for gravitational potential energy.
- **Option B (\\(E_p = \\frac{1}{2}mv^2\\))**: Incorrect. This is the formula for kinetic energy (\(E_k\)).
- **Option C (\\(E_p = mgs^2\\))**: Incorrect. The dimension would be \([M^1 L^3 T^{-2}]\), which is not energy.
- **Option D (\\(E_p = mg/h\\))**: Incorrect. Potential energy increases with height, not inversely.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-027",
    text: "An object of mass \\(15.0\\text{ kg}\\) is elevated to a height of \\(20.0\\text{ m}\\) above the ground. Taking \\(g = 9.8\\text{ m/s}^2\\), calculate its gravitational potential energy.",
    options: [
      "\\(2940\\text{ N}\\)",
      "\\(2940\\text{ J}\\)",
      "\\(2.940\\text{ J}\\)",
      "\\(29.40\\text{ J}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is given by:
\\[
E_p = mgh
\\]
Substitute the given values:
- \(m = 15.0\\text{ kg}\)
- \(g = 9.8\\text{ m/s}^2\)
- \(h = 20.0\\text{ m}\)
\\[
E_p = 15.0\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 20.0\\text{ m}
\\]
\\[
E_p = 300 \\times 9.8 = 2940\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Energy must always be expressed in units of Joules (\(\\text{J}\)), not Newtons (\(\\text{N}\)). A Newton is a unit of force, while a Joule is a unit of work or energy (\(1\\text{ J} = 1\\text{ N}\\cdot\\text{m}\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (2940 N)**: Incorrect. Newton (\(\\text{N}\)) is the unit of force, not energy.
- **Option B (2940 J)**: Correct. Both numerical magnitude and SI unit (\(\\text{J}\)) are exact.
- **Option C (2.940 J)**: Incorrect. Erroneous decimal scaling by \(10^{-3}\).
- **Option D (29.40 J)**: Incorrect. Erroneous decimal scaling by \(10^{-2}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-028",
    text: "Under what physical condition is an object's gravitational potential energy equal to zero relative to the ground reference plane?",
    options: [
      "When its velocity is zero (\\(v = 0\\))",
      "When its acceleration is zero (\\(a = 0\\))",
      "When its mass is doubled (\\(m = 2m_0\\))",
      "When its vertical height above the reference level is zero (\\(h = 0\\))"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The gravitational potential energy relative to a defined reference plane is:
\\[
E_p = mgh
\\]
For an object of non-zero mass (\(m > 0\)) located in Earth's gravitational field (\(g > 0\)):
\\[
E_p = 0 \\iff h = 0
\\]
Hence, the gravitational potential energy is zero whenever the object rests directly on the chosen zero-height reference datum.

### 2. Physical Context & Practical Illustration:
A cricket ball resting motionless on the turf has zero gravitational potential energy relative to the field because \(h = 0\\text{ m}\). If we dig a ditch of depth \(2\\text{ m}\), relative to the bottom of the ditch the ball would possess positive potential energy \(mg(2)\). Potential energy is always defined relative to a reference level.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (v = 0)**: Incorrect. Zero velocity means kinetic energy is zero (\(E_k = 0\)), but a stationary object at height \(h\) still possesses potential energy \(mgh\).
- **Option B (a = 0)**: Incorrect. An object moving at constant speed at height \(h\) has \(a = 0\) but possesses non-zero potential energy.
- **Option C (Mass is doubled)**: Incorrect. Doubling mass doubles the potential energy.
- **Option D (h = 0)**: Correct. When height is zero, \(E_p = mg(0) = 0\\text{ J}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-029",
    text: "Consider the following statements regarding energy sources:\n(I) Hydroelectricity is a renewable source of energy.\n(II) Fossil fuels are renewable and non-conventional sources of energy.\n(III) Non-conventional sources of energy should be preferred over conventional sources to ensure environmental sustainability.\nWhich statement(s) are correct?",
    options: [
      "Only statement I is correct",
      "Only statement II is correct",
      "Statements I and II are correct",
      "Statements I and III are correct"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Analyzing each statement from an environmental and physical standpoint:
- **Statement I**: True. Hydroelectricity utilizes the natural water cycle driven by solar evaporation and precipitation, replenishing reservoir water indefinitely.
- **Statement II**: False. Coal, petroleum, and natural gas are non-renewable (taking millions of years of fossilization to form) and are conventional (traditional) sources of energy.
- **Statement III**: True. Non-conventional sources (solar, wind, tidal, biomass) produce minimal pollution and do not deplete natural fossil reserves, making them essential for sustainable development.

### 2. Physical Context & Practical Illustration:
Transitioning energy infrastructure from fossil fuel thermal plants to solar, wind, and hydroelectric generation dramatically curbs global carbon emissions and prevents catastrophic resource depletion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Only I)**: Incorrect. Statement III is also fully scientifically valid.
- **Option B (Only II)**: Incorrect. Statement II is completely false.
- **Option C (I and II)**: Incorrect. Fossil fuels are non-renewable and conventional.
- **Option D (I and III)**: Correct. Both Statement I and Statement III are accurate.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-030",
    text: "Which of the following is considered the ultimate, prime source of almost all energy on Earth?",
    options: [
      "Terrestrial green plants",
      "The Sun (solar radiation)",
      "Hydroelectric reservoirs",
      "Atmospheric wind currents"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Nuclear fusion reactions occurring inside the Sun's core (\(4\\,^1\\text{H} \\rightarrow \\,^4\\text{He} + 2e^+ + 2\\nu + 26.7\\text{ MeV}\)) continuously emit vast quantities of radiant electromagnetic energy into space. This solar radiation serves as the primary energetic driver for nearly all Earth systems:
- Drives photosynthesis in plants (the foundation of fossil fuels and biomass).
- Drives atmospheric heating, creating temperature/pressure differentials that generate **wind energy**.
- Powers the hydrologic cycle (evaporation, cloud formation, rain), generating **hydroelectric energy**.

### 2. Physical Context & Practical Illustration:
Without incoming solar radiation, plant photosynthesis would cease, atmospheric circulation would collapse, water cycles would freeze, and all renewable energy flows (except geothermal and nuclear) would terminate.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Plants)**: Incorrect. Plants merely capture and convert solar light into chemical energy via photosynthesis; they are not the primary source.
- **Option B (The Sun)**: Correct. The Sun is the ultimate primary source driving wind, hydro, biomass, and fossil fuels.
- **Option C (Hydroelectric reservoirs)**: Incorrect. Water in reservoirs depends on the solar-powered hydrologic cycle.
- **Option D (Wind)**: Incorrect. Wind is driven by uneven solar heating of the Earth's atmosphere.`
  }
];
