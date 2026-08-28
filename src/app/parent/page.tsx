import ParentDashboardClient from './ParentDashboardClient';

export const dynamic = 'force-dynamic';

export default async function ParentDashboardPage() {
  return <ParentDashboardClient initialData={undefined} />;
}
