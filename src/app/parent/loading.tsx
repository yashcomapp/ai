'use client';

import React from 'react';
import { StatsSkeleton, TableSkeleton } from '@/components/common/Skeletons';

export default function ParentLoading() {
  return (
    <div style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '12px 14px' }}>
      {/* Child Bar Skeleton */}
      <div 
        className="skeleton-blink"
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '12px 16px',
          background: 'var(--surface)',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--border-light)',
          marginBottom: '16px'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'var(--bg-soft)' }} />
          <div style={{ width: '150px', height: '18px', background: 'var(--bg-soft)', borderRadius: '4px' }} />
        </div>
        <div style={{ width: '130px', height: '34px', background: 'var(--bg-soft)', borderRadius: '6px' }} />
      </div>

      {/* Metrics Skeleton */}
      <StatsSkeleton count={2} />

      {/* Reviews List Skeleton */}
      <TableSkeleton rows={5} />
    </div>
  );
}
