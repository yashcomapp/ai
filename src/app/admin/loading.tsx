'use client';

import React from 'react';
import { StatsSkeleton, TableSkeleton } from '@/components/common/Skeletons';

export default function AdminLoading() {
  return (
    <div style={{ padding: '16px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      {/* Title skeleton */}
      <div style={{ marginBottom: '20px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ width: '180px', height: '28px', background: 'var(--surface-3)', borderRadius: '6px' }} />
        <div style={{ width: '120px', height: '34px', background: 'var(--surface-3)', borderRadius: '6px' }} />
      </div>

      {/* Admin Stats Grid */}
      <StatsSkeleton count={3} />

      {/* Main Content Table Skeleton */}
      <TableSkeleton rows={6} />
    </div>
  );
}
