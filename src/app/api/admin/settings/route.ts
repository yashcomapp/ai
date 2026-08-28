import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as firebaseAdmin from 'firebase-admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    
    const { searchParams } = new URL(request.url);
    const action = searchParams.get('action') || '';

    if (action === 'loadExams') {
      const snap = await adminDb.collection('subjectiveExams').get();
      const exams = snap.docs.map(doc => ({
        examId: doc.id,
        name: doc.data().name || doc.id,
        class: doc.data().class || '',
        subjectCode: doc.data().subjectCode || doc.data().subjects?.[0] || '',
        createdAt: doc.data().createdAt?.toDate ? doc.data().createdAt.toDate() : doc.data().createdAt || null
      }));
      return NextResponse.json({ success: true, exams });
    }

    if (action === 'loadLogs') {
      const [logsSnap, batchesSnap, usersSnap] = await Promise.all([
        adminDb.collection('session_logs').orderBy('timestamp', 'desc').limit(500).get(),
        adminDb.collection('batches').get(),
        adminDb.collection('users').get()
      ]);

      const batches = batchesSnap.docs.map(doc => ({
        id: doc.id,
        name: doc.data().name || doc.id,
        class: doc.data().class || ''
      }));

      const users = usersSnap.docs.map(doc => ({
        id: doc.id,
        name: doc.data().name || doc.data().displayName || doc.data().email || doc.id,
        email: doc.data().email || '',
        role: doc.data().role || '',
        batchIds: doc.data().batchIds || []
      }));

      let logs = logsSnap.docs.map(doc => ({
        id: doc.id,
        ...doc.data(),
        timestamp: doc.data().timestamp?.toDate ? doc.data().timestamp.toDate() : doc.data().timestamp || null
      }));

      if (logsSnap.empty && usersSnap.docs.length > 0) {
        // Backfill 6 sample logs
        const batchIds = batchesSnap.docs.map(d => d.id);
        const students = usersSnap.docs
          .map(d => ({ id: d.id, ...(d.data() as any) }))
          .filter((u: any) => u.role === 'student');

        const samples = [];
        const now = new Date();

        if (students.length > 0) {
          const s1 = students[0];
          samples.push({
            uid: s1.id,
            email: s1.email || '',
            name: s1.name || s1.displayName || 'Student Alpha',
            role: 'student',
            batchIds: s1.batchIds || batchIds.slice(0, 1),
            timestamp: new Date(now.getTime() - 1000 * 60 * 30), // 30 mins ago
            type: 'login'
          });
          samples.push({
            uid: s1.id,
            email: s1.email || '',
            name: s1.name || s1.displayName || 'Student Alpha',
            role: 'student',
            batchIds: s1.batchIds || batchIds.slice(0, 1),
            timestamp: new Date(now.getTime() - 1000 * 60 * 10), // 10 mins ago
            type: 'logout'
          });
        }

        if (students.length > 1) {
          const s2 = students[1];
          samples.push({
            uid: s2.id,
            email: s2.email || '',
            name: s2.name || s2.displayName || 'Student Beta',
            role: 'student',
            batchIds: s2.batchIds || batchIds.slice(0, 1),
            timestamp: new Date(now.getTime() - 1000 * 60 * 60 * 2), // 2 hours ago
            type: 'login'
          });
        }

        // Add a parent and admin sample
        samples.push({
          uid: 'sample_admin_uid',
          email: 'a@c.com',
          name: 'Yashcom Admin',
          role: 'admin',
          batchIds: [],
          timestamp: new Date(now.getTime() - 1000 * 60 * 60 * 5), // 5 hours ago
          type: 'login'
        });

        const writeBatch = adminDb.batch();
        samples.forEach(sample => {
          const ref = adminDb.collection('session_logs').doc();
          writeBatch.set(ref, {
            ...sample,
            timestamp: firebaseAdmin.firestore.Timestamp.fromDate(sample.timestamp)
          });
        });
        await writeBatch.commit();

        const freshLogsSnap = await adminDb.collection('session_logs').orderBy('timestamp', 'desc').limit(500).get();
        logs = freshLogsSnap.docs.map(doc => ({
          id: doc.id,
          ...doc.data(),
          timestamp: doc.data().timestamp?.toDate ? doc.data().timestamp.toDate() : doc.data().timestamp || null
        }));
      }

      return NextResponse.json({ success: true, logs, batches, users });
    }

    // Backup major collections with safety limits to avoid quota exhaustion on large tables
    const collections = ['users', 'batches', 'questions', 'subjectiveExams', 'examAttempts', 'integrityScores'];
    const limitMap: { [key: string]: number } = {
      users: 500,
      batches: 500,
      questions: 1000,
      subjectiveExams: 500,
      examAttempts: 500,
      integrityScores: 500
    };
    const backupData: { [key: string]: any[] } = {};

    const snaps = await Promise.all(
      collections.map(col => {
        const limit = limitMap[col] || 500;
        return adminDb.collection(col).limit(limit).get();
      })
    );

    collections.forEach((col, idx) => {
      backupData[col] = snaps[idx].docs.map(doc => ({ id: doc.id, ...doc.data() }));
    });

    return NextResponse.json({ success: true, backup: backupData });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// POST restore / database utilities
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();
    const { action, backupPayload, utilityType } = body;

    // Action A: Restore database from local JSON stream backup
    if (action === 'restore') {
      if (!backupPayload || typeof backupPayload !== 'object') {
        return NextResponse.json({ error: 'Missing backup payload' }, { status: 400 });
      }

      // Restores collections sequentially in batch commits
      for (const colName of Object.keys(backupPayload)) {
        const docs = backupPayload[colName];
        if (!Array.isArray(docs)) continue;

        const writeBatch = new ChunkedBatch(adminDb);
        docs.forEach((docData: any) => {
          const docId = docData.id;
          if (!docId) return;
          const cleanData = { ...docData };
          delete cleanData.id;

          const ref = adminDb.collection(colName).doc(docId);
          writeBatch.set(ref, cleanData, { merge: true });
        });
        await writeBatch.commit();
      }
      return NextResponse.json({ success: true });
    }

    // Action B: Run specific database utility purges
    if (action === 'utility') {
      if (utilityType === 'resetFlags') {
        // Clear all used counter flags on questions
        const snap = await adminDb.collection('questions').get();
        const writeBatch = new ChunkedBatch(adminDb);
        snap.docs.forEach(doc => {
          writeBatch.update(doc.ref, {
            usedInClassroomTest: false,
            timesUsed: 0,
            usageHistory: []
          });
        });
        await writeBatch.commit();
        return NextResponse.json({ success: true });
      }

      if (utilityType === 'systemReset') {
        // Clear all collections except syllabus, users, templates, config, batches
        const protectedCollections = ['syllabus', 'users', 'templates', 'config', 'batches'];
        const collections = await adminDb.listCollections();
        
        for (const col of collections) {
          if (protectedCollections.includes(col.id)) continue;
          
          const snap = await col.get();
          if (snap.empty) continue;
          
          const writeBatch = new ChunkedBatch(adminDb);
          snap.docs.forEach(doc => {
            writeBatch.delete(doc.ref);
          });
          await writeBatch.commit();
        }
        return NextResponse.json({ success: true });
      }

      if (utilityType === 'resetProtected') {
        const { selectedCollections } = body;
        if (!Array.isArray(selectedCollections) || selectedCollections.length === 0) {
          return NextResponse.json({ error: 'No collections selected' }, { status: 400 });
        }

        const protectedCollections = ['syllabus', 'users', 'templates', 'config', 'batches'];
        for (const colName of selectedCollections) {
          if (!protectedCollections.includes(colName)) continue;

          const colRef = adminDb.collection(colName);
          const snap = await colRef.get();
          if (snap.empty) continue;

          const writeBatch = new ChunkedBatch(adminDb);
          snap.docs.forEach(doc => {
            writeBatch.delete(doc.ref);
          });
          await writeBatch.commit();
        }
        return NextResponse.json({ success: true });
      }

      if (utilityType === 'purgeOrphans') {
        // Delete any questions not mapped to an active syllabus
        const [questionsSnap, syllabusSnap] = await Promise.all([
          adminDb.collection('questions').get(),
          adminDb.collection('syllabus').get()
        ]);

        const activeSubjectCodes = new Set(syllabusSnap.docs.map(doc => doc.data().subjectCode).filter(Boolean));
        const writeBatch = new ChunkedBatch(adminDb);
        let count = 0;

        questionsSnap.docs.forEach(doc => {
          const q = doc.data();
          // If question subject code doesn't map to any active syllabus, purge it
          if (q.subjectCode && !activeSubjectCodes.has(q.subjectCode)) {
            writeBatch.delete(doc.ref);
            count++;
          }
        });

        await writeBatch.commit();
        return NextResponse.json({ success: true, count });
      }
    }

    return NextResponse.json({ error: 'Invalid action parameter' }, { status: 400 });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
