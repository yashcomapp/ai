'use client';

import React, { useEffect, useState } from 'react';

export default function VisitorCounter() {
  const [visitorCount, setVisitorCount] = useState<number | null>(null);

  useEffect(() => {
    const trackVisitor = async () => {
      try {
        const hasVisited = sessionStorage.getItem('learnos_visited');
        let res: Response;
        if (!hasVisited) {
          sessionStorage.setItem('learnos_visited', 'true');
          res = await fetch('/api/visitor-counter', { method: 'POST' });
        } else {
          res = await fetch('/api/visitor-counter');
        }
        if (res.ok) {
          const data = await res.json();
          setVisitorCount(data.count);
        }
      } catch (err) {
        console.error('Failed to load visitor counter:', err);
      }
    };
    trackVisitor();
  }, []);

  if (visitorCount === null) return null;

  return (
    <p style={{ fontSize: '11px', color: 'var(--text-accent)', opacity: 0.85, margin: 0 }}>
      👤 Visitor Count: <span style={{ fontWeight: 800, background: 'var(--badge-bg)', border: '1px solid var(--badge-border)', padding: '2px 8px', borderRadius: '12px' }}>{visitorCount}</span>
    </p>
  );
}
