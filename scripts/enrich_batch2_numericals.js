const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync('.env.local', 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      const k = trimmed.slice(0, idx).trim();
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[k] = v;
    }
  }
});

const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
admin.initializeApp({ credential: admin.credential.cert(cred) });
const db = admin.firestore();

// 30 Authentic Balbharti Numerical Questions Batch 2
const NUMERICAL_QUESTIONS_BATCH_2 = [
  // --- MH-9-SCIT-1: Laws of Motion ---
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A car covers the first 60 km of a journey at a uniform speed of 30 km/h and the next 60 km at a uniform speed of 60 km/h. What is the average speed of the car for the entire journey in km/h?',
    correctAnswer: '40',
    solution: 'Given: Distance 1 = 60 km at 30 km/h => Time t1 = 60/30 = 2 hours. Distance 2 = 60 km at 60 km/h => Time t2 = 60/60 = 1 hour. Total distance = 120 km. Total time = 2 + 1 = 3 hours. Average speed = Total distance / Total time = 120 / 3 = 40 km/h.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.2',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A train starting from rest attains a speed of 72 km/h in 100 seconds with uniform acceleration. What is its acceleration in m/s^2? (Note: 72 km/h = 20 m/s)',
    correctAnswer: '0.2',
    solution: 'Given: Initial velocity u = 0, Final velocity v = 72 km/h = 72 * (5/18) = 20 m/s, Time t = 100 s. Acceleration a = (v - u) / t = (20 - 0) / 100 = 0.2 m/s^2.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.4',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object is dropped from a cliff and falls freely under gravity with an acceleration of 9.8 m/s^2. What is its velocity in m/s after 3 seconds? (Formula: v = u + at)',
    correctAnswer: '29.4',
    solution: 'Given: Initial velocity u = 0, Acceleration due to gravity a = 9.8 m/s^2, Time t = 3 s. Final velocity v = u + a * t = 0 + (9.8 * 3) = 29.4 m/s.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.4',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A racing car accelerates from rest at a constant rate of 2 m/s^2 for 5 seconds. How many metres does it travel in this time? (Formula: s = ut + 0.5 * a * t^2)',
    correctAnswer: '25',
    solution: 'Given: u = 0, a = 2 m/s^2, t = 5 s. Distance s = u * t + 0.5 * a * t^2 = 0 + 0.5 * 2 * (5)^2 = 1 * 25 = 25 metres.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.6',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A constant horizontal force of 50 Newtons acts on an object of mass 10 kg for a duration of 4 seconds. What is the total change in momentum of the object in kg m/s? (Formula: Impulse = Force * time)',
    correctAnswer: '200',
    solution: 'Given: Force F = 50 N, Time t = 4 s. By Newton’s Second Law, Change in momentum = Force * time = 50 N * 4 s = 200 kg m/s.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },

  // --- MH-9-SCIT-2: Work and Energy ---
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A student applies a constant force of 12 Newtons to slide a textbook through a distance of 5 metres across a table in the direction of the force. How many Joules of work is done? (Formula: W = F * s)',
    correctAnswer: '60',
    solution: 'Given: Force F = 12 N, Displacement s = 5 m. Work done W = F * s = 12 * 5 = 60 Joules.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.2',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A metal sphere of mass 8 kg has a kinetic energy of 100 Joules. What is the velocity of the sphere in m/s? (Formula: KE = 0.5 * m * v^2)',
    correctAnswer: '5',
    solution: 'Given: Kinetic Energy KE = 100 J, Mass m = 8 kg. KE = 0.5 * m * v^2 => 100 = 0.5 * 8 * v^2 => 100 = 4 * v^2 => v^2 = 25 => v = 5 m/s.',
    difficulty: 'medium',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.3',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A water storage tank containing 500 kg of water is situated on the rooftop of a residential building at a height of 20 metres. What is the gravitational potential energy of the water in Joules? (Take g = 9.8 m/s^2)',
    correctAnswer: '98000',
    solution: 'Given: Mass m = 500 kg, Height h = 20 m, g = 9.8 m/s^2. Potential energy PE = m * g * h = 500 * 9.8 * 20 = 98,000 Joules.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.4',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An apple of mass 1 kg drops freely from a branch 5 metres high. What is its kinetic energy in Joules just before it strikes the ground? (Take g = 9.8 m/s^2. Use Conservation of Energy)',
    correctAnswer: '49',
    solution: 'Given: Mass m = 1 kg, Initial height h = 5 m, g = 9.8 m/s^2. By the Law of Conservation of Energy, final KE at ground level = initial PE = m * g * h = 1 * 9.8 * 5 = 49 Joules.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric heater rated at 1000 Watts (1 kW) is operated for 2 hours daily. How many electrical units (kilowatt-hours, kWh) are consumed over a full month of 30 days?',
    correctAnswer: '60',
    solution: 'Given: Power P = 1000 W = 1 kW. Daily usage = 2 hours. Daily consumption = 1 kW * 2 h = 2 kWh. Monthly consumption for 30 days = 2 kWh/day * 30 days = 60 kWh (60 units).',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // --- MH-9-SCIT-3: Current Electricity ---
  {
    topicCode: 'MH-9-SCIT-3-3.1',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How much work in Joules is done in moving an electric charge of 4 Coulombs between two terminals maintained at a potential difference of 12 Volts? (Formula: W = V * Q)',
    correctAnswer: '48',
    solution: 'Given: Potential difference V = 12 V, Charge Q = 4 C. Work done W = V * Q = 12 * 4 = 48 Joules.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.2',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'When a 12 V storage battery is connected across an electrical component, a small current of 0.0025 Amperes (2.5 mA) is measured. What is the resistance of the component in Ohms? (Formula: R = V / I)',
    correctAnswer: '4800',
    solution: 'Given: Voltage V = 12 V, Current I = 0.0025 A. Resistance R = V / I = 12 / 0.0025 = 4800 Ohms.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.3',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A copper conducting wire of length 2 metres has a resistance of 0.034 Ohms. If its length is increased to 4 metres while keeping the cross-sectional area and material identical, what will be its new resistance in Ohms?',
    correctAnswer: '0.068',
    solution: 'Given: Initial length L1 = 2 m, Resistance R1 = 0.034 Ohms. Since resistance is directly proportional to length (R propto L): R2 = R1 * (L2 / L1) = 0.034 * (4 / 2) = 0.034 * 2 = 0.068 Ohms.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.4',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Four resistors of resistances 2 Ohms, 4 Ohms, 6 Ohms, and 8 Ohms are wired in series connection. What is the total combined resistance in Ohms? (Formula: Rs = R1 + R2 + R3 + R4)',
    correctAnswer: '20',
    solution: 'Given: R1 = 2 Ohms, R2 = 4 Ohms, R3 = 6 Ohms, R4 = 8 Ohms connected in series. Total resistance Rs = 2 + 4 + 6 + 8 = 20 Ohms.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.5',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two identical heating coils, each having a resistance of 10 Ohms, are connected in parallel. What is their effective total resistance in Ohms? (Formula: 1/Rp = 1/R1 + 1/R2)',
    correctAnswer: '5',
    solution: 'Given: R1 = 10 Ohms, R2 = 10 Ohms in parallel. 1/Rp = 1/10 + 1/10 = 2/10 = 1/5. Equivalent resistance Rp = 5 Ohms.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // --- MH-9-SCIT-4: Measurement of Matter ---
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the molecular mass of sulfuric acid (H2SO4) in atomic mass units (u)? (Atomic masses: H = 1 u, S = 32 u, O = 16 u)',
    correctAnswer: '98',
    solution: 'Given: H = 1 u, S = 32 u, O = 16 u. Molecular mass of H2SO4 = (2 * 1) + (1 * 32) + (4 * 16) = 2 + 32 + 64 = 98 u.',
    difficulty: 'easy',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the molecular mass of ammonia gas (NH3) in atomic mass units (u). (Atomic masses: N = 14 u, H = 1 u)',
    correctAnswer: '17',
    solution: 'Given: N = 14 u, H = 1 u. Molecular mass of NH3 = (1 * 14) + (3 * 1) = 14 + 3 = 17 u.',
    difficulty: 'easy',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the mass in grams of 0.5 moles of molecular oxygen gas (O2)? (Molar mass of O2 = 32 g/mol)',
    correctAnswer: '16',
    solution: 'Given: Number of moles n = 0.5 mol, Molar mass of O2 = 32 g/mol. Mass m = n * M = 0.5 * 32 = 16 grams.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of sodium chloride (NaCl) are present in 117 grams of pure common salt? (Atomic masses: Na = 23 u, Cl = 35.5 u; Molar mass of NaCl = 58.5 g/mol)',
    correctAnswer: '2',
    solution: 'Given: Mass m = 117 g, Molar mass M = 23 + 35.5 = 58.5 g/mol. Number of moles n = m / M = 117 / 58.5 = 2 moles.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the total mass in grams of 5 moles of pure water (H2O)? (Molar mass of water = 18 g/mol)',
    correctAnswer: '90',
    solution: 'Given: Number of moles n = 5 mol, Molar mass M = 18 g/mol. Mass m = n * M = 5 * 18 = 90 grams.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // --- MH-9-SCIT-11: Reflection of Light ---
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are kept at an angle of 72 degrees to each other. How many images of a small object placed symmetrically between them will be formed? (Formula: n = (360 / theta) - 1)',
    correctAnswer: '4',
    solution: 'Given: theta = 72 degrees. Number of images n = (360 / theta) - 1 = (360 / 72) - 1 = 5 - 1 = 4 images.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object is placed at a perpendicular distance of 25 cm in front of a flat plane mirror. What is the total distance in cm between the object and its reflected image?',
    correctAnswer: '50',
    solution: 'In a plane mirror, the virtual image is formed at an equal distance behind the mirror (image distance = object distance = 25 cm). Total distance between object and image = 25 cm + 25 cm = 50 cm.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A concave spherical mirror has a radius of curvature of 50 cm. What is its focal length in cm? (Formula: f = R / 2)',
    correctAnswer: '25',
    solution: 'Given: Radius of curvature R = 50 cm. Focal length f = R / 2 = 50 / 2 = 25 cm.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.3',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object of height 6 cm placed in front of a concave mirror forms a real inverted image of height 18 cm. What is the linear magnification produced by the mirror? (Magnitude only, Formula: M = h2 / h1)',
    correctAnswer: '3',
    solution: 'Given: Object height h1 = 6 cm, Image height h2 = 18 cm. Magnification M = h2 / h1 = 18 / 6 = 3.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An illuminated object is placed at a distance of 40 cm in front of a concave mirror of focal length 20 cm. At what distance in cm from the mirror will the real inverted image be focused? (Formula: 1/f = 1/v + 1/u)',
    correctAnswer: '40',
    solution: 'Given: u = -40 cm, f = -20 cm (concave mirror). 1/v = 1/f - 1/u = 1/(-20) - 1/(-40) = -1/20 + 1/40 = -1/40. Therefore v = -40 cm. The image is formed at a distance of 40 cm in front of the mirror (at the center of curvature).',
    difficulty: 'medium',
    bloomLevel: 'calculate'
  },

  // --- MH-9-SCIT-12: Study of Sound ---
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A radio broadcast transmitter operates at a frequency of 100 MHz (10^8 Hz). If radio waves travel at the speed of light (3 * 10^8 m/s), what is the wavelength of the waves in metres? (Formula: wavelength = velocity / frequency)',
    correctAnswer: '3',
    solution: 'Given: Velocity v = 3 * 10^8 m/s, Frequency nu = 10^8 Hz. Wavelength lambda = v / nu = (3 * 10^8) / (10^8) = 3 metres.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A student standing 680 metres away from a large vertical cliff shouts into the valley. If the speed of sound in air is 340 m/s, after how many seconds will the student hear the echo? (Formula: t = 2d / v)',
    correctAnswer: '4',
    solution: 'Given: Distance to cliff d = 680 m, Speed of sound v = 340 m/s. Total round-trip distance traveled by sound = 2 * d = 2 * 680 = 1360 m. Time for echo t = 1360 / 340 = 4 seconds.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A clinical ultrasound scanner sends an ultrasonic pulse through soft body tissue at a speed of 1540 m/s. The pulse reflects from an internal organ surface and is detected after 0.0001 seconds (10^-4 s). What is the depth of the organ in centimetres (cm)?',
    correctAnswer: '7.7',
    solution: 'Given: Speed v = 1540 m/s, Round trip time t = 0.0001 s. Total distance = v * t = 1540 * 0.0001 = 0.154 m. Depth d = 0.154 / 2 = 0.077 m = 7.7 cm.',
    difficulty: 'hard',
    bloomLevel: 'calculate'
  },

  // --- MH-8-SCI-3: Force and Pressure ---
  {
    topicCode: 'MH-8-SCI-3-3.3.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A heavy wooden crate weighs 1200 Newtons and rests on a floor covering a contact area of 4 square metres. What is the pressure exerted on the floor in Pascals (N/m^2)? (Formula: P = F / A)',
    correctAnswer: '300',
    solution: 'Given: Force F = 1200 N, Area A = 4 m^2. Pressure P = F / A = 1200 / 4 = 300 N/m^2 (300 Pascals).',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A solid aluminum block has a mass of 540 grams and occupies a volume of 200 cm^3. What is the density of aluminum in g/cm^3? (Formula: Density = Mass / Volume)',
    correctAnswer: '2.7',
    solution: 'Given: Mass = 540 g, Volume = 200 cm^3. Density = Mass / Volume = 540 / 200 = 2.7 g/cm^3.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  }
];

