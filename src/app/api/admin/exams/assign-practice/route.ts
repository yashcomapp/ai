import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { FieldValue } from 'firebase-admin/firestore';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { isTopicPurelyQualitative } from '@/lib/curriculumGuard';

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

    // 3. Look up student user documents to get their UID and user-facing name (Rule 2B/2D)
    const userDocsSnap = await adminDb.collection('users')
      .where('studentCode', 'in', studentCodes.slice(0, 30))
      .get();

    const studentMap = new Map<string, { uid: string; name: string }>();
    userDocsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.role === 'student' && data.studentCode) {
        studentMap.set(data.studentCode, {
          uid: doc.id,
          name: data.name || data.studentCode
        });
      }
    });

    const now = new Date();
    const batch = adminDb.batch();
    let assignedCount = 0;

    for (const sCode of studentCodes) {
      const studentInfo = studentMap.get(sCode) || { uid: '', name: sCode };
      const docId = `${sCode}_${topicCode}`;
      const docRef = adminDb.collection('assignedPractices').doc(docId);

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
        setsCount: cleanSetsCount,
        setsCompleted: 0,
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
