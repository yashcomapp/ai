import { NextRequest, NextResponse } from 'next/server';
import { GET as getExams, POST as postExams, DELETE as deleteExams } from '../handlers/exams';
import { GET as getGenerate, POST as postGenerate } from '../handlers/generate';
import { GET as getLottery, POST as postLottery } from '../handlers/lottery';
import { GET as getObjective, POST as postObjective } from '../handlers/objective';
import { GET as getSubjective, POST as postSubjective } from '../handlers/subjective';
import { POST as postBroadcastResults } from '../handlers/broadcastResults';
import { POST as postConsolidate } from '../handlers/consolidate';
import { POST as postRescheduleToday } from '../handlers/rescheduleToday';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getExams(req);
      case 'generate':
        return await getGenerate(req);
      case 'lottery':
        return await getLottery(req);
      case 'objective':
        return await getObjective(req);
      case 'subjective':
        return await getSubjective(req);
      default:
        return NextResponse.json({ message: `Unknown exam GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Exams Dispatcher GET Error:', error);
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
      case 'generate':
        return await postGenerate(req);
      case 'lottery':
        return await postLottery(req);
      case 'objective':
        return await postObjective(req);
      case 'subjective':
        return await postSubjective(req);
      case 'broadcast-results':
        return await postBroadcastResults(req);
      case 'consolidate':
        return await postConsolidate(req);
      case 'reschedule-today':
        return await postRescheduleToday(req);
      default:
        return NextResponse.json({ message: `Unknown exam POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Exams Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await deleteExams(req);
      default:
        return NextResponse.json({ message: `Unknown exam DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Exams Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
