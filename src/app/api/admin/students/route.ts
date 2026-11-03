import { NextResponse } from 'next/server';
import { adminDb, adminAuth } from '@/lib/firebase/admin';
import { FieldValue } from 'firebase-admin/firestore';
import { verifyRole, invalidateUserCache, syncUserCustomClaims, invalidateParentDeactCache } from '@/lib/auth';
import { ChunkedBatch } from '@/lib/firebase/batch';
import { getFromCache, setInCache, invalidateCache, getCachedBatches } from '@/lib/firebase/cache';
import { isDemoUser } from '@/lib/studentDb';
import { ExamReviewService } from '@/services/examReview.service';
import { assertCanonicalStudentCode } from '@/lib/canonicalValidation';

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

    const cacheKey = 'admin_students_list';
    const cached = getFromCache<any>(cacheKey);
    if (cached) {
      return NextResponse.json(cached, {
        headers: {
          'Cache-Control': 'private, max-age=15, stale-while-revalidate=30'
        }
      });
    }

    // Fetch all students and batches in parallel
    const [snapshot, batchesSnapshot] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      getCachedBatches()
    ]);
      
    const students = (snapshot.docs as any[])
      .map((doc: any) => ({
        id: doc.id,
        ...doc.data()
      }))
      .filter((s: any) => !isDemoUser(s));
    
    const batches = (batchesSnapshot.docs as any[]).map((doc: any) => ({
      id: doc.id,
      name: (typeof doc.data === 'function' ? doc.data().name : doc.name) || doc.id
    }));

    const responseData = { students, batches };
    setInCache(cacheKey, responseData, 30000); // 30s in-memory cache

    return NextResponse.json(responseData, {
      headers: {
        'Cache-Control': 'private, max-age=15, stale-while-revalidate=30'
      }
    });
  } catch (err: any) {
    console.error(err);
    const status = err.message?.includes('[CANONICAL BARRIER VIOLATION]') ? 400 : 500;
    return NextResponse.json({ error: err.message }, { status });
  }
}

