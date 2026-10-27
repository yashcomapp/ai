'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import TargetPicker from '@/components/admin/exams/TargetPicker';
import { Batch } from '@/types/batch.types';
import { formatDateTimeIST, formatTimeIST } from '@/lib/dateUtils';
import { Video, Users, CheckCircle, AlertCircle, Copy, ExternalLink, Square, Play, Sparkles } from 'lucide-react';

interface Student {
  id: string;
  name: string;
  studentCode: string;
  batchIds?: string[];
  batchId?: string;
  [key: string]: any;
}

interface LiveSession {
  id: string;
  title: string;
  subject?: string;
  targetType: 'batch' | 'student' | 'mixed';
  targetBatches: string[];
  targetStudents: string[];
  roomName: string;
  passcode?: string;
  status: 'live' | 'ended';
  startedAt: string;
  endedAt?: string | null;
  startedBy?: string;
  teacherUrl?: string;
}

export default function AdminLiveClassroomPage() {
  const { firebaseUser } = useAuth();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);
  const [copiedPin, setCopiedPin] = useState(false);

  // Batches & Students
  const [batches, setBatches] = useState<Batch[]>([]);
  const [students, setStudents] = useState<Student[]>([]);

  // Live session state
  const [activeSession, setActiveSession] = useState<LiveSession | null>(null);
  const [recentSessions, setRecentSessions] = useState<LiveSession[]>([]);

  // Create form state
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [title, setTitle] = useState('');
  const [subject, setSubject] = useState('');
  const [targetType, setTargetType] = useState<'batch' | 'student' | 'mixed'>('batch');
  const [selectedBatches, setSelectedBatches] = useState<Set<string>>(new Set());
  const [selectedStudents, setSelectedStudents] = useState<Set<string>>(new Set());

  // Load master data and live classroom state
  const loadData = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    setError('');

    try {
      const idToken = await firebaseUser.getIdToken();

      // 1. Load Batches & Students
      const batchesRes = await fetch('/api/admin/batches', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!batchesRes.ok) throw new Error('Failed to load batches.');
      const batchesData = await batchesRes.json();
      setBatches(batchesData.batches || []);
      // Exclude deactivated accounts per Rule 2C
      setStudents((batchesData.students || []).filter((s: any) => s.status !== 'inactive'));

      // 2. Load Live Classroom state
      const classroomRes = await fetch('/api/admin/live-classroom', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!classroomRes.ok) throw new Error('Failed to load live classroom status.');
      const classroomData = await classroomRes.json();
      setActiveSession(classroomData.activeSession || null);
      setRecentSessions(classroomData.recentSessions || []);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error loading live classroom.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, [firebaseUser]);

  // Group students by batch for the TargetPicker
  const getStudentsGroupedByBatch = () => {
    const grouped: { [batchId: string]: { batchName: string; list: any[] } } = {};
    const unassigned: any[] = [];

    batches.forEach(b => {
      grouped[b.id] = { batchName: b.name, list: [] };
    });

    students.forEach(s => {
      const sBatchIds = s.batchIds && s.batchIds.length ? s.batchIds : (s.batchId ? [s.batchId] : []);
      if (sBatchIds.length === 0) {
        unassigned.push(s);
      } else {
        sBatchIds.forEach(bid => {
          if (grouped[bid]) {
            grouped[bid].list.push(s);
          } else {
            grouped[bid] = { batchName: bid, list: [s] };
          }
        });
      }
    });

    return { grouped, unassigned };
  };

  const handleToggleBatch = (batchId: string) => {
    const next = new Set(selectedBatches);
    if (next.has(batchId)) next.delete(batchId);
    else next.add(batchId);
    setSelectedBatches(next);
  };

  const handleToggleStudent = (studentCode: string) => {
    const next = new Set(selectedStudents);
    if (next.has(studentCode)) next.delete(studentCode);
    else next.add(studentCode);
    setSelectedStudents(next);
  };

  const handleSelectAllBatches = () => {
    if (selectedBatches.size === batches.length) {
      setSelectedBatches(new Set());
    } else {
      setSelectedBatches(new Set(batches.map(b => b.id)));
    }
  };

  // Start Live Session
  const handleStartSession = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) {
      alert('Please enter a session title.');
      return;
    }

    if (targetType === 'batch' && selectedBatches.size === 0) {
      alert('Please select at least one batch.');
      return;
    }

    if (targetType === 'student' && selectedStudents.size === 0) {
      alert('Please select at least one student.');
      return;
    }

    if (targetType === 'mixed' && selectedBatches.size === 0 && selectedStudents.size === 0) {
      alert('Please select at least one batch or student.');
      return;
    }

    setSubmitting(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/live-classroom', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'start',
          title: title.trim(),
          subject: subject.trim(),
          targetType,
          targetBatches: Array.from(selectedBatches),
          targetStudents: Array.from(selectedStudents)
        })
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to start live session.');

      setActiveSession(data.session);
      setShowCreateModal(false);
      setTitle('');
      setSubject('');
      setSelectedBatches(new Set());
      setSelectedStudents(new Set());

      // Open Teacher window immediately in a new browser tab
      if (data.session.teacherUrl) {
        window.open(data.session.teacherUrl, '_blank', 'noopener,noreferrer');
      }

      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error launching session.');
    } finally {
      setSubmitting(false);
    }
  };

  // End Live Session
  const handleEndSession = async (sessionId: string) => {
    if (!window.confirm('Are you sure you want to end this live session?\n\nStudents will see that the live class has ended.')) {
      return;
    }

    setSubmitting(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/live-classroom', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'end',
          sessionId
        })
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to end live session.');

      setActiveSession(null);
      await loadData();
    } catch (err: any) {
      alert(err.message || 'Error ending session.');
    } finally {
      setSubmitting(false);
    }
  };

  // Copy student focus mode link
  const handleCopyStudentLink = (roomName: string) => {
    const url = `https://meet.jit.si/${roomName}#config.channelLastN=1&config.startWithAudioMuted=true&config.startWithVideoMuted=false`;
    navigator.clipboard.writeText(url);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 2000);
  };

  const handleCopyPin = (pin: string) => {
    navigator.clipboard.writeText(pin);
    setCopiedPin(true);
    setTimeout(() => setCopiedPin(false), 2000);
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '80vh' }}>
        <div className="spinner" /> Loading Live Classroom Hub...
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '1000px', margin: '0 auto', padding: '24px 16px' }}>
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '24px', flexWrap: 'wrap', gap: '12px' }}>
        <div>
          <h1 style={{ fontSize: '1.6rem', fontWeight: 800, margin: '0 0 4px', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span>🎥</span> Live Classroom (Jitsi Focus Mode)
          </h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: 0 }}>
            Launch zero-cost live interactive video classes. Targeted students enter Focus Mode (they only see you + your screen share, while you monitor their cameras).
          </p>
        </div>

        {!activeSession && (
          <button
            className="btn btn-primary"
            onClick={() => setShowCreateModal(true)}
            style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 18px', fontWeight: 700 }}
          >
            <Play size={16} /> Start Live Classroom
          </button>
        )}
      </div>

      {error && (
        <div className="alert-box alert-box-danger" style={{ marginBottom: '20px' }}>
          {error}
        </div>
      )}

      {/* ACTIVE LIVE CLASS CARD */}
      {activeSession ? (
        <div className="card" style={{
          background: 'linear-gradient(135deg, rgba(239, 68, 68, 0.08), rgba(99, 102, 241, 0.08))',
          border: '2px solid var(--danger)',
          borderRadius: 'var(--radius-lg)',
          padding: '24px',
          marginBottom: '28px',
          boxShadow: '0 8px 24px rgba(239, 68, 68, 0.15)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px', flexWrap: 'wrap', gap: '10px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ 
                background: 'var(--danger)', 
                color: '#fff', 
                padding: '4px 12px', 
                borderRadius: '16px', 
                fontSize: '11px', 
                fontWeight: 800,
                letterSpacing: '0.5px',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}>
                <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#fff' }} />
                LIVE IN PROGRESS
              </span>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                Started at {formatTimeIST(activeSession.startedAt)} • Auto-expires in 100 mins
              </span>
            </div>

            <button
              onClick={() => handleEndSession(activeSession.id)}
              disabled={submitting}
              className="btn btn-danger"
              style={{ display: 'flex', alignItems: 'center', gap: '6px', padding: '8px 14px', fontSize: '12.5px', fontWeight: 700 }}
            >
              <Square size={14} /> End Live Class
            </button>
          </div>

          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, margin: '0 0 6px', color: 'var(--text)' }}>
            {activeSession.title}
          </h2>
          {activeSession.subject && (
            <div style={{ fontSize: '13px', color: 'var(--accent)', fontWeight: 700, marginBottom: '14px' }}>
              Subject: {activeSession.subject}
            </div>
          )}

          {/* Target Audience Summary */}
          <div style={{ background: 'var(--surface)', padding: '12px 16px', borderRadius: 'var(--radius)', border: '1px solid var(--border-light)', marginBottom: '14px', display: 'flex', gap: '20px', flexWrap: 'wrap', fontSize: '12px', alignItems: 'center' }}>
            <div>
              <span style={{ color: 'var(--text-muted)' }}>Audience Type: </span>
              <strong>{activeSession.targetType === 'batch' ? 'Selected Batches' : activeSession.targetType === 'student' ? 'Individual Students' : 'Mixed'}</strong>
            </div>
            {activeSession.targetBatches?.length > 0 && (
              <div>
                <span style={{ color: 'var(--text-muted)' }}>Batches: </span>
                <strong>
                  {activeSession.targetBatches.map(bId => batches.find(b => b.id === bId)?.name || bId).join(', ')}
                </strong>
              </div>
            )}
            {activeSession.targetStudents?.length > 0 && (
              <div>
                <span style={{ color: 'var(--text-muted)' }}>Direct Students: </span>
                <strong>{activeSession.targetStudents.length} Students</strong>
              </div>
            )}
            {activeSession.passcode && (
              <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ color: 'var(--text-muted)' }}>Room PIN / Passcode:</span>
                <span style={{ padding: '2px 8px', background: 'var(--primary-glow)', color: 'var(--primary)', fontWeight: 800, borderRadius: '4px', letterSpacing: '1px' }}>
                  {activeSession.passcode}
                </span>
              </div>
            )}
          </div>

          {/* Moderator Security Guidance */}
          <div style={{
            padding: '8px 12px',
            marginBottom: '18px',
            borderRadius: 'var(--radius-sm)',
            background: 'var(--surface-2)',
            border: '1px solid var(--border-light)',
            fontSize: '11.5px',
            color: 'var(--text-muted)',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }}>
            <span>🛡️</span>
            <span>
              <strong>Host Security Tip:</strong> After entering the room, click the <strong>Shield icon</strong> in Jitsi toolbar &rarr; <em>Add password</em> (enter PIN <strong>{activeSession.passcode || 'above'}</strong>) or enable <em>Lobby</em> to admit students manually.
            </span>
          </div>

          {/* Quick Action Links */}
          <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
            <a
              href={activeSession.teacherUrl || `https://meet.jit.si/${activeSession.roomName}#config.channelLastN=-1`}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-primary"
              style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 18px', fontWeight: 700, fontSize: '13px' }}
            >
              <ExternalLink size={16} /> Open Teacher Moderator View
            </a>

            <button
              onClick={() => handleCopyStudentLink(activeSession.roomName)}
              className="btn btn-secondary"
              style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 16px', fontWeight: 600, fontSize: '13px' }}
            >
              <Copy size={16} /> {copiedLink ? 'Copied Focus Link!' : 'Copy Student Focus Mode Link'}
            </button>

            {activeSession.passcode && (
              <button
                onClick={() => handleCopyPin(activeSession.passcode!)}
                className="btn btn-secondary"
                style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 16px', fontWeight: 600, fontSize: '13px' }}
              >
                <Copy size={16} /> {copiedPin ? 'Copied PIN!' : `Copy PIN (${activeSession.passcode})`}
              </button>
            )}
          </div>
        </div>
      ) : (
        /* Empty Live Banner */
        <div className="card" style={{
          background: 'var(--surface)',
          borderRadius: 'var(--radius-lg)',
          padding: '32px 20px',
          textAlign: 'center',
          border: '1px dashed var(--border-light)',
          marginBottom: '28px'
        }}>
          <div style={{ fontSize: '32px', marginBottom: '8px' }}>📡</div>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, margin: '0 0 6px' }}>No Live Classroom in Progress</h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '13px', margin: '0 0 16px', maxWidth: '480px', marginInline: 'auto' }}>
            Click below to start a live class. You can select specific batches or individual students to invite.
          </p>
          <button
            className="btn btn-primary"
            onClick={() => setShowCreateModal(true)}
            style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '10px 20px', fontWeight: 700 }}
          >
            <Play size={16} /> Start Live Classroom Now
          </button>
        </div>
      )}

      {/* CREATE LIVE CLASSROOM MODAL */}
      {showCreateModal && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0,0,0,0.65)',
          backdropFilter: 'blur(6px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 10000,
          padding: '16px'
        }}>
          <div className="card" style={{
            background: 'var(--surface)',
            borderRadius: 'var(--radius-lg)',
            maxWidth: '650px',
            width: '100%',
            maxHeight: '90vh',
            overflowY: 'auto',
            padding: '24px',
            border: '1px solid var(--border-light)',
            boxShadow: 'var(--shadow-xl)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '18px' }}>
              <h2 style={{ fontSize: '1.3rem', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                🚀 Launch Live Classroom
              </h2>
              <button
                onClick={() => setShowCreateModal(false)}
                style={{ background: 'none', border: 'none', fontSize: '18px', cursor: 'pointer', color: 'var(--text-muted)' }}
              >
                ✕
              </button>
            </div>

            <form onSubmit={handleStartSession}>
              <div style={{ marginBottom: '14px' }}>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '4px' }}>
                  Session Title *
                </label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g. Class 10 Math - Quadratic Equations & Doubt Solving"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  required
                  style={{ width: '100%', padding: '10px 12px', fontSize: '13px' }}
                />
              </div>

              <div style={{ marginBottom: '18px' }}>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 700, marginBottom: '4px' }}>
                  Subject (Optional)
                </label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g. Mathematics, Science"
                  value={subject}
                  onChange={(e) => setSubject(e.target.value)}
                  style={{ width: '100%', padding: '8px 12px', fontSize: '13px' }}
                />
              </div>

              {/* TARGET PICKER: Batches & Students Selector (Same as Exam Assignment) */}
              <div style={{ background: 'var(--bg-soft)', borderRadius: 'var(--radius)', padding: '14px', border: '1px solid var(--border-light)', marginBottom: '14px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <div style={{ fontWeight: 800, fontSize: '12.5px', color: 'var(--text)' }}>
                    🎯 Select Target Classes / Students
                  </div>
                  {targetType === 'batch' && (
                    <button
                      type="button"
                      onClick={handleSelectAllBatches}
                      style={{ background: 'none', border: 'none', color: 'var(--accent)', fontSize: '11px', fontWeight: 700, cursor: 'pointer' }}
                    >
                      {selectedBatches.size === batches.length ? 'Deselect All' : 'Select All Classes'}
                    </button>
                  )}
                </div>

                <TargetPicker
                  targetType={targetType}
                  onChangeTargetType={setTargetType}
                  batches={batches}
                  selectedBatches={selectedBatches}
                  onToggleBatch={handleToggleBatch}
                  selectedStudents={selectedStudents}
                  onToggleStudent={handleToggleStudent}
                  getStudentsGroupedByBatch={getStudentsGroupedByBatch}
                />
              </div>

              {/* 100-Minute Session Policy Notice */}
              <div style={{
                padding: '8px 12px',
                marginBottom: '18px',
                borderRadius: 'var(--radius-sm)',
                background: 'var(--surface-2)',
                border: '1px solid var(--border-light)',
                fontSize: '11.5px',
                color: 'var(--text-muted)',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}>
                <span>⏱️</span>
                <span><strong>100-Minute Session Duration:</strong> Public Jitsi sessions are limited to 95 minutes. The classroom automatically expires after 100 minutes.</span>
              </div>

              {/* Launch Action */}
              <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end' }}>
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowCreateModal(false)}
                  disabled={submitting}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="btn btn-primary"
                  disabled={submitting}
                  style={{ padding: '10px 24px', fontWeight: 800 }}
                >
                  {submitting ? 'Starting Session...' : '🚀 Start Live Class (Launch Jitsi)'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* RECENT SESSIONS HISTORY */}
      <div>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 800, marginBottom: '12px' }}>
          📜 Recent Live Sessions
        </h3>

        {recentSessions.length === 0 ? (
          <div style={{ color: 'var(--text-muted)', fontSize: '13px' }}>
            No past live sessions recorded yet.
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {recentSessions.map(sess => (
              <div key={sess.id} className="card" style={{
                background: 'var(--surface)',
                borderRadius: 'var(--radius)',
                padding: '12px 16px',
                border: '1px solid var(--border-light)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: '8px'
              }}>
                <div>
                  <div style={{ fontWeight: 700, fontSize: '13.5px', color: 'var(--text)' }}>
                    {sess.title}
                  </div>
                  <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', marginTop: '2px' }}>
                    {sess.subject ? `${sess.subject} • ` : ''}
                    {formatDateTimeIST(sess.startedAt)}
                    {sess.endedAt ? ` (Ended ${formatTimeIST(sess.endedAt)})` : ''}
                  </div>
                </div>

                <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                  Audience: <strong>{sess.targetType === 'batch' ? `${sess.targetBatches?.length || 0} Batches` : `${sess.targetStudents?.length || 0} Students`}</strong>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
