import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    // 1. Fetch all exams matching 020 and 021 for class 8 MGP1
    const examsSnap = await adminDb.collection('exams')
      .where('class', '==', 8)
      .get();

    let doc020: any = null;
    let doc021: any = null;

    examsSnap.docs.forEach(doc => {
      const data = doc.data();
      const name = data.name || '';
      const docId = doc.id;
      if (name.includes('020-8-MGP1') || docId.includes('-020') || data.sequence === 20) {
        doc020 = { id: doc.id, ...data };
      }
      if (name.includes('021-8-MGP1') || docId.includes('-021') || data.sequence === 21) {
        doc021 = { id: doc.id, ...data };
      }
    });

    const report: any = {
      found020: doc020 ? doc020.id : null,
      found021: doc021 ? doc021.id : null,
      actions: []
    };

    if (doc020 && doc021) {
      // 2. Fetch assignments for both
      const [assign020Snap, assign021Snap] = await Promise.all([
        adminDb.collection('batchAssignments').where('examId', '==', doc020.id).get(),
        adminDb.collection('batchAssignments').where('examId', '==', doc021.id).get()
      ]);

      // If 021 has an active assignment, copy its parameters over to 020's assignment
      if (!assign021Snap.empty) {
        const active021Data = assign021Snap.docs[0].data();
        const updatedPayload = {
          ...active021Data,
          examId: doc020.id,
          status: 'active',
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        };

        if (!assign020Snap.empty) {
          await assign020Snap.docs[0].ref.set(updatedPayload);
          report.actions.push(`Updated existing assignment for 020 with active schedule from 021`);
        } else {
          await adminDb.collection('batchAssignments').add(updatedPayload);
          report.actions.push(`Created active assignment for 020 using schedule from 021`);
        }

        // Delete redundant assignments of 021
        for (const doc of assign021Snap.docs) {
          await doc.ref.delete();
          report.actions.push(`Deleted duplicate assignment ${doc.id} for 021`);
        }
      }

      // 3. Move any attempts or reviews from 021 to 020
      const [attempts021, reviews021] = await Promise.all([
        adminDb.collection('examAttempts').where('examId', '==', doc021.id).get(),
        adminDb.collection('reviews').where('examId', '==', doc021.id).get()
      ]);

      for (const att of attempts021.docs) {
        await att.ref.update({ examId: doc020.id });
        report.actions.push(`Re-linked attempt ${att.id} to 020`);
      }

      for (const rev of reviews021.docs) {
        await rev.ref.update({ examId: doc020.id });
        report.actions.push(`Re-linked review ${rev.id} to 020`);
      }

      // 4. Update 020 exam name to reflect updated assignment date
      const updatedName = doc020.name.replace(/-\d{6}$/, '-250826');
      await adminDb.collection('exams').doc(doc020.id).update({
        name: updatedName,
        status: 'active',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      report.actions.push(`Updated 020 exam name to ${updatedName}`);

      // 5. Delete the redundant 021 cloned exam document
      await adminDb.collection('exams').doc(doc021.id).delete();
      report.actions.push(`Deleted cloned exam document ${doc021.id}`);

      // 6. Reset counter for class 8 back to 21
      await adminDb.collection('examCounters').doc('class-8').set({ nextSequence: 21 }, { merge: true });
      report.actions.push(`Reset class-8 counter to sequence 21`);
    } else if (doc020 && !doc021) {
      // Just ensure 020 is active and has clean single assignment
      const updatedName = doc020.name.replace(/-\d{6}$/, '-250826');
      await adminDb.collection('exams').doc(doc020.id).update({
        name: updatedName,
        status: 'active',
        updatedAt: admin.firestore.FieldValue.serverTimestamp()
      });
      report.actions.push(`020 already canonical. Refreshed name to ${updatedName}`);
    }

    return NextResponse.json({ success: true, report });

  } catch (error: any) {
    console.error('Consolidate exams error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
