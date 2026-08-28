import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { encrypt } from '@/lib/encryption';
const NAME_RE = /^[a-zA-Z\s.]+$/;
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MOBILE_RE = /^[6789]\d{9}$/;
const PASSWORD_RE = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

const ipLimits = new Map<string, number[]>();

export async function POST(req: NextRequest) {
  try {
    let rawIp = req.headers.get('x-forwarded-for') || req.headers.get('x-real-ip') || 'unknown-ip';
    if (rawIp.includes(',')) {
      rawIp = rawIp.split(',')[0].trim();
    }
    const userAgent = req.headers.get('user-agent') || 'unknown-ua';
    const rateLimitKey = `${rawIp}:${userAgent}`;
    const now = Date.now();

    const timestamps = ipLimits.get(rateLimitKey) || [];
    const validTimestamps = timestamps.filter(t => now - t < 60000);
    if (validTimestamps.length >= 5) {
      return NextResponse.json({ message: 'Too many registration requests. Please try again in a minute.' }, { status: 429 });
    }
    validTimestamps.push(now);
    ipLimits.set(rateLimitKey, validTimestamps);

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
    const getBirthdatePassword = (dobStr: string): string => {
      if (!dobStr) return '010100';
      const parts = dobStr.split('-');
      if (parts.length === 3) {
        const year = parts[0];
        const month = parts[1];
        const day = parts[2];
        const yy = year.substring(year.length - 2);
        return `${day.padStart(2, '0')}${month.padStart(2, '0')}${yy}`;
      }
      const d = new Date(dobStr);
      if (!isNaN(d.getTime())) {
        const day = String(d.getDate()).padStart(2, '0');
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const yy = String(d.getFullYear()).slice(-2);
        return `${day}${month}${yy}`;
      }
      return '010100';
    };
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
