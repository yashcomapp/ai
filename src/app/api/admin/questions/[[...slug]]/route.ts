import { NextRequest, NextResponse } from 'next/server';
import { GET as getQuestions, POST as postQuestions, DELETE as deleteQuestions } from '../handlers/questions';
import { GET as getAuditExplanations } from '../handlers/auditExplanations';
import { GET as getAuditNumerical, POST as postAuditNumerical } from '../handlers/auditNumerical';
import { GET as getDisputes, POST as postDisputes } from '../handlers/disputes';
import { GET as getHarmonize, POST as postHarmonize } from '../handlers/harmonize';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getQuestions(req);
      case 'audit-explanations':
        return await getAuditExplanations(req);
      case 'audit-numerical':
        return await getAuditNumerical(req);
      case 'disputes':
        return await getDisputes(req);
      case 'harmonize':
        return await getHarmonize(req);
      default:
        return NextResponse.json({ message: `Unknown question GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Questions Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postQuestions(req);
      case 'audit-numerical':
        return await postAuditNumerical(req);
      case 'disputes':
        return await postDisputes(req);
      case 'harmonize':
        return await postHarmonize(req);
      default:
        return NextResponse.json({ message: `Unknown question POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Questions Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await deleteQuestions(req);
      default:
        return NextResponse.json({ message: `Unknown question DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Questions Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
