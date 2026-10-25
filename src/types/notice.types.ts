/**
 * Canonical Notice Type Definitions (SSOT).
 */

export interface Notice {
  id: string;
  title: string;
  body: string;
  createdAt: string | null;
  createdBy?: string;
  targetType?: string;
  targetValues?: string[];
  isOverlay?: boolean;
  type?: string;
  noticeDate?: string | null;
  [key: string]: any;
}
