'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function AdminReportsRedirect() {
  const router = useRouter();
  useEffect(() => {
    router.replace('/admin/reports/learning-quotient');
  }, [router]);

  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
      <div className="loading" style={{ display: 'block' }}>
        <div className="spinner"></div> Redirecting to Reports...
      </div>
    </div>
  );
}
