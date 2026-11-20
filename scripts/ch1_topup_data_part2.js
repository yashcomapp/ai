// Part 2: Subtopics 1.5.1 (6 Qs), 1.5.2 (4 Qs), 1.6.1 (16 Qs), 1.6.2 (13 Qs), 1.6.3 (13 Qs), 1.6.4 (13 Qs), 1.6.5 (15 Qs) = 80 Questions

const part2Questions = [
  // --- Subtopic 1.5.1 (6 Questions: v = 2πr / t) ---
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'An artificial satellite circles Earth in a circular orbit of radius \\(42000\\text{ km}\\) in \\(24\\text{ hours}\\). What is its orbital speed in \\(\\text{km/s}\\)? (Use \\(\\pi = \\frac{22}{7}\\))',
    options: [
      '\\(3.06\\text{ km/s}\\)',
      '\\(11.2\\text{ km/s}\\)',
      '\\(7.9\\text{ km/s}\\)',
      '\\(1.53\\text{ km/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: For uniform circular motion, speed is given by \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Calculation**: Radius \\(r = 42000\\text{ km}\\). Time \\(t = 24\\text{ h} = 24 \\times 3600 = 86400\\text{ s}\\). Total distance \\(= 2 \\times \\frac{22}{7} \\times 42000 = 264000\\text{ km}\\). Speed \\(v = \\frac{264000}{86400} \\approx 3.056\\text{ km/s} \\approx 3.06\\text{ km/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(3.06\\text{ km/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: For uniform circular motion, speed is given by \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Calculation**: Radius \\(r = 42000\\text{ km}\\). Time \\(t = 24\\text{ h} = 24 \\times 3600 = 86400\\text{ s}\\). Total distance \\(= 2 \\times \\frac{22}{7} \\times 42000 = 264000\\text{ km}\\). Speed \\(v = \\frac{264000}{86400} \\approx 3.056\\text{ km/s} \\approx 3.06\\text{ km/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(3.06\\text{ km/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'A tip of a minute hand of a wall clock has a length of \\(7\\text{ cm}\\). What is the linear speed of the tip of the minute hand in \\(\\text{cm/s}\\)? (Use \\(\\pi = \\frac{22}{7}\\))',
    options: [
      '\\(0.0122\\text{ cm/s}\\)',
      '\\(0.733\\text{ cm/s}\\)',
      '\\(44\\text{ cm/s}\\)',
      '\\(0.0020\\text{ cm/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: A minute hand completes 1 rotation (\\(2\\pi r\\)) in \\(60\\text{ minutes} = 3600\\text{ s}\\).\n\n**Step 2: Calculation**: Distance in one revolution \\(= 2 \\times \\frac{22}{7} \\times 7 = 44\\text{ cm}\\). Time \\(t = 3600\\text{ s}\\). Linear speed \\(v = \\frac{44}{3600} \\approx 0.0122\\text{ cm/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(0.0122\\text{ cm/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: A minute hand completes 1 rotation (\\(2\\pi r\\)) in \\(60\\text{ minutes} = 3600\\text{ s}\\).\n\n**Step 2: Calculation**: Distance in one revolution \\(= 2 \\times \\frac{22}{7} \\times 7 = 44\\text{ cm}\\). Time \\(t = 3600\\text{ s}\\). Linear speed \\(v = \\frac{44}{3600} \\approx 0.0122\\text{ cm/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(0.0122\\text{ cm/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'An athlete completes one round of a circular track of diameter \\(280\\text{ m}\\) in \\(40\\text{ s}\\). What is the speed of the athlete? (Use \\(\\pi = \\frac{22}{7}\\))',
    options: [
      '\\(22\\text{ m/s}\\)',
      '\\(44\\text{ m/s}\\)',
      '\\(7\\text{ m/s}\\)',
      '\\(11\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Diameter \\(d = 280\\text{ m} \\implies r = 140\\text{ m}\\). Speed \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Calculation**: Circumference \\(= 2 \\times \\frac{22}{7} \\times 140 = 880\\text{ m}\\). Time \\(t = 40\\text{ s}\\). \\(v = \\frac{880}{40} = 22\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(22\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Diameter \\(d = 280\\text{ m} \\implies r = 140\\text{ m}\\). Speed \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Calculation**: Circumference \\(= 2 \\times \\frac{22}{7} \\times 140 = 880\\text{ m}\\). Time \\(t = 40\\text{ s}\\). \\(v = \\frac{880}{40} = 22\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The speed is \\(22\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'In uniform circular motion, why is the motion called accelerated even if the speed \\(v = \\frac{2\\pi r}{t}\\) remains strictly constant?',
    options: [
      'Because the direction of the velocity vector is continuously changing at every instant',
      'Because the radius of the circle expands and contracts',
      'Because the distance covered per unit time continuously increases',
      'Because the speed varies due to air resistance'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Velocity is a vector with magnitude (speed) and direction.\n\n**Step 2: Analysis**: In circular motion, the direction of motion at any instant is along the tangent to the circle. Since the tangent changes direction continuously, velocity changes continuously, producing an acceleration towards the center (centripetal acceleration).\n\n**Step 3: Conclusion**: The continuous change in direction makes it an accelerated motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Velocity is a vector with magnitude (speed) and direction.\n\n**Step 2: Analysis**: In circular motion, the direction of motion at any instant is along the tangent to the circle. Since the tangent changes direction continuously, velocity changes continuously, producing an acceleration towards the center (centripetal acceleration).\n\n**Step 3: Conclusion**: The continuous change in direction makes it an accelerated motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'A stone tied to a string of length \\(0.5\\text{ m}\\) is whirled in a horizontal circle, making \\(4\\text{ complete revolutions}\\) every second. What is the linear speed of the stone? (Use \\(\\pi = 3.14\\))',
    options: [
      '\\(12.56\\text{ m/s}\\)',
      '\\(6.28\\text{ m/s}\\)',
      '\\(3.14\\text{ m/s}\\)',
      '\\(25.12\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Time period \\(T = \\frac{1}{\\text{frequency}} = \\frac{1}{4} = 0.25\\text{ s}\\). Linear speed \\(v = \\frac{2\\pi r}{T}\\).\n\n**Step 2: Calculation**: \\(v = \\frac{2 \\times 3.14 \\times 0.5}{0.25} = \\frac{3.14}{0.25} = 12.56\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The linear speed is \\(12.56\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Time period \\(T = \\frac{1}{\\text{frequency}} = \\frac{1}{4} = 0.25\\text{ s}\\). Linear speed \\(v = \\frac{2\\pi r}{T}\\).\n\n**Step 2: Calculation**: \\(v = \\frac{2 \\times 3.14 \\times 0.5}{0.25} = \\frac{3.14}{0.25} = 12.56\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The linear speed is \\(12.56\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.5.1',
    type: 'OSC',
    text: 'If the radius of a circular track is doubled while the time taken to complete one revolution remains constant, how does the linear speed of the moving body change?',
    options: [
      'The speed is doubled',
      'The speed is halved',
      'The speed becomes four times',
      'The speed remains unchanged'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Linear speed \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Analysis**: Since \\(t\\) is constant, \\(v \\propto r\\). If \\(r\' = 2r\\), then \\(v\' = \\frac{2\\pi(2r)}{t} = 2v\\).\n\n**Step 3: Conclusion**: The linear speed is doubled. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Linear speed \\(v = \\frac{2\\pi r}{t}\\).\n\n**Step 2: Analysis**: Since \\(t\\) is constant, \\(v \\propto r\\). If \\(r\' = 2r\\), then \\(v\' = \\frac{2\\pi(2r)}{t} = 2v\\).\n\n**Step 3: Conclusion**: The linear speed is doubled. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.5.2 (4 Questions: Centripetal force formula F = mv²/r) ---
  {
    subtopicNumber: '1.5.2',
    type: 'OSC',
    text: 'A car of mass \\(1000\\text{ kg}\\) rounds a curve of radius \\(50\\text{ m}\\) at a speed of \\(10\\text{ m/s}\\). What is the centripetal force required to keep the car on the circular path?',
    options: [
      '\\(2000\\text{ N}\\)',
      '\\(5000\\text{ N}\\)',
      '\\(1000\\text{ N}\\)',
      '\\(200\\text{ N}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Centripetal force is given by \\(F = \\frac{m v^2}{r}\\).\n\n**Step 2: Calculation**: \\(m = 1000\\text{ kg}\\), \\(v = 10\\text{ m/s}\\), \\(r = 50\\text{ m}\\). \\(F = \\frac{1000 \\times 10^2}{50} = \\frac{1000 \\times 100}{50} = 2000\\text{ N}\\).\n\n**Step 3: Conclusion**: The required centripetal force is \\(2000\\text{ N}\\) (provided by road friction). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Centripetal force is given by \\(F = \\frac{m v^2}{r}\\).\n\n**Step 2: Calculation**: \\(m = 1000\\text{ kg}\\), \\(v = 10\\text{ m/s}\\), \\(r = 50\\text{ m}\\). \\(F = \\frac{1000 \\times 10^2}{50} = \\frac{1000 \\times 100}{50} = 2000\\text{ N}\\).\n\n**Step 3: Conclusion**: The required centripetal force is \\(2000\\text{ N}\\) (provided by road friction). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.5.2',
    type: 'OSC',
    text: 'What provides the necessary centripetal force to keep the Moon in its stable circular orbit around the Earth?',
    options: [
      'The gravitational force of attraction exerted by the Earth on the Moon',
      'The electrostatic force between Earth and Moon',
      'The magnetic field of the Earth',
      'The atmospheric pressure of outer space'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Any body in circular orbit requires an inward centripetal force towards the center of rotation.\n\n**Step 2: Physical Cause**: For celestial orbits, Sir Isaac Newton showed that the gravitational force between masses provides the necessary centripetal force: \\(F_g = \\frac{G M m}{r^2} = \\frac{m v^2}{r}\\).\n\n**Step 3: Conclusion**: Earth\'s gravitational attraction provides the centripetal force. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Any body in circular orbit requires an inward centripetal force towards the center of rotation.\n\n**Step 2: Physical Cause**: For celestial orbits, Sir Isaac Newton showed that the gravitational force between masses provides the necessary centripetal force: \\(F_g = \\frac{G M m}{r^2} = \\frac{m v^2}{r}\\).\n\n**Step 3: Conclusion**: Earth\'s gravitational attraction provides the centripetal force. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.5.2',
    type: 'OSC',
    text: 'A stone is tied to a string and whirled in a circular path. If the string suddenly snaps, in what direction will the stone fly off?',
    options: [
      'Along the tangent to the circular path at the point of snapping (due to inertia of direction)',
      'Radially outward away from the center',
      'Radially inward towards the center',
      'In a spiral path expanding outwards'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The tension in the string provides the inward centripetal force maintaining the circular path.\n\n**Step 2: Physical Analysis**: The instant the string snaps, the centripetal force drops to zero. By Newton\'s 1st law (inertia of direction), the stone continues along its instantaneous velocity vector, which is tangent to the circle.\n\n**Step 3: Conclusion**: The stone flies off tangentially. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The tension in the string provides the inward centripetal force maintaining the circular path.\n\n**Step 2: Physical Analysis**: The instant the string snaps, the centripetal force drops to zero. By Newton\'s 1st law (inertia of direction), the stone continues along its instantaneous velocity vector, which is tangent to the circle.\n\n**Step 3: Conclusion**: The stone flies off tangentially. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.5.2',
    type: 'OSC',
    text: 'If a body of mass \\(m\\) is moving with speed \\(v\\) in a circle of radius \\(r\\), by what factor does the centripetal force change if the speed is tripled while keeping the radius unchanged?',
    options: [
      'It increases by a factor of 9',
      'It increases by a factor of 3',
      'It increases by a factor of 6',
      'It remains unchanged'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(F = \\frac{m v^2}{r}\\).\n\n**Step 2: Calculation**: Since \\(F \\propto v^2\\), when speed is tripled (\\(v\' = 3v\\)), \\(F\' = \\frac{m (3v)^2}{r} = 9 \\frac{m v^2}{r} = 9F\\).\n\n**Step 3: Conclusion**: Centripetal force increases by 9 times. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(F = \\frac{m v^2}{r}\\).\n\n**Step 2: Calculation**: Since \\(F \\propto v^2\\), when speed is tripled (\\(v\' = 3v\\)), \\(F\' = \\frac{m (3v)^2}{r} = 9 \\frac{m v^2}{r} = 9F\\).\n\n**Step 3: Conclusion**: Centripetal force increases by 9 times. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },

  // --- Subtopic 1.6.1 (16 Questions: Newton First Law - Inertia) ---
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'What physical property of a body is defined as its inherent tendency to resist any change in its state of rest or of uniform motion?',
    options: [
      'Inertia',
      'Momentum',
      'Acceleration',
      'Friction'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia is the natural property of matter by which it continues in its state of rest or uniform motion in a straight line unless acted upon by an external force.\n\n**Step 2: Foundation**: Described by Galileo and formalized by Isaac Newton as the First Law of Motion.\n\n**Step 3: Conclusion**: This property is called inertia. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia is the natural property of matter by which it continues in its state of rest or uniform motion in a straight line unless acted upon by an external force.\n\n**Step 2: Foundation**: Described by Galileo and formalized by Isaac Newton as the First Law of Motion.\n\n**Step 3: Conclusion**: This property is called inertia. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Which physical quantity serves as a direct quantitative measure of a body\'s inertia?',
    options: [
      'Mass',
      'Weight',
      'Volume',
      'Density'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia depends solely on the quantity of matter contained in a body.\n\n**Step 2: Comparison**: A heavier object (greater mass) requires a much larger force to change its state of rest or motion than a lighter object.\n\n**Step 3: Conclusion**: Mass is the quantitative measure of inertia. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia depends solely on the quantity of matter contained in a body.\n\n**Step 2: Comparison**: A heavier object (greater mass) requires a much larger force to change its state of rest or motion than a lighter object.\n\n**Step 3: Conclusion**: Mass is the quantitative measure of inertia. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'When a stationary bus suddenly starts moving forward, the passengers standing inside tend to fall backwards. Which type of inertia explains this phenomenon?',
    options: [
      'Inertia of rest',
      'Inertia of motion',
      'Inertia of direction',
      'Inertia of acceleration'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia of rest is the tendency of a body to remain at rest.\n\n**Step 2: Mechanism**: When the bus accelerates forward, the lower part of the passenger\'s body in contact with the bus moves forward, while the upper part tends to stay at rest due to inertia of rest, causing them to fall backward.\n\n**Step 3: Conclusion**: This is caused by inertia of rest. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia of rest is the tendency of a body to remain at rest.\n\n**Step 2: Mechanism**: When the bus accelerates forward, the lower part of the passenger\'s body in contact with the bus moves forward, while the upper part tends to stay at rest due to inertia of rest, causing them to fall backward.\n\n**Step 3: Conclusion**: This is caused by inertia of rest. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'When a moving bus suddenly applies brakes, the passengers jerk forward. Which type of inertia causes this?',
    options: [
      'Inertia of motion',
      'Inertia of rest',
      'Inertia of direction',
      'Gravitational inertia'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia of motion is the tendency of a moving body to maintain its state of uniform motion.\n\n**Step 2: Mechanism**: When brakes are applied, the bus and the feet of passengers stop, but the upper body continues moving forward at the previous speed due to inertia of motion.\n\n**Step 3: Conclusion**: This is caused by inertia of motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia of motion is the tendency of a moving body to maintain its state of uniform motion.\n\n**Step 2: Mechanism**: When brakes are applied, the bus and the feet of passengers stop, but the upper body continues moving forward at the previous speed due to inertia of motion.\n\n**Step 3: Conclusion**: This is caused by inertia of motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'When a car takes a sharp turn to the left, the passengers lean towards the right. Which type of inertia is responsible for this effect?',
    options: [
      'Inertia of direction',
      'Inertia of rest',
      'Inertia of motion',
      'Centripetal acceleration'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia of direction is the inability of a body to change its direction of motion by itself without an external force.\n\n**Step 2: Mechanism**: As the car steers left, the passengers tend to continue in their original straight-line direction, causing them to be displaced outward (towards the right) relative to the turning car.\n\n**Step 3: Conclusion**: This is inertia of direction. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia of direction is the inability of a body to change its direction of motion by itself without an external force.\n\n**Step 2: Mechanism**: As the car steers left, the passengers tend to continue in their original straight-line direction, causing them to be displaced outward (towards the right) relative to the turning car.\n\n**Step 3: Conclusion**: This is inertia of direction. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Why does a carpet release dust particles when beaten vigorously with a stick?',
    options: [
      'The carpet moves away suddenly, but the dust particles remain at rest due to inertia of rest and fall down under gravity',
      'The stick electrostatically charges the dust particles',
      'The dust particles are destroyed by the impact',
      'The carpet creates a vacuum that pulls dust out'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Beating a carpet relies on inertia of rest.\n\n**Step 2: Mechanism**: The stick causes the carpet fabric to jerk forward rapidly. The dust particles, having inertia of rest, tend to stay in their original position. Separated from the carpet fibers, they fall down due to gravity.\n\n**Step 3: Conclusion**: Inertia of rest separates the dust from the carpet. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Beating a carpet relies on inertia of rest.\n\n**Step 2: Mechanism**: The stick causes the carpet fabric to jerk forward rapidly. The dust particles, having inertia of rest, tend to stay in their original position. Separated from the carpet fibers, they fall down due to gravity.\n\n**Step 3: Conclusion**: Inertia of rest separates the dust from the carpet. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Why does an athlete run some distance before taking a long jump?',
    options: [
      'To acquire momentum and inertia of motion, which helps jump a longer horizontal distance',
      'To increase their body weight',
      'To overcome air resistance completely',
      'To warm up the landing pit'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Running gives the athlete forward velocity.\n\n**Step 2: Mechanism**: The inertia of motion gained during the sprint carries the body forward through the air after taking off from the board, maximizing jump length.\n\n**Step 3: Conclusion**: Inertia of motion helps achieve greater distance. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Running gives the athlete forward velocity.\n\n**Step 2: Mechanism**: The inertia of motion gained during the sprint carries the body forward through the air after taking off from the board, maximizing jump length.\n\n**Step 3: Conclusion**: Inertia of motion helps achieve greater distance. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Which of the following objects has the greatest inertia?',
    options: [
      'A loaded freight train with mass \\(2000\\text{ tonnes}\\)',
      'A cricket ball with mass \\(160\\text{ g}\\)',
      'A racing bicycle with mass \\(8\\text{ kg}\\)',
      'An automobile with mass \\(1500\\text{ kg}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia is directly proportional to mass.\n\n**Step 2: Comparison**: Mass of freight train \\(= 2000\\text{ tonnes} = 2 \\times 10^6\\text{ kg}\\), which is overwhelmingly larger than any car, bicycle, or ball.\n\n**Step 3: Conclusion**: The loaded freight train has the greatest inertia. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia is directly proportional to mass.\n\n**Step 2: Comparison**: Mass of freight train \\(= 2000\\text{ tonnes} = 2 \\times 10^6\\text{ kg}\\), which is overwhelmingly larger than any car, bicycle, or ball.\n\n**Step 3: Conclusion**: The loaded freight train has the greatest inertia. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Newton\'s First Law of Motion is also known by which classical name?',
    options: [
      'Galileo\'s Law of Inertia',
      'Law of Conservation of Energy',
      'Law of Action-Reaction',
      'Kepler\'s First Law'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Historical Context**: Galileo Galilei first formulated the concept that objects in motion stay in motion unless impeded by friction.\n\n**Step 2: Law Formulation**: Newton adapted Galileo\'s deduction into his First Law of Motion, often called the Law of Inertia.\n\n**Step 3: Conclusion**: It is known as Galileo\'s Law of Inertia. Hence, Option A is correct.',
    solution: '**Step 1: Historical Context**: Galileo Galilei first formulated the concept that objects in motion stay in motion unless impeded by friction.\n\n**Step 2: Law Formulation**: Newton adapted Galileo\'s deduction into his First Law of Motion, often called the Law of Inertia.\n\n**Step 3: Conclusion**: It is known as Galileo\'s Law of Inertia. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'A cardboard is placed over a drinking glass, and a coin is placed on top of the cardboard. When the cardboard is flicked away swiftly with a finger, what happens to the coin?',
    options: [
      'The coin drops directly into the glass due to its inertia of rest',
      'The coin flies away along with the cardboard',
      'The coin flies vertically upward to the ceiling',
      'The coin floats in the air indefinitely'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Sudden horizontal force acts on the card, not the coin.\n\n**Step 2: Mechanism**: The momentary friction is too brief to overcome the coin\'s inertia of rest. The coin remains in place as the card slides out, and gravity pulls it straight down into the glass.\n\n**Step 3: Conclusion**: The coin drops into the glass due to inertia of rest. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Sudden horizontal force acts on the card, not the coin.\n\n**Step 2: Mechanism**: The momentary friction is too brief to overcome the coin\'s inertia of rest. The coin remains in place as the card slides out, and gravity pulls it straight down into the glass.\n\n**Step 3: Conclusion**: The coin drops into the glass due to inertia of rest. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Why do mud-guards cover the wheels of motorbikes and cars?',
    options: [
      'To catch mud and water that flies off tangentially due to inertia of direction',
      'To improve the vehicle\'s aerodynamics and reduce drag',
      'To provide structural support to the tire axle',
      'To shield the engine from excessive heat'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Rotating wheels throw mud particles off.\n\n**Step 2: Mechanism**: At any point on the tire rim, adhering mud droplets lose adhesion and fly off along the tangent to the rotating wheel due to inertia of direction.\n\n**Step 3: Conclusion**: Mudguards intercept these tangential mud sprays. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Rotating wheels throw mud particles off.\n\n**Step 2: Mechanism**: At any point on the tire rim, adhering mud droplets lose adhesion and fly off along the tangent to the rotating wheel due to inertia of direction.\n\n**Step 3: Conclusion**: Mudguards intercept these tangential mud sprays. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'According to Newton\'s First Law of Motion, what is required to change the speed or direction of motion of a body?',
    options: [
      'An external unbalanced force',
      'A set of balanced internal forces',
      'Constant kinetic energy',
      'A non-zero gravitational potential'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Balanced forces produce zero net acceleration (\\(\\Sigma F = 0\\)).\n\n**Step 2: Condition**: Only an external, unbalanced force (\\(F_{\\text{net}} \\neq 0\\)) can alter the velocity of a body.\n\n**Step 3: Conclusion**: An external unbalanced force is strictly required. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Balanced forces produce zero net acceleration (\\(\\Sigma F = 0\\)).\n\n**Step 2: Condition**: Only an external, unbalanced force (\\(F_{\\text{net}} \\neq 0\\)) can alter the velocity of a body.\n\n**Step 3: Conclusion**: An external unbalanced force is strictly required. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'A book resting on a smooth horizontal table does not move on its own because:',
    options: [
      'The downward gravitational pull is balanced by the upward normal reaction of the table, resulting in zero net force',
      'There is no gravitational force acting on it',
      'The book has infinite mass and infinite inertia',
      'Frictional force is strictly infinite'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Equilibrium of forces on a resting body.\n\n**Step 2: Force Balance**: The weight of the book \\(W = mg\\) acts downwards, and the normal reaction \\(N\\) acts upwards. Since \\(N = W\\), the net force \\(F_{\\text{net}} = 0\\), and by Newton\'s 1st law, the book remains at rest.\n\n**Step 3: Conclusion**: Balanced vertical forces keep it stationary. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Equilibrium of forces on a resting body.\n\n**Step 2: Force Balance**: The weight of the book \\(W = mg\\) acts downwards, and the normal reaction \\(N\\) acts upwards. Since \\(N = W\\), the net force \\(F_{\\text{net}} = 0\\), and by Newton\'s 1st law, the book remains at rest.\n\n**Step 3: Conclusion**: Balanced vertical forces keep it stationary. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'When a tree branch is shaken vigorously, leaves and ripe fruits detach and fall down. This happens because:',
    options: [
      'The branch comes into rapid motion, but the fruits remain at rest due to inertia of rest, breaking the connecting stems',
      'The branch exerts an electrical charge repelling the fruits',
      'The fruits experience an upward buoyant force from air',
      'The mass of the fruits suddenly increases'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia of rest of the fruit.\n\n**Step 2: Mechanism**: Shaking moves the branch rapidly back and forth. The fruit tends to stay in its original position due to inertia of rest, generating large shear stress at the stem joint and detaching it.\n\n**Step 3: Conclusion**: Inertia of rest breaks the attachment. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia of rest of the fruit.\n\n**Step 2: Mechanism**: Shaking moves the branch rapidly back and forth. The fruit tends to stay in its original position due to inertia of rest, generating large shear stress at the stem joint and detaching it.\n\n**Step 3: Conclusion**: Inertia of rest breaks the attachment. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'Why is it dangerous to jump off a rapidly moving train or bus?',
    options: [
      'The feet stop upon touching the ground, while the upper body continues moving forward at the bus\'s speed due to inertia of motion, causing a violent fall',
      'The earth\'s rotation creates a sudden lateral force',
      'Air friction instantly pulls the person backwards',
      'The bus\'s magnetic field pulls the person towards the wheels'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inertia of motion preserves forward speed.\n\n**Step 2: Mechanism**: A passenger on a bus shares its forward velocity. When jumping off, feet are brought to an abrupt stop by friction with the ground, while the torso continues forward with high speed, leading to tumbling and injury.\n\n**Step 3: Conclusion**: Inertia of motion causes the fall. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inertia of motion preserves forward speed.\n\n**Step 2: Mechanism**: A passenger on a bus shares its forward velocity. When jumping off, feet are brought to an abrupt stop by friction with the ground, while the torso continues forward with high speed, leading to tumbling and injury.\n\n**Step 3: Conclusion**: Inertia of motion causes the fall. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.1',
    type: 'OSC',
    text: 'A spark flying off a grinding stone when sharpening an iron blade travels in which direction?',
    options: [
      'Tangential to the grinding wheel at the contact point due to inertia of direction',
      'Radially toward the axle of the grinding wheel',
      'In a complete circle around the wheel',
      'Directly opposite to the operator\'s view'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Incandescent particles severed from the metal move with the instantaneous velocity of the wheel surface.\n\n**Step 2: Analysis**: Since linear velocity in circular motion is strictly tangential, once detached, inertia of direction carries the spark in a straight line along the tangent.\n\n**Step 3: Conclusion**: Sparks fly tangentially. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Incandescent particles severed from the metal move with the instantaneous velocity of the wheel surface.\n\n**Step 2: Analysis**: Since linear velocity in circular motion is strictly tangential, once detached, inertia of direction carries the spark in a straight line along the tangent.\n\n**Step 3: Conclusion**: Sparks fly tangentially. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.6.2 (13 Questions: Second law - F = ma) ---
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'What horizontal force is required to accelerate a body of mass \\(5\\text{ kg}\\) at \\(3\\text{ m/s}^2\\) on a frictionless surface?',
    options: [
      '\\(15\\text{ N}\\)',
      '\\(1.67\\text{ N}\\)',
      '\\(8\\text{ N}\\)',
      '\\(45\\text{ N}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Second Law states \\(F = m a\\).\n\n**Step 2: Calculation**: \\(m = 5\\text{ kg}\\), \\(a = 3\\text{ m/s}^2\\). \\(F = 5 \\times 3 = 15\\text{ N}\\).\n\n**Step 3: Conclusion**: The required force is \\(15\\text{ N}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Second Law states \\(F = m a\\).\n\n**Step 2: Calculation**: \\(m = 5\\text{ kg}\\), \\(a = 3\\text{ m/s}^2\\). \\(F = 5 \\times 3 = 15\\text{ N}\\).\n\n**Step 3: Conclusion**: The required force is \\(15\\text{ N}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'How is momentum (\\(p\\)) defined in physics, and what is its SI unit?',
    options: [
      'Product of mass and velocity (\\(p = m v\\)); SI unit is \\(\\text{kg}\\cdot\\text{m/s}\\)',
      'Product of mass and acceleration (\\(p = m a\\)); SI unit is \\(\\text{N}\\)',
      'Work divided by time (\\(p = W/t\\)); SI unit is \\(\\text{Watt}\\)',
      'Force times distance (\\(p = F s\\)); SI unit is \\(\\text{Joule}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Linear momentum is the quantity of motion contained in a body.\n\n**Step 2: Formula & Unit**: \\(p = m \\times v\\). Mass is in \\(\\text{kg}\\) and velocity is in \\(\\text{m/s}\\), so the unit is \\(\\text{kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: Momentum is \\(p = mv\\) with unit \\(\\text{kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Linear momentum is the quantity of motion contained in a body.\n\n**Step 2: Formula & Unit**: \\(p = m \\times v\\). Mass is in \\(\\text{kg}\\) and velocity is in \\(\\text{m/s}\\), so the unit is \\(\\text{kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: Momentum is \\(p = mv\\) with unit \\(\\text{kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A net constant force of \\(20\\text{ N}\\) acts on an object of mass \\(4\\text{ kg}\\) initially at rest for \\(5\\text{ s}\\). What is the final momentum acquired by the object?',
    options: [
      '\\(100\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(25\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(400\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(80\\text{ kg}\\cdot\\text{m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: By Newton\'s 2nd Law, \\(F = \\frac{\\Delta p}{\\Delta t} \\implies \\Delta p = F \\times \\Delta t\\).\n\n**Step 2: Calculation**: Impulse \\(J = F \\times t = 20 \\times 5 = 100\\text{ N}\\cdot\\text{s} = 100\\text{ kg}\\cdot\\text{m/s}\\). Since initial momentum is 0, final momentum \\(p = 100\\text{ kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: The final momentum is \\(100\\text{ kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: By Newton\'s 2nd Law, \\(F = \\frac{\\Delta p}{\\Delta t} \\implies \\Delta p = F \\times \\Delta t\\).\n\n**Step 2: Calculation**: Impulse \\(J = F \\times t = 20 \\times 5 = 100\\text{ N}\\cdot\\text{s} = 100\\text{ kg}\\cdot\\text{m/s}\\). Since initial momentum is 0, final momentum \\(p = 100\\text{ kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: The final momentum is \\(100\\text{ kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'What is the relationship between the SI unit Newton (\\(\\text{N}\\)) and the CGS unit Dyne?',
    options: [
      '\\(1\\text{ N} = 10^5\\text{ dynes}\\)',
      '\\(1\\text{ N} = 10^3\\text{ dynes}\\)',
      '\\(1\\text{ N} = 10^7\\text{ dynes}\\)',
      '\\(1\\text{ N} = 10^2\\text{ dynes}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(1\\text{ N} = 1\\text{ kg} \\times 1\\text{ m/s}^2\\).\n\n**Step 2: Conversion**: \\(1\\text{ kg} = 1000\\text{ g} = 10^3\\text{ g}\\) and \\(1\\text{ m/s}^2 = 100\\text{ cm/s}^2 = 10^2\\text{ cm/s}^2\\). Therefore, \\(1\\text{ N} = (10^3\\text{ g}) \\times (10^2\\text{ cm/s}^2) = 10^5\\text{ g}\\cdot\\text{cm/s}^2 = 10^5\\text{ dynes}\\).\n\n**Step 3: Conclusion**: \\(1\\text{ N} = 10^5\\text{ dynes}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(1\\text{ N} = 1\\text{ kg} \\times 1\\text{ m/s}^2\\).\n\n**Step 2: Conversion**: \\(1\\text{ kg} = 1000\\text{ g} = 10^3\\text{ g}\\) and \\(1\\text{ m/s}^2 = 100\\text{ cm/s}^2 = 10^2\\text{ cm/s}^2\\). Therefore, \\(1\\text{ N} = (10^3\\text{ g}) \\times (10^2\\text{ cm/s}^2) = 10^5\\text{ g}\\cdot\\text{cm/s}^2 = 10^5\\text{ dynes}\\).\n\n**Step 3: Conclusion**: \\(1\\text{ N} = 10^5\\text{ dynes}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A fielder in a cricket match pulls their hands backward while catching a fast-moving cricket ball. Why does the fielder do this?',
    options: [
      'To increase the impact time, thereby reducing the rate of change of momentum and the force exerted on the hands',
      'To increase the force with which the ball hits the hand',
      'To reduce the mass of the ball',
      'To look stylish on the field'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Force is the rate of change of momentum: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: By pulling hands backward, the stopping time \\(\\Delta t\\) is increased. For a fixed momentum change \\(\\Delta p\\), increasing \\(\\Delta t\\) dramatically reduces the stopping force \\(F\\), preventing hand injury.\n\n**Step 3: Conclusion**: Longer time lowers the impact force. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Force is the rate of change of momentum: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: By pulling hands backward, the stopping time \\(\\Delta t\\) is increased. For a fixed momentum change \\(\\Delta p\\), increasing \\(\\Delta t\\) dramatically reduces the stopping force \\(F\\), preventing hand injury.\n\n**Step 3: Conclusion**: Longer time lowers the impact force. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A force of \\(10\\text{ N}\\) gives a mass \\(m_1\\) an acceleration of \\(20\\text{ m/s}^2\\) and a mass \\(m_2\\) an acceleration of \\(5\\text{ m/s}^2\\). What acceleration would this same force produce if both masses are tied together?',
    options: [
      '\\(4\\text{ m/s}^2\\)',
      '\\(2.5\\text{ m/s}^2\\)',
      '\\(12.5\\text{ m/s}^2\\)',
      '\\(8\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(m = \\frac{F}{a}\\).\n\n**Step 2: Calculation**: \\(m_1 = \\frac{10}{20} = 0.5\\text{ kg}\\). \\(m_2 = \\frac{10}{5} = 2.0\\text{ kg}\\). Total mass \\(M = m_1 + m_2 = 0.5 + 2.0 = 2.5\\text{ kg}\\). Combined acceleration \\(a = \\frac{F}{M} = \\frac{10}{2.5} = 4\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The combined acceleration is \\(4\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(m = \\frac{F}{a}\\).\n\n**Step 2: Calculation**: \\(m_1 = \\frac{10}{20} = 0.5\\text{ kg}\\). \\(m_2 = \\frac{10}{5} = 2.0\\text{ kg}\\). Total mass \\(M = m_1 + m_2 = 0.5 + 2.0 = 2.5\\text{ kg}\\). Combined acceleration \\(a = \\frac{F}{M} = \\frac{10}{2.5} = 4\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The combined acceleration is \\(4\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'Which requires a greater force: accelerating a \\(2\\text{ kg}\\) mass at \\(5\\text{ m/s}^2\\) or a \\(4\\text{ kg}\\) mass at \\(2\\text{ m/s}^2\\)?',
    options: [
      'Accelerating the \\(2\\text{ kg}\\) mass at \\(5\\text{ m/s}^2\\) (requires \\(10\\text{ N}\\) vs \\(8\\text{ N}\\))',
      'Accelerating the \\(4\\text{ kg}\\) mass at \\(2\\text{ m/s}^2\\) (requires \\(12\\text{ N}\\))',
      'Both require exactly the same force',
      'Neither requires any force because both are in motion'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(F = m a\\).\n\n**Step 2: Calculation**: For 1st case: \\(F_1 = 2 \\times 5 = 10\\text{ N}\\). For 2nd case: \\(F_2 = 4 \\times 2 = 8\\text{ N}\\). Since \\(10\\text{ N} > 8\\text{ N}\\), the 1st case requires greater force.\n\n**Step 3: Conclusion**: The \\(2\\text{ kg}\\) mass at \\(5\\text{ m/s}^2\\) requires more force. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(F = m a\\).\n\n**Step 2: Calculation**: For 1st case: \\(F_1 = 2 \\times 5 = 10\\text{ N}\\). For 2nd case: \\(F_2 = 4 \\times 2 = 8\\text{ N}\\). Since \\(10\\text{ N} > 8\\text{ N}\\), the 1st case requires greater force.\n\n**Step 3: Conclusion**: The \\(2\\text{ kg}\\) mass at \\(5\\text{ m/s}^2\\) requires more force. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A vehicle of mass \\(1200\\text{ kg}\\) moving at \\(20\\text{ m/s}\\) is brought to rest in \\(4\\text{ s}\\) by applying brakes. What is the magnitude of the average braking force?',
    options: [
      '\\(6000\\text{ N}\\)',
      '\\(12000\\text{ N}\\)',
      '\\(3000\\text{ N}\\)',
      '\\(2400\\text{ N}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(F = m \\times \\frac{v - u}{t}\\).\n\n**Step 2: Calculation**: \\(u = 20\\text{ m/s}\\), \\(v = 0\\text{ m/s}\\), \\(t = 4\\text{ s}\\). \\(a = \\frac{0 - 20}{4} = -5\\text{ m/s}^2\\). Force magnitude \\(F = m |a| = 1200 \\times 5 = 6000\\text{ N}\\).\n\n**Step 3: Conclusion**: The braking force is \\(6000\\text{ N}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(F = m \\times \\frac{v - u}{t}\\).\n\n**Step 2: Calculation**: \\(u = 20\\text{ m/s}\\), \\(v = 0\\text{ m/s}\\), \\(t = 4\\text{ s}\\). \\(a = \\frac{0 - 20}{4} = -5\\text{ m/s}^2\\). Force magnitude \\(F = m |a| = 1200 \\times 5 = 6000\\text{ N}\\).\n\n**Step 3: Conclusion**: The braking force is \\(6000\\text{ N}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'What happens to the acceleration of an object if the applied force is doubled while its mass is halved?',
    options: [
      'The acceleration increases by 4 times',
      'The acceleration is doubled',
      'The acceleration remains unchanged',
      'The acceleration is halved'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(a = \\frac{F}{m}\\).\n\n**Step 2: Calculation**: If \\(F\' = 2F\\) and \\(m\' = \\frac{m}{2}\\), then \\(a\' = \\frac{2F}{m/2} = 4 \\frac{F}{m} = 4a\\).\n\n**Step 3: Conclusion**: The acceleration increases by 4 times. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(a = \\frac{F}{m}\\).\n\n**Step 2: Calculation**: If \\(F\' = 2F\\) and \\(m\' = \\frac{m}{2}\\), then \\(a\' = \\frac{2F}{m/2} = 4 \\frac{F}{m} = 4a\\).\n\n**Step 3: Conclusion**: The acceleration increases by 4 times. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'Why are cars fitted with seat belts and crumple zones according to the principles of Newton\'s Second Law?',
    options: [
      'They increase the duration of impact during a collision, thereby dramatically decreasing the deceleration and the retarding force on occupants',
      'They prevent the car from rolling over backwards',
      'They absorb engine oil during crashes',
      'They increase the car\'s mass and momentum'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: Crumple zones collapse progressively, and seat belts stretch slightly. This elongates the stopping time \\(\\Delta t\\). As \\(\\Delta t\\) increases, the impact force \\(F\\) delivered to passenger bodies decreases proportionally, saving lives.\n\n**Step 3: Conclusion**: Increasing impact time lowers force. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: Crumple zones collapse progressively, and seat belts stretch slightly. This elongates the stopping time \\(\\Delta t\\). As \\(\\Delta t\\) increases, the impact force \\(F\\) delivered to passenger bodies decreases proportionally, saving lives.\n\n**Step 3: Conclusion**: Increasing impact time lowers force. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A \\(50\\text{ g}\\) golf ball at rest is struck with a club, leaving with a speed of \\(80\\text{ m/s}\\). If the club was in contact with the ball for \\(0.001\\text{ s}\\), what average force was exerted on the ball?',
    options: [
      '\\(4000\\text{ N}\\)',
      '\\(2000\\text{ N}\\)',
      '\\(400\\text{ N}\\)',
      '\\(8000\\text{ N}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(F = \\frac{m(v - u)}{\\Delta t}\\).\n\n**Step 2: Calculation**: \\(m = 50\\text{ g} = 0.05\\text{ kg}\\), \\(u = 0\\), \\(v = 80\\text{ m/s}\\), \\(\\Delta t = 0.001\\text{ s}\\). Change in momentum \\(\\Delta p = 0.05 \\times 80 = 4\\text{ kg}\\cdot\\text{m/s}\\). Force \\(F = \\frac{4}{0.001} = 4000\\text{ N}\\).\n\n**Step 3: Conclusion**: The average force is \\(4000\\text{ N}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(F = \\frac{m(v - u)}{\\Delta t}\\).\n\n**Step 2: Calculation**: \\(m = 50\\text{ g} = 0.05\\text{ kg}\\), \\(u = 0\\), \\(v = 80\\text{ m/s}\\), \\(\\Delta t = 0.001\\text{ s}\\). Change in momentum \\(\\Delta p = 0.05 \\times 80 = 4\\text{ kg}\\cdot\\text{m/s}\\). Force \\(F = \\frac{4}{0.001} = 4000\\text{ N}\\).\n\n**Step 3: Conclusion**: The average force is \\(4000\\text{ N}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'Newton\'s First Law of Motion can be mathematically derived from Newton\'s Second Law under what condition?',
    options: [
      'When net external force \\(F = 0\\), then \\(ma = 0 \\implies a = 0\\), meaning velocity remains constant',
      'When mass \\(m = 0\\)',
      'When momentum is infinite',
      'When speed of light is reached'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Second Law is \\(F = ma\\).\n\n**Step 2: Derivation**: If no net external force acts (\\(F = 0\\)), then \\(ma = 0\\). Since mass \\(m \\neq 0\\), acceleration \\(a = 0\\). Zero acceleration means \\(v = u\\) (state of rest or uniform rectilinear motion is maintained indefinitely).\n\n**Step 3: Conclusion**: First law is a special case of the second law when \\(F = 0\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Second Law is \\(F = ma\\).\n\n**Step 2: Derivation**: If no net external force acts (\\(F = 0\\)), then \\(ma = 0\\). Since mass \\(m \\neq 0\\), acceleration \\(a = 0\\). Zero acceleration means \\(v = u\\) (state of rest or uniform rectilinear motion is maintained indefinitely).\n\n**Step 3: Conclusion**: First law is a special case of the second law when \\(F = 0\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.2',
    type: 'OSC',
    text: 'A karate player can break a pile of tiles with a single blow of their hand because:',
    options: [
      'The strike is delivered with very high speed in an extremely short time interval, delivering an enormous impact force',
      'The player\'s hand mass is larger than the tiles',
      'The tiles are heated prior to striking',
      'Gravity pulls the hand down with double acceleration'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Impulse and force relation: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: By bringing the hand to rest in an extraordinarily short time \\(\\Delta t\\) (fractions of a millisecond), the entire momentum is transferred almost instantaneously, generating a massive impulse force exceeding the breaking stress of the tiles.\n\n**Step 3: Conclusion**: Extremely small impact time creates enormous breaking force. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Impulse and force relation: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n\n**Step 2: Mechanism**: By bringing the hand to rest in an extraordinarily short time \\(\\Delta t\\) (fractions of a millisecond), the entire momentum is transferred almost instantaneously, generating a massive impulse force exceeding the breaking stress of the tiles.\n\n**Step 3: Conclusion**: Extremely small impact time creates enormous breaking force. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.6.3 (13 Questions: Third law - Action and Reaction) ---
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'Newton\'s Third Law states that "To every action there is an equal and opposite reaction." Why do action and reaction forces NEVER cancel each other out?',
    options: [
      'Because action and reaction forces act simultaneously on two different bodies',
      'Because action is always larger in magnitude than reaction',
      'Because reaction occurs after a measurable time delay',
      'Because action is a scalar while reaction is a vector'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Forces cancel out if and only if they are equal, opposite, and act on the *same* body.\n\n**Step 2: Newton\'s 3rd Law Distinction**: If body \\(A\\) exerts a force on body \\(B\\) (action), body \\(B\\) exerts an equal and opposite force on body \\(A\\) (reaction). Because the two forces act on two entirely distinct bodies, they cannot cancel each other out.\n\n**Step 3: Conclusion**: They act on different bodies. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Forces cancel out if and only if they are equal, opposite, and act on the *same* body.\n\n**Step 2: Newton\'s 3rd Law Distinction**: If body \\(A\\) exerts a force on body \\(B\\) (action), body \\(B\\) exerts an equal and opposite force on body \\(A\\) (reaction). Because the two forces act on two entirely distinct bodies, they cannot cancel each other out.\n\n**Step 3: Conclusion**: They act on different bodies. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'When a person walks forward on the ground, which force directly propels the person forward?',
    options: [
      'The forward reaction force exerted by the ground on the person\'s feet',
      'The backward muscular force exerted by the feet on the ground',
      'The downward gravitational pull of the Earth',
      'The air resistance pushing from behind'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action and reaction pair during walking.\n\n**Step 2: Analysis**: The person\'s foot pushes the ground backward and downward (Action). In reaction, the ground pushes the person\'s foot forward and upward with an equal force (Reaction). It is this forward force from the ground that propels the body.\n\n**Step 3: Conclusion**: Ground reaction propels the person forward. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action and reaction pair during walking.\n\n**Step 2: Analysis**: The person\'s foot pushes the ground backward and downward (Action). In reaction, the ground pushes the person\'s foot forward and upward with an equal force (Reaction). It is this forward force from the ground that propels the body.\n\n**Step 3: Conclusion**: Ground reaction propels the person forward. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'A swimmer pushes water backwards with their hands and legs. What moves the swimmer forward in the pool?',
    options: [
      'The forward reaction force exerted by the water on the swimmer\'s body',
      'The buoyant force of the water alone',
      'The surface tension of the water',
      'The swimmer\'s weight pulling them horizontally'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Third Law in fluids.\n\n**Step 2: Mechanism**: Swimmer pushes water backwards (Action). Water pushes the swimmer forward with equal and opposite force (Reaction).\n\n**Step 3: Conclusion**: Reaction of water propels the swimmer forward. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Third Law in fluids.\n\n**Step 2: Mechanism**: Swimmer pushes water backwards (Action). Water pushes the swimmer forward with equal and opposite force (Reaction).\n\n**Step 3: Conclusion**: Reaction of water propels the swimmer forward. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'How does a rocket accelerate in the vacuum of outer space where there is no air to push against?',
    options: [
      'By ejecting hot exhaust gases downward at high speed (Action), which exerts an upward thrust reaction on the rocket',
      'By pushing against the gravitational field of distant stars',
      'By using solar radiation pressure exclusively',
      'Rockets cannot accelerate in a vacuum'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Rocket propulsion relies on action-reaction and conservation of momentum.\n\n**Step 2: Mechanism**: Burning propellant produces hot gas expelled rearward at supersonic speeds (Action). The escaping gas exerts an equal and opposite forward thrust on the rocket nozzle (Reaction), completely independent of atmospheric air.\n\n**Step 3: Conclusion**: Gas expulsion reaction propels the rocket. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Rocket propulsion relies on action-reaction and conservation of momentum.\n\n**Step 2: Mechanism**: Burning propellant produces hot gas expelled rearward at supersonic speeds (Action). The escaping gas exerts an equal and opposite forward thrust on the rocket nozzle (Reaction), completely independent of atmospheric air.\n\n**Step 3: Conclusion**: Gas expulsion reaction propels the rocket. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'When a bird flies, it flaps its wings downwards and backwards. What enables the bird to lift and move forward?',
    options: [
      'The air pushes the wings upwards and forwards as a reaction force',
      'The bird becomes weightless while flapping',
      'The Earth\'s magnetic field pulls the feathers upward',
      'The bird is sucked upward by atmospheric low pressure'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action-reaction in aerodynamics.\n\n**Step 2: Mechanism**: Flapping pushes air downwards and backwards (Action). By Newton\'s Third Law, the air exerts an equal and opposite reaction force upwards and forwards on the wings, providing lift and propulsion.\n\n**Step 3: Conclusion**: Reaction of air provides lift and thrust. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action-reaction in aerodynamics.\n\n**Step 2: Mechanism**: Flapping pushes air downwards and backwards (Action). By Newton\'s Third Law, the air exerts an equal and opposite reaction force upwards and forwards on the wings, providing lift and propulsion.\n\n**Step 3: Conclusion**: Reaction of air provides lift and thrust. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'When a boatman steps forward onto the bank of a river, the boat tends to move backwards into the water. Why?',
    options: [
      'The boatman pushes the boat backward with his feet (Action) to gain forward propulsion (Reaction)',
      'Water currents always push empty boats backward',
      'The boat loses its buoyancy when vacated',
      'The earth pushes the boat away'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action-reaction pair between person and boat.\n\n**Step 2: Mechanism**: To leap forward, the boatman applies a backward force on the boat with his feet (Action). The boat exerts a forward reaction on him. Since the boat floats freely on water with low resistance, it moves backward.\n\n**Step 3: Conclusion**: The backward action moves the boat. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action-reaction pair between person and boat.\n\n**Step 2: Mechanism**: To leap forward, the boatman applies a backward force on the boat with his feet (Action). The boat exerts a forward reaction on him. Since the boat floats freely on water with low resistance, it moves backward.\n\n**Step 3: Conclusion**: The backward action moves the boat. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'If a massive truck and a light passenger car collide head-on, how does the force exerted by the truck on the car compare to the force exerted by the car on the truck?',
    options: [
      'Both forces are strictly equal in magnitude and opposite in direction',
      'The truck exerts a much larger force on the car because of its greater mass',
      'The car exerts a larger force because it gets damaged more',
      'The forces depend entirely on which vehicle was travelling faster'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Third Law states \\(|F_{AB}| = |F_{BA}|\\) under all conditions, irrespective of mass or velocity.\n\n**Step 2: Clarification**: While both forces are strictly equal, the *acceleration* (\\(a = \\frac{F}{m}\\)) of the car is much greater due to its smaller mass, resulting in far more severe deformation and deceleration.\n\n**Step 3: Conclusion**: The forces are strictly equal in magnitude. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Third Law states \\(|F_{AB}| = |F_{BA}|\\) under all conditions, irrespective of mass or velocity.\n\n**Step 2: Clarification**: While both forces are strictly equal, the *acceleration* (\\(a = \\frac{F}{m}\\)) of the car is much greater due to its smaller mass, resulting in far more severe deformation and deceleration.\n\n**Step 3: Conclusion**: The forces are strictly equal in magnitude. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'A horse pulls a cart forward. According to Newton\'s Third Law, the cart pulls back on the horse with an equal force. How is the horse-cart system able to accelerate forward?',
    options: [
      'The forward force exerted by the ground on the horse\'s hooves exceeds the backward frictional force on the cart wheels',
      'The horse pulls on the cart before the cart has time to pull back',
      'The horse\'s mass is larger than the cart\'s mass',
      'Action and reaction forces do not apply to living animals'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Consider the system of (Horse + Cart) as a single whole.\n\n**Step 2: External Force Analysis**: The internal force between horse and cart cancels out. The external horizontal forces are: (1) Forward friction on horse hooves from ground \\(F_H\\), and (2) Backward rolling friction on wheels \\(f_C\\). When \\(F_H > f_C\\), there is a net forward external force, causing the system to accelerate.\n\n**Step 3: Conclusion**: Net external ground reaction accelerates the system. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Consider the system of (Horse + Cart) as a single whole.\n\n**Step 2: External Force Analysis**: The internal force between horse and cart cancels out. The external horizontal forces are: (1) Forward friction on horse hooves from ground \\(F_H\\), and (2) Backward rolling friction on wheels \\(f_C\\). When \\(F_H > f_C\\), there is a net forward external force, causing the system to accelerate.\n\n**Step 3: Conclusion**: Net external ground reaction accelerates the system. Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'When an inflated balloon is released without tying its mouth, it darts rapidly forward while air rushes out of the neck. Which law of motion directly explains this?',
    options: [
      'Newton\'s Third Law of Motion',
      'Newton\'s Law of Gravitation',
      'Boyle\'s Law',
      'Archimedes\' Principle'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action and reaction.\n\n**Step 2: Mechanism**: Escaping compressed air rushes backward (Action). The air pushes the balloon forward with an equal and opposite force (Reaction).\n\n**Step 3: Conclusion**: Newton\'s Third Law governs this motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action and reaction.\n\n**Step 2: Mechanism**: Escaping compressed air rushes backward (Action). The air pushes the balloon forward with an equal and opposite force (Reaction).\n\n**Step 3: Conclusion**: Newton\'s Third Law governs this motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'Why does a firefighter have to hold a hose pipe firmly when water rushes out of the nozzle at high speed?',
    options: [
      'The backward reaction force exerted by the escaping water stream pushes the nozzle backward',
      'The hose becomes extremely heavy due to water weight',
      'Water creates a suction pulling the hose forward',
      'The hose expands and shocks the firefighter\'s hands'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Reaction force of high-velocity fluid discharge.\n\n**Step 2: Mechanism**: Water is accelerated out of the nozzle forward at high speed and volume (Action). The water exerts an equal and opposite backward thrust on the nozzle (Reaction), requiring strong muscular force to hold it steady.\n\n**Step 3: Conclusion**: Backward reaction force pushes the hose back. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Reaction force of high-velocity fluid discharge.\n\n**Step 2: Mechanism**: Water is accelerated out of the nozzle forward at high speed and volume (Action). The water exerts an equal and opposite backward thrust on the nozzle (Reaction), requiring strong muscular force to hold it steady.\n\n**Step 3: Conclusion**: Backward reaction force pushes the hose back. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'A person standing on roller skates pushes firmly against a wall. What happens to the person?',
    options: [
      'The person rolls backwards away from the wall due to the wall\'s reaction force',
      'The person remains stationary because the wall does not move',
      'The person falls down forward',
      'The wall moves backwards while the person remains at rest'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action-reaction on low-friction support.\n\n**Step 2: Mechanism**: The person pushes against the wall (Action). The wall pushes the person back with an equal force (Reaction). Since roller skates have very little friction, this reaction force accelerates the person backwards.\n\n**Step 3: Conclusion**: The wall pushes the person backward. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action-reaction on low-friction support.\n\n**Step 2: Mechanism**: The person pushes against the wall (Action). The wall pushes the person back with an equal force (Reaction). Since roller skates have very little friction, this reaction force accelerates the person backwards.\n\n**Step 3: Conclusion**: The wall pushes the person backward. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'Which of the following statements about Newton\'s Third Law is FALSE?',
    options: [
      'Action occurs first, and after a brief latency, the reaction follows',
      'Action and reaction forces are strictly simultaneous',
      'Action and reaction always act on two different objects',
      'Action and reaction are always equal in magnitude and opposite in direction'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Action and reaction are mutual interactions that exist concurrently.\n\n**Step 2: Clarification**: There is zero time delay between action and reaction; they arise at the exact same instant. Neither force is the "cause" of the other; both are parts of a single mutual interaction.\n\n**Step 3: Conclusion**: Statement A is false and thus the correct answer. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Action and reaction are mutual interactions that exist concurrently.\n\n**Step 2: Clarification**: There is zero time delay between action and reaction; they arise at the exact same instant. Neither force is the "cause" of the other; both are parts of a single mutual interaction.\n\n**Step 3: Conclusion**: Statement A is false and thus the correct answer. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.3',
    type: 'OSC',
    text: 'When you hit a wooden table with your fist, your hand hurts. Why?',
    options: [
      'The table exerts an equal and opposite reaction force on your hand',
      'The table absorbs your hand\'s energy and transforms it into electricity',
      'Your fist creates a vacuum inside the wood',
      'Frictional force burns your skin'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Third Law.\n\n**Step 2: Mechanism**: Your hand exerts a force on the table (Action). Simultaneously, the table exerts an equal and opposite normal force on your hand (Reaction), compressing your tissues and causing pain.\n\n**Step 3: Conclusion**: The table\'s reaction force hurts your hand. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Third Law.\n\n**Step 2: Mechanism**: Your hand exerts a force on the table (Action). Simultaneously, the table exerts an equal and opposite normal force on your hand (Reaction), compressing your tissues and causing pain.\n\n**Step 3: Conclusion**: The table\'s reaction force hurts your hand. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.6.4 (13 Questions: Conservation of momentum m1u1 + m2u2 = m1v1 + m2v2) ---
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'Under what fundamental condition is the total linear momentum of an interacting system of bodies strictly conserved?',
    options: [
      'When no external unbalanced force acts on the system',
      'When the collision is completely frictionless and elastic',
      'When both colliding bodies have identical masses',
      'When the temperature of the system remains constant'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Law of Conservation of Momentum.\n\n**Step 2: Condition**: \\(\\frac{d\\vec{P}}{dt} = \\vec{F}_{\\text{ext}}\\). If \\(\\vec{F}_{\\text{ext}} = 0\\), then \\(\\vec{P} = \\text{constant}\\). Total linear momentum is conserved in any collision (elastic or inelastic) as long as net external force is zero.\n\n**Step 3: Conclusion**: Absence of external unbalanced force is the required condition. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Law of Conservation of Momentum.\n\n**Step 2: Condition**: \\(\\frac{d\\vec{P}}{dt} = \\vec{F}_{\\text{ext}}\\). If \\(\\vec{F}_{\\text{ext}} = 0\\), then \\(\\vec{P} = \\text{constant}\\). Total linear momentum is conserved in any collision (elastic or inelastic) as long as net external force is zero.\n\n**Step 3: Conclusion**: Absence of external unbalanced force is the required condition. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A ball \\(A\\) of mass \\(2\\text{ kg}\\) moving at \\(6\\text{ m/s}\\) collides head-on with a stationary ball \\(B\\) of mass \\(4\\text{ kg}\\). After the collision, ball \\(A\\) comes to rest. What is the velocity of ball \\(B\\) after collision?',
    options: [
      '\\(3\\text{ m/s}\\)',
      '\\(6\\text{ m/s}\\)',
      '\\(1.5\\text{ m/s}\\)',
      '\\(12\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n\n**Step 2: Calculation**: \\(m_1 = 2\\text{ kg}, u_1 = 6\\text{ m/s}\\). \\(m_2 = 4\\text{ kg}, u_2 = 0\\). \\(v_1 = 0\\). Total initial momentum \\(= 2 \\times 6 + 4 \\times 0 = 12\\text{ kg}\\cdot\\text{m/s}\\). Total final momentum \\(= 2(0) + 4(v_2) = 4 v_2\\). \\(4 v_2 = 12 \\implies v_2 = 3\\text{ m/s}\\).\n\n**Step 3: Conclusion**: Ball \\(B\\) moves at \\(3\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n\n**Step 2: Calculation**: \\(m_1 = 2\\text{ kg}, u_1 = 6\\text{ m/s}\\). \\(m_2 = 4\\text{ kg}, u_2 = 0\\). \\(v_1 = 0\\). Total initial momentum \\(= 2 \\times 6 + 4 \\times 0 = 12\\text{ kg}\\cdot\\text{m/s}\\). Total final momentum \\(= 2(0) + 4(v_2) = 4 v_2\\). \\(4 v_2 = 12 \\implies v_2 = 3\\text{ m/s}\\).\n\n**Step 3: Conclusion**: Ball \\(B\\) moves at \\(3\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'Two skaters of masses \\(50\\text{ kg}\\) and \\(70\\text{ kg}\\) stand facing each other on frictionless ice. The \\(50\\text{ kg}\\) skater pushes the \\(70\\text{ kg}\\) skater away such that the \\(70\\text{ kg}\\) skater moves at \\(2.5\\text{ m/s}\\). What is the recoil velocity of the \\(50\\text{ kg}\\) skater?',
    options: [
      '\\(-3.5\\text{ m/s}\\) (in the opposite direction)',
      '\\(+3.5\\text{ m/s}\\)',
      '\\(-2.5\\text{ m/s}\\)',
      '\\(-1.78\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Initial momentum of system at rest is 0. By conservation of momentum, \\(m_1 v_1 + m_2 v_2 = 0\\).\n\n**Step 2: Calculation**: \\(50 v_1 + 70(2.5) = 0 \\implies 50 v_1 + 175 = 0 \\implies v_1 = -\\frac{175}{50} = -3.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The skater recoils at \\(3.5\\text{ m/s}\\) in the opposite direction. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Initial momentum of system at rest is 0. By conservation of momentum, \\(m_1 v_1 + m_2 v_2 = 0\\).\n\n**Step 2: Calculation**: \\(50 v_1 + 70(2.5) = 0 \\implies 50 v_1 + 175 = 0 \\implies v_1 = -\\frac{175}{50} = -3.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The skater recoils at \\(3.5\\text{ m/s}\\) in the opposite direction. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A truck of mass \\(3000\\text{ kg}\\) moving at \\(10\\text{ m/s}\\) collides with a stationary car of mass \\(1000\\text{ kg}\\). After the collision, both vehicles lock bumpers and move together. What is their common velocity?',
    options: [
      '\\(7.5\\text{ m/s}\\)',
      '\\(5.0\\text{ m/s}\\)',
      '\\(10.0\\text{ m/s}\\)',
      '\\(2.5\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Inelastic collision: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: \\(3000(10) + 1000(0) = (3000 + 1000) v \\implies 30000 = 4000 v \\implies v = \\frac{30000}{4000} = 7.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The combined velocity is \\(7.5\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Inelastic collision: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: \\(3000(10) + 1000(0) = (3000 + 1000) v \\implies 30000 = 4000 v \\implies v = \\frac{30000}{4000} = 7.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The combined velocity is \\(7.5\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'Two identical spheres of mass \\(m\\) travel towards each other at equal speeds \\(v\\) on a frictionless surface and collide head-on elastically. What are their velocities after the collision?',
    options: [
      'They rebound with their velocities reversed (each moving backward at speed \\(v\\))',
      'Both spheres stick together and stop dead',
      'Both spheres continue in the same direction at speed \\(2v\\)',
      'One sphere stops and the other moves at speed \\(2v\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Total initial momentum is \\(m v + m(-v) = 0\\).\n\n**Step 2: Analysis**: In an elastic collision with equal masses, velocities are exchanged: \\(v_1 = u_2 = -v\\) and \\(v_2 = u_1 = +v\\). Kinetic energy and momentum are both conserved.\n\n**Step 3: Conclusion**: Each sphere rebounds at speed \\(v\\) in the opposite direction. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Total initial momentum is \\(m v + m(-v) = 0\\).\n\n**Step 2: Analysis**: In an elastic collision with equal masses, velocities are exchanged: \\(v_1 = u_2 = -v\\) and \\(v_2 = u_1 = +v\\). Kinetic energy and momentum are both conserved.\n\n**Step 3: Conclusion**: Each sphere rebounds at speed \\(v\\) in the opposite direction. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A bomb of mass \\(9\\text{ kg}\\) initially at rest explodes into two fragments of masses \\(3\\text{ kg}\\) and \\(6\\text{ kg}\\). If the \\(3\\text{ kg}\\) fragment flies off with a velocity of \\(16\\text{ m/s}\\), what is the velocity of the \\(6\\text{ kg}\\) fragment?',
    options: [
      '\\(-8\\text{ m/s}\\) (in the opposite direction)',
      '\\(+8\\text{ m/s}\\)',
      '\\(-16\\text{ m/s}\\)',
      '\\(-4\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Before explosion, bomb was at rest: \\(P_{\\text{initial}} = 0\\). Internal explosion forces conserve momentum.\n\n**Step 2: Calculation**: \\(m_1 v_1 + m_2 v_2 = 0 \\implies 3(16) + 6(v_2) = 0 \\implies 48 + 6 v_2 = 0 \\implies v_2 = -\\frac{48}{6} = -8\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The \\(6\\text{ kg}\\) piece moves in the opposite direction at \\(8\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Before explosion, bomb was at rest: \\(P_{\\text{initial}} = 0\\). Internal explosion forces conserve momentum.\n\n**Step 2: Calculation**: \\(m_1 v_1 + m_2 v_2 = 0 \\implies 3(16) + 6(v_2) = 0 \\implies 48 + 6 v_2 = 0 \\implies v_2 = -\\frac{48}{6} = -8\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The \\(6\\text{ kg}\\) piece moves in the opposite direction at \\(8\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'Which law of motion is directly used alongside Newton\'s Second Law to derive the Law of Conservation of Momentum?',
    options: [
      'Newton\'s Third Law of Motion',
      'Newton\'s First Law of Motion',
      'Law of Conservation of Energy',
      'Hooke\'s Law'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Derivation**: Consider two bodies colliding. \\(F_{12} = -F_{21}\\) by Newton\'s Third Law.\n\n**Step 2: Substitution**: From Second Law, \\(F_{12} = \\frac{m_1(v_1 - u_1)}{\\Delta t}\\) and \\(F_{21} = \\frac{m_2(v_2 - u_2)}{\\Delta t}\\). Equating gives \\(m_1(v_1 - u_1) = -m_2(v_2 - u_2) \\implies m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n\n**Step 3: Conclusion**: Third Law is the essential foundation. Hence, Option A is correct.',
    solution: '**Step 1: Derivation**: Consider two bodies colliding. \\(F_{12} = -F_{21}\\) by Newton\'s Third Law.\n\n**Step 2: Substitution**: From Second Law, \\(F_{12} = \\frac{m_1(v_1 - u_1)}{\\Delta t}\\) and \\(F_{21} = \\frac{m_2(v_2 - u_2)}{\\Delta t}\\). Equating gives \\(m_1(v_1 - u_1) = -m_2(v_2 - u_2) \\implies m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n\n**Step 3: Conclusion**: Third Law is the essential foundation. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A girl of mass \\(40\\text{ kg}\\) jumps with a horizontal velocity of \\(5\\text{ m/s}\\) onto a stationary cart of mass \\(10\\text{ kg}\\) with frictionless wheels. What is her velocity with the cart?',
    options: [
      '\\(4\\text{ m/s}\\)',
      '\\(5\\text{ m/s}\\)',
      '\\(2\\text{ m/s}\\)',
      '\\(2.5\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Conservation of momentum: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: \\(40 \\times 5 + 10 \\times 0 = (40 + 10) v \\implies 200 = 50 v \\implies v = \\frac{200}{50} = 4\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The velocity of girl and cart is \\(4\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Conservation of momentum: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: \\(40 \\times 5 + 10 \\times 0 = (40 + 10) v \\implies 200 = 50 v \\implies v = \\frac{200}{50} = 4\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The velocity of girl and cart is \\(4\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'In any collision between two bodies in an isolated system, which of the following quantities is ALWAYS conserved, even if the collision is completely inelastic?',
    options: [
      'Total linear momentum',
      'Total kinetic energy',
      'Total mechanical potential energy',
      'Temperature of the bodies'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Conservation laws in collisions.\n\n**Step 2: Comparison**: In inelastic collisions, kinetic energy is partially converted into heat, sound, or deformation energy, so kinetic energy is NOT conserved. However, as long as no external force acts, linear momentum is unconditionally conserved in every collision.\n\n**Step 3: Conclusion**: Linear momentum is always conserved. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Conservation laws in collisions.\n\n**Step 2: Comparison**: In inelastic collisions, kinetic energy is partially converted into heat, sound, or deformation energy, so kinetic energy is NOT conserved. However, as long as no external force acts, linear momentum is unconditionally conserved in every collision.\n\n**Step 3: Conclusion**: Linear momentum is always conserved. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A bullet of mass \\(0.02\\text{ kg}\\) travelling at \\(200\\text{ m/s}\\) embeds into a stationary wooden target of mass \\(1.98\\text{ kg}\\). What is the velocity of the combined target and bullet immediately after impact?',
    options: [
      '\\(2\\text{ m/s}\\)',
      '\\(1\\text{ m/s}\\)',
      '\\(4\\text{ m/s}\\)',
      '\\(0.2\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: Total mass \\(M = 0.02 + 1.98 = 2.0\\text{ kg}\\). Initial momentum \\(= 0.02 \\times 200 = 4\\text{ kg}\\cdot\\text{m/s}\\). \\(2.0 v = 4 \\implies v = \\frac{4}{2.0} = 2\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The common velocity is \\(2\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\\).\n\n**Step 2: Calculation**: Total mass \\(M = 0.02 + 1.98 = 2.0\\text{ kg}\\). Initial momentum \\(= 0.02 \\times 200 = 4\\text{ kg}\\cdot\\text{m/s}\\). \\(2.0 v = 4 \\implies v = \\frac{4}{2.0} = 2\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The common velocity is \\(2\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'Two bodies of mass \\(1\\text{ kg}\\) and \\(3\\text{ kg}\\) have equal kinetic energies. What is the ratio of their linear momenta (\\(p_1 : p_2\\))?',
    options: [
      '\\(1 : \\sqrt{3}\\)',
      '\\(1 : 3\\)',
      '\\(3 : 1\\)',
      '\\(\\sqrt{3} : 1\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Kinetic energy and momentum relationship: \\(E_k = \\frac{p^2}{2m} \\implies p = \\sqrt{2m E_k}\\).\n\n**Step 2: Calculation**: Since \\(E_k\\) is equal, \\(p \\propto \\sqrt{m}\\). \\(\\frac{p_1}{p_2} = \\sqrt{\\frac{m_1}{m_2}} = \\sqrt{\\frac{1}{3}} = \\frac{1}{\\sqrt{3}}\\).\n\n**Step 3: Conclusion**: The ratio is \\(1 : \\sqrt{3}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Kinetic energy and momentum relationship: \\(E_k = \\frac{p^2}{2m} \\implies p = \\sqrt{2m E_k}\\).\n\n**Step 2: Calculation**: Since \\(E_k\\) is equal, \\(p \\propto \\sqrt{m}\\). \\(\\frac{p_1}{p_2} = \\sqrt{\\frac{m_1}{m_2}} = \\sqrt{\\frac{1}{3}} = \\frac{1}{\\sqrt{3}}\\).\n\n**Step 3: Conclusion**: The ratio is \\(1 : \\sqrt{3}\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A \\(1000\\text{ kg}\\) car moving at \\(15\\text{ m/s}\\) collides with a stationary \\(2000\\text{ kg}\\) pickup truck. If the car rebounds backwards at \\(5\\text{ m/s}\\), what is the forward velocity of the truck?',
    options: [
      '\\(10\\text{ m/s}\\)',
      '\\(5\\text{ m/s}\\)',
      '\\(7.5\\text{ m/s}\\)',
      '\\(15\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\). Taking forward as positive.\n\n**Step 2: Calculation**: \\(m_1 = 1000, u_1 = +15, v_1 = -5\\). \\(m_2 = 2000, u_2 = 0\\). Initial momentum \\(= 1000(15) = 15000\\text{ kg}\\cdot\\text{m/s}\\). Final momentum \\(= 1000(-5) + 2000 v_2 = -5000 + 2000 v_2\\). \\(15000 = -5000 + 2000 v_2 \\implies 2000 v_2 = 20000 \\implies v_2 = 10\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The truck moves forward at \\(10\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\). Taking forward as positive.\n\n**Step 2: Calculation**: \\(m_1 = 1000, u_1 = +15, v_1 = -5\\). \\(m_2 = 2000, u_2 = 0\\). Initial momentum \\(= 1000(15) = 15000\\text{ kg}\\cdot\\text{m/s}\\). Final momentum \\(= 1000(-5) + 2000 v_2 = -5000 + 2000 v_2\\). \\(15000 = -5000 + 2000 v_2 \\implies 2000 v_2 = 20000 \\implies v_2 = 10\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The truck moves forward at \\(10\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.4',
    type: 'OSC',
    text: 'A stationary nucleus of mass \\(M\\) decays by emitting an alpha particle of mass \\(m\\) with speed \\(v\\). What is the recoil speed of the daughter nucleus?',
    options: [
      '\\(\\frac{m v}{M - m}\\)',
      '\\(\\frac{M v}{m}\\)',
      '\\(\\frac{m v}{M}\\)',
      '\\(v\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Initial momentum is 0. Mass of daughter nucleus is \\(M - m\\).\n\n**Step 2: Calculation**: By conservation of momentum: \\(m v + (M - m) v_d = 0 \\implies v_d = -\\frac{m v}{M - m}\\). Speed magnitude is \\(\\frac{m v}{M - m}\\).\n\n**Step 3: Conclusion**: Recoil speed is \\(\\frac{m v}{M - m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Initial momentum is 0. Mass of daughter nucleus is \\(M - m\\).\n\n**Step 2: Calculation**: By conservation of momentum: \\(m v + (M - m) v_d = 0 \\implies v_d = -\\frac{m v}{M - m}\\). Speed magnitude is \\(\\frac{m v}{M - m}\\).\n\n**Step 3: Conclusion**: Recoil speed is \\(\\frac{m v}{M - m}\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },

  // --- Subtopic 1.6.5 (15 Questions: Recoil of gun) ---
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A bullet of mass \\(20\\text{ g}\\) is fired horizontally from a pistol of mass \\(2\\text{ kg}\\) with a muzzle velocity of \\(150\\text{ m/s}\\). What is the recoil velocity of the pistol?',
    options: [
      '\\(-1.5\\text{ m/s}\\) (backwards)',
      '\\(+1.5\\text{ m/s}\\)',
      '\\(-15\\text{ m/s}\\)',
      '\\(-0.15\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: By conservation of linear momentum: \\(m_{\\text{bullet}} v_{\\text{bullet}} + M_{\\text{gun}} V_{\\text{recoil}} = 0\\).\n\n**Step 2: Calculation**: \\(m = 20\\text{ g} = 0.02\\text{ kg}\\), \\(v = 150\\text{ m/s}\\), \\(M = 2\\text{ kg}\\). \\(0.02 \\times 150 + 2 V = 0 \\implies 3 + 2 V = 0 \\implies V = -\\frac{3}{2} = -1.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The gun recoils backwards at \\(1.5\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: By conservation of linear momentum: \\(m_{\\text{bullet}} v_{\\text{bullet}} + M_{\\text{gun}} V_{\\text{recoil}} = 0\\).\n\n**Step 2: Calculation**: \\(m = 20\\text{ g} = 0.02\\text{ kg}\\), \\(v = 150\\text{ m/s}\\), \\(M = 2\\text{ kg}\\). \\(0.02 \\times 150 + 2 V = 0 \\implies 3 + 2 V = 0 \\implies V = -\\frac{3}{2} = -1.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The gun recoils backwards at \\(1.5\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'Why is the recoil velocity of a rifle substantially smaller than the muzzle velocity of the bullet fired from it?',
    options: [
      'Because the mass of the rifle is much larger than the mass of the bullet (\\(V_{\\text{recoil}} = -\\frac{m}{M} v\\))',
      'Because friction inside the rifle barrel absorbs most of the backward momentum',
      'Because the bullet accelerates after leaving the barrel',
      'Because air resistance stops the rifle from moving'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(M V + m v = 0 \\implies |V| = \\frac{m}{M} v\\).\n\n**Step 2: Analysis**: Since the mass of the rifle \\(M\\) is hundreds of times larger than the mass of the bullet \\(m\\) (e.g. \\(M = 4\\text{ kg}\\) vs \\(m = 0.01\\text{ kg}\\)), the ratio \\(\\frac{m}{M}\\) is very small, making recoil velocity small.\n\n**Step 3: Conclusion**: The rifle\'s large mass keeps recoil velocity small. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(M V + m v = 0 \\implies |V| = \\frac{m}{M} v\\).\n\n**Step 2: Analysis**: Since the mass of the rifle \\(M\\) is hundreds of times larger than the mass of the bullet \\(m\\) (e.g. \\(M = 4\\text{ kg}\\) vs \\(m = 0.01\\text{ kg}\\)), the ratio \\(\\frac{m}{M}\\) is very small, making recoil velocity small.\n\n**Step 3: Conclusion**: The rifle\'s large mass keeps recoil velocity small. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'Why does a shooter hold the butt of a heavy rifle firmly pressed against their shoulder before firing?',
    options: [
      'To combine the mass of the shooter\'s body with the rifle, drastically increasing total recoil mass and reducing recoil velocity',
      'To prevent the rifle barrel from melting',
      'To increase the muzzle velocity of the bullet',
      'To steady the trigger against wind'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(V_{\\text{recoil}} = \\frac{m v}{M_{\\text{total}}}\\).\n\n**Step 2: Mechanism**: By pressing tightly against the shoulder, the effective mass receiving the backward impulse becomes \\(M_{\\text{rifle}} + M_{\\text{body}}\\). Since total mass is now ~60-80 kg instead of just 4 kg, recoil velocity drops to near zero, preventing shoulder bruise or fracture.\n\n**Step 3: Conclusion**: Increasing effective recoil mass minimizes recoil velocity. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(V_{\\text{recoil}} = \\frac{m v}{M_{\\text{total}}}\\).\n\n**Step 2: Mechanism**: By pressing tightly against the shoulder, the effective mass receiving the backward impulse becomes \\(M_{\\text{rifle}} + M_{\\text{body}}\\). Since total mass is now ~60-80 kg instead of just 4 kg, recoil velocity drops to near zero, preventing shoulder bruise or fracture.\n\n**Step 3: Conclusion**: Increasing effective recoil mass minimizes recoil velocity. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A rifle of mass \\(4\\text{ kg}\\) fires a bullet of mass \\(50\\text{ g}\\) with a speed of \\(400\\text{ m/s}\\). What is the kinetic energy of the recoiling rifle?',
    options: [
      '\\(50\\text{ Joules}\\)',
      '\\(25\\text{ Joules}\\)',
      '\\(100\\text{ Joules}\\)',
      '\\(4000\\text{ Joules}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Calculate recoil velocity first: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 0.05\\text{ kg}\\), \\(v = 400\\text{ m/s}\\), \\(M = 4\\text{ kg}\\). \\(V = \\frac{0.05 \\times 400}{4} = 5\\text{ m/s}\\). Kinetic energy of rifle \\(E_k = \\frac{1}{2} M V^2 = \\frac{1}{2} \\times 4 \\times 5^2 = 2 \\times 25 = 50\\text{ J}\\).\n\n**Step 3: Conclusion**: The kinetic energy is \\(50\\text{ J}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Calculate recoil velocity first: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 0.05\\text{ kg}\\), \\(v = 400\\text{ m/s}\\), \\(M = 4\\text{ kg}\\). \\(V = \\frac{0.05 \\times 400}{4} = 5\\text{ m/s}\\). Kinetic energy of rifle \\(E_k = \\frac{1}{2} M V^2 = \\frac{1}{2} \\times 4 \\times 5^2 = 2 \\times 25 = 50\\text{ J}\\).\n\n**Step 3: Conclusion**: The kinetic energy is \\(50\\text{ J}\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A cannon of mass \\(500\\text{ kg}\\) fires a cannonball of mass \\(10\\text{ kg}\\) horizontally at \\(100\\text{ m/s}\\). What is the recoil velocity of the cannon?',
    options: [
      '\\(-2\\text{ m/s}\\)',
      '\\(+2\\text{ m/s}\\)',
      '\\(-5\\text{ m/s}\\)',
      '\\(-20\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Conservation of linear momentum: \\(M V + m v = 0\\).\n\n**Step 2: Calculation**: \\(500 V + 10(100) = 0 \\implies 500 V = -1000 \\implies V = -2\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The cannon recoils backwards at \\(2\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Conservation of linear momentum: \\(M V + m v = 0\\).\n\n**Step 2: Calculation**: \\(500 V + 10(100) = 0 \\implies 500 V = -1000 \\implies V = -2\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The cannon recoils backwards at \\(2\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'If a gun of mass \\(M\\) fires a bullet of mass \\(m\\), what is the ratio of the kinetic energy of the bullet to the kinetic energy of the gun (\\(E_{\\text{bullet}} : E_{\\text{gun}}\\))?',
    options: [
      '\\(M : m\\)',
      '\\(m : M\\)',
      '\\(M^2 : m^2\\)',
      '\\(1 : 1\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Both gun and bullet have equal magnitude of momentum: \\(p_{\\text{bullet}} = p_{\\text{gun}} = p\\).\n\n**Step 2: Derivation**: Kinetic energy \\(E_k = \\frac{p^2}{2m}\\). Therefore, \\(\\frac{E_{\\text{bullet}}}{E_{\\text{gun}}} = \\frac{p^2 / 2m}{p^2 / 2M} = \\frac{M}{m}\\).\n\n**Step 3: Conclusion**: Ratio of kinetic energies is \\(M : m\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Both gun and bullet have equal magnitude of momentum: \\(p_{\\text{bullet}} = p_{\\text{gun}} = p\\).\n\n**Step 2: Derivation**: Kinetic energy \\(E_k = \\frac{p^2}{2m}\\). Therefore, \\(\\frac{E_{\\text{bullet}}}{E_{\\text{gun}}} = \\frac{p^2 / 2m}{p^2 / 2M} = \\frac{M}{m}\\).\n\n**Step 3: Conclusion**: Ratio of kinetic energies is \\(M : m\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A toy gun of mass \\(300\\text{ g}\\) shoots a plastic dart of mass \\(10\\text{ g}\\) at \\(15\\text{ m/s}\\). What is the recoil velocity of the toy gun?',
    options: [
      '\\(-0.5\\text{ m/s}\\)',
      '\\(-1.5\\text{ m/s}\\)',
      '\\(+0.5\\text{ m/s}\\)',
      '\\(-0.05\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 10\\text{ g}\\), \\(M = 300\\text{ g}\\), \\(v = 15\\text{ m/s}\\). \\(V = -\\frac{10 \\times 15}{300} = -\\frac{150}{300} = -0.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The toy gun recoils at \\(0.5\\text{ m/s}\\) backwards. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 10\\text{ g}\\), \\(M = 300\\text{ g}\\), \\(v = 15\\text{ m/s}\\). \\(V = -\\frac{10 \\times 15}{300} = -\\frac{150}{300} = -0.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The toy gun recoils at \\(0.5\\text{ m/s}\\) backwards. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'What happens to the recoil velocity of a pistol if a heavier bullet (double mass) is fired at the same muzzle velocity?',
    options: [
      'The recoil velocity is doubled',
      'The recoil velocity is halved',
      'The recoil velocity becomes four times',
      'The recoil velocity remains unchanged'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Analysis**: Since \\(V \\propto m\\), doubling the bullet mass \\(m\\) directly doubles the backward momentum, hence doubling the pistol\'s recoil velocity.\n\n**Step 3: Conclusion**: Recoil velocity doubles. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Analysis**: Since \\(V \\propto m\\), doubling the bullet mass \\(m\\) directly doubles the backward momentum, hence doubling the pistol\'s recoil velocity.\n\n**Step 3: Conclusion**: Recoil velocity doubles. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A machine gun fires \\(20\\text{ bullets}\\) per second, each of mass \\(30\\text{ g}\\), at a muzzle velocity of \\(500\\text{ m/s}\\). What average backward force does the gunner need to exert to keep the gun stationary?',
    options: [
      '\\(300\\text{ N}\\)',
      '\\(150\\text{ N}\\)',
      '\\(600\\text{ N}\\)',
      '\\(30\\text{ N}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Average force is the rate of momentum ejection: \\(F = n \\times \\frac{\\Delta p}{\\Delta t} = n m v\\) per second.\n\n**Step 2: Calculation**: \\(n = 20\\text{ bullets/s}\\), \\(m = 0.03\\text{ kg}\\), \\(v = 500\\text{ m/s}\\). Momentum per second \\(= 20 \\times 0.03 \\times 500 = 300\\text{ N}\\).\n\n**Step 3: Conclusion**: The gunner must push with \\(300\\text{ N}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Average force is the rate of momentum ejection: \\(F = n \\times \\frac{\\Delta p}{\\Delta t} = n m v\\) per second.\n\n**Step 2: Calculation**: \\(n = 20\\text{ bullets/s}\\), \\(m = 0.03\\text{ kg}\\), \\(v = 500\\text{ m/s}\\). Momentum per second \\(= 20 \\times 0.03 \\times 500 = 300\\text{ N}\\).\n\n**Step 3: Conclusion**: The gunner must push with \\(300\\text{ N}\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'Why does an artillery cannon on wheels roll backwards across the ground upon firing a heavy shell?',
    options: [
      'The explosion gases expand equally in all directions, driving the projectile forward and the cannon backward according to Newton\'s Third Law',
      'The ground tilts downward behind the cannon',
      'The cannon shell drags air backwards over the barrel',
      'Wheels lose all traction due to shockwave vibrations'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Newton\'s Third Law and Conservation of Momentum.\n\n**Step 2: Mechanism**: High-pressure combustion gas pushes the shell forward (Action) and the breech of the barrel backward (Reaction), driving the wheeled carriage backwards.\n\n**Step 3: Conclusion**: Gas expansion drives cannon backward. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Newton\'s Third Law and Conservation of Momentum.\n\n**Step 2: Mechanism**: High-pressure combustion gas pushes the shell forward (Action) and the breech of the barrel backward (Reaction), driving the wheeled carriage backwards.\n\n**Step 3: Conclusion**: Gas expansion drives cannon backward. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A shotgun of mass \\(3.5\\text{ kg}\\) fires \\(35\\text{ g}\\) of lead pellets at \\(300\\text{ m/s}\\). What is the recoil velocity of the shotgun?',
    options: [
      '\\(-3.0\\text{ m/s}\\)',
      '\\(-0.3\\text{ m/s}\\)',
      '\\(+3.0\\text{ m/s}\\)',
      '\\(-30\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 0.035\\text{ kg}\\), \\(M = 3.5\\text{ kg}\\), \\(v = 300\\text{ m/s}\\). \\(V = -\\frac{0.035 \\times 300}{3.5} = -\\frac{10.5}{3.5} = -3.0\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The recoil velocity is \\(-3.0\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(V = -\\frac{m v}{M}\\).\n\n**Step 2: Calculation**: \\(m = 0.035\\text{ kg}\\), \\(M = 3.5\\text{ kg}\\), \\(v = 300\\text{ m/s}\\). \\(V = -\\frac{0.035 \\times 300}{3.5} = -\\frac{10.5}{3.5} = -3.0\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The recoil velocity is \\(-3.0\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'What would happen if an astronaut fired a conventional handgun in outer space while floating in zero gravity?',
    options: [
      'The bullet would travel forward indefinitely, and the astronaut would drift backwards in the opposite direction at a speed determined by momentum conservation',
      'The gun would fail to fire because there is no oxygen in space for gunpowder to ignite',
      'The bullet would stop immediately due to vacuum resistance',
      'The astronaut would spin in a circle without moving backward'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Modern gunpowder contains its own oxidizer, so it fires without external atmospheric oxygen.\n\n**Step 2: Physics in Zero Gravity**: The bullet moves forward at muzzle velocity. By conservation of linear momentum, the astronaut recoils backwards at \\(V = -\\frac{m v}{M}\\) and continues drifting in that direction forever unless stopped.\n\n**Step 3: Conclusion**: The astronaut drifts backward. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Modern gunpowder contains its own oxidizer, so it fires without external atmospheric oxygen.\n\n**Step 2: Physics in Zero Gravity**: The bullet moves forward at muzzle velocity. By conservation of linear momentum, the astronaut recoils backwards at \\(V = -\\frac{m v}{M}\\) and continues drifting in that direction forever unless stopped.\n\n**Step 3: Conclusion**: The astronaut drifts backward. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A hunter holds a rifle loosely away from their shoulder and pulls the trigger. Why does this cause a painful impact against the hunter\'s body?',
    options: [
      'The loose rifle accelerates freely across the gap before striking the shoulder, delivering a sharp impact at full recoil velocity',
      'The rifle gains mass during flight',
      'The bullet curves backward',
      'Air fills the gap creating an explosive shockwave'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Impact mechanics of recoil.\n\n**Step 2: Mechanism**: If the rifle is pressed firmly against the shoulder, the recoil velocity of the combined (rifle + body) is tiny. But if held loose, the rifle accelerates backwards alone to its full free recoil velocity (e.g. 5 m/s) and hits the stationary shoulder like a flying hammer.\n\n**Step 3: Conclusion**: Striking at full free recoil speed causes injury. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Impact mechanics of recoil.\n\n**Step 2: Mechanism**: If the rifle is pressed firmly against the shoulder, the recoil velocity of the combined (rifle + body) is tiny. But if held loose, the rifle accelerates backwards alone to its full free recoil velocity (e.g. 5 m/s) and hits the stationary shoulder like a flying hammer.\n\n**Step 3: Conclusion**: Striking at full free recoil speed causes injury. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A rifle of mass \\(5\\text{ kg}\\) fires a bullet of mass \\(25\\text{ g}\\) at \\(600\\text{ m/s}\\). What momentum is transferred to the shooter\'s shoulder?',
    options: [
      '\\(15\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(30\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(7.5\\text{ kg}\\cdot\\text{m/s}\\)',
      '\\(150\\text{ kg}\\cdot\\text{m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: By conservation of momentum, \\(p_{\\text{rifle}} = p_{\\text{bullet}} = m v\\).\n\n**Step 2: Calculation**: \\(m = 0.025\\text{ kg}\\), \\(v = 600\\text{ m/s}\\). \\(p = 0.025 \\times 600 = 15\\text{ kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: The backward momentum transferred is \\(15\\text{ kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: By conservation of momentum, \\(p_{\\text{rifle}} = p_{\\text{bullet}} = m v\\).\n\n**Step 2: Calculation**: \\(m = 0.025\\text{ kg}\\), \\(v = 600\\text{ m/s}\\). \\(p = 0.025 \\times 600 = 15\\text{ kg}\\cdot\\text{m/s}\\).\n\n**Step 3: Conclusion**: The backward momentum transferred is \\(15\\text{ kg}\\cdot\\text{m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.6.5',
    type: 'OSC',
    text: 'A gun recoils backwards after firing a bullet. This is a direct practical demonstration of which conservation principle and Newton\'s law?',
    options: [
      'Conservation of Linear Momentum and Newton\'s Third Law of Motion',
      'Conservation of Angular Momentum and Newton\'s First Law',
      'Conservation of Mechanical Energy and Newton\'s Second Law',
      'Law of Gravitational Acceleration'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Recoil is governed by action-reaction and momentum balance.\n\n**Step 2: Analysis**: The bullet is pushed forward with force \\(F\\) (Action) and the gun is pushed backward with force \\(-F\\) (Reaction, Newton\'s 3rd Law). Since internal forces cancel, total momentum before firing (0) equals total momentum after firing (Conservation of Linear Momentum).\n\n**Step 3: Conclusion**: Governed by Conservation of Momentum and Newton\'s Third Law. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Recoil is governed by action-reaction and momentum balance.\n\n**Step 2: Analysis**: The bullet is pushed forward with force \\(F\\) (Action) and the gun is pushed backward with force \\(-F\\) (Reaction, Newton\'s 3rd Law). Since internal forces cancel, total momentum before firing (0) equals total momentum after firing (Conservation of Linear Momentum).\n\n**Step 3: Conclusion**: Governed by Conservation of Momentum and Newton\'s Third Law. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  }
];

module.exports = { part2Questions };
