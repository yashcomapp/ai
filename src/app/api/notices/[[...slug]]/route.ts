import { NextRequest, NextResponse } from 'next/server';
import { GET as getNotices } from '../handlers/notices';
import { POST as postSeen } from '../handlers/seen';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getNotices(req);
      default:
        return NextResponse.json({ message: `Unknown notice GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Notices Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'seen':
        return await postSeen(req);
      default:
        return NextResponse.json({ message: `Unknown notice POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Notices Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
