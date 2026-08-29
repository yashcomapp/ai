import { NextRequest, NextResponse } from 'next/server';
import { GET as getRooms, POST as postRooms } from '../handlers/rooms';
import { GET as getMessages, POST as postMessages, DELETE as deleteMessages } from '../handlers/messages';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getRooms(req);
      case 'messages':
        return await getMessages(req);
      default:
        return NextResponse.json({ message: `Unknown chat GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Chat Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postRooms(req);
      case 'messages':
        return await postMessages(req);
      default:
        return NextResponse.json({ message: `Unknown chat POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Chat Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'messages':
        return await deleteMessages(req);
      default:
        return NextResponse.json({ message: `Unknown chat DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Chat Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
