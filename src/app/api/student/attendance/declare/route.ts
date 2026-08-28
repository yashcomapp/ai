import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyAnyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    // 1. Authenticate user - support admin, student, and parent roles in a single pass
    const session = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!session) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 401 });
    }

    if (session.role === 'admin') {
      // Admin gets all declarations
      const snap = await adminDb.collection('attendanceDeclarations')
        .orderBy('createdAt', 'desc')
        .get();
      const declarations = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
      return NextResponse.json({ success: true, declarations });
    }

    let studentCodes: string[] = [];

    if (session.role === 'student') {
      const code = session.userData?.studentCode;
      if (code) studentCodes.push(code.toUpperCase());
    } else if (session.role === 'parent') {
      const parentData = session.userData;
      let parentCodes: string[] = [];
      if (Array.isArray(parentData?.studentCodes)) {
        parentCodes = parentData.studentCodes.filter(Boolean);
      } else if (parentData?.studentCode) {
        parentCodes = [parentData.studentCode];
      }

      const parentEmail = parentData?.email?.toLowerCase()?.trim();
      if (parentEmail) {
        const querySnap = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('parentEmail', '==', parentEmail)
          .get();
        querySnap.docs.forEach(doc => {
          const data = doc.data();
          if (data.studentCode && !parentCodes.includes(data.studentCode)) {
            parentCodes.push(data.studentCode);
          }
        });
      }
      studentCodes = parentCodes.map((c: string) => c.toUpperCase());
    }

    if (studentCodes.length === 0) {
      return NextResponse.json({ message: 'Unauthorized. Active student or parent profile required.' }, { status: 403 });
    }

    // Fetch declarations for these student codes
    const snap = await adminDb.collection('attendanceDeclarations')
      .where('studentCode', 'in', studentCodes)
      .get();

    const declarations = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }))
      .sort((a: any, b: any) => (b.createdAt || '').localeCompare(a.createdAt || ''));

    return NextResponse.json({ success: true, declarations });
  } catch (error: any) {
    console.error('API GET declarations error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    let studentCode = '';
    let role: 'student' | 'parent' = 'student';
    let studentName = 'Student';

    // 1. Authenticate user in a single pass
    const session = await verifyAnyRole(req, ['student', 'parent']);
    if (!session) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 401 });
    }

    if (session.role === 'student') {
      studentCode = session.userData?.studentCode || '';
      studentName = session.userData?.name || 'Student';
      role = 'student';
    } else if (session.role === 'parent') {
      role = 'parent';
      const bodyCopy = await req.clone().json().catch(() => ({}));
      const { searchParams } = new URL(req.url);
      const targetCode = (bodyCopy.studentCode || searchParams.get('studentCode'))?.trim().toUpperCase();

      const parentData = session.userData;
      let parentCodes: string[] = [];
      if (Array.isArray(parentData?.studentCodes)) {
        parentCodes = parentData.studentCodes.filter(Boolean);
      } else if (parentData?.studentCode) {
        parentCodes = [parentData.studentCode];
      }

      const parentEmail = parentData?.email?.toLowerCase()?.trim();
      if (parentEmail) {
        const querySnap = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('parentEmail', '==', parentEmail)
          .get();
        querySnap.docs.forEach(doc => {
          const data = doc.data();
          if (data.studentCode && !parentCodes.includes(data.studentCode)) {
            parentCodes.push(data.studentCode);
          }
        });
      }
      const parentCodesUpper = parentCodes.map((c: string) => c.toUpperCase());

      if (targetCode && parentCodesUpper.includes(targetCode)) {
        studentCode = targetCode;
      } else if (parentCodesUpper.length > 0) {
        studentCode = parentCodesUpper[0];
      }

      if (studentCode) {
        const studentQuery = await adminDb.collection('users')
          .where('role', '==', 'student')
          .where('studentCode', '==', studentCode)
          .limit(1)
          .get();
        if (!studentQuery.empty) {
          studentName = studentQuery.docs[0].data().name || 'Student';
        }
      }
    }

    if (!studentCode) {
      return NextResponse.json({ message: 'Unauthorized or missing student profile.' }, { status: 403 });
    }

    const body = await req.json();
    let { status, startDate, endDate, remarks } = body;

    if (!status || !['present', 'leave'].includes(status)) {
      return NextResponse.json({ error: 'Invalid status. Choose present or leave.' }, { status: 400 });
    }

    if (status === 'leave' && role !== 'parent') {
      return NextResponse.json({ error: 'Forbidden. Only parent accounts can declare excused leaves.' }, { status: 403 });
    }

    // Resolve today's date in IST YYYY-MM-DD
    const todayStr = getDateKeyIST();

    if (status === 'present') {
      // Present can only be marked for today
      startDate = todayStr;
      endDate = todayStr;
    } else {
      // Leaves must not be in the past
      if (!startDate || !endDate) {
        return NextResponse.json({ error: 'Start date and end date are required for leaves.' }, { status: 400 });
      }
      if (startDate < todayStr) {
        return NextResponse.json({ error: 'Leaves cannot be applied for past dates.' }, { status: 400 });
      }
      if (startDate > endDate) {
        return NextResponse.json({ error: 'Start date cannot be after end date.' }, { status: 400 });
      }
    }

    const declRef = adminDb.collection('attendanceDeclarations').doc();
    const newDeclaration = {
      declarationId: declRef.id,
      studentCode: studentCode.toUpperCase(),
      studentName,
      status, // "present" | "leave"
      startDate, // YYYY-MM-DD
      endDate,   // YYYY-MM-DD
      remarks: remarks || '',
      declaredBy: role,
      createdAt: new Date().toISOString()
    };

    await declRef.set(newDeclaration);

    // If it's a leave, register it in leaveApplications so daily check-ins pick it up
    if (status === 'leave') {
      const leaveRef = adminDb.collection('leaveApplications').doc();
      await leaveRef.set({
        applicationId: leaveRef.id,
        studentCode: studentCode.toUpperCase(),
        studentName,
        startDate,
        endDate,
        type: 'planned',
        remarks: remarks || `${role.toUpperCase()} leave declaration`,
        status: 'pending', // Leaves applied by parent must be pending approval
        declaredBy: role,
        createdAt: new Date().toISOString()
      });
    }

    return NextResponse.json({ success: true, declaration: newDeclaration });
  } catch (error: any) {
    console.error('API POST declarations error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  try {
    const session = await verifyAnyRole(req, ['admin', 'student', 'parent']);
    if (!session) {
      return NextResponse.json({ message: 'Unauthorized.' }, { status: 401 });
    }

    const { searchParams } = new URL(req.url);
    const declarationId = searchParams.get('id');
    if (!declarationId) {
      return NextResponse.json({ error: 'Missing declaration ID.' }, { status: 400 });
    }

    const docRef = adminDb.collection('attendanceDeclarations').doc(declarationId);
    const docSnap = await docRef.get();
    if (!docSnap.exists) {
      return NextResponse.json({ error: 'Declaration not found.' }, { status: 404 });
    }

    const declData = docSnap.data()!;
    const studentCode = declData.studentCode;

    // Check authorization for students/parents
    if (session.role === 'student') {
      const selfCode = session.userData?.studentCode || '';
      if (selfCode.toUpperCase() !== studentCode.toUpperCase()) {
        return NextResponse.json({ message: 'Forbidden.' }, { status: 403 });
      }
    } else if (session.role === 'parent') {
      const parentCodes = session.userData?.studentCodes || (session.userData?.studentCode ? [session.userData?.studentCode] : []);
      const parentCodesUpper = parentCodes.map((c: string) => c.toUpperCase());
      if (!parentCodesUpper.includes(studentCode.toUpperCase())) {
        return NextResponse.json({ message: 'Forbidden.' }, { status: 403 });
      }
    }

    // Delete corresponding leaveApplications documents
    const leaveAppsSnap = await adminDb.collection('leaveApplications')
      .where('studentCode', '==', studentCode.toUpperCase())
      .where('startDate', '==', declData.startDate)
      .where('endDate', '==', declData.endDate)
      .get();

    const batch = adminDb.batch();
    leaveAppsSnap.docs.forEach(doc => {
      batch.delete(doc.ref);
    });
    batch.delete(docRef);
    await batch.commit();

    return NextResponse.json({ success: true });
  } catch (error: any) {
    console.error('API DELETE declarations error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
