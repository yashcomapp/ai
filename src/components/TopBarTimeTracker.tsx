'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { formatDurationHM } from '@/lib/dateUtils';

interface TimeLogStats {
  todaySeconds: number;
  thisWeekSeconds: number;
  lastWeekSeconds: number;
  pctChange: number;
  trend: 'up' | 'down' | 'flat';
  todayTrend: 'up' | 'down' | 'flat';
  todayPct: number;
}

interface TopBarTimeTrackerProps {
  targetUid?: string;
}

export default function TopBarTimeTracker({ targetUid }: TopBarTimeTrackerProps) {
  const { firebaseUser } = useAuth();
  const [stats, setStats] = useState<TimeLogStats | null>(null);
  const [extraSeconds, setExtraSeconds] = useState(0);

  useEffect(() => {
    if (!firebaseUser) return;

    const fetchStats = async () => {
      try {
        const idToken = await firebaseUser.getIdToken();
        let url = '/api/user/time-log';
        if (targetUid) {
          url += `?uid=${targetUid}`;
        }
        const res = await fetch(url, {
          headers: {
            'Authorization': `Bearer ${idToken}`
          }
        });
        if (res.ok) {
          const data = await res.json();
          setStats(data);
          setExtraSeconds(0);
        }
      } catch (e) {
        console.warn('Failed to fetch topbar time stats:', e);
      }
    };

    fetchStats();
  }, [firebaseUser, targetUid]);

  useEffect(() => {
    if (targetUid) return;

    const TICK_MS = 1000;
    const timer = setInterval(() => {
      if (document.hasFocus() && document.visibilityState === 'visible') {
        setExtraSeconds(prev => prev + 1);
      }
    }, TICK_MS);

    return () => clearInterval(timer);
  }, [targetUid]);

  const formatTime = formatDurationHM;

  if (!stats) return null;

  const getWeekTrendIcon = () => {
    if (stats.trend === 'up') {
      return <span style={{ color: '#10b981', fontWeight: 800, marginLeft: '4px' }} title={`${stats.pctChange}% more than last week`}>▲</span>;
    }
    if (stats.trend === 'down') {
      return <span style={{ color: '#ef4444', fontWeight: 800, marginLeft: '4px' }} title={`${Math.abs(stats.pctChange)}% less than last week`}>▼</span>;
    }
    return <span style={{ color: '#6b7280', fontWeight: 800, marginLeft: '4px' }} title="About the same as last week">▪</span>;
  };

  const getTodayTrendIcon = () => {
    if (stats.todayTrend === 'up') {
      return <span style={{ color: '#10b981', fontWeight: 800, marginLeft: '4px' }} title={`${stats.todayPct}% more than yesterday`}>▲</span>;
    }
    if (stats.todayTrend === 'down') {
      return <span style={{ color: '#ef4444', fontWeight: 800, marginLeft: '4px' }} title={`${Math.abs(stats.todayPct)}% less than yesterday`}>▼</span>;
    }
    return <span style={{ color: '#6b7280', fontWeight: 800, marginLeft: '4px' }} title="About the same as yesterday">▪</span>;
  };

  return (
    <>
      <style>{`
        @media (max-width: 480px) {
          .topbar-time-tracker {
            padding: 3px 8px !important;
            font-size: 10px !important;
          }
          .topbar-time-tracker-week,
          .topbar-time-tracker-dot {
            display: none !important;
          }
        }
      `}</style>
      <div className="topbar-time-tracker" style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '5px',
        fontSize: '11px',
        fontWeight: 600,
        background: 'var(--bg-soft)',
        color: 'var(--text)',
        padding: '4px 10px',
        borderRadius: '20px',
        border: '1px solid var(--border-light)',
        flexShrink: 0
      }}>
        <span>⏱️ <strong>{formatTime(stats.todaySeconds + extraSeconds)}</strong>{getTodayTrendIcon()}</span>
        <span className="topbar-time-tracker-dot" style={{ color: 'var(--text-muted)', opacity: 0.5 }}>•</span>
        <span className="topbar-time-tracker-week">W: <strong>{formatTime(stats.thisWeekSeconds + extraSeconds)}</strong>{getWeekTrendIcon()}</span>
      </div>
    </>
  );
}
