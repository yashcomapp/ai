'use client';

import React from 'react';
import { StatsSkeleton, TableSkeleton } from '@/components/common/Skeletons';

export default function StudentLoading() {
  return (
    <div style={{ maxWidth: '1000px', width: '100%', margin: '0 auto', padding: '12px 14px' }}>
      {/* Top Profile / Greeting Skeleton */}
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
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ width: '40px', height: '40px', borderRadius: '50%', background: 'var(--bg-soft)' }} />
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div style={{ width: '140px', height: '16px', background: 'var(--bg-soft)', borderRadius: '4px' }} />
            <div style={{ width: '90px', height: '12px', background: 'var(--bg-soft)', borderRadius: '4px' }} />
          </div>
        </div>
        <div style={{ width: '80px', height: '28px', background: 'var(--bg-soft)', borderRadius: '6px' }} />
      </div>

      {/* 4 Metric Cards Skeleton */}
      <StatsSkeleton count={2} />

      {/* Quick Navigation / Action Skeleton */}
      <div 
        className="skeleton-blink"
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(70px, 1fr))',
          gap: '8px',
          marginBottom: '18px'
        }}
      >
        {Array.from({ length: 5 }).map((_, i) => (
          <div
            key={i}
            style={{
              height: '64px',
              background: 'var(--surface)',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border-light)'
            }}
          />
        ))}
      </div>

      {/* Content Skeleton */}
      <TableSkeleton rows={4} />
    </div>
  );
}
