import { NextRequest, NextResponse } from 'next/server';
import { GET as getAttendance } from '../handlers/attendance';
import { GET as getDeclare, POST as postDeclare } from '../handlers/declare';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getAttendance(req);
      case 'declare':
        return await getDeclare(req);
      default:
        return NextResponse.json({ message: `Unknown student attendance GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Attendance Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'declare':
        return await postDeclare(req);
      default:
        return NextResponse.json({ message: `Unknown student attendance POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Attendance Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
