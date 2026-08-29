import { NextRequest, NextResponse } from 'next/server';
import { GET as getTimeLog, POST as postTimeLog } from '../handlers/timeLog';
import { POST as postClientStorageSync } from '../handlers/clientStorageSync';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'time-log':
        return await getTimeLog(req);
      default:
        return NextResponse.json({ message: `Unknown user GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API User Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'time-log':
        return await postTimeLog(req);
      case 'client-storage-sync':
        return await postClientStorageSync(req);
      default:
        return NextResponse.json({ message: `Unknown user POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API User Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
