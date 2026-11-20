const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx > 0) {
        let v = trimmed.slice(idx + 1).trim();
        if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = v;
      }
    }
  });
}

const sa = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({
    credential: admin.credential.cert(cred),
    projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom'
  });
}
const db = admin.firestore();

// 10 Practice Questions for 1.3.1: Interpreting slopes for velocity and acceleration
const questions_131 = [
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'A car moves along a straight road. Its position-time (\\(s\\)-\\(t\\)) graph is a straight line inclined at an angle of \\(45^\\circ\\) to the time axis. If the position scale is \\(1\\text{ unit} = 1\\text{ m}\\) and the time scale is \\(1\\text{ unit} = 1\\text{ s}\\), what is the velocity of the car?',
    options: [
      '\\(1\\text{ m/s}\\)',
      '\\(0.5\\text{ m/s}\\)',
      '\\(2\\text{ m/s}\\)',
      '\\(0\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: On a position-time (\\(s\\)-\\(t\\)) graph, the slope of the curve represents the velocity of the object (\\(v = \\frac{\\Delta s}{\\Delta t} = \\tan \\theta\\)).\n\n**Step 2: Formula & Calculation**: The slope of a line inclined at an angle \\(\\theta\\) to the horizontal axis is given by \\(\\tan \\theta\\). Here, \\(\\theta = 45^\\circ\\). Therefore, \\(\\text{Slope} = \\tan 45^\\circ = 1\\). Thus, velocity \\(v = 1\\text{ m/s}\\).\n\n**Step 3: Verification**: Since the line is straight with a non-zero constant slope, the car moves with uniform velocity of \\(1\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: On a position-time (\\(s\\)-\\(t\\)) graph, the slope of the curve represents the velocity of the object (\\(v = \\frac{\\Delta s}{\\Delta t} = \\tan \\theta\\)).\n\n**Step 2: Formula & Calculation**: The slope of a line inclined at an angle \\(\\theta\\) to the horizontal axis is given by \\(\\tan \\theta\\). Here, \\(\\theta = 45^\\circ\\). Therefore, \\(\\text{Slope} = \\tan 45^\\circ = 1\\). Thus, velocity \\(v = 1\\text{ m/s}\\).\n\n**Step 3: Verification**: Since the line is straight with a non-zero constant slope, the car moves with uniform velocity of \\(1\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'On a velocity-time (\\(v\\)-\\(t\\)) graph, the graph is a straight horizontal line parallel to the time axis at \\(v = 25\\text{ m/s}\\). What is the acceleration of the object?',
    options: [
      '\\(0\\text{ m/s}^2\\)',
      '\\(25\\text{ m/s}^2\\)',
      '\\(9.8\\text{ m/s}^2\\)',
      '\\(-25\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of a velocity-time (\\(v\\)-\\(t\\)) graph represents acceleration (\\(a = \\frac{\\Delta v}{\\Delta t}\\)).\n\n**Step 2: Analysis**: A horizontal line parallel to the time axis has a change in vertical coordinate \\(\\Delta v = 0\\). Therefore, \\(\\text{Slope} = \\frac{0}{\\Delta t} = 0\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: When an object moves with a constant velocity, its acceleration is zero. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of a velocity-time (\\(v\\)-\\(t\\)) graph represents acceleration (\\(a = \\frac{\\Delta v}{\\Delta t}\\)).\n\n**Step 2: Analysis**: A horizontal line parallel to the time axis has a change in vertical coordinate \\(\\Delta v = 0\\). Therefore, \\(\\text{Slope} = \\frac{0}{\\Delta t} = 0\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: When an object moves with a constant velocity, its acceleration is zero. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'A bicycle starts from rest and accelerates uniformly. Its velocity increases from \\(0\\text{ m/s}\\) to \\(18\\text{ m/s}\\) in \\(6\\text{ s}\\). What is the slope of its velocity-time graph during this interval?',
    options: [
      '\\(3\\text{ m/s}^2\\)',
      '\\(6\\text{ m/s}^2\\)',
      '\\(12\\text{ m/s}^2\\)',
      '\\(108\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of a \\(v\\)-\\(t\\) graph represents acceleration: \\(\\text{Slope} = \\frac{v_2 - v_1}{t_2 - t_1}\\).\n\n**Step 2: Calculation**: Given \\(v_1 = 0\\text{ m/s}\\), \\(v_2 = 18\\text{ m/s}\\), \\(t_1 = 0\\text{ s}\\), and \\(t_2 = 6\\text{ s}\\). \\(\\text{Slope} = \\frac{18 - 0}{6 - 0} = \\frac{18}{6} = 3\\text{ m/s}^2\\).\n\n**Step 3: Verification**: An acceleration of \\(3\\text{ m/s}^2\\) means the velocity increases by \\(3\\text{ m/s}\\) every second. Over \\(6\\text{ s}\\), \\(3 \\times 6 = 18\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of a \\(v\\)-\\(t\\) graph represents acceleration: \\(\\text{Slope} = \\frac{v_2 - v_1}{t_2 - t_1}\\).\n\n**Step 2: Calculation**: Given \\(v_1 = 0\\text{ m/s}\\), \\(v_2 = 18\\text{ m/s}\\), \\(t_1 = 0\\text{ s}\\), and \\(t_2 = 6\\text{ s}\\). \\(\\text{Slope} = \\frac{18 - 0}{6 - 0} = \\frac{18}{6} = 3\\text{ m/s}^2\\).\n\n**Step 3: Verification**: An acceleration of \\(3\\text{ m/s}^2\\) means the velocity increases by \\(3\\text{ m/s}\\) every second. Over \\(6\\text{ s}\\), \\(3 \\times 6 = 18\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'A train moving at \\(30\\text{ m/s}\\) applies brakes and comes to a complete halt in \\(10\\text{ s}\\). What is the nature and value of the slope of its velocity-time graph?',
    options: [
      'Negative slope of \\(-3\\text{ m/s}^2\\), representing deceleration (retardation)',
      'Positive slope of \\(+3\\text{ m/s}^2\\), representing positive acceleration',
      'Zero slope, representing uniform speed',
      'Negative slope of \\(-300\\text{ m/s}^2\\), representing sudden stop'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: When brakes are applied, the velocity decreases with time, producing a downward-sloping straight line on the \\(v\\)-\\(t\\) graph (negative slope), which signifies deceleration.\n\n**Step 2: Calculation**: \\(\\text{Slope} = \\frac{v - u}{t} = \\frac{0 - 30}{10} = -3\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The negative sign confirms retardation or deceleration of \\(3\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: When brakes are applied, the velocity decreases with time, producing a downward-sloping straight line on the \\(v\\)-\\(t\\) graph (negative slope), which signifies deceleration.\n\n**Step 2: Calculation**: \\(\\text{Slope} = \\frac{v - u}{t} = \\frac{0 - 30}{10} = -3\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The negative sign confirms retardation or deceleration of \\(3\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'The displacement-time graph of two runners \\(A\\) and \\(B\\) are straight lines inclined at \\(30^\\circ\\) and \\(60^\\circ\\) to the time axis respectively. What is the ratio of the velocity of runner \\(A\\) to that of runner \\(B\\) (\\(v_A : v_B\\))?',
    options: [
      '\\(1 : 3\\)',
      '\\(3 : 1\\)',
      '\\(1 : \\sqrt{3}\\)',
      '\\(\\sqrt{3} : 1\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Velocity on an \\(s\\)-\\(t\\) graph is given by the slope: \\(v = \\tan \\theta\\).\n\n**Step 2: Calculation**: For runner \\(A\\): \\(v_A = \\tan 30^\\circ = \\frac{1}{\\sqrt{3}}\\). For runner \\(B\\): \\(v_B = \\tan 60^\\circ = \\sqrt{3}\\). Ratio \\(\\frac{v_A}{v_B} = \\frac{1/\\sqrt{3}}{\\sqrt{3}} = \\frac{1}{3}\\).\n\n**Step 3: Conclusion**: The ratio of velocities is \\(1 : 3\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Velocity on an \\(s\\)-\\(t\\) graph is given by the slope: \\(v = \\tan \\theta\\).\n\n**Step 2: Calculation**: For runner \\(A\\): \\(v_A = \\tan 30^\\circ = \\frac{1}{\\sqrt{3}}\\). For runner \\(B\\): \\(v_B = \\tan 60^\\circ = \\sqrt{3}\\). Ratio \\(\\frac{v_A}{v_B} = \\frac{1/\\sqrt{3}}{\\sqrt{3}} = \\frac{1}{3}\\).\n\n**Step 3: Conclusion**: The ratio of velocities is \\(1 : 3\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'If the displacement-time graph of an object curves upwards with increasing steepness (convex towards the time axis), what does this indicate about the slope and the motion?',
    options: [
      'The slope increases with time, indicating accelerated motion (increasing velocity)',
      'The slope remains constant, indicating uniform velocity',
      'The slope decreases with time, indicating retardation',
      'The slope is zero, indicating the object is stationary'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of the tangent at any point on an \\(s\\)-\\(t\\) graph gives the instantaneous velocity \\(v = \\frac{ds}{dt}\\).\n\n**Step 2: Analysis**: If the graph becomes steeper as time progresses, the tangent angle \\(\\theta\\) increases, meaning \\(\\tan \\theta\\) (velocity) increases.\n\n**Step 3: Conclusion**: An increasing slope on an \\(s\\)-\\(t\\) graph directly signifies that velocity is increasing with time, i.e., the motion is accelerated. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of the tangent at any point on an \\(s\\)-\\(t\\) graph gives the instantaneous velocity \\(v = \\frac{ds}{dt}\\).\n\n**Step 2: Analysis**: If the graph becomes steeper as time progresses, the tangent angle \\(\\theta\\) increases, meaning \\(\\tan \\theta\\) (velocity) increases.\n\n**Step 3: Conclusion**: An increasing slope on an \\(s\\)-\\(t\\) graph directly signifies that velocity is increasing with time, i.e., the motion is accelerated. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'understand'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'On a velocity-time graph, the curve passes through points \\((2\\text{ s}, 10\\text{ m/s})\\) and \\((6\\text{ s}, 26\\text{ m/s})\\). What is the average acceleration represented by the slope between these two points?',
    options: [
      '\\(4\\text{ m/s}^2\\)',
      '\\(8\\text{ m/s}^2\\)',
      '\\(16\\text{ m/s}^2\\)',
      '\\(2.6\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of the secant line between two points on a \\(v\\)-\\(t\\) graph gives the average acceleration: \\(a_{\\text{avg}} = \\frac{v_2 - v_1}{t_2 - t_1}\\).\n\n**Step 2: Calculation**: Here, \\((t_1, v_1) = (2, 10)\\) and \\((t_2, v_2) = (6, 26)\\). \\(a = \\frac{26 - 10}{6 - 2} = \\frac{16}{4} = 4\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The average acceleration during this time interval is \\(4\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of the secant line between two points on a \\(v\\)-\\(t\\) graph gives the average acceleration: \\(a_{\\text{avg}} = \\frac{v_2 - v_1}{t_2 - t_1}\\).\n\n**Step 2: Calculation**: Here, \\((t_1, v_1) = (2, 10)\\) and \\((t_2, v_2) = (6, 26)\\). \\(a = \\frac{26 - 10}{6 - 2} = \\frac{16}{4} = 4\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The average acceleration during this time interval is \\(4\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'Which of the following physical quantities has the same dimensional unit as the slope of a velocity-time graph?',
    options: [
      'Acceleration due to gravity (\\(g\\))',
      'Momentum (\\(p\\))',
      'Velocity (\\(v\\))',
      'Force (\\(F\\))'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of a velocity-time graph is \\(\\frac{\\Delta v}{\\Delta t}\\), which has SI units of \\(\\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2\\).\n\n**Step 2: Comparison**: Acceleration due to gravity (\\(g\\)) also has SI units of \\(\\text{m/s}^2\\). Momentum has \\(\\text{kg}\\cdot\\text{m/s}\\), velocity has \\(\\text{m/s}\\), and force has \\(\\text{N} = \\text{kg}\\cdot\\text{m/s}^2\\).\n\n**Step 3: Conclusion**: The slope represents acceleration, so its unit matches that of acceleration due to gravity. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of a velocity-time graph is \\(\\frac{\\Delta v}{\\Delta t}\\), which has SI units of \\(\\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2\\).\n\n**Step 2: Comparison**: Acceleration due to gravity (\\(g\\)) also has SI units of \\(\\text{m/s}^2\\). Momentum has \\(\\text{kg}\\cdot\\text{m/s}\\), velocity has \\(\\text{m/s}\\), and force has \\(\\text{N} = \\text{kg}\\cdot\\text{m/s}^2\\).\n\n**Step 3: Conclusion**: The slope represents acceleration, so its unit matches that of acceleration due to gravity. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'A ball is thrown vertically upward into the air. Taking the upward direction as positive, what does the slope of its velocity-time graph represent during the entire flight (upward, at highest point, and downward)?',
    options: [
      'A constant negative slope equal to \\(-9.8\\text{ m/s}^2\\) (acceleration due to gravity)',
      'A positive slope going up and a negative slope coming down',
      'Zero slope at the highest point because velocity is zero',
      'A variable slope that depends on the ball\'s mass'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The slope of a \\(v\\)-\\(t\\) graph represents acceleration (\\(a = \\frac{dv}{dt}\\)).\n\n**Step 2: Physical Analysis**: For a freely falling body under gravity (neglecting air resistance), the only force acting is gravity, directed downwards. With upwards taken as positive, the acceleration is constant throughout: \\(a = -g = -9.8\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: Even at the highest point where instantaneous velocity is zero, gravity still acts downward with \\(-9.8\\text{ m/s}^2\\). Thus, the slope remains constant and negative. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The slope of a \\(v\\)-\\(t\\) graph represents acceleration (\\(a = \\frac{dv}{dt}\\)).\n\n**Step 2: Physical Analysis**: For a freely falling body under gravity (neglecting air resistance), the only force acting is gravity, directed downwards. With upwards taken as positive, the acceleration is constant throughout: \\(a = -g = -9.8\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: Even at the highest point where instantaneous velocity is zero, gravity still acts downward with \\(-9.8\\text{ m/s}^2\\). Thus, the slope remains constant and negative. Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'On a position-time graph, line \\(X\\) has a slope of \\(+15\\text{ m/s}\\) and line \\(Y\\) has a slope of \\(-20\\text{ m/s}\\). Which of the following statements is TRUE?',
    options: [
      'Body \\(Y\\) has a greater speed than Body \\(X\\), but moves in the opposite direction',
      'Body \\(X\\) has a greater speed than Body \\(Y\\) because \\(+15 > -20\\)',
      'Both bodies have zero acceleration and zero speed',
      'Body \\(Y\\) is decelerating while Body \\(X\\) is accelerating'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: On an \\(s\\)-\\(t\\) graph, the slope represents velocity (which includes direction). Speed is the magnitude of velocity: \\(\\text{Speed} = |v| = |\\text{Slope}|\\).\n\n**Step 2: Analysis**: Speed of \\(X = |+15| = 15\\text{ m/s}\\). Speed of \\(Y = |-20| = 20\\text{ m/s}\\). Since \\(20 > 15\\), Body \\(Y\\) has higher speed. The negative sign for \\(Y\\) indicates motion in the negative direction (towards origin).\n\n**Step 3: Conclusion**: Body \\(Y\\) has a higher speed than Body \\(X\\), moving in the opposite direction. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: On an \\(s\\)-\\(t\\) graph, the slope represents velocity (which includes direction). Speed is the magnitude of velocity: \\(\\text{Speed} = |v| = |\\text{Slope}|\\).\n\n**Step 2: Analysis**: Speed of \\(X = |+15| = 15\\text{ m/s}\\). Speed of \\(Y = |-20| = 20\\text{ m/s}\\). Since \\(20 > 15\\), Body \\(Y\\) has higher speed. The negative sign for \\(Y\\) indicates motion in the negative direction (towards origin).\n\n**Step 3: Conclusion**: Body \\(Y\\) has a higher speed than Body \\(X\\), moving in the opposite direction. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  }
];

// 2 Practice Questions for 1.3.2: Area under velocity-time graph gives displacement
const questions_132 = [
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'A car moves with a constant velocity of \\(20\\text{ m/s}\\) for \\(15\\text{ s}\\). What is the displacement covered by the car, calculated from the area under its velocity-time graph?',
    options: [
      '\\(300\\text{ m}\\)',
      '\\(150\\text{ m}\\)',
      '\\(600\\text{ m}\\)',
      '\\(35\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: The area enclosed under a velocity-time (\\(v\\)-\\(t\\)) graph and the time axis equals the displacement (\\(s = \\text{Area}\\)).\n\n**Step 2: Calculation**: For constant velocity, the enclosed area is a rectangle: \\(\\text{Area} = \\text{height} \\times \\text{base} = v \\times t\\). Here, \\(v = 20\\text{ m/s}\\) and \\(t = 15\\text{ s}\\). \\(s = 20 \\times 15 = 300\\text{ m}\\).\n\n**Step 3: Conclusion**: The displacement covered by the car is \\(300\\text{ m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: The area enclosed under a velocity-time (\\(v\\)-\\(t\\)) graph and the time axis equals the displacement (\\(s = \\text{Area}\\)).\n\n**Step 2: Calculation**: For constant velocity, the enclosed area is a rectangle: \\(\\text{Area} = \\text{height} \\times \\text{base} = v \\times t\\). Here, \\(v = 20\\text{ m/s}\\) and \\(t = 15\\text{ s}\\). \\(s = 20 \\times 15 = 300\\text{ m}\\).\n\n**Step 3: Conclusion**: The displacement covered by the car is \\(300\\text{ m}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    type: 'OSC',
    questionType: 'OSC',
    text: 'An athlete accelerates uniformly from rest (\\(0\\text{ m/s}\\)) to a top velocity of \\(12\\text{ m/s}\\) in \\(4\\text{ s}\\). What is the total distance covered during this acceleration, determined using the area under the \\(v\\)-\\(t\\) graph?',
    options: [
      '\\(24\\text{ m}\\)',
      '\\(48\\text{ m}\\)',
      '\\(16\\text{ m}\\)',
      '\\(3\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: For uniform acceleration starting from rest, the \\(v\\)-\\(t\\) graph forms a right triangle with the time axis. Displacement equals the area of this triangle: \\(\\text{Displacement} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}\\).\n\n**Step 2: Calculation**: Base \\(t = 4\\text{ s}\\), height \\(v = 12\\text{ m/s}\\). \\(\\text{Displacement} = \\frac{1}{2} \\times 4 \\times 12 = 24\\text{ m}\\).\n\n**Step 3: Conclusion**: The distance covered during the \\(4\\text{ s}\\) sprint is \\(24\\text{ m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: For uniform acceleration starting from rest, the \\(v\\)-\\(t\\) graph forms a right triangle with the time axis. Displacement equals the area of this triangle: \\(\\text{Displacement} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}\\).\n\n**Step 2: Calculation**: Base \\(t = 4\\text{ s}\\), height \\(v = 12\\text{ m/s}\\). \\(\\text{Displacement} = \\frac{1}{2} \\times 4 \\times 12 = 24\\text{ m}\\).\n\n**Step 3: Conclusion**: The distance covered during the \\(4\\text{ s}\\) sprint is \\(24\\text{ m}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  }
];

async function insertTopup() {
  console.log('--- Fetching current highest sequence for 1.3.1 OSC ---');
  const snap131 = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.1')
    .get();

  let maxOsc131 = 0;
  snap131.docs.forEach(d => {
    const code = d.data().questionCode || '';
    if (code.includes('-OSC-')) {
      const parts = code.split('-');
      const num = parseInt(parts[parts.length - 1], 10);
      if (!isNaN(num)) maxOsc131 = Math.max(maxOsc131, num);
    }
  });
  console.log('Max 1.3.1 OSC seq:', maxOsc131);

  console.log('--- Fetching current highest sequence for 1.3.2 OSC ---');
  const snap132 = await db.collection('questions')
    .where('subtopicCode', '==', 'MH-9-SCIT-1-1.3.2')
    .get();

  let maxOsc132 = 0;
  snap132.docs.forEach(d => {
    const code = d.data().questionCode || '';
    if (code.includes('-OSC-')) {
      const parts = code.split('-');
      const num = parseInt(parts[parts.length - 1], 10);
      if (!isNaN(num)) maxOsc132 = Math.max(maxOsc132, num);
    }
  });
  console.log('Max 1.3.2 OSC seq:', maxOsc132);

  const batch = db.batch();
  let count = 0;

  // Insert 1.3.1 questions
  questions_131.forEach(q => {
    maxOsc131++;
    const qcode = `MH-9-SCIT-1-1.3.1-OSC-${String(maxOsc131).padStart(3, '0')}`;
    const docRef = db.collection('questions').doc(qcode);
    const data = {
      ...q,
      boardCode: 'MH',
      class: '9',
      subjectCode: 'SCIT',
      board: 'Maharashtra State Board',
      subject: 'Science and Technology',
      chapterNumber: 1,
      chapter: 'Laws of Motion',
      vault: 'practice',
      examCategory: 'standard',
      requiresFigure: false,
      marks: 4,
      timesUsed: 0,
      usedInClassroomTest: false,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      subtopicCode: 'MH-9-SCIT-1-1.3.1',
      subtopicName: 'Interpreting slopes for velocity and acceleration',
      subtopicNumber: '1.3.1',
      subtopic: 'Interpreting slopes for velocity and acceleration',
      topicCode: 'MH-9-SCIT-1-1.3',
      parentTopicCode: 'MH-9-SCIT-1-1.3',
      parentTopicName: 'Distance-Time and Velocity-Time Graphs',
      topic: 'Distance-Time and Velocity-Time Graphs',
      topicName: 'Distance-Time and Velocity-Time Graphs',
      topicNumber: '1.3.1',
      questionCode: qcode
    };
    batch.set(docRef, data);
    count++;
  });

  // Insert 1.3.2 questions
  questions_132.forEach(q => {
    maxOsc132++;
    const qcode = `MH-9-SCIT-1-1.3.2-OSC-${String(maxOsc132).padStart(3, '0')}`;
    const docRef = db.collection('questions').doc(qcode);
    const data = {
      ...q,
      boardCode: 'MH',
      class: '9',
      subjectCode: 'SCIT',
      board: 'Maharashtra State Board',
      subject: 'Science and Technology',
      chapterNumber: 1,
      chapter: 'Laws of Motion',
      vault: 'practice',
      examCategory: 'standard',
      requiresFigure: false,
      marks: 4,
      timesUsed: 0,
      usedInClassroomTest: false,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      subtopicCode: 'MH-9-SCIT-1-1.3.2',
      subtopicName: 'Area under velocity-time graph gives displacement',
      subtopicNumber: '1.3.2',
      subtopic: 'Area under velocity-time graph gives displacement',
      topicCode: 'MH-9-SCIT-1-1.3',
      parentTopicCode: 'MH-9-SCIT-1-1.3',
      parentTopicName: 'Distance-Time and Velocity-Time Graphs',
      topic: 'Distance-Time and Velocity-Time Graphs',
      topicName: 'Distance-Time and Velocity-Time Graphs',
      topicNumber: '1.3.2',
      questionCode: qcode
    };
    batch.set(docRef, data);
    count++;
  });

  console.log(`Committing ${count} new practice questions to Firestore...`);
  await batch.commit();
  console.log('Committed successfully!');

  // Update syllabus document counts
  const sylRef = db.collection('syllabus').doc('mh_9_scit');
  const sylDoc = await sylRef.get();
  if (sylDoc.exists) {
    const data = sylDoc.data();
    const ch1 = (data.chapters || []).find(c => String(c.number) === '1');
    if (ch1) {
      const t13 = (ch1.topics || []).find(t => t.number === '1.3');
      if (t13 && t13.subtopics) {
        const st131 = t13.subtopics.find(st => st.number === '1.3.1');
        const st132 = t13.subtopics.find(st => st.number === '1.3.2');
        if (st131 && st132) {
          st131.objectiveCount = (st131.objectiveCount || 0) + questions_131.length;
          st132.objectiveCount = (st132.objectiveCount || 0) + questions_132.length;
          t13.objectiveCount = (t13.objectiveCount || 0) + count;
          ch1.objectiveCount = (ch1.objectiveCount || 0) + count;
          console.log(`Updated syllabus counts:`);
          console.log(`  1.3.1 obj = ${st131.objectiveCount}`);
          console.log(`  1.3.2 obj = ${st132.objectiveCount}`);
          console.log(`  Topic 1.3 obj = ${t13.objectiveCount}`);
          console.log(`  Chapter 1 obj = ${ch1.objectiveCount}`);
          await sylRef.update({ chapters: data.chapters });
          console.log('Syllabus updated successfully.');
        }
      }
    }
  }
}

insertTopup().catch(err => {
  console.error('Error inserting topup:', err);
  process.exit(1);
});
