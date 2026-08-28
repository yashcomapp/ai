/**
 * Canonical Date & Time Utilities for YASHCOM Learning OS
 * GUARANTEED Timezone: IST (Asia/Kolkata, UTC+05:30) everywhere across client and server.
 */

export const IST_TIMEZONE = 'Asia/Kolkata';

/**
 * Formats a Date/Timestamp into 12-hour or 24-hour time string in IST
 * Example: "05:09 PM" or "5:09 pm"
 */
export function formatTimeIST(
  dateInput?: Date | string | number | null,
  options?: { hour12?: boolean; uppercase?: boolean }
): string {
  if (!dateInput) return '';
  const d = new Date(dateInput);
  if (isNaN(d.getTime())) return '';

  const formatted = d.toLocaleTimeString('en-IN', {
    timeZone: IST_TIMEZONE,
    hour: '2-digit',
    minute: '2-digit',
    hour12: options?.hour12 !== false
  });

  return options?.uppercase !== false ? formatted : formatted.toLowerCase();
}

/**
 * Formats a Date/Timestamp into date string in IST
 * Example: "20/07/2026"
 */
export function formatDateIST(dateInput?: Date | string | number | null): string {
  if (!dateInput) return '';
  const d = new Date(dateInput);
  if (isNaN(d.getTime())) return '';

  const day = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, day: 'numeric' })).padStart(2, '0');
  const month = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, month: 'numeric' })).padStart(2, '0');
  const year = d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, year: 'numeric' });
  return `${day}/${month}/${year}`;
}

/**
 * Formats full Date & Time in IST
 * Example: "20/07/2026, 05:09 PM"
 */
export function formatDateTimeIST(dateInput?: Date | string | number | null): string {
  if (!dateInput) return '';
  const d = new Date(dateInput);
  if (isNaN(d.getTime())) return '';

  const day = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, day: 'numeric' })).padStart(2, '0');
  const month = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, month: 'numeric' })).padStart(2, '0');
  const year = d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, year: 'numeric' });
  
  const timeStr = d.toLocaleTimeString('en-IN', {
    timeZone: IST_TIMEZONE,
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  });

  return `${day}/${month}/${year}, ${timeStr}`;
}

/**
 * Returns YYYY-MM-DD date key strictly computed in IST (Asia/Kolkata)
 */
export function getDateKeyIST(dateInput?: Date | string | number | null): string {
  const d = dateInput ? new Date(dateInput) : new Date();
  if (isNaN(d.getTime())) {
    const now = new Date();
    return now.toLocaleDateString('en-CA', { timeZone: IST_TIMEZONE });
  }
  return d.toLocaleDateString('en-CA', { timeZone: IST_TIMEZONE });
}

/**
 * Formats a Firestore/JS timestamp into relative time string in IST
 * Example: "Just now", "5m ago", "2h ago", or "20/07/2026, 05:09 PM"
 */
export function formatLastActiveIST(lastActiveAt: any): string {
  if (!lastActiveAt) return 'Never';
  const date = lastActiveAt.seconds 
    ? new Date(lastActiveAt.seconds * 1000) 
    : new Date(lastActiveAt);
  if (isNaN(date.getTime())) return 'Never';
  
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffMins = Math.floor(diffMs / 60000);
  
  if (diffMins < 1) return 'Just now';
  if (diffMins < 60) return `${diffMins}m ago`;
  
  const diffHours = Math.floor(diffMins / 60);
  if (diffHours < 24) return `${diffHours}h ago`;
  
  const day = String(date.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, day: 'numeric' })).padStart(2, '0');
  const month = String(date.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, month: 'numeric' })).padStart(2, '0');
  const year = date.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, year: 'numeric' });
  const timeStr = date.toLocaleTimeString('en-IN', {
    timeZone: IST_TIMEZONE,
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  });

  return `${day}/${month}/${year}, ${timeStr}`;
}

/**
 * Formats a Date/Timestamp into standard DD/MM/YYYY format in IST
 */
