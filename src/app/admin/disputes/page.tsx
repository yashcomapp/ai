'use client';

import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { formatDateTimeIST } from '@/lib/dateUtils';
import { useMathRender } from '@/hooks/useMathRender';
import { 
  preprocessMathText, 
  stripOptionLabel, 
  resolveOptionDisplayText, 
  extractAssertionAndReason, 
  isAssertionReasonType 
} from '@/lib/questionTypes';

export default function AdminDisputesPage() {
  const { user, firebaseUser, loading: authLoading } = useAuth();
  const router = useRouter();

  const [disputes, setDisputes] = useState<any[]>([]);
  const [grouped, setGrouped] = useState<Record<string, Record<string, any[]>>>({});
  const [questionsMap, setQuestionsMap] = useState<Record<string, any>>({});
  const [loading, setLoading] = useState<boolean>(true);
  const [resolvingKey, setResolvingKey] = useState<string | null>(null);
  const [actionSuccessMsg, setActionSuccessMsg] = useState<string>('');
  const [expandedCodes, setExpandedCodes] = useState<Set<string>>(new Set());

  // Resolution Modal
  const [activeModalItem, setActiveModalItem] = useState<{ examId: string; questionId: string; reports: any[] } | null>(null);
  const [newCorrectOption, setNewCorrectOption] = useState<string>('B');
  const [resolutionAction, setResolutionAction] = useState<'correct_key' | 'bonus_all' | 'quarantine' | 'reject_challenge'>('correct_key');
  const [resolutionNotes, setResolutionNotes] = useState<string>('');

  // Student History Modal
  const [selectedStudentForHistory, setSelectedStudentForHistory] = useState<{ studentCode: string; studentName: string; className?: string } | null>(null);

  // MathKaTeX renderer hook
  useMathRender([loading, disputes, activeModalItem, expandedCodes, selectedStudentForHistory]);

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
        setQuestionsMap(data.questionsMap || {});
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

  const toggleExpand = (key: string) => {
    setExpandedCodes(prev => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const handleResolve = async (overrideAction?: 'reject_challenge') => {
    if (!activeModalItem || !firebaseUser) return;
    const actionToApply = overrideAction || resolutionAction;
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
          action: actionToApply,
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

  const activeQuestionData = useMemo(() => {
    if (!activeModalItem) return null;
    return questionsMap[activeModalItem.questionId] || null;
  }, [activeModalItem, questionsMap]);

  // Sorted exam keys: exams with open pending disputes appear first
  const sortedExamKeys = useMemo(() => {
    const keys = Object.keys(grouped);
    return keys.sort((a, b) => {
      const qMapA = grouped[a] || {};
      const qMapB = grouped[b] || {};
      const hasPendingA = Object.values(qMapA).some(reports =>
        !reports.every((r: any) => r.status && r.status !== 'pending')
      );
      const hasPendingB = Object.values(qMapB).some(reports =>
        !reports.every((r: any) => r.status && r.status !== 'pending')
      );
      if (hasPendingA !== hasPendingB) {
        return hasPendingA ? -1 : 1;
      }
      return 0;
    });
  }, [grouped]);

  // Student history disputes
  const studentDisputesList = useMemo(() => {
    if (!selectedStudentForHistory) return [];
    const targetCode = (selectedStudentForHistory.studentCode || '').toUpperCase();
    const targetName = (selectedStudentForHistory.studentName || '').toLowerCase();
    return disputes.filter(d => {
      const sCode = (d.studentCode || '').toUpperCase();
      const sName = (d.studentName || '').toLowerCase();
      return (targetCode && sCode === targetCode) || (targetName && sName === targetName);
    });
  }, [selectedStudentForHistory, disputes]);

  if (authLoading || !user) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', background: 'var(--bg)' }}>
        <span>Loading Disputes Hub...</span>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', padding: '16px 12px' }}>
      <div style={{ maxWidth: '1280px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        
        {/* Back to Dashboard Link on Top */}
        <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
          <button 
            onClick={() => router.push('/admin')} 
            style={{
              background: 'none',
              border: 'none',
              color: 'var(--accent)',
              cursor: 'pointer',
              fontSize: '13px',
              fontWeight: 600,
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
              padding: 0
            }}
          >
            ← Back to Dashboard
          </button>
        </div>

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
              1-Click Batch Exam Re-Evaluation or Challenge Dismissal when issues are reported. Awards Diligence Bounties (+2 points & badges) strictly to the first 3 spotters.
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
        ) : sortedExamKeys.length === 0 ? (
          <div className="card" style={{ background: 'var(--surface)', padding: '40px 20px', textAlign: 'center', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <span style={{ fontSize: '36px' }}>🎉</span>
            <h3 style={{ margin: '10px 0 4px', fontSize: '16px', fontWeight: 700 }}>Zero Pending Question Disputes</h3>
            <p style={{ margin: 0, fontSize: '12px', color: 'var(--text-muted)' }}>
              All exam reviews are currently clear or all reported issues have been verified and resolved.
            </p>
          </div>
        ) : (
          sortedExamKeys.map(eId => {
            const qMap = grouped[eId];
            const rawQKeys = Object.keys(qMap);
            const firstReport = qMap[rawQKeys[0]]?.[0];
            const examName = firstReport?.examName || eId;

            // Sort questions: unresolved first, resolved sent to the bottom of the list
            const sortedQKeys = [...rawQKeys].sort((a, b) => {
              const repA = qMap[a] || [];
              const repB = qMap[b] || [];
              const isResA = repA.every((r: any) => r.status && r.status !== 'pending') || repA.some((r: any) => r.status?.startsWith('approved') || r.status === 'rejected');
              const isResB = repB.every((r: any) => r.status && r.status !== 'pending') || repB.some((r: any) => r.status?.startsWith('approved') || r.status === 'rejected');
              if (isResA !== isResB) {
                return isResA ? 1 : -1; // Unresolved (false) at top, Resolved (true) at bottom
              }
              return repB.length - repA.length;
            });

            const pendingCount = sortedQKeys.filter(qId => {
              const rep = qMap[qId] || [];
              return !rep.every((r: any) => r.status && r.status !== 'pending') && !rep.some((r: any) => r.status?.startsWith('approved') || r.status === 'rejected');
            }).length;

            return (
              <div key={eId} className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
                  <div>
                    <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--accent)' }}>
                      📝 {examName}
                    </h3>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)', display: 'flex', gap: '8px', alignItems: 'center', marginTop: '2px' }}>
                      <span>Exam ID: <code>{eId}</code></span>
                      <span>•</span>
                      <span>{sortedQKeys.length} flagged question(s)</span>
                      {pendingCount > 0 ? (
                        <span className="badge" style={{ background: 'var(--danger-bg)', color: 'var(--danger)', fontSize: '10px', fontWeight: 700, padding: '1px 6px', borderRadius: '4px' }}>
                          ⚠️ {pendingCount} Pending
                        </span>
                      ) : (
                        <span className="badge" style={{ background: 'var(--success-bg)', color: 'var(--success)', fontSize: '10px', fontWeight: 700, padding: '1px 6px', borderRadius: '4px' }}>
                          ✅ All Resolved
                        </span>
                      )}
                    </div>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {sortedQKeys.map(qId => {
                    const reports = qMap[qId];
                    const reportCount = reports.length;
                    const isResolving = resolvingKey === `${eId}_${qId}`;
                    const isAlreadyApproved = reports.some(r => r.status?.startsWith('approved'));
                    const isAlreadyRejected = reports.every(r => r.status === 'rejected');
                    const isResolved = isAlreadyApproved || isAlreadyRejected;
                    const qData = questionsMap[qId] || null;
                    const itemKey = `${eId}_${qId}`;
                    
                    // Resolved questions are collapsed by default unless explicitly expanded by user
                    const isExpanded = expandedCodes.has(itemKey);

                    // Determine current correct answer label
                    const rawCorrect = qData?.correctAnswer || qData?.answer || 'A';
                    const isAssertion = isAssertionReasonType(qData?.type);
                    const { assertionText, reasonText } = isAssertion 
                      ? extractAssertionAndReason(qData?.text || qData?.questionText || '', qData?.assertion, qData?.reason)
                      : { assertionText: '', reasonText: '' };

                    return (
                      <div
                        key={qId}
                        style={{
                          background: isResolved ? 'var(--surface)' : 'var(--surface-light)',
                          border: isAlreadyApproved
                            ? '1px solid var(--success-border, #10b981)'
                            : isAlreadyRejected
                              ? '1px solid var(--border-light)'
                              : '1px solid var(--warning-border, #f59e0b)',
                          borderRadius: 'var(--radius-md, 8px)',
                          padding: isResolved && !isExpanded ? '10px 14px' : '14px',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '10px',
                          opacity: isResolved && !isExpanded ? 0.9 : 1
                        }}
                      >
                        {/* Top Bar with Question Code & Action Buttons */}
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                            <span className="badge" style={{ background: 'var(--accent-soft)', color: 'var(--accent)', fontWeight: 800, fontSize: '11px', padding: '3px 8px', borderRadius: '6px' }}>
                              Question: {qId}
                            </span>
                            {qData?.type && (
                              <span className="badge" style={{ background: 'var(--surface-2)', color: 'var(--text-muted)', fontSize: '10px', fontWeight: 600, padding: '2px 6px', borderRadius: '4px' }}>
                                {qData.type}
                              </span>
                            )}
                            {isAlreadyApproved ? (
                              <span className="badge" style={{ background: 'var(--success-bg)', color: 'var(--success)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '10px' }}>
                                ✅ Resolved & Re-evaluated
                              </span>
                            ) : isAlreadyRejected ? (
                              <span className="badge" style={{ background: 'rgba(148, 163, 184, 0.2)', color: '#94a3b8', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '10px' }}>
                                ❌ Challenge Dismissed / Valid
                              </span>
                            ) : (
                              <span className="badge" style={{ background: 'var(--danger-bg)', color: 'var(--danger)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '10px' }}>
                                ⚠️ {reportCount} Student Report(s)
                              </span>
                            )}
                          </div>

                          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                            <button
                              type="button"
                              className="btn btn-secondary btn-sm"
                              onClick={() => toggleExpand(itemKey)}
                              style={{ fontSize: '11px', padding: '4px 10px', display: 'flex', alignItems: 'center', gap: '4px' }}
                            >
                              <span>{isExpanded ? '▲' : '▼'}</span> {isExpanded ? 'Hide Details' : isResolved ? 'View Question' : 'Details'}
                            </button>

                            <button
                              type="button"
                              className="btn btn-primary btn-sm"
                              onClick={() => {
                                setActiveModalItem({ examId: eId, questionId: qId, reports });
                                setNewCorrectOption(String(rawCorrect).toUpperCase().trim().slice(0, 1) || 'B');
                                setResolutionAction('correct_key');
                                setResolutionNotes('');
                              }}
                              disabled={isResolving}
                              style={{ fontSize: '11px', padding: '4px 12px', fontWeight: 700 }}
                            >
                              ⚡ Re-Evaluate / Resolve
                            </button>
                          </div>
                        </div>

                        {/* Question Content & Options Display (Shown when expanded or open) */}
                        {isExpanded && (
                          <div
                            style={{
                              background: 'var(--surface)',
                              border: '1px solid var(--border-light)',
                              borderRadius: '8px',
                              padding: '12px'
                            }}
                          >
                            {qData ? (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                                {/* Question Text */}
                                <div>
                                  <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '4px' }}>
                                    Question Statement:
                                  </div>
                                  <div 
                                    style={{ fontSize: '13px', lineHeight: 1.5, color: 'var(--text)', fontWeight: 600 }}
                                    dangerouslySetInnerHTML={{ __html: preprocessMathText(qData.text || qData.questionText || '') }}
                                  />
                                </div>

                                {/* Assertion & Reason if applicable */}
                                {isAssertion && (
                                  <div style={{ background: 'var(--surface-light)', padding: '8px 10px', borderRadius: '6px', fontSize: '12px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                    {assertionText && (
                                      <div><strong>Assertion (A):</strong> <span dangerouslySetInnerHTML={{ __html: preprocessMathText(assertionText) }} /></div>
                                    )}
                                    {reasonText && (
                                      <div><strong>Reason (R):</strong> <span dangerouslySetInnerHTML={{ __html: preprocessMathText(reasonText) }} /></div>
                                    )}
                                  </div>
                                )}

                                {/* Options List */}
                                {qData.options && qData.options.length > 0 && (
                                  <div>
                                    <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '6px' }}>
                                      Options:
                                    </div>
                                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '6px' }}>
                                      {qData.options.map((opt: any, oIdx: number) => {
                                        const optLetter = String.fromCharCode(65 + oIdx);
                                        const isCorrect = String(rawCorrect).toUpperCase().includes(optLetter);
                                        const optText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);

                                        return (
                                          <div
                                            key={oIdx}
                                            style={{
                                              display: 'flex',
                                              alignItems: 'center',
                                              gap: '8px',
                                              padding: '6px 10px',
                                              borderRadius: '6px',
                                              fontSize: '12px',
                                              background: isCorrect ? 'var(--success-bg, rgba(16, 185, 129, 0.15))' : 'var(--surface-light)',
                                              border: isCorrect ? '1px solid var(--success, #10b981)' : '1px solid var(--border-light)',
                                              color: isCorrect ? 'var(--success, #10b981)' : 'var(--text)'
                                            }}
                                          >
                                            <strong style={{ minWidth: '22px' }}>({optLetter})</strong>
                                            <span 
                                              style={{ flex: 1 }}
                                              dangerouslySetInnerHTML={{ __html: preprocessMathText(stripOptionLabel(optText)) }}
                                            />
                                            {isCorrect && (
                                              <span style={{ fontSize: '10px', fontWeight: 800, padding: '1px 6px', borderRadius: '4px', background: 'var(--success)', color: '#fff' }}>
                                                ✓ Key
                                              </span>
                                            )}
                                          </div>
                                        );
                                      })}
                                    </div>
                                  </div>
                                )}

                                {/* Solution / Explanation */}
                                {(qData.solution || qData.explanation) && (
                                  <div style={{ background: 'rgba(59, 130, 246, 0.08)', border: '1px solid rgba(59, 130, 246, 0.2)', borderRadius: '6px', padding: '8px 10px', fontSize: '12px' }}>
                                    <strong style={{ color: 'var(--accent)' }}>💡 Solution / Explanation:</strong>
                                    <div 
                                      style={{ marginTop: '3px', color: 'var(--text-muted)' }}
                                      dangerouslySetInnerHTML={{ __html: preprocessMathText(qData.solution || qData.explanation) }}
                                    />
                                  </div>
                                )}
                              </div>
                            ) : (
                              <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                                Question data not found in index. Question Code: <code>{qId}</code>
                              </div>
                            )}
                          </div>
                        )}

                        {/* Top Reporters List - Clean One-Line Format as per Class & Student Name */}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', background: 'var(--surface)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                          <span style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                            Reporters & Bounty Eligibility (First 3 Only):
                          </span>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                            {reports.map((rep, rIdx) => {
                              const rank = rep.reporterRank || rIdx + 1;
                              const isTop3 = rank <= 3;
                              const studentClass = rep.className || (rep.classNum ? `Class ${rep.classNum}` : 'Student');

                              return (
                                <div
                                  key={rep.id || rIdx}
                                  style={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    justifyContent: 'space-between',
                                    flexWrap: 'wrap',
                                    gap: '8px',
                                    background: isTop3 ? 'rgba(245, 158, 11, 0.07)' : 'var(--surface-2)',
                                    border: isTop3 ? '1px solid rgba(245, 158, 11, 0.25)' : '1px solid var(--border-light)',
                                    padding: '5px 10px',
                                    borderRadius: '6px',
                                    fontSize: '12px'
                                  }}
                                >
                                  {/* Left: Rank, Class, Clickable Student Name, Reason & Notes */}
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                                    <span style={{ fontWeight: 800, color: isTop3 ? 'var(--warning)' : 'var(--text-muted)', fontSize: '11px', minWidth: '35px' }}>
                                      {isTop3 ? `🏆 #${rank}` : `#${rank}`}
                                    </span>

                                    <span className="badge" style={{ background: 'var(--surface)', color: 'var(--text-muted)', fontSize: '10px', fontWeight: 700, padding: '1px 6px', borderRadius: '4px', border: '1px solid var(--border-light)' }}>
                                      {studentClass}
                                    </span>

                                    {/* Clickable Student Name to open dispute history modal */}
                                    <button
                                      type="button"
                                      onClick={() => setSelectedStudentForHistory({
                                        studentCode: rep.studentCode || '',
                                        studentName: rep.studentName || 'Student',
                                        className: studentClass
                                      })}
                                      style={{
                                        background: 'none',
                                        border: 'none',
                                        padding: 0,
                                        fontWeight: 800,
                                        color: 'var(--accent)',
                                        textDecoration: 'underline',
                                        cursor: 'pointer',
                                        fontSize: '12px'
                                      }}
                                      title="Click to view all reports and questions disputed by this student"
                                    >
                                      {rep.studentName}
                                    </button>

                                    <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>
                                      • <strong>{rep.reason || 'issue'}</strong>
                                      {rep.notes && <span style={{ fontStyle: 'italic', marginLeft: '4px' }}>— &quot;{rep.notes}&quot;</span>}
                                      {rep.suggestedAnswer && <span style={{ marginLeft: '4px', color: 'var(--text)' }}>[Suggested: {rep.suggestedAnswer}]</span>}
                                    </span>
                                  </div>

                                  {/* Right: Timestamp & Bounty status */}
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>
                                      📅 {formatDateTimeIST(rep.submittedAt || rep.createdAt)}
                                    </span>
                                    {isTop3 && (
                                      <span className="badge" style={{ background: 'var(--warning-bg)', color: 'var(--warning)', fontWeight: 800, fontSize: '9px', padding: '2px 6px', borderRadius: '4px', border: '1px solid var(--warning-border)' }}>
                                        +2 Bounty Eligible
                                      </span>
                                    )}
                                  </div>
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

      {/* Student Dispute & Report History Modal */}
      {selectedStudentForHistory && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.65)', backdropFilter: 'blur(6px)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px', overflowY: 'auto' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg, 12px)', maxWidth: '720px', width: '100%', padding: '20px', maxHeight: '90vh', overflowY: 'auto', boxShadow: 'var(--shadow-xl)' }}>
            
            {/* Modal Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <h4 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: 'var(--text)' }}>
                    👤 {selectedStudentForHistory.studentName}&apos;s Disputed Questions
                  </h4>
                  {selectedStudentForHistory.className && (
                    <span className="badge" style={{ background: 'var(--accent-soft)', color: 'var(--accent)', fontSize: '10px', fontWeight: 700, padding: '2px 6px', borderRadius: '4px' }}>
                      {selectedStudentForHistory.className}
                    </span>
                  )}
                </div>
                <p style={{ margin: '2px 0 0', fontSize: '11px', color: 'var(--text-muted)' }}>
                  Complete track record of all questions reported and challenged by this student.
                </p>
              </div>
              <button 
                className="close-modal" 
                onClick={() => setSelectedStudentForHistory(null)} 
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.4rem', color: 'var(--text-muted)' }}
              >
                ✕
              </button>
            </div>

            {/* Summary Statistics Bar */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginBottom: '14px' }}>
              <div style={{ background: 'var(--surface-light)', padding: '10px', borderRadius: '8px', textAlign: 'center', border: '1px solid var(--border-light)' }}>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--accent)' }}>{studentDisputesList.length}</div>
                <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>Total Reports Filed</div>
              </div>
              <div style={{ background: 'rgba(245, 158, 11, 0.08)', padding: '10px', borderRadius: '8px', textAlign: 'center', border: '1px solid rgba(245, 158, 11, 0.2)' }}>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--warning)' }}>
                  {studentDisputesList.filter(d => (d.reporterRank || 1) <= 3).length}
                </div>
                <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--warning)', textTransform: 'uppercase' }}>🏆 Top 3 Spotters</div>
              </div>
              <div style={{ background: 'rgba(16, 185, 129, 0.08)', padding: '10px', borderRadius: '8px', textAlign: 'center', border: '1px solid rgba(16, 185, 129, 0.2)' }}>
                <div style={{ fontSize: '18px', fontWeight: 800, color: 'var(--success)' }}>
                  {studentDisputesList.filter(d => d.status?.startsWith('approved')).length}
                </div>
                <div style={{ fontSize: '10px', fontWeight: 700, color: 'var(--success)', textTransform: 'uppercase' }}>Resolved / Awarded</div>
              </div>
            </div>

            {/* Student's Reports List */}
            {studentDisputesList.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '30px 10px', color: 'var(--text-muted)', fontSize: '12px' }}>
                No active dispute reports found for this student.
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {studentDisputesList.map((d, idx) => {
                  const qData = questionsMap[d.questionId || d.questionCode] || null;
                  const isApproved = d.status?.startsWith('approved');
                  const isRejected = d.status === 'rejected';
                  const isTop3 = (d.reporterRank || idx + 1) <= 3;

                  return (
                    <div
                      key={d.id || idx}
                      style={{
                        background: 'var(--surface-light)',
                        border: isApproved 
                          ? '1px solid var(--success-border)' 
                          : isRejected 
                            ? '1px solid var(--border-light)' 
                            : '1px solid var(--warning-border)',
                        borderRadius: '8px',
                        padding: '12px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '8px'
                      }}
                    >
                      {/* Top Header of Question */}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '6px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                          <span className="badge" style={{ background: 'var(--accent-soft)', color: 'var(--accent)', fontWeight: 800, fontSize: '11px', padding: '2px 8px', borderRadius: '4px' }}>
                            {d.questionCode || d.questionId}
                          </span>
                          <span style={{ fontSize: '11px', fontWeight: 700, color: 'var(--text)' }}>
                            {d.examName || d.examId}
                          </span>
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                          {isApproved ? (
                            <span className="badge" style={{ background: 'var(--success-bg)', color: 'var(--success)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '8px' }}>
                              ✅ Resolved & Re-evaluated
                            </span>
                          ) : isRejected ? (
                            <span className="badge" style={{ background: 'rgba(148, 163, 184, 0.2)', color: '#94a3b8', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '8px' }}>
                              ❌ Challenge Dismissed
                            </span>
                          ) : (
                            <span className="badge" style={{ background: 'var(--danger-bg)', color: 'var(--danger)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '8px' }}>
                              ⏳ Pending Review
                            </span>
                          )}

                          {isTop3 && (
                            <span className="badge" style={{ background: 'var(--warning-bg)', color: 'var(--warning)', fontSize: '10px', fontWeight: 700, padding: '2px 8px', borderRadius: '8px' }}>
                              🏆 Spotter #{d.reporterRank || 1}
                            </span>
                          )}
                        </div>
                      </div>

                      {/* Question text preview if available */}
                      {qData?.text && (
                        <div style={{ background: 'var(--surface)', padding: '8px 10px', borderRadius: '6px', fontSize: '12px', border: '1px solid var(--border-light)' }}>
                          <div 
                            style={{ color: 'var(--text)', fontWeight: 600, lineHeight: 1.4 }}
                            dangerouslySetInnerHTML={{ __html: preprocessMathText(qData.text || qData.questionText || '') }}
                          />
                        </div>
                      )}

                      {/* Student's Challenge Details */}
                      <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', display: 'flex', flexDirection: 'column', gap: '3px' }}>
                        <div>
                          <strong style={{ color: 'var(--text)' }}>Reason:</strong> {d.reason || 'General issue'}
                        </div>
                        {d.suggestedAnswer && (
                          <div>
                            <strong style={{ color: 'var(--text)' }}>Suggested Answer:</strong> {d.suggestedAnswer}
                          </div>
                        )}
                        {d.notes && (
                          <div>
                            <strong style={{ color: 'var(--text)' }}>Student Notes:</strong> &quot;{d.notes}&quot;
                          </div>
                        )}
                        <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '2px' }}>
                          Reported on {formatDateTimeIST(d.submittedAt || d.createdAt)}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Modal Footer */}
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '14px', paddingTop: '10px', borderTop: '1px solid var(--border-light)' }}>
              <button
                type="button"
                className="btn btn-secondary btn-sm"
                onClick={() => setSelectedStudentForHistory(null)}
              >
                Close View
              </button>
            </div>

          </div>
        </div>
      )}

      {/* Resolution & Challenge Management Modal */}
      {activeModalItem && (
        <div className="modal show" style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.65)', backdropFilter: 'blur(6px)', zIndex: 40000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px', overflowY: 'auto' }}>
          <div className="modal-content" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg, 12px)', maxWidth: '680px', width: '100%', padding: '22px', maxHeight: '90vh', overflowY: 'auto', boxShadow: 'var(--shadow-xl)' }}>
            
            {/* Modal Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', borderBottom: '1px solid var(--border-light)', paddingBottom: '10px' }}>
              <h4 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: 'var(--text)' }}>
                ⚖️ Dispute Resolution & Exam Re-Evaluation
              </h4>
              <button className="close-modal" onClick={() => setActiveModalItem(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.4rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            {/* Exam & Question Meta Header */}
            <div style={{ background: 'var(--bg-soft)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', marginBottom: '14px', fontSize: '12px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
              <div><strong>Exam ID:</strong> <code>{activeModalItem.examId}</code></div>
              <div><strong>Question Code:</strong> <code>{activeModalItem.questionId}</code></div>
              <div style={{ color: 'var(--warning)', fontWeight: 700, marginTop: '2px' }}>
                🏆 Top {Math.min(3, activeModalItem.reports.length)} reporter(s) will automatically receive the Diligence Bounty (+2 Marks & Profile Badge) if correction is approved.
              </div>
            </div>

            {/* Live Question & Options Preview inside Modal */}
            {activeQuestionData && (
              <div style={{ background: 'var(--surface-light)', border: '1px solid var(--border-light)', borderRadius: '8px', padding: '14px', marginBottom: '16px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <div>
                  <span style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                    Question Statement:
                  </span>
                  <div 
                    style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text)', marginTop: '3px', lineHeight: 1.5 }}
                    dangerouslySetInnerHTML={{ __html: preprocessMathText(activeQuestionData.text || activeQuestionData.questionText || '') }}
                  />
                </div>

                {/* Options List */}
                {activeQuestionData.options && activeQuestionData.options.length > 0 && (
                  <div>
                    <span style={{ fontSize: '10px', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                      Options (Current Answer Key Marked):
                    </span>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '6px', marginTop: '4px' }}>
                      {activeQuestionData.options.map((opt: any, oIdx: number) => {
                        const optLetter = String.fromCharCode(65 + oIdx);
                        const isCurrentKey = String(activeQuestionData.correctAnswer || activeQuestionData.answer || '').toUpperCase().includes(optLetter);
                        const optText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);

                        return (
                          <div
                            key={oIdx}
                            style={{
                              display: 'flex',
                              alignItems: 'center',
                              gap: '8px',
                              padding: '6px 10px',
                              borderRadius: '6px',
                              fontSize: '12px',
                              background: isCurrentKey ? 'var(--success-bg, rgba(16, 185, 129, 0.15))' : 'var(--surface)',
                              border: isCurrentKey ? '1px solid var(--success, #10b981)' : '1px solid var(--border-light)',
                              color: isCurrentKey ? 'var(--success, #10b981)' : 'var(--text)'
                            }}
                          >
                            <strong>({optLetter})</strong>
                            <span 
                              style={{ flex: 1 }}
                              dangerouslySetInnerHTML={{ __html: preprocessMathText(stripOptionLabel(optText)) }}
                            />
                            {isCurrentKey && (
                              <span style={{ fontSize: '10px', fontWeight: 800, padding: '2px 8px', borderRadius: '4px', background: 'var(--success)', color: '#fff' }}>
                                🟢 Current Answer Key
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}

                {/* Solution */}
                {(activeQuestionData.solution || activeQuestionData.explanation) && (
                  <div style={{ background: 'rgba(59, 130, 246, 0.08)', border: '1px solid rgba(59, 130, 246, 0.2)', borderRadius: '6px', padding: '8px 10px', fontSize: '11px' }}>
                    <strong style={{ color: 'var(--accent)' }}>💡 Solution / Explanation:</strong>
                    <div 
                      style={{ marginTop: '2px', color: 'var(--text-muted)' }}
                      dangerouslySetInnerHTML={{ __html: preprocessMathText(activeQuestionData.solution || activeQuestionData.explanation) }}
                    />
                  </div>
                )}
              </div>
            )}

            {/* Resolution Form Controls */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, color: 'var(--text)', marginBottom: '4px' }}>
                  Select Resolution Action:
                </label>
                <select
                  value={resolutionAction}
                  onChange={(e) => setResolutionAction(e.target.value as any)}
                  style={{ width: '100%', padding: '8px 10px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--surface-light)', color: 'var(--text)', fontWeight: 600 }}
                >
                  <option value="correct_key">🔑 Change Correct Key (Re-evaluate all student attempts against new key)</option>
                  <option value="bonus_all">🎁 Award Bonus Marks to All Students (Flawed / Ambiguous Question)</option>
                  <option value="quarantine">🚫 Delete from Question Bank & Exclude Question from Exam Total</option>
                  <option value="reject_challenge">❌ Reject / Dismiss Challenge (Question is 100% Valid - No Changes)</option>
                </select>
              </div>

              {resolutionAction === 'correct_key' && (
                <div>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, color: 'var(--text)', marginBottom: '4px' }}>
                    Select New Correct Option:
                  </label>
                  <select
                    value={newCorrectOption}
                    onChange={(e) => setNewCorrectOption(e.target.value)}
                    style={{ width: '100%', padding: '8px 10px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--surface-light)', color: 'var(--text)', fontWeight: 700 }}
                  >
                    {activeQuestionData?.options && activeQuestionData.options.length > 0 ? (
                      activeQuestionData.options.map((opt: any, oIdx: number) => {
                        const optLetter = String.fromCharCode(65 + oIdx);
                        const optText = typeof opt === 'object' && opt ? (opt.text || opt.value || '') : String(opt);
                        return (
                          <option key={oIdx} value={optLetter}>
                            Option {optLetter}: {stripOptionLabel(optText).slice(0, 60)}
                          </option>
                        );
                      })
                    ) : (
                      <>
                        <option value="A">Option A</option>
                        <option value="B">Option B</option>
                        <option value="C">Option C</option>
                        <option value="D">Option D</option>
                      </>
                    )}
                  </select>
                </div>
              )}

              <div>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, color: 'var(--text)', marginBottom: '4px' }}>
                  Resolution Notes / Explanation:
                </label>
                <textarea
                  rows={2}
                  value={resolutionNotes}
                  onChange={(e) => setResolutionNotes(e.target.value)}
                  placeholder={
                    resolutionAction === 'reject_challenge'
                      ? 'e.g. Verified answer key: Option A is correct according to textbook Chapter 3. Challenge dismissed.'
                      : 'e.g. Verified answer key was incorrectly marked as A instead of B...'
                  }
                  style={{ width: '100%', padding: '8px', fontSize: '12px', borderRadius: '6px', border: '1px solid var(--border-light)', background: 'var(--bg)', color: 'var(--text)' }}
                />
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '8px', marginTop: '12px', paddingTop: '10px', borderTop: '1px solid var(--border-light)' }}>
                <button
                  type="button"
                  className="btn btn-secondary btn-sm"
                  onClick={() => setActiveModalItem(null)}
                >
                  Cancel
                </button>

                <div style={{ display: 'flex', gap: '8px' }}>
                  {resolutionAction !== 'reject_challenge' && (
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => handleResolve('reject_challenge')}
                      disabled={resolvingKey !== null}
                      style={{ color: 'var(--danger)', borderColor: 'var(--danger-border)', fontWeight: 700 }}
                    >
                      ❌ Dismiss Challenge
                    </button>
                  )}

                  <button
                    type="button"
                    className="btn btn-primary btn-sm"
                    onClick={() => handleResolve()}
                    disabled={resolvingKey !== null}
                    style={{
                      fontWeight: 700,
                      background: resolutionAction === 'reject_challenge' ? 'var(--danger, #ef4444)' : undefined
                    }}
                  >
                    {resolvingKey 
                      ? 'Processing...' 
                      : resolutionAction === 'reject_challenge'
                        ? 'Confirm Dismissal (Reject Challenge)'
                        : '⚡ Apply Correction & Recalculate'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
