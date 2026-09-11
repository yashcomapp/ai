'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function FeesJournalRedirectPage() {
  const router = useRouter();

  useEffect(() => {
    router.replace('/admin/fees?tab=journal');
  }, [router]);

  return null;
}
