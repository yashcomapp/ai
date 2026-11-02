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

// 102 Authentic Balbharti Numerical Questions to achieve 25-30+ numericals per chapter
const CHAPTER_NUMERICALS = [
  // =========================================================================
  // 1. MH-9-SCIT-2: Work and Energy (15 questions -> Total = 27)
  // =========================================================================
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A force of 20 N displaces an object through 4 m at an angle of 60 degrees to the direction of force. Calculate the work done in Joules. (Given: cos 60 = 0.5. Formula: W = F * s * cos theta)',
    correctAnswer: '40',
    solution: 'Given: F = 20 N, s = 4 m, theta = 60 degrees, cos 60 = 0.5. Work done W = F * s * cos(60) = 20 * 4 * 0.5 = 40 Joules.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A bullock exerts a force of 140 N while plowing a field. If the field plowed is 15 m long, how much work in Joules is done by the bullock? (Formula: W = F * s)',
    correctAnswer: '2100',
    solution: 'Given: Force F = 140 N, Displacement s = 15 m. Work done W = F * s = 140 * 15 = 2100 Joules.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.1',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A porter lifts a box weighing 200 N vertically through a height of 2 metres. What is the work done against gravity in Joules?',
    correctAnswer: '400',
    solution: 'Given: Weight (Force) F = 200 N, Displacement s = 2 m. Work done W = F * s = 200 * 2 = 400 Joules.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.2',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the kinetic energy in Joules of a cricket ball of mass 0.25 kg bowling with a velocity of 20 m/s. (Formula: KE = 0.5 * m * v^2)',
    correctAnswer: '50',
    solution: 'Given: m = 0.25 kg, v = 20 m/s. KE = 0.5 * 0.25 * (20)^2 = 0.5 * 0.25 * 400 = 50 Joules.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.2',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A body of mass 4 kg has a kinetic energy of 72 Joules. What is the speed of the body in m/s?',
    correctAnswer: '6',
    solution: 'Given: KE = 72 J, m = 4 kg. 72 = 0.5 * 4 * v^2 => 72 = 2 * v^2 => v^2 = 36 => v = 6 m/s.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.2',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If the velocity of an object is doubled, by what factor does its kinetic energy increase? (Compute: ratio KE_new / KE_initial)',
    correctAnswer: '4',
    solution: 'Since KE = 0.5 * m * v^2, KE is proportional to v^2. If v is doubled (2v), (2v)^2 = 4v^2. Kinetic energy increases by a factor of 4.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.3',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Find the gravitational potential energy in Joules of a 5 kg stone raised to a height of 4 metres. (Take g = 9.8 m/s^2. Formula: PE = m * g * h)',
    correctAnswer: '196',
    solution: 'Given: m = 5 kg, h = 4 m, g = 9.8 m/s^2. PE = m * g * h = 5 * 9.8 * 4 = 196 Joules.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.3',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object of mass 10 kg has a potential energy of 490 Joules. At what height in metres above the ground is the object placed? (Take g = 9.8 m/s^2)',
    correctAnswer: '5',
    solution: 'Given: PE = 490 J, m = 10 kg, g = 9.8 m/s^2. h = PE / (m * g) = 490 / (10 * 9.8) = 490 / 98 = 5 metres.',
    difficulty: 'easy', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.3',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A weightlifter raises a barbell of mass 120 kg through a vertical height of 2 m in 3 seconds. What is the potential energy gained by the barbell in Joules? (Take g = 9.8 m/s^2)',
    correctAnswer: '2352',
    solution: 'Given: m = 120 kg, h = 2 m, g = 9.8 m/s^2. PE = m * g * h = 120 * 9.8 * 2 = 2352 Joules.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.4',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A 2 kg metal ball is dropped from a height of 10 m. What is its potential energy in Joules when it has fallen through 4 metres (at height 6 m)? (Take g = 9.8 m/s^2)',
    correctAnswer: '117.6',
    solution: 'Given: m = 2 kg, Remaining height h = 10 - 4 = 6 m, g = 9.8 m/s^2. PE = m * g * h = 2 * 9.8 * 6 = 117.6 Joules.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.4',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A ball of mass 0.5 kg falls from a height of 20 m. Neglecting air friction, what is its kinetic energy in Joules just before it touches the ground? (Take g = 9.8 m/s^2)',
    correctAnswer: '98',
    solution: 'By Conservation of Mechanical Energy: Final KE = Initial PE = m * g * h = 0.5 * 9.8 * 20 = 98 Joules.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric pump lifts 7200 kg of water into an overhead tank 10 m high in 20 minutes (1200 seconds). What is the useful power developed by the pump in Watts? (Take g = 9.8 m/s^2)',
    correctAnswer: '588',
    solution: 'Given: m = 7200 kg, h = 10 m, g = 9.8 m/s^2, t = 1200 s. Work done W = m * g * h = 7200 * 9.8 * 10 = 705,600 J. Power P = W / t = 705600 / 1200 = 588 Watts.',
    difficulty: 'hard', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A 60 Watt light bulb is kept switched on for 5 hours each day. How many kilowatt-hours (kWh) of electrical energy does it consume in 10 days?',
    correctAnswer: '3',
    solution: 'Given: Power P = 60 W = 0.06 kW. Time = 5 hours/day * 10 days = 50 hours. Energy = P * t = 0.06 kW * 50 h = 3 kWh (3 units).',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A machine performs 18,000 Joules of work in 1 minute (60 seconds). What is the power output of the machine in Watts? (Formula: P = W / t)',
    correctAnswer: '300',
    solution: 'Given: Work W = 18000 J, Time t = 60 s. Power P = W / t = 18000 / 60 = 300 Watts.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-2-2.5',
    chapterName: 'Work and Energy',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An air conditioner rated at 2000 W (2 kW) runs for 6 hours daily. If electricity costs 5 Rupees per unit (kWh), what is the daily electricity bill in Rupees?',
    correctAnswer: '60',
    solution: 'Units consumed per day = 2 kW * 6 h = 12 kWh. Daily cost = 12 units * 5 Rs/unit = 60 Rupees.',
    difficulty: 'medium', bloomLevel: 'apply'
  },

  // =========================================================================
  // 2. MH-9-SCIT-3: Current Electricity (15 questions -> Total = 29)
  // =========================================================================
  {
    topicCode: 'MH-9-SCIT-3-3.1',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If a charge of 360 Coulombs flows through a conductor in 2 minutes (120 seconds), what is the electric current in Amperes? (Formula: I = Q / t)',
    correctAnswer: '3',
    solution: 'Given: Q = 360 C, t = 120 s. Current I = Q / t = 360 / 120 = 3 Amperes.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.1',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How much charge in Coulombs passes through a wire carrying a current of 1.5 Amperes in 40 seconds? (Formula: Q = I * t)',
    correctAnswer: '60',
    solution: 'Given: I = 1.5 A, t = 40 s. Charge Q = I * t = 1.5 * 40 = 60 Coulombs.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.1',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What potential difference in Volts is required to pass a charge of 5 Coulombs doing 100 Joules of work? (Formula: V = W / Q)',
    correctAnswer: '20',
    solution: 'Given: Work W = 100 J, Charge Q = 5 C. Potential difference V = W / Q = 100 / 5 = 20 Volts.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.2',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric heater draws 5 Amperes from a 230 V power supply. Calculate the resistance of the heater element in Ohms. (Formula: R = V / I)',
    correctAnswer: '46',
    solution: 'Given: V = 230 V, I = 5 A. Resistance R = V / I = 230 / 5 = 46 Ohms.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.2',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A light bulb filament has a resistance of 1200 Ohms. How much current in Amperes will flow through it when connected to a 240 V line? (Formula: I = V / R)',
    correctAnswer: '0.2',
    solution: 'Given: V = 240 V, R = 1200 Ohms. Current I = V / R = 240 / 1200 = 0.2 Amperes.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.2',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What potential difference in Volts must be applied across an 8 Ohm resistor to establish a current of 2.5 Amperes? (Formula: V = I * R)',
    correctAnswer: '20',
    solution: 'Given: I = 2.5 A, R = 8 Ohms. Potential difference V = I * R = 2.5 * 8 = 20 Volts.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.3',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A wire of resistance 10 Ohms is stretched so that its length becomes 3 times its original length while volume remains constant. What is the new resistance in Ohms? (Note: R propto L^2 when stretched)',
    correctAnswer: '90',
    solution: 'When stretched to 3 times length (L2 = 3L1), area decreases to A2 = A1/3. New resistance R2 = rho * (3L1) / (A1/3) = 9 * (rho * L1 / A1) = 9 * 10 = 90 Ohms.',
    difficulty: 'hard', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.3',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If a wire of length 1 m and area 10^-6 m^2 has a resistance of 1.7 * 10^-2 Ohms, what is the resistivity of the material in Ohm-metres? (Formula: rho = R * A / L)',
    correctAnswer: '0.000000017',
    solution: 'Given: R = 0.017 Ohm, A = 10^-6 m^2, L = 1 m. Resistivity rho = R * A / L = 0.017 * 10^-6 = 1.7 * 10^-8 Ohm-m.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.4',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two resistors of 15 Ohms and 25 Ohms are connected in series with a 12 V battery. What is the current in Amperes flowing through the circuit?',
    correctAnswer: '0.3',
    solution: 'Equivalent resistance Rs = 15 + 25 = 40 Ohms. Total current I = V / Rs = 12 / 40 = 0.3 Amperes.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.4',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Three identical resistors are connected in series and have an equivalent resistance of 45 Ohms. What is the resistance of each individual resistor in Ohms?',
    correctAnswer: '15',
    solution: 'Given: Rs = 3 * R = 45 Ohms. Resistance of each resistor R = 45 / 3 = 15 Ohms.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.5',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two resistors of 20 Ohms and 30 Ohms are connected in parallel. Calculate their combined resistance in Ohms. (Formula: Rp = (R1 * R2) / (R1 + R2))',
    correctAnswer: '12',
    solution: 'Given: R1 = 20 Ohms, R2 = 30 Ohms. Rp = (20 * 30) / (20 + 30) = 600 / 50 = 12 Ohms.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.5',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Four identical 100 Ohm resistors are connected in parallel. What is their equivalent resistance in Ohms? (Formula: Rp = R / n)',
    correctAnswer: '25',
    solution: 'For n equal resistors in parallel: Rp = R / n = 100 / 4 = 25 Ohms.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.5',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A 6 Ohm resistor and a 12 Ohm resistor are connected in parallel across a 6 V battery. What is the total current in Amperes supplied by the battery?',
    correctAnswer: '1.5',
    solution: 'Equivalent resistance Rp = (6 * 12) / (6 + 12) = 72 / 18 = 4 Ohms. Total current I = V / Rp = 6 / 4 = 1.5 Amperes.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.6',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An electric kettle consumes 2200 Watts when connected to a 220 V line. What should be the minimum rating of the fuse wire in Amperes? (Formula: I = P / V)',
    correctAnswer: '10',
    solution: 'Given: Power P = 2200 W, Voltage V = 220 V. Current I = P / V = 2200 / 220 = 10 Amperes. The fuse rating should be at least 10 A.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-3-3.6',
    chapterName: 'Current Electricity',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'In a household circuit, three 100 W bulbs and one 500 W refrigerator operate simultaneously at 250 V. What is the total current in Amperes drawn from the main supply?',
    correctAnswer: '3.2',
    solution: 'Total Power P = (3 * 100) + 500 = 300 + 500 = 800 W. Voltage V = 250 V. Total Current I = P / V = 800 / 250 = 3.2 Amperes.',
    difficulty: 'medium', bloomLevel: 'apply'
  },

  // =========================================================================
  // 3. MH-9-SCIT-4: Measurement of Matter (18 questions -> Total = 28)
  // =========================================================================
  {
    topicCode: 'MH-9-SCIT-4-4.1',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'When 10 g of calcium carbonate is heated, it decomposes into 5.6 g of calcium oxide and carbon dioxide gas. What is the mass in grams of carbon dioxide gas evolved according to the Law of Conservation of Mass?',
    correctAnswer: '4.4',
    solution: 'Given: Reactant mass (CaCO3) = 10 g. Solid product (CaO) = 5.6 g. Mass of CO2 = 10 g - 5.6 g = 4.4 g.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.1',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'In carbon dioxide (CO2), carbon and oxygen combine in the fixed ratio 3:8 by mass. How many grams of oxygen are required to react completely with 9 grams of carbon?',
    correctAnswer: '24',
    solution: 'Given ratio C:O = 3:8. For 9 g of carbon: Mass of oxygen = 9 * (8 / 3) = 24 grams.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the molecular mass of nitric acid (HNO3) in atomic mass units (u)? (Atomic masses: H = 1 u, N = 14 u, O = 16 u)',
    correctAnswer: '63',
    solution: 'Given: H = 1, N = 14, O = 16. Molecular mass of HNO3 = 1 + 14 + (3 * 16) = 15 + 48 = 63 u.',
    difficulty: 'easy', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the molecular mass of magnesium chloride (MgCl2) in atomic mass units (u). (Atomic masses: Mg = 24 u, Cl = 35.5 u)',
    correctAnswer: '95',
    solution: 'Given: Mg = 24 u, Cl = 35.5 u. Molecular mass of MgCl2 = 24 + (2 * 35.5) = 24 + 71 = 95 u.',
    difficulty: 'easy', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Calculate the molecular mass of aluminum oxide (Al2O3) in atomic mass units (u). (Atomic masses: Al = 27 u, O = 16 u)',
    correctAnswer: '102',
    solution: 'Given: Al = 27 u, O = 16 u. Molecular mass of Al2O3 = (2 * 27) + (3 * 16) = 54 + 48 = 102 u.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.2',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the molecular mass of glucose (C6H12O6) in atomic mass units (u)? (Atomic masses: C = 12 u, H = 1 u, O = 16 u)',
    correctAnswer: '180',
    solution: 'Given: C = 12, H = 1, O = 16. Molecular mass of C6H12O6 = (6 * 12) + (12 * 1) + (6 * 16) = 72 + 12 + 96 = 180 u.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of helium atoms are contained in 52 grams of helium gas? (Atomic mass of He = 4 u)',
    correctAnswer: '13',
    solution: 'Given: Mass m = 52 g, Molar mass M = 4 g/mol. Number of moles n = m / M = 52 / 4 = 13 moles.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the mass in grams of 0.2 moles of sulfuric acid (H2SO4)? (Molar mass of H2SO4 = 98 g/mol)',
    correctAnswer: '19.6',
    solution: 'Given: n = 0.2 mol, M = 98 g/mol. Mass m = n * M = 0.2 * 98 = 19.6 grams.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles are present in 12.8 grams of sulfur dioxide (SO2)? (Molar mass of SO2 = 64 g/mol)',
    correctAnswer: '0.2',
    solution: 'Given: Mass m = 12.8 g, Molar mass M = 64 g/mol. Number of moles n = 12.8 / 64 = 0.2 moles.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of oxygen atoms are present in 1 mole of aluminum oxide (Al2O3)?',
    correctAnswer: '3',
    solution: 'In 1 formula unit of Al2O3, there are 3 oxygen atoms. Therefore, 1 mole of Al2O3 contains 3 moles of oxygen atoms.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the mass in grams of 2.5 moles of sodium hydroxide (NaOH)? (Molar mass of NaOH = 40 g/mol)',
    correctAnswer: '100',
    solution: 'Given: n = 2.5 mol, M = 40 g/mol. Mass m = n * M = 2.5 * 40 = 100 grams.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many moles of hydrogen atoms are contained in 4 moles of methane (CH4)?',
    correctAnswer: '16',
    solution: 'Each molecule of CH4 has 4 hydrogen atoms. In 4 moles of CH4: Moles of H atoms = 4 * 4 = 16 moles.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the percentage of calcium by mass in calcium carbonate (CaCO3)? (Atomic masses: Ca = 40 u, C = 12 u, O = 16 u)',
    correctAnswer: '40',
    solution: 'Molar mass of CaCO3 = 40 + 12 + 48 = 100 g/mol. Mass of Ca = 40 g. Percentage of Ca = (40 / 100) * 100 = 40%.',
    difficulty: 'easy', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.3',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the percentage of oxygen by mass in pure water (H2O)? (Atomic masses: H = 1 u, O = 16 u; Round to 2 decimal places)',
    correctAnswer: '88.89',
    solution: 'Molar mass of H2O = 18 g/mol. Mass of oxygen = 16 g. Mass percentage = (16 / 18) * 100 = 88.89%.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.4',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Aluminum has a valency of 3 and oxygen has a valency of 2. In one neutral molecule of aluminum oxide (Al2O3), what is the total number of constituent atoms?',
    correctAnswer: '5',
    solution: 'In Al2O3, there are 2 aluminum atoms and 3 oxygen atoms. Total number of atoms = 2 + 3 = 5 atoms.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.4',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'The valency of carbon is 4 and that of hydrogen is 1. How many hydrogen atoms combine with one carbon atom to form a stable methane molecule (CH4)?',
    correctAnswer: '4',
    solution: 'By cross-multiplication of valencies: C(4) and H(1) combine to form CH4, requiring 4 hydrogen atoms.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.4',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many total ions (cations + anions) are formed when 1 formula unit of calcium chloride (CaCl2) completely dissociates in water?',
    correctAnswer: '3',
    solution: 'CaCl2 dissociates into 1 Ca^(2+) cation and 2 Cl^(-) anions. Total ions = 1 + 2 = 3 ions.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-4-4.4',
    chapterName: 'Measurement of Matter',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the total positive charge in electronic units on the ferric cation in ferric oxide (Fe2O3)?',
    correctAnswer: '3',
    solution: 'In Fe2O3, iron is in the ferric state with an oxidation state / ionic charge of +3.',
    difficulty: 'easy', bloomLevel: 'understand'
  },

  // =========================================================================
  // 4. MH-9-SCIT-11: Reflection of Light (18 questions -> Total = 27)
  // =========================================================================
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A ray of light is incident on a plane mirror at an angle of incidence of 42 degrees. What is the total angle of deviation in degrees experienced by the light ray? (Formula: Deviation delta = 180 - 2 * i)',
    correctAnswer: '96',
    solution: 'Given: i = 42 degrees. Angle of deviation delta = 180 - 2 * i = 180 - (2 * 42) = 180 - 84 = 96 degrees.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are placed at an angle of 40 degrees to each other. How many images of a lighted matchstick placed between them will be observed? (Formula: n = (360 / theta) - 1)',
    correctAnswer: '8',
    solution: 'Given: theta = 40 degrees. Number of images n = (360 / theta) - 1 = (360 / 40) - 1 = 9 - 1 = 8 images.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Two plane mirrors are inclined at an angle of 30 degrees. How many images of a coin placed between them are visible? (Formula: n = (360 / theta) - 1)',
    correctAnswer: '11',
    solution: 'Given: theta = 30 degrees. Number of images n = (360 / 30) - 1 = 12 - 1 = 11 images.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A person stands 3 metres in front of a vertical dressing mirror. If the person walks 1 metre closer to the mirror, what will be the distance in metres between the person and their image?',
    correctAnswer: '4',
    solution: 'New object distance = 3 - 1 = 2 metres. Image distance = 2 metres. Total distance between person and image = 2 + 2 = 4 metres.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A spherical concave makeup mirror has a radius of curvature of 60 cm. What is its focal length in cm? (Formula: f = R / 2)',
    correctAnswer: '30',
    solution: 'Given: R = 60 cm. Focal length f = R / 2 = 60 / 2 = 30 cm.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A convex security mirror installed in a shopping mall has a focal length of 40 cm. What is its radius of curvature in cm?',
    correctAnswer: '80',
    solution: 'Given: f = 40 cm. Radius of curvature R = 2 * f = 2 * 40 = 80 cm.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.3',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object of height 5 cm placed before a concave mirror produces an image of height 15 cm. What is the magnification magnitude produced by the mirror?',
    correctAnswer: '3',
    solution: 'Given: h1 = 5 cm, h2 = 15 cm. Magnification M = h2 / h1 = 15 / 5 = 3.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.3',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A concave mirror produces an image that is twice as tall as the object (magnification magnitude = 2). If the object height is 3.5 cm, what is the image height in cm?',
    correctAnswer: '7',
    solution: 'Given: M = 2, h1 = 3.5 cm. Image height h2 = M * h1 = 2 * 3.5 = 7 cm.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A candle is placed at 60 cm in front of a concave mirror having a focal length of 20 cm. At what distance in cm in front of the mirror is the real image formed? (Formula: 1/f = 1/v + 1/u)',
    correctAnswer: '30',
    solution: 'Given: u = -60 cm, f = -20 cm. 1/v = 1/f - 1/u = -1/20 - (-1/60) = -3/60 + 1/60 = -2/60 = -1/30. Therefore v = -30 cm (30 cm in front of mirror).',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object is placed at a distance of 10 cm in front of a concave mirror of focal length 15 cm. At what distance in cm behind the mirror is the virtual upright image formed?',
    correctAnswer: '30',
    solution: 'Given: u = -10 cm, f = -15 cm. 1/v = 1/f - 1/u = -1/15 - (-1/10) = -1/15 + 1/10 = (-2 + 3)/30 = +1/30. Therefore v = +30 cm (30 cm behind the mirror).',
    difficulty: 'hard', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A convex mirror with focal length 20 cm forms an image of an object placed 20 cm in front of it. At what distance in cm behind the mirror is the image located? (For convex mirror: f = +20 cm, u = -20 cm)',
    correctAnswer: '10',
    solution: 'Given: f = +20 cm, u = -20 cm. 1/v = 1/f - 1/u = 1/20 - (-1/20) = 1/20 + 1/20 = 2/20 = 1/10. Therefore v = +10 cm.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.4',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A concave mirror of focal length 10 cm forms a real image at 20 cm in front of the mirror. What is the magnification M of the image? (Formula: M = -v / u)',
    correctAnswer: '1',
    solution: 'Given: f = -10 cm, v = -20 cm. Since v = 2f, object is at center of curvature u = -20 cm. Magnification magnitude M = |-v / u| = |-(-20) / (-20)| = 1.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.5',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'In a solar furnace using a large concave mirror of focal length 1.5 metres, at what distance in metres from the pole of the mirror should the cooking pot be placed to receive maximum concentrated solar heat?',
    correctAnswer: '1.5',
    solution: 'Sun rays arrive parallel to the principal axis and converge exactly at the principal focus. The pot must be placed at the focal point, distance = 1.5 metres.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.5',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A dentist uses a small concave mirror of focal length 3 cm to examine a tooth held 2 cm from the mirror. What is the magnification magnitude of the tooth image? (Formula: M = -v / u)',
    correctAnswer: '3',
    solution: 'Given: u = -2 cm, f = -3 cm. 1/v = 1/(-3) - 1/(-2) = -1/3 + 1/2 = 1/6 => v = +6 cm. Magnification M = -v / u = -6 / (-2) = 3.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.5',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'In a car headlight reflector, a small incandescent bulb is placed at the focus 5 cm from the vertex of a concave mirror. What is the radius of curvature of the reflector mirror in cm?',
    correctAnswer: '10',
    solution: 'Given: Focal length f = 5 cm. Radius of curvature R = 2 * f = 2 * 5 = 10 cm.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.1',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If the angle between the incident ray and the reflected ray from a plane mirror is 80 degrees, what is the angle of incidence in degrees?',
    correctAnswer: '40',
    solution: 'By the law of reflection, angle of incidence i = angle of reflection r. Total angle between rays = i + r = 2i = 80 degrees. Therefore i = 40 degrees.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.2',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A convex rear-view mirror has a radius of curvature of 2 metres (200 cm). What is the focal length of the mirror in metres?',
    correctAnswer: '1',
    solution: 'Given: R = 2 m. Focal length f = R / 2 = 2 / 2 = 1 metre.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-11-11.3',
    chapterName: 'Reflection of Light',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An object placed 15 cm in front of a mirror forms an image at 45 cm on the same side. What is the magnification magnitude?',
    correctAnswer: '3',
    solution: 'Given: u = 15 cm, v = 45 cm. Magnification M = v / u = 45 / 15 = 3.',
    difficulty: 'easy', bloomLevel: 'apply'
  },

  // =========================================================================
  // 5. MH-9-SCIT-12: Study of Sound (18 questions -> Total = 27)
  // =========================================================================
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A sound wave of frequency 200 Hz has a wavelength of 1.7 metres in air. What is the speed of the sound wave in m/s? (Formula: v = nu * lambda)',
    correctAnswer: '340',
    solution: 'Given: Frequency nu = 200 Hz, Wavelength lambda = 1.7 m. Speed v = 200 * 1.7 = 340 m/s.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the time period in seconds of a sound wave vibrating at an audible frequency of 500 Hz? (Formula: T = 1 / nu)',
    correctAnswer: '0.002',
    solution: 'Given: Frequency nu = 500 Hz. Time period T = 1 / nu = 1 / 500 = 0.002 seconds.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A source produces 20 crests and 20 troughs in 0.2 seconds. What is the frequency of the wave in Hertz (Hz)?',
    correctAnswer: '100',
    solution: '20 complete waves in 0.2 s. Frequency nu = Number of waves / time = 20 / 0.2 = 100 Hz.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.2',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'Sound travels through an aluminum rod at a speed of 6420 m/s. How many seconds will a sound impulse take to travel through an aluminum pipeline 3210 metres long?',
    correctAnswer: '0.5',
    solution: 'Given: Distance d = 3210 m, Speed v = 6420 m/s. Time t = d / v = 3210 / 6420 = 0.5 seconds.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.2',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'If the velocity of sound in iron is 5000 m/s and in air is 340 m/s, what is the ratio of the speed of sound in iron to that in air? (Round to 2 decimal places)',
    correctAnswer: '14.71',
    solution: 'Ratio = 5000 / 340 = 14.7058... = 14.71.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A trekker claps between two parallel hills and hears the first echo after 1.5 seconds. If the speed of sound is 340 m/s, what is the distance in metres to the nearer hill?',
    correctAnswer: '255',
    solution: 'Given: t = 1.5 s, v = 340 m/s. Distance to nearer cliff d = (v * t) / 2 = (340 * 1.5) / 2 = 510 / 2 = 255 metres.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'At 0 degrees C, the speed of sound in air is 331 m/s. What is the minimum distance in metres required from a reflecting surface to hear an echo? (Persistence of hearing = 0.1 s; round to 2 decimal places)',
    correctAnswer: '16.55',
    solution: 'Given: v = 331 m/s, t = 0.1 s. Minimum distance d = (v * t) / 2 = (331 * 0.1) / 2 = 33.1 / 2 = 16.55 metres.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A girl stands 850 m from a high mountain and blows a whistle. After how many seconds will she hear her echo if sound travels at 340 m/s?',
    correctAnswer: '5',
    solution: 'Given: d = 850 m, v = 340 m/s. Round trip distance = 2 * 850 = 1700 m. Time t = 1700 / 340 = 5 seconds.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A SONAR transmitter on a ship emits an ultrasound pulse which returns from an underwater reef after 2.8 seconds. If the speed of sound in seawater is 1500 m/s, what is the depth of the reef in metres?',
    correctAnswer: '2100',
    solution: 'Given: t = 2.8 s, v = 1500 m/s. Depth d = (v * t) / 2 = (1500 * 2.8) / 2 = 4200 / 2 = 2100 metres.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A bat flying in the dark emits an ultrasonic squeak of frequency 40 kHz (40,000 Hz). If the speed of sound in air is 340 m/s, what is the wavelength of the bat ultrasonic squeak in millimetres (mm)?',
    correctAnswer: '8.5',
    solution: 'Given: v = 340 m/s, nu = 40,000 Hz. Wavelength lambda = 340 / 40000 = 0.0085 m = 8.5 mm.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A bat detects an obstacle when its ultrasonic echo returns after 0.04 seconds. If sound travels at 340 m/s, how far in metres is the obstacle from the bat?',
    correctAnswer: '6.8',
    solution: 'Given: t = 0.04 s, v = 340 m/s. Distance d = (v * t) / 2 = (340 * 0.04) / 2 = 13.6 / 2 = 6.8 metres.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.5',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'An obstetrician uses diagnostic ultrasound of frequency 2 MHz (2 * 10^6 Hz). If ultrasound moves through amniotic fluid at 1500 m/s, what is the wavelength in millimetres (mm)?',
    correctAnswer: '0.75',
    solution: 'Given: v = 1500 m/s, nu = 2 * 10^6 Hz. Wavelength lambda = 1500 / (2 * 10^6) = 0.00075 m = 0.75 mm.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'What is the wavelength in metres of an infrasonic wave having a frequency of 10 Hz traveling through air at 340 m/s?',
    correctAnswer: '34',
    solution: 'Given: nu = 10 Hz, v = 340 m/s. Wavelength lambda = v / nu = 340 / 10 = 34 metres.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A vibrating diaphragm produces a sound wave of wavelength 0.5 m with a frequency of 680 Hz. What is the speed of sound in m/s?',
    correctAnswer: '340',
    solution: 'Given: lambda = 0.5 m, nu = 680 Hz. Speed v = nu * lambda = 680 * 0.5 = 340 m/s.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.2',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A flash of lightning is seen, and thunder is heard 4 seconds later. If the speed of sound in air is 340 m/s, how far in metres did the lightning strike occur?',
    correctAnswer: '1360',
    solution: 'Given: t = 4 s, v = 340 m/s. Distance d = v * t = 340 * 4 = 1360 metres.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.3',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A person standing between two cliffs produces a sound and hears two echoes after 2 seconds and 3 seconds respectively. What is the total distance in metres between the two cliffs? (Speed of sound = 340 m/s)',
    correctAnswer: '850',
    solution: 'Distance to first cliff d1 = (340 * 2) / 2 = 340 m. Distance to second cliff d2 = (340 * 3) / 2 = 510 m. Total distance between cliffs = 340 + 510 = 850 metres.',
    difficulty: 'hard', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.4',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'A marine vessel SONAR unit emits ultrasound that reaches a seabed depth of 4500 metres. How many seconds will the signal take to return to the vessel? (Speed of sound in seawater = 1500 m/s)',
    correctAnswer: '6',
    solution: 'Total round trip distance = 2 * 4500 = 9000 m. Time t = 9000 / 1500 = 6 seconds.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-9-SCIT-12-12.1',
    chapterName: 'Study of Sound',
    subject: 'Science and Technology',
    className: 'Class 9',
    text: 'How many sound vibrations are completed by a 440 Hz musical tuning fork in 5 seconds?',
    correctAnswer: '2200',
    solution: 'Total vibrations = Frequency * time = 440 vibrations/second * 5 seconds = 2200 vibrations.',
    difficulty: 'easy', bloomLevel: 'apply'
  },

  // =========================================================================
  // 6. MH-8-SCI-3: Force and Pressure (18 questions -> Total = 28)
  // =========================================================================
  {
    topicCode: 'MH-8-SCI-3-3.3.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A force of 150 N is applied uniformly over an area of 0.5 m^2. Calculate the pressure exerted in Pascals (N/m^2). (Formula: P = F / A)',
    correctAnswer: '300',
    solution: 'Given: Force F = 150 N, Area A = 0.5 m^2. Pressure P = F / A = 150 / 0.5 = 300 Pascals.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A girl weighing 450 N stands on one foot with a shoe sole area of 0.015 m^2. What pressure in Pascals does she exert on the ground?',
    correctAnswer: '30000',
    solution: 'Given: F = 450 N, A = 0.015 m^2. Pressure P = 450 / 0.015 = 30,000 Pascals (30 kPa).',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'What force in Newtons must be applied over a piston of area 0.2 m^2 to generate a hydraulic pressure of 5000 Pa? (Formula: F = P * A)',
    correctAnswer: '1000',
    solution: 'Given: Pressure P = 5000 Pa, Area A = 0.2 m^2. Force F = P * A = 5000 * 0.2 = 1000 Newtons.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A sharp knife edge has an area of 0.0002 m^2. If pressed against an apple with a force of 20 N, what pressure in Pascals is applied?',
    correctAnswer: '100000',
    solution: 'Given: F = 20 N, A = 0.0002 m^2. Pressure P = 20 / 0.0002 = 100,000 Pascals (10^5 Pa).',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'An elephant of mass 4000 kg stands on 4 feet. If the area of each foot is 0.1 m^2, what is the total pressure in Pascals exerted by the elephant on the ground? (Take g = 10 m/s^2)',
    correctAnswer: '100000',
    solution: 'Total weight F = m * g = 4000 * 10 = 40,000 N. Total area of 4 feet = 4 * 0.1 = 0.4 m^2. Pressure P = 40,000 / 0.4 = 100,000 Pascals.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-8-SCI-3-3.3.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A rectangular brick weighing 30 N measures 0.2 m by 0.1 m by 0.05 m. What is the maximum pressure in Pascals it can exert on a table when resting on its smallest face (0.1 m x 0.05 m)?',
    correctAnswer: '6000',
    solution: 'Smallest face area = 0.1 * 0.05 = 0.005 m^2. Maximum pressure = Weight / Smallest area = 30 / 0.005 = 6000 Pascals.',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'Calculate the liquid pressure in Pascals at the base of a water cylinder filled to a height of 2 metres. (Density of water = 1000 kg/m^3, take g = 9.8 m/s^2. Formula: P = h * rho * g)',
    correctAnswer: '19600',
    solution: 'Given: h = 2 m, rho = 1000 kg/m^3, g = 9.8 m/s^2. Pressure P = 2 * 1000 * 9.8 = 19,600 Pascals.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A column of mercury of density 13,600 kg/m^3 has a height of 0.76 m. What pressure in Pascals does this mercury column exert? (Take g = 9.8 m/s^2; round to nearest integer)',
    correctAnswer: '101293',
    solution: 'Given: h = 0.76 m, rho = 13600 kg/m^3, g = 9.8 m/s^2. P = 0.76 * 13600 * 9.8 = 101,292.8 Pa => 101,293 Pascals (Standard 1 atm).',
    difficulty: 'medium', bloomLevel: 'calculate'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'At what depth in metres in fresh water is the water pressure equal to 49,000 Pascals? (Density = 1000 kg/m^3, g = 9.8 m/s^2. Formula: h = P / (rho * g))',
    correctAnswer: '5',
    solution: 'Given: P = 49000 Pa, rho = 1000, g = 9.8. Depth h = 49000 / (1000 * 9.8) = 49000 / 9800 = 5 metres.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'Standard atmospheric pressure at sea level is approximately 101.3 kPa. How many Pascals (Pa) is this equivalent to?',
    correctAnswer: '101300',
    solution: '1 kPa = 1000 Pa. Therefore, 101.3 kPa = 101.3 * 1000 = 101,300 Pascals.',
    difficulty: 'easy', bloomLevel: 'understand'
  },
  {
    topicCode: 'MH-8-SCI-3-3.4.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'If 1 bar of pressure equals 10^5 Pascals (100,000 Pa), how many bars is a pressure of 250,000 Pascals?',
    correctAnswer: '2.5',
    solution: 'Bars = 250,000 / 100,000 = 2.5 bar.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A metal cube of volume 0.002 m^3 is completely submerged in water (density = 1000 kg/m^3). What is the buoyant upthrust force in Newtons exerted by the water on the cube? (Take g = 9.8 m/s^2. Formula: F_b = V * rho * g)',
    correctAnswer: '19.6',
    solution: 'Given: V = 0.002 m^3, rho = 1000 kg/m^3, g = 9.8 m/s^2. Buoyant force F_b = V * rho * g = 0.002 * 1000 * 9.8 = 19.6 Newtons.',
    difficulty: 'medium', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.1',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A solid body weighs 50 N in air and 42 N when completely immersed in water. What is the buoyant force in Newtons acting on the body?',
    correctAnswer: '8',
    solution: 'Buoyant force = Apparent loss of weight = Weight in air - Weight in water = 50 - 42 = 8 Newtons.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.2',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'According to Archimedes’ principle, an object immersed in liquid experiences an upward buoyant force equal to the weight of liquid displaced. If a floating block displaces 1.2 kg of water, what is the magnitude of the buoyant force in Newtons? (Take g = 9.8 m/s^2)',
    correctAnswer: '11.76',
    solution: 'Mass of water displaced = 1.2 kg. Weight of displaced water = m * g = 1.2 * 9.8 = 11.76 Newtons.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'A piece of silver has a mass of 210 grams and a volume of 20 cm^3. What is the density of silver in g/cm^3? (Formula: Density = Mass / Volume)',
    correctAnswer: '10.5',
    solution: 'Given: Mass = 210 g, Volume = 20 cm^3. Density = 210 / 20 = 10.5 g/cm^3.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'The density of gold is 19.3 g/cm^3. What is the mass in grams of a pure gold bar having a volume of 50 cm^3?',
    correctAnswer: '965',
    solution: 'Given: Density = 19.3 g/cm^3, Volume = 50 cm^3. Mass = Density * Volume = 19.3 * 50 = 965 grams.',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'The density of a substance is 8000 kg/m^3. Since the density of water is 1000 kg/m^3, what is the relative density of the substance? (Formula: Relative Density = Density of substance / Density of water)',
    correctAnswer: '8',
    solution: 'Relative density = 8000 / 1000 = 8 (a dimensionless quantity).',
    difficulty: 'easy', bloomLevel: 'apply'
  },
  {
    topicCode: 'MH-8-SCI-3-3.5.3',
    chapterName: 'Force and Pressure',
    subject: 'General Science',
    className: 'Class 8',
    text: 'If the relative density of lead is 11.3 and the density of water is 1000 kg/m^3, what is the density of lead in kg/m^3?',
    correctAnswer: '11300',
    solution: 'Density of lead = Relative density * Density of water = 11.3 * 1000 = 11,300 kg/m^3.',
    difficulty: 'easy', bloomLevel: 'apply'
  }
];