export function formatDateDMY(dateInput?: Date | string | number | null): string {
  if (!dateInput) return '--';
  // If it's already a YYYY-MM-DD string, quickly split and format to avoid Date parsing issues
  if (typeof dateInput === 'string') {
    const parts = dateInput.split('T')[0].split('-');
    if (parts.length === 3 && parts[0].length === 4) {
      return `${parts[2]}/${parts[1]}/${parts[0]}`;
    }
  }
  try {
    const d = new Date(dateInput);
    if (!isNaN(d.getTime())) {
      const day = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, day: 'numeric' })).padStart(2, '0');
      const month = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, month: 'numeric' })).padStart(2, '0');
      const year = d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, year: 'numeric' });
      return `${day}/${month}/${year}`;
    }
  } catch (e) {}
  return String(dateInput);
}

/**
 * Formats duration in seconds into MM:SS (e.g. 05:32) or HH:MM:SS (e.g. 01:05:32)
 */
export function formatDuration(seconds: number, options?: { padMinutes?: boolean }): string {
  if (isNaN(seconds) || seconds <= 0) return '00:00';
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = Math.floor(seconds % 60);

  const padMins = options?.padMinutes !== false;
  const minsStr = padMins ? String(mins).padStart(2, '0') : String(mins);
  const secsStr = String(secs).padStart(2, '0');

  if (hrs > 0) {
    return `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${secsStr}`;
  }
  return `${minsStr}:${secsStr}`;
}

/**
 * Formats duration in seconds into human-readable hours and minutes
 * Example: "1h 30m" or "45m"
 */
export function formatDurationHM(totalSeconds: number): string {
  if (isNaN(totalSeconds) || totalSeconds <= 0) return '0m';
  const mins = Math.round(totalSeconds / 60);
  if (mins < 60) return `${mins}m`;
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  return m > 0 ? `${h}h ${m}m` : `${h}h`;
}

/**
 * Formats any Date/Timestamp into YYYY-MM-DDTHH:mm string for datetime-local inputs in IST
 */
export function toISTDateTimeLocalInput(dateInput?: any): string {
  if (!dateInput) return '';
  let d: Date;
  if (dateInput?.toDate && typeof dateInput.toDate === 'function') {
    d = dateInput.toDate();
  } else if (dateInput?._seconds) {
    d = new Date(dateInput._seconds * 1000);
  } else if (dateInput?.seconds) {
    d = new Date(dateInput.seconds * 1000);
  } else {
    d = new Date(dateInput);
  }
  if (isNaN(d.getTime())) return '';

  const day = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, day: 'numeric' })).padStart(2, '0');
  const month = String(d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, month: 'numeric' })).padStart(2, '0');
  const year = d.toLocaleDateString('en-US', { timeZone: IST_TIMEZONE, year: 'numeric' });
  const timeStr = d.toLocaleTimeString('en-GB', {
    timeZone: IST_TIMEZONE,
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  });

  return `${year}-${month}-${day}T${timeStr}`;
}

/**
 * Converts a date string in YYYY-MM-DD or ISO to DD/MM/YYYY
 */
export function formatToDDMMYYYY(val?: string | null): string {
  if (!val) return '';
  const clean = String(val).trim();
  if (/^\d{2}\/\d{2}\/\d{4}$/.test(clean)) return clean;
  if (/^\d{4}-\d{2}-\d{2}$/.test(clean)) {
    const [y, m, d] = clean.split('-');
    return `${d}/${m}/${y}`;
  }
  const d = new Date(val);
  if (!isNaN(d.getTime())) {
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    return `${day}/${month}/${d.getFullYear()}`;
  }
  return clean;
}

/**
 * Converts a date string in DD/MM/YYYY to YYYY-MM-DD
 */
export function formatToYYYYMMDD(val?: string | null): string {
  if (!val) return '';
  const clean = String(val).trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(clean)) return clean;
  if (/^\d{2}\/\d{2}\/\d{4}$/.test(clean)) {
    const [d, m, y] = clean.split('/');
    return `${y}-${m}-${d}`;
  }
  return clean;
}
