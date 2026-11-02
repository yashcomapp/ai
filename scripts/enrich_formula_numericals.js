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

// Authentic Balbharti numerical questions data
const NUMERICAL_QUESTIONS = [
  // ==========================================
  // MH-9-SCIT-4: Measurement of Matter
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-4-4.1',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'In an experiment, 6 g of carbon reacts completely with 16 g of oxygen to form carbon dioxide. What is the mass in grams of carbon dioxide produced according to the Law of Conservation of Mass?',
    correctAnswer: '22',
    solution: 'Given: Mass of carbon = 6 g, Mass of oxygen = 16 g. According to the Law of Conservation of Mass: Total mass of reactants = Total mass of products. Mass of CO2 = 6 g + 16 g = 22 g.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.1',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'According to the Law of Constant Proportions, hydrogen and oxygen always combine in the ratio 1:8 by mass to form water. How many grams of water will be formed when 3 g of hydrogen reacts completely with excess oxygen?',
    correctAnswer: '27',
    solution: 'Given: Mass of hydrogen = 3 g. Hydrogen to oxygen mass ratio is 1:8. Therefore, mass of oxygen required = 3 * 8 = 24 g. Mass of water formed = Mass of hydrogen + Mass of oxygen = 3 g + 24 g = 27 g.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the molecular mass of water (H2O) in atomic mass units (u)? (Atomic masses: H = 1 u, O = 16 u)',
    correctAnswer: '18',
    solution: 'Given: Atomic mass of H = 1 u, Atomic mass of O = 16 u. Molecular mass of H2O = (2 * 1) + (1 * 16) = 2 + 16 = 18 u.',
    difficulty: 'easy',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the molecular mass of carbon dioxide (CO2) in unified mass units (u). (Atomic masses: C = 12 u, O = 16 u)',
    correctAnswer: '44',
    solution: 'Given: Atomic mass of C = 12 u, Atomic mass of O = 16 u. Molecular mass of CO2 = (1 * 12) + (2 * 16) = 12 + 32 = 44 u.',
    difficulty: 'easy',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the molecular mass of calcium carbonate (CaCO3) in u. (Atomic masses: Ca = 40 u, C = 12 u, O = 16 u)',
    correctAnswer: '100',
    solution: 'Given: Ca = 40 u, C = 12 u, O = 16 u. Molecular mass of CaCO3 = 40 + 12 + (3 * 16) = 52 + 48 = 100 u.',
    difficulty: 'medium',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles are present in 36 grams of pure water (H2O)? (Molar mass of H2O = 18 g/mol)',
    correctAnswer: '2',
    solution: 'Given: Mass of water (m) = 36 g, Molar mass of water (M) = 18 g/mol. Number of moles (n) = Mass / Molar mass = 36 / 18 = 2 moles.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of carbon dioxide (CO2) are contained in 88 grams of CO2 gas? (Molar mass of CO2 = 44 g/mol)',
    correctAnswer: '2',
    solution: 'Given: Mass of CO2 = 88 g, Molar mass = 44 g/mol. Number of moles n = m / M = 88 / 44 = 2 moles.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the mass in grams of 0.5 moles of calcium carbonate (CaCO3)? (Molar mass of CaCO3 = 100 g/mol)',
    correctAnswer: '50',
    solution: 'Given: Number of moles n = 0.5 mol, Molar mass M = 100 g/mol. Mass m = n * M = 0.5 * 100 = 50 g.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of sodium hydroxide (NaOH) are present in 120 grams of NaOH? (Atomic masses: Na = 23 u, O = 16 u, H = 1 u)',
    correctAnswer: '3',
    solution: 'Molar mass of NaOH = 23 + 16 + 1 = 40 g/mol. Given mass = 120 g. Number of moles = 120 / 40 = 3 moles.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.4',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'The valency of magnesium is 2 and the valency of chloride is 1. How many chloride ions combine with one magnesium ion to form a neutral magnesium chloride molecule (MgCl2)?',
    correctAnswer: '2',
    solution: 'Magnesium has a valency of +2 and chloride has a valency of -1. By cross-multiplication, 1 Mg^(2+) combines with 2 Cl^(-) ions to form neutral MgCl2.',
    difficulty: 'easy',
    bloomLevel: 'understand'
  },

  // ==========================================
  // MH-9-SCIT-11: Reflection of Light
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A light ray strikes a plane mirror such that the angle between the incident ray and the mirror surface is 35 degrees. What is the angle of reflection in degrees?',
    correctAnswer: '55',
    solution: 'The normal is perpendicular (90 degrees) to the mirror. Angle of incidence i = 90 - 35 = 55 degrees. By the First Law of Reflection, angle of reflection r = angle of incidence i = 55 degrees.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are kept perpendicular to each other (angle = 90 degrees). How many images of an object placed between them will be formed? (Formula: n = (360 / theta) - 1)',
    correctAnswer: '3',
    solution: 'Given: theta = 90 degrees. Number of images n = (360 / theta) - 1 = (360 / 90) - 1 = 4 - 1 = 3 images.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are arranged at an angle of 60 degrees to each other. Calculate the number of images formed of a coin placed symmetrically between them.',
    correctAnswer: '5',
    solution: 'Given: theta = 60 degrees. Formula: n = (360 / theta) - 1 = (360 / 60) - 1 = 6 - 1 = 5 images.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are kept at an angle of 120 degrees to each other. What is the total number of images formed of a candle placed between them?',
    correctAnswer: '2',
    solution: 'Given: theta = 120 degrees. Formula: n = (360 / theta) - 1 = (360 / 120) - 1 = 3 - 1 = 2 images.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are inclined at an angle of 45 degrees. How many images of an object will be visible?',
    correctAnswer: '7',
    solution: 'Given: theta = 45 degrees. Formula: n = (360 / 45) - 1 = 8 - 1 = 7 images.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'The radius of curvature of a concave spherical mirror is 36 cm. What is its focal length in cm? (Formula: f = R / 2)',
    correctAnswer: '18',
    solution: 'Given: Radius of curvature R = 36 cm. Focal length f = R / 2 = 36 / 2 = 18 cm.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A convex mirror used in a vehicle has a focal length of 25 cm. What is its radius of curvature in cm?',
    correctAnswer: '50',
    solution: 'Given: Focal length f = 25 cm. Radius of curvature R = 2 * f = 2 * 25 = 50 cm.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.3',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object of height 4 cm is placed in front of a concave mirror. If the magnification produced by the mirror is -2, what is the height of the image in cm? (Magnitude only)',
    correctAnswer: '8',
    solution: 'Given: Object height h1 = 4 cm, Magnification M = -2. Formula: M = h2 / h1. Height of image h2 = M * h1 = -2 * 4 = -8 cm (inverted image of height 8 cm).',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object is placed at a distance of 30 cm in front of a concave mirror of focal length 15 cm. At what distance in cm from the mirror will the real image be formed? (Use mirror formula: 1/f = 1/v + 1/u)',
    correctAnswer: '30',
    solution: 'Given: u = -30 cm, f = -15 cm. 1/v = 1/f - 1/u = 1/(-15) - 1/(-30) = -1/15 + 1/30 = (-2 + 1)/30 = -1/30. Therefore v = -30 cm (at the center of curvature).',
    difficulty: 'hard',
    bloomLevel: 'calculate'
  },

  // ==========================================
  // MH-9-SCIT-12: Study of Sound
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A sound wave has a frequency of 500 Hz and a wavelength of 0.68 m. What is the velocity of the sound wave in m/s? (Formula: v = frequency * wavelength)',
    correctAnswer: '340',
    solution: 'Given: Frequency (nu) = 500 Hz, Wavelength (lambda) = 0.68 m. Velocity v = nu * lambda = 500 * 0.68 = 340 m/s.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A tuning fork vibrates at a frequency of 256 Hz in air. If the speed of sound in air is 332.8 m/s, what is the wavelength of the sound wave in metres?',
    correctAnswer: '1.3',
    solution: 'Given: Frequency = 256 Hz, Velocity = 332.8 m/s. Wavelength lambda = v / nu = 332.8 / 256 = 1.3 m.',
    difficulty: 'medium',
    bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A sound wave with a wavelength of 0.85 m travels at a speed of 340 m/s. What is the frequency of the sound wave in Hertz (Hz)?',
    correctAnswer: '400',
    solution: 'Given: Velocity v = 340 m/s, Wavelength lambda = 0.85 m. Frequency nu = v / lambda = 340 / 0.85 = 400 Hz.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.2',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If the speed of sound in air at 20 degrees C is 344 m/s, how many seconds will a sound pulse take to travel a distance of 1720 metres?',
    correctAnswer: '5',
    solution: 'Given: Distance d = 1720 m, Velocity v = 344 m/s. Time t = d / v = 1720 / 344 = 5 seconds.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A student claps her hands near a tall cliff and hears an echo after 2 seconds. If the speed of sound in air is 340 m/s, what is the distance in metres from the student to the cliff? (Formula: d = (v * t) / 2)',
    correctAnswer: '340',
    solution: 'Given: Time t = 2 s, Speed v = 340 m/s. The sound travels to the cliff and back (total distance = 2d). Distance d = (v * t) / 2 = (340 * 2) / 2 = 340 m.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'To hear a distinct echo, what is the minimum distance in metres from the reflecting surface when the speed of sound in air is 344 m/s and the persistence of hearing is 0.1 s?',
    correctAnswer: '17.2',
    solution: 'Given: v = 344 m/s, t = 0.1 s. Total two-way distance 2d = v * t = 344 * 0.1 = 34.4 m. Minimum distance d = 34.4 / 2 = 17.2 m.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A person stands 510 m away from a high wall and fires a pistol. If the speed of sound is 340 m/s, after how many seconds will the person hear the echo?',
    correctAnswer: '3',
    solution: 'Given: d = 510 m, v = 340 m/s. Total distance traveled by sound = 2 * d = 2 * 510 = 1020 m. Time for echo t = 1020 / 340 = 3 seconds.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A SONAR station on a research ship transmits an ultrasonic wave into seawater and receives the reflected signal after 4 seconds. If the speed of sound in seawater is 1500 m/s, what is the depth of the ocean floor in metres?',
    correctAnswer: '3000',
    solution: 'Given: Time t = 4 s, Speed in seawater v = 1500 m/s. Total round-trip distance 2d = v * t = 1500 * 4 = 6000 m. Depth of ocean bed d = 6000 / 2 = 3000 m.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A ship equipped with SONAR detects a submerged submarine. The ultrasonic pulse returns in 1.6 seconds. If the speed of sound in seawater is 1500 m/s, what is the distance to the submarine in metres?',
    correctAnswer: '1200',
    solution: 'Given: t = 1.6 s, v = 1500 m/s. Distance d = (v * t) / 2 = (1500 * 1.6) / 2 = 2400 / 2 = 1200 m.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },

  // ==========================================
  // MH-9-SCIT-1: Laws of Motion (Enrichment)
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A cyclist completes one round of a circular track of circumference 440 metres in 44 seconds. What is the average speed of the cyclist in m/s?',
    correctAnswer: '10',
    solution: 'Given: Total distance = 440 m, Total time = 44 s. Average speed = Total distance / Total time = 440 / 44 = 10 m/s.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.1',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A car travels a distance of 180 km in 3 hours at uniform speed. What is its speed in m/s? (Note: 1 km/h = 5/18 m/s)',
    correctAnswer: '16.67',
    solution: 'Given: Distance = 180 km, Time = 3 h. Speed in km/h = 180 / 3 = 60 km/h. Speed in m/s = 60 * (5/18) = 300 / 18 = 16.67 m/s.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.4',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A bus starting from rest moves with a uniform acceleration of 0.5 m/s^2 for 20 seconds. What is its final speed in m/s? (Formula: v = u + at)',
    correctAnswer: '10',
    solution: 'Given: Initial velocity u = 0, Acceleration a = 0.5 m/s^2, Time t = 20 s. Final velocity v = u + a * t = 0 + (0.5 * 20) = 10 m/s.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.4',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A train moving at 20 m/s applies brakes and comes to a stop with a uniform retardation of 2 m/s^2. What distance in metres does the train travel before coming to rest? (Formula: v^2 = u^2 + 2as)',
    correctAnswer: '100',
    solution: 'Given: u = 20 m/s, v = 0 m/s, a = -2 m/s^2. Using v^2 = u^2 + 2as: 0 = (20)^2 + 2 * (-2) * s => 0 = 400 - 4s => 4s = 400 => s = 100 m.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.6',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A constant force of 25 Newtons acts on an object of mass 5 kg. What acceleration in m/s^2 is produced in the object? (Formula: F = m * a)',
    correctAnswer: '5',
    solution: 'Given: Force F = 25 N, Mass m = 5 kg. Acceleration a = F / m = 25 / 5 = 5 m/s^2.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-1-1.6',
    chapterName: 'Laws of Motion',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A ball of mass 0.2 kg is thrown with a velocity of 30 m/s. What is its momentum in kg m/s? (Formula: p = m * v)',
    correctAnswer: '6',
    solution: 'Given: Mass m = 0.2 kg, Velocity v = 30 m/s. Momentum p = m * v = 0.2 * 30 = 6 kg m/s.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // ==========================================
  // MH-9-SCIT-2: Work and Energy (Enrichment)
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A force of 50 Newtons displaces a box through 6 metres along the direction of the force. What is the work done in Joules? (Formula: W = F * s)',
    correctAnswer: '300',
    solution: 'Given: Force F = 50 N, Displacement s = 6 m. Work done W = F * s = 50 * 6 = 300 Joules.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A porter lifts a luggage of mass 15 kg from the ground and puts it on his head 1.5 m above the ground. Calculate the work done by the porter in Joules. (Take g = 9.8 m/s^2)',
    correctAnswer: '220.5',
    solution: 'Given: Mass m = 15 kg, Height h = 1.5 m, g = 9.8 m/s^2. Work done W = m * g * h = 15 * 9.8 * 1.5 = 220.5 Joules.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.2',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the kinetic energy in Joules of an object of mass 2 kg moving with a uniform velocity of 4 m/s? (Formula: KE = 0.5 * m * v^2)',
    correctAnswer: '16',
    solution: 'Given: Mass m = 2 kg, Velocity v = 4 m/s. Kinetic Energy KE = 0.5 * m * v^2 = 0.5 * 2 * (4)^2 = 1 * 16 = 16 Joules.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric bulb of 100 Watts is used for 10 hours daily. How many units (kilowatt-hours, kWh) of electrical energy does it consume per day? (Formula: Energy in kWh = (Power in W * hours) / 1000)',
    correctAnswer: '1',
    solution: 'Given: Power P = 100 W = 0.1 kW, Time t = 10 h. Energy consumed = Power * time = 0.1 kW * 10 h = 1 kWh (1 unit).',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // ==========================================
  // MH-9-SCIT-3: Current Electricity (Enrichment)
  // ==========================================
  {
    topicCode: 'MH-9-SCIT-3-3.1',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A current of 0.5 Amperes is drawn by a filament of an electric bulb for 10 minutes (600 seconds). What is the total electric charge in Coulombs that flows through the circuit? (Formula: Q = I * t)',
    correctAnswer: '300',
    solution: 'Given: Current I = 0.5 A, Time t = 10 min = 600 s. Charge Q = I * t = 0.5 * 600 = 300 Coulombs.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.2',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric iron connected to a 220 V line draws a current of 4.4 Amperes. What is the resistance of the heating element in Ohms? (Formula: R = V / I)',
    correctAnswer: '50',
    solution: 'Given: Voltage V = 220 V, Current I = 4.4 A. Resistance R = V / I = 220 / 4.4 = 50 Ohms.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.4',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Three resistors of resistances 5 Ohms, 10 Ohms, and 15 Ohms are connected in series. What is the equivalent resistance of the combination in Ohms? (Formula: Rs = R1 + R2 + R3)',
    correctAnswer: '30',
    solution: 'Given: R1 = 5 Ohms, R2 = 10 Ohms, R3 = 15 Ohms in series. Equivalent resistance Rs = 5 + 10 + 15 = 30 Ohms.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.5',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two resistors of resistances 6 Ohms and 3 Ohms are connected in parallel. What is their effective equivalent resistance in Ohms? (Formula: 1/Rp = 1/R1 + 1/R2)',
    correctAnswer: '2',
    solution: 'Given: R1 = 6 Ohms, R2 = 3 Ohms in parallel. 1/Rp = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2. Therefore Rp = 2 Ohms.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },

  // ==========================================
  // MH-8-SCI-3: Force and Pressure (Enrichment)
  // ==========================================
  {
    topicCode: 'MH-8-SCI-3-3.3.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A force of 600 Newtons is applied perpendicularly on a wooden table having a surface area of 3 square metres. What is the pressure exerted on the table in N/m^2 (Pascals)? (Formula: P = F / A)',
    correctAnswer: '200',
    solution: 'Given: Force F = 600 N, Area A = 3 m^2. Pressure P = Force / Area = 600 / 3 = 200 N/m^2 (200 Pa).',
    difficulty: 'easy',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'The tip of a sharp drawing pin has an area of 0.0001 m^2 (10^-4 m^2). When pressed with a force of 10 N, what pressure in Pascals (N/m^2) does it exert on the pinboard?',
    correctAnswer: '100000',
    solution: 'Given: Force F = 10 N, Area A = 0.0001 m^2. Pressure P = F / A = 10 / 0.0001 = 100,000 N/m^2 (10^5 Pa).',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A diver is at a depth of 10 metres under water in a swimming pool. What is the liquid pressure in Pascals exerted by the water at this depth? (Take density of water rho = 1000 kg/m^3 and g = 9.8 m/s^2. Formula: P = h * rho * g)',
    correctAnswer: '98000',
    solution: 'Given: Depth h = 10 m, Density rho = 1000 kg/m^3, g = 9.8 m/s^2. Pressure P = h * rho * g = 10 * 1000 * 9.8 = 98,000 Pa.',
    difficulty: 'medium',
    bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'An iron block has a mass of 780 grams and a volume of 100 cm^3. What is the density of iron in g/cm^3? (Formula: Density = Mass / Volume)',
    correctAnswer: '7.8',
    solution: 'Given: Mass = 780 g, Volume = 100 cm^3. Density = Mass / Volume = 780 / 100 = 7.8 g/cm^3.',
    difficulty: 'easy',
    bloomLevel: 'apply'
  }
];

