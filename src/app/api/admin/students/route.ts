import { NextResponse } from 'next/server';
import { adminDb, adminAuth } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    
    const { searchParams } = new URL(request.url);
    const studentCode = searchParams.get('studentCode');
    
    if (studentCode) {
      const masterySnap = await adminDb.collection('studentTopicMastery')
        .where('studentCode', '==', studentCode)
        .get();
        
      const alerts: any[] = [];
      masterySnap.docs.forEach(doc => {
        const data = doc.data();
        if (data.honestyAlerts && Array.isArray(data.honestyAlerts) && data.honestyAlerts.length > 0) {
          alerts.push({
            topicCode: data.topicCode || '',
            topicName: data.topicName || '',
            chapterName: data.chapterName || '',
            alerts: data.honestyAlerts
          });
        }
      });
      return NextResponse.json({ alerts });
    }

    // Fetch all students and batches in parallel
    const [snapshot, batchesSnapshot] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      adminDb.collection('batches')
        .get()
    ]);
      
    const students = snapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
    
    const batches = batchesSnapshot.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    return NextResponse.json({ students, batches });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// POST updates to student details (Status toggles / edits)
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();
    const { studentId, updateData } = body;
    
    if (!studentId || !updateData) {
      return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
    }
    
    // Exclude protected system fields from manual updates
    const cleanUpdates = { ...updateData };
    delete cleanUpdates.id;
    delete cleanUpdates.email;
    delete cleanUpdates.role;
    cleanUpdates.updatedAt = new Date();

    await adminDb.collection('users').doc(studentId).update(cleanUpdates);
    
    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// DELETE student and cascade delete all related database records
export async function DELETE(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const url = new URL(request.url);
    const studentId = url.searchParams.get('studentId');
    const studentCode = url.searchParams.get('studentCode');
    
    if (!studentId) {
      return NextResponse.json({ error: 'Missing student ID parameter' }, { status: 400 });
    }
    
    const batch = new ChunkedBatch(adminDb);
    
    // 1. Delete user doc
    batch.delete(adminDb.collection('users').doc(studentId));
    
    // 2. Delete studentTopicMastery docs if studentCode is available
    if (studentCode) {

      const topicMasterySnap = await adminDb.collection('studentTopicMastery')
        .where('studentCode', '==', studentCode)
        .get();
      topicMasterySnap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });
      
      // 3. Delete examAttempts / reviews matching studentCode
      const attemptsSnap = await adminDb.collection('examAttempts')
        .where('studentCode', '==', studentCode)
        .get();
      attemptsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });

      const reviewsSnap = await adminDb.collection('reviews')
        .where('studentCode', '==', studentCode)
        .get();
      reviewsSnap.docs.forEach(doc => {
        batch.delete(doc.ref);
      });
    }
    
    await batch.commit();
    
    // 4. Delete user record in Firebase Auth safely
    try {
      await adminAuth.deleteUser(studentId);
    } catch (authErr: any) {
      console.warn(`Auth user delete failed or user does not exist in Auth: ${authErr.message}`);
    }
    
    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