async function runFullEnrichment() {
  console.log(`Starting full enrichment of ${CHAPTER_NUMERICALS.length} authentic numerical questions...`);

  // 1. Gather all protected question IDs from exams
  const usedQuestionIds = new Set();
  const examsSnap = await db.collection('exams').select('questionCodes').get();
  examsSnap.forEach(doc => {
    const codes = doc.data().questionCodes || [];
    codes.forEach(c => usedQuestionIds.add(c));
  });

  console.log(`Identified ${usedQuestionIds.size} protected used question identifiers.`);

  // 2. Pair each new numerical with an unused theoretical question in the same topic
  const replacementPairs = [];

  for (const nq of CHAPTER_NUMERICALS) {
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
      console.warn(`Could not find an unused theoretical question for topic ${nq.topicCode}`);
    }
  }

  console.log(`Found ${replacementPairs.length} eligible target questions to replace.`);

  // 3. Pre-Mutation Snapshot (Rule 2Q)
  const now = new Date();
  const timestamp = now.toISOString().replace(/[:.]/g, '-');
  const snapshotDir = path.join(process.cwd(), 'backups', 'snapshots');
  if (!fs.existsSync(snapshotDir)) fs.mkdirSync(snapshotDir, { recursive: true });
  const snapshotFile = path.join(snapshotDir, `snapshot_${timestamp}_enrich_102_formula_numericals.json`);

  const snapshotData = {
    timestamp: now.toISOString(),
    reason: 'Replace 102 unused theoretical questions to reach 25-30+ authentic Balbharti numericals per formula-heavy chapter',
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

  // 4. Atomic batch writes
  let batch = db.batch();
  let opCount = 0;

  for (const pair of replacementPairs) {
    const original = pair.targetDoc.data();
    const nq = pair.newQuestion;

    const seqMatch = String(original.questionCode || pair.targetDoc.id).match(/(\d{3,})$/);
    const seq = seqMatch ? seqMatch[1] : '060';
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

  console.log(`Successfully updated ${replacementPairs.length} questions across all formula-based chapters!`);
}

runFullEnrichment().then(() => process.exit(0)).catch(console.error);
