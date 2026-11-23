import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { getFromCache, setInCache } from '@/lib/firebase/cache';
import { sortBatchesAscending } from '@/lib/batchUtils';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    // Public directory for candidate registration. Admin batch modifications are strictly protected via verifyRole on /api/admin/batches.
    const cacheKey = 'all-batches';
    const cached = getFromCache<any[]>(cacheKey);
    if (cached) {
      return NextResponse.json({ batches: cached }, {
        headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' }
      });
    }

    const snapshot = await adminDb.collection('batches').limit(100).get();
    // Return minimal metadata fields needed by registration, sorted ascending (8th, 9th, 10th)
    const rawBatches = snapshot.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || '',
      class: doc.data().class || '',
      subject: doc.data().subject || '',
      description: doc.data().description || ''
    }));
    const batches = sortBatchesAscending(rawBatches);
    setInCache(cacheKey, batches, 300000); // 5 mins

    return NextResponse.json({ batches }, {
      headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' }
    });
  } catch (error: any) {
    console.error('API /api/batches error:', error);
    return NextResponse.json({ message: 'Failed to load batches' }, { status: 500 });
  }
}
