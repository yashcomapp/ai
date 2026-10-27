import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';

export interface DocIdPageOptions {
  selectFields?: string[];
  cursor?: string | null;
  limit?: number;
}

export interface DocIdPageResult {
  docs: admin.firestore.QueryDocumentSnapshot[];
  nextCursor: string | null;
  hasMore: boolean;
  totalReturned: number;
}

/**
 * Fetches a single page of documents ordered by documentId()
 */
export async function fetchPageByDocId(
  collectionName: string,
  options?: DocIdPageOptions
): Promise<DocIdPageResult> {
  const limit = options?.limit || 500;
  let q: admin.firestore.Query = adminDb.collection(collectionName);
  if (options?.selectFields && options.selectFields.length > 0) {
    q = q.select(...options.selectFields);
  }
  q = q.orderBy(admin.firestore.FieldPath.documentId()).limit(limit);
  if (options?.cursor) {
    q = q.startAfter(options.cursor);
  }

  const snap = await q.get();
  const hasMore = snap.docs.length === limit;
  const nextCursor = hasMore && snap.docs.length > 0 ? snap.docs[snap.docs.length - 1].id : null;

  return {
    docs: snap.docs,
    nextCursor,
    hasMore,
    totalReturned: snap.docs.length,
  };
}

export interface FetchAllByDocIdRangeOptions {
  selectFields?: string[];
  chunkSize?: number;
  maxLimit?: number;
  onChunk?: (docs: admin.firestore.QueryDocumentSnapshot[]) => Promise<void> | void;
}

/**
 * Iterates through an entire Firestore collection using document ID ranges in safe chunks
 * to avoid unbounded single-query memory spikes and prevent silent truncation.
 */
export async function fetchAllByDocIdRange(
  collectionName: string,
  options?: FetchAllByDocIdRangeOptions
): Promise<admin.firestore.QueryDocumentSnapshot[]> {
  const chunkSize = options?.chunkSize || 500;
  const allDocs: admin.firestore.QueryDocumentSnapshot[] = [];
  let cursor: string | null = null;
  let hasMore = true;

  while (hasMore) {
    const page = await fetchPageByDocId(collectionName, {
      selectFields: options?.selectFields,
      cursor,
      limit: chunkSize,
    });

    if (page.docs.length === 0) {
      break;
    }

    if (options?.onChunk) {
      await options.onChunk(page.docs);
    }

    allDocs.push(...page.docs);

    if (!page.hasMore || (options?.maxLimit && allDocs.length >= options.maxLimit)) {
      hasMore = false;
    } else {
      cursor = page.nextCursor;
    }
  }

  return options?.maxLimit ? allDocs.slice(0, options.maxLimit) : allDocs;
}

function parsePaginationParams(reqUrl: string, defaultLimit = 500, maxLimit = 1000) {
  const { searchParams } = new URL(reqUrl);
  const cursor = searchParams.get('cursor');
  const limitParam = searchParams.get('limit');
  const isPaginated = cursor !== null || limitParam !== null;
  const limit = limitParam ? Math.min(Math.max(parseInt(limitParam, 10) || defaultLimit, 1), maxLimit) : defaultLimit;

  return { cursor, limit, isPaginated };
}

export async function fetchCollectionWithPagination(
  collectionName: string,
  reqUrl: string,
  selectFields?: string[]
) {
  const { cursor, limit, isPaginated } = parsePaginationParams(reqUrl);
  if (isPaginated) {
    const page = await fetchPageByDocId(collectionName, { cursor, limit, selectFields });
    return {
      docs: page.docs,
      hasMore: page.hasMore,
      nextCursor: page.nextCursor,
      isPaginated: true
    };
  } else {
    const docs = await fetchAllByDocIdRange(collectionName, { selectFields, chunkSize: 500 });
    return {
      docs,
      hasMore: false,
      nextCursor: null,
      isPaginated: false
    };
  }
}