// POST updates to student details (Status toggles / edits)
export async function POST(request: Request) {
  try {
    const admin = await verifyRole(request, 'admin');
    if (!admin) return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    const body = await request.json();

    if (body.action === 'sweep_autonomous') {
      if (body.studentCode) {
        assertCanonicalStudentCode(body.studentCode);
      }
      const result = await ExamReviewService.sweepAutonomousReviews(body.studentCode);
      return NextResponse.json(result);
    }

    const { studentId, updateData } = body;
    
    if (!studentId || !updateData) {
      return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
    }
    
    // Canonical Ingress Barrier (Rule 2.R & 2.B)
    if (updateData.studentCode) {
      assertCanonicalStudentCode(updateData.studentCode);
    }

    // Exclude protected system fields from manual updates
    const cleanUpdates = { ...updateData };
    delete cleanUpdates.id;
    delete cleanUpdates.email;
    delete cleanUpdates.role;
    cleanUpdates.updatedAt = new Date();

    // Harmonize Student Mode & Autonomous Flag (Rule: Mode 2 & Mode 3 have parent login disabled)
    if (cleanUpdates.studentMode !== undefined) {
      if (cleanUpdates.studentMode === 'autonomous' || cleanUpdates.studentMode === 'limited') {
        cleanUpdates.autonomous = true;
      } else {
        cleanUpdates.autonomous = false;
        cleanUpdates.studentMode = 'regular';
      }
    } else if (cleanUpdates.autonomous !== undefined) {
      cleanUpdates.studentMode = cleanUpdates.autonomous ? 'autonomous' : 'regular';
    }

    const studentDocRef = adminDb.collection('users').doc(studentId);
    const studentSnap = await studentDocRef.get();
    const studentData = studentSnap.exists ? studentSnap.data() || {} : {};
    const studentCode = studentData.studentCode;
    const parentEmail = (cleanUpdates.parentEmail || studentData.parentEmail || '').trim().toLowerCase();

    await studentDocRef.update(cleanUpdates);

    // Keep custom claims in sync. Strictly revoke tokens ONLY on account deactivation or role changes to prevent signing out active students mid-exam.
    const shouldRevoke = cleanUpdates.status === 'inactive' || (cleanUpdates.role !== undefined && cleanUpdates.role !== studentData.role);
    await syncUserCustomClaims(studentId, {
      ...studentData,
      ...cleanUpdates
    }, shouldRevoke);

    // 1. If switched to Autonomous, auto-approve any legacy pending parent reviews for this student
    if (cleanUpdates.autonomous === true && studentCode) {
      try {
        await ExamReviewService.sweepAutonomousReviews(studentCode);
      } catch (mErr) {
        console.warn('Could not auto-approve pending reviews on autonomous toggle:', mErr);
      }
    }

    // 2. Parent-Student Linking Lifecycle: Handle parent email re-assignment
    const oldParentEmail = (studentData.parentEmail || '').trim().toLowerCase();
    const newParentEmail = cleanUpdates.parentEmail !== undefined 
      ? (cleanUpdates.parentEmail || '').trim().toLowerCase() 
      : oldParentEmail;

    if (studentCode && oldParentEmail && oldParentEmail !== newParentEmail) {
      // Unlink student from old parent account
      const oldParentSnaps = await adminDb.collection('users')
        .where('role', '==', 'parent')
        .where('email', '==', oldParentEmail)
        .get()
        .catch(() => ({ docs: [] } as any));
      for (const oldDoc of oldParentSnaps.docs) {
        const oldData = oldDoc.data();
        const updates: any = {
          studentCodes: FieldValue.arrayRemove(studentCode)
        };
        if (oldData.studentCode === studentCode) {
          updates.studentCode = FieldValue.delete();
        }
        await oldDoc.ref.update(updates);
        invalidateUserCache(oldDoc.id);
      }
      invalidateParentDeactCache(oldParentEmail);
    }

    // 3. Synchronize linked parent accounts safely (handling multi-student siblings & autonomous status)
    if (cleanUpdates.parentEmail !== undefined || cleanUpdates.autonomous !== undefined || cleanUpdates.status !== undefined) {
      const parentUserDocs: any[] = [];
      const effectiveAutonomous = cleanUpdates.autonomous !== undefined ? cleanUpdates.autonomous : studentData.autonomous === true;

      if (studentCode) {
        const [snapByCode, snapByArray] = await Promise.all([
          adminDb.collection('users').where('role', '==', 'parent').where('studentCode', '==', studentCode).get(),
          adminDb.collection('users').where('role', '==', 'parent').where('studentCodes', 'array-contains', studentCode).get()
        ]);
        snapByCode.docs.forEach(d => {
          if (!parentUserDocs.some(existing => existing.id === d.id)) parentUserDocs.push(d);
        });
        snapByArray.docs.forEach(d => {
          if (!parentUserDocs.some(existing => existing.id === d.id)) parentUserDocs.push(d);
        });
      }

      if (newParentEmail) {
        const snapByEmail = await adminDb.collection('users').where('role', '==', 'parent').where('email', '==', newParentEmail).get();
        snapByEmail.docs.forEach(d => {
          if (!parentUserDocs.some(existing => existing.id === d.id)) parentUserDocs.push(d);
        });
      }

      for (const pDoc of parentUserDocs) {
        const pData = pDoc.data() || {};
        invalidateUserCache(pDoc.id);

        // If this parent does not match the new parent email, ensure studentCode and legacy studentCode are removed
        if (studentCode && newParentEmail && pData.email?.toLowerCase() !== newParentEmail) {
          const updates: any = {
            studentCodes: FieldValue.arrayRemove(studentCode)
          };
          if (pData.studentCode === studentCode) {
            updates.studentCode = FieldValue.delete();
          }
          await pDoc.ref.update(updates);
          continue;
        }

        // SSOT Linking Guarantee: Ensure studentCode is registered in parent's studentCodes array
        if (studentCode && pData.email?.toLowerCase() === newParentEmail) {
          const currentCodes = Array.isArray(pData.studentCodes)
            ? pData.studentCodes
            : (pData.studentCode ? [pData.studentCode] : []);
          if (!currentCodes.includes(studentCode)) {
            await pDoc.ref.update({
              studentCodes: FieldValue.arrayUnion(studentCode)
            });
          }
        }

        if (effectiveAutonomous) {
          // Check if parent has any other non-autonomous active child before deactivating
          let allCodes: string[] = [];
          if (Array.isArray(pData.studentCodes)) {
            allCodes = pData.studentCodes.filter(Boolean);
          } else if (pData.studentCode) {
            allCodes = [pData.studentCode];
          }

          let hasOtherRegularChild = false;
          if (allCodes.length > 1) {
            const otherCodes = allCodes.filter(c => c !== studentCode);
            if (otherCodes.length > 0) {
              const otherStudentsSnap = await adminDb.collection('users')
                .where('role', '==', 'student')
                .where('studentCode', 'in', otherCodes.slice(0, 30))
                .get();
              
              hasOtherRegularChild = otherStudentsSnap.docs.some(d => {
                const s = d.data();
                return s.status === 'active' && s.autonomous !== true;
              });
            }
          }

          if (!hasOtherRegularChild) {
            await pDoc.ref.update({
              status: 'inactive',
              deactivationReason: 'student_autonomous',
              updatedAt: new Date()
            });
            invalidateUserCache(pDoc.id);
            await syncUserCustomClaims(pDoc.id, { ...pData, status: 'inactive' }, true);
          }
        } else {
          // Reactivate parent if student is regular (non-autonomous) and active
          if (pData.status === 'inactive' || !pData.status) {
            await pDoc.ref.update({
              status: 'active',
              deactivationReason: null,
              updatedAt: new Date()
            });
            invalidateUserCache(pDoc.id);
            await syncUserCustomClaims(pDoc.id, { ...pData, status: 'active' }, false);
          }
        }
      }
      invalidateParentDeactCache(newParentEmail || undefined);
    }

    invalidateUserCache(studentId);
    invalidateCache('admin_students_list');
    
    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error(err);
    const status = err.message?.includes('[CANONICAL BARRIER VIOLATION]') ? 400 : 500;
    return NextResponse.json({ error: err.message }, { status });
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
      // 4. Clean up studentCode and studentCodes from any linked parent accounts
      const [parentSnapsByArray, parentSnapsByCode] = await Promise.all([
        adminDb.collection('users')
          .where('role', '==', 'parent')
          .where('studentCodes', 'array-contains', studentCode)
          .get()
          .catch(() => ({ docs: [] } as any)),
        adminDb.collection('users')
          .where('role', '==', 'parent')
          .where('studentCode', '==', studentCode)
          .get()
          .catch(() => ({ docs: [] } as any))
      ]);

      const seenParentDocIds = new Set<string>();
      [...parentSnapsByArray.docs, ...parentSnapsByCode.docs].forEach((pDoc: any) => {
        if (!seenParentDocIds.has(pDoc.id)) {
          seenParentDocIds.add(pDoc.id);
          const pData = pDoc.data();
          const updates: any = {
            studentCodes: FieldValue.arrayRemove(studentCode)
          };
          if (pData.studentCode === studentCode) {
            updates.studentCode = FieldValue.delete();
          }
          batch.update(pDoc.ref, updates);
        }
      });
    }
    
    await batch.commit();
    
    // 4. Delete user record in Firebase Auth safely
    try {
      await adminAuth.deleteUser(studentId);
    } catch (authErr: any) {
      console.warn(`Auth user delete failed or user does not exist in Auth: ${authErr.message}`);
    }
    
    invalidateCache('admin_students_list');

    return NextResponse.json({ success: true });
  } catch (err: any) {
    console.error(err);
    const status = err.message?.includes('[CANONICAL BARRIER VIOLATION]') ? 400 : 500;
    return NextResponse.json({ error: err.message }, { status });
  }
}
