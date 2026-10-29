// scripts/ch2_part2.js - Questions 31 to 60 of Chapter 2 (Work and Energy)
module.exports = [
  {
    id: "MH-9-SCIT-2-2.1-OSC-031",
    text: "Which of the following simple tools is a Class I lever?",
    options: [
      "A wheelbarrow",
      "A kitchen knife",
      "A pair of laboratory forceps",
      "A pair of scissors (or seesaw)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a **Class I lever**, the **Fulcrum (F)** is situated between the **Effort (E)** and the **Load (L)**:
\\[
\\text{Effort} \\longleftrightarrow \\text{Fulcrum} \\longleftrightarrow \\text{Load}
\\]
In a pair of scissors (or a seesaw), the central screw/pivot serves as the fulcrum. The hand applies effort on the handles at one end, and the blades cut through the load (paper or cloth) at the opposite end.

### 2. Physical Context & Practical Illustration:
Depending on the position of the pivot, a Class I lever can provide a mechanical advantage greater than 1 (shear cutters with long handles and short blades) or a displacement/speed advantage (scissors with long blades for rapid paper cutting).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Wheelbarrow)**: Incorrect. A wheelbarrow is a Class II lever (wheel is fulcrum, load in middle, handles at end).
- **Option B (Kitchen knife)**: Incorrect. A knife operates primarily as a wedge or Class III lever.
- **Option C (Pair of forceps)**: Incorrect. Forceps and tweezers are Class III levers (effort applied in the center).
- **Option D (Pair of scissors)**: Correct. The pivot pin (fulcrum) sits directly between the handles (effort) and the blades (load).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-032",
    text: "For an inclined plane, how does decreasing the angle of inclination \\(\\theta\\) affect the magnitude of effort force required to push a load up the slope (neglecting friction)?",
    options: [
      "The required effort force decreases",
      "The required effort force increases",
      "The required effort force remains strictly unchanged",
      "The effort force becomes zero regardless of the load"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
When an object of mass \(m\) is pushed up a frictionless inclined plane inclined at angle \(\\theta\) to the horizontal, the component of gravity acting down the incline is:
\\[
F = mg \\sin\\theta
\\]
Since the sine function \(\\sin\\theta\) is monotonically increasing for \(0^\\circ \\le \\theta \\le 90^\\circ\):
\\[
\\theta \\downarrow \\implies \\sin\\theta \\downarrow \\implies F \\downarrow
\\]
Thus, as the angle of inclination decreases (making the ramp gentler), the force required to move the load up the plane **decreases**.

### 2. Physical Context & Practical Illustration:
Wheelchair ramps and highway mountain passes are constructed with very gentle gradients (small inclination angles) so that heavy vehicles and wheelchairs require minimal driving force to ascend to higher elevations.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Decreases)**: Correct. A smaller slope angle reduces \(\\sin\\theta\), decreasing the required pushing force.
- **Option B (Increases)**: Incorrect. A steeper slope (larger \(\\theta\)) requires greater force, approaching \(mg\) as \(\\theta \\rightarrow 90^\\circ\).
- **Option C (Remains unchanged)**: Incorrect. Force depends directly on \(\\sin\\theta\).
- **Option D (Becomes zero)**: Incorrect. Gravity still acts down the plane unless the slope is completely flat (\(\\theta = 0^\\circ\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-033",
    text: "Which of the following physical systems possesses potential energy?",
    options: [
      "A stretched rubber catapult band",
      "Flowing water in a fast river",
      "Atmospheric wind rotating a wind turbine",
      "A rolling bowling ball"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Potential energy is the energy stored in a body due to its **position, configuration, or state of strain**.
When a rubber catapult band is pulled and stretched, work is performed against the internal elastic intermolecular forces. This work is stored as **elastic potential energy**:
\\[
E_p = \\frac{1}{2} k x^2
\\]
In contrast, flowing river water, blowing wind, and rolling balls possess energy exclusively due to their motion (**kinetic energy**).

### 2. Physical Context & Practical Illustration:
When the stretched rubber band is released, its stored elastic potential energy is instantly converted into kinetic energy, propelling a projectile with high velocity.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Stretched rubber band)**: Correct. Stores elastic potential energy due to structural deformation.
- **Option B (Flowing river water)**: Incorrect. Possesses kinetic energy due to bulk flow velocity.
- **Option C (Wind)**: Incorrect. Moving air masses possess kinetic energy (\(E_k = \\frac{1}{2}mv^2\)).
- **Option D (Rolling bowling ball)**: Incorrect. Possesses translational and rotational kinetic energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-034",
    text: "When a body falls freely towards the Earth in the absence of air resistance, what happens to its total mechanical energy?",
    options: [
      "It continuously increases",
      "It continuously decreases",
      "It remains constant throughout the fall",
      "It drops to zero at the midpoint"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to the **Law of Conservation of Mechanical Energy**, in the presence of only conservative forces (such as gravity), the total mechanical energy \(E\) of an isolated system remains strictly constant:
\\[
E = E_k + E_p = \\frac{1}{2}mv^2 + mgh = \\text{constant}
\\]
At the initial release height \(h\): \(E_p = mgh\) and \(E_k = 0 \\implies E = mgh\).
At any intermediate height \(y\): \(v = \\sqrt{2g(h-y)}\), so \(E_k = mg(h-y)\) and \(E_p = mgy\).
Total energy:
\\[
E = mg(h-y) + mgy = mgh
\\]
The total mechanical energy remains invariant at every instant.

### 2. Physical Context & Practical Illustration:
As a skydiver or dropped stone falls, potential energy is not destroyed; it transforms seamlessly into kinetic energy. Neglecting atmospheric drag, every single Joule of potential energy lost becomes an identical Joule of kinetic energy gained.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Increases)**: Incorrect. Energy cannot be created out of nothing (First Law of Thermodynamics).
- **Option B (Decreases)**: Incorrect. In a conservative field without dissipative air drag, mechanical energy is conserved.
- **Option C (Remains constant)**: Correct. The sum \(E_k + E_p\) is conserved at all points along the vertical trajectory.
- **Option D (Drops to zero)**: Incorrect. Energy is continuous and never vanishes.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-035",
    text: "Why are winding, zigzag roads (ghats) constructed along steep mountainsides rather than straight, direct vertical roads?",
    options: [
      "To reduce the driving effort force required by vehicles to climb the elevation",
      "To shorten the total travel distance to the mountain summit",
      "To decrease the total mechanical work required to reach the top",
      "To maximize vehicle fuel consumption"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A winding ghat road acts as an **inclined plane**.
The gravitational component opposing vehicle motion up an incline is:
\\[
F_{\\text{effort}} = mg \\sin\\theta
\\]
By wrapping the road around the mountain, the track length \(s\) increases substantially, which dramatically reduces the slope angle \(\\theta\). Because \(\\theta\) is small:
\\[
\\sin\\theta = \\frac{h}{s} \\ll 1 \\implies F_{\\text{effort}} \\ll mg
\\]
Vehicle engines do not possess enough torque to drive straight up a vertical cliff (\(\\theta \\approx 90^\\circ\)), but can easily climb a gentle slope.

### 2. Physical Context & Practical Illustration:
Although the total work done against gravity (\(W = mgh\)) remains unchanged, spreading that work over a much longer displacement drastically reduces the required engine thrust force:
\\[
W = F_{\\text{effort}} \\times s = mgh = \\text{constant}
\\]

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Reduces effort force)**: Correct. Increasing the path length reduces the slope angle, drastically decreasing required climbing force.
- **Option B (Shortens distance)**: Incorrect. Winding roads significantly lengthen total path distance.
- **Option C (Decreases total work)**: Incorrect. Work against gravity (\(mgh\)) is path-independent; total work remains the same.
- **Option D (Maximizes fuel consumption)**: Incorrect. It makes ascending physically feasible for standard engines.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-036",
    text: "During photosynthesis, what type of energy is stored in the glucose molecules synthesized by green plants?",
    options: [
      "Solar radiant energy",
      "Gravitational potential energy",
      "Chemical potential energy",
      "Thermal energy"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
During photosynthesis, chloroplasts capture radiant solar photons to drive an endothermic biochemical reaction:
\\[
6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{Solar Energy} \\xrightarrow{\\text{chlorophyll}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2
\\]
The radiant energy of absorbed sunlight is converted into stable covalent bond energies of carbohydrates, stored as **chemical potential energy**.

### 2. Physical Context & Practical Illustration:
This chemical energy stored in plant tissue forms the foundational energetic base for all terrestrial food chains and the origin of fossil fuels (coal, petroleum), which represent ancient plant biomass compressed over millions of years.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Solar radiant energy)**: Incorrect. Solar energy is the input; it is converted and no longer exists as radiant photons.
- **Option B (Gravitational potential energy)**: Incorrect. Molecular bonds do not store gravitational elevation energy.
- **Option C (Chemical potential energy)**: Correct. Energy is stored within the chemical bonds of glucose and starch.
- **Option D (Thermal energy)**: Incorrect. Thermal energy is dissipated heat, not the stable stored bond energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-037",
    text: "Which of the following cutting tools functions on the mechanical principle of a wedge?",
    options: [
      "A carpenter's chisel",
      "An axe blade",
      "A kitchen knife",
      "All of the above"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **wedge** is a simple machine formed by two inclined planes placed back to back, tapering to a sharp edge. When a driving force is applied to the blunt end of the wedge, it converts the forward longitudinal effort into large perpendicular lateral forces that split, cut, or slice materials apart.

### 2. Physical Context & Practical Illustration:
- **Knives**: Sharp double-beveled blades slice vegetables by wedging fibers apart.
- **Chisels**: Woodworkers drive chisels with mallets to cleave wood along grain boundaries.
- **Axes**: Woodchoppers split massive logs using heavy, wedge-shaped steel axe heads.
All of these utilize identical dual inclined plane geometry.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Chisel)**: A valid wedge, but not the only one.
- **Option B (Axe blade)**: A classic heavy wedge, but not the only one.
- **Option C (Kitchen knife)**: A sharp slicing wedge, but not the only one.
- **Option D (All of the above)**: Correct. Chisels, axe heads, and knives are all canonical examples of wedges.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-038",
    text: "Which of the following conditions is essential for the viable operation of commercial wind power plants?",
    options: [
      "They can only be established deep underground",
      "They can operate effectively in regions with zero atmospheric air movement",
      "They require high solar radiation levels to generate electricity directly",
      "They can be economically established only in regions with consistent wind speeds above approximately \\(15\\text{ km/h}\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The theoretical kinetic power available in a moving wind stream of density \(\\rho\) sweeping through a rotor area \(A\) with velocity \(v\) is:
\\[
P_{\\text{wind}} = \\frac{1}{2} \\rho A v^3
\\]
Because power depends on the **cube of wind speed** (\(P \\propto v^3\)), a slight drop in wind velocity causes a massive drop in generated electrical power. Commercial wind turbines require a minimum 'cut-in' speed (typically \(\\approx 15\\text{ km/h}\) or \(4.2\\text{ m/s}\)) to overcome mechanical friction and turn generators profitably.

### 2. Physical Context & Practical Illustration:
Consequently, large wind turbine farms are located along windy coastal zones, high mountain ridges, and open plains (such as Tamil Nadu, Gujarat, and Maharashtra in India) where robust, sustained wind speeds persist year-round.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Underground)**: Incorrect. Wind turbines require unobstructed atmospheric airflow high above ground.
- **Option B (Zero air movement)**: Incorrect. If \(v = 0\), wind power is strictly zero.
- **Option C (Solar radiation directly)**: Incorrect. Turbines convert kinetic energy of air, not photons.
- **Option D (Consistent wind speeds \\(\\ge 15\\text{ km/h}\\))**: Correct. Necessary to ensure continuous, economical electrical generation.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-039",
    text: "In a hydroelectric power station, water stored at a high elevation is released to drive hydraulic turbines connected to electrical generators. Which fundamental physical principle governs this generation cycle?",
    options: [
      "Law of Conservation of Mass",
      "Law of Conservation of Electric Charge",
      "Law of Conservation of Energy",
      "Law of Conservation of Linear Momentum"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A hydroelectric facility performs a multi-stage energy conversion:
\\[
\\text{Gravitational Potential Energy (water at height } h)
\\]
\\[
\\downarrow
\\]
\\[
\\text{Kinetic Energy (rushing water in penstocks: } \\frac{1}{2}mv^2)
\\]
\\[
\\downarrow
\\]
\\[
\\text{Mechanical Rotational Energy (spinning turbine blades)}
\\]
\\[
\\downarrow
\\]
\\[
\\text{Electrical Energy (electromagnetic induction in generators)}
\\]
No energy is created or destroyed; it is merely transformed from potential energy into electrical energy, strictly obeying the **Law of Conservation of Energy**.

### 2. Physical Context & Practical Illustration:
Hydroelectric power represents one of the most efficient renewable energy systems worldwide, operating at energy conversion efficiencies often exceeding \(90\\%\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Conservation of mass)**: Incorrect. While mass is conserved, it is not the principle driving energy transformation.
- **Option B (Conservation of charge)**: Incorrect. Relates to circuit neutrality, not bulk energy conversion.
- **Option C (Conservation of energy)**: Correct. Potential energy of elevated water converts into kinetic and then electrical energy.
- **Option D (Conservation of momentum)**: Incorrect. Momentum transfer occurs at turbine blades, but the macroscopic power conversion principle is conservation of energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-040",
    text: "In which of the following solar-powered devices is the primary ultimate useful output NOT thermal (heat) energy?",
    options: [
      "A solar photovoltaic cell",
      "A domestic solar water heater",
      "A solar box cooker",
      "A solar metallurgical furnace"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let us analyze the operational mechanism of each device:
- **Solar cell (Photovoltaic cell)**: Uses semiconductor p-n junctions (silicon) to absorb solar photons and create electron-hole pairs, producing an electromotive force (EMF) that drives an electric current. The useful output is **electrical energy**.
- **Solar water heater**: Absorbs sunlight using black-coated copper collector tubes to heat water (**thermal energy**).
- **Solar cooker**: Uses mirrors to trap infrared radiation in an insulated box to cook food (**thermal energy**).
- **Solar furnace**: Uses parabolic reflectors to concentrate sunlight onto a small focal point, reaching temperatures exceeding \(3000^\\circ\\text{C}\) (**thermal energy**).

### 2. Physical Context & Practical Illustration:
Solar photovoltaic cells power home inverters, laptops, streetlights, and orbital space stations by generating clean electric voltage directly from sunlight without generating heat as the desired output.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Solar photovoltaic cell)**: Correct. Produces electrical energy directly, not thermal energy.
- **Option B (Solar water heater)**: Incorrect. Designed explicitly to produce thermal heat.
- **Option C (Solar cooker)**: Incorrect. Designed explicitly to produce thermal heat.
- **Option D (Solar furnace)**: Incorrect. Designed to generate intense concentrated thermal heat.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-041",
    text: "A satellite orbits the Earth in a circular orbit of constant radius \\(R\\) at constant speed \\(v\\). How much work is done by the gravitational force on the satellite during one complete revolution?",
    options: [
      "\\(F_g \\times 2\\pi R\\)",
      "\\(-F_g \\times 2\\pi R\\)",
      "\\(mgh\\)",
      "Zero"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Earth's gravitational attraction provides the required **centripetal force** \(\\vec{F}_g\) acting radially inwards towards the center of Earth:
\\[
\\vec{F}_g = -\\frac{G M m}{R^2} \\hat{r}
\\]
At every point along the circular orbit, the instantaneous displacement vector \(d\\vec{s}\) is directed tangentially to the orbit.
Because radius is perpendicular to the tangent at all points:
\\[
\\vec{F}_g \\perp d\\vec{s} \\implies \\theta = 90^\\circ
\\]
Work done in any infinitesimal displacement is:
\\[
dW = \\vec{F}_g \\cdot d\\vec{s} = F_g \\cdot ds \\cdot \\cos 90^\\circ = 0
\\]
Integrating over one full orbit:
\\[
W = \\oint \\vec{F}_g \\cdot d\\vec{s} = 0\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Because the gravitational force does zero work on the satellite, the satellite's orbital speed and kinetic energy remain constant year after year without consuming any onboard fuel to maintain orbit.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(F_g \\times 2\\pi R\\))**: Incorrect. Assumes force acts in the direction of motion, which is false.
- **Option B (\\(-F_g \\times 2\\pi R\\))**: Incorrect. Gravity does not act opposite to motion.
- **Option C (\\(mgh\\))**: Incorrect. Applies to vertical lifting near Earth's surface, not circular orbits.
- **Option D (Zero)**: Correct. Gravitational force is strictly perpendicular to the displacement at every point (\(\\cos 90^\\circ = 0\\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-042",
    text: "A block of mass \\(m\\) is displaced horizontally over a distance \\(d\\). A force \\(F\\) is applied strictly perpendicular to the block's displacement. How much work is done on the block by this force \\(F\\)?",
    options: [
      "\\(mFd\\)",
      "Zero",
      "\\(Fd\\)",
      "\\(-Fd\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The work done by a constant force \(F\) causing a displacement \(d\) is:
\\[
W = F \\cdot d \\cdot \\cos\\theta
\\]
Since the applied force is perpendicular to displacement, \(\\theta = 90^\\circ\).
\\[
\\cos 90^\\circ = 0 \\implies W = F \\times d \\times 0 = 0\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
For example, the normal reaction force exerted by the ground on a sliding crate acts vertically upward while the crate moves horizontally. Consequently, the normal reaction force does zero work on the sliding crate.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (mFd)**: Incorrect. Incompatible dimensional units.
- **Option B (Zero)**: Correct. Force perpendicular to displacement does strictly zero work.
- **Option C (Fd)**: Incorrect. Valid only when \(\\theta = 0^\\circ\) (parallel).
- **Option D (-Fd)**: Incorrect. Valid only when \(\\theta = 180^\\circ\) (antiparallel).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-043",
    text: "According to the Work-Energy Theorem, what happens to the kinetic energy of a moving object if the net work done on it is positive (\\(W_{\\text{net}} > 0\\))?",
    options: [
      "The kinetic energy increases",
      "The kinetic energy decreases",
      "The kinetic energy remains completely unchanged",
      "The kinetic energy instantly drops to zero"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Work-Energy Theorem** states that the net work done by all forces acting on a particle equals the change in its kinetic energy:
\\[
W_{\\text{net}} = \\Delta E_k = E_{k,\\text{final}} - E_{k,\\text{initial}}
\\]
If the net work done is positive (\(W_{\\text{net}} > 0\)):
\\[
E_{k,\\text{final}} - E_{k,\\text{initial}} > 0 \\implies E_{k,\\text{final}} > E_{k,\\text{initial}}
\\]
Hence, the kinetic energy of the object **increases**.

### 2. Physical Context & Practical Illustration:
When a car's engine applies forward traction that exceeds resistive rolling friction and air drag, the net work done on the car is positive, causing the car to accelerate and increase its kinetic energy.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Increases)**: Correct. Positive net work transfers energy into the body, increasing \(E_k\).
- **Option B (Decreases)**: Incorrect. Kinetic energy decreases when net work done is negative (\(W_{\\text{net}} < 0\), e.g. braking).
- **Option C (Remains unchanged)**: Incorrect. Kinetic energy remains constant only when net work done is zero.
- **Option D (Drops to zero)**: Incorrect. Positive work accelerates the body, never stopping it.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-044",
    text: "A block of mass \\(m\\) is pulled horizontally over a distance \\(d\\) by an applied force \\(F\\) directed parallel and in the same direction as the displacement. What is the work done on the block by this force?",
    options: [
      "\\(mFd\\)",
      "Zero",
      "\\(Fd\\)",
      "\\(-Fd\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done by a constant force is:
\\[
W = F \\cdot d \\cdot \\cos\\theta
\\]
When the force acts parallel and along the direction of displacement:
\\[
\\theta = 0^\\circ \\implies \\cos 0^\\circ = 1
\\]
\\[
W = F \\times d \\times 1 = Fd
\\]

### 2. Physical Context & Practical Illustration:
This represents maximum positive work for given magnitudes of force and displacement. Energy is efficiently transferred directly into the kinetic energy or potential energy of the block.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (mFd)**: Incorrect. Mass is not multiplied into work; \(W = Fd\).
- **Option B (Zero)**: Incorrect. Valid only if \(\\theta = 90^\\circ\).
- **Option C (Fd)**: Correct. Standard formulation when \(\\theta = 0^\\circ\).
- **Option D (-Fd)**: Incorrect. Valid when force opposes displacement (\(\\theta = 180^\\circ\)).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-045",
    text: "A container of mass \\(5\\text{ kg}\\) is lifted vertically to a height of \\(8\\text{ m}\\) and then slowly lowered back to its initial ground position. What is the total net work done by the gravitational force on the container over this entire round trip?",
    options: [
      "\\(+400\\text{ J}\\)",
      "\\(-400\\text{ J}\\)",
      "\\(0\\text{ J}\\)",
      "\\(50\\text{ J}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravity is a **conservative force**. The work done by any conservative force on a closed path (round trip where initial and final positions are identical) is strictly zero:
\\[
\\oint \\vec{F}_g \\cdot d\\vec{r} = 0
\\]
Mathematically, dividing the journey into two parts (taking \(g \\approx 10\\text{ m/s}^2\) or \(9.8\\text{ m/s}^2\)):
1. **Lifting upward** (\(\\vec{F}_g\) downwards, displacement upwards, \(\\theta = 180^\\circ\)):
\\[
W_{\\text{up}} = -mgh = - (5 \\times 10 \\times 8) = -400\\text{ J}
\\]
2. **Lowering downward** (\(\\vec{F}_g\) downwards, displacement downwards, \(\\theta = 0^\\circ\)):
\\[
W_{\\text{down}} = +mgh = + (5 \\times 10 \\times 8) = +400\\text{ J}
\\]
**Total work done by gravity**:
\\[
W_{\\text{total}} = W_{\\text{up}} + W_{\\text{down}} = -400\\text{ J} + 400\\text{ J} = 0\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
Because gravitational work depends solely on initial and final positions (state function) and not on the path taken, whenever an object returns to its starting elevation, net gravitational work is always exactly **zero**.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (+400 J)**: Incorrect. This is the work done by gravity on the downward trip only.
- **Option B (-400 J)**: Incorrect. This is the work done by gravity on the upward trip only.
- **Option C (0 J)**: Correct. Over the complete round trip, negative upward work and positive downward work cancel completely.
- **Option D (50 J)**: Incorrect. Arbitrary calculation error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-046",
    text: "An object is thrown straight up into the air and then falls back down. Which of the following correctly describes the sign of the work done by gravity during the upward and downward motions?",
    options: [
      "Positive on the way up, positive on the way down",
      "Negative on the way up, negative on the way down",
      "Negative on the way up, positive on the way down",
      "Positive on the way up, negative on the way down"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational force \(\\vec{F}_g\) always points vertically downward towards the center of Earth.
1. **On the way up**:
   - Displacement vector \(\\vec{s}\) is directed vertically upward.
   - Angle between \(\\vec{F}_g\) and \(\\vec{s}\) is \(\\theta = 180^\\circ\).
   - Work done: \(W = F_g s \\cos 180^\\circ = -mgh\) (**Negative work**).
2. **On the way down**:
   - Displacement vector \(\\vec{s}\) is directed vertically downward.
   - Angle between \(\\vec{F}_g\) and \(\\vec{s}\) is \(\\theta = 0^\\circ\).
   - Work done: \(W = F_g s \\cos 0^\\circ = +mgh\) (**Positive work**).

### 2. Physical Context & Practical Illustration:
On the way up, gravity opposes the motion, removing kinetic energy and storing it as potential energy (\(W < 0\)). On the way down, gravity assists the motion, accelerating the object and restoring kinetic energy (\(W > 0\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. Gravity cannot do positive work when pulling opposite to upward motion.
- **Option B**: Incorrect. Gravity does not do negative work when the body falls in the direction of the force.
- **Option C**: Correct. Negative on the way up (\(\\theta = 180^\\circ\)), positive on the way down (\(\\theta = 0^\\circ\)).
- **Option D**: Incorrect. Inverts the physical signs of both phases.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-047",
    text: "An iron block of mass \\(15.0\\text{ kg}\\) rests on a platform \\(20.0\\text{ m}\\) above the ground. Taking \\(g = 9.8\\text{ m/s}^2\\), what is its gravitational potential energy?",
    options: [
      "\\(2940\\text{ N}\\)",
      "\\(2940\\text{ J}\\)",
      "\\(300\\text{ J}\\)",
      "\\(150\\text{ J}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is given by:
\\[
E_p = mgh
\\]
Given:
- Mass \(m = 15.0\\text{ kg}\)
- Acceleration due to gravity \(g = 9.8\\text{ m/s}^2\)
- Height \(h = 20.0\\text{ m}\)

Calculation:
\\[
E_p = 15.0 \\times 9.8 \\times 20.0 = 300 \\times 9.8 = 2940\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
The Joules unit denotes energy, which equals force multiplied by distance (\(1\\text{ J} = 1\\text{ N}\\cdot\\text{m}\)). The weight of the block is \(W = mg = 15 \\times 9.8 = 147\\text{ N}\). Moving this weight through \(20\\text{ m}\) yields \(147\\text{ N} \\times 20\\text{ m} = 2940\\text{ J}\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (2940 N)**: Incorrect. Newton is the unit of force, not energy.
- **Option B (2940 J)**: Correct. Both numerical value and SI energy unit are correct.
- **Option C (300 J)**: Incorrect. This is simply \(m \\times h = 15 \\times 20\), omitting \(g\).
- **Option D (150 J)**: Incorrect. Calculation error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-048",
    text: "During the free fall of an object under gravity from a height, which continuous energy conversion occurs?",
    options: [
      "Kinetic energy is converted into potential energy",
      "Mechanical energy is converted into nuclear energy",
      "Thermal energy is converted into chemical energy",
      "Gravitational potential energy is continuously converted into kinetic energy"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
As a body falls freely from initial height \(h\):
- Elevation \(y\) decreases continuously, causing gravitational potential energy \(E_p = mgy\) to decrease.
- Downward velocity \(v = \\sqrt{2g(h-y)}\) increases continuously, causing kinetic energy \(E_k = \\frac{1}{2}mv^2 = mg(h-y)\) to increase.
Since total mechanical energy is conserved (\(E = E_p + E_k = \\text{constant}\)), the lost potential energy converts directly into kinetic energy:
\\[
-\\Delta E_p = +\\Delta E_k
\\]

### 2. Physical Context & Practical Illustration:
A diver jumping off a \(10\\text{ m}\) high platform starts with maximum potential energy and zero speed. Just before hitting the water, potential energy is minimal and speed is maximum (\(\\approx 14\\text{ m/s}\)), illustrating complete potential-to-kinetic conversion.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Kinetic to potential)**: Incorrect. This occurs when an object is launched upward against gravity.
- **Option B (Mechanical to nuclear)**: Incorrect. Free fall does not alter atomic nuclei.
- **Option C (Thermal to chemical)**: Incorrect. Free fall involves macroscopic mechanical energy.
- **Option D (Potential to kinetic)**: Correct. Gravitational potential energy continuously transforms into kinetic energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-049",
    text: "Which of the following devices is an example of a Class II lever?",
    options: [
      "A human forearm lifting a weight",
      "A playground seesaw",
      "A lime (lemon) squeezer",
      "A pair of laboratory tongs"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a **Class II lever**, the **Load (L)** is situated between the **Fulcrum (F)** and the **Effort (E)**:
\\[
F - L - E
\\]
In a lime squeezer:
- Fulcrum: The pivot hinge joining the two arms at the tip.
- Load: The lime placed in the central perforated cup.
- Effort: The human hand pressing down on the handles at the outer ends.

### 2. Physical Context & Practical Illustration:
Because the distance from the pivot to the effort handle is always greater than the distance from the pivot to the lemon (\(d_E > d_L\)), the mechanical advantage is greater than 1, allowing easy squeezing of tough fruit rind.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Human forearm)**: Class III lever (elbow is fulcrum, bicep effort attaches between elbow and hand load).
- **Option B (Seesaw)**: Class I lever (central fulcrum between two seats).
- **Option C (Lime squeezer)**: Correct. Load sits between the pivot fulcrum and effort handles.
- **Option D (Pair of tongs)**: Class III lever (fulcrum at joint, effort applied in middle by fingers).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-050",
    text: "A student of mass \\(55\\text{ kg}\\) runs up a flight of stairs consisting of \\(27\\text{ steps}\\), each \\(20\\text{ cm}\\) high, in a time of \\(5.4\\text{ seconds}\\). Taking \\(g = 9.8\\text{ m/s}^2\\), calculate the power developed by the student.",
    options: [
      "\\(400\\text{ W}\\)",
      "\\(1485\\text{ W}\\)",
      "\\(539\\text{ W}\\)",
      "\\(664\\text{ W}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Total vertical height climbed (\\(h\\))**:
\\[
h = 27 \\times 20\\text{ cm} = 540\\text{ cm} = 5.4\\text{ m}
\\]
2. **Work done against gravity (\\(W\\))**:
\\[
W = mgh = 55\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 5.4\\text{ m} = 2910.6\\text{ J}
\\]
3. **Power developed (\\(P\\))**:
\\[
P = \\frac{W}{t} = \\frac{2910.6\\text{ J}}{5.4\\text{ s}} = 55 \\times 9.8 = 539\\text{ W}
\\]

### 2. Physical Context & Practical Illustration:
A power output of \(539\\text{ W}\) is equivalent to approximately \(0.72\\text{ horsepower}\) (\(1\\text{ hp} \\approx 746\\text{ W}\)). An athletic teenager can sustain this level of mechanical exertion during a brief, intense sprint up stairs.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (400 W)**: Incorrect. Underestimates work done or assumes incorrect height.
- **Option B (1485 W)**: Incorrect. Omits gravity (\(55 \\times 27\)) or arithmetic error.
- **Option C (539 W)**: Correct. Exact computation: \(P = \\frac{55 \\times 9.8 \\times 5.4}{5.4} = 539\\text{ W}\).
- **Option D (664 W)**: Incorrect. Calculation error.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-051",
    text: "What is the angle \\(\\theta\\) between the applied force and the displacement vector when the work done by the force is negative?",
    options: [
      "\\(0^\\circ\\)",
      "\\(45^\\circ\\)",
      "\\(90^\\circ\\)",
      "\\(180^\\circ\\)"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done is defined by the dot product:
\\[
W = F s \\cos\\theta
\\]
Since magnitudes \(F > 0\) and \(s > 0\), the sign of \(W\) depends strictly on \(\\cos\\theta\):
- For \(0^\\circ \\le \\theta < 90^\\circ\): \(\\cos\\theta > 0 \\implies W > 0\) (Positive work).
- For \(\\theta = 90^\\circ\): \(\\cos 90^\\circ = 0 \\implies W = 0\) (Zero work).
- For \(90^\\circ < \\theta \\le 180^\\circ\): \(\\cos\\theta < 0 \\implies W < 0\) (**Negative work**).
Specifically, at \(\\theta = 180^\\circ\), \(\\cos 180^\\circ = -1\), producing maximum negative work (\(W = -Fs\)).

### 2. Physical Context & Practical Illustration:
When brake pads clamp onto rotating bicycle wheels, the frictional force opposes the direction of forward motion (\(\\theta = 180^\\circ\\)). The work done by friction is negative, removing kinetic energy from the bicycle and dissipating it as heat into the rims and air.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(0^\\circ\\))**: Incorrect. \(\\cos 0^\\circ = +1\\), which yields positive work.
- **Option B (\\(45^\\circ\\))**: Incorrect. \(\\cos 45^\\circ = +0.707\\), which yields positive work.
- **Option C (\\(90^\\circ\\))**: Incorrect. \(\\cos 90^\\circ = 0\\), which yields zero work.
- **Option D (\\(180^\\circ\\))**: Correct. \(\\cos 180^\\circ = -1\\), giving negative work.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-052",
    text: "What is the standard SI unit of work and energy?",
    options: [
      "Joule (\\(\\text{J}\\))",
      "Kilogram (\\(\\text{kg}\\))",
      "Meter (\\(\\text{m}\\))",
      "Newton (\\(\\text{N}\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work is defined as:
\\[
W = \\text{Force} \\times \\text{Displacement}
\\]
In SI base units:
\\[
[W] = \\text{Newton} \\times \\text{meter} = (\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}) \\times \\text{m} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2} = \\text{Joule (J)}
\\]
One Joule is the work done by a force of \(1\\text{ Newton}\) displacing an object by \(1\\text{ meter}\) along its line of action.

### 2. Physical Context & Practical Illustration:
Named after English physicist James Prescott Joule for his pioneering work on the mechanical equivalence of heat, the Joule serves as the unified SI unit for all mechanical, electrical, chemical, and thermal energy measurements.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Joule)**: Correct. Standard SI unit for both work and energy.
- **Option B (Kilogram)**: Incorrect. SI unit of mass.
- **Option C (Meter)**: Incorrect. SI unit of length/displacement.
- **Option D (Newton)**: Incorrect. SI unit of force.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-053",
    text: "In an isolated (closed) physical system, what happens to the total amount of energy over time?",
    options: [
      "It continuously decreases due to natural entropy decay",
      "It remains strictly conserved and constant",
      "It increases exponentially as the universe expands",
      "It converts completely into mass without remainder"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The **Law of Conservation of Energy** (First Law of Thermodynamics) asserts that:
*Energy can neither be created nor destroyed; it can only be transformed from one form into another.*
For an isolated system with no mass or energy exchange with surroundings:
\\[
\\Delta E_{\\text{total}} = 0 \\implies E_{\\text{total}} = \\text{constant}
\\]

### 2. Physical Context & Practical Illustration:
In an isolated thermos flask or an oscillating frictionless pendulum, energy may shift back and forth between kinetic energy, gravitational potential energy, and internal thermal vibration, but the grand total of all energy forms remains identical.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Continuously decreases)**: Incorrect. Energy cannot disappear or be destroyed.
- **Option B (Remains conserved and constant)**: Correct. Fundamental conservation law of physics.
- **Option C (Increases exponentially)**: Incorrect. Energy cannot be created from nothing.
- **Option D (Converts completely into mass)**: Incorrect. Mass-energy equivalence holds, but total mass-energy remains conserved.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-054",
    text: "If the mass of an object is doubled while keeping its height above the ground constant, its gravitational potential energy will:",
    options: [
      "Double (increase by a factor of 2)",
      "Decrease to half",
      "Remain unchanged",
      "Quadruple (increase by a factor of 4)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is given by:
\\[
E_p = mgh
\\]
Since \(g\) and \(h\) are kept constant, potential energy is directly proportional to mass:
\\[
E_p \\propto m
\\]
If the mass becomes \(m' = 2m\):
\\[
E_p' = (2m)gh = 2(mgh) = 2E_p
\\]
Therefore, the gravitational potential energy **doubles**.

### 2. Physical Context & Practical Illustration:
Lifting a \(10\\text{ kg}\) box to the top of a shelf requires exactly twice as much mechanical work against gravity as lifting a \(5\\text{ kg}\) box to the same height. Consequently, the stored potential energy is twice as large.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Double)**: Correct. Direct linear dependence on mass (\(E_p \\propto m\)).
- **Option B (Decrease to half)**: Incorrect. Potential energy increases with mass, not inversely.
- **Option C (Remain unchanged)**: Incorrect. Potential energy depends explicitly on mass.
- **Option D (Quadruple)**: Incorrect. Quadratic scaling applies to velocity in kinetic energy (\(v^2\)), not mass in potential energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-055",
    text: "A speed of \\(10\\text{ m/s}\\) is equivalent to what speed in kilometers per hour (\\(\\text{km/h}\\))?",
    options: [
      "\\(20\\text{ km/h}\\)",
      "\\(36\\text{ km/h}\\)",
      "\\(25\\text{ km/h}\\)",
      "\\(18\\text{ km/h}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
To convert speed from meters per second (\(\\text{m/s}\)) to kilometers per hour (\(\\text{km/h}\)):
\\[
1\\text{ m/s} = \\frac{10^{-3}\\text{ km}}{(1/3600)\\text{ h}} = \\frac{3600}{1000}\\text{ km/h} = \\frac{18}{5}\\text{ km/h} = 3.6\\text{ km/h}
\\]
Given speed \(v = 10\\text{ m/s}\):
\\[
v = 10 \\times \\frac{18}{5}\\text{ km/h} = 2 \\times 18 = 36\\text{ km/h}
\\]

### 2. Physical Context & Practical Illustration:
A sprinter running at \(10\\text{ m/s}\) (covering \(100\\text{ m}\) in \(10\\text{ seconds}\)) moves at an instantaneous speed of \(36\\text{ km/h}\), which is roughly the speed of an urban city bus.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (20 km/h)**: Incorrect. Simple doubling error.
- **Option B (36 km/h)**: Correct. Exact conversion: \(10 \\times 3.6 = 36\\text{ km/h}\).
- **Option C (25 km/h)**: Incorrect. Random distractor.
- **Option D (18 km/h)**: Incorrect. Represents \(5\\text{ m/s} \\times 3.6 = 18\\text{ km/h}\).`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-056",
    text: "What is the standard unit of work and energy in the CGS (Centimeter-Gram-Second) system?",
    options: [
      "Joule (\\(\\text{J}\\))",
      "Dyne (\\(\\text{dyn}\\))",
      "Erg",
      "Watt (\\(\\text{W}\\))"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the CGS system:
- Unit of force = **Dyne** (\(1\\text{ dyn} = 1\\text{ g}\\cdot\\text{cm/s}^2 = 10^{-5}\\text{ N}\))
- Unit of displacement = **Centimeter** (\(\\text{cm} = 10^{-2}\\text{ m}\))

The unit of work is:
\\[
\\text{Work} = \\text{Force} \\times \\text{Displacement} = 1\\text{ dyne} \\times 1\\text{ cm} = 1\\text{ erg}
\\]
Conversion to SI Joules:
\\[
1\\text{ erg} = 10^{-5}\\text{ N} \\times 10^{-2}\\text{ m} = 10^{-7}\\text{ J} \\implies 1\\text{ J} = 10^7\\text{ erg}
\\]

### 2. Physical Context & Practical Illustration:
Because an erg represents a tiny amount of energy (\(10^{-7}\\text{ Joules}\)), it was historically used in micro-calorimetry and astrophysics before the worldwide standardization of the SI Joule.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Joule)**: Incorrect. Joule is the SI (MKS) unit of work/energy.
- **Option B (Dyne)**: Incorrect. Dyne is the CGS unit of force, not work.
- **Option C (Erg)**: Correct. Erg is the canonical CGS unit of work and energy.
- **Option D (Watt)**: Incorrect. Watt is the SI unit of power.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-057",
    text: "Which of the following physical systems possesses kinetic energy rather than purely potential energy?",
    options: [
      "A drawn, stretched bow and arrow held stationary",
      "A rapidly spinning toy top on a table",
      "Water stored behind a high hydroelectric dam",
      "A tightly wound steel watch spring"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
- **Kinetic energy** (\(E_k = \\frac{1}{2}I\\omega^2\) or \(\\frac{1}{2}mv^2\)) is the energy possessed by a body by virtue of its **motion**. A spinning top is undergoing rotational motion at high angular velocity \(\\omega\), so it possesses rotational kinetic energy.
- **Potential energy** is energy possessed due to position or deformed configuration:
  - Stretched bow: Elastic potential energy (\(\\frac{1}{2}kx^2\)).
  - Dam water: Gravitational potential energy (\(mgh\)).
  - Wound spring: Elastic potential energy (\(\\frac{1}{2}k\\theta^2\)).

### 2. Physical Context & Practical Illustration:
The spinning top is the odd one out because its energy is dynamic and kinetic, whereas the other three systems store stationary potential energy ready to be released upon trigger.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Stretched bow)**: Stores elastic potential energy.
- **Option B (Spinning top)**: Correct. Possesses rotational kinetic energy due to active motion.
- **Option C (Dam water)**: Stores gravitational potential energy.
- **Option D (Wound watch spring)**: Stores elastic potential energy.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-058",
    text: "How much gravitational potential energy does an object of mass \\(15\\text{ kg}\\) possess when placed on a ledge \\(2\\text{ m}\\) above the floor? (Take \\(g = 9.8\\text{ m/s}^2\\))",
    options: [
      "\\(30\\text{ J}\\)",
      "\\(294\\text{ J}\\)",
      "\\(147\\text{ J}\\)",
      "\\(0\\text{ J}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Gravitational potential energy is calculated by:
\\[
E_p = mgh
\\]
Given:
- Mass \(m = 15\\text{ kg}\)
- Acceleration due to gravity \(g = 9.8\\text{ m/s}^2\)
- Height \(h = 2\\text{ m}\)

Substituting the values:
\\[
E_p = 15\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 2\\text{ m} = 30 \\times 9.8 = 294\\text{ J}
\\]

### 2. Physical Context & Practical Illustration:
This \(294\\text{ Joules}\) of energy represents the exact physical work that was performed against gravity to hoist the \(15\\text{ kg}\) load up from the floor to the ledge.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (30 J)**: Incorrect. Multiplies only mass and height (\(15 \\times 2 = 30\)), completely omitting \(g\).
- **Option B (294 J)**: Correct. Exact computation: \(15 \\times 9.8 \\times 2 = 294\\text{ J}\).
- **Option C (147 J)**: Incorrect. Computes \(E_p\) for \(1\\text{ m}\) height instead of \(2\\text{ m}\).
- **Option D (0 J)**: Incorrect. Potential energy is non-zero at an elevation above the reference floor.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-059",
    text: "Plimsoll lines (load lines) indicating legal buoyancy and safe cargo limits are marked on the hull of which of the following vehicles?",
    options: [
      "Commercial cargo airplanes",
      "Submarines",
      "Electric commuter trains",
      "Cargo and merchant ocean ships"
    ],
    correctAnswer: "D",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A **Plimsoll line** is a reference mark located on a ship's hull that indicates the maximum depth to which the vessel may be safely loaded in different water densities and temperatures (Fresh water, Summer salt water, Winter North Atlantic, etc.).
By Archimedes' principle:
\\[
\\text{Buoyant Force } F_B = \\rho_{\\text{water}} \\cdot V_{\\text{submerged}} \\cdot g = \\text{Total Weight of Ship}
\\]
Because seawater density \(\\rho\) varies with salinity and water temperature, the submerged displacement volume \(V_{\\text{submerged}}\) changes.

### 2. Physical Context & Practical Illustration:
Introduced by British Member of Parliament Samuel Plimsoll in 1876, these lines prevent unscrupulous shipowners from overloading merchant vessels, which had previously caused hundreds of shipwrecks and sailor fatalities.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Airplanes)**: Incorrect. Airplanes use gross takeoff weight limits, not hull waterlines.
- **Option B (Submarines)**: Incorrect. Submarines submerge completely; they regulate buoyancy using internal ballast tanks.
- **Option C (Trains)**: Incorrect. Trains operate on rails, not floating water.
- **Option D (Ships)**: Correct. Plimsoll lines are universally painted on the hulls of commercial merchant ships.`
  },
  {
    id: "MH-9-SCIT-2-2.1-OSC-060",
    text: "The volume of an air bubble increases as it rises from the deep bottom to the surface of a water tank. Which physical laws explain this phenomenon?",
    options: [
      "Only the density change of water as the bubble rises",
      "The liquid hydrostatic pressure decreases as the depth decreases, and at constant temperature volume is inversely proportional to pressure (Boyle's Law)",
      "The surface tension of water doubles near the top",
      "The gravitational acceleration drops to zero at the surface"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. **Hydrostatic Pressure**: Total pressure at depth \(h\) below water surface of atmospheric pressure \(P_0\) is:
\\[
P = P_0 + h \\rho g
\\]
As the bubble ascends towards the surface, the depth of the liquid column above it \(h \\rightarrow 0\), so hydrostatic pressure **decreases**.
2. **Boyle's Law**: Assuming constant water temperature \(T\):
\\[
P \\cdot V = \\text{constant} \\implies V \\propto \\frac{1}{P}
\\]
As external pressure \(P\) drops, the air inside the bubble expands, causing its volume \(V\) to **increase**.

### 2. Physical Context & Practical Illustration:
Deep-sea scuba divers observe the same phenomenon with exhaust bubbles, which start tiny at depth and expand significantly as they float towards the surface. Divers must breathe out continuously when ascending to prevent pulmonary barotrauma from expanding air in their lungs.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Density change of water)**: Incorrect. Water is practically incompressible; its density is nearly uniform throughout the tank.
- **Option B (Hydrostatic pressure decrease + Boyle's Law)**: Correct. Decreasing depth decreases pressure, causing inversely proportional volume expansion.
- **Option C (Surface tension doubles)**: Incorrect. Surface tension is constant at uniform temperature.
- **Option D (Gravity drops to zero)**: Incorrect. Gravitational acceleration \(g\) is identical throughout the tank depth.`
  }
];
