'use client';

import useSWR, { mutate as globalMutate } from 'swr';
import { useAuth } from '@/context/AuthContext';
import { fetchWithToken } from '@/lib/swrFetcher';

/**
 * Shared SWR hook for Admin Batches reference data (/api/admin/batches)
 */
export function useAdminBatches<TBatch = any, TStudent = any>(options?: { enabled?: boolean }) {
  const { firebaseUser } = useAuth();
  const enabled = options?.enabled ?? true;

  const swrKey = firebaseUser && enabled ? '/api/admin/batches' : null;

  const { data, error, isLoading, isValidating, mutate } = useSWR<any>(
    swrKey,
    (url: string) => fetchWithToken(url, firebaseUser),
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000, // 1 minute client cache
      keepPreviousData: true
    }
  );

  return {
    batches: ((data?.batches || []) as TBatch[]),
    students: ((data?.students || []) as TStudent[]),
    raw: data,
    isLoading: !data && !error && isLoading,
    isValidating,
    error: error?.message || null,
    mutate
  };
}

/**
 * Shared SWR hook for Admin Students reference data (/api/admin/students)
 */
export function useAdminStudents<TStudent = any, TBatch = any>(options?: { enabled?: boolean; studentCode?: string }) {
  const { firebaseUser } = useAuth();
  const enabled = options?.enabled ?? true;
  const studentCode = options?.studentCode;

  const url = studentCode 
    ? `/api/admin/students?studentCode=${encodeURIComponent(studentCode)}`
    : '/api/admin/students';

  const swrKey = firebaseUser && enabled ? url : null;

  const { data, error, isLoading, isValidating, mutate } = useSWR<any>(
    swrKey,
    (fetchUrl: string) => fetchWithToken(fetchUrl, firebaseUser),
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000, // 1 minute client cache
      keepPreviousData: true
    }
  );

  return {
    students: ((data?.students || []) as TStudent[]),
    batches: ((data?.batches || []) as TBatch[]),
    alerts: data?.alerts || [],
    raw: data,
    isLoading: !data && !error && isLoading,
    isValidating,
    error: error?.message || null,
    mutate
  };
}

/**
 * Shared SWR hook for Admin Syllabus reference data (/api/admin/syllabus)
 */
export function useAdminSyllabus(options?: { enabled?: boolean; subjectId?: string }) {
  const { firebaseUser } = useAuth();
  const enabled = options?.enabled ?? true;
  const subjectId = options?.subjectId;

  const url = subjectId 
    ? `/api/admin/syllabus?subjectId=${encodeURIComponent(subjectId)}`
    : '/api/admin/syllabus';

  const swrKey = firebaseUser && enabled ? url : null;

  const { data, error, isLoading, isValidating, mutate } = useSWR<any>(
    swrKey,
    (fetchUrl: string) => fetchWithToken(fetchUrl, firebaseUser),
    {
      revalidateOnFocus: false,
      dedupingInterval: 120000, // 2 minutes client cache
      keepPreviousData: true
    }
  );

  return {
    syllabusList: Array.isArray(data) ? data : (data?.syllabusList || []),
    subjectData: Array.isArray(data) ? null : data,
    raw: data,
    isLoading: !data && !error && isLoading,
    isValidating,
    error: error?.message || null,
    mutate
  };
}

const SYLLABUS_SUBJECT_CLIENT_CACHE = new Map<string, { data: any; timestamp: number }>();

export async function fetchCachedSyllabusSubject(subjectId: string, firebaseUser: any) {
  if (!subjectId || !firebaseUser) return null;
  const cached = SYLLABUS_SUBJECT_CLIENT_CACHE.get(subjectId);
  if (cached && Date.now() - cached.timestamp < 120000) {
    return cached.data;
  }
  const data = await fetchWithToken(`/api/admin/syllabus?subjectId=${encodeURIComponent(subjectId)}`, firebaseUser);
  if (data) {
    SYLLABUS_SUBJECT_CLIENT_CACHE.set(subjectId, { data, timestamp: Date.now() });
  }
  return data;
}

/**
 * Invalidate all admin reference caches after a mutation
 */
export function invalidateAdminReferenceData(target?: 'batches' | 'students' | 'syllabus' | 'all') {
  if (!target || target === 'all' || target === 'syllabus') {
    SYLLABUS_SUBJECT_CLIENT_CACHE.clear();
  }
  if (!target || target === 'all') {
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/batches'));
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/students'));
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/syllabus'));
  } else if (target === 'batches') {
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/batches'));
  } else if (target === 'students') {
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/students'));
  } else if (target === 'syllabus') {
    globalMutate((key: any) => typeof key === 'string' && key.startsWith('/api/admin/syllabus'));
  }
}
