const path = require('path');
const fs = require('fs');

// Load environment variables
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

const admin = require('firebase-admin');
const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || 'ai-yashcom';

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  if (serviceAccount) {
    const credential = JSON.parse(
      serviceAccount.startsWith('{')
        ? serviceAccount
        : Buffer.from(serviceAccount, 'base64').toString('utf-8')
    );
    admin.initializeApp({
      credential: admin.credential.cert(credential)
    });
  } else {
    admin.initializeApp({ projectId });
  }
}

const db = admin.firestore();

async function runSnapshotAndHeal() {
  console.log('--- Step 1: Rule Q Pre-Mutation Snapshot ---');
  const chatRoomsSnap = await db.collection('chatRooms').get();
  console.log(`Fetched ${chatRoomsSnap.size} total chatRooms for backup.`);

  const snapshotDir = path.join(__dirname, '..', 'backups', 'snapshots', `snapshot-chatrooms-${Date.now()}`);
  fs.mkdirSync(snapshotDir, { recursive: true });

  const backupData = {};
  chatRoomsSnap.docs.forEach(doc => {
    backupData[doc.id] = doc.data();
  });
  fs.writeFileSync(path.join(snapshotDir, 'chatRooms.json'), JSON.stringify(backupData, null, 2), 'utf-8');
  console.log(`Saved snapshot of ${chatRoomsSnap.size} chatRooms to: ${snapshotDir}`);

  console.log('\n--- Step 2: Healing DM Rooms Missing lastMessage ---');
  let healedCount = 0;
  let alreadyGoodCount = 0;
  let emptyDmsCount = 0;

  for (const doc of chatRoomsSnap.docs) {
    const data = doc.data();
    if (data.type !== 'dm') continue;

    // Check subcollection messages
    const msgsSnap = await doc.ref.collection('messages').orderBy('createdAt', 'desc').limit(1).get();
    if (msgsSnap.empty) {
      emptyDmsCount++;
      continue;
    }

    const latestMsg = msgsSnap.docs[0].data();
    const currentLast = data.lastMessage;

    const needsHeal = !currentLast || !currentLast.text || currentLast.timestamp !== latestMsg.createdAt;

    if (needsHeal) {
      const newLastMessage = {
        text: (latestMsg.text || (latestMsg.type === 'poll' ? '📊 Poll' : '')).substring(0, 100),
        senderName: latestMsg.senderName || 'User',
        timestamp: latestMsg.createdAt || new Date().toISOString()
      };

      console.log(`Healing room ${doc.id} [${data.name}]: Setting lastMessage: "${newLastMessage.text}" by ${newLastMessage.senderName} (${newLastMessage.timestamp})`);
      await doc.ref.update({ lastMessage: newLastMessage });
      healedCount++;
    } else {
      alreadyGoodCount++;
    }
  }

  console.log('\n--- Summary ---');
  console.log(`Total DM rooms checked: ${alreadyGoodCount + healedCount + emptyDmsCount}`);
  console.log(`Healed rooms: ${healedCount}`);
  console.log(`Already good rooms: ${alreadyGoodCount}`);
  console.log(`Empty DM rooms: ${emptyDmsCount}`);
}

runSnapshotAndHeal()
  .then(() => {
    console.log('\nHealing script completed successfully!');
    process.exit(0);
  })
  .catch(err => {
    console.error('Error during healing script:', err);
    process.exit(1);
  });
