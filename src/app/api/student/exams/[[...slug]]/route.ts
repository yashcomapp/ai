import { NextRequest, NextResponse } from 'next/server';
import { GET as getExams, POST as postExams } from '../handlers/exams';
import { GET as getSubjective, POST as postSubjective } from '../handlers/subjective';
import { POST as postPeerReview } from '../handlers/peerReview';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getExams(req);
      case 'subjective':
        return await getSubjective(req);
      default:
        return NextResponse.json({ message: `Unknown student exam GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Exams Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postExams(req);
      case 'subjective':
        return await postSubjective(req);
      case 'subjective/peer-review':
        return await postPeerReview(req);
      default:
        return NextResponse.json({ message: `Unknown student exam POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Exams Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
