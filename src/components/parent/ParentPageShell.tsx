'use client';

import React from 'react';
import { PageShell, PageShellProps } from '@/components/common/PageShell';

export type ParentPageShellProps = Omit<PageShellProps, 'role'>;

export function ParentPageShell(props: ParentPageShellProps) {
  return <PageShell role="parent" {...props} />;
}

export default ParentPageShell;
