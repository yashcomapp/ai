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

// Subtopic metadata
const SUBTOPIC_INFO = {
  '1.1.1': {
    parentTopicCode: 'MH-9-SCIT-1-1.1',
    parentTopicName: 'Distance, Displacement, Speed and Velocity',
    subtopicCode: 'MH-9-SCIT-1-1.1.1',
    subtopicName: 'Scalar distance vs vector displacement'
  },
  '1.1.2': {
    parentTopicCode: 'MH-9-SCIT-1-1.1',
    parentTopicName: 'Distance, Displacement, Speed and Velocity',
    subtopicCode: 'MH-9-SCIT-1-1.1.2',
    subtopicName: 'Speed = distance / time, Velocity = displacement / time'
  },
  '1.1.3': {
    parentTopicCode: 'MH-9-SCIT-1-1.1',
    parentTopicName: 'Distance, Displacement, Speed and Velocity',
    subtopicCode: 'MH-9-SCIT-1-1.1.3',
    subtopicName: 'Uniform vs non-uniform motion along straight line'
  },
  '1.2.2': {
    parentTopicCode: 'MH-9-SCIT-1-1.2',
    parentTopicName: 'Acceleration (Positive, Negative/Deceleration, Zero)',
    subtopicCode: 'MH-9-SCIT-1-1.2.2',
    subtopicName: 'SI unit m/s²'
  },
  '1.5.1': {
    parentTopicCode: 'MH-9-SCIT-1-1.5',
    parentTopicName: 'Uniform Circular Motion & Centripetal Force',
    subtopicCode: 'MH-9-SCIT-1-1.5.1',
    subtopicName: 'v = 2πr / t'
  },
  '1.5.2': {
    parentTopicCode: 'MH-9-SCIT-1-1.5',
    parentTopicName: 'Uniform Circular Motion & Centripetal Force',
    subtopicCode: 'MH-9-SCIT-1-1.5.2',
    subtopicName: 'Centripetal force towards center formula F = mv²/r'
  },
  '1.6.1': {
    parentTopicCode: 'MH-9-SCIT-1-1.6',
    parentTopicName: 'Newton Three Laws of Motion & Law of Conservation of Momentum',
    subtopicCode: 'MH-9-SCIT-1-1.6.1',
    subtopicName: 'First law (Inertia)'
  },
  '1.6.2': {
    parentTopicCode: 'MH-9-SCIT-1-1.6',
    parentTopicName: 'Newton Three Laws of Motion & Law of Conservation of Momentum',
    subtopicCode: 'MH-9-SCIT-1-1.6.2',
    subtopicName: 'Second law (F = ma)'
  },
  '1.6.3': {
    parentTopicCode: 'MH-9-SCIT-1-1.6',
    parentTopicName: 'Newton Three Laws of Motion & Law of Conservation of Momentum',
    subtopicCode: 'MH-9-SCIT-1-1.6.3',
    subtopicName: 'Third law (Action and Reaction)'
  },
  '1.6.4': {
    parentTopicCode: 'MH-9-SCIT-1-1.6',
    parentTopicName: 'Newton Three Laws of Motion & Law of Conservation of Momentum',
    subtopicCode: 'MH-9-SCIT-1-1.6.4',
    subtopicName: 'Conservation of momentum (m1u1 + m2u2 = m1v1 + m2v2)'
  },
  '1.6.5': {
    parentTopicCode: 'MH-9-SCIT-1-1.6',
    parentTopicName: 'Newton Three Laws of Motion & Law of Conservation of Momentum',
    subtopicCode: 'MH-9-SCIT-1-1.6.5',
    subtopicName: 'Recoil of gun'
  }
};

module.exports = { db, SUBTOPIC_INFO };
