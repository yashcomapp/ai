import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { encrypt } from '@/lib/encryption';
import { checkDistributedRateLimit } from '@/lib/rateLimit';
import { getBirthdatePassword } from '@/lib/dateUtils';
import { validateName, validateEmail, validateMobile, validatePassword } from '@/lib/validation';

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

    const sNameVal = validateName(studentName);
    if (!sNameVal.valid) {
      return NextResponse.json({ message: sNameVal.error }, { status: 400 });
    }

    const sEmailVal = validateEmail(studentEmail);
    if (!sEmailVal.valid) {
      return NextResponse.json({ message: sEmailVal.error }, { status: 400 });
    }

    const sMobileVal = validateMobile(studentMobile);
    if (!sMobileVal.valid) {
      return NextResponse.json({ message: sMobileVal.error }, { status: 400 });
    }

    const pNameVal = validateName(parentName, false);
    if (!pNameVal.valid) {
      return NextResponse.json({ message: pNameVal.error }, { status: 400 });
    }

    const pMobileVal = validateMobile(parentMobile);
    if (!pMobileVal.valid) {
      return NextResponse.json({ message: pMobileVal.error }, { status: 400 });
    }

    const pEmailVal = validateEmail(parentEmail);
    if (!pEmailVal.valid) {
      return NextResponse.json({ message: pEmailVal.error }, { status: 400 });
    }

    const pwdVal = validatePassword(password);
    if (!pwdVal.valid) {
      return NextResponse.json({ message: pwdVal.error }, { status: 400 });
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