async function runEnrichment() {
  console.log(`Starting enrichment of ${NUMERICAL_QUESTIONS.length} authentic numerical questions...`);

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

  for (const nq of NUMERICAL_QUESTIONS) {
    const topicSnap = await db.collection('questions')
      .where('topicCode', '==', nq.topicCode)
      .get();
    
    // Find an unused, non-numerical question
    let targetDoc = null;
    for (const doc of topicSnap.docs) {
      const q = doc.data();
      const isUsed = usedQuestionIds.has(doc.id) || usedQuestionIds.has(q.questionCode);
      const isNum = q.type === 'ONE' || q.type === 'SSN' || q.type === 'SLN';
      if (!isUsed && !isNum) {
        // Ensure this targetDoc isn't already claimed in replacementPairs
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
  const snapshotFile = path.join(snapshotDir, `snapshot_${timestamp}_enrich_formula_numericals.json`);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'Replace unused theoretical questions with authentic Balbharti school numericals in formula-heavy science chapters',
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

    // Build canonical question code: topicCode-ONE-seq
    const seqMatch = String(original.questionCode || pair.targetDoc.id).match(/(\d{3,})$/);
    const seq = seqMatch ? seqMatch[1] : '050';
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
      options: [], // Pure numerical objective - no distractor letters
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

  console.log(`Successfully replaced ${replacementPairs.length} unused theoretical questions with authentic school-level numericals!`);
}

runEnrichment().then(() => process.exit(0)).catch(console.error);
