import DOMPurify from 'dompurify';

let hookConfigured = false;

function ensurePurifyHooks() {
  if (hookConfigured || typeof window === 'undefined') return;
  DOMPurify.addHook('afterSanitizeAttributes', (node) => {
    if (node.tagName === 'A' && node.hasAttribute('target')) {
      node.setAttribute('rel', 'noopener noreferrer');
    }
  });
  hookConfigured = true;
}

/**
 * Sanitizes rich HTML for safe rendering (notices, descriptions, math labels).
 * Strips script tags, style attributes, and enforces rel="noopener noreferrer".
 */
function sanitizeHtml(dirty: string): string {
  if (!dirty) return '';
  if (typeof window === 'undefined') {
    // Return empty on server to prevent unsanitized HTML in SSR hydration mismatch
    return '';
  }
  ensurePurifyHooks();
  return DOMPurify.sanitize(dirty, {
    ALLOWED_TAGS: [
      'b', 'i', 'em', 'strong', 'a', 'p', 'div', 'span', 'br', 'ul', 'ol', 'li',
      'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
      'blockquote', 'code', 'pre', 'hr', 'sub', 'sup'
    ],
    ALLOWED_ATTR: ['href', 'title', 'target', 'class', 'rel'],
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
