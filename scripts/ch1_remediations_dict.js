// scripts/ch1_remediations_dict.js
// Custom handcrafted gold-standard enhancements for all flagged and flawed questions in Chapter 1 (Laws of Motion)

module.exports = {
  // Q26
  "MH-9-SCIT-1-1.1-OSC-026": {
    text: "What is the standard SI unit of acceleration?",
    options: [
      "\\(\\text{m/s}\\)",
      "\\(\\text{m}\\cdot\\text{s}\\)",
      "\\(\\text{m/s}^2\\)",
      "\\(\\text{kg}\\cdot\\text{m/s}\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is defined as the time rate of change of velocity:
\\[
a = \\frac{\\Delta v}{\\Delta t}
\\]
In SI base units:
\\[
[a] = \\frac{\\text{Velocity}}{\\text{Time}} = \\frac{\\text{m/s}}{\\text{s}} = \\frac{\\text{m}}{\\text{s}^2} = \\text{m/s}^2
\\]

### 2. Physical Context & Practical Illustration:
An acceleration of \\(1\\text{ m/s}^2\\) means the object's velocity increases by \\(1\\text{ m/s}\\) during every second of elapsed time. For example, freely falling objects accelerate downward at approximately \\(9.8\\text{ m/s}^2\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(\\text{m/s}\\))**: Incorrect. This is the SI unit of speed or velocity.
- **Option B (\\(\\text{m}\\cdot\\text{s}\\))**: Incorrect. Not a standard physical unit in basic kinematics.
- **Option C (\\(\\text{m/s}^2\\))**: Correct. Standard SI unit of acceleration.
- **Option D (\\(\\text{kg}\\cdot\\text{m/s}\\))**: Incorrect. SI unit of linear momentum.`
  },

  // Q27
  "MH-9-SCIT-1-1.1-OSC-027": {
    text: "An object moving along a straight-line path with constant speed has:",
    options: [
      "A non-zero net external force acting in the direction of motion",
      "Zero acceleration",
      "Constantly increasing linear momentum",
      "A continuously changing velocity vector"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Velocity is a vector having both magnitude (speed) and direction:
\\[
\\vec{v} = v \\hat{u}
\\]
If both the speed \\(v\\) and the straight-line direction \\(\\hat{u}\\) remain constant:
\\[
\\frac{d\\vec{v}}{dt} = 0 \\implies \\vec{a} = 0\\text{ m/s}^2
\\]
By Newton's first law, the net external force acting on the object is also zero (\\(\\vec{F}_{\\text{net}} = m\\vec{a} = 0\\)).

### 2. Physical Context & Practical Illustration:
A car cruising on cruise control on a perfectly straight, flat highway at \\(80\\text{ km/h}\\) has balanced forward engine thrust and opposing friction/drag forces, resulting in zero net force and zero acceleration.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. A net force would cause non-zero acceleration, changing speed.
- **Option B (Zero acceleration)**: Correct. Constant speed in a fixed straight direction means velocity does not change, so \\(a = 0\\).
- **Option C**: Incorrect. Momentum \\(p = mv\\) remains constant if velocity and mass are constant.
- **Option D**: Incorrect. Velocity vector is strictly constant.`
  },

  // Q31
  "MH-9-SCIT-1-1.1-OSC-031": {
    text: "If an object's mass decreases continuously while a constant net force is applied to it, its acceleration will:",
    options: [
      "Decrease linearly",
      "Increase continuously",
      "Remain strictly constant",
      "Drop instantly to zero"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's second law of motion:
\\[
F = ma \\implies a = \\frac{F}{m}
\\]
For a constant force \\(F\\), acceleration is inversely proportional to mass:
\\[
a \\propto \\frac{1}{m}
\\]
As mass \\(m\\) decreases, the denominator becomes smaller, which causes the acceleration \\(a\\) to **increase**.

### 2. Physical Context & Practical Illustration:
This occurs in rocket propulsion. As a rocket burns and ejects massive amounts of propellants, its total mass drops rapidly. Under constant engine thrust, the rocket accelerates faster and faster as it ascends.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Decreases)**: Incorrect. Inversely proportional; decreasing mass increases acceleration.
- **Option B (Increases)**: Correct. \\(a = F/m\\); decreasing mass leads to higher acceleration.
- **Option C (Remains constant)**: Incorrect. Acceleration only remains constant if mass is constant.
- **Option D (Drops to zero)**: Incorrect. A non-zero force always produces non-zero acceleration.`
  },

  // Q34
  "MH-9-SCIT-1-1.1-OSC-034": {
    text: "A fireworks rocket ejects \\(0.05\\text{ kg}\\) of exhaust gases per second at an exhaust velocity of \\(400\\text{ m/s}\\). What is the accelerating thrust force exerted on the rocket?",
    options: [
      "\\(20\\text{ dynes}\\)",
      "\\(20\\text{ N}\\)",
      "\\(200\\text{ N}\\)",
      "\\(2\\text{ N}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's second law in terms of momentum rate of change:
\\[
F_{\\text{thrust}} = \\frac{dp}{dt} = v_{\\text{rel}} \\frac{dm}{dt}
\\]
Given data:
- Rate of gas ejection \\(\\frac{dm}{dt} = 0.05\\text{ kg/s}\\)
- Exhaust velocity \\(v_{\\text{rel}} = 400\\text{ m/s}\\)

Calculating thrust:
\\[
F = 400\\text{ m/s} \\times 0.05\\text{ kg/s} = 20\\text{ kg}\\cdot\\text{m/s}^2 = 20\\text{ N}
\\]

### 2. Physical Context & Practical Illustration:
By Newton's third law, the backward momentum imparted to the escaping high-speed exhaust gas creates an equal and opposite forward reaction force (thrust) that accelerates the rocket upwards.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (20 dynes)**: Incorrect. Dyne is CGS (\\(1\\text{ N} = 10^5\\text{ dynes}\\)); the force here is \\(20\\text{ Newtons}\\).
- **Option B (20 N)**: Correct. \\(400 \\times 0.05 = 20\\text{ N}\\).
- **Option C (200 N)**: Incorrect. Arithmetic error by a factor of 10.
- **Option D (2 N)**: Incorrect. Arithmetic error by a factor of 0.1.`
  },

  // Q42
  "MH-9-SCIT-1-1.1-OSC-042": {
    text: "If the velocity of a body does not change with the passage of time, what is its acceleration?",
    options: [
      "Zero (\\(0\\text{ m/s}^2\\))",
      "Infinite",
      "Unity (\\(1\\text{ m/s}^2\\))",
      "Dependent on the mass of the body"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is the rate of change of velocity:
\\[
a = \\frac{\\Delta v}{\\Delta t} = \\frac{v_2 - v_1}{t}
\\]
When velocity does not change with time, \\(v_2 = v_1 \\implies \\Delta v = 0\\).
Therefore:
\\[
a = \\frac{0}{t} = 0\\text{ m/s}^2
\\]

### 2. Physical Context & Practical Illustration:
A train moving along a straight track at a steady speed of \\(60\\text{ km/h}\\) has zero acceleration. Passengers do not feel any jerks or leaning forces because \\(F = ma = 0\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Zero)**: Correct. Constant velocity implies strictly zero rate of change, so acceleration is zero.
- **Option B (Infinite)**: Incorrect. Infinite acceleration would require instantaneous velocity changes.
- **Option C (Unity)**: Incorrect. Acceleration is zero, not \\(1\\text{ m/s}^2\\).
- **Option D**: Incorrect. Zero velocity change gives zero acceleration regardless of mass.`
  },

  // Q50
  "MH-9-SCIT-1-1.1-OSC-050": {
    text: "When a lubricating grease is applied between two rubbing machine surfaces, which opposing force is significantly reduced?",
    options: [
      "Gravitational force",
      "Electrostatic attraction",
      "Frictional force",
      "Magnetic force"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Friction arises from microscopic interlocking of surface irregularities (asperities) and adhesive molecular bonding between contacting surfaces. Applying grease or oil forms a thin fluid film that separates the solid surfaces, replacing dry solid-solid friction with much lower fluid viscosity drag:
\\[
f_{\\text{lubricated}} \\ll f_{\\text{dry}}
\\]

### 2. Physical Context & Practical Illustration:
Greasing bicycle chains, wheel bearings, and automotive gears minimizes wear and tear, reduces heat dissipation, and boosts mechanical efficiency.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Gravitational force)**: Incorrect. Lubrication does not affect mass or gravitational pull.
- **Option B (Electrostatic)**: Incorrect. Minor compared to macroscopic friction.
- **Option C (Frictional force)**: Correct. Lubrication's primary function is reducing friction and wear.
- **Option D (Magnetic force)**: Incorrect. Machine friction is mechanical, not magnetic.`
  },

  // Q51
  "MH-9-SCIT-1-1.1-OSC-051": {
    text: "In a velocity-time graph, what physical quantity is represented by the area under the curve between two time intervals?",
    options: [
      "Total elapsed time",
      "Magnitude of displacement (or distance)",
      "Instantaneous acceleration",
      "Average rate of retardation"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Velocity is the derivative of displacement:
\\[
v = \\frac{ds}{dt} \\implies ds = v \\, dt
\\]
Integrating both sides between times \\(t_1\\) and \\(t_2\\):
\\[
s = \\int_{t_1}^{t_2} v(t) \\, dt
\\]
In geometry, the definite integral \\(\\int v \\, dt\\) equals the **area under the curve** of the velocity-time graph.
Checking units:
\\[
[\\text{Area}] = \\text{Velocity} \\times \\text{Time} = \\left(\\frac{\\text{m}}{\\text{s}}\\right) \\times \\text{s} = \\text{meters (m)}
\\]

### 2. Physical Context & Practical Illustration:
To find how far an accelerating car travels between \\(t = 0\\) and \\(t = 10\\text{ s}\\), one simply computes the area of the shape (rectangle, triangle, or trapezium) formed under the velocity curve.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Time)**: Incorrect. Time is the horizontal axis itself.
- **Option B (Displacement)**: Correct. Area under \\(v-t\\) graph represents displacement.
- **Option C (Acceleration)**: Incorrect. Acceleration is represented by the **slope** of the \\(v-t\\) graph, not the area.
- **Option D (Retardation)**: Incorrect. Negative slope gives retardation.`
  },

  // Q56
  "MH-9-SCIT-1-1.1-OSC-056": {
    text: "Which of the following physical quantities represents the product of a constant force and the duration of time for which it acts (\\(F \\times \\Delta t\\))?",
    options: [
      "Linear momentum",
      "Impulse of force",
      "Mechanical power",
      "Acceleration"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The impulse \\(J\\) of a force is defined as the integral of force over time:
\\[
J = F \\Delta t
\\]
By Newton's second law (\\(F = \\frac{\\Delta p}{\\Delta t}\\)):
\\[
J = F \\Delta t = \\Delta p = m(v - u)
\\]
This is the **Impulse-Momentum Theorem**: the impulse delivered to a body equals the total change in its linear momentum. Its SI unit is \\(\\text{N}\\cdot\\text{s}\\) or \\(\\text{kg}\\cdot\\text{m/s}\\).

### 2. Physical Context & Practical Illustration:
A cricketer pulls his hands backward when catching a fast cricket ball to increase the impact time \\(\\Delta t\\). By extending time, the required stopping force \\(F = \\frac{J}{\\Delta t}\\) is drastically reduced, preventing hand injury.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Linear momentum)**: Incorrect. Momentum is \\(p = mv\\); impulse is the *change* in momentum.
- **Option B (Impulse of force)**: Correct. \\(J = F \\Delta t\\) is by definition the impulse.
- **Option C (Mechanical power)**: Incorrect. Power is work divided by time (\\(W/t\\)).
- **Option D (Acceleration)**: Incorrect. Acceleration is \\(F/m\\).`
  },

  // Q59
  "MH-9-SCIT-1-1.1-OSC-059": {
    text: "A velocity-time graph shows a downward-sloping straight line that intersects the time axis. What type of motion does this graph describe?",
    options: [
      "Uniform positive acceleration",
      "Uniform velocity with zero acceleration",
      "Uniform deceleration (retardation)",
      "Non-uniform variable acceleration"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The slope of a velocity-time graph represents acceleration:
\\[
\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = a
\\]
When the graph is a downward-sloping straight line:
1. The line is straight \\(\\implies\\) slope is constant (uniform).
2. The line slopes downwards \\(\\implies\\) slope is negative (\\(a < 0\\)).
A constant negative acceleration is known as **uniform deceleration** or **uniform retardation**.

### 2. Physical Context & Practical Illustration:
When a driver applies steady, constant brakes on a car, the vehicle slows down smoothly from \\(60\\text{ km/h}\\) to \\(0\\text{ km/h}\\) with a straight downward \\(v-t\\) line.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Positive acceleration)**: Incorrect. Downward slope means velocity is decreasing, not increasing.
- **Option B (Uniform velocity)**: Incorrect. Uniform velocity produces a horizontal line parallel to time axis.
- **Option C (Uniform deceleration)**: Correct. Constant negative slope represents uniform retardation.
- **Option D (Non-uniform)**: Incorrect. A straight line has constant slope; a curve would indicate non-uniform acceleration.`
  },

  // Q62
  "MH-9-SCIT-1-1.1-OSC-062": {
    text: "A ball is rolled horizontally with an initial velocity of \\(12\\text{ m/s}\\). If it rolls to a complete stop in \\(36\\text{ seconds}\\) due to friction, what is its acceleration?",
    options: [
      "\\(-0.33\\text{ m/s}^2\\)",
      "\\(+0.33\\text{ m/s}^2\\)",
      "\\(-3.3\\text{ m/s}^2\\)",
      "\\(-0.5\\text{ m/s}^2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Use the first kinematic equation:
\\[
v = u + at \\implies a = \\frac{v - u}{t}
\\]
Given data:
- Initial velocity \\(u = 12\\text{ m/s}\\)
- Final velocity \\(v = 0\\text{ m/s}\\) (comes to stop)
- Time interval \\(t = 36\\text{ s}\\)

Substitute the values:
\\[
a = \\frac{0 - 12}{36} = -\\frac{12}{36} = -\\frac{1}{3} \\approx -0.33\\text{ m/s}^2
\\]
The negative sign confirms that the ball is decelerating.

### 2. Physical Context & Practical Illustration:
Friction between the ball and floor acts opposite to the direction of motion, exerting a constant resistive force that removes speed at the rate of \\(0.33\\text{ m/s}\\) every second.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(-0.33\\text{ m/s}^2\\))**: Correct. \\(-12 / 36 = -0.33\\text{ m/s}^2\\).
- **Option B (\\(+0.33\\text{ m/s}^2\\))**: Incorrect. Omission of negative sign; positive acceleration would speed up the ball.
- **Option C (\\(-3.3\\text{ m/s}^2\\))**: Incorrect. Decimal place error by a factor of 10.
- **Option D (\\(-0.5\\text{ m/s}^2\\))**: Incorrect. Calculation error.`
  },

  // Q63
  "MH-9-SCIT-1-1.1-OSC-063": {
    text: "Whenever an object experiences a change in either the magnitude or the direction of its velocity, the object is said to be:",
    options: [
      "At rest",
      "Moving with uniform inertia",
      "Accelerating (undergoing acceleration)",
      "Maintaining zero net force"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By definition, acceleration is the rate of change of the velocity vector:
\\[
\\vec{a} = \\frac{d\\vec{v}}{dt}
\\]
Because velocity \\(\\vec{v}\\) has both magnitude (speed) and direction:
1. Changing speed alone creates tangential acceleration.
2. Changing direction alone creates radial (centripetal) acceleration.
3. Changing both speed and direction creates net acceleration.
In all three cases, \\(\\frac{d\\vec{v}}{dt} \\neq 0\\), so the object is **accelerating**.

### 2. Physical Context & Practical Illustration:
A car turning around a circular roundabout at a steady speed of \\(30\\text{ km/h}\\) is accelerating continuously towards the center of the circle, because its direction of travel changes at every single instant.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (At rest)**: Incorrect. Changing velocity indicates active motion.
- **Option B (Uniform inertia)**: Incorrect. Inertia is mass, not an acceleration state.
- **Option C (Accelerating)**: Correct. Any change in velocity vector constitutes acceleration.
- **Option D (Zero net force)**: Incorrect. By \\(F = ma\\), non-zero acceleration requires non-zero net force.`
  },

  // Q69
  "MH-9-SCIT-1-1.1-OSC-069": {
    text: "What is the magnitude of acceleration of a particle executing simple harmonic motion (SHM) as it passes through its equilibrium (mean) position?",
    options: [
      "Maximum",
      "Zero",
      "Infinite",
      "Equal to its initial displacement"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In simple harmonic motion, the restoring acceleration is directly proportional to displacement from the mean position:
\\[
a = -\\omega^2 x
\\]
where \\(\\omega\\) is angular frequency and \\(x\\) is displacement from equilibrium.
At the equilibrium (mean) position, the displacement is zero:
\\[
x = 0 \\implies a = -\\omega^2(0) = 0\\text{ m/s}^2
\\]
Thus, the acceleration is **zero** at the mean position (while velocity is maximum).

### 2. Physical Context & Practical Illustration:
In a swinging pendulum bob, as it passes through the lowest vertical center point, the restoring tangential force is zero, meaning restoring acceleration momentarily vanishes.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Maximum)**: Incorrect. Acceleration is maximum at the *extreme* positions (\\(x = \\pm A\\)), not at the mean position.
- **Option B (Zero)**: Correct. Displacement \\(x = 0 \\implies a = 0\\).
- **Option C (Infinite)**: Incorrect. Acceleration in SHM is finite and bounded.
- **Option D**: Incorrect. Incompatible dimensional units.`
  },

  // Q70
  "MH-9-SCIT-1-1.1-OSC-070": {
    text: "An airplane accelerates uniformly from rest along a runway of length \\(5000\\text{ m}\\) and achieves a take-off speed of \\(1800\\text{ km/h}\\). What is its uniform acceleration?",
    options: [
      "\\(25\\text{ m/s}^2\\)",
      "\\(250\\text{ m/s}^2\\)",
      "\\(2.5\\text{ m/s}^2\\)",
      "\\(50\\text{ m/s}^2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
First, convert the take-off speed from \\(\\text{km/h}\\) into \\(\\text{m/s}\\):
\\[
v = 1800\\text{ km/h} = 1800 \\times \\frac{5}{18}\\text{ m/s} = 100 \\times 5 = 500\\text{ m/s}
\\]
Initial velocity from rest \\(u = 0\\text{ m/s}\\).
Runway displacement \\(s = 5000\\text{ m}\\).
Using the third kinematic equation:
\\[
v^2 = u^2 + 2as \\implies (500)^2 = 0^2 + 2a(5000)
\\]
\\[
250,000 = 10,000 \\, a \\implies a = \\frac{250,000}{10,000} = 25\\text{ m/s}^2
\\]

### 2. Physical Context & Practical Illustration:
Achieving \\(500\\text{ m/s}\\) (Mach 1.5, supersonic speed) along a \\(5\\text{ km}\\) runway requires sustained high acceleration of \\(25\\text{ m/s}^2\\) (approximately \\(2.55\\,g\\)), typical of high-performance experimental aircraft or rocket sleds.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(25\\text{ m/s}^2\\))**: Correct. Exact computation: \\(a = \\frac{500^2}{2 \\times 5000} = 25\\text{ m/s}^2\\).
- **Option B (\\(250\\text{ m/s}^2\\))**: Incorrect. Factor of 10 error from forgetting to square 500 properly or dividing by 1,000.
- **Option C (\\(2.5\\text{ m/s}^2\\))**: Incorrect. Decimal place error.
- **Option D (\\(50\\text{ m/s}^2\\))**: Incorrect. Forgets the factor of 2 in \\(2as\\).`
  },

  // Q71
  "MH-9-SCIT-1-1.1-OSC-071": {
    text: "An object travels \\(20\\text{ m}\\) in \\(5\\text{ seconds}\\) and then travels another \\(20\\text{ m}\\) in \\(4\\text{ seconds}\\). What is the average speed of the object?",
    options: [
      "\\(4.0\\text{ m/s}\\)",
      "\\(4.44\\text{ m/s}\\)",
      "\\(4.5\\text{ m/s}\\)",
      "\\(5.0\\text{ m/s}\\)"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Average speed is defined as the total distance traveled divided by the total time taken:
\\[
v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{s_1 + s_2}{t_1 + t_2}
\\]
Given:
- \\(s_1 = 20\\text{ m}, \\quad t_1 = 5\\text{ s}\\)
- \\(s_2 = 20\\text{ m}, \\quad t_2 = 4\\text{ s}\\)

Substitute the values:
\\[
v_{\\text{avg}} = \\frac{20 + 20}{5 + 4} = \\frac{40\\text{ m}}{9\\text{ s}} \\approx 4.44\\text{ m/s}
\\]

### 2. Physical Context & Practical Illustration:
Note that average speed is NOT the simple arithmetic average of the two speeds:
\\(v_1 = 20/5 = 4\\text{ m/s}\\), \\(v_2 = 20/4 = 5\\text{ m/s}\\).
The simple average \\(\\frac{4+5}{2} = 4.5\\text{ m/s}\\) is incorrect because the object spends more time traveling at the slower speed. Total distance over total time correctly yields \\(4.44\\text{ m/s}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (4.0 m/s)**: Incorrect. This is only the speed of the first interval.
- **Option B (4.44 m/s)**: Correct. Exact computation: \\(40 / 9 = 4.44\\text{ m/s}\\).
- **Option C (4.5 m/s)**: Incorrect. Common student misconception of taking arithmetic mean of speeds \\((4+5)/2\\).
- **Option D (5.0 m/s)**: Incorrect. Speed of second interval only.`
  },

  // Q72
  "MH-9-SCIT-1-1.1-OSC-072": {
    text: "Why are passengers required to wear safety seatbelts in a moving motor car?",
    options: [
      "To prevent passengers from being thrown forward due to inertia of motion during sudden braking",
      "To reduce the gravitational force acting on passengers",
      "To eliminate all friction between passengers and their seats",
      "To increase the vehicle's engine horsepower"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
According to **Newton's First Law of Motion (Law of Inertia)**, a body in motion continues in motion with uniform velocity unless acted upon by an external net force.
When a moving car brakes abruptly:
1. The brakes apply an external stopping force to the car chassis.
2. The passengers' upper bodies, due to **inertia of motion**, tend to maintain their forward velocity.
3. Seatbelts provide the necessary backward external restraining force to safely decelerate passengers along with the vehicle.

### 2. Physical Context & Practical Illustration:
Without a seatbelt, the passenger's torso continues moving forward at the pre-braking speed until striking the steering wheel, dashboard, or windshield, causing severe traumatic injury.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Inertia of motion)**: Correct. Counteracts forward inertia during sudden braking.
- **Option B (Reduce gravity)**: Incorrect. Seatbelts do not alter Earth's gravitational pull.
- **Option C (Eliminate friction)**: Incorrect. Seatbelts do not eliminate seat friction.
- **Option D (Engine power)**: Incorrect. Seatbelts are purely passive safety restraints.`
  },

  // Q73
  "MH-9-SCIT-1-1.1-OSC-073": {
    text: "A force \\(F_1\\) accelerates a mass of \\(4\\text{ kg}\\) at \\(7\\text{ m/s}^2\\), while a force \\(F_2\\) accelerates a mass of \\(8\\text{ kg}\\) at \\(5\\text{ m/s}^2\\). Which force has a greater magnitude?",
    options: [
      "Force \\(F_1\\) is greater than \\(F_2\\)",
      "Force \\(F_2\\) is greater than \\(F_1\\)",
      "Both forces are equal in magnitude",
      "Neither force can be determined without knowing displacement"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's second law:
\\[
F = m \\times a
\\]
Compute each force:
- For first mass:
\\[
F_1 = 4\\text{ kg} \\times 7\\text{ m/s}^2 = 28\\text{ N}
\\]
- For second mass:
\\[
F_2 = 8\\text{ kg} \\times 5\\text{ m/s}^2 = 40\\text{ N}
\\]
Comparing the two forces:
\\[
40\\text{ N} > 28\\text{ N} \\implies F_2 > F_1
\\]
Therefore, force \\(F_2\\) applied on the \\(8\\text{ kg}\\) mass is greater.

### 2. Physical Context & Practical Illustration:
Although the \\(4\\text{ kg}\\) mass experiences a higher acceleration (\\(7\\text{ m/s}^2\\) vs \\(5\\text{ m/s}^2\\)), the \\(8\\text{ kg}\\) mass has twice the inertia, requiring a larger total force (\\(40\\text{ N}\\)) to produce its acceleration.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (F1 > F2)**: Incorrect. Confuses higher acceleration with higher force.
- **Option B (F2 > F1)**: Correct. \\(F_2 = 40\\text{ N}\\) while \\(F_1 = 28\\text{ N}\\).
- **Option C (Equal)**: Incorrect. \\(28\\text{ N} \\neq 40\\text{ N}\\).
- **Option D**: Incorrect. Force depends strictly on mass and acceleration (\\(F = ma\\)).`
  },

  // Q75
  "MH-9-SCIT-1-1.1-OSC-075": {
    text: "When an object moves along a curved path, which of the following physical quantities can remain constant throughout its motion?",
    options: [
      "Velocity vector",
      "Linear momentum vector",
      "Speed (magnitude of velocity)",
      "Centripetal acceleration vector"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A curved path implies that the direction of the tangent vector changes continuously at every point.
- **Velocity** (\\(\\vec{v}\\)) is a vector; since direction changes, velocity cannot be constant.
- **Linear momentum** (\\(\\vec{p} = m\\vec{v}\\)) changes direction and cannot be constant.
- **Centripetal acceleration** (\\(\\vec{a}_c\\)) points towards the center of curvature; its spatial heading rotates continuously, so its vector is not constant.
However, the **speed** \\(v = |\\vec{v}|\\) is a scalar magnitude representing distance per unit time and can easily remain strictly constant (as in uniform circular motion).

### 2. Physical Context & Practical Illustration:
A car driving around a circular test track at a steady \\(60\\text{ km/h}\\) maintains constant speed, but its velocity and momentum continuously rotate in space.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Velocity)**: Incorrect. Vector direction changes along any curve.
- **Option B (Linear momentum)**: Incorrect. Vector quantity, direction changes.
- **Option C (Speed)**: Correct. The scalar magnitude of velocity can remain uniform.
- **Option D (Centripetal acceleration vector)**: Incorrect. While its magnitude is constant, its direction rotates continuously.`
  },

  // Q76
  "MH-9-SCIT-1-1.1-OSC-076": {
    text: "According to Newton's First Law of Motion, when a rolling ball on the floor gradually slows down and comes to rest, what does this observation signify?",
    options: [
      "An external opposing force (friction) is acting on the rolling ball",
      "The ball naturally tends to stop because its internal inertia runs out",
      "The ball's gravitational mass increases as it rolls",
      "Zero net force is acting on the ball"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Newton's First Law states:
*Every body continues in its state of rest or of uniform motion in a straight line, unless compelled to change that state by applied external forces.*
If a body in motion decelerates (\\(a < 0\\)), Newton's second law dictates:
\\[
F_{\\text{net}} = ma \\neq 0
\\]
The slowing down of the ball is direct proof that an external opposing force—namely **rolling friction** and air resistance—is acting upon it.

### 2. Physical Context & Practical Illustration:
Before Galileo and Newton, ancient Aristotelian physics falsely believed that objects naturally seek rest. Newton proved that in a frictionless vacuum (such as deep interstellar space), a moving body will continue coasting forever without slowing down.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (External opposing force)**: Correct. Friction exerts an external retarding force that stops the ball.
- **Option B (Inertia runs out)**: Incorrect. Inertia is an intrinsic property of mass that never 'runs out'.
- **Option C (Mass increases)**: Incorrect. Mass remains constant.
- **Option D (Zero net force)**: Incorrect. Zero net force would mean constant velocity.`
  },

  // Q80
  "MH-9-SCIT-1-1.1-OSC-080": {
    text: "While sharpening a knife on a rotating grinding wheel, glowing sparks fly off tangentially from the rim. Which type of inertia causes this phenomenon?",
    options: [
      "Inertia of rest",
      "Inertia of motion",
      "Inertia of direction",
      "Thermal expansion inertia"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In circular motion, the velocity vector of any particle on the rim is directed **tangential** to the circumference:
\\[
\\vec{v} = \\vec{\\omega} \\times \\vec{r}
\\]
As long as the sparks (incandescent iron particles) are attached to the grinding wheel, centripetal forces constrain them to circular paths. The moment a spark separates from the wheel:
1. Centripetal force becomes zero (\\(F_c = 0\\)).
2. By Newton's First Law (Inertia of direction), the particle continues traveling in a straight line along its instantaneous velocity vector—which is tangential to the wheel.

### 2. Physical Context & Practical Illustration:
Similarly, mud flying off rotating bicycle tires or water droplets thrown off a spinning umbrella fly out tangentially due to inertia of direction.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Inertia of rest)**: Incorrect. The sparks were already in rapid rotation.
- **Option B (Inertia of motion)**: Incorrect. While speed is maintained, the specific straight-line tangential path illustrates preservation of direction.
- **Option C (Inertia of direction)**: Correct. Tendency of a body to maintain its straight-line directional heading.
- **Option D**: Incorrect. Not a recognized mechanical form of inertia.`
  },

  // Q84
  "MH-9-SCIT-1-1.1-OSC-084": {
    text: "In a displacement-time graph, two straight lines representing objects A and B have different positive slopes (\\(m_A \\neq m_B\\)). What does this indicate about their motions?",
    options: [
      "Both objects move with different constant velocities",
      "Both objects move with identical velocities",
      "Object A is accelerating while Object B is decelerating",
      "Both objects are stationary at different locations"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In a displacement-time (\\(s-t\\)) graph:
\\[
\\text{Slope } m = \\frac{\\Delta s}{\\Delta t} = \\text{Velocity } v
\\]
1. Since both plots are straight lines, their slopes are constant \\(\\implies\\) both objects move with uniform (constant) velocities.
2. Since their slopes are unequal (\\(m_A \\neq m_B\\)):
\\[
v_A \\neq v_B
\\]
The two objects are moving with **different constant velocities**.

### 2. Physical Context & Practical Illustration:
The object whose line has a steeper inclination angle to the time axis has a larger slope, meaning it covers more displacement in the same time interval and moves faster.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Different constant velocities)**: Correct. Straight lines mean constant velocity; different slopes mean different velocities.
- **Option B (Identical velocities)**: Incorrect. Identical velocities would produce parallel lines with equal slopes.
- **Option C (Accelerating/decelerating)**: Incorrect. Acceleration produces curved lines on a displacement-time graph.
- **Option D (Stationary)**: Incorrect. Stationary objects produce horizontal lines with zero slope.`
  },

  // Q86
  "MH-9-SCIT-1-1.1-OSC-086": {
    text: "A particle of mass \\(100\\text{ g}\\) moving in a straight line accelerates uniformly from \\(0\\text{ m/s}\\) to \\(40\\text{ m/s}\\) in \\(10\\text{ seconds}\\). What is the net force acting on the particle?",
    options: [
      "\\(0.4\\text{ N}\\)",
      "\\(4.0\\text{ N}\\)",
      "\\(40\\text{ N}\\)",
      "\\(0.04\\text{ N}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. Convert mass into SI units:
\\[
m = 100\\text{ g} = 0.1\\text{ kg}
\\]
2. Calculate uniform acceleration:
\\[
a = \\frac{v - u}{t} = \\frac{40 - 0}{10} = 4\\text{ m/s}^2
\\]
3. Calculate net force using Newton's second law:
\\[
F = ma = 0.1\\text{ kg} \\times 4\\text{ m/s}^2 = 0.4\\text{ N}
\\]

### 2. Physical Context & Practical Illustration:
A force of \\(0.4\\text{ Newtons}\\) is roughly equivalent to the weight of a small \\(40\\text{ g}\\) plum. When exerted continuously for 10 seconds on a \\(100\\text{ g}\\) toy car, it accelerates it up to \\(144\\text{ km/h}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (0.4 N)**: Correct. \\(F = 0.1 \\times 4 = 0.4\\text{ N}\\).
- **Option B (4.0 N)**: Incorrect. Fails to convert grams to kilograms (uses \\(m = 1\\text{ kg}\\)).
- **Option C (40 N)**: Incorrect. Multiplies velocity by mass without dividing by time.
- **Option D (0.04 N)**: Incorrect. Decimal error.`
  },

  // Q88
  "MH-9-SCIT-1-1.1-OSC-088": {
    text: "Which of the following physical quantities is a scalar quantity rather than a vector?",
    options: [
      "Displacement",
      "Hydrostatic pressure",
      "Acceleration",
      "Linear momentum"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Pressure is defined as normal force per unit surface area:
\\[
P = \\frac{F_{\\perp}}{A}
\\]
Although force is a vector, pressure acts equally in all directions within a fluid at a given depth (Pascal's Principle). Because it does not possess a unique spatial direction, **pressure is a scalar quantity**.
In contrast, displacement, acceleration, and momentum are all vectors.

### 2. Physical Context & Practical Illustration:
When a submarine is submerged, water pressure pushes inward perpendicular to every point on its curved hull. Pressure has magnitude, but no single fixed directional vector.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Displacement)**: Vector quantity (magnitude + direction).
- **Option B (Pressure)**: Correct. Pressure is an isotropic scalar quantity.
- **Option C (Acceleration)**: Vector quantity.
- **Option D (Momentum)**: Vector quantity (\\(\\vec{p} = m\\vec{v}\\)).`
  },

  // Q92
  "MH-9-SCIT-1-1.1-OSC-092": {
    text: "In a laboratory spring balance, how is the elongation (extension) of the spring related to the suspended weight of the object?",
    options: [
      "Extension is directly proportional to the suspended weight (Hooke's Law)",
      "Extension is inversely proportional to the weight",
      "Extension is proportional to the square of the weight",
      "Extension is independent of the suspended weight"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Within the elastic limit of a spring, **Hooke's Law** states that the restoring force is directly proportional to elongation:
\\[
F_s = k \\cdot x
\\]
When a mass \\(m\\) hangs in static equilibrium:
\\[
\\text{Weight } W = mg = k \\cdot x \\implies x = \\frac{mg}{k} \\propto W
\\]
The extension \\(x\\) is **directly proportional to the weight** of the suspended body.

### 2. Physical Context & Practical Illustration:
Because elongation scales linearly with weight, the calibrated scale on a spring balance features evenly spaced graduation marks (e.g. \\(1\\text{ cm}\\) per \\(100\\text{ g-wt}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Directly proportional)**: Correct. Follows Hooke's Law \\(W = kx\\).
- **Option B (Inversely proportional)**: Incorrect. Heavier weights stretch the spring more, not less.
- **Option C (Square of weight)**: Incorrect. Quadratic scaling applies to elastic potential energy, not extension.
- **Option D (Independent)**: Incorrect. Extension is produced directly by the weight.`
  },

  // Q98
  "MH-9-SCIT-1-1.1-OSC-098": {
    text: "Which of the following physical quantities possesses both magnitude and a specific spatial direction?",
    options: [
      "Velocity",
      "Speed",
      "Distance",
      "Mass"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Physical quantities with both magnitude and direction that obey vector addition laws are **vectors**:
\\[
\\vec{v} = v \\hat{u}
\\]
**Velocity** is the vector rate of displacement with time.
Speed, distance, and mass have magnitude only and are scalars.

### 2. Physical Context & Practical Illustration:
Stating that an aircraft flies at \\(800\\text{ km/h}\\) specifies its speed. Adding the heading "North-East" specifies its velocity vector.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Velocity)**: Correct. Vector quantity possessing magnitude and direction.
- **Option B (Speed)**: Incorrect. Scalar magnitude of velocity.
- **Option C (Distance)**: Incorrect. Scalar total path length.
- **Option D (Mass)**: Incorrect. Scalar quantity of matter.`
  },

  // Q99
  "MH-9-SCIT-1-1.1-OSC-099": {
    text: "If the speed of a moving object of constant mass is doubled, which of the following physical quantities will also be doubled?",
    options: [
      "Linear momentum",
      "Kinetic energy",
      "Gravitational potential energy",
      "Centripetal acceleration for fixed radius"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Let the initial speed be \\(v\\) and new speed be \\(v' = 2v\\):
1. **Linear Momentum**:
\\[
p = mv \\implies p' = m(2v) = 2(mv) = 2p \\quad (\\text{Doubles})
\\]
2. **Kinetic Energy**:
\\[
E_k = \\frac{1}{2}mv^2 \\implies E_k' = \\frac{1}{2}m(2v)^2 = 4E_k \\quad (\\text{Quadruples})
\\]
Therefore, linear momentum doubles linearly with speed.

### 2. Physical Context & Practical Illustration:
Momentum scales linearly (\\(p \\propto v\\)), while kinetic energy scales quadratically (\\(E_k \\propto v^2\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Linear momentum)**: Correct. \\(p = mv\\); doubling \\(v\\) doubles \\(p\\).
- **Option B (Kinetic energy)**: Incorrect. \\(E_k \\propto v^2\\); quadruples.
- **Option C (Potential energy)**: Incorrect. Depends on height, not horizontal speed.
- **Option D (Centripetal acceleration)**: Incorrect. \\(a_c = v^2/r\\); quadruples.`
  },

  // Q100
  "MH-9-SCIT-1-1.1-OSC-100": {
    text: "When a graph plotted between two physical quantities \\(y\\) and \\(x\\) yields a straight line passing through the origin, what does this mathematically indicate?",
    options: [
      "Both quantities are constant",
      "Quantity \\(y\\) is inversely proportional to \\(x\\)",
      "Quantity \\(y\\) is directly proportional to \\(x\\) (\\(y \\propto x\\))",
      "Quantity \\(y\\) is completely independent of \\(x\\)"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The equation of a straight line passing through the origin is:
\\[
y = m x
\\]
where \\(m = \\frac{\\Delta y}{\\Delta x}\\) is the constant slope.
This is the foundational mathematical definition of **direct proportionality**:
\\[
y \\propto x
\\]
Doubling \\(x\\) produces a proportional doubling of \\(y\\).

### 2. Physical Context & Practical Illustration:
Common examples in physics include:
- Distance vs. time at constant speed: \\(s = vt\\)
- Force vs. acceleration at constant mass: \\(F = ma\\)
- Voltage vs. current in an ohmic resistor: \\(V = IR\\)

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. A straight line passing through origin has variables changing together.
- **Option B (Inversely proportional)**: Incorrect. Inverse proportionality produces a rectangular hyperbola (\\(y \\propto 1/x\\)).
- **Option C (Directly proportional)**: Correct. Standard linear relation \\(y = mx\\).
- **Option D (Independent)**: Incorrect. Would produce a flat horizontal line.`
  },

  // Q101
  "MH-9-SCIT-1-1.1-OSC-101": {
    text: "Car A moves North at \\(60\\text{ km/h}\\), while Car B moves South on the same straight highway at \\(60\\text{ km/h}\\). What is the relative velocity of Car A with respect to Car B?",
    options: [
      "\\(0\\text{ km/h}\\)",
      "\\(120\\text{ km/h}\\) Northward",
      "\\(120\\text{ km/h}\\) Southward",
      "\\(60\\text{ km/h}\\) Northward"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Relative velocity of object A with respect to object B is:
\\[
\\vec{v}_{A/B} = \\vec{v}_A - \\vec{v}_B
\\]
Assigning North as the positive direction (\\(+\\hat{j}\\)) and South as negative (\\(-\\hat{j}\\)):
- \\(\\vec{v}_A = +60\\hat{j}\\text{ km/h}\\)
- \\(\\vec{v}_B = -60\\hat{j}\\text{ km/h}\\)

Calculating relative velocity:
\\[
\\vec{v}_{A/B} = (+60\\hat{j}) - (-60\\hat{j}) = 60\\hat{j} + 60\\hat{j} = +120\\hat{j}\\text{ km/h}
\\]
Thus, the relative velocity of Car A with respect to Car B is **\\(120\\text{ km/h}\\) Northward**.

### 2. Physical Context & Practical Illustration:
To passengers inside Car B looking out, Car A appears to approach and pass them at a combined speed of \\(120\\text{ km/h}\\), explaining why head-on traffic appears to move exceptionally fast.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (0 km/h)**: Incorrect. Relative velocity is zero only if both cars move in the *same* direction.
- **Option B (120 km/h Northward)**: Correct. \\(60 - (-60) = 120\\text{ km/h}\\) towards North.
- **Option C (120 km/h Southward)**: Incorrect. This is the relative velocity of Car B with respect to Car A.
- **Option D (60 km/h)**: Incorrect. Ignores the motion of observer B.`
  },

  // Q102
  "MH-9-SCIT-1-1.1-OSC-102": {
    text: "A person walks \\(2\\text{ m}\\) East and then \\(2\\text{ m}\\) South. What is the magnitude and direction of the net displacement vector?",
    options: [
      "\\(4\\text{ m}\\) South-East",
      "\\(2\\sqrt{2}\\text{ m}\\) (\\(\\approx 2.83\\text{ m}\\)) South-East",
      "\\(2\\text{ m}\\) South-East",
      "\\(4\\text{ m}\\) North-East"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Displacement is the vector from start to finish:
\\[
\\vec{s} = 2\\hat{i} - 2\\hat{j}
\\]
Since East and South are mutually perpendicular (\\(\\theta = 90^\\circ\\)):
\\[
|\\vec{s}| = \\sqrt{(2)^2 + (-2)^2} = \\sqrt{4 + 4} = \\sqrt{8} = 2\\sqrt{2}\\text{ m} \\approx 2.83\\text{ m}
\\]
Direction:
\\[
\\tan\\alpha = \\frac{\\text{South}}{\\text{East}} = \\frac{2}{2} = 1 \\implies \\alpha = 45^\\circ \\quad (\\text{South-East})
\\]

### 2. Physical Context & Practical Illustration:
Total distance traveled is a scalar sum (\\(2 + 2 = 4\\text{ m}\\)), but displacement is the straight-line shortcut across the hypotenuse of the right-angled triangle, which is \\(2\\sqrt{2}\\text{ m}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (4 m)**: Incorrect. Scalar distance path, not vector displacement.
- **Option B (\\(2\\sqrt{2}\\text{ m}\\) South-East)**: Correct. Calculated via Pythagorean theorem.
- **Option C (2 m)**: Incorrect. Less than each leg.
- **Option D (North-East)**: Incorrect. Person walked South, not North.`
  },

  // Q103
  "MH-9-SCIT-1-1.1-OSC-103": {
    text: "In a distance-time graph, what physical quantity is given by the slope of the curve?",
    options: [
      "Speed",
      "Acceleration",
      "Total distance",
      "Displacement"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The slope of a graph is the ratio of change in the vertical axis to change in the horizontal axis:
\\[
\\text{Slope} = \\frac{\\Delta y}{\\Delta x} = \\frac{\\Delta(\\text{Distance})}{\\Delta(\\text{Time})} = \\text{Speed}
\\]
Checking dimensions:
\\[
[\\text{Slope}] = \\frac{\\text{m}}{\\text{s}} = \\text{Speed (m/s)}
\\]

### 2. Physical Context & Practical Illustration:
A steeper slope means more distance covered per unit time, representing higher speed. A flat horizontal line has zero slope, representing an object at rest.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Speed)**: Correct. Slope of distance-time graph gives speed.
- **Option B (Acceleration)**: Incorrect. Acceleration is the slope of a velocity-time graph.
- **Option C (Total distance)**: Incorrect. Distance is read directly from vertical axis.
- **Option D (Displacement)**: Incorrect. Requires a displacement-time graph.`
  },

  // Q104
  "MH-9-SCIT-1-1.1-OSC-104": {
    text: "In a displacement-time graph, what physical quantity is given by the slope of the curve?",
    options: [
      "Velocity",
      "Speed",
      "Acceleration",
      "Force"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The slope of a displacement-time graph is:
\\[
\\text{Slope} = \\frac{\\Delta s}{\\Delta t} = \\text{Velocity } v
\\]
Because displacement is a vector, its slope can be positive (moving forward), negative (moving backward), or zero (at rest).

### 2. Physical Context & Practical Illustration:
If an athlete runs forward, turns around, and walks back, the \\(s-t\\) graph slope switches from positive to negative, indicating velocity vector reversal.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Velocity)**: Correct. Derivative of displacement with respect to time is velocity.
- **Option B (Speed)**: Incorrect. Speed is scalar; displacement slope gives signed velocity.
- **Option C (Acceleration)**: Incorrect. Second derivative or slope of velocity graph.
- **Option D (Force)**: Incorrect. Requires mass multiplication.`
  },

  // Q105
  "MH-9-SCIT-1-1.1-OSC-105": {
    text: "In a velocity-time graph, what physical quantity is determined by the slope of the curve?",
    options: [
      "Acceleration",
      "Displacement",
      "Speed",
      "Total travel time"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The slope of a velocity-time curve is:
\\[
\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = a
\\]
Checking units:
\\[
\\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2
\\]
The slope directly gives the **acceleration** of the moving object.

### 2. Physical Context & Practical Illustration:
A positive slope indicates acceleration (speeding up), a negative slope indicates retardation (braking), and a zero slope indicates constant velocity cruise.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Acceleration)**: Correct. Slope of \\(v-t\\) graph is acceleration.
- **Option B (Displacement)**: Incorrect. Displacement is given by the *area* under the \\(v-t\\) curve.
- **Option C (Speed)**: Incorrect. Read directly from the vertical axis.
- **Option D (Time)**: Incorrect. Read from horizontal axis.`
  },

  // Q106
  "MH-9-SCIT-1-1.1-OSC-106": {
    text: "In a velocity-time graph, a straight horizontal line parallel to the time axis indicates:",
    options: [
      "Uniform velocity (zero acceleration)",
      "Uniform non-zero acceleration",
      "Object remaining at rest at the origin",
      "Constant retardation"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A line parallel to the time axis has a constant vertical coordinate (\\(v = v_0 = \\text{constant}\\)):
\\[
\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = \\frac{0}{\\Delta t} = 0 \\implies a = 0
\\]
Therefore, the object moves with **uniform velocity and zero acceleration**.

### 2. Physical Context & Practical Illustration:
This describes an airplane at steady cruising altitude moving at constant airspeed without accelerating or braking.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Uniform velocity)**: Correct. Constant velocity with zero slope and zero acceleration.
- **Option B (Uniform acceleration)**: Incorrect. Would require an inclined straight line.
- **Option C (At rest)**: Incorrect. At rest is a line coinciding with \\(v = 0\\); here \\(v > 0\\).
- **Option D (Constant retardation)**: Incorrect. Would require downward sloping line.`
  },

  // Q107
  "MH-9-SCIT-1-1.1-OSC-107": {
    text: "In a velocity-time graph, what physical quantity is obtained by calculating the area enclosed between the curve and the time axis?",
    options: [
      "Magnitude of displacement",
      "Acceleration",
      "Force",
      "Rate of change of momentum"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The area under a \\(v-t\\) graph is the definite integral:
\\[
\\text{Area} = \\int v(t) \\, dt = \\Delta s
\\]
Dimensions:
\\[
[\\text{Area}] = \\text{Velocity} \\times \\text{Time} = \\frac{\\text{m}}{\\text{s}} \\times \\text{s} = \\text{meters (m)}
\\]
Thus, the enclosed area represents the **magnitude of displacement** (or distance for unidirectional motion).

### 2. Physical Context & Practical Illustration:
If an electric car moves at \\(20\\text{ m/s}\\) for \\(10\\text{ seconds}\\), the area of the rectangle is \\(20 \\times 10 = 200\\text{ m}\\), exactly the distance traveled.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Displacement)**: Correct. Integral of velocity over time yields displacement.
- **Option B (Acceleration)**: Incorrect. Acceleration is the slope, not the area.
- **Option C (Force)**: Incorrect. Requires mass multiplication.
- **Option D**: Incorrect. Rate of change of momentum is force.`
  },

  // Q108
  "MH-9-SCIT-1-1.1-OSC-108": {
    text: "A velocity-time graph shows an inclined straight line sloping downwards towards the right. What does this graph indicate?",
    options: [
      "Acceleration is positive and increasing",
      "Acceleration is uniform and negative (uniform retardation)",
      "Object is at rest",
      "Displacement is decreasing to zero"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The slope of a \\(v-t\\) line is:
\\[
m = \\frac{v_2 - v_1}{t_2 - t_1}
\\]
Since velocity decreases as time advances, \\(v_2 < v_1 \\implies m < 0\\).
Because the line is straight, the slope is constant:
\\[
a = \\text{constant} < 0
\\]
This represents **uniform retardation (negative acceleration)**.

### 2. Physical Context & Practical Illustration:
Applying steady brakes to bring a high-speed passenger train to a halt produces this exact downward sloping line.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A**: Incorrect. Slope is negative, not positive.
- **Option B (Uniform retardation)**: Correct. Straight downward line indicates constant negative acceleration.
- **Option C (At rest)**: Incorrect. Velocity is non-zero during the descent.
- **Option D**: Incorrect. Area is still positive, so displacement increases forward.`
  },

  // Q109
  "MH-9-SCIT-1-1.1-OSC-109": {
    text: "In a distance-time graph, a curve that bends upwards with increasing slope as time progresses indicates:",
    options: [
      "Uniform speed",
      "Increasing speed (positive acceleration)",
      "Decreasing speed (retardation)",
      "Object remaining at rest"
    ],
    correctAnswer: "B",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Speed is given by the instantaneous slope of the distance-time graph:
\\[
v = \\frac{ds}{dt}
\\]
When the curve bends upwards (concave upward), the tangent becomes steeper as time \\(t\\) increases:
\\[
\\frac{d^2 s}{dt^2} > 0 \\implies v \\uparrow
\\]
The object is traveling with **increasing speed (positive acceleration)**.

### 2. Physical Context & Practical Illustration:
A rocket launching from a launchpad starts slowly and gains speed rapidly, producing a distance-time graph that curves sharply upwards.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Uniform speed)**: Incorrect. Uniform speed produces a straight line, not a curve.
- **Option B (Increasing speed)**: Correct. Steeper slope over time signifies accelerating motion.
- **Option C (Decreasing speed)**: Incorrect. Decreasing speed curves downwards (concave downward, flattening out).
- **Option D (At rest)**: Incorrect. At rest is a flat horizontal line.`
  },

  // Q110
  "MH-9-SCIT-1-1.1-OSC-110": {
    text: "In a distance-time graph, a straight horizontal line parallel to the time axis indicates that:",
    options: [
      "The object is moving with uniform speed",
      "The object is moving with uniform acceleration",
      "The object is stationary (at rest)",
      "The object is moving with variable speed"
    ],
    correctAnswer: "C",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A line parallel to the time axis on a distance-time graph has a fixed distance coordinate \\(s(t) = s_0 = \\text{constant}\\).
The slope of this line is:
\\[
v = \\frac{ds}{dt} = 0\\text{ m/s}
\\]
Because the position does not change with time and velocity is zero, the object is **stationary (at rest)**.

### 2. Physical Context & Practical Illustration:
A parked car by the roadside has a constant distance from the observer, producing a horizontal line on a distance-time plot.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Uniform speed)**: Incorrect. Requires an inclined line with non-zero slope.
- **Option B (Uniform acceleration)**: Incorrect. Requires a parabolic upward curve.
- **Option C (Stationary / at rest)**: Correct. Zero slope means zero speed.
- **Option D (Variable speed)**: Incorrect. Requires changing slope.`
  },

  // Q111
  "MH-9-SCIT-1-1.1-OSC-111": {
    text: "A vehicle accelerates uniformly from rest to \\(16\\text{ m/s}\\) in \\(8\\text{ seconds}\\). What is the total distance traveled during this time?",
    options: [
      "\\(64\\text{ m}\\)",
      "\\(128\\text{ m}\\)",
      "\\(32\\text{ m}\\)",
      "\\(16\\text{ m}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Method 1 (Area under triangular \\(v-t\\) graph):
\\[
s = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 8\\text{ s} \\times 16\\text{ m/s} = 64\\text{ m}
\\]
Method 2 (Kinematic formula):
\\[
a = \\frac{16 - 0}{8} = 2\\text{ m/s}^2
\\]
\\[
s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2}(2)(8)^2 = 64\\text{ m}
\\]

### 2. Physical Context & Practical Illustration:
Average velocity is \\(\\frac{0 + 16}{2} = 8\\text{ m/s}\\). Over \\(8\\text{ seconds}\\), distance is \\(8\\text{ m/s} \\times 8\\text{ s} = 64\\text{ m}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (64 m)**: Correct. Exact computation: \\(\\frac{1}{2} \\times 8 \\times 16 = 64\\text{ m}\\).
- **Option B (128 m)**: Incorrect. Forgets the factor of \\(1/2\\) (\\(8 \\times 16 = 128\\)).
- **Option C (32 m)**: Incorrect. Calculation error.
- **Option D (16 m)**: Incorrect. Confuses speed with distance.`
  },

  // Q112
  "MH-9-SCIT-1-1.1-OSC-112": {
    text: "Can a velocity-time graph ever be a straight vertical line perpendicular to the time axis in classical mechanics?",
    options: [
      "No, because it would imply infinite acceleration and infinite displacement in zero time, which is physically impossible",
      "Yes, when an object is at rest",
      "Yes, during free fall under gravity",
      "Yes, when an object moves with uniform speed"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
A vertical line perpendicular to the time axis has \\(\\Delta t = 0\\).
The slope (acceleration) would be:
\\[
a = \\frac{\\Delta v}{\\Delta t} = \\frac{v_2 - v_1}{0} = \\infty
\\]
By Newton's second law, infinite acceleration would require an **infinite net force** (\\(F = m \\times \\infty = \\infty\\)), which violates physical reality. Furthermore, a single object cannot possess multiple velocities at the exact same instant of time.

### 2. Physical Context & Practical Illustration:
Every physical change in velocity requires a non-zero time interval, no matter how short (even in explosive collisions, \\(\\Delta t \\sim 10^{-3}\\text{ s}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Impossible)**: Correct. Physically impossible due to infinite acceleration and causality violation.
- **Option B (At rest)**: Incorrect. At rest is a horizontal line along \\(v = 0\\).
- **Option C (Free fall)**: Incorrect. Free fall has finite slope \\(g = 9.8\\text{ m/s}^2\\).
- **Option D**: Incorrect. Uniform speed is horizontal.`
  },

  // Q113
  "MH-9-SCIT-1-1.1-OSC-113": {
    text: "When a straight line on a velocity-time graph forms an acute angle \\(\\theta\\) (\\(0^\\circ < \\theta < 90^\\circ\\)) with the positive time axis, the acceleration is:",
    options: [
      "Positive (speed is increasing)",
      "Negative (speed is decreasing)",
      "Zero",
      "Infinite"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is given by the slope:
\\[
a = \\tan\\theta
\\]
For an acute angle \\(0^\\circ < \\theta < 90^\\circ\\):
\\[
\\tan\\theta > 0 \\implies a > 0
\\]
Thus, the acceleration is **positive**, meaning the velocity increases with time.

### 2. Physical Context & Practical Illustration:
A motorcycle accelerating away from a stoplight exhibits an upward sloping line with an acute inclination angle to the time axis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Positive)**: Correct. Acute angle \\(\\implies \\tan\\theta > 0 \\implies a > 0\\).
- **Option B (Negative)**: Incorrect. Negative acceleration corresponds to an obtuse angle (\\(\\theta > 90^\\circ\\)).
- **Option C (Zero)**: Incorrect. Zero acceleration corresponds to \\(\\theta = 0^\\circ\\).
- **Option D (Infinite)**: Incorrect. Corresponds to \\(\\theta = 90^\\circ\\).`
  },

  // Q118, Q119, Q120: Rebuilt into clear, self-contained kinematic problems
  "MH-9-SCIT-1-1.1-OSC-118": {
    text: "Three cyclists A, B, and C start from the same point and travel along a straight road with uniform speeds of \\(10\\text{ km/h}\\), \\(15\\text{ km/h}\\), and \\(20\\text{ km/h}\\) respectively. What is the time interval between the start of C and when C is \\(10\\text{ km}\\) ahead of A?",
    options: [
      "\\(1.0\\text{ hour}\\)",
      "\\(0.5\\text{ hours}\\)",
      "\\(2.0\\text{ hours}\\)",
      "\\(1.5\\text{ hours}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Relative speed of cyclist C with respect to cyclist A:
\\[
v_{\\text{rel}} = v_C - v_A = 20\\text{ km/h} - 10\\text{ km/h} = 10\\text{ km/h}
\\]
To gain a lead of \\(d = 10\\text{ km}\\):
\\[
t = \\frac{d}{v_{\\text{rel}}} = \\frac{10\\text{ km}}{10\\text{ km/h}} = 1.0\\text{ hour}
\\]

### 2. Physical Context & Practical Illustration:
After 1 hour:
- Cyclist C travels: \\(20\\text{ km}\\)
- Cyclist A travels: \\(10\\text{ km}\\)
Lead: \\(20 - 10 = 10\\text{ km}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (1.0 hour)**: Correct. \\(10 / (20 - 10) = 1.0\\text{ h}\\).
- **Option B (0.5 hours)**: Incorrect. In 0.5 h, lead is only 5 km.
- **Option C (2.0 hours)**: Incorrect. Lead would be 20 km.
- **Option D (1.5 hours)**: Incorrect. Calculation error.`
  },

  "MH-9-SCIT-1-1.1-OSC-119": {
    text: "A vehicle traveling at a constant speed of \\(72\\text{ km/h}\\) applies brakes and comes to rest in \\(10\\text{ seconds}\\). What distance does it cover during this braking period?",
    options: [
      "\\(100\\text{ m}\\)",
      "\\(200\\text{ m}\\)",
      "\\(50\\text{ m}\\)",
      "\\(360\\text{ m}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
1. Convert initial speed:
\\[
u = 72\\text{ km/h} = 72 \\times \\frac{5}{18} = 20\\text{ m/s}
\\]
2. Uniform acceleration:
\\[
a = \\frac{0 - 20}{10} = -2\\text{ m/s}^2
\\]
3. Distance traveled:
\\[
s = ut + \\frac{1}{2}at^2 = (20)(10) + \\frac{1}{2}(-2)(10)^2 = 200 - 100 = 100\\text{ m}
\\]

### 2. Physical Context & Practical Illustration:
This represents standard highway emergency stopping distance: at \\(72\\text{ km/h}\\), an emergency stop over 10 seconds requires \\(100\\text{ meters}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (100 m)**: Correct. \\(s = \\frac{u + v}{2} \\cdot t = \\frac{20}{2} \\times 10 = 100\\text{ m}\\).
- **Option B (200 m)**: Incorrect. Distance if it maintained full speed without braking.
- **Option C (50 m)**: Incorrect. Underestimates stopping distance.
- **Option D (360 m)**: Incorrect. Converted incorrectly.`
  },

  "MH-9-SCIT-1-1.1-OSC-120": {
    text: "A train \\(100\\text{ m}\\) long moving at a constant speed of \\(54\\text{ km/h}\\) crosses a railway bridge of length \\(400\\text{ m}\\). How much time does it take to cross the bridge completely?",
    options: [
      "\\(33.3\\text{ seconds}\\)",
      "\\(26.7\\text{ seconds}\\)",
      "\\(10\\text{ seconds}\\)",
      "\\(40\\text{ seconds}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Speed in \\(\\text{m/s}\\):
\\[
v = 54\\text{ km/h} = 54 \\times \\frac{5}{18} = 15\\text{ m/s}
\\]
For the train to completely cross the bridge, its front must enter and its rear must exit, covering total distance:
\\[
d = \\text{Length of bridge} + \\text{Length of train} = 400\\text{ m} + 100\\text{ m} = 500\\text{ m}
\\]
Time taken:
\\[
t = \\frac{d}{v} = \\frac{500\\text{ m}}{15\\text{ m/s}} = \\frac{100}{3} \\approx 33.33\\text{ seconds}
\\]

### 2. Physical Context & Practical Illustration:
Students often forget to add the train's own length to the bridge length. Because crossing is complete only when the last car clears the bridge, the total path length is \\(500\\text{ m}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (33.3 s)**: Correct. \\(500 / 15 = 33.33\\text{ s}\\).
- **Option B (26.7 s)**: Incorrect. Forgets train length (\\(400 / 15 = 26.67\\text{ s}\\)).
- **Option C (10 s)**: Incorrect. Calculation error.
- **Option D (40 s)**: Incorrect. Arbitrary estimate.`
  },

  // Q127
  "MH-9-SCIT-1-1.1-OSC-127": {
    text: "In a velocity-time graph, if the line is inclined at an obtuse angle (\\(\\theta > 90^\\circ\\)) to the positive time axis, it indicates that:",
    options: [
      "The object's speed is decreasing with time (retardation)",
      "The object's speed is increasing with time",
      "The object is moving with constant velocity",
      "The displacement is zero"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is given by:
\\[
a = \\text{slope} = \\tan\\theta
\\]
In trigonometry, for an obtuse angle \\(90^\\circ < \\theta < 180^\\circ\\):
\\[
\\tan\\theta < 0 \\implies a < 0
\\]
A negative slope indicates that velocity is decreasing as time progresses (**retardation**).

### 2. Physical Context & Practical Illustration:
When a cyclist applies brakes, the velocity drops from \\(10\\text{ m/s}\\) towards \\(0\\text{ m/s}\\), producing an obtuse inclination with the time axis.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Speed decreasing / retardation)**: Correct. Obtuse angle \\(\\implies \\tan\\theta < 0 \\implies a < 0\\).
- **Option B (Speed increasing)**: Incorrect. Would require an acute angle (\\(\\theta < 90^\\circ\\)).
- **Option C (Constant velocity)**: Incorrect. Requires \\(\\theta = 0^\\circ\\).
- **Option D**: Incorrect. Displacement is the area under the line.`
  },

  // Q131
  "MH-9-SCIT-1-1.1-OSC-131": {
    text: "What is the least count of a standard classroom circular or semi-circular geometric protractor?",
    options: [
      "\\(1^\\circ\\)",
      "\\(0.1^\\circ\\)",
      "\\(0.5^\\circ\\)",
      "\\(5^\\circ\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The least count of an instrument is the smallest division marked on its measuring scale.
On a standard geometry protractor:
- Total angle span = \\(180^\\circ\\)
- Number of division markings = \\(180\\)
Value of one smallest graduation mark:
\\[
\\text{Least Count} = \\frac{180^\\circ}{180} = 1^\\circ
\\]

### 2. Physical Context & Practical Illustration:
Any angle measured with a student protractor is accurate to \\(\\pm 1^\\circ\\). High-precision surveying instruments (theodolites) utilize Vernier angular scales to achieve least counts of \\(1'\\) (one arcminute).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(1^\\circ\\))**: Correct. Smallest graduation is \\(1\\text{ degree}\\).
- **Option B (\\(0.1^\\circ\\))**: Incorrect. Standard protractors do not have fractional degree marks.
- **Option C (\\(0.5^\\circ\\))**: Incorrect. Only specialized technical protractors have half-degree marks.
- **Option D (\\(5^\\circ\\))**: Incorrect. Major subdivisions are marked every \\(5^\\circ\\) or \\(10^\\circ\\), but smallest marks are \\(1^\\circ\\).`
  },

  // Q133
  "MH-9-SCIT-1-1.1-OSC-133": {
    text: "Linear momentum is defined as the product of which two physical quantities?",
    options: [
      "Mass and velocity",
      "Force and velocity",
      "Mass and acceleration",
      "Weight and height"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Linear momentum \\(\\vec{p}\\) is defined in classical mechanics as the product of mass and velocity:
\\[
\\vec{p} = m \\vec{v}
\\]
It is a vector quantity possessing the exact direction of the velocity vector \\(\\vec{v}\\). In SI units:
\\[
[p] = \\text{kg}\\cdot\\text{m/s}
\\]

### 2. Physical Context & Practical Illustration:
Momentum quantifies the 'impact force' needed to stop a moving object. A heavy truck and a light sports car traveling at the same speed have very different momenta because the truck's mass is far greater.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Mass and velocity)**: Correct. Standard definition \\(\\vec{p} = m\\vec{v}\\).
- **Option B (Force and velocity)**: Incorrect. \\(F \\cdot v\\) is mechanical **power**.
- **Option C (Mass and acceleration)**: Incorrect. \\(m \\cdot a\\) is net **force**.
- **Option D (Weight and height)**: Incorrect. \\(W \\cdot h\\) is gravitational potential energy.`
  },

  // Q134
  "MH-9-SCIT-1-1.1-OSC-134": {
    text: "What is the standard unit of force in the SI system?",
    options: [
      "Newton (\\(\\text{N}\\))",
      "Dyne (\\(\\text{dyn}\\))",
      "Joule (\\(\\text{J}\\))",
      "Pascal (\\(\\text{Pa}\\))"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's second law:
\\[
F = ma \\implies [F] = \\text{kg} \\times \\frac{\\text{m}}{\\text{s}^2} = \\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2} = \\text{Newton (N)}
\\]
One Newton is defined as the force required to accelerate a mass of \\(1\\text{ kg}\\) at a rate of \\(1\\text{ m/s}^2\\).

### 2. Physical Context & Practical Illustration:
Named in honor of Sir Isaac Newton. In CGS, force is measured in dynes (\\(1\\text{ N} = 10^5\\text{ dynes}\\)).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Newton)**: Correct. Standard SI unit of force.
- **Option B (Dyne)**: Incorrect. CGS unit of force.
- **Option C (Joule)**: Incorrect. Unit of work and energy.
- **Option D (Pascal)**: Incorrect. Unit of pressure (\\(\\text{N/m}^2\\)).`
  },

  // Q135
  "MH-9-SCIT-1-1.1-OSC-135": {
    text: "A particle moving with an initial velocity of \\(10\\text{ cm/s}\\) is subjected to a constant force that increases its velocity to \\(100\\text{ cm/s}\\) in \\(30\\text{ seconds}\\). What is the acceleration produced?",
    options: [
      "\\(3.0\\text{ cm/s}^2\\)",
      "\\(0.3\\text{ cm/s}^2\\)",
      "\\(30\\text{ cm/s}^2\\)",
      "\\(0.03\\text{ cm/s}^2\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Acceleration is given by:
\\[
a = \\frac{v - u}{t}
\\]
Given data:
- Initial velocity \\(u = 10\\text{ cm/s}\\)
- Final velocity \\(v = 100\\text{ cm/s}\\)
- Time \\(t = 30\\text{ s}\\)

Substitute the values:
\\[
a = \\frac{100 - 10}{30} = \\frac{90}{30} = 3.0\\text{ cm/s}^2
\\]

### 2. Physical Context & Practical Illustration:
In CGS units, the velocity increases by \\(3\\text{ cm/s}\\) each second. In SI units, this corresponds to \\(0.03\\text{ m/s}^2\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(3.0\\text{ cm/s}^2\\))**: Correct. \\(90 / 30 = 3.0\\text{ cm/s}^2\\).
- **Option B (\\(0.3\\text{ cm/s}^2\\))**: Incorrect. Decimal place error.
- **Option C (\\(30\\text{ cm/s}^2\\))**: Incorrect. Did not divide by 30 properly.
- **Option D (\\(0.03\\text{ cm/s}^2\\))**: Incorrect. This would be the value in \\(\\text{m/s}^2\\), not \\(\\text{cm/s}^2\\).`
  },

  // Q137
  "MH-9-SCIT-1-1.1-OSC-137": {
    text: "A constant force acts on a body of mass \\(10\\text{ g}\\) initially at rest. If the body attains a velocity of \\(30\\text{ cm/s}\\) after \\(1\\text{ minute}\\), what is the magnitude of the applied force?",
    options: [
      "\\(5\\text{ dynes}\\)",
      "\\(5\\text{ N}\\)",
      "\\(50\\text{ dynes}\\)",
      "\\(0.5\\text{ dynes}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In CGS units:
- Mass \\(m = 10\\text{ g}\\)
- Initial velocity \\(u = 0\\)
- Final velocity \\(v = 30\\text{ cm/s}\\)
- Time \\(t = 1\\text{ minute} = 60\\text{ s}\\)

Calculate acceleration:
\\[
a = \\frac{v - u}{t} = \\frac{30 - 0}{60} = 0.5\\text{ cm/s}^2
\\]
Now compute force:
\\[
F = ma = 10\\text{ g} \\times 0.5\\text{ cm/s}^2 = 5\\text{ dynes}
\\]

### 2. Physical Context & Practical Illustration:
A force of 5 dynes is a tiny force (\\(5 \\times 10^{-5}\\text{ N}\\)), roughly the weight of a tiny mosquito, capable of slowly accelerating a 10 g pebble over 60 seconds.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (5 dynes)**: Correct. \\(F = 10 \\times (30/60) = 5\\text{ dynes}\\).
- **Option B (5 N)**: Incorrect. Newton is SI (\\(5\\text{ N} = 500,000\\text{ dynes}\\)).
- **Option C (50 dynes)**: Incorrect. Omits converting 1 minute to 60 seconds (dividing by 1 instead of 60).
- **Option D (0.5 dynes)**: Incorrect. Did not multiply by mass.`
  },

  // Q138
  "MH-9-SCIT-1-1.1-OSC-138": {
    text: "A constant horizontal force \\(F\\) acts on a body, displacing it along a straight horizontal path from point A to point B over a distance \\(s_{AB}\\). What is the mechanical work done by the force?",
    options: [
      "\\(W = F \\times s_{AB}\\)",
      "\\(W = \\frac{F}{s_{AB}}\\)",
      "\\(W = F + s_{AB}\\)",
      "\\(W = 0\\text{ J}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Work done by a constant force is defined as the dot product:
\\[
W = \\vec{F} \\cdot \\vec{s} = F s \\cos\\theta
\\]
When the force acts in the exact direction of displacement from A to B:
\\[
\\theta = 0^\\circ \\implies \\cos 0^\\circ = 1
\\]
\\[
W = F \\times s_{AB}
\\]

### 2. Physical Context & Practical Illustration:
Pulling a crate from point A to point B across a warehouse floor with a force of \\(50\\text{ N}\\) over \\(10\\text{ m}\\) yields \\(W = 50 \\times 10 = 500\\text{ Joules}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (\\(W = F \\times s_{AB}\\))**: Correct. Standard definition of work.
- **Option B**: Incorrect. Division does not yield work.
- **Option C**: Incorrect. Incompatible dimensional units cannot be added.
- **Option D (0 J)**: Incorrect. Force acts along displacement, so work is non-zero.`
  },

  // Q139
  "MH-9-SCIT-1-1.1-OSC-139": {
    text: "Which of Newton's laws of motion provides the qualitative definition of force as an external agency that alters an object's state of rest or uniform motion?",
    options: [
      "Newton's First Law of Motion",
      "Newton's Second Law of Motion",
      "Newton's Third Law of Motion",
      "Newton's Law of Universal Gravitation"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Newton's laws define force in complementary ways:
- **Newton's First Law**: Gives the **qualitative definition** of force. It defines force as that external agency which changes or tends to change the state of rest or of uniform motion in a straight line of a body.
- **Newton's Second Law**: Gives the **quantitative measure** of force (\\(F = \\frac{dp}{dt} = ma\\)).

### 2. Physical Context & Practical Illustration:
The First Law establishes the concept of inertia and establishes that without force, motion remains unchanged.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (First Law)**: Correct. Qualitatively defines what a force is.
- **Option B (Second Law)**: Incorrect. Measures the numerical magnitude of force (\\(F = ma\\)).
- **Option C (Third Law)**: Incorrect. Describes the interactive nature of action-reaction pairs.
- **Option D (Gravitation)**: Incorrect. Specifies the particular law for gravitational mass attraction.`
  },

  // Q140
  "MH-9-SCIT-1-1.1-OSC-140": {
    text: "When a projectile is launched horizontally from the top of a high cliff into still air, what trajectory path does it follow under gravity?",
    options: [
      "Parabolic path",
      "Hyperbolic path",
      "Circular path",
      "Straight inclined line"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Resolve motion into independent horizontal and vertical components:
- Horizontal motion: \\(x = u t \\implies t = \\frac{x}{u}\\) (constant speed \\(u\\)).
- Vertical motion under gravity: \\(y = \\frac{1}{2}gt^2\\).
Substitute \\(t\\) into vertical displacement:
\\[
y = \\frac{1}{2}g \\left(\\frac{x}{u}\\right)^2 = \\left(\\frac{g}{2u^2}\\right) x^2
\\]
This is the standard equation of a **parabola** (\\(y = k x^2\\)).

### 2. Physical Context & Practical Illustration:
Water spurting horizontally from a garden hose or a cannonball fired horizontally from a fortress follows a smooth parabolic arc towards the ground.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Parabolic)**: Correct. Quadratic relation \\(y \\propto x^2\\) forms a parabola.
- **Option B (Hyperbolic)**: Incorrect. Hyperbolic orbits occur at speeds exceeding escape velocity.
- **Option C (Circular)**: Incorrect. Requires central centripetal force.
- **Option D (Straight line)**: Incorrect. Gravity constantly bends the path downward.`
  },

  // Q141
  "MH-9-SCIT-1-1.1-OSC-141": {
    text: "Hypothetically, if a frictionless tunnel is drilled through the Earth from the North Pole to the South Pole and a \\(2\\text{ kg}\\) sphere is dropped into it, what motion will the sphere execute?",
    options: [
      "Simple harmonic motion oscillating back and forth through Earth's center",
      "It will fall to Earth's center and come to a permanent stop there",
      "It will fly out into space from the South Pole with escape velocity",
      "It will instantly bounce backward at the North Pole"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Inside a uniform sphere of mass \\(M\\) and radius \\(R\\), the gravitational force at distance \\(r\\) from the center is:
\\[
F(r) = -\\frac{G M m}{R^3} r = -k r
\\]
Because the restoring force is directly proportional to displacement from the center (\\(F \\propto -r\\)), the sphere executes **Simple Harmonic Motion (SHM)** about Earth's center.
The period of oscillation is:
\\[
T = 2\\pi \\sqrt{\\frac{R}{g}} \\approx 84.6\\text{ minutes}
\\]

### 2. Physical Context & Practical Illustration:
The sphere accelerates towards the center, reaches maximum speed at the center (\\(\\approx 7.9\\text{ km/s}\\)), then decelerates as it approaches the South Pole, momentarily coming to rest before falling back.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Simple Harmonic Motion)**: Correct. Linear restoring force \\(F = -kr\\) produces SHM with a period of ~84.6 minutes.
- **Option B (Stops at center)**: Incorrect. At the center, gravity is zero but velocity is maximum, so inertia carries it through.
- **Option C (Flies out into space)**: Incorrect. Energy is conserved; it stops exactly at the opposite surface.
- **Option D**: Incorrect. Bouncing requires a physical collision surface.`
  },

  // Q146
  "MH-9-SCIT-1-1.1-OSC-146": {
    text: "Which of the four fundamental interactions of nature binds protons and neutrons together inside the atomic nucleus?",
    options: [
      "Strong nuclear force",
      "Gravitational force",
      "Electromagnetic force",
      "Weak nuclear force"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Protons inside an atomic nucleus are positively charged and experience intense electrostatic repulsion:
\\[
F_e = \\frac{1}{4\\pi\\varepsilon_0} \\frac{e^2}{r^2}
\\]
To overcome this repulsive force and hold nucleons together, the **strong nuclear force** acts at short ranges (\\(\\le 10^{-15}\\text{ m} = 1\\text{ fm}\\)). It is approximately \\(100\\) times stronger than electromagnetism and is charge-independent (acts equally between \\(p-p\\), \\(n-n\\), and \\(p-n\\)).

### 2. Physical Context & Practical Illustration:
Without the strong nuclear force, atomic nuclei would fly apart instantly due to proton repulsion, making chemical elements and matter impossible.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Strong nuclear force)**: Correct. The fundamental force that binds atomic nuclei.
- **Option B (Gravitational force)**: Incorrect. Far too weak by a factor of \\(10^{-38}\\).
- **Option C (Electromagnetic force)**: Incorrect. Repels like-charged protons.
- **Option D (Weak nuclear force)**: Incorrect. Governs beta decay, not nuclear binding.`
  },

  // Q147
  "MH-9-SCIT-1-1.1-OSC-147": {
    text: "A constant force acts on a body of mass \\(2\\text{ kg}\\). The body travels \\(3\\text{ m}\\) in the 1st second and \\(1\\text{ m}\\) in the 2nd second. What is the magnitude of the retarding force acting on the body?",
    options: [
      "\\(4\\text{ N}\\)",
      "\\(2\\text{ N}\\)",
      "\\(12\\text{ N}\\)",
      "\\(1\\text{ N}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The distance traveled in the \\(n^{\\text{th}}\\) second is given by:
\\[
s_n = u + \\frac{1}{2}a(2n - 1)
\\]
For \\(n = 1\\):
\\[
s_1 = u + \\frac{1}{2}a(1) = 3 \\implies u + 0.5a = 3 \\quad \\text{--- (Eq 1)}
\\]
For \\(n = 2\\):
\\[
s_2 = u + \\frac{1}{2}a(3) = 1 \\implies u + 1.5a = 1 \\quad \\text{--- (Eq 2)}
\\]
Subtract (Eq 1) from (Eq 2):
\\[
(1.5a - 0.5a) = 1 - 3 \\implies a = -2\\text{ m/s}^2
\\]
Magnitude of force:
\\[
F = m |a| = 2\\text{ kg} \\times 2\\text{ m/s}^2 = 4\\text{ N}
\\]

### 2. Physical Context & Practical Illustration:
The body decelerates at \\(2\\text{ m/s}^2\\) under a constant opposing friction or braking force of \\(4\\text{ Newtons}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (4 N)**: Correct. \\(a = -2\\text{ m/s}^2 \\implies F = 2 \\times 2 = 4\\text{ N}\\).
- **Option B (2 N)**: Incorrect. Equals acceleration, not force.
- **Option C (12 N)**: Incorrect. Arithmetic error.
- **Option D (1 N)**: Incorrect. Calculation error.`
  },

  // Q148
  "MH-9-SCIT-1-1.1-OSC-148": {
    text: "Two forces \\(\\vec{F}_1\\) and \\(\\vec{F}_2\\) act at an angle \\(\\theta\\) to each other. If the angle \\(\\theta\\) between their directions is increased from \\(0^\\circ\\) towards \\(180^\\circ\\), what happens to the magnitude of their resultant force \\(R\\)?",
    options: [
      "The resultant force decreases continuously",
      "The resultant force increases continuously",
      "The resultant force remains strictly constant",
      "The resultant force first increases then drops to zero"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
The magnitude of the resultant of two forces is given by the law of vector addition:
\\[
R = \\sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \\cos\\theta}
\\]
As the angle \\(\\theta\\) increases from \\(0^\\circ\\) to \\(180^\\circ\\), \\(\\cos\\theta\\) decreases monotonically from \\(+1\\) to \\(-1\\):
- At \\(\\theta = 0^\\circ\\): \\(R = F_1 + F_2\\) (maximum).
- At \\(\\theta = 90^\\circ\\): \\(R = \\sqrt{F_1^2 + F_2^2}\\).
- At \\(\\theta = 180^\\circ\\): \\(R = |F_1 - F_2|\\) (minimum).
Therefore, increasing \\(\\theta\\) causes the resultant force to **decrease continuously**.

### 2. Physical Context & Practical Illustration:
Two horses pulling a cart forward in parallel (\\(\\theta = 0^\\circ\\)) exert maximum combined pull. If they pull at an angle to each other, their useful forward combined force decreases.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Decreases continuously)**: Correct. \\(\\cos\\theta\\) decreases as \\(\\theta\\) increases, reducing \\(R\\).
- **Option B (Increases)**: Incorrect. Inverts the cosine dependence.
- **Option C (Constant)**: Incorrect. Vectors add geometrically, not as constant scalars.
- **Option D**: Incorrect. Monotonic decrease throughout the interval.`
  },

  // Q149
  "MH-9-SCIT-1-1.1-OSC-149": {
    text: "When a rigid body remains at rest on a horizontal surface, what is the net condition of the external forces acting upon it?",
    options: [
      "The vector sum of all external forces acting on the body is strictly zero (\\(\\sum \\vec{F} = 0\\))",
      "There are absolutely zero forces acting on the body",
      "The gravitational downward force is greater than the upward normal reaction",
      "Only frictional forces are acting on the body"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By Newton's first law of motion and conditions of static equilibrium:
\\[
\\sum \\vec{F} = m\\vec{a}
\\]
If the body remains in a state of rest (\\(\\vec{v} = 0, \\vec{a} = 0\\)):
\\[
\\sum \\vec{F} = 0
\\]
For a book resting on a table, downward gravity \\(mg\\) and upward normal reaction force \\(N\\) are equal in magnitude and opposite in direction:
\\[
N - mg = 0 \\implies N = mg
\\]

### 2. Physical Context & Practical Illustration:
Forces are actively present, but they are in perfect balance (**balanced forces**).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Vector sum is zero)**: Correct. Forces balance each other out (\\(\\sum \\vec{F} = 0\\)).
- **Option B (Zero forces)**: Incorrect. Gravity and normal force are actively acting.
- **Option C**: Incorrect. If downward force were greater, the body would accelerate downwards.
- **Option D**: Incorrect. Static friction is zero if there is no horizontal applied force.`
  },

  // Q158
  "MH-9-SCIT-1-1.1-OSC-158": {
    text: "A ball is thrown vertically upwards with an initial velocity of \\(19.6\\text{ m/s}\\). Taking \\(g = 9.8\\text{ m/s}^2\\), what is the maximum height reached by the ball?",
    options: [
      "\\(19.6\\text{ m}\\)",
      "\\(9.8\\text{ m}\\)",
      "\\(39.2\\text{ m}\\)",
      "\\(4.9\\text{ m}\\)"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
At maximum height, the vertical velocity momentarily becomes zero: \\(v = 0\\text{ m/s}\\).
Using the third kinematic equation:
\\[
v^2 = u^2 - 2gh \\implies 0 = u^2 - 2gh \\implies h = \\frac{u^2}{2g}
\\]
Substitute given values:
- \\(u = 19.6\\text{ m/s}\\)
- \\(g = 9.8\\text{ m/s}^2\\)
\\[
h = \\frac{(19.6)^2}{2 \\times 9.8} = \\frac{19.6 \\times 19.6}{19.6} = 19.6\\text{ m}
\\]

### 2. Physical Context & Practical Illustration:
The time to reach maximum height is \\(t = u/g = 19.6 / 9.8 = 2\\text{ seconds}\\). During these 2 seconds, gravity steadily removes velocity until the ball peaks at \\(19.6\\text{ m}\\).

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (19.6 m)**: Correct. Exact computation: \\(h = \\frac{19.6^2}{19.6} = 19.6\\text{ m}\\).
- **Option B (9.8 m)**: Incorrect. Divides by \\(4g\\) instead of \\(2g\\).
- **Option C (39.2 m)**: Incorrect. Multiplies by 2 instead of dividing.
- **Option D (4.9 m)**: Incorrect. Calculation error.`
  },

  // Q159
  "MH-9-SCIT-1-1.1-OSC-159": {
    text: "A simple pendulum oscillates along the arc \\(A \\rightarrow O \\rightarrow B\\), where \\(O\\) is the central equilibrium position and \\(A\\) and \\(B\\) are the extreme turning points. At which position is the magnitude of the bob's restoring acceleration maximum?",
    options: [
      "At the extreme positions A and B",
      "At the central equilibrium position O",
      "Midway between O and A only",
      "Acceleration is uniform throughout the entire path"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
For a simple pendulum oscillating with angular displacement \\(\\theta\\), the restoring force acting tangential to the arc is:
\\[
F_{\\text{restoring}} = -mg \\sin\\theta \\implies a = -g \\sin\\theta
\\]
1. **At the mean position O** (\\(\\theta = 0\\)): \\(a = -g \\sin 0 = 0\\text{ m/s}^2\\) (acceleration is minimum/zero).
2. **At extreme positions A and B** (\\(\\theta = \\theta_{\\text{max}}\\)): \\(a_{\\text{max}} = g \\sin\\theta_{\\text{max}}\\) (acceleration is **maximum**).

### 2. Physical Context & Practical Illustration:
At the extreme positions, the bob stops moving momentarily (\\(v = 0\\)), but the gravitational restoring component pulling it back toward the center is at its absolute peak.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (At extreme positions A and B)**: Correct. Maximum displacement produces maximum restoring force and acceleration.
- **Option B (At central position O)**: Incorrect. At the center, restoring acceleration is zero (while velocity is maximum).
- **Option C**: Incorrect. Acceleration increases monotonically towards the extremes.
- **Option D**: Incorrect. Simple pendulum motion is non-uniform acceleration.`
  },

  // Q160
  "MH-9-SCIT-1-1.1-OSC-160": {
    text: "During a severe cyclone, huge trees can be uprooted when exposed to violent storm gusts. Which physical concept of mechanics explains why trees initially resist deformation before falling?",
    options: [
      "Inertia of rest",
      "Inertia of motion",
      "Inertia of direction",
      "Conservation of charge"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
By **Newton's First Law of Motion**, a massive body has an inherent property called **inertia of rest**—the tendency to resist any sudden change in its state of rest.
When violent cyclone winds strike:
1. Tremendous aerodynamic drag exerts large forces on the tree's upper foliage.
2. The massive trunk and root system possess large inertia of rest and resist moving.
3. The resulting extreme mechanical shear strain and torque snap the root network at the soil boundary.

### 2. Physical Context & Practical Illustration:
Similarly, when a carpet is beaten with a stick, the dust particles remain stationary due to inertia of rest while the fabric moves away, freeing the dust.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Inertia of rest)**: Correct. Massive trees resist sudden acceleration by high-velocity wind.
- **Option B (Inertia of motion)**: Incorrect. Trees are stationary before the wind hits.
- **Option C (Inertia of direction)**: Incorrect. Relates to curved motion.
- **Option D**: Incorrect. Electrical charges play no role in macroscopic wind mechanical forces.`
  },

  // Q175
  "MH-9-SCIT-1-1.1-OSC-175": {
    text: "In Newton's second kinematic equation of motion, \\(s = ut + \\frac{1}{2}at^2\\), what physical quantity does the symbol \\(s\\) represent?",
    options: [
      "Displacement covered in time interval \\(t\\)",
      "Speed of the object at time \\(t\\)",
      "Distance covered during the \\(t^{\\text{th}}\\) second only",
      "Maximum vertical elevation reached"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
In the derivation of kinematics from calculus:
\\[
v = \\frac{ds}{dt} = u + at \\implies ds = (u + at) \\, dt
\\]
Integrating from \\(t = 0\\) to \\(t\\):
\\[
s(t) - s(0) = \\int_0^t (u + at) \\, dt = ut + \\frac{1}{2}at^2
\\]
Thus, \\(s\\) represents the **net displacement** achieved by the body during the total elapsed time interval \\(t\\).

### 2. Physical Context & Practical Illustration:
For unidirectional motion along a straight line without reversing direction, the magnitude of displacement \\(s\\) is equal to the total distance covered.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Displacement covered in time \\(t\\))**: Correct. Standard definition in the equations of motion.
- **Option B (Speed)**: Incorrect. Speed/velocity is represented by \\(v\\).
- **Option C (Distance in \\(t^{\\text{th}}\\) second)**: Incorrect. That is \\(s_n = u + \\frac{1}{2}a(2n - 1)\\).
- **Option D**: Incorrect. True only for the special case of vertical apex.`
  },

  // Q177
  "MH-9-SCIT-1-1.1-OSC-177": {
    text: "If the displacement-time graph of a moving particle is a horizontal straight line parallel to the time axis, what is the velocity of the particle?",
    options: [
      "Zero (\\(0\\text{ m/s}\\))",
      "Uniform and positive",
      "Infinite",
      "Equal to its acceleration"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
Velocity is defined as the slope of the displacement-time graph:
\\[
v = \\frac{ds}{dt}
\\]
A line parallel to the time axis has constant displacement (\\(s = \\text{constant}\\)):
\\[
\\frac{ds}{dt} = 0 \\implies v = 0\\text{ m/s}
\\]
The velocity of the particle is **zero**, meaning the particle is permanently stationary.

### 2. Physical Context & Practical Illustration:
A person sitting on a park bench maintains a constant distance from a lamp post. The displacement-time graph is a horizontal flat line, indicating zero speed.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Zero)**: Correct. Flat horizontal slope means \\(v = 0\\).
- **Option B (Uniform and positive)**: Incorrect. Would require an upward inclined straight line.
- **Option C (Infinite)**: Incorrect. Would require a vertical line.
- **Option D**: Incorrect. Both velocity and acceleration are zero.`
  },

  // Q187
  "MH-9-SCIT-1-1.1-OSC-187": {
    text: "While sharpening a knife, glowing metal sparks fly off tangentially from the grinding wheel. This practical observation illustrates which physical principle?",
    options: [
      "Inertia of direction",
      "Inertia of rest",
      "Inertia of mass",
      "Thermal radiation pressure"
    ],
    correctAnswer: "A",
    solution: `### 1. Scientific Principle & Mathematical Derivation:
At the point of contact on the rim of the rotating grinding wheel, friction shears off incandescent metal particles. At the exact instant of separation, each spark has an instantaneous velocity \\(\\vec{v}\\) directed **tangential** to the circular rim.
Because the centripetal adhesive force ceases upon separation:
\\[
\\vec{F}_{\\text{net}} = 0
\\]
By Newton's First Law (Inertia of direction), the spark continues in an unswerving straight line along its tangential launch heading.

### 2. Physical Context & Practical Illustration:
This directional inertia is utilized in rotary tools, centrifuge separators, and explains why mud guards are mounted over bicycle wheels.

### 3. Step-by-Step Option & Misconception Analysis:
- **Option A (Inertia of direction)**: Correct. Demonstrates persistence of directional velocity upon release of centripetal constraint.
- **Option B (Inertia of rest)**: Incorrect. Sparks are already moving at high speed.
- **Option C (Inertia of mass)**: Incorrect. Not the specific category of inertia involved.
- **Option D**: Incorrect. Radiation pressure is negligible on macroscopic sparks.`
  }
};
