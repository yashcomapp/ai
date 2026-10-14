import DOMPurify from 'dompurify';

/**
 * Sanitizes rich HTML for safe rendering (notices, descriptions, math labels).
 * Strips script tags, onerror/onload attributes, and javascript: URIs.
 */
export function sanitizeHtml(dirty: string): string {
  if (!dirty) return '';
  if (typeof window === 'undefined') {
    // Basic server fallback escaping script/iframe/event handlers
    return dirty
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
      .replace(/\bon\w+\s*=\s*["'][^"']*["']/gi, '')
      .replace(/\bon\w+\s*=\s*[^>\s]+/gi, '')
      .replace(/javascript:/gi, '');
  }
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: [
      'b', 'i', 'em', 'strong', 'a', 'p', 'div', 'span', 'br', 'ul', 'ol', 'li',
      'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
      'blockquote', 'code', 'pre', 'hr', 'sub', 'sup'
    ],
    ALLOWED_ATTR: ['href', 'title', 'target', 'class', 'style', 'rel'],
    ALLOWED_URI_REGEXP: /^(?:(?:https?|mailto):|[^a-z]|[a-z+.\-]+(?:[^a-z+.\-:]|$))/i
  });
}

/**
 * Specifically sanitizes notice body text, ensuring safe HTML with line-break handling.
 */
export function sanitizeNoticeHtml(rawText: string): string {
  if (!rawText) return '';
  let formatted = rawText;
  formatted = formatted.replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1');
  formatted = formatted.replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1');
  formatted = formatted.replace(/\r?\n/g, '<br/>');
  return sanitizeHtml(formatted);
}
