import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const admin = await verifyRole(req, 'admin');
    if (!admin) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const templatesSnap = await adminDb.collection('feeTemplates').get();
    const templates = templatesSnap.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));

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
      const { name, classNum, totalPackageAmount, registrationFee, installments } = templateData;
      if (!name || !classNum || totalPackageAmount === undefined || !installments) {
        return NextResponse.json({ error: 'Missing required template fields.' }, { status: 400 });
      }

      const docId = templateId || `tmpl_${classNum}_${Date.now()}`;
      const docRef = adminDb.collection('feeTemplates').doc(docId);
      
      const payload = {
        templateId: docId,
        name,
        classNum: String(classNum),
        totalPackageAmount: Number(totalPackageAmount),
        registrationFee: Number(registrationFee || 0),
        installments: installments.map((inst: any) => ({
          installmentNo: Number(inst.installmentNo),
          amount: Number(inst.amount),
          dueDate: String(inst.dueDate || '')
        })),
        updatedAt: new Date().toISOString()
      };

      await docRef.set(payload, { merge: true });
      return NextResponse.json({ success: true, template: payload });
    }

    if (action === 'deleteTemplate') {
      if (!templateId) {
        return NextResponse.json({ error: 'Missing templateId.' }, { status: 400 });
      }
      await adminDb.collection('feeTemplates').doc(templateId).delete();
      return NextResponse.json({ success: true, message: 'Template deleted successfully.' });
    }

    return NextResponse.json({ error: 'Invalid action.' }, { status: 400 });
  } catch (error: any) {
    console.error('API POST fee templates error:', error);
    return NextResponse.json({ error: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
