import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';

export class ReportService {

  /**
   * Compiles global application usage and evaluations statistics.
   */
  static async getUsageReport() {
    const [
      usersCountSnap,
      examsCountSnap,
      questionsCountSnap,
      attemptsCountSnap,
      evaluationsSnap
    ] = await Promise.all([
      adminDb.collection('users').count().get(),
      adminDb.collection('subjectiveExams').count().get(),
      adminDb.collection('questions').count().get(),
      adminDb.collection('examAttempts').count().get(),
      adminDb.collection('evaluations').get()
    ]);

    let parentReviews = 0;
    let studentReviews = 0;

    const evaluations = evaluationsSnap.docs.map(doc => {
      const data = doc.data();
      if (data.reviewedByActor === 'student') {
        studentReviews++;
      } else if (data.reviewedByActor === 'parent' || data.evaluatorType === 'parent') {
        parentReviews++;
      }
      return {
        id: doc.id,
        ...data,
        createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : data.createdAt || null,
        date: data.date?.toDate ? data.date.toDate() : data.date || null
      };
    });

    return {
      stats: {
        totalUsers: usersCountSnap.data().count,
        totalExams: examsCountSnap.data().count,
        totalQuestions: questionsCountSnap.data().count,
        totalAttempts: attemptsCountSnap.data().count,
        parentReviews,
        studentReviews
      },
      evaluations
    };
  }

  /**
   * Compiles proctoring compliance and integrity statistics.
   */
  static async getIntegrityReport() {
    const [scoresSnap, studentsSnap] = await Promise.all([
      adminDb.collection('integrityScores').get(),
      adminDb.collection('users').where('role', '==', 'student').get()
    ]);

    const scores = scoresSnap.docs.map(doc => {
      const data = doc.data();
      const val = data.integrityScore !== undefined ? data.integrityScore : data.score;
      return {
        ...data,
        resolvedScore: val !== undefined ? Number(val) : 100
      };
    });
    const totalScores = scores.length;
    const reviewCount = scores.filter(s => s.resolvedScore < 60).length;
    const avgScore = totalScores > 0
      ? Math.round(scores.reduce((sum, s) => sum + s.resolvedScore, 0) / totalScores)
      : 100;

    const students = studentsSnap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        name: data.name || '',
        email: data.email || '',
        studentCode: data.studentCode || '',
        rollNumber: data.rollNumber || '',
        class: data.class || '',
        status: data.status || 'active'
      };
    }).filter(s => s.status !== 'inactive');

    return {
      totalScores,
      reviewCount,
      avgScore,
      students
    };
  }

}
