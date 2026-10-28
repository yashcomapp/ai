const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  fs.readFileSync(envPath, 'utf8').split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[trimmed.slice(0, idx).trim()] = val;
      }
    }
  });
}

const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
if (serviceAccount) {
  const cred = JSON.parse(serviceAccount.startsWith('{') ? serviceAccount : Buffer.from(serviceAccount, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
} else {
  admin.initializeApp({ projectId: 'ai-yashcom' });
}

const db = admin.firestore();

const DEFAULT_OAR_OPTIONS = [
  "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
  "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
  "Assertion (A) is true, but Reason (R) is false.",
  "Assertion (A) is false, but Reason (R) is true."
];

const manual7Fixes = {
  "CBSE-8-CURI-5-5.3.5-OAR-002": {
    assertion: "A spring balance calibrated in Newtons can be used to measure the weight of an object.",
    reason: "Weight is a downward gravitational force, and forces are measured in Newtons.",
    text: "Assertion (A): A spring balance calibrated in Newtons can be used to measure the weight of an object.\nReason (R): Weight is a downward gravitational force, and forces are measured in Newtons."
  },
  "MH-10-SCIT1-10-10.3.1-OAR-005": {
    assertion: "Geostationary satellites are completely ineffective for establishing high-speed, real-time interactive financial trading networks.",
    reason: "The inherent propagation delay caused by the 35,786 km altitude creates a round-trip latency of about 250 milliseconds, which is too slow for high-frequency trading.",
    text: "Assertion (A): Geostationary satellites are completely ineffective for establishing high-speed, real-time interactive financial trading networks.\nReason (R): The inherent propagation delay caused by the 35,786 km altitude creates a round-trip latency of about 250 milliseconds, which is too slow for high-frequency trading."
  },
  "MH-10-SCIT1-8-8.6-OAR-006": {
    assertion: "Galvanized iron items retain their corrosion resistance even when the outer zinc coating is scratched and the underlying iron is exposed.",
    reason: "Zinc has a lower reduction potential than iron, making it act as a sacrificial anode that preferentially oxidizes.",
    text: "Assertion (A): Galvanized iron items retain their corrosion resistance even when the outer zinc coating is scratched and the underlying iron is exposed.\nReason (R): Zinc has a lower reduction potential than iron, making it act as a sacrificial anode that preferentially oxidizes."
  },
  "MH-10-SCIT2-1-1.3.4-OAR-003": {
    assertion: "Paleontological evidence provides concrete historical proof of organic evolution.",
    reason: "Fossils recovered from successive sedimentary strata display a sequence of gradual structural changes from simple to complex organisms.",
    text: "Assertion (A): Paleontological evidence provides concrete historical proof of organic evolution.\nReason (R): Fossils recovered from successive sedimentary strata display a sequence of gradual structural changes from simple to complex organisms."
  },
  "MH-10-SCIT2-8-8.5.2-OAR-003": {
    assertion: "India transitioned from being a milk-deficient nation to the world's leading milk producer.",
    reason: "The replication of the Anand dairy cooperative pattern across India under Operation Flood achieved massive scalability.",
    text: "Assertion (A): India transitioned from being a milk-deficient nation to the world's leading milk producer.\nReason (R): The replication of the Anand dairy cooperative pattern across India under Operation Flood achieved massive scalability."
  },
  "MH-8-MTH-13-13.3.1-OAR-002": {
    assertion: "The AAA test is a valid criterion to prove two triangles are congruent.",
    reason: "AAA ensures that two triangles have identical corresponding side lengths as well as angles.",
    text: "Assertion (A): The AAA test is a valid criterion to prove two triangles are congruent.\nReason (R): AAA ensures that two triangles have identical corresponding side lengths as well as angles."
  },
  "MH-8-MTH-4-4.1.2-OAR-003": {
    assertion: "In a right-angled triangle, the altitude to the hypotenuse lies entirely inside the triangle.",
    reason: "The hypotenuse lies opposite to the right angle, allowing a perpendicular drop from the vertex inside the triangle boundary.",
    text: "Assertion (A): In a right-angled triangle, the altitude to the hypotenuse lies entirely inside the triangle.\nReason (R): The hypotenuse lies opposite to the right angle, allowing a perpendicular drop from the vertex inside the triangle boundary."
  }
};

async function fix7() {
  const batch = db.batch();
  for (const [id, f] of Object.entries(manual7Fixes)) {
    const ref = db.collection('questions').doc(id);
    batch.update(ref, {
      assertion: f.assertion,
      reason: f.reason,
      text: f.text,
      options: DEFAULT_OAR_OPTIONS,
      updatedAt: new Date()
    });
  }
  await batch.commit();
  console.log('✓ Successfully fixed the remaining 7 OAR questions!');
}

fix7().then(() => process.exit(0)).catch(e => { console.error(e); process.exit(1); });
