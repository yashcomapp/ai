import { NextRequest, NextResponse } from 'next/server';
import { GET as getDashboard } from '../handlers/dashboard';
import { GET as getNotificationHistory } from '../handlers/notificationHistory';
import { GET as getReview, POST as postReview } from '../handlers/review';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'dashboard':
        return await getDashboard(req);
      case 'notification-history':
        return await getNotificationHistory(req);
      case 'review':
        return await getReview(req);
      default:
        return NextResponse.json({ message: `Unknown parent GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Parent Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'review':
        return await postReview(req);
      default:
        return NextResponse.json({ message: `Unknown parent POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Parent Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
