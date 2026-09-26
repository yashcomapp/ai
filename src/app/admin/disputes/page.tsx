'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateTimeIST } from '@/lib/dateUtils';

export default function AdminDisputesPage() {
  const { user, firebaseUser, loading: authLoading } = useAuth();
  const router = useRouter();

  const [disputes, setDisputes] = useState<any[]>([]);
  const [grouped, setGrouped] = useState<Record<string, Record<string, any[]>>>({});
  const [loading, setLoading] = useState<boolean>(true);
  const [resolvingKey, setResolvingKey] = useState<string | null>(null);
  const [actionSuccessMsg, setActionSuccessMsg] = useState<string>('');

  // Resolution Modal
  const [activeModalItem, setActiveModalItem] = useState<{ examId: string; questionId: string; reports: any[] } | null>(null);
  const [newCorrectOption, setNewCorrectOption] = useState<string>('B');
  const [resolutionAction, setResolutionAction] = useState<'correct_key' | 'bonus_all' | 'quarantine'>('correct_key');
  const [resolutionNotes, setResolutionNotes] = useState<string>('');

  const loadDisputes = useCallback(async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/disputes?status=all', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setDisputes(data.disputes || []);
        setGrouped(data.grouped || {});
      }
    } catch (err) {
      console.error('Failed to load exam disputes:', err);
    } finally {
      setLoading(false);
    }
  }, [firebaseUser]);

  useEffect(() => {
    if (user && user.role === 'admin') {
      loadDisputes();
    }
  }, [user, loadDisputes]);

  const handleResolve = async () => {
    if (!activeModalItem || !firebaseUser) return;
    setResolvingKey(`${activeModalItem.examId}_${activeModalItem.questionId}`);
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/disputes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          examId: activeModalItem.examId,
          questionId: activeModalItem.questionId,
          newCorrectOption,
          action: resolutionAction,
          notes: resolutionNotes
        })
      });

      if (res.ok) {
        const data = await res.json();
        setActionSuccessMsg(`✅ ${data.message}`);
        setActiveModalItem(null);
        setTimeout(() => setActionSuccessMsg(''), 6000);
        loadDisputes();
      } else {
        const err = await res.json();
        alert('Error: ' + (err.message || 'Failed to resolve dispute'));
      }
    } catch (e: any) {
      alert('Error: ' + e.message);
    } finally {
      setResolvingKey(null);
    }
  };

  if (authLoading || !user) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'var(--bg)' }}>
        <span>Loading Disputes Hub...</span>
      </div>
    );
  }

  const examKeys = Object.keys(grouped);

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '16px 12px' }}>
      <div style={{ maxWidth: '1280px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        
        {/* Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px', background: 'var(--surface)', padding: '14px 18px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ margin: 0, fontSize: '18px', fontWeight: 800, color: 'var(--text)' }}>
                ⚖️ Exam Question Disputes & Diligence Bounty Hub
              </h2>
              <span className="badge" style={{ background: 'var(--warning-bg)', color: 'var(--warning)', border: '1px solid var(--warning-border)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '12px' }}>
                Top 3 Bounty Tracking
              </span>
            </div>
            <p style={{ margin: '3px 0 0', fontSize: '12px', color: 'var(--text-muted)' }}>
              1-Click Batch Exam Re-Evaluation when flawed keys are reported. Awards Diligence Bounties (+2 points & badges) strictly to the first 3 spotters.
            </p>
          </div>

          <div style={{ display: 'flex', gap: '8px' }}>
            <button
              type="button"
              className="btn btn-secondary btn-sm"
              onClick={() => router.push('/admin/fault-register')}
              style={{ fontSize: '12px', padding: '6px 12px' }}
            >
              📋 Fault Register
            </button>
            <button
              type="button"
              className="btn btn-secondary btn-sm"
              onClick={loadDisputes}
              disabled={loading}
              style={{ fontSize: '12px', padding: '6px 12px' }}
            >
              🔄 Refresh
            </button>
          </div>
        </div>

        {actionSuccessMsg && (
          <div style={{ background: 'var(--success-bg)', color: 'var(--success)', border: '1px solid var(--success-border)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', fontSize: '12px', fontWeight: 700 }}>
            {actionSuccessMsg}
          </div>
        )}

        {/* Content */}
        {loading ? (
          <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
            <div className="spinner" style={{ margin: '0 auto 10px' }}></div> Loading disputes and reporter ranks...
          </div>
        ) : examKeys.length === 0 ? (
          <div className="card" style={{ background: 'var(--surface)', padding: '40px 20px', textAlign: 'center', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <span style={{ fontSize: '36px' }}>🎉</span>
            <h3 style={{ margin: '10px 0 4px', fontSize: '16px', fontWeight: 700 }}>Zero Pending Question Disputes</h3>
            <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)' }}>
              All exam reviews are currently clear or all reported issues have been verified and resolved.
            </p>
          </div>
        ) : (
          examKeys.map(eId => {
            const qMap = grouped[eId];
            const qKeys = Object.keys(qMap);
            const firstReport = qMap[qKeys[0]]?.[0];
            const examName = firstReport?.examName || eId;

            return (
              <div key={eId} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
                  <div>
                    <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--accent)' }}>
                      📝 {examName}
                    </h3>
                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>Exam ID: {eId} • {qKeys.length} flagged question(s)</span>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {qKeys.map(qId => {
                    const reports = qMap[qId];
                    const reportCount = reports.length;
                    const isResolving = resolvingKey === `${eId}_${qId}`;
                    const isAlreadyResolved = reports.some(r => r.status?.startsWith('approved'));

                    return (
                      <div
                        key={qId}
                        style={{
                          background: 'var(--surface-light)',
                          border: '1px solid var(--border-light)',
                          borderRadius: 'var(--radius-sm)',
                          padding: '12px',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '8px'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                          <div>
                            <span className="badge" style={{ background: 'var(--accent-soft)', color: 'var(--accent)', fontWeight: 800, fontSize: '11px', padding: '2px 8px', borderRadius: '10px' }}>
                              Question: {qId}
                            </span>
                            {isAlreadyResolved ? (
                              <span className="badge" style={{ marginLeft: '6px', background: 'var(--success-bg)', color: 'var(--success)', fontSize: '10px', fontWeight: 700, padding: '2px 6px', borderRadius: '10px' }}>
                                ✅ Resolved & Re-evaluated
                              </span>
                            ) : (
                              <span className="badge" style={{ marginLeft: '6px', background: 'var(--danger-bg)', color: 'var(--danger)', fontSize: '10px', fontWeight: 700, padding: '2px 6px', borderRadius: '10px' }}>
                                ⚠️ {reportCount} Student Report(s)
                              </span>
                            )}
                          </div>

                          {!isAlreadyResolved && (
                            <button
                              type="button"
                              className="btn btn-primary btn-sm"
                              onClick={() => {
                                setActiveModalItem({ examId: eId, questionId: qId, reports });
                                setNewCorrectOption('B');
                                setResolutionAction('correct_key');
                                setResolutionNotes('');
                              }}
                              disabled={isResolving}
                              style={{ fontSize: '11px', padding: '4px 12px', fontWeight: 700 }}
                            >
                              ⚡ Correct Key & Batch Re-evaluate
                            </button>
                          )}
                        </div>

                        {/* Top Reporters List with Bounty Badges */}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', background: 'var(--surface)', padding: '8px 10px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                          <span style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                            Reporters & Bounty Eligibility (First 3 Only):
                          </span>
                          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                            {reports.map((rep, rIdx) => {
                              const rank = rep.reporterRank || rIdx + 1;
                              const isTop3 = rank <= 3;
                              return (
                                <div
                                  key={rep.id || rIdx}
                                  style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '6px',
                                    background: isTop3 ? 'var(--warning-bg)' : 'var(--surface-2)',
                                    border: isTop3 ? '1px solid var(--warning-border)' : '1px solid var(--border-light)',
                                    padding: '3px 8px',
                                    borderRadius: '12px',
                                    fontSize: '11px'
                                  }}
                                >
                                  <span>{isTop3 ? `🏆 #${rank}` : `#${rank}`}</span>
                                  <strong>{rep.studentName}</strong>
                                  <span style={{ fontSize: '9px', color: 'var(--text-muted)' }}>
                                    ({rep.reason || 'issue'} • {formatDateTimeIST(rep.submittedAt || rep.createdAt)})
                                  </span>
                                  {isTop3 && (
                                    <span style={{ fontSize: '9px', color: 'var(--warning)', fontWeight: 800 }}>
                                      [+2 Bounty Eligible]
                                    </span>
                                  )}
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })
        )}

      </div>

      {/* Resolution Modal */}
      {activeModalItem && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.5)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '12px' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '100%', padding: '18px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 800 }}>⚡ Batch Re-Evaluate Exam</h4>
              <button className="close-modal" onClick={() => setActiveModalItem(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            <div style={{ background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', marginBottom: '12px', fontSize: '11px' }}>
              <div><strong>Exam ID:</strong> {activeModalItem.examId}</div>
              <div><strong>Question:</strong> {activeModalItem.questionId}</div>
              <div style={{ color: 'var(--accent)', fontWeight: 700, marginTop: '4px' }}>
                🏆 Top {Math.min(3, activeModalItem.reports.length)} reporter(s) will automatically receive the Diligence Bounty (+2 Marks & Profile Badge).
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Resolution Action</label>
                <select
                  value={resolutionAction}
                  onChange={(e) => setResolutionAction(e.target.value as any)}
                  style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)' }}
                >
                  <option value="correct_key">Change Correct Key (Re-evaluate all attempts against new key)</option>
                  <option value="bonus_all">Award Bonus Marks to All Students (Flawed Question)</option>
                  <option value="quarantine">Quarantine / Exclude Question from Exam Total</option>
                </select>
              </div>

              {resolutionAction === 'correct_key' && (
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>New Correct Option Letter</label>
                  <select
                    value={newCorrectOption}
                    onChange={(e) => setNewCorrectOption(e.target.value)}
                    style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', fontWeight: 700 }}
                  >
                    <option value="A">Option A</option>
                    <option value="B">Option B</option>
                    <option value="C">Option C</option>
                    <option value="D">Option D</option>
                  </select>
                </div>
              )}

              <div>
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '3px' }}>Resolution Notes / Explanation</label>
                <textarea
                  rows={2}
                  value={resolutionNotes}
                  onChange={(e) => setResolutionNotes(e.target.value)}
                  placeholder="e.g. Verified answer key was incorrectly marked as A instead of B..."
                  style={{ width: '100%', padding: '6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg)', color: 'var(--text)' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '10px' }}>
                <button
                  type="button"
                  className="btn btn-secondary btn-sm"
                  onClick={() => setActiveModalItem(null)}
                >
                  Cancel
                </button>
                <button
                  type="button"
                  className="btn btn-primary btn-sm"
                  onClick={handleResolve}
                  disabled={resolvingKey !== null}
                  style={{ fontWeight: 700 }}
                >
                  {resolvingKey ? 'Re-evaluating...' : 'Apply Correction & Recalculate'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
