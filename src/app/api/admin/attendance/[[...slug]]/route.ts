import { NextRequest, NextResponse } from 'next/server';
import { GET as getRoster, POST as postRoster } from '../handlers/roster';
import { GET as getLeaves, POST as postLeaves } from '../handlers/leaves';
import { GET as getParentSync, POST as postParentSync } from '../handlers/parentSync';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getRoster(req);
      case 'leaves':
        return await getLeaves(req);
      case 'parent-sync':
        return await getParentSync(req);
      default:
        return NextResponse.json({ message: `Unknown attendance GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Attendance Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postRoster(req);
      case 'leaves':
        return await postLeaves(req);
      case 'parent-sync':
        return await postParentSync(req);
      default:
        return NextResponse.json({ message: `Unknown attendance POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Attendance Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