async function runBatch2Enrichment() {
  console.log(`Starting Batch 2 enrichment of ${NUMERICAL_QUESTIONS_BATCH_2.length} authentic numerical questions...`);

  // 1. Gather all used question IDs from exams
  const usedQuestionIds = new Set();
  const examsSnap = await db.collection('exams').select('questionCodes').get();
  examsSnap.forEach(doc => {
    const codes = doc.data().questionCodes || [];
    codes.forEach(c => usedQuestionIds.add(c));
  });

  console.log(`Identified ${usedQuestionIds.size} protected used question identifiers.`);

  // 2. For each new numerical question, find an unused theoretical question in the same topic to replace
  const replacementPairs = [];

  for (const nq of NUMERICAL_QUESTIONS_BATCH_2) {
    const topicSnap = await db.collection('questions')
      .where('topicCode', '==', nq.topicCode)
      .get();
    
    let targetDoc = null;
    for (const doc of topicSnap.docs) {
      const q = doc.data();
      const isUsed = usedQuestionIds.has(doc.id) || usedQuestionIds.has(q.questionCode);
      const isNum = q.type === 'ONE' || q.type === 'SSN' || q.type === 'SLN';
      if (!isUsed && !isNum) {
        if (!replacementPairs.some(p => p.targetDoc.id === doc.id)) {
          targetDoc = doc;
          break;
        }
      }
    }

    if (targetDoc) {
      replacementPairs.push({ targetDoc, newQuestion: nq });
    } else {
      console.warn(`Could not find an unused theoretical question to replace for topic ${nq.topicCode}`);
    }
  }

  console.log(`Found ${replacementPairs.length} eligible target questions to replace with authentic numericals.`);

  // 3. Pre-Mutation Snapshot (Rule 2Q)
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotDir = path.join(process.cwd(), 'backups', 'snapshots');
  if (!fs.existsSync(snapshotDir)) fs.mkdirSync(snapshotDir, { recursive: true });
  const snapshotFile = path.join(snapshotDir, `snapshot_${timestamp}_enrich_batch2_numericals.json`);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'Batch 2: Replace 30 unused theoretical questions with authentic Balbharti school numericals in formula-heavy chapters',
    count: replacementPairs.length,
    documents: replacementPairs.map(p => ({ id: p.targetDoc.id, ...p.targetDoc.data() }))
  };
  fs.writeFileSync(snapshotFile, JSON.stringify(snapshotData, null, 2));
  console.log(`Pre-mutation snapshot saved to: ${snapshotFile}`);

  await db.collection('_systemBackups').doc(`snapshot_${timestamp}`).set({
    timestamp: now.toISOString(),
    reason: snapshotData.reason,
    count: replacementPairs.length,
    file: snapshotFile
  });

  // 4. Execute atomic batch update
  let batch = db.batch();
  let opCount = 0;

  for (const pair of replacementPairs) {
    const original = pair.targetDoc.data();
    const nq = pair.newQuestion;

    const seqMatch = String(original.questionCode || pair.targetDoc.id).match(/(\d{3,})$/);
    const seq = seqMatch ? seqMatch[1] : '055';
    const canonicalQuestionCode = `${nq.topicCode}-ONE-${seq}`;

    const updatedData = {
      ...original,
      type: 'ONE',
      questionType: 'objective',
      questionCode: canonicalQuestionCode,
      text: nq.text,
      correctAnswer: nq.correctAnswer,
      solution: nq.solution,
      explanation: nq.solution,
      difficulty: nq.difficulty,
      bloomLevel: nq.bloomLevel,
      marks: 4,
      options: [],
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    };

    batch.set(pair.targetDoc.ref, updatedData);
    opCount++;

    if (opCount === 400) {
      await batch.commit();
      batch = db.batch();
      opCount = 0;
    }
  }

  if (opCount > 0) {
    await batch.commit();
  }

  console.log(`Successfully replaced ${replacementPairs.length} unused theoretical questions with authentic Batch 2 school-level numericals!`);
}

runBatch2Enrichment().then(() => process.exit(0)).catch(console.error);
