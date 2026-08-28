import { cookies } from 'next/headers';
import { adminAuth, adminDb } from '@/lib/firebase/admin';
import { getStudentLearningData } from '@/lib/studentDb';
import StudentLearningClient from './StudentLearningClient';

export const dynamic = 'force-dynamic';

export default async function StudentLearningPage() {
  const cookieStore = cookies();
  const ycIdToken = cookieStore.get('yc_id_token')?.value || '';

  let initialData: any = null;

  if (ycIdToken) {
    try {
      const decodedToken = await adminAuth.verifyIdToken(ycIdToken);
      if (decodedToken) {
        const userDoc = await adminDb.collection('users').doc(decodedToken.uid).get();
        if (userDoc.exists) {
          const userData = userDoc.data() || {};
          if (userData.role?.toLowerCase() === 'student' && userData.autonomous !== true) {
            initialData = await getStudentLearningData(userData);
          }
        }
      }
    } catch (err) {
      console.warn('Failed to pre-fetch student learning data server-side:', err);
    }
  }

  return <StudentLearningClient initialData={initialData ? JSON.parse(JSON.stringify(initialData)) : null} />;
}
