'use client';

import React from 'react';
import { formatDateIST } from '@/lib/dateUtils';
import { ParentDashboardData } from './types';

interface DailySyncModalProps {
  isOpen: boolean;
  onClose: () => void;
  syncSecondsRemaining: number;
  formatSyncTimer: (seconds: number) => string;
  dailySyncStep: 1 | 2 | 3;
  setDailySyncStep: (step: 1 | 2 | 3) => void;
  dailySyncFeedback: 'excellent' | 'good' | 'needs_attention';
  setDailySyncFeedback: (fb: 'excellent' | 'good' | 'needs_attention') => void;
  dailySyncSubmitting: boolean;
  handleCompleteDailySync: () => void;
  captureSyncSnapshot: () => Promise<string | null>;
  activeChildName: string;
  childData?: ParentDashboardData | null;
  syncVideoRef: any;
  syncLiveStream: MediaStream | null;
}

export const DailySyncModal = React.memo(function DailySyncModal({
  isOpen,
  onClose,
  syncSecondsRemaining,
  formatSyncTimer,
  dailySyncStep,
  setDailySyncStep,
  dailySyncFeedback,
  setDailySyncFeedback,
  dailySyncSubmitting,
  handleCompleteDailySync,
  captureSyncSnapshot,
  activeChildName,
  childData,
  syncVideoRef,
  syncLiveStream
}: DailySyncModalProps) {
  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'rgba(2, 6, 23, 0.95)',
      zIndex: 11000,
      display: 'flex',
      flexDirection: 'column',
      backdropFilter: 'blur(12px)',
      overflowY: 'auto'
    }}>
      {/* Container Top Bar */}
      <div style={{
        background: 'rgba(0, 0, 0, 0.85)',
        borderBottom: '1px solid rgba(20, 184, 166, 0.3)',
        padding: '12px 20px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{
            width: '36px',
            height: '36px',
            borderRadius: '50%',
            background: 'var(--accent-grad)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '18px'
          }}>
            🎯
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: 'var(--text-white)' }}>
                Daily 5-Min Parent-Kid Sync
              </h3>
              <span style={{ fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px', background: 'var(--accent-soft)', color: 'var(--accent)', border: '1px solid var(--accent-ring)' }}>
                {activeChildName}
              </span>
            </div>
            <p style={{ margin: '2px 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
              A 5-minute ritual to review topics, encourage effort, and verify sincerity.
            </p>
          </div>
        </div>

        {/* Live Proctoring Status Indicator & Lock Badge */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            background: 'rgba(239, 68, 68, 0.15)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            borderRadius: '20px',
            padding: '4px 10px',
            fontSize: '11px',
            color: 'var(--danger-muted)',
            fontWeight: 700
          }}>
            <span style={{
              width: '8px',
              height: '8px',
              borderRadius: '50%',
              background: 'var(--danger)',
              display: 'inline-block'
            }} />
            <span>Live Feed Active (Educator Monitored)</span>
          </div>

          {syncSecondsRemaining > 0 ? (
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              background: 'linear-gradient(135deg, rgba(15, 118, 110, 0.25), rgba(20, 184, 166, 0.25))',
              border: '1px solid rgba(20, 184, 166, 0.5)',
              color: 'var(--accent)',
              borderRadius: '20px',
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 800,
              letterSpacing: '0.5px'
            }}>
              <span>🔒 Mandatory:</span>
              <span style={{ color: 'var(--text-white)', fontFamily: 'monospace', fontSize: '13px' }}>{formatSyncTimer(syncSecondsRemaining)} left</span>
            </div>
          ) : (
            <button 
              onClick={onClose}
              style={{
                background: 'rgba(255, 255, 255, 0.1)',
                border: '1px solid rgba(255, 255, 255, 0.2)',
                color: 'var(--text-white)',
                padding: '8px 16px',
                borderRadius: '20px',
                fontSize: '13px',
                fontWeight: 700,
                cursor: 'pointer'
              }}
            >
              ✕ Close Sync
            </button>
          )}
        </div>
      </div>

      {/* Stepper Progress Line */}
      <div style={{ display: 'flex', background: 'rgba(255,255,255,0.05)', height: '4px' }}>
        <div style={{ flex: 1, background: dailySyncStep >= 1 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
        <div style={{ flex: 1, background: dailySyncStep >= 2 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
        <div style={{ flex: 1, background: dailySyncStep >= 3 ? 'var(--accent)' : 'transparent', transition: 'background 0.3s' }} />
      </div>

      {/* Main Sync Workspace Container */}
      <div style={{
        flex: 1,
        maxWidth: '1100px',
        width: '100%',
        margin: '0 auto',
        padding: '24px 16px',
        display: 'grid',
        gridTemplateColumns: '1fr 320px',
        gap: '24px',
        alignItems: 'start'
      }}>
        
        {/* Left: Interactive Sync Flow (Steps 1, 2, 3) */}
        <div style={{
          background: 'var(--surface)',
          border: '1.5px solid var(--border)',
          borderRadius: 'var(--radius-lg)',
          padding: '24px',
          boxShadow: 'var(--shadow-md)',
          display: 'flex',
          flexDirection: 'column',
          gap: '20px'
        }}>
          
          {/* STEP 1: Current Day Activity */}
          {dailySyncStep === 1 && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
              <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  Step 1 • 60-Second Check
                </span>
                <h2 style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-white)', margin: '4px 0 2px' }}>
                  Today&apos;s Study Effort ({formatDateIST(new Date().toISOString())})
                </h2>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                  Here is what {activeChildName} achieved today. Start by appreciating their consistency!
                </p>
              </div>

              {/* Today's Stats Cards Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '12px' }}>
                {/* Card 1: Today's Practice Time */}
                <div style={{ background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>⏱️ Studied Today</div>
                  <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>
                    {childData?.todayStats?.todayMinutes || Math.round((childData?.snapshot?.todaySeconds || 0) / 60)}m
                  </div>
                  <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Active Practice & Exams</div>
                </div>

                {/* Card 2: Sessions Completed Today */}
                <div style={{ background: 'var(--surface-2)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>📝 Completed Today</div>
                  <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--success)', marginTop: '4px' }}>
                    {childData?.todayStats?.todaySessionsCount || 0}
                  </div>
                  <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Tests / Practice Sets</div>
                </div>

                {/* Card 3: Questions Solved Today */}
                <div style={{ background: 'var(--surface-2)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>✨ Questions Today</div>
                  <div style={{ fontSize: '24px', fontWeight: 800, color: 'var(--accent)', marginTop: '4px' }}>
                    {childData?.todayStats?.todayQuestionsCount || 0}
                  </div>
                  <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Problems Attempted</div>
                </div>

                {/* Card 4: Today's Average Score */}
                <div style={{ background: 'var(--surface-2)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)', padding: '14px', textAlign: 'center' }}>
                  <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>📊 Today&apos;s Accuracy</div>
                  <div style={{ fontSize: '24px', fontWeight: 800, color: (childData?.todayStats?.todayAverageScore || 0) >= 70 ? 'var(--success)' : 'var(--warning)', marginTop: '4px' }}>
                    {childData?.todayStats?.todayAverageScore !== undefined ? `${childData.todayStats.todayAverageScore}%` : '0%'}
                  </div>
                  <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>Today&apos;s Average Score</div>
                </div>
              </div>

              {/* Encouragement Card */}
              <div style={{
                background: 'var(--accent-soft)',
                border: '1px solid var(--accent-border, var(--border-light))',
                borderRadius: 'var(--radius)',
                padding: '14px 18px',
                fontSize: '13px',
                color: 'var(--text)',
                lineHeight: '1.5'
              }}>
                💡 <strong>Parent Encouragement Prompt:</strong> Tell {activeChildName}: <em>&ldquo;I saw you spent {childData?.todayStats?.todayMinutes || 25} minutes practicing today. Great job keeping your {childData?.todayStats?.streakDays || childData?.snapshot?.streakDays || 1}-day streak alive!&rdquo;</em>
              </div>

              <button 
                className="btn" 
                onClick={() => setDailySyncStep(2)}
                style={{
                  background: 'var(--accent-grad)',
                  color: 'var(--text-white)',
                  fontWeight: 700,
                  padding: '12px',
                  borderRadius: 'var(--radius)',
                  border: 'none',
                  cursor: 'pointer',
                  fontSize: '14px',
                  width: '100%',
                  boxShadow: '0 4px 14px rgba(15, 118, 110, 0.3)'
                }}
              >
                Next: Review Diagnostic Movement & Tricky Questions →
              </button>
            </div>
          )}

          {/* STEP 2: Diagnostic Movement & Tricky Questions */}
          {dailySyncStep === 2 && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
              <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  Step 2 • 3-Minute Discussion
                </span>
                <h2 style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-white)', margin: '4px 0 2px' }}>
                  Diagnostic Topic Movement & Tricky Questions
                </h2>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                  Review progress and talk through today&apos;s trickiest question.
                </p>
              </div>

              {/* Diagnostic Topic Movement Breakdown */}
              <div style={{
                background: 'var(--surface-2)',
                border: '1px solid var(--border-light)',
                borderRadius: 'var(--radius)',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                gap: '14px'
              }}>
                <h4 style={{ margin: 0, fontSize: '13px', fontWeight: 800, color: 'var(--text)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  📊 Topic Mastery Diagnostic Movement
                </h4>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
                  {/* Box 1: Needs Attention Yesterday */}
                  <div style={{ background: 'var(--danger-bg)', border: '1px solid var(--danger-border)', borderRadius: '8px', padding: '12px' }}>
                    <div style={{ fontSize: '11px', color: 'var(--danger)', fontWeight: 700 }}>🚨 In Needs Attention (Yesterday)</div>
                    <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--danger)', marginTop: '2px' }}>
                      {childData?.topicDiagnostics?.needsAttentionYesterdayCount || childData?.snapshot?.needsAttentionCount || 0} topics
                    </div>
                  </div>

                  {/* Box 2: Practiced & Removed Today */}
                  <div style={{ background: 'var(--success-bg)', border: '1px solid var(--success-border)', borderRadius: '8px', padding: '12px' }}>
                    <div style={{ fontSize: '11px', color: 'var(--success)', fontWeight: 700 }}>🟢 Practiced & Recovered Today</div>
                    <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--success)', marginTop: '2px' }}>
                      {childData?.topicDiagnostics?.recoveredTodayCount || 0} topics removed
                    </div>
                  </div>

                  {/* Box 3: Remaining in Needs Attention */}
                  <div style={{ background: 'var(--warning-bg)', border: '1px solid var(--warning-border)', borderRadius: '8px', padding: '12px' }}>
                    <div style={{ fontSize: '11px', color: 'var(--warning)', fontWeight: 700 }}>🟡 Remaining Needs Attention</div>
                    <div style={{ fontSize: '22px', fontWeight: 800, color: 'var(--warning)', marginTop: '2px' }}>
                      {childData?.topicDiagnostics?.needsAttentionRemainingCount || 0} topics
                    </div>
                  </div>
                </div>

                {/* Recovered topics tags */}
                {(childData?.topicDiagnostics?.recoveredTodayTopics || []).length > 0 && (
                  <div style={{ marginTop: '4px' }}>
                    <div style={{ fontSize: '11px', color: 'var(--success)', fontWeight: 700, marginBottom: '6px' }}>
                      ✓ Topics successfully practiced and graduated today:
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                      {childData?.topicDiagnostics?.recoveredTodayTopics.map((t, idx) => (
                        <span key={idx} style={{ fontSize: '11px', padding: '3px 10px', borderRadius: '12px', background: 'var(--success-bg)', color: 'var(--success)', border: '1px solid var(--success-border)', fontWeight: 600 }}>
                          ✅ {t}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Tricky Question Spotlight */}
              <div style={{
                background: 'var(--surface-2)',
                border: '1px solid var(--border-light)',
                borderRadius: 'var(--radius)',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                gap: '10px'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: '10px', fontWeight: 700, background: 'var(--danger-bg)', color: 'var(--danger)', padding: '2px 8px', borderRadius: '10px' }}>
                    Tricky Question Spotlight
                  </span>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Daily Mistake Review</span>
                </div>

                <div style={{ fontSize: '13px', color: 'var(--text-white)', fontWeight: 600, lineHeight: '1.4' }}>
                  &ldquo;When solving numerical problems or multi-step derivations, double-check sign inversions and unit conversions.&rdquo;
                </div>

                <div style={{ fontSize: '12px', color: 'var(--text-muted)', background: 'rgba(0,0,0,0.3)', padding: '10px 12px', borderRadius: '6px', lineHeight: '1.4' }}>
                  💡 <strong>Discussion Question for Parent:</strong> Ask {activeChildName}: <em>&ldquo;Which question gave you the most trouble today? How did you figure out the solution?&rdquo;</em>
                </div>
              </div>

              <div style={{ display: 'flex', gap: '10px' }}>
                <button 
                  className="btn btn-secondary" 
                  onClick={() => setDailySyncStep(1)}
                  style={{ flex: 1, padding: '12px', fontSize: '13px' }}
                >
                  ← Back
                </button>
                <button 
                  className="btn" 
                  onClick={() => {
                    setDailySyncStep(3);
                    captureSyncSnapshot();
                  }}
                  style={{
                    flex: 2,
                    background: 'var(--accent-grad)',
                    color: 'var(--text-white)',
                    fontWeight: 700,
                    padding: '12px',
                    borderRadius: 'var(--radius)',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: '13px'
                  }}
                >
                  Next: Complete Parent Signoff →
                </button>
              </div>
            </div>
          )}

          {/* STEP 3: Parent Signoff & Verification */}
          {dailySyncStep === 3 && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '18px' }}>
              <div style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '12px' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  Step 3 • Final Signoff
                </span>
                <h2 style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-white)', margin: '4px 0 2px' }}>
                  Parent Verification & Signoff
                </h2>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', margin: 0 }}>
                  Rate today&apos;s session and sign off. This logs into the educator sincerity report with zero penalty to student LQ.
                </p>
              </div>

              {/* Reaction Selector */}
              <div>
                <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '8px' }}>
                  How did {activeChildName} perform in today&apos;s sync?
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
                  {[
                    { id: 'excellent', label: '🌟 Excellent', desc: 'Deep Focus & Clarity' },
                    { id: 'good', label: '👍 Good', desc: 'Active Discussion' },
                    { id: 'needs_attention', label: '⚠️ Needs Focus', desc: 'Extra Practice Needed' }
                  ].map(r => (
                    <div 
                      key={r.id}
                      onClick={() => setDailySyncFeedback(r.id as any)}
                      style={{
                        background: dailySyncFeedback === r.id ? 'rgba(20, 184, 166, 0.25)' : 'rgba(255,255,255,0.04)',
                        border: dailySyncFeedback === r.id ? '2px solid var(--accent)' : '1px solid rgba(255,255,255,0.1)',
                        padding: '12px 10px',
                        borderRadius: 'var(--radius)',
                        cursor: 'pointer',
                        textAlign: 'center',
                        transition: 'all 0.2s'
                      }}
                    >
                      <div style={{ fontSize: '14px', fontWeight: 800, color: 'var(--text-white)' }}>{r.label}</div>
                      <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>{r.desc}</div>
                    </div>
                  ))}
                </div>
              </div>

              <div style={{ display: 'flex', gap: '10px' }}>
                <button 
                  className="btn btn-secondary" 
                  onClick={() => setDailySyncStep(2)}
                  style={{ flex: 1, padding: '12px', fontSize: '13px' }}
                >
                  ← Back
                </button>
                <button 
                  className="btn" 
                  onClick={handleCompleteDailySync}
                  disabled={dailySyncSubmitting || syncSecondsRemaining > 0}
                  style={{
                    flex: 2,
                    background: syncSecondsRemaining > 0
                      ? 'rgba(255, 255, 255, 0.08)'
                      : 'var(--accent-grad)',
                    color: syncSecondsRemaining > 0 ? 'var(--text-muted)' : 'var(--text-white)',
                    fontWeight: 800,
                    padding: '12px',
                    borderRadius: 'var(--radius)',
                    border: syncSecondsRemaining > 0 ? '1px solid rgba(255,255,255,0.15)' : 'none',
                    cursor: syncSecondsRemaining > 0 ? 'not-allowed' : 'pointer',
                    fontSize: '13px',
                    boxShadow: syncSecondsRemaining > 0 ? 'none' : '0 4px 14px rgba(16, 185, 129, 0.3)'
                  }}
                >
                  {dailySyncSubmitting ? 'Recording Verification...' : syncSecondsRemaining > 0 ? `🔒 Complete 5-Min Sync to Sign (${formatSyncTimer(syncSecondsRemaining)} left)` : '✍️ Sign & Complete Sync'}
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Right: Prominent 5-Minute Sync Countdown Card + Floating Live Video Proctoring Box */}
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '16px',
          position: 'sticky',
          top: '20px'
        }}>
          {/* PROMINENT 5-MINUTE COUNTDOWN CARD */}
          <div style={{
            background: 'var(--surface-3)',
            border: syncSecondsRemaining > 0 ? '2px solid var(--accent)' : '2px solid var(--success)',
            borderRadius: 'var(--radius-lg)',
            padding: '18px',
            textAlign: 'center',
            boxShadow: syncSecondsRemaining > 0 ? '0 0 25px rgba(20, 184, 166, 0.25)' : '0 0 25px rgba(16, 185, 129, 0.35)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '8px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span style={{
                width: '10px',
                height: '10px',
                borderRadius: '50%',
                background: syncSecondsRemaining > 0 ? 'var(--danger)' : 'var(--success)',
                display: 'inline-block'
              }} />
              <span style={{ fontSize: '11px', fontWeight: 800, color: syncSecondsRemaining > 0 ? 'var(--danger-muted)' : 'var(--success)', textTransform: 'uppercase', letterSpacing: '0.8px' }}>
                {syncSecondsRemaining > 0 ? 'Mandatory 5-Min Sync Timer' : '5-Min Goal Reached!'}
              </span>
            </div>

            {/* Big Digital Clock Display */}
            <div style={{
              fontSize: '44px',
              fontWeight: 900,
              fontFamily: 'monospace',
              letterSpacing: '3px',
              color: syncSecondsRemaining > 0 ? 'var(--text-white)' : 'var(--success)',
              textShadow: syncSecondsRemaining > 0 ? '0 0 20px rgba(20, 184, 166, 0.4)' : '0 0 20px rgba(16, 185, 129, 0.6)',
              lineHeight: '1',
              margin: '4px 0'
            }}>
              {formatSyncTimer(syncSecondsRemaining)}
            </div>

            {/* Visual Progress Bar */}
            <div style={{
              width: '100%',
              height: '8px',
              background: 'rgba(255, 255, 255, 0.1)',
              borderRadius: '10px',
              overflow: 'hidden',
              position: 'relative'
            }}>
              <div style={{
                width: `${((300 - syncSecondsRemaining) / 300) * 100}%`,
                height: '100%',
                background: syncSecondsRemaining > 0
                  ? 'var(--accent-grad)'
                  : 'var(--accent-grad)',
                transition: 'width 1s linear',
                borderRadius: '10px'
              }} />
            </div>

            <div style={{ fontSize: '11.5px', color: syncSecondsRemaining > 0 ? 'var(--text-muted)' : 'var(--success)', fontWeight: 600, marginTop: '2px', lineHeight: '1.4' }}>
              {syncSecondsRemaining > 0 ? (
                <>🔒 <strong>Active Discussion Required:</strong> Screen locked for 5 minutes. No logout or exit allowed.</>
              ) : (
                <>✅ <strong>5 Minutes Completed!</strong> You may now sign off and complete the review.</>
              )}
            </div>
          </div>

          {/* CAMERA FEED BOX */}
          <div style={{
            background: 'var(--surface)',
            border: '1.5px solid var(--border)',
            borderRadius: 'var(--radius-lg)',
            padding: '16px',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            boxShadow: 'var(--shadow-md)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span style={{ fontSize: '12px', fontWeight: 800, color: 'var(--text)' }}>📷 Live Camera Feed</span>
              <span style={{ fontSize: '9px', fontWeight: 700, padding: '2px 6px', borderRadius: '4px', background: 'var(--danger)', color: 'var(--text-white)' }}>
                LIVE
              </span>
            </div>

            {/* Video Player */}
            <div style={{
              width: '100%',
              height: '180px',
              borderRadius: '8px',
              overflow: 'hidden',
              background: 'var(--text-black)',
              border: '1px solid var(--accent-ring)',
              position: 'relative'
            }}>
              <video 
                ref={syncVideoRef} 
                autoPlay 
                playsInline 
                muted 
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  transform: 'scaleX(-1)'
                }} 
              />
              {!syncLiveStream && (
                <div style={{
                  position: 'absolute',
                  inset: 0,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: 'var(--text-muted)',
                  fontSize: '11px',
                  textAlign: 'center',
                  padding: '8px'
                }}>
                  Connecting camera & audio stream...
                </div>
              )}
            </div>

            <div style={{ fontSize: '11px', color: 'var(--text-muted)', background: 'rgba(255,255,255,0.03)', padding: '8px 10px', borderRadius: '6px', lineHeight: '1.4' }}>
              📢 <strong>Educator Live Link:</strong> Your camera and audio are streaming directly to the Live Exam Monitor so educators can observe, talk, or listen during this sync.
            </div>
          </div>
        </div>

      </div>
    </div>
  );
});
