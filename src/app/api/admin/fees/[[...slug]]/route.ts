import { NextRequest, NextResponse } from 'next/server';
import { GET as getFees, POST as postFees, DELETE as deleteFees } from '../handlers/fees';
import { GET as getTemplates, POST as postTemplates, DELETE as deleteTemplates } from '../handlers/templates';
import { GET as getTransactions, POST as postTransactions } from '../handlers/transactions';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await getFees(req);
      case 'templates':
        return await getTemplates(req);
      case 'transactions':
        return await getTransactions(req);
      default:
        return NextResponse.json({ message: `Unknown fees GET route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Fees Dispatcher GET Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await postFees(req);
      case 'templates':
        return await postTemplates(req);
      case 'transactions':
        return await postTransactions(req);
      default:
        return NextResponse.json({ message: `Unknown fees POST route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Fees Dispatcher POST Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest, { params }: { params: { slug?: string[] } | Promise<{ slug?: string[] }> }) {
  try {
    const resolvedParams = await Promise.resolve(params);
    const subroute = (resolvedParams.slug || []).join('/');

    switch (subroute) {
      case '':
        return await deleteFees(req);
      case 'templates':
        return await deleteTemplates(req);
      default:
        return NextResponse.json({ message: `Unknown fees DELETE route: ${subroute}` }, { status: 404 });
    }
  } catch (error: any) {
    console.error('API Admin Fees Dispatcher DELETE Error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
