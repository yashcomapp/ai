/**
 * Canonical Batch Type Definitions (SSOT).
 */

export interface Batch {
  id: string;
  name: string;
  description?: string;
  desc?: string;
  subject?: string;
  subjects?: string;
  board?: string;
  class?: string;
  className?: string;
  classNum?: string;
  timing?: string;
  days?: string[];
  status?: string;
  studentCount?: number;
  rollPrefix?: string;
  academicYear?: string;
  zoomMeetingNumber?: string;
  zoomMeetingPasscode?: string;
  zoomMeetingActive?: boolean;
  createdAt?: any;
  updatedAt?: any;
  [key: string]: any;
}
