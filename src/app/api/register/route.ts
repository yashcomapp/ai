import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { encrypt } from '@/lib/encryption';
import { checkDistributedRateLimit } from '@/lib/rateLimit';
import { getBirthdatePassword } from '@/lib/dateUtils';
import { NAME_RE, EMAIL_RE, MOBILE_RE, PASSWORD_RE } from '@/lib/validation';

export async function POST(req: NextRequest) {
  try {
    let rawIp = req.headers.get('x-forwarded-for') || req.headers.get('x-real-ip') || 'unknown-ip';
    if (rawIp.includes(',')) {
      rawIp = rawIp.split(',')[0].trim();
    }
    const rateLimitKey = `register:${rawIp}`;

    const { allowed } = await checkDistributedRateLimit({
      key: rateLimitKey,
      limit: 5,
      windowMs: 60000
    });

    if (!allowed) {
      return NextResponse.json({ message: 'Too many registration requests. Please try again in a minute.' }, { status: 429 });
    }

    const data = await req.json();
    const {
      studentName, studentEmail, studentMobile, dob, gender, bloodGroup, address,
      parentName, parentRelation, parentMobile, parentEmail, parentOccupation,
      batchId, password
    } = data;

    // Server-side validation
    if (!studentName || !studentEmail || !studentMobile || !dob || !gender || !bloodGroup || !address ||
        !parentName || !parentMobile || !parentEmail || !batchId || !password) {
      return NextResponse.json({ message: 'All required fields must be completed.' }, { status: 400 });
    }

    if (!NAME_RE.test(studentName.trim()) || studentName.trim().split(/\s+/).length < 2) {
      return NextResponse.json({ message: 'Invalid student name. Provide first and last name.' }, { status: 400 });
    }

    if (!EMAIL_RE.test(studentEmail.trim())) {
      return NextResponse.json({ message: 'Invalid student email format.' }, { status: 400 });
    }

    if (!MOBILE_RE.test(studentMobile.trim()) || !MOBILE_RE.test(parentMobile.trim())) {
      return NextResponse.json({ message: 'Mobile numbers must be valid 10-digit Indian numbers.' }, { status: 400 });
    }

    // Derive password from student's date of birth in DDMMYY format to satisfy Firebase 6-character minimum
    const dobPassword = getBirthdatePassword(dob);

    // Get batch information to formulate tempId
    const batchDoc = await adminDb.collection('batches').doc(batchId).get();
    if (!batchDoc.exists) {
      return NextResponse.json({ message: 'Selected batch does not exist.' }, { status: 400 });
    }

    const batchName = batchDoc.data()?.name || '';
    const gradeMatch = batchName.match(/\d+/);
    const grade = gradeMatch ? gradeMatch[0] : 'X';
    const tempId = `TEMP-${grade}-${Math.floor(100000 + Math.random() * 900000)}`;

    const isAutonomous = data.autonomous !== undefined ? Boolean(data.autonomous) : true;

    const registration = {
      studentName: studentName.trim(),
      studentEmail: studentEmail.trim().toLowerCase(),
      studentMobile: studentMobile.trim(),
      dob,
      gender,
      bloodGroup,
      address: address.trim(),
      parentName: parentName.trim(),
      parentRelation: parentRelation || '',
      parentMobile: parentMobile.trim(),
      parentEmail: parentEmail.trim().toLowerCase(),
      parentOccupation: parentOccupation?.trim() || '',
      batchId,
      batchName,
      tempId,
      autonomous: isAutonomous,
      password: encrypt(dobPassword),
      status: 'pending',
      createdAt: admin.firestore.FieldValue.serverTimestamp()
    };

    // Save registration document
    const res = await adminDb.collection('registrations').add(registration);

    return NextResponse.json({ success: true, id: res.id, tempId });
  } catch (error: any) {
    console.error('Registration API error:', error);
    return NextResponse.json({ message: error.message || 'Registration failed' }, { status: 500 });
  }
}
