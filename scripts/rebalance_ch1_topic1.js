const admin = require('firebase-admin');
require('./pre-mutation-snapshot.js');
const db = admin.firestore();

// 12 Foundation / Homi Bhabha diagram questions for Topic 1.1 (Distance, Displacement, Speed, Velocity)
const topic1_foundation_questions = [
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `An athlete runs along a circular track of radius \\(R = 70\\text{ m}\\) from starting point \\(A\\) to diametrically opposite point \\(B\\) as shown in the diagram.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 220" width="300" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Track Circle -->
  <circle cx="160" cy="110" r="80" stroke="#38bdf8" stroke-width="3" fill="none" stroke-dasharray="6 4" />
  <!-- Diameter line -->
  <line x1="80" y1="110" x2="240" y2="110" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrow)" />
  <!-- Center dot -->
  <circle cx="160" cy="110" r="4" fill="#f8fafc" />
  <text x="160" y="100" fill="#94a3b8" font-size="12" text-anchor="middle">O (Centre, R=70m)</text>
  <!-- Points A and B -->
  <circle cx="80" cy="110" r="6" fill="#22c55e" />
  <text x="65" y="115" fill="#22c55e" font-size="14" font-weight="bold">A</text>
  <circle cx="240" cy="110" r="6" fill="#f43f5e" />
  <text x="252" y="115" fill="#f43f5e" font-size="14" font-weight="bold">B</text>
  <!-- Semicircle motion arrow -->
  <path d="M 80 110 A 80 80 0 0 1 240 110" fill="none" stroke="#eab308" stroke-width="3" />
  <text x="160" y="24" fill="#eab308" font-size="12" text-anchor="middle">Semi-circular Path (Distance)</text>
  <text x="160" y="130" fill="#f43f5e" font-size="11" text-anchor="middle">Displacement Vector AB</text>
</svg>
</div>
What are the magnitudes of the distance covered and the net displacement vector \\(\\vec{s}\\) respectively? (Take \\(\\pi = \\frac{22}{7}\\))`,
    options: [
      { text: 'Distance = \\(220\\text{ m}\\), Displacement = \\(140\\text{ m}\\)', isCorrect: true },
      { text: 'Distance = \\(140\\text{ m}\\), Displacement = \\(220\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(440\\text{ m}\\), Displacement = \\(0\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(220\\text{ m}\\), Displacement = \\(0\\text{ m}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Step 1: Distance is the actual path length traversed along the perimeter of the semi-circle:
\\[\\text{Distance} = \\pi R = \\frac{22}{7} \\times 70 = 220\\text{ m}\\]
• Step 2: Displacement is the shortest straight-line distance from initial point \\(A\\) to final point \\(B\\), which equals the diameter of the circular track:
\\[|\\vec{s}| = 2R = 2 \\times 70 = 140\\text{ m}\\]
• Conclusion: Distance is \\(220\\text{ m}\\) and Displacement is \\(140\\text{ m}\\). Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A robotic survey vehicle travels from point \\(O\\) directly \\(300\\text{ m}\\) due East to point \\(A\\), and then turns sharply North traveling \\(400\\text{ m}\\) to point \\(B\\) as shown.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 230" width="300" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Axes / Grid -->
  <line x1="40" y1="180" x2="280" y2="180" stroke="#334155" stroke-width="1.5" />
  <line x1="60" y1="200" x2="60" y2="30" stroke="#334155" stroke-width="1.5" />
  <!-- East leg OA -->
  <line x1="60" y1="180" x2="220" y2="180" stroke="#38bdf8" stroke-width="3" />
  <text x="140" y="198" fill="#38bdf8" font-size="12" text-anchor="middle">300 m (East)</text>
  <!-- North leg AB -->
  <line x1="220" y1="180" x2="220" y2="50" stroke="#eab308" stroke-width="3" />
  <text x="260" y="120" fill="#eab308" font-size="12" text-anchor="middle">400 m (North)</text>
  <!-- Displacement Hypotenuse OB -->
  <line x1="60" y1="180" x2="220" y2="50" stroke="#f43f5e" stroke-width="3" stroke-dasharray="5 3" />
  <text x="120" y="105" fill="#f43f5e" font-size="12" font-weight="bold">Net Displacement</text>
  <!-- Vertex markers -->
  <circle cx="60" cy="180" r="5" fill="#22c55e" />
  <text x="45" y="185" fill="#22c55e" font-size="14" font-weight="bold">O</text>
  <circle cx="220" cy="180" r="4" fill="#f8fafc" />
  <text x="230" y="195" fill="#f8fafc" font-size="13">A</text>
  <circle cx="220" cy="50" r="5" fill="#ec4899" />
  <text x="230" y="45" fill="#ec4899" font-size="14" font-weight="bold">B</text>
</svg>
</div>
If the entire journey takes \\(50\\text{ seconds}\\), what are the average speed and the magnitude of average velocity of the vehicle?`,
    options: [
      { text: 'Average speed = \\(14\\text{ m/s}\\), Average velocity = \\(10\\text{ m/s}\\)', isCorrect: true },
      { text: 'Average speed = \\(10\\text{ m/s}\\), Average velocity = \\(14\\text{ m/s}\\)', isCorrect: false },
      { text: 'Average speed = \\(14\\text{ m/s}\\), Average velocity = \\(14\\text{ m/s}\\)', isCorrect: false },
      { text: 'Average speed = \\(700\\text{ m/s}\\), Average velocity = \\(500\\text{ m/s}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Total Distance = \\(OA + AB = 300\\text{ m} + 400\\text{ m} = 700\\text{ m}\\).
• Net Displacement = \\(|\\vec{OB}| = \\sqrt{OA^2 + AB^2} = \\sqrt{300^2 + 400^2} = \\sqrt{90000 + 160000} = 500\\text{ m}\\).
• Total Time = \\(50\\text{ s}\\).
• Average Speed:
\\[v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{700}{50} = 14\\text{ m/s}\\]
• Magnitude of Average Velocity:
\\[|\\vec{v}_{\\text{avg}}| = \\frac{|\\text{Displacement}|}{\\text{Total Time}} = \\frac{500}{50} = 10\\text{ m/s}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A particle moves along a straight coordinate line from position \\(P\\) to \\(Q\\), then reverses direction and moves back to point \\(R\\) as illustrated in the coordinate diagram below.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 160" width="320" height="150" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Number Line Axis -->
  <line x1="20" y1="100" x2="320" y2="100" stroke="#cbd5e1" stroke-width="2.5" />
  <!-- Ticks and labels -->
  <circle cx="60" cy="100" r="4" fill="#cbd5e1" /><text x="60" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">-20m</text>
  <circle cx="110" cy="100" r="4" fill="#cbd5e1" /><text x="110" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">0m</text>
  <circle cx="160" cy="100" r="4" fill="#cbd5e1" /><text x="160" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">+20m</text>
  <circle cx="210" cy="100" r="4" fill="#cbd5e1" /><text x="210" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">+40m</text>
  <circle cx="260" cy="100" r="4" fill="#cbd5e1" /><text x="260" y="125" fill="#94a3b8" font-size="11" text-anchor="middle">+60m</text>
  <!-- Forward Path P (0) -> Q (+60) -->
  <path d="M 110 90 Q 185 40 260 90" fill="none" stroke="#38bdf8" stroke-width="3" />
  <circle cx="110" cy="90" r="5" fill="#22c55e" /><text x="110" y="45" fill="#22c55e" font-size="12" font-weight="bold">P (Start: 0m)</text>
  <circle cx="260" cy="90" r="5" fill="#38bdf8" /><text x="260" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Q (+60m)</text>
  <!-- Backward Path Q (+60) -> R (-20) -->
  <path d="M 260 105 Q 160 155 60 105" fill="none" stroke="#f43f5e" stroke-width="3" />
  <circle cx="60" cy="105" r="5" fill="#f43f5e" /><text x="45" y="150" fill="#f43f5e" font-size="12" font-weight="bold">R (End: -20m)</text>
</svg>
</div>
What are the total distance traveled and net displacement of the particle for the entire trip \\(P \\to Q \\to R\\)?`,
    options: [
      { text: 'Distance = \\(140\\text{ m}\\), Displacement = \\(-20\\text{ m}\\)', isCorrect: true },
      { text: 'Distance = \\(80\\text{ m}\\), Displacement = \\(+20\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(140\\text{ m}\\), Displacement = \\(+20\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(60\\text{ m}\\), Displacement = \\(-20\\text{ m}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Leg 1 (P to Q): \\(x_P = 0\\text{ m}\\), \\(x_Q = +60\\text{ m}\\). Distance \\(d_1 = |60 - 0| = 60\\text{ m}\\).
• Leg 2 (Q to R): \\(x_Q = +60\\text{ m}\\), \\(x_R = -20\\text{ m}\\). Distance \\(d_2 = |-20 - 60| = 80\\text{ m}\\).
• Total Distance = \\(d_1 + d_2 = 60 + 80 = 140\\text{ m}\\).
• Net Displacement = \\(x_{\\text{final}} - x_{\\text{initial}} = x_R - x_P = -20\\text{ m} - 0\\text{ m} = -20\\text{ m}\\).
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A farmer walks around the perimeter of a square field \\(ABCD\\) of side \\(L = 10\\text{ m}\\) in \\(40\\text{ seconds}\\) at uniform speed.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 230" width="260" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Square Field -->
  <rect x="50" y="40" width="140" height="140" stroke="#38bdf8" stroke-width="3" fill="none" />
  <!-- Corner Labels -->
  <text x="35" y="40" fill="#22c55e" font-size="14" font-weight="bold">A (0s)</text>
  <text x="195" y="40" fill="#38bdf8" font-size="14" font-weight="bold">B (10s)</text>
  <text x="195" y="195" fill="#eab308" font-size="14" font-weight="bold">C (20s)</text>
  <text x="35" y="195" fill="#f43f5e" font-size="14" font-weight="bold">D (30s)</text>
  <!-- Diagonal AC displacement -->
  <line x1="50" y1="40" x2="190" y2="180" stroke="#ec4899" stroke-width="2.5" stroke-dasharray="6 3" />
  <text x="125" y="100" fill="#ec4899" font-size="12" font-weight="bold">Displacement at 2 min 20 s</text>
  <text x="120" y="30" fill="#94a3b8" font-size="11" text-anchor="middle">10 m</text>
  <text x="210" y="115" fill="#94a3b8" font-size="11" text-anchor="middle">10 m</text>
</svg>
</div>
What will be the magnitude of displacement of the farmer from his initial position at the end of \\(2\\text{ minutes } 20\\text{ seconds}\\)?`,
    options: [
      { text: '\\(10\\sqrt{2}\\text{ m} \\approx 14.14\\text{ m}\\)', isCorrect: true },
      { text: '\\(35\\text{ m}\\)', isCorrect: false },
      { text: '\\(10\\text{ m}\\)', isCorrect: false },
      { text: '\\(0\\text{ m}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Time taken for 1 complete round = \\(40\\text{ s}\\).
• Total elapsed time = \\(2\\text{ min } 20\\text{ s} = 140\\text{ s}\\).
• Number of rounds completed:
\\[\\text{Rounds} = \\frac{140}{40} = 3.5\\text{ rounds}\\]
• After 3 complete rounds, the farmer is back at vertex \\(A\\).
• The remaining 0.5 round takes him from \\(A \\to B \\to C\\) (opposite diagonal corner).
• The net displacement is the straight line diagonal \\(AC\\):
\\[|\\vec{s}| = \\sqrt{AB^2 + BC^2} = \\sqrt{10^2 + 10^2} = \\sqrt{200} = 10\\sqrt{2}\\text{ m} \\approx 14.14\\text{ m}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `The diagram below shows the face of an analog wall clock where the minute hand has a length of \\(r = 14\\text{ cm}\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 260 260" width="220" height="220" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:50%;">
  <circle cx="130" cy="130" r="100" stroke="#475569" stroke-width="4" fill="#1e293b" />
  <!-- Clock Marks -->
  <text x="130" y="52" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">12 (Point P)</text>
  <text x="130" y="222" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">6 (Point Q)</text>
  <!-- Hand at 12 (Initial) -->
  <line x1="130" y1="130" x2="130" y2="60" stroke="#38bdf8" stroke-width="4" />
  <!-- Hand at 6 (Final) -->
  <line x1="130" y1="130" x2="130" y2="200" stroke="#f43f5e" stroke-width="4" stroke-dasharray="4 2" />
  <!-- Centre -->
  <circle cx="130" cy="130" r="6" fill="#facc15" />
  <text x="155" y="95" fill="#38bdf8" font-size="11">r = 14 cm</text>
  <!-- Curving path of tip -->
  <path d="M 130 60 A 70 70 0 0 1 130 200" fill="none" stroke="#22c55e" stroke-width="2.5" />
</svg>
</div>
Between \\(9:00\\text{ AM}\\) and \\(9:30\\text{ AM}\\), what are the distance traveled by the tip of the minute hand and the magnitude of its net displacement vector respectively? (Use \\(\\pi = \\frac{22}{7}\\))`,
    options: [
      { text: 'Distance = \\(44\\text{ cm}\\), Displacement = \\(28\\text{ cm}\\)', isCorrect: true },
      { text: 'Distance = \\(88\\text{ cm}\\), Displacement = \\(0\\text{ cm}\\)', isCorrect: false },
      { text: 'Distance = \\(28\\text{ cm}\\), Displacement = \\(44\\text{ cm}\\)', isCorrect: false },
      { text: 'Distance = \\(44\\text{ cm}\\), Displacement = \\(0\\text{ cm}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• In 30 minutes, the minute hand rotates by \\(180^\\circ\\) from pointing at 12 to pointing at 6.
• The tip traverses a semi-circle of radius \\(r = 14\\text{ cm}\\):
\\[\\text{Distance} = \\pi r = \\frac{22}{7} \\times 14 = 44\\text{ cm}\\]
• Net displacement is the direct straight line separating the tip at 12 and the tip at 6:
\\[|\\vec{s}| = 2r = 2 \\times 14 = 28\\text{ cm}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A speed-time chart compares four different moving objects \\(A, B, C, D\\) over an interval of \\(10\\text{ s}\\) as depicted below.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 300 220" width="280" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Axes -->
  <line x1="40" y1="180" x2="280" y2="180" stroke="#cbd5e1" stroke-width="2" />
  <line x1="40" y1="180" x2="40" y2="20" stroke="#cbd5e1" stroke-width="2" />
  <text x="260" y="200" fill="#cbd5e1" font-size="11">Time (s)</text>
  <text x="20" y="20" fill="#cbd5e1" font-size="11" text-anchor="middle">Speed</text>
  <!-- Curve A: horizontal constant speed -->
  <line x1="40" y1="60" x2="260" y2="60" stroke="#38bdf8" stroke-width="3" />
  <text x="270" y="65" fill="#38bdf8" font-size="12" font-weight="bold">A</text>
  <!-- Curve B: line with positive slope from origin -->
  <line x1="40" y1="180" x2="260" y2="80" stroke="#22c55e" stroke-width="3" />
  <text x="270" y="85" fill="#22c55e" font-size="12" font-weight="bold">B</text>
  <!-- Curve C: line on x-axis (zero speed) -->
  <line x1="40" y1="176" x2="260" y2="176" stroke="#f43f5e" stroke-width="4" />
  <text x="270" y="175" fill="#f43f5e" font-size="12" font-weight="bold">C</text>
  <!-- Curve D: decreasing speed -->
  <line x1="40" y1="80" x2="260" y2="180" stroke="#eab308" stroke-width="3" />
  <text x="270" y="150" fill="#eab308" font-size="12" font-weight="bold">D</text>
</svg>
</div>
Which object is moving with a uniform (constant non-zero) speed throughout the entire observation?`,
    options: [
      { text: 'Object A', isCorrect: true },
      { text: 'Object B', isCorrect: false },
      { text: 'Object C', isCorrect: false },
      { text: 'Object D', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• On a speed-time graph, uniform (constant non-zero) speed is represented by a horizontal straight line parallel to the time axis.
• Line A remains flat at a constant non-zero value, meaning its speed does not change with time.
• Line B represents uniformly accelerating motion, Line C represents an object at rest (speed = 0), and Line D represents uniform deceleration.
• Therefore, Object A represents uniform speed. Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A swimmer wants to cross a river of width \\(d = 120\\text{ m}\\) flowing East at velocity \\(v_r = 3\\text{ m/s}\\). The swimmer swims directly North perpendicular to the flow at \\(v_s = 4\\text{ m/s}\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 220" width="300" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- River banks -->
  <line x1="20" y1="40" x2="300" y2="40" stroke="#94a3b8" stroke-width="3" />
  <line x1="20" y1="180" x2="300" y2="180" stroke="#94a3b8" stroke-width="3" />
  <text x="35" y="115" fill="#38bdf8" font-size="12">River (120m wide)</text>
  <!-- River flow arrow -->
  <line x1="100" y1="110" x2="160" y2="110" stroke="#38bdf8" stroke-width="2.5" />
  <polygon points="160,106 168,110 160,114" fill="#38bdf8" />
  <text x="135" y="98" fill="#38bdf8" font-size="11">v_r = 3 m/s (East)</text>
  <!-- Swimmer velocity vector North -->
  <line x1="80" y1="180" x2="80" y2="80" stroke="#22c55e" stroke-width="3" />
  <polygon points="76,80 80,72 84,80" fill="#22c55e" />
  <text x="95" y="140" fill="#22c55e" font-size="11">v_s = 4 m/s (North)</text>
  <!-- Resultant Path -->
  <line x1="80" y1="180" x2="170" y2="40" stroke="#f43f5e" stroke-width="3" stroke-dasharray="5 3" />
  <polygon points="166,42 173,36 172,46" fill="#f43f5e" />
  <text x="145" y="150" fill="#f43f5e" font-size="11">Resultant v_net</text>
  <!-- Drift point B' -->
  <circle cx="80" cy="40" r="4" fill="#94a3b8" />
  <text x="75" y="30" fill="#94a3b8" font-size="12">Opposite Point</text>
  <circle cx="170" cy="40" r="4" fill="#f43f5e" />
  <text x="175" y="30" fill="#f43f5e" font-size="12">Landing Point</text>
</svg>
</div>
What are the time taken to cross the river and the horizontal downstream drift distance respectively?`,
    options: [
      { text: 'Time = \\(30\\text{ s}\\), Drift = \\(90\\text{ m}\\)', isCorrect: true },
      { text: 'Time = \\(24\\text{ s}\\), Drift = \\(72\\text{ m}\\)', isCorrect: false },
      { text: 'Time = \\(40\\text{ s}\\), Drift = \\(120\\text{ m}\\)', isCorrect: false },
      { text: 'Time = \\(30\\text{ s}\\), Drift = \\(150\\text{ m}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Time to cross depends solely on the perpendicular component of velocity \\(v_s = 4\\text{ m/s}\\):
\\[t = \\frac{d}{v_s} = \\frac{120\\text{ m}}{4\\text{ m/s}} = 30\\text{ s}\\]
• In this time, the river's flow carries the swimmer downstream (East):
\\[\\text{Drift} = v_r \\times t = 3\\text{ m/s} \\times 30\\text{ s} = 90\\text{ m}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A train \\(T_1\\) of length \\(150\\text{ m}\\) travels East at \\(72\\text{ km/h}\\) and another train \\(T_2\\) of length \\(100\\text{ m}\\) travels West on an adjacent parallel track at \\(54\\text{ km/h}\\) as depicted in the vector diagram.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 180" width="320" height="170" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Parallel Tracks -->
  <line x1="20" y1="65" x2="320" y2="65" stroke="#475569" stroke-width="2" stroke-dasharray="8 4" />
  <line x1="20" y1="125" x2="320" y2="125" stroke="#475569" stroke-width="2" stroke-dasharray="8 4" />
  <!-- Train 1 going East -->
  <rect x="40" y="50" width="100" height="30" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
  <text x="90" y="70" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Train 1 (150m)</text>
  <line x1="145" y1="65" x2="195" y2="65" stroke="#38bdf8" stroke-width="3" />
  <polygon points="195,61 205,65 195,69" fill="#38bdf8" />
  <text x="175" y="52" fill="#38bdf8" font-size="11">72 km/h East</text>
  <!-- Train 2 going West -->
  <rect x="200" y="110" width="80" height="30" rx="4" fill="#dc2626" stroke="#f87171" stroke-width="2" />
  <text x="240" y="130" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Train 2 (100m)</text>
  <line x1="195" y1="125" x2="145" y2="125" stroke="#f87171" stroke-width="3" />
  <polygon points="145,121 135,125 145,129" fill="#f87171" />
  <text x="165" y="148" fill="#f87171" font-size="11">54 km/h West</text>
</svg>
</div>
How long will it take for the two trains to completely cross each other from the moment their front ends meet?`,
    options: [
      { text: '\\(7.14\\text{ s}\\) (approx \\(\\frac{50}{7}\\text{ s}\\))', isCorrect: true },
      { text: '\\(14.28\\text{ s}\\)', isCorrect: false },
      { text: '\\(25.0\\text{ s}\\)', isCorrect: false },
      { text: '\\(5.0\\text{ s}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Step 1: Convert speeds to SI units (\\(\\text{m/s}\\)):
\\[v_1 = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\]
\\[v_2 = 54 \\times \\frac{5}{18} = 15\\text{ m/s}\\]
• Step 2: Since they move in opposite directions, their relative speed is:
\\[v_{\\text{rel}} = v_1 + v_2 = 20 + 15 = 35\\text{ m/s}\\]
• Step 3: Total relative distance to completely clear each other:
\\[L = L_1 + L_2 = 150\\text{ m} + 100\\text{ m} = 250\\text{ m}\\]
• Step 4: Time to cross:
\\[t = \\frac{L}{v_{\\text{rel}}} = \\frac{250}{35} = \\frac{50}{7} \\approx 7.14\\text{ s}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A toy car travels from point \\(A\\) to \\(B\\) at a constant speed of \\(v_1 = 30\\text{ km/h}\\), and immediately returns from \\(B\\) back to \\(A\\) along the exact same path at \\(v_2 = 20\\text{ km/h}\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 160" width="300" height="150" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Track line AB -->
  <line x1="50" y1="80" x2="270" y2="80" stroke="#475569" stroke-width="2" />
  <!-- Forward vector v1 -->
  <line x1="60" y1="60" x2="250" y2="60" stroke="#38bdf8" stroke-width="3" />
  <polygon points="250,56 260,60 250,64" fill="#38bdf8" />
  <text x="160" y="48" fill="#38bdf8" font-size="12" text-anchor="middle">Forward: v1 = 30 km/h (Distance d)</text>
  <!-- Return vector v2 -->
  <line x1="250" y1="100" x2="60" y2="100" stroke="#f43f5e" stroke-width="3" />
  <polygon points="60,96 50,100 60,104" fill="#f43f5e" />
  <text x="160" y="122" fill="#f43f5e" font-size="12" text-anchor="middle">Return: v2 = 20 km/h (Distance d)</text>
  <!-- Endpoints -->
  <circle cx="50" cy="80" r="5" fill="#22c55e" /><text x="35" y="85" fill="#22c55e" font-size="14" font-weight="bold">A</text>
  <circle cx="270" cy="80" r="5" fill="#eab308" /><text x="280" y="85" fill="#eab308" font-size="14" font-weight="bold">B</text>
</svg>
</div>
What are the average speed and the average velocity of the toy car for the entire round trip?`,
    options: [
      { text: 'Average speed = \\(24\\text{ km/h}\\), Average velocity = \\(0\\text{ km/h}\\)', isCorrect: true },
      { text: 'Average speed = \\(25\\text{ km/h}\\), Average velocity = \\(0\\text{ km/h}\\)', isCorrect: false },
      { text: 'Average speed = \\(24\\text{ km/h}\\), Average velocity = \\(24\\text{ km/h}\\)', isCorrect: false },
      { text: 'Average speed = \\(25\\text{ km/h}\\), Average velocity = \\(25\\text{ km/h}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Let the one-way distance between A and B be \\(d\\). Total distance = \\(2d\\).
• Total displacement is zero because the car returns to its starting point \\(A\\). Therefore, \\(\\vec{v}_{\\text{avg}} = 0\\text{ km/h}\\).
• Time taken forward: \\(t_1 = \\frac{d}{30}\\).
• Time taken return: \\(t_2 = \\frac{d}{20}\\).
• Average speed is the harmonic mean:
\\[v_{\\text{avg}} = \\frac{2d}{t_1 + t_2} = \\frac{2d}{\\frac{d}{30} + \\frac{d}{20}} = \\frac{2 \\times 30 \\times 20}{30 + 20} = \\frac{1200}{50} = 24\\text{ km/h}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A vehicle’s dashboard instruments are observed during a test drive. The speedometer indicator and odometer display are recorded at the start and end of a 30-minute journey as represented below.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 180" width="300" height="170" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Odometer reading box -->
  <rect x="30" y="30" width="260" height="50" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2" />
  <text x="45" y="50" fill="#94a3b8" font-size="11">Initial Odometer (9:00 AM):</text>
  <text x="45" y="70" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold">2450.0 km</text>
  <rect x="30" y="95" width="260" height="50" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2" />
  <text x="45" y="115" fill="#94a3b8" font-size="11">Final Odometer (9:30 AM):</text>
  <text x="45" y="135" fill="#22c55e" font-size="14" font-family="monospace" font-weight="bold">2475.0 km</text>
</svg>
</div>
What physical quantity does the odometer measure, and what is the average speed of the vehicle during this 30-minute interval?`,
    options: [
      { text: 'Odometer measures distance; Average speed = \\(50\\text{ km/h}\\)', isCorrect: true },
      { text: 'Odometer measures displacement; Average speed = \\(25\\text{ km/h}\\)', isCorrect: false },
      { text: 'Odometer measures instantaneous velocity; Average speed = \\(50\\text{ km/h}\\)', isCorrect: false },
      { text: 'Odometer measures acceleration; Average speed = \\(100\\text{ km/h}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• An odometer in a motor vehicle records the actual path length traversed, which is distance (not displacement).
• Distance traversed: \\(\\Delta s = 2475.0 - 2450.0 = 25\\text{ km}\\).
• Time interval: \\(\\Delta t = 30\\text{ minutes} = 0.5\\text{ hours}\\).
• Average speed:
\\[v_{\\text{avg}} = \\frac{\\Delta s}{\\Delta t} = \\frac{25\\text{ km}}{0.5\\text{ h}} = 50\\text{ km/h}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `A boy walks on a grid from point \\(A(0,0)\\) to \\(B(4\\text{m}, 0)\\), then to \\(C(4\\text{m}, 3\\text{m})\\), and finally to \\(D(0, 3\\text{m})\\) as shown in the Cartesian grid diagram below.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 220" width="260" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Grid -->
  <line x1="50" y1="170" x2="230" y2="170" stroke="#334155" stroke-width="1.5" />
  <line x1="50" y1="170" x2="50" y2="40" stroke="#334155" stroke-width="1.5" />
  <!-- Path A -> B -> C -> D -->
  <line x1="50" y1="170" x2="210" y2="170" stroke="#38bdf8" stroke-width="3" />
  <line x1="210" y1="170" x2="210" y2="70" stroke="#38bdf8" stroke-width="3" />
  <line x1="210" y1="70" x2="50" y2="70" stroke="#38bdf8" stroke-width="3" />
  <!-- Displacement vector AD -->
  <line x1="50" y1="170" x2="50" y2="70" stroke="#f43f5e" stroke-width="3.5" stroke-dasharray="5 3" />
  <!-- Vertices -->
  <circle cx="50" cy="170" r="5" fill="#22c55e" /><text x="30" y="185" fill="#22c55e" font-size="12" font-weight="bold">A (0,0)</text>
  <circle cx="210" cy="170" r="4" fill="#cbd5e1" /><text x="215" y="185" fill="#cbd5e1" font-size="12">B (4,0)</text>
  <circle cx="210" cy="70" r="4" fill="#cbd5e1" /><text x="215" y="65" fill="#cbd5e1" font-size="12">C (4,3)</text>
  <circle cx="50" cy="70" r="5" fill="#f43f5e" /><text x="25" y="65" fill="#f43f5e" font-size="12" font-weight="bold">D (0,3)</text>
</svg>
</div>
What are the total distance traveled and the magnitude of net displacement vector \\(\\vec{AD}\\)?`,
    options: [
      { text: 'Distance = \\(11\\text{ m}\\), Displacement = \\(3\\text{ m}\\)', isCorrect: true },
      { text: 'Distance = \\(14\\text{ m}\\), Displacement = \\(0\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(11\\text{ m}\\), Displacement = \\(5\\text{ m}\\)', isCorrect: false },
      { text: 'Distance = \\(7\\text{ m}\\), Displacement = \\(3\\text{ m}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Leg 1 \\(AB\\): from \\((0,0)\\) to \\((4,0)\\) length = \\(4\\text{ m}\\).
• Leg 2 \\(BC\\): from \\((4,0)\\) to \\((4,3)\\) length = \\(3\\text{ m}\\).
• Leg 3 \\(CD\\): from \\((4,3)\\) to \\((0,3)\\) length = \\(4\\text{ m}\\).
• Total distance = \\(4 + 3 + 4 = 11\\text{ m}\\).
• Net displacement is the direct vector from initial point \\(A(0,0)\\) to final point \\(D(0,3)\\):
\\[|\\vec{AD}| = \\sqrt{(0 - 0)^2 + (3 - 0)^2} = 3\\text{ m}\\text{ (due North)}\\]
Correct Choice is (A).`
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    boardCode: 'MH',
    class: '9',
    subjectCode: 'SCIT',
    board: 'Maharashtra Board',
    subject: 'Science and Technology',
    chapterNumber: 1,
    chapter: 'Laws of Motion',
    topic: 'Distance, Displacement, Speed and Velocity',
    topicName: 'Distance, Displacement, Speed and Velocity',
    type: 'OSC',
    vault: 'mock',
    examCategory: 'foundation',
    requiresFigure: true,
    difficulty: 'hard',
    bloomLevel: 'Analyze',
    marks: 4,
    text: `An object starts from rest at point \\(O\\) and completes three stages of motion on a straight line: \\(20\\text{ m}\\) East in \\(2\\text{ s}\\), then \\(40\\text{ m}\\) East in \\(3\\text{ s}\\), and finally \\(30\\text{ m}\\) West in \\(5\\text{ s}\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 150" width="300" height="140" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Line -->
  <line x1="30" y1="90" x2="290" y2="90" stroke="#475569" stroke-width="2" />
  <!-- Vectors -->
  <line x1="50" y1="70" x2="120" y2="70" stroke="#38bdf8" stroke-width="3" />
  <text x="85" y="60" fill="#38bdf8" font-size="11" text-anchor="middle">+20m (2s)</text>
  <line x1="120" y1="70" x2="260" y2="70" stroke="#22c55e" stroke-width="3" />
  <text x="190" y="60" fill="#22c55e" font-size="11" text-anchor="middle">+40m (3s)</text>
  <line x1="260" y1="110" x2="160" y2="110" stroke="#f43f5e" stroke-width="3" />
  <text x="210" y="130" fill="#f43f5e" font-size="11" text-anchor="middle">-30m (5s)</text>
  <circle cx="50" cy="90" r="5" fill="#f8fafc" /><text x="50" y="108" fill="#f8fafc" font-size="11" text-anchor="middle">O(0m)</text>
  <circle cx="160" cy="90" r="5" fill="#facc15" /><text x="160" y="108" fill="#facc15" font-size="11" text-anchor="middle">End(+30m)</text>
</svg>
</div>
What are the average speed and the average velocity of the object for the entire \\(10\\text{ second}\\) interval?`,
    options: [
      { text: 'Average speed = \\(9\\text{ m/s}\\), Average velocity = \\(3\\text{ m/s}\\)', isCorrect: true },
      { text: 'Average speed = \\(3\\text{ m/s}\\), Average velocity = \\(9\\text{ m/s}\\)', isCorrect: false },
      { text: 'Average speed = \\(9\\text{ m/s}\\), Average velocity = \\(9\\text{ m/s}\\)', isCorrect: false },
      { text: 'Average speed = \\(6\\text{ m/s}\\), Average velocity = \\(0\\text{ m/s}\\)', isCorrect: false }
    ],
    correctAnswer: 'A',
    solution: `• Total Distance = \\(20 + 40 + 30 = 90\\text{ m}\\).
• Total Time = \\(2 + 3 + 5 = 10\\text{ s}\\).
• Average speed:
\\[v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{90}{10} = 9\\text{ m/s}\\]
• Net Displacement = \\(+20 + 40 - 30 = +30\\text{ m}\\) (East).
• Average velocity:
\\[\\vec{v}_{\\text{avg}} = \\frac{\\text{Displacement}}{\\text{Total Time}} = \\frac{+30}{10} = +3\\text{ m/s}\\]
Correct Choice is (A).`
  }
];

async function rebalanceTopic1() {
  console.log('--- REBALANCING TOPIC MH-9-SCIT-1-1.1 ---');
  const snap = await db.collection('questions')
    .where('topicCode', '==', 'MH-9-SCIT-1-1.1')
    .get();

  console.log('Total current questions in Topic 1.1:', snap.size);
  const docs = snap.docs;

  // Verify none are used
  // First 40 -> vault: 'exam'
  // Next 30 -> vault: 'practice'
  // The rest -> archive / delete surplus unused

  const batch = db.batch();
  let updatedExam = 0;
  let updatedPractice = 0;
  let deletedSurplus = 0;

  for (let i = 0; i < docs.length; i++) {
    const docRef = docs[i].ref;
    if (i < 40) {
      batch.update(docRef, {
        vault: 'exam',
        examCategory: 'standard',
        pool: 'exam',
        updatedAt: new Date()
      });
      updatedExam++;
    } else if (i < 70) {
      batch.update(docRef, {
        vault: 'practice',
        examCategory: 'standard',
        pool: 'practice',
        updatedAt: new Date()
      });
      updatedPractice++;
    } else {
      batch.delete(docRef);
      deletedSurplus++;
    }
  }

  await batch.commit();
  console.log(`Updated ${updatedExam} questions to vault 'exam'`);
  console.log(`Updated ${updatedPractice} questions to vault 'practice'`);
  console.log(`Deleted ${deletedSurplus} surplus unused questions`);

  // Now insert the 12 Foundation questions into vault: 'mock'
  console.log('Inserting 12 Foundation Diagram questions into vault mock...');
  const batch2 = db.batch();
  for (let i = 0; i < topic1_foundation_questions.length; i++) {
    const qData = topic1_foundation_questions[i];
    const qCode = `MH-9-SCIT-1-1.1-OSC-5${String(i + 1).padStart(2, '0')}`;
    const docRef = db.collection('questions').doc(qCode);
    batch2.set(docRef, {
      ...qData,
      questionCode: qCode,
      createdAt: new Date(),
      updatedAt: new Date(),
      timesUsed: 0,
      usedInClassroomTest: false
    });
  }
  await batch2.commit();
  console.log('Successfully committed 12 Foundation Diagram questions to Topic 1.1!');
}

rebalanceTopic1().catch(console.error);
