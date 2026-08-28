import { NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { getFromCache, setInCache } from '@/lib/firebase/cache';

export async function GET() {
  try {
    const cacheKey = 'all-batches';
    const cached = getFromCache<any[]>(cacheKey);
    if (cached) {
      return NextResponse.json({ batches: cached }, {
        headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' }
      });
    }

    const snapshot = await adminDb.collection('batches').orderBy('name', 'asc').limit(100).get();
    const batches = snapshot.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || '',
      subject: doc.data().subject || '',
      description: doc.data().description || ''
    }));
    setInCache(cacheKey, batches, 300000); // 5 mins

    return NextResponse.json({ batches }, {
      headers: { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' }
    });
  } catch (error: any) {
    console.error('API /api/batches error:', error);
    return NextResponse.json({ message: 'Failed to load batches' }, { status: 500 });
  }
}
