/**
 * Centralized Markdown & Mentions Renderer for Yashcom chat systems.
 * Hardened with strict HTML entity escaping and URL scheme whitelisting (XSS prevention).
 */

/**
 * Validates whether a URL uses an approved, safe scheme (http, https, mailto, tel, or safe base64 media).
 * Blocks javascript:, vbscript:, data:text/html, and other arbitrary script execution vectors.
 */
export function isSafeUrl(rawUrl: string): boolean {
  if (!rawUrl) return false;
  const trimmed = rawUrl.trim();

  // Reject any url containing quotes, angle brackets, or whitespace
  if (/[\s"'<>]/.test(trimmed)) return false;

  // Reject any control characters
  if (/[\u0000-\u001f\u007f-\u009f]/.test(trimmed)) return false;

  // Explicitly block dangerous schemes even if obfuscated
  if (/^(javascript|vbscript|data):/i.test(trimmed)) {
    // Only allow specific safe base64 media data URIs (images / PDFs)
    if (/^data:(image\/(png|jpeg|jpg|webp|gif)|application\/pdf);base64,[A-Za-z0-9+/=]+$/i.test(trimmed)) {
      return true;
    }
    return false;
  }

  // Whitelist safe web and communication protocols
  if (/^(https?:\/\/|mailto:|tel:)/i.test(trimmed)) {
    return true;
  }

  // Safe root-relative internal links
  if (/^\/[a-zA-Z0-9_.\-\/?=&#%]+$/.test(trimmed)) {
    return true;
  }

  return false;
}

export function renderMarkdown(text: string, participantNames: Record<string, string> = {}): string {
  if (!text) return '';

  // 1. Initial comprehensive HTML entity escaping
  let escaped = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');

  // 2. Style mentions/tags
  Object.values(participantNames).forEach(name => {
    if (!name) return;
    const tagRegex = new RegExp(`@${name.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&')}\\b`, 'gi');
    escaped = escaped.replace(tagRegex, `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@${name}</span>`);
  });

  // 3. Fallback for student codes / uids / emails if written as @ST-2026-000005
  escaped = escaped.replace(/@(ST-[0-9-]+)\b/gi, (match, code) => {
    const name = participantNames[code.toUpperCase()] || code;
    return `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@${name}</span>`;
  });

  // 4. Handle @admin
  escaped = escaped.replace(/@admin\b/gi, `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@Admin</span>`);

  // 5. Basic markdown formatting
  escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  escaped = escaped.replace(/\*(.*?)\*/g, '<em>$1</em>');
  escaped = escaped.replace(/`(.*?)`/g, '<code style="background: var(--bg-soft); padding: 2px 4px; border-radius: 4px; font-family: monospace;">$1</code>');

  // 6. Markdown links [label](url) with strict URL scheme validation
  escaped = escaped.replace(/\[(.*?)\]\((.*?)\)/g, (match, label, rawUrl) => {
    const cleanUrl = rawUrl
      .replace(/&amp;/g, '&')
      .replace(/&quot;/g, '"')
      .replace(/&#039;/g, "'")
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>');

    if (isSafeUrl(cleanUrl)) {
      const safeHref = encodeURI(cleanUrl).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
      return `<a href="${safeHref}" target="_blank" rel="noopener noreferrer" style="color: var(--secondary, #4a88d9); text-decoration: underline; font-weight: 600;">${label}</a>`;
    }
    // Disallowed scheme (e.g. javascript:, vbscript:, data:text/html) -> render as safe escaped text
    return `[${label}](${rawUrl})`;
  });

  // 7. Plain text autolinks with strict URL validation
  escaped = escaped.replace(/(?<!href=")(https?:\/\/[^\s<"']+)/g, (match, rawUrl) => {
    const cleanUrl = rawUrl
      .replace(/&amp;/g, '&')
      .replace(/&quot;/g, '"')
      .replace(/&#039;/g, "'")
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>');

    if (isSafeUrl(cleanUrl)) {
      const safeHref = encodeURI(cleanUrl).replace(/"/g, '&quot;').replace(/'/g, '&#039;');
      return `<a href="${safeHref}" target="_blank" rel="noopener noreferrer" style="color: var(--secondary, #4a88d9); text-decoration: underline; font-weight: 600;">${rawUrl}</a>`;
    }
    return rawUrl;
  });

  escaped = escaped.replace(/\n/g, '<br/>');
  return escaped;
}
