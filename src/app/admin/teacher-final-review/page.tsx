'use client';

import React, { useEffect, useState, Suspense } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
import Script from 'next/script';
import { useMathRender } from '@/hooks/useMathRender';
import { preprocessMathText, formatRichText } from '@/lib/questionTypes';

interface AttemptRow {
  id: string;
  studentCode: string;
  status: string;
  parentScore: number | null;
  peerScore: number | null;
  finalScore: number | null;
  totalMarks: number;
  isFinalReviewed: boolean;
  flagged: boolean;
  weeklyAvgPercent?: number | null;
  examPercent?: number | null;
  truthPercent?: number | null;
}

interface Question {
  id: string;
  questionCode: string;
  text: string;
  marks: number;
  solution?: string;
  answerLines?: Array<{ lineNo: number; text: string }>;
  steps?: Array<{ description: string; marks: number }>;
}

function TeacherFinalReviewContent() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();

  const examId = searchParams.get('examId') || '';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [examName, setExamName] = useState('Final review');
  const [examMeta, setExamMeta] = useState('');
  const [examMode, setExamMode] = useState('home');
  const [attempts, setAttempts] = useState<AttemptRow[]>([]);

  // Modal active states
  const [selectedAttemptId, setSelectedAttemptId] = useState<string | null>(null);
  const [modalLoading, setModalLoading] = useState(false);
  const [activeAttempt, setActiveAttempt] = useState<any>(null);
  const [activeQuestions, setActiveQuestions] = useState<Question[]>([]);
  const [activeEvaluations, setActiveEvaluations] = useState<any[]>([]);

  // Review scores inputs state
  const [reviewAnswers, setReviewAnswers] = useState<{ [key: string]: number | string }>({});
  const [reviewFeedback, setReviewFeedback] = useState<{ [key: string]: string }>({});
  const [submittingReview, setSubmittingReview] = useState(false);
  const [studentMap, setStudentMap] = useState<{[key: string]: string}>({});

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'student' | 'status' | 'finalScore' | 'examPercent' | 'weeklyAvgPercent' | 'truthPercent' | 'diffPercent'>('student');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);
  useMathRender([activeQuestions, selectedAttemptId]);

  const fetchAttempts = async () => {
    if (!firebaseUser || !examId) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      
      // Fetch student names map
      try {
        const stuRes = await fetch('/api/admin/students', {
          headers: { 'Authorization': `Bearer ${idToken}` }
        });
        if (stuRes.ok) {
          const stuData = await stuRes.json();
          const map: {[key: string]: string} = {};
          if (Array.isArray(stuData.students)) {
            stuData.students.forEach((s: any) => {
              if (s.studentCode) {
                map[s.studentCode] = s.name + (s.autonomous ? ' ⭐' : '');
              }
            });
          }
          setStudentMap(map);
        }
      } catch (e) {
        console.warn('Failed to load students mapping:', e);
      }

      const res = await fetch(`/api/admin/exams/subjective?examId=${examId}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to retrieve completed exam attempts.');
      }
      const data = await res.json();
      setAttempts(data.attempts);
      setExamName(data.exam?.name || 'Subjective Exam');
      const mode = data.exam?.mode || (data.exam?.type === 'classroom_test' ? 'classroom' : 'home');
      setExamMode(mode);
      setExamMeta(`Mode: ${mode} • ${data.exam?.questionIds?.length || 0} Questions`);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error occurred loading attempts.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (examId && firebaseUser) {
      fetchAttempts();
    }
  }, [firebaseUser, examId]);

  const handleSort = (field: 'student' | 'status' | 'finalScore' | 'examPercent' | 'weeklyAvgPercent' | 'truthPercent' | 'diffPercent') => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('asc');
    }
  };

  const sortedAttempts = [...attempts].sort((a, b) => {
    let comparison = 0;
    if (sortField === 'student') {
      const nameA = studentMap[a.studentCode] || 'Student';
      const nameB = studentMap[b.studentCode] || 'Student';
      comparison = nameA.localeCompare(nameB);
    } else if (sortField === 'status') {
      comparison = (a.status || '').localeCompare(b.status || '');
    } else if (sortField === 'examPercent') {
      comparison = (a.examPercent || 0) - (b.examPercent || 0);
    } else if (sortField === 'weeklyAvgPercent') {
      comparison = (a.weeklyAvgPercent || 0) - (b.weeklyAvgPercent || 0);
    } else if (sortField === 'diffPercent') {
      const diffA = (a.examPercent || 0) - (a.weeklyAvgPercent || 0);
      const diffB = (b.examPercent || 0) - (b.weeklyAvgPercent || 0);
      comparison = diffA - diffB;
    } else if (sortField === 'truthPercent') {
      comparison = (a.truthPercent || 0) - (b.truthPercent || 0);
    } else {
      comparison = (a.finalScore || 0) - (b.finalScore || 0);
    }
    return sortDir === 'asc' ? comparison : -comparison;
  });

  const openAttempt = async (attemptId: string) => {
    if (!firebaseUser) return;
    setSelectedAttemptId(attemptId);
    setModalLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/exams/subjective?attemptId=${attemptId}`, {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load attempt details.');
      }
      const data = await res.json();
      setActiveAttempt(data.attempt);
      setActiveQuestions(data.questions);
      setActiveEvaluations(data.evaluations);

      // Pre-fill grading answers state
      const initialAnswers: { [key: string]: number | string } = {};
      const initialFeedback: { [key: string]: string } = {};

      data.questions.forEach((q: Question, qi: number) => {
        const teacherItem = data.evaluations?.find((ev: any) => (ev.questionId === q.id || ev.questionId === q.questionCode || ev.rubricUsed === q.id) && ev.evaluatorType === 'teacher');
        const parentItem = data.evaluations?.find((ev: any) => (ev.questionId === q.id || ev.questionId === q.questionCode || ev.rubricUsed === q.id) && (ev.evaluatorType === 'parent' || ev.source === 'parent_subjective_review'));
        const peerItem = data.evaluations?.find((ev: any) => (ev.questionId === q.id || ev.questionId === q.questionCode || ev.rubricUsed === q.id) && (ev.evaluatorType === 'peer' || ev.source === 'peer_subjective_review'));

        const evalItem = teacherItem || parentItem || peerItem;

        if (evalItem) {
          initialFeedback[`pf_${qi}`] = evalItem.feedback || '';
          if (q.steps && q.steps.length > 0) {
            q.steps.forEach((step, si) => {
              const sItem = evalItem.stepMarks?.find((s: any) => s.stepNo === si + 1);
              initialAnswers[`ps_${qi}_${si}`] = sItem ? sItem.awarded : step.marks;
            });
          } else {
            initialAnswers[`ps_${qi}_0`] = evalItem.marksAwarded !== undefined ? evalItem.marksAwarded : q.marks;
          }
        }
      });

      setReviewAnswers(initialAnswers);
      setReviewFeedback(initialFeedback);
    } catch (err: any) {
      alert(err.message || 'Could not load details.');
      setSelectedAttemptId(null);
    } finally {
      setModalLoading(false);
    }
  };

  const closeAttemptModal = () => {
    setSelectedAttemptId(null);
    setActiveAttempt(null);
    setActiveQuestions([]);
    setActiveEvaluations([]);
  };

  const submitFinalGrades = async () => {
    if (!firebaseUser || !activeAttempt || submittingReview) return;

    // Validate all evaluation fields are explicitly answered
    for (let i = 0; i < activeQuestions.length; i++) {
      const q = activeQuestions[i];
      if (q.steps && q.steps.length > 0) {
        for (let s = 0; s < q.steps.length; s++) {
          const rawVal = reviewAnswers[`ps_${i}_${s}`];
          if (rawVal === undefined || rawVal === null || rawVal === "") {
            alert(`Please award marks for Question ${i + 1}, Step ${s + 1}.`);
            return;
          }
        }
      } else {
        const rawVal = reviewAnswers[`ps_${i}_0`];
        if (rawVal === undefined || rawVal === null || rawVal === "") {
          alert(`Please award marks for Question ${i + 1}.`);
          return;
        }
      }
    }

    if (!confirm('Submit these as the final canonical grades for this attempt? This cannot be changed later.')) return;

    setSubmittingReview(true);
    try {
      const questionReviews = [];
      let totalScore = 0;

      for (let i = 0; i < activeQuestions.length; i++) {
        const q = activeQuestions[i];
        let questionTotal = 0;
        const stepMarks: Array<{ stepNo: number; awarded: number }> = [];

        if (q.steps && q.steps.length > 0) {
          for (let s = 0; s < q.steps.length; s++) {
            const val = Number(reviewAnswers[`ps_${i}_${s}`]);
            stepMarks.push({ stepNo: s + 1, awarded: val });
            questionTotal += val;
          }
        } else {
          const val = Number(reviewAnswers[`ps_${i}_0`]);
          stepMarks.push({ stepNo: 1, awarded: val });
          questionTotal = val;
        }

        const feedback = reviewFeedback[`pf_${i}`] || '';
        questionReviews.push({
          questionId: q.id,
          maxMarks: q.marks,
          marksAwarded: questionTotal,
          stepMarks,
          feedback
        });
        totalScore += questionTotal;
      }

      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/subjective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          attemptId: activeAttempt.id,
          questionReviews,
          totalScore
        })
      });

      if (!res.ok) {
        throw new Error('Failed to submit final grades.');
      }

      alert(`✅ Grades finalized successfully! Total: ${totalScore}`);
      closeAttemptModal();
      await fetchAttempts();
    } catch (err: any) {
      alert(err.message || 'Error saving grading.');
    } finally {
      setSubmittingReview(false);
    }
  };

  const handleResetAttempt = async (attemptId: string, studentName: string) => {
    if (!window.confirm(`⚠️ Are you sure you want to RESET the attempt of ${studentName}? This will delete their grades/answers and let them retake the test. This cannot be undone.`)) {
      return;
    }
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/exams/subjective', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'delete',
          attemptId
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.message || 'Failed to reset attempt.');
      }

      alert('✅ Attempt successfully reset!');
      await fetchAttempts();
    } catch (err: any) {
      alert(err.message || 'Error occurred resetting attempt.');
    }
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading subjective attempts...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>


      {/* Page Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800, cursor: 'pointer' }} onClick={() => router.push('/admin')}>YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>Teacher Final Review</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Moderate and canonicalize student subjective marks</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main content grid */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto' }}>
        <button 
          onClick={() => router.push('/admin/exams')}
          className="btn btn-secondary" 
          style={{ marginBottom: '16px', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
        >
          ← Back to Exams
        </button>
        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
            {error}
          </div>
        )}

        <div className="card" style={{ padding: '20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', marginBottom: '20px' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800 }}>📝 {examName}</h2>
          <div style={{ color: 'var(--text-muted)', fontSize: '12px', marginTop: '6px' }}>{examMeta}</div>
        </div>


        {examMode === 'home' ? (
          <div className="alert-box alert-box-info" style={{ display: 'block', marginBottom: '20px', fontSize: '12.5px', lineHeight: 1.6 }}>
            🏠 <strong>Home Tests:</strong> Student writes answers on paper while questions & timer run on screen. Parents evaluate answers against keyword-highlighted model answers and award marks. Parent review marks are final for Home Tests.<br/>
            ⚠️ <strong>Discrepancies:</strong> Highlights student attempts where the variance between Parent Home reviews and Peer Classroom reviews on overlapping questions is significant (greater than 25% of total marks).
          </div>
        ) : (
          <div className="alert-box alert-box-info" style={{ display: 'block', marginBottom: '20px', fontSize: '12.5px', lineHeight: 1.6 }}>
            🏫 <strong>Classroom Tests:</strong> Student writes answers on paper while questions & timer run on screen and attempts are peer evaluated. Grading completed here by Teacher records the <strong>canonical final score (Self)</strong>.
          </div>
        )}

        {/* Attempts Table */}
        <div id="final-review-table-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
              <thead>
                {examMode === 'home' ? (
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '12px', color: 'var(--text-muted)' }}>
                    <th onClick={() => handleSort('student')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Student {sortField === 'student' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('status')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Status {sortField === 'status' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '12px 16px' }}>Reference score (Parent)</th>
                    <th style={{ padding: '12px 16px' }}>Discrepancies</th>
                    <th onClick={() => handleSort('finalScore')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Final grading {sortField === 'finalScore' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '12px 16px', textAlign: 'right' }}>Action</th>
                  </tr>
                ) : (
                  <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontSize: '12px', color: 'var(--text-muted)' }}>
                    <th onClick={() => handleSort('student')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Student {sortField === 'student' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('examPercent')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Exam % {sortField === 'examPercent' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('weeklyAvgPercent')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Weekly Average % {sortField === 'weeklyAvgPercent' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th onClick={() => handleSort('diffPercent')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Difference % {sortField === 'diffPercent' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '12px 16px' }}>Peer Score</th>
                    <th onClick={() => handleSort('finalScore')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                      Final grading {sortField === 'finalScore' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                    </th>
                    <th style={{ padding: '12px 16px', textAlign: 'right' }}>Action</th>
                  </tr>
                )}
              </thead>
              <tbody>
                {sortedAttempts.length === 0 ? (
                  <tr>
                    <td colSpan={examMode === 'home' ? 6 : 7} style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '13px' }}>
                      No completed student attempts found for this exam yet.
                    </td>
                  </tr>
                ) : (
                  sortedAttempts.map(a => {
                    const isHome = examMode === 'home';
                    const scoreText = isHome
                      ? (a.parentScore !== null ? `Parent: ${a.parentScore}/${a.totalMarks}` : '—')
                      : (a.peerScore !== null ? `Peer: ${a.peerScore}/${a.totalMarks}` : '—');

                    if (isHome) {
                      return (
                        <tr 
                          key={a.id} 
                          onClick={() => openAttempt(a.id)}
                          style={{ cursor: 'pointer', borderBottom: '1px solid var(--border-light)', fontSize: '13px' }}
                          className="attempt-row-hover"
                        >
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>{studentMap[a.studentCode] || 'Student'}</td>
                          <td style={{ padding: '12px 16px', textTransform: 'capitalize' }}>{a.status}</td>
                          <td style={{ padding: '12px 16px' }}>{scoreText}</td>
                          <td style={{ padding: '12px 16px' }}>—</td>
                          <td style={{ padding: '12px 16px' }}>
                            {a.parentScore !== null ? (
                              <span style={{ background: 'rgba(76,175,80,0.1)', color: 'var(--success)', padding: '4px 10px', borderRadius: '12px', fontSize: '11px', fontWeight: 600 }}>
                                Parent Final: {a.parentScore}/{a.totalMarks}
                              </span>
                            ) : (
                              <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>Pending Parent Review</span>
                            )}
                          </td>
                          <td style={{ padding: '12px 16px', textAlign: 'right' }} onClick={(e) => e.stopPropagation()}>
                            <button
                              className="btn btn-secondary btn-sm"
                              style={{ 
                                padding: '2px 8px', 
                                fontSize: '11px', 
                                color: 'var(--danger)', 
                                background: 'var(--surface-3)', 
                                border: '1px solid var(--danger)',
                                borderRadius: '4px',
                                cursor: 'pointer'
                              }}
                              onClick={() => handleResetAttempt(a.id, studentMap[a.studentCode] || a.studentCode)}
                            >
                              Reset
                            </button>
                          </td>
                        </tr>
                      );
                    } else {
                      return (
                        <tr 
                          key={a.id} 
                          onClick={() => openAttempt(a.id)}
                          style={{ cursor: 'pointer', borderBottom: '1px solid var(--border-light)', fontSize: '13px' }}
                          className="attempt-row-hover"
                        >
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>{studentMap[a.studentCode] || 'Student'}</td>
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                            {a.examPercent !== undefined && a.examPercent !== null ? `${a.examPercent}%` : '—'}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                            {a.weeklyAvgPercent !== undefined && a.weeklyAvgPercent !== null ? `${a.weeklyAvgPercent}%` : '—'}
                          </td>
                          <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                            {a.examPercent !== undefined && a.examPercent !== null && a.weeklyAvgPercent !== undefined && a.weeklyAvgPercent !== null ? (
                              (() => {
                                const diff = a.examPercent - a.weeklyAvgPercent;
                                const color = diff >= 0 ? 'var(--success)' : 'var(--danger)';
                                const prefix = diff >= 0 ? '+' : '';
                                return (
                                  <span style={{ color }}>
                                    {prefix}{diff}%
                                  </span>
                                );
                              })()
                            ) : '—'}
                          </td>
                          <td style={{ padding: '12px 16px' }}>{scoreText}</td>
                          <td style={{ padding: '12px 16px' }}>
                            {a.isFinalReviewed ? (
                              <span style={{ background: 'rgba(76,175,80,0.1)', color: 'var(--success)', padding: '4px 10px', borderRadius: '12px', fontSize: '11px', fontWeight: 600 }}>
                                Self: {a.finalScore}/{a.totalMarks}
                              </span>
                            ) : (
                              <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>Not Finalized</span>
                            )}
                          </td>
                          <td style={{ padding: '12px 16px', textAlign: 'right' }} onClick={(e) => e.stopPropagation()}>
                            <button
                              className="btn btn-secondary btn-sm"
                              style={{ 
                                padding: '2px 8px', 
                                fontSize: '11px', 
                                color: 'var(--danger)', 
                                background: 'var(--surface-3)', 
                                border: '1px solid var(--danger)',
                                borderRadius: '4px',
                                cursor: 'pointer'
                              }}
                              onClick={() => handleResetAttempt(a.id, studentMap[a.studentCode] || a.studentCode)}
                            >
                              Reset
                            </button>
                          </td>
                        </tr>
                      );
                    }
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </main>

      {/* Attempt Modal for Grading details */}
      {selectedAttemptId && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.65)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface-popover)', color: 'var(--text)', borderRadius: 'var(--radius-lg)', maxWidth: '750px', width: '92%', maxHeight: '90vh', display: 'flex', flexDirection: 'column', overflow: 'hidden', border: '1px solid var(--border-popover)', boxShadow: 'var(--shadow-lg)' }}>
            
            <div style={{ padding: '16px 20px', background: 'var(--surface-2)', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ fontSize: '15px', fontWeight: 700, margin: 0, color: 'var(--text)' }}>
                📝 Finalize Grades for {studentMap[activeAttempt?.studentCode] || 'Student'}
              </h3>
              <button onClick={closeAttemptModal} style={{ background: 'none', border: 'none', color: 'var(--text-muted)', fontSize: '18px', cursor: 'pointer' }}>✕</button>
            </div>

            {modalLoading ? (
              <div style={{ padding: '50px', textAlign: 'center', flex: 1, color: 'var(--text-muted)' }}>
                <div className="spinner"></div> Loading attempt details...
              </div>
            ) : (
              <>
                <div style={{ padding: '20px', overflowY: 'auto', maxHeight: 'calc(90vh - 140px)', display: 'flex', flexDirection: 'column', gap: '20px', flex: '1 1 auto' }}>
                  
                  {/* Overall Scores Header Banner */}
                  <div style={{ background: 'var(--surface-2)', border: '1px solid var(--border)', borderRadius: 'var(--radius-md)', padding: '12px 16px', display: 'flex', flexWrap: 'wrap', gap: '16px', alignItems: 'center', justifyContent: 'space-between' }}>
                    <div>
                      <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 'bold', letterSpacing: '0.5px' }}>STUDENT NAME</span>
                      <strong style={{ fontSize: '14px', color: 'var(--text)' }}>
                        {(activeAttempt?.studentCode ? (studentMap[activeAttempt.studentCode] || activeAttempt.studentCode) : 'Student')}
                      </strong>
                    </div>

                    <div style={{ display: 'flex', gap: '12px', alignItems: 'center', flexWrap: 'wrap' }}>
                      {activeAttempt?.parentScore !== undefined && activeAttempt?.parentScore !== null && (
                        <div style={{ background: 'var(--surface-popover)', padding: '6px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--success)', textAlign: 'center' }}>
                          <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 'bold' }}>👨‍👩‍👦 PARENT SCORE</span>
                          <strong style={{ fontSize: '14px', color: 'var(--success)' }}>
                            {activeAttempt.parentScore} / {activeAttempt.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}
                          </strong>
                        </div>
                      )}

                      {activeAttempt?.peerScore !== undefined && activeAttempt?.peerScore !== null && (
                        <div style={{ background: 'var(--surface-popover)', padding: '6px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', textAlign: 'center' }}>
                          <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 'bold' }}>👥 PEER SCORE</span>
                          <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>
                            {activeAttempt.peerScore} / {activeAttempt.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}
                          </strong>
                        </div>
                      )}

                      {activeAttempt?.finalScore !== undefined && activeAttempt?.finalScore !== null && (
                        <div style={{ background: 'var(--surface-popover)', padding: '6px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--accent)', textAlign: 'center' }}>
                          <span style={{ fontSize: '10px', color: 'var(--text-muted)', display: 'block', fontWeight: 'bold' }}>⭐ CANONICAL FINAL SCORE</span>
                          <strong style={{ fontSize: '14px', color: 'var(--accent)' }}>
                            {activeAttempt.finalScore} / {activeAttempt.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}
                          </strong>
                        </div>
                      )}
                    </div>
                  </div>

                  {activeQuestions.map((q, idx) => {
                    // Grading solution text
                    let answerHtml = '';
                    if (q.answerLines && q.answerLines.length > 0) {
                      answerHtml = q.answerLines.map(l => `<div style="margin:4px 0;">${l.lineNo}. ${formatRichText(l.text)}</div>`).join('');
                    } else if (q.solution) {
                      answerHtml = `<div>${formatRichText(q.solution)}</div>`;
                    } else {
                      answerHtml = '<em>No model answer config.</em>';
                    }

                    // Robust matching for parent & peer evaluation items per question
                    const parentVal = activeEvaluations?.find((e: any) => 
                      (e.evaluatorType === 'parent' || e.reviewerType === 'parent' || e.source === 'parent_subjective_review') &&
                      (
                        (q.id && String(e.questionId) === String(q.id)) ||
                        (q.questionCode && String(e.questionId) === String(q.questionCode)) ||
                        (e.rubricUsed && String(e.rubricUsed) === String(q.id)) ||
                        (e.questionId === String(idx)) ||
                        (e.questionId === `q_${idx}`)
                      )
                    );

                    const peerVal = activeEvaluations?.find((e: any) => 
                      (e.evaluatorType === 'peer' || e.reviewerType === 'peer' || e.source === 'peer_subjective_review') &&
                      (
                        (q.id && String(e.questionId) === String(q.id)) ||
                        (q.questionCode && String(e.questionId) === String(q.questionCode)) ||
                        (e.rubricUsed && String(e.rubricUsed) === String(q.id)) ||
                        (e.questionId === String(idx)) ||
                        (e.questionId === `q_${idx}`)
                      )
                    );

                    return (
                      <div key={q.id || idx} style={{ background: 'var(--surface-popover)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border)', overflow: 'hidden', flexShrink: 0 }}>
                        <div style={{ padding: '10px 14px', background: 'var(--surface-2)', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', fontSize: '12.5px', color: 'var(--text)' }}>
                          <span style={{ fontWeight: 700, color: 'var(--accent)' }}>Question {idx + 1}</span>
                          <span style={{ fontWeight: 600, color: 'var(--text-muted)' }}>Max: {q.marks} Marks</span>
                        </div>

                        <div style={{ padding: '16px' }}>
                          <p className="math-container" style={{ fontSize: '14px', color: 'var(--text)', margin: '0 0 16px 0', lineHeight: 1.6, whiteSpace: 'pre-line', fontWeight: 600 }}>
                            {preprocessMathText(q.text)}
                          </p>

                          {/* Per-Question Parent Graded Score Badge */}
                          {(parentVal || activeAttempt?.parentScore !== undefined) && (
                            <div style={{ background: 'rgba(22, 163, 74, 0.08)', border: '1px solid var(--success)', borderRadius: 'var(--radius-sm)', padding: '10px 14px', marginBottom: '14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <span style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--success)' }}>👨‍👩‍👦 Parent Graded Score:</span>
                              <span style={{ fontSize: '13.5px', fontWeight: 800, color: 'var(--success)' }}>
                                {parentVal ? `${parentVal.marksAwarded} / ${parentVal.maxMarks}` : `${activeAttempt?.parentScore} / ${activeAttempt?.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}`}
                              </span>
                            </div>
                          )}

                          {/* Per-Question Peer Graded Score Badge */}
                          {peerVal && (
                            <div style={{ background: 'var(--surface-2)', border: '1px solid var(--accent)', borderRadius: 'var(--radius-sm)', padding: '10px 14px', marginBottom: '14px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <span style={{ fontSize: '12.5px', fontWeight: 700, color: 'var(--accent)' }}>👥 Peer Graded Score:</span>
                              <span style={{ fontSize: '13.5px', fontWeight: 800, color: 'var(--accent)' }}>
                                {peerVal.marksAwarded} / {peerVal.maxMarks}
                              </span>
                            </div>
                          )}

                          {/* Reference solutions */}
                          <div style={{ background: 'rgba(22, 163, 74, 0.05)', borderLeft: '4px solid var(--success)', padding: '12px 14px', borderRadius: '4px', fontSize: '12.5px', marginBottom: '16px', color: 'var(--text)' }}>
                            <strong style={{ color: 'var(--success)', fontSize: '12px' }}>📖 Model Answer & Key:</strong>
                            <div className="math-container" dangerouslySetInnerHTML={{ __html: answerHtml }} style={{ marginTop: '6px', whiteSpace: 'pre-line', lineHeight: 1.6 }} />
                          </div>

                          {/* Reference Evaluations grid */}
                          {(parentVal || peerVal || activeAttempt?.parentScore !== undefined || activeAttempt?.peerScore !== undefined) && (
                            <div style={{ display: 'flex', gap: '12px', marginBottom: '14px', fontSize: '11.5px', flexWrap: 'wrap' }}>
                              {(parentVal || activeAttempt?.parentScore !== undefined) && (
                                <div style={{ background: 'var(--surface)', padding: '6px 12px', borderRadius: '4px', border: '1px solid #16a34a44', color: '#16a34a', fontWeight: 'bold' }}>
                                  👨‍👩‍👦 Parent Graded: {parentVal ? `${parentVal.marksAwarded}/${parentVal.maxMarks}` : `Overall ${activeAttempt?.parentScore}/${activeAttempt?.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}`}
                                  {parentVal?.feedback && <span style={{ display: 'block', fontWeight: 'normal', fontSize: '10.5px', color: 'var(--text-muted)' }}>"{parentVal.feedback}"</span>}
                                </div>
                              )}
                              {(peerVal || activeAttempt?.peerScore !== undefined) && (
                                <div style={{ background: 'var(--surface)', padding: '6px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', color: 'var(--accent)', fontWeight: 'bold' }}>
                                  👥 Peer Graded: {peerVal ? `${peerVal.marksAwarded}/${peerVal.maxMarks}` : `Overall ${activeAttempt?.peerScore}/${activeAttempt?.totalMarks || activeQuestions.reduce((a, b) => a + (b.marks || 0), 0)}`}
                                  {peerVal?.feedback && <span style={{ display: 'block', fontWeight: 'normal', fontSize: '10.5px', color: 'var(--text-muted)' }}>"{peerVal.feedback}"</span>}
                                </div>
                              )}
                            </div>
                          )}

                          {/* Grading Score Inputs */}
                          <strong style={{ fontSize: '12.5px', display: 'block', marginBottom: '8px', color: 'var(--text)' }}>✏️ Award Canonical Marks:</strong>

                          {q.steps && q.steps.length > 0 ? (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                              {q.steps.map((step, si) => (
                                <div key={si} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface-2)', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', color: 'var(--text)' }}>
                                  <span style={{ fontSize: '12px' }}>{step.description}</span>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {step.marks}</span>
                                    <input 
                                      type="number" 
                                      min="0" 
                                      max={step.marks} 
                                      step="0.5" 
                                      disabled={!!activeAttempt?.isFinalReviewed}
                                      value={reviewAnswers[`ps_${idx}_${si}`] ?? ""}
                                      onChange={(e) => {
                                        const raw = e.target.value;
                                        if (raw === "") {
                                          setReviewAnswers(prev => {
                                            const copy = { ...prev };
                                            delete copy[`ps_${idx}_${si}`];
                                            return copy;
                                          });
                                        } else {
                                          const val = Math.min(step.marks, Math.max(0, parseFloat(raw) || 0));
                                          setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_${si}`]: val }));
                                        }
                                      }}
                                      style={{ width: '70px', padding: '6px', border: '2px solid var(--accent)', borderRadius: '6px', textAlign: 'center', background: 'var(--surface-2)', color: 'var(--text)', fontWeight: 800, fontSize: '14px', outline: 'none' }}
                                    />
                                  </div>
                                </div>
                              ))}
                            </div>
                          ) : (
                            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--surface-2)', border: '1.5px solid var(--border)', borderRadius: 'var(--radius-sm)', color: 'var(--text)' }}>
                              <span style={{ fontSize: '12px', fontWeight: 600 }}>Overall Score</span>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Max: {q.marks}</span>
                                <input 
                                  type="number" 
                                  min="0" 
                                  max={q.marks} 
                                  step="0.5" 
                                  disabled={!!activeAttempt?.isFinalReviewed}
                                  value={reviewAnswers[`ps_${idx}_0`] ?? ""}
                                  onChange={(e) => {
                                    const raw = e.target.value;
                                    if (raw === "") {
                                      setReviewAnswers(prev => {
                                        const copy = { ...prev };
                                        delete copy[`ps_${idx}_0`];
                                        return copy;
                                      });
                                    } else {
                                      const val = Math.min(q.marks, Math.max(0, parseFloat(raw) || 0));
                                      setReviewAnswers(prev => ({ ...prev, [`ps_${idx}_0`]: val }));
                                    }
                                  }}
                                  style={{ width: '70px', padding: '6px', border: '2px solid var(--accent)', borderRadius: '6px', textAlign: 'center', background: 'var(--surface-2)', color: 'var(--text)', fontWeight: 800, fontSize: '14px', outline: 'none' }}
                                />
                              </div>
                            </div>
                          )}

                          <textarea 
                            placeholder="Add evaluation comments..."
                            rows={2}
                            disabled={!!activeAttempt?.isFinalReviewed}
                            value={reviewFeedback[`pf_${idx}`] || ''}
                            onChange={(e) => setReviewFeedback(prev => ({ ...prev, [`pf_${idx}`]: e.target.value }))}
                            style={{ width: '100%', marginTop: '12px', padding: '8px 12px', border: '1px solid var(--border)', borderRadius: 'var(--radius-sm)', fontSize: '12px', background: 'var(--surface-2)', color: 'var(--text)', fontFamily: 'inherit' }}
                          />
                        </div>
                      </div>
                    );
                  })}
                </div>

                {/* Modal actions footer */}
                <div style={{ padding: '16px 20px', background: 'var(--surface-2)', borderTop: '1px solid var(--border)', display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
                  <button className="btn btn-secondary" onClick={closeAttemptModal}>Close</button>
                  {!activeAttempt?.isFinalReviewed && (
                    <button className="btn btn-primary" onClick={submitFinalGrades} disabled={submittingReview}>
                      {submittingReview ? 'Saving Grading...' : '✅ Finalize Grading'}
                    </button>
                  )}
                </div>
              </>
            )}
          </div>
        </div>
      )}
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title={`Subjective Final Grading Review — ${examName}`}
        filename="Subjective_Grading_Review.pdf"
        sections={[
          { id: 'roster', name: 'Subjective Submissions Grading Table', elementId: 'final-review-table-section' }
        ]}
      />
    </div>
  );
}

export default function TeacherFinalReviewPage() {
  return (
    <Suspense fallback={
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading page...
        </div>
      </div>
    }>
      <TeacherFinalReviewContent />
    </Suspense>
  );
}
