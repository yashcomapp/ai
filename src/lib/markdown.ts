/**
 * Centralized Markdown & Mentions Renderer for Yashcom chat systems.
 */
export function renderMarkdown(text: string, participantNames: Record<string, string> = {}) {
  if (!text) return '';
  let escaped = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
  
  // Style mentions/tags
  Object.values(participantNames).forEach(name => {
    if (!name) return;
    const tagRegex = new RegExp(`@${name.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&')}\\b`, 'gi');
    escaped = escaped.replace(tagRegex, `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@${name}</span>`);
  });
  
  // Also fallback for student codes / uids / emails if written as @ST-2026-000005
  escaped = escaped.replace(/@(ST-[0-9-]+)\b/gi, (match, code) => {
    const name = participantNames[code.toUpperCase()] || code;
    return `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@${name}</span>`;
  });

  // Handle @admin
  escaped = escaped.replace(/@admin\b/gi, `<span style="color: #facc15; font-weight: 700; background: rgba(250,204,21,0.12); padding: 1px 5px; border-radius: 4px;">@Admin</span>`);
  
  escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  escaped = escaped.replace(/\*(.*?)\*/g, '<em>$1</em>');
  escaped = escaped.replace(/`(.*?)`/g, '<code style="background: var(--bg-soft); padding: 2px 4px; border-radius: 4px; font-family: monospace;">$1</code>');
  escaped = escaped.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" style="color: #60a5fa; text-decoration: underline; font-weight: 600;">$1</a>');
  escaped = escaped.replace(/(?<!href=")(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener noreferrer" style="color: #60a5fa; text-decoration: underline; font-weight: 600;">$1</a>');
  escaped = escaped.replace(/\n/g, '<br/>');
  return escaped;
}
