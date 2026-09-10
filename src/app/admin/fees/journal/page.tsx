'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import FeesJournal, { StudentFeeRecord } from '@/components/admin/FeesJournal';

export default function FeesJournalPage() {
  const { firebaseUser } = useAuth();
  const router = useRouter();

  const [students, setStudents] = useState<StudentFeeRecord[]>([]);
  const [loadingStudents, setLoadingStudents] = useState(true);
  const [error, setError] = useState('');

  // Fetch student sheets
  async function loadStudents() {
    if (!firebaseUser) return;
    setLoadingStudents(true);
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/fees', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setStudents(data.students || []);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setLoadingStudents(false);
    }
  }

  useEffect(() => {
    loadStudents();
  }, [firebaseUser]);

  const getIdToken = async () => {
    if (!firebaseUser) return null;
    return await firebaseUser.getIdToken();
  };

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '24px 12px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        {/* Header Block */}
        <div className="card glass" style={{ padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: 'var(--accent)', margin: 0 }}>
              📖 Fees Journal & Collection Ledger
            </h2>
            <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
              Comprehensive revenue reports, batch summaries, date-wise audit trails, and student balance sheets.
            </p>
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button className="btn btn-secondary" onClick={() => router.push('/admin/fees')}>
              🪙 Fee Configurations
            </button>
            <button className="btn btn-secondary" onClick={() => router.push('/admin')}>
              Back
            </button>
          </div>
        </div>

        {error && <div className="alert-box alert-box-danger">{error}</div>}

        {/* Fees Journal Reports View */}
        <FeesJournal
          students={students}
          loadingStudents={loadingStudents}
          getIdToken={getIdToken}
          onSelectStudent={() => {
            router.push('/admin/fees');
          }}
        />

      </div>
    </div>
  );
}
