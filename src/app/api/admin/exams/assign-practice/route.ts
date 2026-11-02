import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { FieldValue } from 'firebase-admin/firestore';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { isTopicPurelyQualitative } from '@/lib/curriculumGuard';
import { invalidateCache } from '@/lib/firebase/cache';

export const dynamic = 'force-dynamic';

/**
 * POST /api/admin/exams/assign-practice
 * 
 * Assigns targeted practice sets for a specific topic to selected students in a batch.
 * Enables the teacher to:
 * 1. Target students based on performance (Needs Attention, Practicing, or Custom selection).
 * 2. Assign more practice beyond the standard self-serve 2-set quota.
 * 3. Choose to focus on numerical calculation questions (ONE type) in science/math chapters.
 */
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const {
      batchId,
      topicCode,
      studentCodes,
      setsCount = 2,
      numericalFocus = false,
      note = '',
      dueDate = null
    } = body;

    if (!batchId || !topicCode || !Array.isArray(studentCodes) || studentCodes.length === 0) {
      return NextResponse.json({
        message: 'Missing required parameters (batchId, topicCode, studentCodes).'
      }, { status: 400 });
    }

    const cleanSetsCount = Math.max(1, Math.min(4, Number(setsCount) || 2));

    // 1. Fetch Topic details
    let topicName = topicCode;
    let chapterName = '';
    let subjectName = '';
    let className = '';

    try {
      const sSnap = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
      if (sSnap.exists) {
        const sd = sSnap.data()!;
        topicName = sd.topicName || sd.title || topicName;
        chapterName = sd.chapterName || chapterName;
        subjectName = sd.subjectName || sd.subject || subjectName;
        className = sd.class || className;
      }
    } catch (e) {
      console.warn('Could not read syllabusTopicIndex for topicCode:', topicCode);
    }

    // Safety: Verify if numericalFocus is valid for this topic
    const hasNumericals = !isTopicPurelyQualitative(topicCode, chapterName, subjectName);
    const finalNumericalFocus = Boolean(numericalFocus && hasNumericals);

    // 2. Fetch Batch details
    let batchName = batchId;
    try {
      const bSnap = await adminDb.collection('batches').doc(batchId).get();
      if (bSnap.exists) {
        batchName = bSnap.data()?.name || batchName;
      }
    } catch (e) {
      // silent fallback
    }

    // 3. Look up student user documents in chunks of 30 (Rule 2B/2D)
    // and verify they are active students belonging to this batch
    const codeChunks: string[][] = [];
    for (let i = 0; i < studentCodes.length; i += 30) {
      codeChunks.push(studentCodes.slice(i, i + 30));
    }

    const userDocsSnaps = await Promise.all(
      codeChunks.map(chunk =>
        adminDb.collection('users')
          .where('studentCode', 'in', chunk)
          .select('studentCode', 'name', 'role', 'batchIds', 'batchId', 'status')
          .get()
      )
    );

    const studentMap = new Map<string, { uid: string; name: string }>();
    userDocsSnaps.forEach(snap => {
      snap.docs.forEach(doc => {
        const data = doc.data();
        if (data.role === 'student' && data.studentCode && data.status !== 'inactive') {
          const bIds = data.batchIds || [data.batchId].filter(Boolean);
          if (bIds.includes(batchId)) {
            studentMap.set(data.studentCode, {
              uid: doc.id,
              name: data.name || data.studentCode
            });
          }
        }
      });
    });

    const validStudentCodes = studentCodes.filter(c => studentMap.has(c));
    if (validStudentCodes.length === 0) {
      return NextResponse.json({
        message: 'No active students from this batch matched the provided student codes.'
      }, { status: 400 });
    }

    // 4. Batch read existing assignedPractices documents to preserve progress
    const docRefs = validStudentCodes.map(sCode =>
      adminDb.collection('assignedPractices').doc(`${sCode}_${topicCode}`)
    );
    const existingSnaps = await adminDb.getAll(...docRefs);
    const existingMap = new Map<string, any>();
    existingSnaps.forEach(snap => {
      if (snap.exists) {
        existingMap.set(snap.id, snap.data());
      }
    });

    const now = new Date();
    const batch = adminDb.batch();
    let assignedCount = 0;

    for (const sCode of validStudentCodes) {
      const studentInfo = studentMap.get(sCode)!;
      const docId = `${sCode}_${topicCode}`;
      const docRef = adminDb.collection('assignedPractices').doc(docId);
      const existingData = existingMap.get(docId);

      const existingCompleted = existingData ? (Number(existingData.setsCompleted) || 0) : 0;
      // Add new sets on top of existing completed sets to never wipe student progress
      const targetSetsCount = existingCompleted + cleanSetsCount;

      batch.set(docRef, {
        studentCode: sCode,
        studentName: studentInfo.name,
        batchId,
        batchName,
        topicCode,
        topicName,
        chapterName,
        subject: subjectName,
        className,
        setsCount: targetSetsCount,
        setsCompleted: existingCompleted,
        numericalFocus: finalNumericalFocus,
        note: String(note || '').trim(),
        dueDate: dueDate || null,
        status: 'pending',
        assignedBy: adminUser.userData?.email || adminUser.decodedToken?.email || 'admin',
        assignedAt: FieldValue.serverTimestamp(),
        updatedAt: FieldValue.serverTimestamp()
      }, { merge: true });

      // Create an in-app notification for the student (Rule 2U: lightweight metadata only)
      if (studentInfo.uid) {
        const notifRef = adminDb.collection('notifications').doc();
        batch.set(notifRef, {
          userId: studentInfo.uid,
          studentCode: sCode,
          title: `🎯 Teacher Assigned Practice: ${topicName}`,
          message: `Your teacher assigned ${cleanSetsCount} practice set(s) on ${topicName}${finalNumericalFocus ? ' with focus on Numerical Calculations' : ''}.${note ? ` Note: "${note}"` : ''}`,
          type: 'practice_assignment',
          topicCode,
          numericalFocus: finalNumericalFocus,
          link: `/student/topic?topicCode=${encodeURIComponent(topicCode)}&category=needsAttention${finalNumericalFocus ? '&numericalFocus=true' : ''}`,
          read: false,
          createdAt: FieldValue.serverTimestamp()
        });
      }

      assignedCount++;
    }

    await batch.commit();

    // Invalidate cached coverage for this batch so next view reflects new status
    invalidateCache(`topic-coverage_${batchId}`);

    return NextResponse.json({
      success: true,
      message: `Successfully assigned ${cleanSetsCount} practice set(s) on "${topicName}" to ${assignedCount} student(s).`,
      assignedCount,
      topicCode,
      topicName,
      numericalFocus: finalNumericalFocus
    });

  } catch (error: any) {
    console.error('Error in POST /api/admin/exams/assign-practice:', error);
    return NextResponse.json({
      message: error.message || 'Failed to assign practice.'
    }, { status: 500 });
  }
}
