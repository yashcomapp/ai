const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

const TARGET_FIXES = [
  { id: 'MH-9-SCIT-2-2.3-ONE-040', newAnswer: 'A', newValue: 98, note: 'mgh = 4 * 9.8 * 2.5 = 98 J (was B/49)' },
  { id: 'MH-9-SCIT-2-2.3-ONE-070', newAnswer: 'C', newValue: 1176, note: 'mgh = 10 * 9.8 * 12 = 1176 J (was A/588)' },
  { id: 'MH-9-SCIT-2-2.4-ONE-040', newAnswer: 'D', newValue: 900, note: 'mgh = 2 * 10 * 45 = 900 J (was B/450)' },
  { id: 'MH-9-SCIT-2-2.4-ONE-070', newAnswer: 'A', newValue: 30, note: 'KE = 30 J (was C/15)' },
  { id: 'MH-9-SCIT-3-3.1-ONE-040', newAnswer: 'C', newValue: 5, note: 'I = Q/t = 60/12 = 5 A (numericalValue was 2.5)' },
  { id: 'MH-9-SCIT-3-3.1-ONE-070', newAnswer: 'D', newValue: 120, note: 'W = V * Q = 8 * 15 = 120 J (was A/60)' },
  { id: 'MH-9-SCIT-3-3.2-ONE-040', newAnswer: 'C', newValue: 5, note: 'I = V/R = 220/44 = 5 A (was A/2.5)' },
  { id: 'MH-9-SCIT-3-3.2-ONE-070', newAnswer: 'B', newValue: 16, note: 'R = V/I = 48/3 = 16 ohm (was D/8)' },
  { id: 'MH-9-SCIT-3-3.3-ONE-040', newAnswer: 'A', newValue: 1, note: 'R = rho * L / A = 1 ohm (was B/0.5)' },
  { id: 'MH-9-SCIT-3-3.3-ONE-070', newAnswer: 'D', newValue: 16, note: 'Stretched 2x -> 4x R = 16 ohm (was B/8)' },
  { id: 'MH-9-SCIT-3-3.4-ONE-040', newAnswer: 'C', newValue: 40, note: 'Rs = 8 + 12 + 20 = 40 ohm (was B/20)' },
  { id: 'MH-9-SCIT-3-3.4-ONE-070', newAnswer: 'B', newValue: 100, note: 'Rs = 15 + 25 + 60 = 100 ohm (was A/50)' },
  { id: 'MH-9-SCIT-3-3.5-ONE-040', newAnswer: 'B', newValue: 12, note: '1/Rp = 1/20 + 1/30 -> Rp = 12 ohm (was C/6)' },
  { id: 'MH-9-SCIT-3-3.5-ONE-070', newAnswer: 'C', newValue: 2, note: '1/Rp = 1/6 + 1/12 + 1/4 = 6/12 -> Rp = 2 ohm (was D/1)' },
];

async function applyFixes() {
  const backupDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true });
  }

  const backupData = {};
  for (const item of TARGET_FIXES) {
    const doc = await adminDb.collection('questions').doc(item.id).get();
    if (doc.exists) {
      backupData[item.id] = doc.data();
    }
  }

  const backupPath = path.join(backupDir, `fix_mh9_scit_numerical_${Date.now()}.json`);
  fs.writeFileSync(backupPath, JSON.stringify(backupData, null, 2), 'utf8');
  console.log(`Saved pre-mutation backup to: ${backupPath}`);

  for (const item of TARGET_FIXES) {
    await adminDb.collection('questions').doc(item.id).update({
      correctAnswer: item.newAnswer,
      numericalValue: item.newValue,
      updatedAt: new Date()
    });
    console.log(`Fixed [${item.id}]: correctAnswer -> ${item.newAnswer}, numericalValue -> ${item.newValue} (${item.note})`);
  }

  console.log('\nAll 14 numerical anomalies successfully patched in Firestore!');
}

applyFixes().catch(console.error);
