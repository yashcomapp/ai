import { cookies } from 'next/headers';
import { adminAuth, adminDb } from '@/lib/firebase/admin';
import { getStudentResultsData } from '@/lib/resultsDb';
import StudentResultsClient from './StudentResultsClient';

export const dynamic = 'force-dynamic';

export default async function StudentResultsPage() {
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
          if (userData.role?.toLowerCase() === 'student') {
            const isListAutonomous = userData.autonomous === true;
            const studentBatches = userData.batchIds || [];
            initialData = await getStudentResultsData(userData.studentCode || '', isListAutonomous, studentBatches);
          }
        }
      }
    } catch (err) {
      console.warn('Failed to pre-fetch student results data server-side:', err);
    }
  }

  return <StudentResultsClient initialData={initialData ? JSON.parse(JSON.stringify(initialData)) : null} />;
}
