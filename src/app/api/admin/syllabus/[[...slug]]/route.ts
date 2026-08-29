import { NextRequest, NextResponse } from 'next/server';
import { GET as getSyllabus, POST as postSyllabus, DELETE as deleteSyllabus } from '../handlers/syllabus';
import { POST as postRebuild } from '../handlers/rebuild';
import { POST as postSwapTopics } from '../handlers/swapTopics';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getSyllabus(req);
      default:
        return NextResponse.json({ message: `Unknown syllabus GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Syllabus Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postSyllabus(req);
      case 'rebuild':
        return await postRebuild(req);
      case 'swap-topics':
        return await postSwapTopics(req);
      default:
        return NextResponse.json({ message: `Unknown syllabus POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Syllabus Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await deleteSyllabus(req);
      default:
        return NextResponse.json({ message: `Unknown syllabus DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Syllabus Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
