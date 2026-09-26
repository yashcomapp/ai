import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { getDateKeyIST } from '@/lib/dateUtils';
import { FaultService } from '@/services/fault.service';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const dateKey = searchParams.get('date') || getDateKeyIST();
    const batchId = searchParams.get('batchId') || 'all';

    const matrix = await FaultService.getBatchMatrix(dateKey, batchId);

    return NextResponse.json({
      success: true,
      ...matrix
    });
  } catch (error: any) {
    console.error('API admin get fault matrix error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin access required.' }, { status: 403 });
    }

    const body = await req.json();
    const { date, studentCode, faults, notes, bulk } = body;
    const recordedBy = admin.decodedToken?.email || 'Admin';

    if (Array.isArray(bulk) && bulk.length > 0) {
      for (const entry of bulk) {
        if (entry.studentCode && entry.date) {
          await FaultService.saveStudentFaults({
            date: entry.date,
            studentCode: entry.studentCode,
            faults: entry.faults || {},
            notes: entry.notes || {},
            recordedBy
          });
        }
      }
      return NextResponse.json({ success: true, message: `Successfully saved fault register for ${bulk.length} students.` });
    }

    if (!studentCode || !date) {
      return NextResponse.json({ message: 'Missing studentCode or date parameter.' }, { status: 400 });
    }

    await FaultService.saveStudentFaults({
      date,
      studentCode,
      faults: faults || {},
      notes: notes || {},
      recordedBy
    });

    return NextResponse.json({
      success: true,
      message: 'Student fault record saved successfully.'
    });
  } catch (error: any) {
    console.error('API admin save fault record error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
