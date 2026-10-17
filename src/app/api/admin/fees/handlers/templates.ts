import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { toNonNegativeNumber } from '@/lib/validationUtils';
import { getFromCache, setInCache, invalidateCache } from '@/lib/firebase/cache';

const FEE_TEMPLATES_CACHE_KEY = 'fee_templates_all';
const FEE_TEMPLATES_CACHE_TTL = 300000; // 5 minutes

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const cached = getFromCache<any[]>(FEE_TEMPLATES_CACHE_KEY);
    if (cached) {
      return NextResponse.json({ success: true, templates: cached });
    }

    const templatesSnap = await adminDb.collection('feeTemplates').limit(100).get();
    const templates = templatesSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

    setInCache(FEE_TEMPLATES_CACHE_KEY, templates, FEE_TEMPLATES_CACHE_TTL);
    return NextResponse.json({ success: true, templates });
  } catch (error: any) {
    console.error('API GET fee templates error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action, templateId, templateData } = body;

    if (action === 'saveTemplate') {
      const { name, classNum, totalPackageAmount, installments } = templateData;
      if (!name || !classNum || totalPackageAmount === undefined || !installments) {
        return NextResponse.json({ error: 'Missing required template fields.' }, { status: 400 });
      }

      const totalPkg = toNonNegativeNumber(totalPackageAmount, 'totalPackageAmount');
      const docId = templateId || `tmpl_${classNum}_${Date.now()}`;
      const docRef = adminDb.collection('feeTemplates').doc(docId);
      
      const payload = {
        templateId: docId,
        name,
        classNum: String(classNum),
        totalPackageAmount: totalPkg,
        registrationFee: 0,
        installments: (Array.isArray(installments) ? installments : []).map((inst: any, idx: number) => ({
          installmentNo: idx + 1,
          amount: toNonNegativeNumber(inst.amount, `installment ${idx + 1} amount`),
          dueDate: String(inst.dueDate || (idx === 0 ? '2026-03-15' : ''))
        })),
        updatedAt: new Date().toISOString()
      };

      await docRef.set(payload, { merge: true });
      invalidateCache(FEE_TEMPLATES_CACHE_KEY);
      return NextResponse.json({ success: true, template: payload });
    }

    if (action === 'deleteTemplate') {
      if (!templateId) {
        return NextResponse.json({ error: 'Missing templateId.' }, { status: 400 });
      }
      await adminDb.collection('feeTemplates').doc(templateId).delete();
      invalidateCache(FEE_TEMPLATES_CACHE_KEY);
      return NextResponse.json({ success: true, message: 'Template deleted successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST fee templates error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
