'use client';

import React from 'react';
import { SWRConfig } from 'swr';
import { FetchError } from '@/lib/swrFetcher';

export default function SWRProvider({ children }: { children: React.ReactNode }) {
  return (
    <SWRConfig
      value={{
        revalidateOnFocus: false,
        revalidateOnReconnect: false,
        dedupingInterval: 60000,
        onErrorRetry: (error: any, key: string, config: any, revalidate: any, { retryCount }: { retryCount: number }) => {
          const status = error?.status || (error instanceof FetchError ? error.status : undefined);

          // 1. 4xx Client Errors (401, 403, 404, 400, etc.) -> NEVER retry
          if (status && status >= 400 && status < 500) {
            return;
          }

          // 2. 5xx Server / Network Errors -> Limited to max 2 retries
          if (retryCount >= 2) {
            return;
          }

          // Retry with exponential backoff (e.g. 3s, 6s)
          const delay = Math.min(3000 * Math.pow(2, retryCount), 15000);
          setTimeout(() => revalidate({ retryCount }), delay);
        }
      }}
    >
      {children}
    </SWRConfig>
  );
}
