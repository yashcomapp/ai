const admin = require('firebase-admin');
const fs = require('fs');
const path = require('path');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
const envVars = {};
envContent.split('\n').forEach(line => {
  const trimmed = line.trim();
  if (trimmed && !trimmed.startsWith('#')) {
    const idx = trimmed.indexOf('=');
    if (idx > 0) {
      let v = trimmed.slice(idx + 1).trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      envVars[trimmed.slice(0, idx).trim()] = v;
    }
  }
});
const sa = envVars.FIREBASE_SERVICE_ACCOUNT_KEY;
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

const final6 = {
  'MH-8-SCI-5-5.3.1-OSC-016': {
    text: "According to Bohr's atomic model, which of the following electron shells has the highest energy?",
    options: [
      'K shell',
      'L shell',
      'M shell',
      'N shell'
    ],
    correctAnswer: 'D',
    explanation: 'Electron shells further from the nucleus possess higher energy, so the N shell (\\(n = 4\\)) has higher energy than K, L, and M shells.'
  },
  'MH-8-SCI-5-5.3.1-OSC-027': {
    text: "What is the maximum number of electrons that can be accommodated in the outermost valence shell of any stable atom?",
    options: [
      '2 electrons',
      '8 electrons',
      '18 electrons',
      '32 electrons'
    ],
    correctAnswer: 'B',
    explanation: 'According to the octet rule, the outermost shell of an atom cannot accommodate more than 8 electrons.'
  },
  'MH-8-SCI-5-5.4.1-OSC-007': {
    text: "Which subatomic particle located in the nucleus carries a unit positive electric charge?",
    options: [
      'Proton',
      'Neutron',
      'Electron',
      'Alpha particle'
    ],
    correctAnswer: 'A',
    explanation: 'The proton is the positively charged subatomic particle residing in the nucleus of an atom.'
  },
  'MH-8-SCI-5-5.4.2-OSC-006': {
    text: "Where are neutrons located inside an atom?",
    options: [
      'Revolving in the outermost electron shell',
      'Inside the nucleus along with protons',
      'In the space between electron shells',
      'Floating outside the boundary of the atom'
    ],
    correctAnswer: 'B',
    explanation: 'Neutrons are situated inside the central atomic nucleus together with protons; collectively they are called nucleons.'
  },
  'MH-8-SCI-5-5.4.3-OSC-009': {
    text: "Which scientist discovered the electron in 1897 through cathode ray experiments?",
    options: [
      'John Dalton',
      'Ernest Rutherford',
      'J.J. Thomson',
      'James Chadwick'
    ],
    correctAnswer: 'C',
    explanation: 'J.J. Thomson discovered the electron in 1897 and showed that cathode rays are streams of negatively charged particles.'
  },
  'MH-8-SCI-5-5.4.3-OSC-018': {
    text: "Why is an atom electrically neutral under normal conditions?",
    options: [
      'Because it contains no charged particles at all',
      'Because the number of positively charged protons equals the number of negatively charged electrons',
      'Because neutrons cancel out the charge of the nucleus',
      'Because electrons absorb all positive charges'
    ],
    correctAnswer: 'B',
    explanation: 'An atom is electrically neutral because the total positive charge of its nuclear protons equals the total negative charge of its revolving electrons.'
  }
};

async function updateFinal6() {
  const batch = db.batch();
  for (const [id, data] of Object.entries(final6)) {
    const ref = db.collection('questions').doc(id);
    batch.update(ref, {
      text: data.text,
      options: data.options,
      correctAnswer: data.correctAnswer,
      explanation: data.explanation,
      solution: data.explanation,
      updatedAt: admin.firestore.FieldValue.serverTimestamp()
    });
  }
  await batch.commit();
  console.log('Committed final 6 updates.');
}

updateFinal6().catch(console.error);
