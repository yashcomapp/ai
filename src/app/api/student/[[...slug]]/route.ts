import { NextRequest, NextResponse } from 'next/server';
import { GET as getDashboard } from '../handlers/dashboard';
import { GET as getLearning } from '../handlers/learning';
import { GET as getPractice, POST as postPractice } from '../handlers/practice';
import { GET as getResults } from '../handlers/results';
import { GET as getFees } from '../handlers/fees';
import { GET as getSettings, POST as postSettings } from '../handlers/settings';
import { POST as postDisputes } from '../handlers/disputes';
import { GET as getExamRegister, POST as postExamRegister } from '../handlers/examRegister';
import { GET as getAttendance } from '../handlers/attendance';
import { GET as getAttendanceDeclare, POST as postAttendanceDeclare } from '../handlers/attendanceDeclare';
import { GET as getExams, POST as postExams } from '../handlers/exams';
import { GET as getExamsSubjective, POST as postExamsSubjective } from '../handlers/examsSubjective';
import { POST as postExamsPeerReview } from '../handlers/examsPeerReview';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'dashboard':
        return await getDashboard(req);
      case 'learning':
        return await getLearning(req);
      case 'practice':
        return await getPractice(req);
      case 'results':
        return await getResults(req);
      case 'fees':
        return await getFees(req);
      case 'settings':
        return await getSettings(req);
      case 'exam-register':
        return await getExamRegister(req);
      case 'attendance':
        return await getAttendance(req);
      case 'attendance/declare':
        return await getAttendanceDeclare(req);
      case 'exams':
        return await getExams(req);
      case 'exams/subjective':
        return await getExamsSubjective(req);
      default:
        return NextResponse.json({ message: `Unknown student GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case 'practice':
        return await postPractice(req);
      case 'settings':
        return await postSettings(req);
      case 'disputes':
        return await postDisputes(req);
      case 'exam-register':
        return await postExamRegister(req);
      case 'attendance/declare':
        return await postAttendanceDeclare(req);
      case 'exams':
        return await postExams(req);
      case 'exams/subjective':
        return await postExamsSubjective(req);
      case 'exams/subjective/peer-review':
        return await postExamsPeerReview(req);
      default:
        return NextResponse.json({ message: `Unknown student POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Student Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
