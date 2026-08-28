import StudentDashboardClient from './StudentDashboardClient';

export const dynamic = 'force-dynamic';

export default async function StudentDashboardPage() {
  return <StudentDashboardClient initialData={null} />;
}
