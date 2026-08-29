import { NextRequest, NextResponse } from 'next/server';
import { GET as getNotices, POST as postNotices, DELETE as deleteNotices } from '../handlers/notices';
import { GET as getLogs, POST as postLogs } from '../handlers/logs';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getNotices(req);
      case 'logs':
        return await getLogs(req);
      default:
        return NextResponse.json({ message: `Unknown admin notice GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Notices Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postNotices(req);
      case 'logs':
        return await postLogs(req);
      default:
        return NextResponse.json({ message: `Unknown admin notice POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Notices Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await deleteNotices(req);
      default:
        return NextResponse.json({ message: `Unknown admin notice DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Notices Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
