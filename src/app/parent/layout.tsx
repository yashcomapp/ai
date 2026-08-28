'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { db } from '@/lib/firebase/firestore';
import { doc, onSnapshot } from 'firebase/firestore';

export default function ParentLayout({ children }: { children: React.ReactNode }) {
  const { logout } = useAuth();
  const [maintenance, setMaintenance] = useState<{ active: boolean; message: string } | null>(null);

  useEffect(() => {
    const unsub = onSnapshot(doc(db, 'config', 'systemAccess'), (snapshot) => {
      if (snapshot.exists()) {
        const data = snapshot.data();
        if (data.maintenanceMode && data.blockedRoles?.includes('parent')) {
          setMaintenance({
            active: true,
            message: data.message || 'The system is undergoing scheduled maintenance. Access will be restored shortly.'
          });
        } else {
          setMaintenance(null);
        }
      } else {
        setMaintenance(null);
      }
    }, () => {});
    return () => unsub();
  }, []);

  if (maintenance?.active) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)', padding: '24px' }}>
        <div className="card glass" style={{ maxWidth: '480px', width: '100%', padding: '32px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '20px', background: 'var(--surface)' }}>
          <span style={{ fontSize: '3rem' }}>🛠️</span>
          <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 800, color: 'var(--accent)' }}>System Under Maintenance</h2>
          <p style={{ margin: 0, fontSize: '14px', lineHeight: '1.6', color: 'var(--text)' }}>
            {maintenance.message}
          </p>
          <button className="btn btn-secondary" onClick={logout} style={{ marginTop: '10px', height: '40px', fontWeight: 700 }}>
            Sign Out
          </button>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
