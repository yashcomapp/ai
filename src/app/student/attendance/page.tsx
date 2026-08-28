'use client';

import React, { Suspense } from 'react';
import dynamic from 'next/dynamic';
const AttendanceManager = dynamic(() => import('@/components/AttendanceManager'), { ssr: false });

export default function StudentAttendancePage() {
  return (
    <Suspense fallback={<div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading...</div>}>
      <AttendanceManager role="student" />
    </Suspense>
  );
}
