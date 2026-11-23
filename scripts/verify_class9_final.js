const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const fs = require('fs');
const path = require('path');
const admin = require('firebase-admin');

const envContent = fs.readFileSync(path.join(__dirname, '..', '.env.local'), 'utf-8');
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
if (!admin.apps.length) {
  const cred = JSON.parse(sa.startsWith('{') ? sa : Buffer.from(sa, 'base64').toString('utf-8'));
  admin.initializeApp({ credential: admin.credential.cert(cred) });
}
const db = admin.firestore();

async function verifyClass9() {
  const subjects = ['cbse_9_mgm', 'cbse_9_scie', 'mh_9_mth1', 'mh_9_mth2', 'mh_9_scit'];
  
  console.log('======================================================================');
  console.log('             CLASS 9 FINAL COMPLIANCE & READINESS AUDIT               ');
  console.log('======================================================================\n');

  let grandTotalLeaf = 0;
  let grandTotalQs = 0;
  let grandTargetQs = 0;
  let grandDeficitLeaf = 0;

  for (const subId of subjects) {
    const doc = await db.collection('syllabus').doc(subId).get();
    if (!doc.exists) {
      console.log('MISSING DOC: ' + subId);
      continue;
    }
    const data = doc.data();
    let totalLeaf = 0;
    let deficitLeaf = 0;
    let totalQuestions = 0;
    let below80Details = [];

    (data.chapters || []).forEach(ch => {
      (ch.topics || []).forEach(top => {
        const subtopics = top.subtopics || [];
        if (subtopics.length > 0) {
          subtopics.forEach(sub => {
            totalLeaf++;
            const count = (sub.objectiveCount || 0);
            totalQuestions += count;
            if (count < 80) {
              deficitLeaf++;
              below80Details.push({ code: sub.code, title: sub.title, count });
            }
          });
        } else {
          totalLeaf++;
          const count = (top.objectiveCount || 0);
          totalQuestions += count;
          if (count < 80) {
            deficitLeaf++;
            below80Details.push({ code: top.code, title: top.title, count });
          }
        }
      });
    });

    grandTotalLeaf += totalLeaf;
    grandTotalQs += totalQuestions;
    grandTargetQs += (totalLeaf * 80);
    grandDeficitLeaf += deficitLeaf;

    console.log(`Subject: ${data.name} (${subId})`);
    console.log(`  Chapters:             ${(data.chapters || []).length}`);
    console.log(`  Total Leaf Subtopics: ${totalLeaf}`);
    console.log(`  Total Objective Qs:   ${totalQuestions}`);
    console.log(`  Target (80 Qs/sub):   ${totalLeaf * 80}`);
    console.log(`  Surplus / Deficit:    ${totalQuestions >= totalLeaf * 80 ? '+' + (totalQuestions - totalLeaf * 80) : '-' + (totalLeaf * 80 - totalQuestions)}`);
    console.log(`  Subtopics < 80 Qs:    ${deficitLeaf}`);
    if (deficitLeaf > 0) {
      console.log('  Deficit items:', below80Details.slice(0, 5));
    }
    console.log(`  Compliance Status:    ${deficitLeaf === 0 ? '✅ 100% COMPLIANT' : '❌ DEFICIT DETECTED'}\n`);
  }

  console.log('----------------------------------------------------------------------');
  console.log('GRADE 9 SUMMARY:');
  console.log(`  Total Subtopics Across All 5 Subjects: ${grandTotalLeaf}`);
  console.log(`  Total Questions in Firestore:          ${grandTotalQs}`);
  console.log(`  Required Target (80 per subtopic):     ${grandTargetQs}`);
  console.log(`  Subtopics with Deficit (< 80 Qs):      ${grandDeficitLeaf}`);
  console.log(`  Overall Compliance:                    ${grandDeficitLeaf === 0 ? '🏆 100% COMPLETE & PRODUCTION READY' : '❌ INCOMPLETE'}`);
  console.log('======================================================================\n');
}

verifyClass9().catch(err => {
  console.error(err);
  process.exit(1);
});
