// Part 1: Subtopics 1.1.1 (5 Qs), 1.1.2 (10 Qs), 1.1.3 (15 Qs), 1.2.2 (16 Qs) = 46 Questions

const part1Questions = [
  // --- Subtopic 1.1.1 (5 Questions) ---
  {
    subtopicNumber: '1.1.1',
    type: 'OSC',
    text: 'A person completes one full round around a circular track of radius \\(14\\text{ m}\\) and returns to the starting point. What are the distance travelled and the displacement of the person? (Use \\(\\pi = \\frac{22}{7}\\))',
    options: [
      'Distance = \\(88\\text{ m}\\), Displacement = \\(0\\text{ m}\\)',
      'Distance = \\(0\\text{ m}\\), Displacement = \\(88\\text{ m}\\)',
      'Distance = \\(88\\text{ m}\\), Displacement = \\(28\\text{ m}\\)',
      'Distance = \\(44\\text{ m}\\), Displacement = \\(0\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Distance is the total actual path length covered by a body, whereas displacement is the shortest straight-line distance between the initial and final positions.\n\n**Step 2: Formula & Calculation**: Total distance is the circumference of the circle: \\(s = 2\\pi r = 2 \\times \\frac{22}{7} \\times 14 = 88\\text{ m}\\). Since the person returns to the initial starting point, initial position = final position, so displacement = \\(0\\text{ m}\\).\n\n**Step 3: Verification**: Distance is a scalar with magnitude \\(88\\text{ m}\\); displacement is a vector with magnitude \\(0\\text{ m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Distance is the total actual path length covered by a body, whereas displacement is the shortest straight-line distance between the initial and final positions.\n\n**Step 2: Formula & Calculation**: Total distance is the circumference of the circle: \\(s = 2\\pi r = 2 \\times \\frac{22}{7} \\times 14 = 88\\text{ m}\\). Since the person returns to the initial starting point, initial position = final position, so displacement = \\(0\\text{ m}\\).\n\n**Step 3: Verification**: Distance is a scalar with magnitude \\(88\\text{ m}\\); displacement is a vector with magnitude \\(0\\text{ m}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.1',
    type: 'OSC',
    text: 'An athlete runs from corner \\(A\\) to the diagonally opposite corner \\(C\\) of a rectangular field of length \\(40\\text{ m}\\) and breadth \\(30\\text{ m}\\) along the boundary \\(A \\to B \\to C\\). What is the magnitude of the athlete\'s displacement?',
    options: [
      '\\(50\\text{ m}\\)',
      '\\(70\\text{ m}\\)',
      '\\(10\\text{ m}\\)',
      '\\(120\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Displacement is the length of the straight line connecting the initial point \\(A\\) and final point \\(C\\).\n\n**Step 2: Formula & Calculation**: By Pythagoras theorem, \\(\\text{Displacement} = \\sqrt{\\text{length}^2 + \\text{breadth}^2} = \\sqrt{40^2 + 30^2} = \\sqrt{1600 + 900} = \\sqrt{2500} = 50\\text{ m}\\).\n\n**Step 3: Verification**: The path distance is \\(40 + 30 = 70\\text{ m}\\), but displacement is the diagonal \\(50\\text{ m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Displacement is the length of the straight line connecting the initial point \\(A\\) and final point \\(C\\).\n\n**Step 2: Formula & Calculation**: By Pythagoras theorem, \\(\\text{Displacement} = \\sqrt{\\text{length}^2 + \\text{breadth}^2} = \\sqrt{40^2 + 30^2} = \\sqrt{1600 + 900} = \\sqrt{2500} = 50\\text{ m}\\).\n\n**Step 3: Verification**: The path distance is \\(40 + 30 = 70\\text{ m}\\), but displacement is the diagonal \\(50\\text{ m}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.1',
    type: 'OSC',
    text: 'Under which of the following conditions is the magnitude of displacement strictly equal to the distance travelled by an object?',
    options: [
      'The object moves along a straight line in a fixed direction without reversing',
      'The object moves in a circular path at constant speed',
      'The object moves along a straight line and then reverses its direction',
      'The object oscillates back and forth like a simple pendulum'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Distance \\(s\\) is always greater than or equal to the magnitude of displacement \\(|\\vec{d}|\\) (i.e., \\(s \\ge |\\vec{d}|\\)).\n\n**Step 2: Condition for Equality**: Equality \\(s = |\\vec{d}|\\) holds if and only if the motion is strictly rectilinear (along a straight line) and unidirectional (without any turnaround or backtracking).\n\n**Step 3: Verification**: In circular, reversing, or oscillating motion, the path length exceeds the net straight-line distance. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Distance \\(s\\) is always greater than or equal to the magnitude of displacement \\(|\\vec{d}|\\) (i.e., \\(s \\ge |\\vec{d}|\\)).\n\n**Step 2: Condition for Equality**: Equality \\(s = |\\vec{d}|\\) holds if and only if the motion is strictly rectilinear (along a straight line) and unidirectional (without any turnaround or backtracking).\n\n**Step 3: Verification**: In circular, reversing, or oscillating motion, the path length exceeds the net straight-line distance. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.1',
    type: 'OSC',
    text: 'A particle moves \\(6\\text{ m}\\) due East, then \\(8\\text{ m}\\) due North. What is the ratio of distance travelled to magnitude of displacement?',
    options: [
      '\\(1.4\\)',
      '\\(0.71\\)',
      '\\(1.0\\)',
      '\\(2.0\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Distance is scalar sum of paths, while displacement is the vector hypotenuse.\n\n**Step 2: Calculation**: Distance \\(= 6 + 8 = 14\\text{ m}\\). Displacement \\(= \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ m}\\). Ratio \\(= \\frac{14}{10} = 1.4\\).\n\n**Step 3: Verification**: Since path length is \\(14\\text{ m}\\) and displacement is \\(10\\text{ m}\\), the ratio is \\(1.4\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Distance is scalar sum of paths, while displacement is the vector hypotenuse.\n\n**Step 2: Calculation**: Distance \\(= 6 + 8 = 14\\text{ m}\\). Displacement \\(= \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ m}\\). Ratio \\(= \\frac{14}{10} = 1.4\\).\n\n**Step 3: Verification**: Since path length is \\(14\\text{ m}\\) and displacement is \\(10\\text{ m}\\), the ratio is \\(1.4\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.1',
    type: 'OSC',
    text: 'Which of the following statements comparing distance and displacement is FALSE?',
    options: [
      'Distance can be zero even when displacement is non-zero',
      'Displacement can be zero even when distance is non-zero',
      'Distance is a scalar quantity while displacement is a vector quantity',
      'The magnitude of displacement can never exceed distance'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Distance is the total length of path travelled. If a body moves at all, its distance must be strictly positive (\\(s > 0\\)).\n\n**Step 2: Analysis of False Statement**: If distance is zero, the body has not moved at all, which means displacement must also be zero. Therefore, it is impossible for distance to be zero while displacement is non-zero.\n\n**Step 3: Conclusion**: Statement A is false and thus the correct answer to the question. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Distance is the total length of path travelled. If a body moves at all, its distance must be strictly positive (\\(s > 0\\)).\n\n**Step 2: Analysis of False Statement**: If distance is zero, the body has not moved at all, which means displacement must also be zero. Therefore, it is impossible for distance to be zero while displacement is non-zero.\n\n**Step 3: Conclusion**: Statement A is false and thus the correct answer to the question. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.1.2 (10 Questions) ---
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A car travels a distance of \\(180\\text{ km}\\) in \\(3\\text{ hours}\\). What is its average speed in \\(\\text{m/s}\\)?',
    options: [
      '\\(16.67\\text{ m/s}\\)',
      '\\(60\\text{ m/s}\\)',
      '\\(25\\text{ m/s}\\)',
      '\\(50\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total Distance}}{\\text{Total Time}}\\). To convert \\(\\text{km/h}\\) to \\(\\text{m/s}\\), multiply by \\(\\frac{5}{18}\\).\n\n**Step 2: Calculation**: Speed in \\(\\text{km/h} = \\frac{180}{3} = 60\\text{ km/h}\\). Speed in \\(\\text{m/s} = 60 \\times \\frac{5}{18} = \\frac{50}{3} \\approx 16.67\\text{ m/s}\\).\n\n**Step 3: Verification**: \\(16.67 \\times 3600 = 60012\\text{ m} \\approx 60\\text{ km}\\) in 1 hour. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total Distance}}{\\text{Total Time}}\\). To convert \\(\\text{km/h}\\) to \\(\\text{m/s}\\), multiply by \\(\\frac{5}{18}\\).\n\n**Step 2: Calculation**: Speed in \\(\\text{km/h} = \\frac{180}{3} = 60\\text{ km/h}\\). Speed in \\(\\text{m/s} = 60 \\times \\frac{5}{18} = \\frac{50}{3} \\approx 16.67\\text{ m/s}\\).\n\n**Step 3: Verification**: \\(16.67 \\times 3600 = 60012\\text{ m} \\approx 60\\text{ km}\\) in 1 hour. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A train travels from station \\(P\\) to \\(Q\\) at a uniform speed of \\(40\\text{ km/h}\\) and returns from \\(Q\\) to \\(P\\) along the same track at \\(60\\text{ km/h}\\). What is the average speed of the train for the entire round trip?',
    options: [
      '\\(48\\text{ km/h}\\)',
      '\\(50\\text{ km/h}\\)',
      '\\(52\\text{ km/h}\\)',
      '\\(0\\text{ km/h}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: For equal distances covered at speeds \\(v_1\\) and \\(v_2\\), average speed is the harmonic mean: \\(v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}\\).\n\n**Step 2: Calculation**: \\(v_{\\text{avg}} = \\frac{2 \\times 40 \\times 60}{40 + 60} = \\frac{4800}{100} = 48\\text{ km/h}\\).\n\n**Step 3: Verification**: Note that average velocity is \\(0\\text{ km/h}\\) because net displacement is zero, but average speed is \\(48\\text{ km/h}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: For equal distances covered at speeds \\(v_1\\) and \\(v_2\\), average speed is the harmonic mean: \\(v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2}\\).\n\n**Step 2: Calculation**: \\(v_{\\text{avg}} = \\frac{2 \\times 40 \\times 60}{40 + 60} = \\frac{4800}{100} = 48\\text{ km/h}\\).\n\n**Step 3: Verification**: Note that average velocity is \\(0\\text{ km/h}\\) because net displacement is zero, but average speed is \\(48\\text{ km/h}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A bus moves with a speed of \\(20\\text{ m/s}\\) for \\(10\\text{ s}\\) and then with a speed of \\(30\\text{ m/s}\\) for the next \\(20\\text{ s}\\) along a straight line in the same direction. What is its average speed during this \\(30\\text{ s}\\) interval?',
    options: [
      '\\(26.67\\text{ m/s}\\)',
      '\\(25.00\\text{ m/s}\\)',
      '\\(24.00\\text{ m/s}\\)',
      '\\(28.33\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total distance}}{\\text{Total time}} = \\frac{s_1 + s_2}{t_1 + t_2}\\).\n\n**Step 2: Calculation**: \\(s_1 = v_1 t_1 = 20 \\times 10 = 200\\text{ m}\\). \\(s_2 = v_2 t_2 = 30 \\times 20 = 600\\text{ m}\\). Total distance \\(= 200 + 600 = 800\\text{ m}\\). Total time \\(= 10 + 20 = 30\\text{ s}\\). \\(v_{\\text{avg}} = \\frac{800}{30} = 26.67\\text{ m/s}\\).\n\n**Step 3: Verification**: Since more time (20 s vs 10 s) was spent at \\(30\\text{ m/s}\\), the average speed is weighted closer to \\(30\\) than \\(20\\) (\\(26.67\\text{ m/s}\\)). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total distance}}{\\text{Total time}} = \\frac{s_1 + s_2}{t_1 + t_2}\\).\n\n**Step 2: Calculation**: \\(s_1 = v_1 t_1 = 20 \\times 10 = 200\\text{ m}\\). \\(s_2 = v_2 t_2 = 30 \\times 20 = 600\\text{ m}\\). Total distance \\(= 200 + 600 = 800\\text{ m}\\). Total time \\(= 10 + 20 = 30\\text{ s}\\). \\(v_{\\text{avg}} = \\frac{800}{30} = 26.67\\text{ m/s}\\).\n\n**Step 3: Verification**: Since more time (20 s vs 10 s) was spent at \\(30\\text{ m/s}\\), the average speed is weighted closer to \\(30\\) than \\(20\\) (\\(26.67\\text{ m/s}\\)). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'What instrument fitted in an automobile indicates the instantaneous speed of the vehicle?',
    options: [
      'Speedometer',
      'Odometer',
      'Tachometer',
      'Barometer'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: In vehicles, instruments measure different motion metrics.\n\n**Step 2: Distinctions**: The speedometer measures the instantaneous speed at any given second (in km/h). The odometer measures the cumulative total distance travelled (in km).\n\n**Step 3: Conclusion**: The instrument measuring instantaneous speed is the speedometer. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: In vehicles, instruments measure different motion metrics.\n\n**Step 2: Distinctions**: The speedometer measures the instantaneous speed at any given second (in km/h). The odometer measures the cumulative total distance travelled (in km).\n\n**Step 3: Conclusion**: The instrument measuring instantaneous speed is the speedometer. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'Convert a velocity of \\(54\\text{ km/h}\\) into \\(\\text{m/s}\\).',
    options: [
      '\\(15\\text{ m/s}\\)',
      '\\(20\\text{ m/s}\\)',
      '\\(12\\text{ m/s}\\)',
      '\\(18\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: To convert \\(\\text{km/h}\\) to \\(\\text{m/s}\\), multiply by \\(\\frac{5}{18}\\).\n\n**Step 2: Calculation**: \\(54 \\times \\frac{5}{18} = 3 \\times 5 = 15\\text{ m/s}\\).\n\n**Step 3: Verification**: \\(15\\text{ m/s} \\times 3600\\text{ s/h} = 54000\\text{ m/h} = 54\\text{ km/h}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: To convert \\(\\text{km/h}\\) to \\(\\text{m/s}\\), multiply by \\(\\frac{5}{18}\\).\n\n**Step 2: Calculation**: \\(54 \\times \\frac{5}{18} = 3 \\times 5 = 15\\text{ m/s}\\).\n\n**Step 3: Verification**: \\(15\\text{ m/s} \\times 3600\\text{ s/h} = 54000\\text{ m/h} = 54\\text{ km/h}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A runner sprints along a straight track of length \\(100\\text{ m}\\) in \\(10\\text{ s}\\) and immediately walks back \\(50\\text{ m}\\) towards the starting line in \\(10\\text{ s}\\). What are the average speed and average velocity of the runner?',
    options: [
      'Average speed = \\(7.5\\text{ m/s}\\), Average velocity = \\(2.5\\text{ m/s}\\)',
      'Average speed = \\(2.5\\text{ m/s}\\), Average velocity = \\(7.5\\text{ m/s}\\)',
      'Average speed = \\(5.0\\text{ m/s}\\), Average velocity = \\(5.0\\text{ m/s}\\)',
      'Average speed = \\(10.0\\text{ m/s}\\), Average velocity = \\(0\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total distance}}{\\text{Total time}}\\); Average velocity \\(= \\frac{\\text{Net displacement}}{\\text{Total time}}\\).\n\n**Step 2: Calculation**: Total distance \\(= 100 + 50 = 150\\text{ m}\\). Net displacement \\(= 100 - 50 = 50\\text{ m}\\). Total time \\(= 10 + 10 = 20\\text{ s}\\). Average speed \\(= \\frac{150}{20} = 7.5\\text{ m/s}\\). Average velocity \\(= \\frac{50}{20} = 2.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: Average speed is \\(7.5\\text{ m/s}\\) and average velocity is \\(2.5\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Average speed \\(= \\frac{\\text{Total distance}}{\\text{Total time}}\\); Average velocity \\(= \\frac{\\text{Net displacement}}{\\text{Total time}}\\).\n\n**Step 2: Calculation**: Total distance \\(= 100 + 50 = 150\\text{ m}\\). Net displacement \\(= 100 - 50 = 50\\text{ m}\\). Total time \\(= 10 + 10 = 20\\text{ s}\\). Average speed \\(= \\frac{150}{20} = 7.5\\text{ m/s}\\). Average velocity \\(= \\frac{50}{20} = 2.5\\text{ m/s}\\).\n\n**Step 3: Conclusion**: Average speed is \\(7.5\\text{ m/s}\\) and average velocity is \\(2.5\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A car covers the first half of a total distance at \\(30\\text{ km/h}\\) and the remaining half at \\(20\\text{ km/h}\\). What is the average speed of the car for the entire journey?',
    options: [
      '\\(24\\text{ km/h}\\)',
      '\\(25\\text{ km/h}\\)',
      '\\(26\\text{ km/h}\\)',
      '\\(22\\text{ km/h}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: When two halves of a journey distance are covered at speeds \\(v_1\\) and \\(v_2\\), average speed is \\(\\frac{2 v_1 v_2}{v_1 + v_2}\\).\n\n**Step 2: Calculation**: \\(v_{\\text{avg}} = \\frac{2 \\times 30 \\times 20}{30 + 20} = \\frac{1200}{50} = 24\\text{ km/h}\\).\n\n**Step 3: Verification**: Arithmetic mean is \\(25\\text{ km/h}\\), but because more time is spent travelling at the lower speed, harmonic mean \\(24\\text{ km/h}\\) correctly gives the true average speed. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: When two halves of a journey distance are covered at speeds \\(v_1\\) and \\(v_2\\), average speed is \\(\\frac{2 v_1 v_2}{v_1 + v_2}\\).\n\n**Step 2: Calculation**: \\(v_{\\text{avg}} = \\frac{2 \\times 30 \\times 20}{30 + 20} = \\frac{1200}{50} = 24\\text{ km/h}\\).\n\n**Step 3: Verification**: Arithmetic mean is \\(25\\text{ km/h}\\), but because more time is spent travelling at the lower speed, harmonic mean \\(24\\text{ km/h}\\) correctly gives the true average speed. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'Which of the following statements about velocity is TRUE?',
    options: [
      'Velocity changes whenever speed changes, direction changes, or both change',
      'Velocity depends only on the speed of the object and is independent of direction',
      'A body moving in a curved path at constant speed has constant velocity',
      'Average velocity can never be negative'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Velocity is a vector quantity that has both magnitude (speed) and direction.\n\n**Step 2: Analysis**: Since \\(\\vec{v}\\) has both magnitude and direction, it changes if either magnitude (speed) changes, direction of motion changes, or both change.\n\n**Step 3: Conclusion**: Statement A is correct. A body in curved motion at constant speed undergoes continuous acceleration because its direction of velocity changes continuously. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Velocity is a vector quantity that has both magnitude (speed) and direction.\n\n**Step 2: Analysis**: Since \\(\\vec{v}\\) has both magnitude and direction, it changes if either magnitude (speed) changes, direction of motion changes, or both change.\n\n**Step 3: Conclusion**: Statement A is correct. A body in curved motion at constant speed undergoes continuous acceleration because its direction of velocity changes continuously. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'A sound wave travels through air at \\(340\\text{ m/s}\\). A lightning flash is observed, and the thunderclap is heard \\(5\\text{ s}\\) later. Approximately how far away is the storm lightning strike?',
    options: [
      '\\(1700\\text{ m}\\)',
      '\\(68\\text{ m}\\)',
      '\\(850\\text{ m}\\)',
      '\\(3400\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Light travels almost instantaneously (\\(3 \\times 10^8\\text{ m/s}\\)). The time delay is due to the speed of sound: \\(\\text{Distance} = \\text{Speed of sound} \\times \\text{Time}\\).\n\n**Step 2: Calculation**: \\(s = v \\times t = 340 \\times 5 = 1700\\text{ m} = 1.7\\text{ km}\\).\n\n**Step 3: Conclusion**: The lightning strike occurred \\(1700\\text{ m}\\) away. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Light travels almost instantaneously (\\(3 \\times 10^8\\text{ m/s}\\)). The time delay is due to the speed of sound: \\(\\text{Distance} = \\text{Speed of sound} \\times \\text{Time}\\).\n\n**Step 2: Calculation**: \\(s = v \\times t = 340 \\times 5 = 1700\\text{ m} = 1.7\\text{ km}\\).\n\n**Step 3: Conclusion**: The lightning strike occurred \\(1700\\text{ m}\\) away. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.2',
    type: 'OSC',
    text: 'If a car travels \\(72\\text{ km/h}\\) for \\(20\\text{ minutes}\\), how much distance does it cover in kilometers?',
    options: [
      '\\(24\\text{ km}\\)',
      '\\(36\\text{ km}\\)',
      '\\(14.4\\text{ km}\\)',
      '\\(72\\text{ km}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(\\text{Distance} = \\text{Speed} \\times \\text{Time}\\).\n\n**Step 2: Calculation**: Convert time to hours: \\(t = \\frac{20}{60} = \\frac{1}{3}\\text{ hour}\\). Distance \\(s = 72 \\times \\frac{1}{3} = 24\\text{ km}\\).\n\n**Step 3: Conclusion**: The car covers \\(24\\text{ km}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(\\text{Distance} = \\text{Speed} \\times \\text{Time}\\).\n\n**Step 2: Calculation**: Convert time to hours: \\(t = \\frac{20}{60} = \\frac{1}{3}\\text{ hour}\\). Distance \\(s = 72 \\times \\frac{1}{3} = 24\\text{ km}\\).\n\n**Step 3: Conclusion**: The car covers \\(24\\text{ km}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // --- Subtopic 1.1.3 (15 Questions: Uniform vs non-uniform motion along straight line) ---
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'A car covers \\(15\\text{ m}\\) in the 1st second, \\(15\\text{ m}\\) in the 2nd second, \\(15\\text{ m}\\) in the 3rd second, and \\(15\\text{ m}\\) in the 4th second along a straight highway. What type of motion is the car undergoing?',
    options: [
      'Uniform rectilinear motion',
      'Non-uniform accelerated motion',
      'Uniformly decelerated motion',
      'Oscillatory motion'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: When an object covers equal distances in equal intervals of time along a straight line, however small these intervals may be, the motion is defined as uniform rectilinear motion.\n\n**Step 2: Analysis**: Here, the distance in each \\(1\\text{ s}\\) interval is constantly \\(15\\text{ m}\\). The speed is constant at \\(15\\text{ m/s}\\) with unchanging direction.\n\n**Step 3: Conclusion**: The car is in uniform rectilinear motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: When an object covers equal distances in equal intervals of time along a straight line, however small these intervals may be, the motion is defined as uniform rectilinear motion.\n\n**Step 2: Analysis**: Here, the distance in each \\(1\\text{ s}\\) interval is constantly \\(15\\text{ m}\\). The speed is constant at \\(15\\text{ m/s}\\) with unchanging direction.\n\n**Step 3: Conclusion**: The car is in uniform rectilinear motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'A bus travels in crowded city traffic, covering \\(10\\text{ m}\\) in the first second, \\(4\\text{ m}\\) in the second, \\(18\\text{ m}\\) in the third, and \\(2\\text{ m}\\) in the fourth second. What type of motion does this represent?',
    options: [
      'Non-uniform motion',
      'Uniform rectilinear motion',
      'Periodic motion',
      'Uniform circular motion'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: When an object covers unequal distances in equal intervals of time, its motion is non-uniform.\n\n**Step 2: Analysis**: The distances covered in consecutive 1-second intervals vary widely (10 m, 4 m, 18 m, 2 m) due to braking, stopping, and accelerating.\n\n**Step 3: Conclusion**: This is non-uniform motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: When an object covers unequal distances in equal intervals of time, its motion is non-uniform.\n\n**Step 2: Analysis**: The distances covered in consecutive 1-second intervals vary widely (10 m, 4 m, 18 m, 2 m) due to braking, stopping, and accelerating.\n\n**Step 3: Conclusion**: This is non-uniform motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'What is the acceleration of a train moving with uniform velocity along a straight track?',
    options: [
      '\\(0\\text{ m/s}^2\\)',
      '\\(9.8\\text{ m/s}^2\\)',
      'A constant positive non-zero value',
      'Variable depending on mass of train'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Acceleration is defined as the rate of change of velocity: \\(a = \\frac{v - u}{t}\\).\n\n**Step 2: Analysis**: In uniform velocity, the magnitude and direction of velocity do not change with time, so \\(v = u\\). Thus, \\(v - u = 0\\), and \\(a = \\frac{0}{t} = 0\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: Uniform motion along a straight line always has zero acceleration. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Acceleration is defined as the rate of change of velocity: \\(a = \\frac{v - u}{t}\\).\n\n**Step 2: Analysis**: In uniform velocity, the magnitude and direction of velocity do not change with time, so \\(v = u\\). Thus, \\(v - u = 0\\), and \\(a = \\frac{0}{t} = 0\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: Uniform motion along a straight line always has zero acceleration. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'Which of the following is an example of uniform motion in daily life?',
    options: [
      'The hands of a mechanical clock sweeping around the dial',
      'A car navigating a busy market street',
      'A freely falling apple from a tree',
      'A sprinter launching off the starting blocks'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Uniform motion occurs when equal displacements or angles are traversed in equal intervals of time.\n\n**Step 2: Comparison**: The hands of a clock sweep through exact fixed angles in exact time intervals (e.g. minute hand moves 360 degrees in 60 minutes). A car in traffic, a falling apple (accelerating due to gravity), and a sprinter are all non-uniform motions.\n\n**Step 3: Conclusion**: The sweeping of clock hands is uniform motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Uniform motion occurs when equal displacements or angles are traversed in equal intervals of time.\n\n**Step 2: Comparison**: The hands of a clock sweep through exact fixed angles in exact time intervals (e.g. minute hand moves 360 degrees in 60 minutes). A car in traffic, a falling apple (accelerating due to gravity), and a sprinter are all non-uniform motions.\n\n**Step 3: Conclusion**: The sweeping of clock hands is uniform motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'What shape does the distance-time graph take for a body executing uniform motion along a straight line?',
    options: [
      'A straight line inclined at an angle to the time axis',
      'A parabola curving upwards',
      'A horizontal line parallel to the distance axis',
      'A zig-zag irregular curve'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: In uniform motion, distance is directly proportional to time (\\(s = v t\\)).\n\n**Step 2: Graphical Property**: A linear equation \\(y = mx\\) plots as a straight line passing through origin (or having constant slope \\(m = v\\)).\n\n**Step 3: Conclusion**: The graph is a straight line inclined to the time axis. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: In uniform motion, distance is directly proportional to time (\\(s = v t\\)).\n\n**Step 2: Graphical Property**: A linear equation \\(y = mx\\) plots as a straight line passing through origin (or having constant slope \\(m = v\\)).\n\n**Step 3: Conclusion**: The graph is a straight line inclined to the time axis. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'What shape does the distance-time graph take for a body executing non-uniform motion?',
    options: [
      'A curved line whose slope changes at different points',
      'A perfectly straight line inclined at 45 degrees',
      'A horizontal line with slope zero',
      'A vertical line parallel to the distance axis'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: In non-uniform motion, speed changes with time, meaning the rate of change of distance (slope \\(\\frac{ds}{dt}\\)) is not constant.\n\n**Step 2: Graphical Property**: A variable slope produces a curved line (such as a parabola for constant acceleration).\n\n**Step 3: Conclusion**: A curved line represents non-uniform motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: In non-uniform motion, speed changes with time, meaning the rate of change of distance (slope \\(\\frac{ds}{dt}\\)) is not constant.\n\n**Step 2: Graphical Property**: A variable slope produces a curved line (such as a parabola for constant acceleration).\n\n**Step 3: Conclusion**: A curved line represents non-uniform motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'A stone is dropped from the terrace of a tall building. As it falls freely under gravity, is its motion uniform or non-uniform, and why?',
    options: [
      'Non-uniform, because its velocity increases by \\(9.8\\text{ m/s}\\) every second due to gravitational acceleration',
      'Uniform, because gravitational acceleration \\(g = 9.8\\text{ m/s}^2\\) is constant',
      'Uniform, because it travels along a straight vertical path',
      'Non-uniform, because its mass decreases as it falls'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Uniform motion requires constant velocity (equal distances in equal times).\n\n**Step 2: Analysis**: Free fall has a constant acceleration \\(g = 9.8\\text{ m/s}^2\\). Constant acceleration means velocity changes constantly (0 m/s, 9.8 m/s, 19.6 m/s, 29.4 m/s...). The distance covered in each second increases (4.9 m, 14.7 m, 24.5 m...).\n\n**Step 3: Conclusion**: The motion covers unequal distances in equal times, so it is non-uniform motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Uniform motion requires constant velocity (equal distances in equal times).\n\n**Step 2: Analysis**: Free fall has a constant acceleration \\(g = 9.8\\text{ m/s}^2\\). Constant acceleration means velocity changes constantly (0 m/s, 9.8 m/s, 19.6 m/s, 29.4 m/s...). The distance covered in each second increases (4.9 m, 14.7 m, 24.5 m...).\n\n**Step 3: Conclusion**: The motion covers unequal distances in equal times, so it is non-uniform motion. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'An object travels along a straight line. During the first \\(2\\text{ s}\\) it covers \\(20\\text{ m}\\), in the next \\(2\\text{ s}\\) it covers \\(20\\text{ m}\\), and in the following \\(2\\text{ s}\\) it covers \\(20\\text{ m}\\). What is its instantaneous speed at \\(t = 5\\text{ s}\\)?',
    options: [
      '\\(10\\text{ m/s}\\)',
      '\\(20\\text{ m/s}\\)',
      '\\(5\\text{ m/s}\\)',
      '\\(0\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Since the object covers equal distances of \\(20\\text{ m}\\) in every equal interval of \\(2\\text{ s}\\), the motion is uniform.\n\n**Step 2: Calculation**: In uniform motion, instantaneous speed equals average speed at all times: \\(v = \\frac{20\\text{ m}}{2\\text{ s}} = 10\\text{ m/s}\\).\n\n**Step 3: Conclusion**: At \\(t = 5\\text{ s}\\), the speed is \\(10\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Since the object covers equal distances of \\(20\\text{ m}\\) in every equal interval of \\(2\\text{ s}\\), the motion is uniform.\n\n**Step 2: Calculation**: In uniform motion, instantaneous speed equals average speed at all times: \\(v = \\frac{20\\text{ m}}{2\\text{ s}} = 10\\text{ m/s}\\).\n\n**Step 3: Conclusion**: At \\(t = 5\\text{ s}\\), the speed is \\(10\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'A car is moving with a constant speed of \\(60\\text{ km/h}\\) around a circular roundabout. Is its velocity uniform or non-uniform?',
    options: [
      'Non-uniform, because its direction of motion is continuously changing',
      'Uniform, because its speed remains constant at \\(60\\text{ km/h}\\)',
      'Uniform, because circular motion is always uniform',
      'Non-uniform, because circular radius keeps shrinking'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Velocity is a vector requiring both constant speed AND constant direction to be considered uniform.\n\n**Step 2: Analysis**: In circular motion, the direction of motion at any instant is along the tangent to the circle, which changes continuously from moment to moment.\n\n**Step 3: Conclusion**: Because the direction changes continuously, the velocity is non-uniform, even though the speed is constant. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Velocity is a vector requiring both constant speed AND constant direction to be considered uniform.\n\n**Step 2: Analysis**: In circular motion, the direction of motion at any instant is along the tangent to the circle, which changes continuously from moment to moment.\n\n**Step 3: Conclusion**: Because the direction changes continuously, the velocity is non-uniform, even though the speed is constant. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'Which of the following conditions is NECESSARY and SUFFICIENT for a motion to be classified as uniform rectilinear motion?',
    options: [
      'Both the speed and the direction of motion remain completely constant with time',
      'Only the speed remains constant, while direction can vary',
      'The body moves in a straight line with constant non-zero acceleration',
      'The body completes one full cycle in fixed periodic time'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Rectilinear means along a straight line (constant direction). Uniform means constant speed (zero acceleration).\n\n**Step 2: Condition**: Both magnitude of velocity (speed) and direction must remain unchanging.\n\n**Step 3: Conclusion**: Constant speed and constant direction define uniform rectilinear motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Rectilinear means along a straight line (constant direction). Uniform means constant speed (zero acceleration).\n\n**Step 2: Condition**: Both magnitude of velocity (speed) and direction must remain unchanging.\n\n**Step 3: Conclusion**: Constant speed and constant direction define uniform rectilinear motion. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'Consider the following data for an object moving along a straight line:\nAt \\(t = 0\\text{ s}, s = 0\\text{ m}\\);\nAt \\(t = 1\\text{ s}, s = 3\\text{ m}\\);\nAt \\(t = 2\\text{ s}, s = 12\\text{ m}\\);\nAt \\(t = 3\\text{ s}, s = 27\\text{ m}\\).\nWhat type of motion is this?',
    options: [
      'Non-uniform motion where distance is proportional to \\(t^2\\) (constant acceleration)',
      'Uniform rectilinear motion with speed \\(3\\text{ m/s}\\)',
      'Motion with constant negative deceleration',
      'Stationary body'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Check distance intervals: In 1st sec, \\(\\Delta s = 3 - 0 = 3\\text{ m}\\). In 2nd sec, \\(\\Delta s = 12 - 3 = 9\\text{ m}\\). In 3rd sec, \\(\\Delta s = 27 - 12 = 15\\text{ m}\\).\n\n**Step 2: Analysis**: Since unequal distances are covered in equal time intervals, the motion is non-uniform. Notice \\(s = 3 t^2\\), which corresponds to \\(s = \\frac{1}{2} a t^2\\) with \\(a = 6\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: This is non-uniform motion with constant acceleration. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Check distance intervals: In 1st sec, \\(\\Delta s = 3 - 0 = 3\\text{ m}\\). In 2nd sec, \\(\\Delta s = 12 - 3 = 9\\text{ m}\\). In 3rd sec, \\(\\Delta s = 27 - 12 = 15\\text{ m}\\).\n\n**Step 2: Analysis**: Since unequal distances are covered in equal time intervals, the motion is non-uniform. Notice \\(s = 3 t^2\\), which corresponds to \\(s = \\frac{1}{2} a t^2\\) with \\(a = 6\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: This is non-uniform motion with constant acceleration. Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'A person walks \\(2\\text{ km}\\) in the first hour, \\(2\\text{ km}\\) in the second hour, and \\(2\\text{ km}\\) in the third hour in a fixed direction towards North. What is the person\'s velocity?',
    options: [
      '\\(2\\text{ km/h}\\) due North (uniform)',
      '\\(6\\text{ km/h}\\) due North',
      '\\(0.67\\text{ km/h}\\) due North',
      'Variable velocity'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Uniform velocity requires covering equal displacements in equal time intervals in a fixed direction.\n\n**Step 2: Calculation**: \\(v = \\frac{2\\text{ km}}{1\\text{ h}} = 2\\text{ km/h}\\) towards North.\n\n**Step 3: Conclusion**: The velocity is uniform at \\(2\\text{ km/h}\\) due North. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Uniform velocity requires covering equal displacements in equal time intervals in a fixed direction.\n\n**Step 2: Calculation**: \\(v = \\frac{2\\text{ km}}{1\\text{ h}} = 2\\text{ km/h}\\) towards North.\n\n**Step 3: Conclusion**: The velocity is uniform at \\(2\\text{ km/h}\\) due North. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'When a body moves with non-uniform motion, which of the following physical quantities must be non-zero?',
    options: [
      'Acceleration',
      'Initial velocity',
      'Frictional force',
      'Displacement'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: By definition, non-uniform motion involves a change in velocity over time (\\(\\Delta v \\neq 0\\)).\n\n**Step 2: Analysis**: Since \\(a = \\frac{\\Delta v}{\\Delta t}\\) and \\(\\Delta v \\neq 0\\), acceleration \\(a\\) must be non-zero.\n\n**Step 3: Conclusion**: Non-uniform motion always implies non-zero acceleration. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: By definition, non-uniform motion involves a change in velocity over time (\\(\\Delta v \\neq 0\\)).\n\n**Step 2: Analysis**: Since \\(a = \\frac{\\Delta v}{\\Delta t}\\) and \\(\\Delta v \\neq 0\\), acceleration \\(a\\) must be non-zero.\n\n**Step 3: Conclusion**: Non-uniform motion always implies non-zero acceleration. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'In which of the following cases is the motion of the body non-uniform?',
    options: [
      'A ball rolling down an inclined plane',
      'A spacecraft cruising through interstellar space with engines off',
      'Light propagating in a vacuum',
      'A conveyor belt moving at constant speed along a straight factory line'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: An object on an inclined plane accelerates due to the component of gravity (\\(g \\sin \\theta\\)), causing its velocity to continuously increase.\n\n**Step 2: Comparison**: A spacecraft with engines off in deep space travels at constant velocity (Newton\'s 1st law). Light in vacuum moves at constant \\(c = 3 \\times 10^8\\text{ m/s}\\). A straight conveyor belt moves at uniform speed.\n\n**Step 3: Conclusion**: The rolling ball undergoes accelerated (non-uniform) motion. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: An object on an inclined plane accelerates due to the component of gravity (\\(g \\sin \\theta\\)), causing its velocity to continuously increase.\n\n**Step 2: Comparison**: A spacecraft with engines off in deep space travels at constant velocity (Newton\'s 1st law). Light in vacuum moves at constant \\(c = 3 \\times 10^8\\text{ m/s}\\). A straight conveyor belt moves at uniform speed.\n\n**Step 3: Conclusion**: The rolling ball undergoes accelerated (non-uniform) motion. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.1.3',
    type: 'OSC',
    text: 'On a velocity-time graph, uniform rectilinear motion is depicted as:',
    options: [
      'A straight line parallel to the time axis',
      'A straight line sloping upwards from the origin',
      'A parabola opening upwards',
      'A line coincident with the distance axis'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: In uniform rectilinear motion, velocity remains constant at all times (\\(v = \\text{constant}\\)).\n\n**Step 2: Graphical Representation**: Plotting \\(v = c\\) against time \\(t\\) yields a horizontal line parallel to the time axis at height \\(c\\).\n\n**Step 3: Conclusion**: The graph is a straight line parallel to the time axis. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: In uniform rectilinear motion, velocity remains constant at all times (\\(v = \\text{constant}\\)).\n\n**Step 2: Graphical Representation**: Plotting \\(v = c\\) against time \\(t\\) yields a horizontal line parallel to the time axis at height \\(c\\).\n\n**Step 3: Conclusion**: The graph is a straight line parallel to the time axis. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // --- Subtopic 1.2.2 (16 Questions: SI unit m/s² and acceleration calculations) ---
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'What is the SI unit of acceleration, and how is it derived from fundamental units?',
    options: [
      '\\(\\text{m/s}^2\\), derived as rate of change of velocity \\(\\frac{\\text{m/s}}{\\text{s}}\\)',
      '\\(\\text{m/s}\\), derived as distance divided by time',
      '\\(\\text{km/h}^2\\), derived from kilometer per hour squared',
      '\\(\\text{m}^2/\\text{s}\\), derived from area divided by time'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Acceleration is the rate of change of velocity: \\(a = \\frac{\\Delta v}{\\Delta t}\\).\n\n**Step 2: Unit Derivation**: Unit of velocity is \\(\\text{m/s}\\) and unit of time is \\(\\text{s}\\). Therefore, \\(\\text{Unit of } a = \\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2 = \\text{m}\\cdot\\text{s}^{-2}\\).\n\n**Step 3: Conclusion**: The SI unit of acceleration is \\(\\text{m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Acceleration is the rate of change of velocity: \\(a = \\frac{\\Delta v}{\\Delta t}\\).\n\n**Step 2: Unit Derivation**: Unit of velocity is \\(\\text{m/s}\\) and unit of time is \\(\\text{s}\\). Therefore, \\(\\text{Unit of } a = \\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2 = \\text{m}\\cdot\\text{s}^{-2}\\).\n\n**Step 3: Conclusion**: The SI unit of acceleration is \\(\\text{m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'What is the CGS unit of acceleration, and what is its relationship to the SI unit \\(\\text{m/s}^2\\)?',
    options: [
      '\\(\\text{cm/s}^2\\), where \\(1\\text{ m/s}^2 = 100\\text{ cm/s}^2\\)',
      '\\(\\text{cm/s}\\), where \\(1\\text{ m/s}^2 = 10\\text{ cm/s}\\)',
      '\\(\\text{mm/s}^2\\), where \\(1\\text{ m/s}^2 = 1000\\text{ mm/s}^2\\)',
      '\\(\\text{dyne}\\), where \\(1\\text{ m/s}^2 = 10^5\\text{ dyne}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: In the CGS system, length is in centimeters (\\(\\text{cm}\\)) and time is in seconds (\\(\\text{s}\\)).\n\n**Step 2: Unit Relation**: CGS unit of acceleration is \\(\\text{cm/s}^2\\). Since \\(1\\text{ m} = 100\\text{ cm}\\), \\(1\\text{ m/s}^2 = 100\\text{ cm/s}^2\\).\n\n**Step 3: Conclusion**: The CGS unit is \\(\\text{cm/s}^2\\) and equals \\(100\\text{ cm/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: In the CGS system, length is in centimeters (\\(\\text{cm}\\)) and time is in seconds (\\(\\text{s}\\)).\n\n**Step 2: Unit Relation**: CGS unit of acceleration is \\(\\text{cm/s}^2\\). Since \\(1\\text{ m} = 100\\text{ cm}\\), \\(1\\text{ m/s}^2 = 100\\text{ cm/s}^2\\).\n\n**Step 3: Conclusion**: The CGS unit is \\(\\text{cm/s}^2\\) and equals \\(100\\text{ cm/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A car accelerates uniformly from rest to \\(72\\text{ km/h}\\) in \\(10\\text{ s}\\). What is its acceleration in \\(\\text{m/s}^2\\)?',
    options: [
      '\\(2\\text{ m/s}^2\\)',
      '\\(7.2\\text{ m/s}^2\\)',
      '\\(20\\text{ m/s}^2\\)',
      '\\(0.2\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(a = \\frac{v - u}{t}\\). Convert velocity to \\(\\text{m/s}\\).\n\n**Step 2: Calculation**: \\(u = 0\\text{ m/s}\\). \\(v = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\). \\(t = 10\\text{ s}\\). \\(a = \\frac{20 - 0}{10} = 2\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(2\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(a = \\frac{v - u}{t}\\). Convert velocity to \\(\\text{m/s}\\).\n\n**Step 2: Calculation**: \\(u = 0\\text{ m/s}\\). \\(v = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\). \\(t = 10\\text{ s}\\). \\(a = \\frac{20 - 0}{10} = 2\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(2\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A scooter travelling at \\(15\\text{ m/s}\\) slows down to \\(5\\text{ m/s}\\) in \\(5\\text{ s}\\) upon applying brakes. What is its acceleration?',
    options: [
      '\\(-2\\text{ m/s}^2\\) (retardation of \\(2\\text{ m/s}^2\\))',
      '\\(+2\\text{ m/s}^2\\)',
      '\\(-10\\text{ m/s}^2\\)',
      '\\(-1\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(a = \\frac{v - u}{t}\\).\n\n**Step 2: Calculation**: \\(u = 15\\text{ m/s}\\), \\(v = 5\\text{ m/s}\\), \\(t = 5\\text{ s}\\). \\(a = \\frac{5 - 15}{5} = \\frac{-10}{5} = -2\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(-2\\text{ m/s}^2\\), which indicates deceleration of \\(2\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(a = \\frac{v - u}{t}\\).\n\n**Step 2: Calculation**: \\(u = 15\\text{ m/s}\\), \\(v = 5\\text{ m/s}\\), \\(t = 5\\text{ s}\\). \\(a = \\frac{5 - 15}{5} = \\frac{-10}{5} = -2\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(-2\\text{ m/s}^2\\), which indicates deceleration of \\(2\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A bullet enters a wooden block with a velocity of \\(100\\text{ m/s}\\) and comes to rest after penetrating \\(0.2\\text{ m}\\). What is the deceleration experienced by the bullet in \\(\\text{m/s}^2\\)?',
    options: [
      '\\(25000\\text{ m/s}^2\\)',
      '\\(50000\\text{ m/s}^2\\)',
      '\\(500\\text{ m/s}^2\\)',
      '\\(10000\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Use 3rd equation of motion: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(u = 100\\text{ m/s}\\), \\(v = 0\\text{ m/s}\\), \\(s = 0.2\\text{ m}\\). \\(0 = 100^2 + 2a(0.2) \\implies 0.4 a = -10000 \\implies a = -25000\\text{ m/s}^2\\). Deceleration is the magnitude: \\(25000\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The deceleration is \\(25000\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Use 3rd equation of motion: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(u = 100\\text{ m/s}\\), \\(v = 0\\text{ m/s}\\), \\(s = 0.2\\text{ m}\\). \\(0 = 100^2 + 2a(0.2) \\implies 0.4 a = -10000 \\implies a = -25000\\text{ m/s}^2\\). Deceleration is the magnitude: \\(25000\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The deceleration is \\(25000\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'If the velocity of an object increases by \\(5\\text{ m/s}\\) every second, what is its acceleration?',
    options: [
      '\\(5\\text{ m/s}^2\\)',
      '\\(10\\text{ m/s}^2\\)',
      '\\(2.5\\text{ m/s}^2\\)',
      '\\(0\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Acceleration is the change in velocity per unit time: \\(a = \\frac{\\Delta v}{\\Delta t}\\).\n\n**Step 2: Calculation**: \\(\\Delta v = 5\\text{ m/s}\\) and \\(\\Delta t = 1\\text{ s}\\). \\(a = \\frac{5}{1} = 5\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(5\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Acceleration is the change in velocity per unit time: \\(a = \\frac{\\Delta v}{\\Delta t}\\).\n\n**Step 2: Calculation**: \\(\\Delta v = 5\\text{ m/s}\\) and \\(\\Delta t = 1\\text{ s}\\). \\(a = \\frac{5}{1} = 5\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(5\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A racing car has a uniform acceleration of \\(4\\text{ m/s}^2\\). What distance will it cover in \\(10\\text{ s}\\) after starting from rest?',
    options: [
      '\\(200\\text{ m}\\)',
      '\\(400\\text{ m}\\)',
      '\\(40\\text{ m}\\)',
      '\\(100\\text{ m}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(s = ut + \\frac{1}{2}at^2\\).\n\n**Step 2: Calculation**: \\(u = 0\\), \\(a = 4\\text{ m/s}^2\\), \\(t = 10\\text{ s}\\). \\(s = 0 + \\frac{1}{2} \\times 4 \\times 10^2 = 2 \\times 100 = 200\\text{ m}\\).\n\n**Step 3: Conclusion**: The distance covered is \\(200\\text{ m}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(s = ut + \\frac{1}{2}at^2\\).\n\n**Step 2: Calculation**: \\(u = 0\\), \\(a = 4\\text{ m/s}^2\\), \\(t = 10\\text{ s}\\). \\(s = 0 + \\frac{1}{2} \\times 4 \\times 10^2 = 2 \\times 100 = 200\\text{ m}\\).\n\n**Step 3: Conclusion**: The distance covered is \\(200\\text{ m}\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'Which of the following is equivalent to \\(1\\text{ m/s}^2\\) expressed in \\(\\text{km/h}^2\\)?',
    options: [
      '\\(12960\\text{ km/h}^2\\)',
      '\\(3600\\text{ km/h}^2\\)',
      '\\(129.6\\text{ km/h}^2\\)',
      '\\(72\\text{ km/h}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Convert meters to kilometers (\\(1\\text{ m} = 10^{-3}\\text{ km}\\)) and seconds to hours (\\(1\\text{ s} = \\frac{1}{3600}\\text{ h}\\)).\n\n**Step 2: Calculation**: \\(1\\text{ m/s}^2 = \\frac{10^{-3}\\text{ km}}{(1/3600\\text{ h})^2} = 10^{-3} \\times (3600)^2 = 10^{-3} \\times 12960000 = 12960\\text{ km/h}^2\\).\n\n**Step 3: Conclusion**: \\(1\\text{ m/s}^2 = 12960\\text{ km/h}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Convert meters to kilometers (\\(1\\text{ m} = 10^{-3}\\text{ km}\\)) and seconds to hours (\\(1\\text{ s} = \\frac{1}{3600}\\text{ h}\\)).\n\n**Step 2: Calculation**: \\(1\\text{ m/s}^2 = \\frac{10^{-3}\\text{ km}}{(1/3600\\text{ h})^2} = 10^{-3} \\times (3600)^2 = 10^{-3} \\times 12960000 = 12960\\text{ km/h}^2\\).\n\n**Step 3: Conclusion**: \\(1\\text{ m/s}^2 = 12960\\text{ km/h}^2\\). Hence, Option A is correct.',
    difficulty: 'hard',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A plane starting from rest accelerates along a runway at \\(3\\text{ m/s}^2\\) and takes off after \\(30\\text{ s}\\). What is its takeoff speed?',
    options: [
      '\\(90\\text{ m/s}\\)',
      '\\(45\\text{ m/s}\\)',
      '\\(10\\text{ m/s}\\)',
      '\\(270\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 0\\), \\(a = 3\\text{ m/s}^2\\), \\(t = 30\\text{ s}\\). \\(v = 0 + 3 \\times 30 = 90\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The takeoff speed is \\(90\\text{ m/s}\\) (which is \\(324\\text{ km/h}\\)). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 0\\), \\(a = 3\\text{ m/s}^2\\), \\(t = 30\\text{ s}\\). \\(v = 0 + 3 \\times 30 = 90\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The takeoff speed is \\(90\\text{ m/s}\\) (which is \\(324\\text{ km/h}\\)). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'When an object travels with negative acceleration (deceleration), what happens to its velocity?',
    options: [
      'The magnitude of its velocity decreases with time',
      'The magnitude of its velocity increases with time',
      'Its velocity becomes constant',
      'Its velocity immediately drops to zero'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Negative acceleration acts in the direction opposite to the direction of motion.\n\n**Step 2: Analysis**: Opposing the velocity vector causes the magnitude of velocity (speed) to decrease over time.\n\n**Step 3: Conclusion**: Deceleration decreases the velocity. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Negative acceleration acts in the direction opposite to the direction of motion.\n\n**Step 2: Analysis**: Opposing the velocity vector causes the magnitude of velocity (speed) to decrease over time.\n\n**Step 3: Conclusion**: Deceleration decreases the velocity. Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A car travelling at \\(20\\text{ m/s}\\) accelerates at a constant rate of \\(1.5\\text{ m/s}^2\\) for \\(8\\text{ s}\\). What is its final velocity?',
    options: [
      '\\(32\\text{ m/s}\\)',
      '\\(12\\text{ m/s}\\)',
      '\\(24\\text{ m/s}\\)',
      '\\(40\\text{ m/s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 20\\text{ m/s}\\), \\(a = 1.5\\text{ m/s}^2\\), \\(t = 8\\text{ s}\\). \\(v = 20 + (1.5 \\times 8) = 20 + 12 = 32\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The final velocity is \\(32\\text{ m/s}\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 20\\text{ m/s}\\), \\(a = 1.5\\text{ m/s}^2\\), \\(t = 8\\text{ s}\\). \\(v = 20 + (1.5 \\times 8) = 20 + 12 = 32\\text{ m/s}\\).\n\n**Step 3: Conclusion**: The final velocity is \\(32\\text{ m/s}\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'An emergency brake on a train moving at \\(36\\text{ km/h}\\) produces a uniform retardation of \\(0.5\\text{ m/s}^2\\). How long will it take for the train to stop?',
    options: [
      '\\(20\\text{ s}\\)',
      '\\(72\\text{ s}\\)',
      '\\(10\\text{ s}\\)',
      '\\(18\\text{ s}\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 36 \\times \\frac{5}{18} = 10\\text{ m/s}\\). \\(v = 0\\text{ m/s}\\). Retardation means \\(a = -0.5\\text{ m/s}^2\\). \\(0 = 10 - 0.5 t \\implies 0.5 t = 10 \\implies t = \\frac{10}{0.5} = 20\\text{ s}\\).\n\n**Step 3: Conclusion**: The train takes \\(20\\text{ s}\\) to come to a stop. Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(v = u + at\\).\n\n**Step 2: Calculation**: \\(u = 36 \\times \\frac{5}{18} = 10\\text{ m/s}\\). \\(v = 0\\text{ m/s}\\). Retardation means \\(a = -0.5\\text{ m/s}^2\\). \\(0 = 10 - 0.5 t \\implies 0.5 t = 10 \\implies t = \\frac{10}{0.5} = 20\\text{ s}\\).\n\n**Step 3: Conclusion**: The train takes \\(20\\text{ s}\\) to come to a stop. Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'Can a body have zero velocity and non-zero acceleration simultaneously?',
    options: [
      'Yes, at the highest point of a vertically projected body (where \\(v = 0\\) and \\(a = -g\\))',
      'No, because acceleration is velocity divided by time, so if \\(v = 0\\), \\(a\\) must be \\(0\\)',
      'No, because acceleration requires motion',
      'Yes, but only in outer space where gravity is zero'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Acceleration is the rate of *change* of velocity, not velocity divided by time.\n\n**Step 2: Physical Example**: When a ball is thrown vertically upwards, it momentarily comes to rest at the peak (\\(v = 0\\)), but Earth\'s gravity still exerts a downward force on it, causing an acceleration \\(g = 9.8\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: At the highest point, velocity is zero while acceleration is \\(-9.8\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Acceleration is the rate of *change* of velocity, not velocity divided by time.\n\n**Step 2: Physical Example**: When a ball is thrown vertically upwards, it momentarily comes to rest at the peak (\\(v = 0\\)), but Earth\'s gravity still exerts a downward force on it, causing an acceleration \\(g = 9.8\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: At the highest point, velocity is zero while acceleration is \\(-9.8\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'analyze'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A particle moves along a straight line such that its velocity changes from \\(12\\text{ m/s}\\) to \\(32\\text{ m/s}\\) while covering a distance of \\(88\\text{ m}\\). What is its uniform acceleration?',
    options: [
      '\\(5\\text{ m/s}^2\\)',
      '\\(2.5\\text{ m/s}^2\\)',
      '\\(10\\text{ m/s}^2\\)',
      '\\(4\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(32^2 = 12^2 + 2a(88) \\implies 1024 = 144 + 176a \\implies 176a = 880 \\implies a = \\frac{880}{176} = 5\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(5\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(32^2 = 12^2 + 2a(88) \\implies 1024 = 144 + 176a \\implies 176a = 880 \\implies a = \\frac{880}{176} = 5\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The acceleration is \\(5\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'What is the dimensional formula for acceleration in terms of \\([M], [L], [T]\\)?',
    options: [
      '\\([M^0 L^1 T^{-2}]\\)',
      '\\([M^0 L^1 T^{-1}]\\)',
      '\\([M^1 L^1 T^{-2}]\\)',
      '\\([M^0 L^2 T^{-2}]\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: Acceleration \\(a = \\frac{\\text{Velocity}}{\\text{Time}} = \\frac{\\text{Length}/\\text{Time}}{\\text{Time}} = \\frac{\\text{Length}}{\\text{Time}^2}\\).\n\n**Step 2: Dimensions**: Length has dimension \\([L]\\), time has \\([T]\\), and mass is absent \\([M^0]\\). Thus, \\([a] = [M^0 L^1 T^{-2}]\\).\n\n**Step 3: Conclusion**: The dimensional formula is \\([M^0 L^1 T^{-2}]\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: Acceleration \\(a = \\frac{\\text{Velocity}}{\\text{Time}} = \\frac{\\text{Length}/\\text{Time}}{\\text{Time}} = \\frac{\\text{Length}}{\\text{Time}^2}\\).\n\n**Step 2: Dimensions**: Length has dimension \\([L]\\), time has \\([T]\\), and mass is absent \\([M^0]\\). Thus, \\([a] = [M^0 L^1 T^{-2}]\\).\n\n**Step 3: Conclusion**: The dimensional formula is \\([M^0 L^1 T^{-2}]\\). Hence, Option A is correct.',
    difficulty: 'easy',
    bloomLevel: 'remember'
  },
  {
    subtopicNumber: '1.2.2',
    type: 'OSC',
    text: 'A truck travelling at \\(25\\text{ m/s}\\) stops in \\(50\\text{ m}\\) after braking. What is the magnitude of the retarding acceleration?',
    options: [
      '\\(6.25\\text{ m/s}^2\\)',
      '\\(12.5\\text{ m/s}^2\\)',
      '\\(0.5\\text{ m/s}^2\\)',
      '\\(2.5\\text{ m/s}^2\\)'
    ],
    correctAnswer: 'A',
    explanation: '**Step 1: Core Concept**: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(0 = 25^2 + 2a(50) \\implies 100a = -625 \\implies a = -6.25\\text{ m/s}^2\\). Magnitude of retardation is \\(6.25\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The retardation is \\(6.25\\text{ m/s}^2\\). Hence, Option A is correct.',
    solution: '**Step 1: Core Concept**: \\(v^2 = u^2 + 2as\\).\n\n**Step 2: Calculation**: \\(0 = 25^2 + 2a(50) \\implies 100a = -625 \\implies a = -6.25\\text{ m/s}^2\\). Magnitude of retardation is \\(6.25\\text{ m/s}^2\\).\n\n**Step 3: Conclusion**: The retardation is \\(6.25\\text{ m/s}^2\\). Hence, Option A is correct.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  }
];

module.exports = { part1Questions };
