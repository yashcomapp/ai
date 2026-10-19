'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { AlertTriangle, CheckCircle2, ChevronRight } from 'lucide-react';
import { ReviewItem } from './types';

interface ParentActionLedgerProps {
  selectedChildCode: string;
  pendingReviews: ReviewItem[];
}

export const ParentActionLedger = React.memo(function ParentActionLedger({
  selectedChildCode,
  pendingReviews
}: ParentActionLedgerProps) {
  const router = useRouter();
  const hasPending = pendingReviews.length > 0;
  const firstPending = pendingReviews[0];

  const handleActionClick = () => {
    if (hasPending && firstPending) {
      const targetTab = firstPending.type === 'practice' 
        ? 'practice' 
        : (firstPending.type === 'subjective' 
          ? 'subjective' 
          : (firstPending.type === 'entrance' ? 'mock' : 'objective'));
      router.push(`/parent/review?child=${selectedChildCode}&tab=${targetTab}${firstPending.id ? `&select=${firstPending.id}` : ''}`);
    } else {
      router.push(`/parent/review?child=${selectedChildCode}`);
    }
  };

  return (
    <div className={hasPending ? "card card-amber" : "card card-emerald"} style={{
      borderRadius: 'var(--radius)',
      padding: '10px 12px',
      marginBottom: '8px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      flexWrap: 'wrap',
      gap: '8px'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
        {hasPending ? (
          <AlertTriangle size={18} color="var(--warning)" style={{ flexShrink: 0 }} />
        ) : (
          <CheckCircle2 size={18} color="var(--success)" style={{ flexShrink: 0 }} />
        )}
        <div>
          <h3 style={{ margin: 0, fontSize: '13.5px', fontWeight: 800, color: hasPending ? 'var(--warning)' : 'var(--success)', lineHeight: 1.25 }}>
            {hasPending 
              ? `${pendingReviews.length} item(s) need attention / आपके ध्यान की आवश्यकता है` 
              : 'All Clear! / सब ठीक है!'}
          </h3>
          <p style={{ margin: '2px 0 0 0', fontSize: '11px', color: 'var(--text-muted)', lineHeight: 1.3 }}>
            {hasPending 
              ? (firstPending?.type === 'absent_exam'
                  ? `Exam absence pending acknowledgment • ${firstPending?.name} • अनुपस्थिति की पुष्टि बाकी`
                  : `Submission pending for review • ${firstPending?.subject || 'Mathematics'} • पालक जांच/समीक्षा बाकी`)
              : 'All exam paper reviews are completed / सभी टेस्ट एवं परीक्षाओं की समीक्षा पूरी है।'}
          </p>
        </div>
      </div>

      <div>
        {hasPending ? (
          <button
            className="btn btn-primary"
            onClick={handleActionClick}
            style={{
              padding: '6px 14px',
              borderRadius: '16px',
              fontSize: '11.5px',
              fontWeight: 800,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}
          >
            <span>{firstPending?.type === 'absent_exam' ? 'Acknowledge Now / अभी पुष्टि करें' : 'Review Now / अभी चेक करें'}</span>
            <ChevronRight size={12} />
          </button>
        ) : (
          <button
            className="btn btn-secondary"
            onClick={() => router.push(`/parent/review?child=${selectedChildCode}`)}
            style={{ padding: '5px 12px', fontSize: '11px', borderRadius: '16px', fontWeight: 700 }}
          >
            View History / इतिहास देखें <ChevronRight size={12} style={{ display: 'inline', verticalAlign: 'middle' }} />
          </button>
        )}
      </div>
    </div>
  );
});
