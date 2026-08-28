'use client';

import React, { Suspense } from 'react';
import dynamic from 'next/dynamic';
const AttendanceManager = dynamic(() => import('@/components/AttendanceManager'), { ssr: false });

export default function ParentAttendancePage() {
  return (
    <Suspense fallback={<div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading...</div>}>
      <AttendanceManager role="parent" />
    </Suspense>
  );
}
