'use client';

import React from 'react';

/**
 * Universal Stats Cards Skeleton
 */
export function StatsSkeleton({ count = 3 }: { count?: number }) {
  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '12px',
        marginBottom: '20px'
      }}
      className="skeleton-blink"
    >
      <div
        className="card"
        style={{
          background: 'var(--surface)',
          padding: '12px 14px',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--border-light)',
          display: 'flex',
          flexDirection: 'column',
          gap: '8px'
        }}
      >
        {Array.from({ length: count }).map((_, i) => (
          <div
            key={i}
            style={{ width: '100%', height: '34px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)' }}
          />
        ))}
      </div>
      <div
        className="card"
        style={{
          background: 'var(--surface)',
          padding: '12px 14px',
          borderRadius: 'var(--radius-lg)',
          border: '1px solid var(--border-light)',
          display: 'flex',
          flexDirection: 'column',
          gap: '8px'
        }}
      >
        {Array.from({ length: Math.max(2, count - 1) }).map((_, i) => (
          <div
            key={i}
            style={{ width: '100%', height: '34px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)' }}
          />
        ))}
      </div>
    </div>
  );
}

/**
 * Universal Tabs Bar Skeleton
 */
export function TabsSkeleton({ count = 3 }: { count?: number }) {
  return (
    <div
      className="tabs-container skeleton-blink"
      style={{
        display: 'flex',
        gap: '8px',
        marginBottom: '20px',
        borderBottom: '1.5px solid var(--border-light)',
        paddingBottom: '8px',
        height: '45px'
      }}
    >
      {Array.from({ length: count }).map((_, i) => (
        <div
          key={i}
          style={{ width: '100px', height: '30px', background: 'var(--bg-soft)', borderRadius: '4px' }}
        />
      ))}
    </div>
  );
}

/**
 * Universal Table View Skeleton
 */
export function TableSkeleton({ rows = 5 }: { rows?: number }) {
  return (
    <div
      className="card skeleton-blink"
      style={{
        background: 'var(--surface)',
        borderRadius: 'var(--radius-lg)',
        border: '1px solid var(--border-light)',
        overflow: 'hidden'
      }}
    >
      <div
        style={{
          padding: '16px 20px',
          borderBottom: '1px solid var(--border-light)',
          height: '56px',
          display: 'flex',
          alignItems: 'center'
        }}
      >
        <div style={{ width: '220px', height: '16px', background: 'var(--bg-soft)', borderRadius: '4px' }} />
      </div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {Array.from({ length: rows }).map((_, i) => (
          <div
            key={i}
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              height: '36px',
              borderBottom: '1px solid var(--border-light)'
            }}
          >
            <div style={{ width: '150px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }} />
            <div style={{ width: '80px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }} />
            <div style={{ width: '60px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }} />
          </div>
        ))}
      </div>
    </div>
  );
}
