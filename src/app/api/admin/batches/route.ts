import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
export async function GET(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    
    // Fetch all batches
    const batchesSnap = await adminDb.collection('batches')
      .orderBy('createdAt', 'desc')
      .get();
    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
    
    // Fetch all students (names, emails, batchIds, feeStatus, rollNumber)
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .get();
    const students = studentsSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || '',
      email: doc.data().email || '',
      studentCode: doc.data().studentCode || '',
      rollNumber: doc.data().rollNumber || '',
      feeStatus: doc.data().feeStatus || 'pending',
      batchIds: doc.data().batchIds || []
    }));

    return NextResponse.json({ batches, students });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// POST create, edit, or map student to batch
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();
    const { action, batchId, batchData, studentId, studentEmail, rollNumber, feeStatus } = body;
    
    if (action === 'saveBatch') {
      // Create or Update Batch
      const data = { ...batchData };
      data.updatedAt = new Date();
      
      if (batchId) {
        // Edit
        await adminDb.collection('batches').doc(batchId).update(data);
      } else {
        // Create
        data.createdAt = new Date();
        await adminDb.collection('batches').add(data);
      }
      return NextResponse.json({ success: true });
    }
    
    if (action === 'addStudent') {
      // Add student to batch by email
      if (!batchId || !studentEmail) {
        return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
      }
      
      const userSnap = await adminDb.collection('users')
        .where('email', '==', studentEmail.toLowerCase())
        .get();
        
      if (userSnap.empty) {
        return NextResponse.json({ error: 'No student found matching this email address' }, { status: 404 });
      }
      
      const studentDoc = userSnap.docs[0];
      const studentData = studentDoc.data();
      const currentBatches = studentData.batchIds || [];
      
      if (currentBatches.includes(batchId)) {
        return NextResponse.json({ error: 'Student is already mapped to this batch' }, { status: 400 });
      }
      
      await studentDoc.ref.update({
        batchIds: [...currentBatches, batchId],
        updatedAt: new Date()
      });
      
      return NextResponse.json({ success: true });
    }
    
    if (action === 'removeStudent') {
      // Remove student from batch
      if (!batchId || !studentId) {
        return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
      }
      
      const studentRef = adminDb.collection('users').doc(studentId);
      const studentDoc = await studentRef.get();
      if (!studentDoc.exists) {
        return NextResponse.json({ error: 'Student not found' }, { status: 404 });
      }
      
      const currentBatches = studentDoc.data()?.batchIds || [];
      await studentRef.update({
        batchIds: currentBatches.filter((id: string) => id !== batchId),
        updatedAt: new Date()
      });
      
      return NextResponse.json({ success: true });
    }
    
    if (action === 'updateRollAndFee') {
      // Update permanent roll and fee status
      if (!studentId) {
        return NextResponse.json({ error: 'Missing student ID' }, { status: 400 });
      }
      
      await adminDb.collection('users').doc(studentId).update({
        rollNumber: rollNumber || '',
        studentCode: rollNumber || '', // Keep studentCode synced as rollNumber
        feeStatus: feeStatus || 'pending',
        updatedAt: new Date()
      });
      
      return NextResponse.json({ success: true });
    }

    return NextResponse.json({ error: 'Invalid action parameter' }, { status: 400 });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

// DELETE a batch
export async function DELETE(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const url = new URL(request.url);
    const batchId = url.searchParams.get('batchId');
    
    if (!batchId) {
      return NextResponse.json({ error: 'Missing batch ID parameter' }, { status: 400 });
    }
    
    // Delete the batch doc
    await adminDb.collection('batches').doc(batchId).delete();
    
    // Optional: unlink this batch ID from all mapped student docs
    const studentsSnap = await adminDb.collection('users')
      .where('role', '==', 'student')
      .get();
      
    const writeBatch = new ChunkedBatch(adminDb);
    studentsSnap.docs.forEach(doc => {
      const batchIds = doc.data().batchIds || [];
      if (batchIds.includes(batchId)) {
        writeBatch.update(doc.ref, {
          batchIds: batchIds.filter((id: string) => id !== batchId),
          updatedAt: new Date()
        });
      }
    });
    await writeBatch.commit();
    
    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error(err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
