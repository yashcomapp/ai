import { NextRequest, NextResponse } from 'next/server';
import * as admin from 'firebase-admin';
import { adminDb, adminAuth } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { decrypt } from '@/lib/encryption';
export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const snapshot = await adminDb.collection('registrations')
      .orderBy('createdAt', 'desc')
      .limit(500)
      .get();

    const registrations = snapshot.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        ...data,
        createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : data.createdAt
      };
    });

    return NextResponse.json({ registrations });
  } catch (error: any) {
    console.error('API get registrations error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 2. POST - Process actions (approve / reject)
export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { id, action } = body;

    if (!id || !action) {
      return NextResponse.json({ message: 'Missing registration ID or action.' }, { status: 400 });
    }

    const regRef = adminDb.collection('registrations').doc(id);
    const regDoc = await regRef.get();

    if (!regDoc.exists) {
      return NextResponse.json({ message: 'Registration profile not found.' }, { status: 404 });
    }

    const regData = regDoc.data() || {};

    if (action === 'reject') {
      await regRef.update({
        status: 'rejected',
        rejectedAt: admin.firestore.FieldValue.serverTimestamp(),
        rejectedBy: (adminUser.decodedToken?.email || adminUser.userData?.email),
        password: admin.firestore.FieldValue.delete()
      });
      return NextResponse.json({ success: true });
    }

    if (action === 'approve') {
      if (regData.status === 'approved') {
        return NextResponse.json({ message: 'Registration is already approved.' }, { status: 400 });
      }

      // Compute birthdate DDMMYY format password to satisfy Firebase 6-character minimum
      const getBirthdatePassword = (dobStr: string): string => {
        if (!dobStr) return '010100';
        const parts = dobStr.split('-');
        if (parts.length === 3) {
          const year = parts[0];
          const month = parts[1];
          const day = parts[2];
          const yy = year.substring(year.length - 2);
          return `${day.padStart(2, '0')}${month.padStart(2, '0')}${yy}`;
        }
        const d = new Date(dobStr);
        if (!isNaN(d.getTime())) {
          const day = String(d.getDate()).padStart(2, '0');
          const month = String(d.getMonth() + 1).padStart(2, '0');
          const yy = String(d.getFullYear()).slice(-2);
          return `${day}${month}${yy}`;
        }
        return '010100';
      };
      const rawPassword = getBirthdatePassword(regData.dob);

      // Step 2a: Create Student Auth user
      let studentEmailToUse = (regData.studentEmail || '').trim().toLowerCase();
      if (regData.parentEmail && studentEmailToUse === regData.parentEmail.trim().toLowerCase()) {
        studentEmailToUse = studentEmailToUse.replace('@', '+student@');
      }

      let studentId = '';
      try {
        const studentCred = await adminAuth.createUser({
          email: studentEmailToUse,
          password: rawPassword,
          displayName: regData.studentName
        });
        studentId = studentCred.uid;
      } catch (authErr: any) {
        if (authErr.code === 'auth/email-already-in-use' || authErr.code === 'auth/email-already-exists') {
          // Look up user by email
          const existingUsers = await adminDb.collection('users')
            .where('email', '==', studentEmailToUse)
            .limit(1)
            .get();

          if (existingUsers.empty) {
            // Auth account exists but no firestore users doc, query authentication to get uid
            const userRecord = await adminAuth.getUserByEmail(studentEmailToUse);
            studentId = userRecord.uid;
          } else {
            const studentDoc = existingUsers.docs[0];
            if (studentDoc.data()?.role === 'admin') {
              return NextResponse.json({ message: 'Email belongs to an existing admin account.' }, { status: 400 });
            }
            if (studentDoc.data()?.role === 'parent') {
              // If it matches a parent user (which means the parent email is used by a student),
              // we automatically suffix it to create a unique separate account
              studentEmailToUse = studentEmailToUse.replace('@', '+student@');
              try {
                const studentCred = await adminAuth.createUser({
                  email: studentEmailToUse,
                  password: rawPassword,
                  displayName: regData.studentName
                });
                studentId = studentCred.uid;
              } catch (retryErr: any) {
                if (retryErr.code === 'auth/email-already-in-use' || retryErr.code === 'auth/email-already-exists') {
                  const retryUserRecord = await adminAuth.getUserByEmail(studentEmailToUse);
                  studentId = retryUserRecord.uid;
                } else {
                  throw retryErr;
                }
              }
            } else {
              studentId = studentDoc.id;
            }
          }
        } else {
          throw authErr;
        }
      }

      // Step 2b: Generate unique sequential studentCode ST-YYYY-NNNNNN
      const year = new Date().getFullYear();
      const counterRef = adminDb.collection('counters').doc(`studentCode_${year}`);
      let nextSeq = 1;

      await adminDb.runTransaction(async (tx) => {
        const snap = await tx.get(counterRef);
        nextSeq = snap.exists ? (snap.data()?.nextSequence || 1) : 1;
        tx.set(counterRef, { nextSequence: nextSeq + 1 }, { merge: true });
      });

      const studentCode = `ST-${year}-${String(nextSeq).padStart(6, '0')}`;

      // Step 2c: Retrieve batch class to populate user.class
      let batchClass = null;
      let batchSnap = null;
      if (regData.batchId) {
        batchSnap = await adminDb.collection('batches').doc(regData.batchId).get();
        if (batchSnap.exists) {
          batchClass = batchSnap.data()?.class || null;
        }
      }

      // Step 2d: Save Student document to users collection
      const studentUserRef = adminDb.collection('users').doc(studentId);
      await studentUserRef.set({
        name: regData.studentName,
        email: studentEmailToUse,
        rollNumber: regData.tempId || `TEMP-00-${Date.now().toString().slice(-6)}`,
        studentCode: studentCode,
        mobile: regData.studentMobile,
        class: batchClass || regData.class || regData.studentClass || null,
        role: 'student',
        batchIds: regData.batchId ? [regData.batchId] : [],
        status: 'active',
        parentEmail: regData.parentEmail || null,
        createdAt: admin.firestore.FieldValue.serverTimestamp(),
        registeredFrom: id
      }, { merge: true });

      // Step 2e: Increment studentCount in batches collection
      if (regData.batchId && batchSnap && batchSnap.exists) {
        await adminDb.collection('batches').doc(regData.batchId).update({
          studentCount: admin.firestore.FieldValue.increment(1)
        }).catch(err => console.warn('Could not update batch student count:', err.message));
      }

      // Step 2f: Process Parent account creation (optional on form)
      let parentId = null;
      let parentMsg = '';
      let existingParentData: any = null;

      if (regData.parentEmail) {
        try {
          const parentPassword = rawPassword;
          const parentCred = await adminAuth.createUser({
            email: regData.parentEmail,
            password: parentPassword,
            displayName: regData.parentName
          });
          parentId = parentCred.uid;
        } catch (parentAuthErr: any) {
          if (parentAuthErr.code === 'auth/email-already-in-use' || parentAuthErr.code === 'auth/email-already-exists') {
            const existingUsers = await adminDb.collection('users')
              .where('email', '==', regData.parentEmail)
              .limit(1)
              .get();

            if (existingUsers.empty) {
              const userRecord = await adminAuth.getUserByEmail(regData.parentEmail);
              parentId = userRecord.uid;
            } else {
              const parentDoc = existingUsers.docs[0];
              if (parentDoc.data()?.role === 'admin') {
                return NextResponse.json({ message: 'Parent email belongs to an admin account.' }, { status: 400 });
              }
              parentId = parentDoc.id;
              existingParentData = parentDoc.data();
            }
          } else {
            throw parentAuthErr;
          }
        }

        // Merge multiple children details
        let newStudentCodes = [studentCode];
        let newStudentIds = [studentId];
        let newStudentNames = [regData.studentName];

        if (existingParentData) {
          const currentCodes = Array.isArray(existingParentData.studentCodes) 
            ? existingParentData.studentCodes 
            : (existingParentData.studentCode ? [existingParentData.studentCode] : []);
          
          const currentIds = Array.isArray(existingParentData.studentIds) 
            ? existingParentData.studentIds 
            : (existingParentData.studentId ? [existingParentData.studentId] : []);

          const currentNames = Array.isArray(existingParentData.studentNames) 
            ? existingParentData.studentNames 
            : (existingParentData.studentName ? [existingParentData.studentName] : []);

          newStudentCodes = Array.from(new Set([...currentCodes, studentCode].filter(Boolean)));
          newStudentIds = Array.from(new Set([...currentIds, studentId].filter(Boolean)));
          newStudentNames = Array.from(new Set([...currentNames, regData.studentName].filter(Boolean)));
        }

        // Save Parent document to users collection
        const parentUserRef = adminDb.collection('users').doc(parentId);
        await parentUserRef.set({
          name: regData.parentName,
          email: regData.parentEmail,
          mobile: regData.parentMobile,
          role: 'parent',
          studentId: studentId,
          studentCode: studentCode,
          studentName: regData.studentName,
          studentCodes: newStudentCodes,
          studentIds: newStudentIds,
          studentNames: newStudentNames,
          createdAt: existingParentData?.createdAt || admin.firestore.FieldValue.serverTimestamp(),
          registeredFrom: id
        }, { merge: true });
      } else {
        parentMsg = ' (no parent account created - email was not provided)';
      }

      // Step 2g: Automatically initialize student's fee details from blanket class template
      try {
        const targetClass = batchClass || regData.class || regData.studentClass || '10';
        const tmplSnap = await adminDb.collection('feeTemplates')
          .where('classNum', '==', String(targetClass))
          .limit(1)
          .get();
        
        if (!tmplSnap.empty) {
          const tmpl = tmplSnap.docs[0].data();
          const netPayable = Number(tmpl.totalPackageAmount || 0);
          const installments = Array.isArray(tmpl.installments) ? tmpl.installments : [];
          
          const formattedInstallments = installments.map((inst: any, idx: number) => ({
            installmentId: `inst_${idx + 1}`,
            installmentNo: idx + 1,
            amount: Number(inst.amount),
            dueDate: inst.dueDate || '',
            status: 'pending',
            paidAt: null
          }));

          const studentFeeRecord = {
            studentCode: studentCode,
            studentName: regData.studentName,
            classNum: String(targetClass),
            batchId: regData.batchId || '',
            totalPackageAmount: Number(tmpl.totalPackageAmount || 0),
            discountAmount: 0,
            netPayableAmount: netPayable,
            registrationFee: {
              amount: Number(tmpl.registrationFee || 0),
              status: 'pending',
              paidAt: null
            },
            installments: formattedInstallments,
            totalPaidAmount: 0,
            outstandingAmount: netPayable,
            feeStatus: 'unpaid',
            hasOverdueInstallment: false,
            nextInstallmentDueDate: formattedInstallments[0]?.dueDate || null,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
          };

          await adminDb.collection('studentFees').doc(studentCode).set(studentFeeRecord);
        }
      } catch (feeInitErr: any) {
        console.warn('Could not auto-initialize student fees record on approval:', feeInitErr.message);
      }

      // Step 2h: Mark registration document as approved and delete plaintext password
      await regRef.update({
        status: 'approved',
        approvedAt: admin.firestore.FieldValue.serverTimestamp(),
        approvedBy: (adminUser.decodedToken?.email || adminUser.userData?.email),
        studentId,
        parentId: parentId || null,
        password: admin.firestore.FieldValue.delete()
      });

      return NextResponse.json({
        success: true,
        message: `Approved successfully! Accounts created.${parentMsg}`
      });
    }

    return NextResponse.json({ message: 'Invalid action' }, { status: 400 });

  } catch (error: any) {
    console.error('API registrations action error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 3. PUT - Edit registration
export async function PUT(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { id, updates } = body;

    if (!id || !updates) {
      return NextResponse.json({ message: 'Missing registration ID or updates.' }, { status: 400 });
    }

    // Filter updates to avoid updating system fields accidentally
    const cleanUpdates: Record<string, any> = {
      studentName: updates.studentName,
      studentEmail: updates.studentEmail,
      studentMobile: updates.studentMobile,
      dob: updates.dob,
      gender: updates.gender,
      bloodGroup: updates.bloodGroup,
      address: updates.address,
      parentName: updates.parentName,
      parentEmail: updates.parentEmail,
      parentMobile: updates.parentMobile,
      parentRelation: updates.parentRelation,
      status: updates.status,
      updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      updatedBy: (adminUser.decodedToken?.email || adminUser.userData?.email)
    };



    await adminDb.collection('registrations').doc(id).update(cleanUpdates);

    return NextResponse.json({ success: true });
  } catch (error: any) {
    console.error('API update registration error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

// 4. DELETE - Delete registration
export async function DELETE(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const id = searchParams.get('id');

    if (!id) {
      return NextResponse.json({ message: 'Missing registration ID.' }, { status: 400 });
    }

    await adminDb.collection('registrations').doc(id).delete();

    return NextResponse.json({ success: true });
  } catch (error: any) {
    console.error('API delete registration error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
