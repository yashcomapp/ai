'use client';

import React, { Suspense, useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import StudentsManager from '@/components/admin/StudentsManager';
import BatchesManager from '@/components/admin/BatchesManager';
import RegistrationsManager from '@/components/admin/RegistrationsManager';

type TabType = 'students' | 'batches' | 'registrations';

function AdminStudentsUnifiedContent({ initialTab }: { initialTab?: TabType }) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const tabParam = searchParams.get('tab') as TabType | null;
  const [activeTab, setActiveTab] = useState<TabType>(initialTab || tabParam || 'students');

  useEffect(() => {
    if (tabParam && (tabParam === 'students' || tabParam === 'batches' || tabParam === 'registrations')) {
      setActiveTab(tabParam);
    }
  }, [tabParam]);

  const handleTabChange = (tab: TabType) => {
    setActiveTab(tab);
    router.replace(`/admin/students?tab=${tab}`, { scroll: false });
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>

      {/* Main Container with Tab Bar */}
      <main style={{ flex: 1, padding: '20px 16px', maxWidth: '1200px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>

        {/* Modern Tab Switcher */}
        <div style={{ display: 'flex', gap: '6px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '2px' }}>
          <button
            onClick={() => handleTabChange('students')}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'students' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'students' ? '2.5px solid var(--accent)' : '2.5px solid transparent',
              color: activeTab === 'students' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 700,
              cursor: 'pointer',
              fontSize: '13px',
              borderRadius: 'var(--radius-sm) var(--radius-sm) 0 0',
              transition: 'all 0.15s ease'
            }}
          >
            Students
          </button>
          <button
            onClick={() => handleTabChange('batches')}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'batches' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'batches' ? '2.5px solid var(--accent)' : '2.5px solid transparent',
              color: activeTab === 'batches' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 700,
              cursor: 'pointer',
              fontSize: '13px',
              borderRadius: 'var(--radius-sm) var(--radius-sm) 0 0',
              transition: 'all 0.15s ease'
            }}
          >
            Batches
          </button>
          <button
            onClick={() => handleTabChange('registrations')}
            style={{
              padding: '10px 20px',
              border: 'none',
              background: activeTab === 'registrations' ? 'var(--surface)' : 'transparent',
              borderBottom: activeTab === 'registrations' ? '2.5px solid var(--accent)' : '2.5px solid transparent',
              color: activeTab === 'registrations' ? 'var(--accent)' : 'var(--text-muted)',
              fontWeight: 700,
              cursor: 'pointer',
              fontSize: '13px',
              borderRadius: 'var(--radius-sm) var(--radius-sm) 0 0',
              transition: 'all 0.15s ease'
            }}
          >
            Registrations
          </button>
        </div>

        {/* Tab Contents */}
        <div style={{ marginTop: '8px' }}>
          {activeTab === 'students' && <StudentsManager />}
          {activeTab === 'batches' && <BatchesManager />}
          {activeTab === 'registrations' && <RegistrationsManager />}
        </div>
      </main>
    </div>
  );
}

export default function UnifiedStudentsManager({ initialTab }: { initialTab?: TabType }) {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>Loading...</div>
      </div>
    }>
      <AdminStudentsUnifiedContent initialTab={initialTab} />
    </Suspense>
  );
}
