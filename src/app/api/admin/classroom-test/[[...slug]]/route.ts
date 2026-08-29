import { NextRequest, NextResponse } from 'next/server';
import { GET as getClassroomTest, POST as postClassroomTest } from '../handlers/classroomTest';
import { GET as getWeeklySuite, POST as postWeeklySuite } from '../handlers/weeklySuite';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getClassroomTest(req);
      case 'weekly-suite':
        return await getWeeklySuite(req);
      default:
        return NextResponse.json({ message: `Unknown classroom-test GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Classroom Test Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postClassroomTest(req);
      case 'weekly-suite':
        return await postWeeklySuite(req);
      default:
        return NextResponse.json({ message: `Unknown classroom-test POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Classroom Test Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
