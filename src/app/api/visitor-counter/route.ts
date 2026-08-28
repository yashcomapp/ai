import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const docRef = adminDb.collection('systemStats').doc('visitors');
    const snap = await docRef.get();
    const count = snap.exists ? (snap.data()?.count || 0) : 0;
    return NextResponse.json({ count });
  } catch (error: any) {
    console.error('Visitor counter GET error:', error);
    return NextResponse.json({ count: 0, error: error.message }, { status: 500 });
  }
}

const ipRateLimit = new Map<string, number>();

export async function POST(req: NextRequest) {
  try {
    const ip = req.headers.get('x-forwarded-for') || req.headers.get('x-real-ip') || 'unknown-ip';
    const now = Date.now();
    const lastHit = ipRateLimit.get(ip) || 0;

    // Rate limit: 1 increment per IP every 60 seconds
    if (now - lastHit < 60000) {
      const docRef = adminDb.collection('systemStats').doc('visitors');
      const snap = await docRef.get();
      return NextResponse.json({ count: snap.data()?.count || 0 });
    }

    ipRateLimit.set(ip, now);

    // Clean up old rate limit entries (> 10 mins)
    if (ipRateLimit.size > 1000) {
      ipRateLimit.forEach((time, key) => {
        if (now - time > 600000) ipRateLimit.delete(key);
      });
    }

    const docRef = adminDb.collection('systemStats').doc('visitors');
    await docRef.set({
      count: admin.firestore.FieldValue.increment(1)
    }, { merge: true });

    const snap = await docRef.get();
    const count = snap.data()?.count || 1;
    return NextResponse.json({ count });
  } catch (error: any) {
    console.error('Visitor counter POST error:', error);
    return NextResponse.json({ count: 0, error: error.message }, { status: 500 });
  }
}
