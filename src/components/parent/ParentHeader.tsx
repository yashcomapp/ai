'use client';

import React from 'react';
import Image from 'next/image';
import { useRouter } from 'next/navigation';
import { Bell, LogOut } from 'lucide-react';

interface ParentHeaderProps {
  pendingReviewsCount: number;
  onOpenNotifications: () => void;
  onLogout: () => void;
}

export const ParentHeader = React.memo(function ParentHeader({
  pendingReviewsCount,
  onOpenNotifications,
  onLogout
}: ParentHeaderProps) {
  const router = useRouter();

  return (
    <div className="page-header glass" style={{ 
      padding: '12px 20px', 
      display: 'flex', 
      justifyContent: 'space-between', 
      alignItems: 'center', 
      borderBottom: '1px solid var(--border)',
      background: 'var(--surface-glass)',
      backdropFilter: 'blur(16px)',
      WebkitBackdropFilter: 'blur(16px)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <div 
          onClick={() => router.push('/parent')} 
          style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}
        >
          <Image 
            src="/logo.png" 
            alt="YASHCOM Logo" 
            width={28}
            height={28}
            style={{ borderRadius: '50%', objectFit: 'cover' }} 
            priority
          />
          <span style={{ fontWeight: 900, fontSize: '1.2rem', letterSpacing: '0.5px', color: 'var(--text)' }}>
            YASHCOM
          </span>
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
        {/* Notifications Bell Icon Button */}
        <button 
          onClick={onOpenNotifications}
          style={{ 
            position: 'relative', 
            background: 'rgba(255,255,255,0.05)', 
            border: '1px solid var(--border-light)', 
            borderRadius: '50%', 
            width: '38px', 
            height: '38px', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            color: 'var(--text)', 
            cursor: 'pointer'
          }}
          title="Notifications"
        >
          <Bell size={18} />
          {pendingReviewsCount > 0 && (
            <span style={{
              position: 'absolute',
              top: '-2px',
              right: '-2px',
              background: 'var(--danger)',
              color: 'white',
              fontSize: '10px',
              fontWeight: 800,
              width: '18px',
              height: '18px',
              borderRadius: '50%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              border: '2px solid var(--surface-popover)'
            }}>
              {pendingReviewsCount}
            </span>
          )}
        </button>

        {/* User Profile / Logout */}
        <button 
          onClick={onLogout} 
          style={{ 
            background: 'rgba(255,255,255,0.05)', 
            border: '1px solid var(--border-light)', 
            borderRadius: '50%', 
            width: '38px', 
            height: '38px', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            color: 'var(--danger)', 
            cursor: 'pointer'
          }}
          title="Logout"
        >
          <LogOut size={18} />
        </button>
      </div>
    </div>
  );
});
