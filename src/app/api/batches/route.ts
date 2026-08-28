import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
export async function GET() {
  try {
    const snapshot = await adminDb.collection('batches').orderBy('name', 'asc').limit(100).get();
    const batches = snapshot.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || '',
      subject: doc.data().subject || '',
      description: doc.data().description || ''
    }));
    return NextResponse.json({ batches });
  } catch (error: any) {
    console.error('API /api/batches error:', error);
    return NextResponse.json({ message: 'Failed to load batches' }, { status: 500 });
  }
}
