'use client';

import React from 'react';
import { PageShell, PageShellProps } from '@/components/common/PageShell';

export type StudentPageShellProps = Omit<PageShellProps, 'role'>;

export function StudentPageShell(props: StudentPageShellProps) {
  return <PageShell role="student" {...props} />;
}

export default StudentPageShell;
