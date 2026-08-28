'use client';

import React, { useEffect, useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
const ExportPdfModal = dynamic(() => import('@/components/ExportPdfModal').then(m => ({ default: m.ExportPdfModal })), { ssr: false });
import { collection, query, where, onSnapshot } from 'firebase/firestore';
import { ref, push, set, onValue, off, remove, serverTimestamp } from 'firebase/database';
import { db } from '@/lib/firebase/firestore';
import { rtdb } from '@/lib/firebase/rtdb';

interface Session {
  id: string;
  examId: string;
  examName: string;
  examType: string;
  studentCode: string;
  studentName: string;
  currentQuestionIndex: number | null;
  totalQuestions: number | null;
  answeredCount: number | null;
  violations?: {
    tabViolations?: number;
    noFaceCount?: number;
    multipleFacesCount?: number;
    lookingAwayCount?: number;
    headMovementCount?: number;
    awayTimeTotal?: number;
  };
  status: string;
  cameraAvailable: boolean;
  micAvailable?: boolean;
  lastActive: any;
}

const RTC_CONFIG = {
  iceServers: [
    { urls: 'stun:stun.l.google.com:19302' },
    {
      urls: 'turn:openrelay.metered.ca:80',
      username: 'openrelayproject',
      credential: 'openrelayproject'
    },
    {
      urls: 'turn:openrelay.metered.ca:443',
      username: 'openrelayproject',
      credential: 'openrelayproject'
    }
  ]
};

export default function AdminLiveMonitorPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'exam' | 'practice' | 'sync'>('exam');
  const [sessions, setSessions] = useState<{ [key: string]: Session }>({});

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'studentName' | 'status' | 'violations' | 'lastActive'>('lastActive');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');
  const [pdfSelectorOpen, setPdfSelectorOpen] = useState(false);

  // Heartbeat staleness ticker
  const [tickerTime, setTickerTime] = useState(Date.now());

  // WebRTC Video Modal State
  const [videoModal, setVideoModal] = useState({
    show: false,
    studentName: '',
    examId: '',
    studentCode: '',
    status: 'Requesting connection...'
  });
  const [isSpeakerMuted, setIsSpeakerMuted] = useState(true);
  const [isTalking, setIsTalking] = useState(false);
  const [hasAudioTrack, setHasAudioTrack] = useState(false);
  const [hasAdminMic, setHasAdminMic] = useState(false);

  const videoRef = useRef<HTMLVideoElement | null>(null);
  const activeCallRef = useRef<{ close: () => void } | null>(null);
  const localAudioStreamRef = useRef<MediaStream | null>(null);

  // Periodic ticker to recalculate time-ago labels
  useEffect(() => {
    const timer = setInterval(() => {
      setTickerTime(Date.now());
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  // Listen to Firestore active live proctoring sessions
  useEffect(() => {
    if (!firebaseUser) return;

    const qSessions = query(
      collection(db, 'liveExamSessions'),
      where('status', '==', 'in-progress')
    );

    const unsubscribe = onSnapshot(qSessions, (snapshot) => {
      const updated: { [key: string]: Session } = {};
      snapshot.docs.forEach(doc => {
        updated[doc.id] = { id: doc.id, ...doc.data() as any };
      });
      setSessions(updated);
      setLoading(false);
    }, (err) => {
      console.error('liveExamSessions listener error:', err);
      setLoading(false);
    });

    return () => unsubscribe();
  }, [firebaseUser]);

  // Helpers
  const sanitizeForRtdbPath = (s: string) => {
    return String(s).replace(/[.$#\[\]/]/g, '_');
  };

  const getSessionDocId = (examId: string, studentCode: string) => {
    return `${sanitizeForRtdbPath(examId)}_${sanitizeForRtdbPath(studentCode)}`;
  };

  const isAbandoned = (lastActive: any) => {
    if (!lastActive) return false;
    const d = lastActive.toDate ? lastActive.toDate() : new Date(lastActive);
    if (!d || isNaN(d.getTime())) return false;
    const ABANDONED_MS = 5 * 60 * 1000;
    return (Date.now() - d.getTime()) > ABANDONED_MS;
  };

  const isStale = (lastActive: any) => {
    if (!lastActive) return true;
    const d = lastActive.toDate ? lastActive.toDate() : new Date(lastActive);
    return (Date.now() - d.getTime()) > 30000;
  };

  const timeAgo = (lastActive: any) => {
    if (!lastActive) return 'unknown';
    const d = lastActive.toDate ? lastActive.toDate() : new Date(lastActive);
    const secs = Math.round((Date.now() - d.getTime()) / 1000);
    if (secs < 60) return `${secs}s ago`;
    return `${Math.round(secs / 60)}m ago`;
  };

  // Sort handle
  const handleSort = (field: typeof sortField) => {
    if (sortField === field) {
      setSortDir(prev => (prev === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortField(field);
      setSortDir('desc');
    }
  };

  // Filter list by tab and remove abandoned sessions
  const getFilteredList = (type: 'exam' | 'practice' | 'sync') => {
    const list = Object.values(sessions)
      .filter(s => {
        const isSync = s.examId?.startsWith('daily-sync') || 
                       s.examName?.toLowerCase().includes('daily 5-min') || 
                       s.examName?.toLowerCase().includes('parent-child') ||
                       s.examType === 'sync' ||
                       (s as any).type === 'sync';
        if (type === 'sync') return isSync && !isAbandoned(s.lastActive);
        if (type === 'practice') return s.examType === 'practice' && !isSync && !isAbandoned(s.lastActive);
        return s.examType !== 'practice' && !isSync && !isAbandoned(s.lastActive);
      });

    return list.sort((a, b) => {
      let valA: any = 0;
      let valB: any = 0;

      if (sortField === 'studentName') {
        valA = a.studentName || '';
        valB = b.studentName || '';
        return sortDir === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
      } else if (sortField === 'status') {
        valA = a.status || '';
        valB = b.status || '';
        return sortDir === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
      } else if (sortField === 'violations') {
        valA = (a.violations?.tabViolations || 0) + (a.violations?.noFaceCount || 0) + (a.violations?.multipleFacesCount || 0);
        valB = (b.violations?.tabViolations || 0) + (b.violations?.noFaceCount || 0) + (b.violations?.multipleFacesCount || 0);
      } else {
        valA = a.lastActive?.toDate ? a.lastActive.toDate().getTime() : (a.lastActive ? new Date(a.lastActive).getTime() : 0);
        valB = b.lastActive?.toDate ? b.lastActive.toDate().getTime() : (b.lastActive ? new Date(b.lastActive).getTime() : 0);
      }

      return sortDir === 'asc' ? valA - valB : valB - valA;
    });
  };

  // Close peer connection and modal
  const handleCloseVideoModal = () => {
    setVideoModal(prev => ({ ...prev, show: false }));
    if (activeCallRef.current) {
      activeCallRef.current.close();
      activeCallRef.current = null;
    }
    if (localAudioStreamRef.current) {
      localAudioStreamRef.current.getTracks().forEach(t => t.stop());
      localAudioStreamRef.current = null;
    }
    setIsSpeakerMuted(true);
    setIsTalking(false);
    setHasAdminMic(false);
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
  };

  // WebRTC viewer signaling connection (RTDB-based)
  const handleOpenVideoFeed = async (examId: string, studentCode: string, studentName: string) => {
    setVideoModal({
      show: true,
      studentName,
      examId,
      studentCode,
      status: 'Requesting connection...'
    });
    setIsSpeakerMuted(true);
    setIsTalking(false);
    setHasAudioTrack(false);
    setHasAdminMic(false);

    if (videoRef.current) {
      videoRef.current.muted = true;
    }

    try {
      if (!rtdb) {
        throw new Error('Realtime Database is not configured.');
      }

      const sId = getSessionDocId(examId, studentCode);
      const sigRef = ref(rtdb, `webrtcSignaling/${sId}`);

      const pc = new RTCPeerConnection(RTC_CONFIG);
      const remoteStream = new MediaStream();

      // Acquire and add admin mic track for two-way audio (strictly disabled by default)
      let localAudioStream: MediaStream | null = null;
      try {
        localAudioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        if (localAudioStream) {
          localAudioStream.getTracks().forEach(t => {
            t.enabled = false; // Muted by default so teacher voice is NOT transmitted on listen
            pc.addTrack(t, localAudioStream!);
          });
          localAudioStreamRef.current = localAudioStream;
          setHasAdminMic(true);
          console.log('[viewer] Admin microphone track acquired and disabled (Listen-Only default).');
        }
      } catch (e) {
        setHasAdminMic(false);
        console.warn('[viewer] Could not get admin microphone stream:', e);
      }

      if (videoRef.current) {
        videoRef.current.srcObject = remoteStream;
      }

      pc.ontrack = (event) => {
        console.log('[viewer] Track received:', event.track.kind);
        if (event.streams && event.streams[0]) {
          event.streams[0].getTracks().forEach(t => {
            if (!remoteStream.getTracks().includes(t)) {
              remoteStream.addTrack(t);
            }
          });
        } else {
          remoteStream.addTrack(event.track);
        }

        // Dynamically update audio track indicator
        const hasAudio = remoteStream.getAudioTracks().length > 0;
        setHasAudioTrack(hasAudio);

        if (videoRef.current) {
          videoRef.current.srcObject = remoteStream;
          videoRef.current.play().catch(e => console.warn('[viewer] Video autoplay failed:', e));
        }
      };

      pc.onicecandidate = (event) => {
        if (event.candidate) {
          const candidatesRef = ref(rtdb, `webrtcSignaling/${sId}/callerCandidates`);
          const newCandidateRef = push(candidatesRef);
          set(newCandidateRef, event.candidate.toJSON());
        }
      };

      pc.oniceconnectionstatechange = () => {
        console.log('[viewer] iceConnectionState:', pc.iceConnectionState);
        if (pc.iceConnectionState === 'connected' || pc.iceConnectionState === 'completed') {
          setVideoModal(prev => ({ ...prev, status: '🟢 Live' }));
        }
      };

      const offer = await pc.createOffer({ offerToReceiveVideo: true, offerToReceiveAudio: true });
      await pc.setLocalDescription(offer);

      // Create signaling node
      await set(sigRef, {
        requestedAt: serverTimestamp(),
        offer: { type: offer.type, sdp: offer.sdp }
      });

      const appliedKeys = new Set<string>();
      let answerApplied = false;

      // Listen to RTDB response channel
      const unsubscribeSig = onValue(sigRef, async (snap) => {
        const data = snap.val();
        if (!data) return;

        try {
          if (data.answer && !answerApplied) {
            answerApplied = true;
            await pc.setRemoteDescription(new RTCSessionDescription(data.answer));
            
            // Check audio track existence
            if (videoRef.current) {
              const hasAudio = remoteStream.getAudioTracks().length > 0;
              setHasAudioTrack(hasAudio);
            }
          }

          const callee = data.calleeCandidates || {};
          for (const key in callee) {
            if (appliedKeys.has(key)) continue;
            // Only add if answer has already been applied!
            if (!answerApplied) continue;
            
            appliedKeys.add(key);
            try {
              await pc.addIceCandidate(new RTCIceCandidate(callee[key]));
            } catch (e) {
              console.debug('Failed to add candidate:', e);
            }
          }
        } catch (err) {
          console.error('Error parsing RTDB signaling snapshot:', err);
        }
      });

      // Keep call reference to close it later
      activeCallRef.current = {
        close: () => {
          unsubscribeSig();
          pc.close();
          if (localAudioStream) {
            localAudioStream.getTracks().forEach(t => t.stop());
          }
          remove(sigRef).catch(() => {});
        }
      };

      // Set timeout fallback if feed remains empty
      setTimeout(() => {
        if (videoRef.current && (!videoRef.current.srcObject || remoteStream.getVideoTracks().length === 0)) {
          setVideoModal(prev => {
            if (prev.status === 'Requesting connection...') {
              return { ...prev, status: '⌛ Still waiting — student may have closed the tab.' };
            }
            return prev;
          });
        }
      }, 8000);

    } catch (err: any) {
      console.error(err);
      setVideoModal(prev => ({ ...prev, status: `Could not connect: ${err.message}` }));
    }
  };

  const handleToggleSpeaker = () => {
    if (videoRef.current) {
      const next = !isSpeakerMuted;
      setIsSpeakerMuted(next);
      videoRef.current.muted = next;
    }
  };

  const handleToggleTalk = () => {
    if (!localAudioStreamRef.current) return;
    const next = !isTalking;
    setIsTalking(next);
    localAudioStreamRef.current.getTracks().forEach(t => {
      t.enabled = next;
    });
    console.log(`[viewer] Admin microphone transmission set to: ${next}`);
  };

  const renderViolationsBadge = (v?: any) => {
    if (!v) return <span className="viol-pill">✅ Clean</span>;
    const totalViol = (v.tabViolations || 0) + (v.noFaceCount || 0) + (v.multipleFacesCount || 0)
      + (v.lookingAwayCount || 0) + (v.headMovementCount || 0)
      + (v.awayTimeTotal ? Math.round(v.awayTimeTotal / 10) : 0);

    if (totalViol > 0) {
      return (
        <span className={`viol-pill ${totalViol >= 5 ? 'high' : ''}`} style={{ background: totalViol >= 5 ? '#fde2e1' : 'var(--bg-soft)', color: totalViol >= 5 ? '#c0392b' : 'var(--text)', padding: '2px 8px', borderRadius: '10px', fontSize: '11px', whiteSpace: 'nowrap' }}>
          ⚠️ {totalViol}
        </span>
      );
    }
    return <span className="viol-pill" style={{ background: 'var(--bg-soft)', padding: '2px 8px', borderRadius: '10px', fontSize: '11px', whiteSpace: 'nowrap' }}>✅ Clean</span>;
  };

  const list = getFilteredList(activeTab);

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Connecting to live channels...
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
            <h1 style={{ fontSize: '16px', margin: 0 }}>Live Monitor</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Real-time exam sessions & practice activity</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-primary" style={{ padding: '6px 12px', fontSize: '12px' }} onClick={() => setPdfSelectorOpen(true)}>📄 Export PDF</button>
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {/* Tabs Selection with Dynamic Active Badges */}
        <div className="tabs-container" style={{ display: 'flex', gap: '8px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px' }}>
          {(() => {
            const examCount = getFilteredList('exam').length;
            const syncCount = getFilteredList('sync').length;
            const practiceCount = getFilteredList('practice').length;

            return (
              <>
                <button 
                  className={`tab-btn ${activeTab === 'exam' ? 'active' : ''}`}
                  onClick={() => setActiveTab('exam')}
                  style={{
                    padding: '8px 16px',
                    border: 'none',
                    cursor: 'pointer',
                    background: 'none',
                    fontWeight: 700,
                    borderBottom: activeTab === 'exam' ? '2.5px solid var(--accent)' : 'none',
                    color: activeTab === 'exam' ? 'var(--accent)' : 'var(--text-muted)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px'
                  }}
                >
                  <span>Live Exams</span>
                  {examCount > 0 && (
                    <span style={{ fontSize: '11px', background: '#ef4444', color: '#fff', padding: '1px 6px', borderRadius: '10px', fontWeight: 800 }}>
                      {examCount}
                    </span>
                  )}
                </button>

                <button 
                  className={`tab-btn ${activeTab === 'sync' ? 'active' : ''}`}
                  onClick={() => setActiveTab('sync')}
                  style={{
                    padding: '8px 16px',
                    border: 'none',
                    cursor: 'pointer',
                    background: 'none',
                    fontWeight: 700,
                    borderBottom: activeTab === 'sync' ? '2.5px solid #a855f7' : 'none',
                    color: activeTab === 'sync' ? '#a855f7' : 'var(--text-muted)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px'
                  }}
                >
                  <span>Parent-Child Sync</span>
                  {syncCount > 0 ? (
                    <span style={{
                      fontSize: '11px',
                      background: 'linear-gradient(135deg, #a855f7, #6366f1)',
                      color: '#ffffff',
                      padding: '1px 7px',
                      borderRadius: '10px',
                      fontWeight: 800,
                      boxShadow: '0 0 8px rgba(168, 85, 247, 0.6)'
                    }}>
                      {syncCount} LIVE
                    </span>
                  ) : null}
                </button>

                <button 
                  className={`tab-btn ${activeTab === 'practice' ? 'active' : ''}`}
                  onClick={() => setActiveTab('practice')}
                  style={{
                    padding: '8px 16px',
                    border: 'none',
                    cursor: 'pointer',
                    background: 'none',
                    fontWeight: 700,
                    borderBottom: activeTab === 'practice' ? '2.5px solid var(--accent)' : 'none',
                    color: activeTab === 'practice' ? 'var(--accent)' : 'var(--text-muted)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px'
                  }}
                >
                  <span>Practice Activity</span>
                  {practiceCount > 0 && (
                    <span style={{ fontSize: '11px', background: '#3b82f6', color: '#fff', padding: '1px 6px', borderRadius: '10px', fontWeight: 800 }}>
                      {practiceCount}
                    </span>
                  )}
                </button>
              </>
            );
          })()}
        </div>

        {/* Info card */}
        <div id="live-info-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', padding: '15px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
          <div style={{ fontSize: '13px' }}>
            <strong>{list.length}</strong> students currently active
          </div>
          <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
            Sessions drop off automatically 5 minutes after disconnection.
          </span>
        </div>

        {/* Sessions table */}
        <div id="live-sessions-section" className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table className="reviews-table" style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', color: 'var(--text-muted)', fontSize: '12px' }}>
                  <th onClick={() => handleSort('studentName')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Student {sortField === 'studentName' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 16px' }}>{activeTab === 'exam' ? 'Exam' : activeTab === 'sync' ? 'Ritual / Session' : 'Topic'}</th>
                  <th onClick={() => handleSort('status')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Status {sortField === 'status' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 16px' }}>Progress</th>
                  <th onClick={() => handleSort('violations')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Violations {sortField === 'violations' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th onClick={() => handleSort('lastActive')} style={{ padding: '12px 16px', cursor: 'pointer', userSelect: 'none' }}>
                    Updated {sortField === 'lastActive' ? (sortDir === 'asc' ? '▲' : '▼') : '⇅'}
                  </th>
                  <th style={{ padding: '12px 16px', textAlign: 'right' }}>Camera</th>
                </tr>
              </thead>
              <tbody>
                {list.length === 0 ? (
                  <tr>
                    <td colSpan={7} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                      📭 No active {activeTab === 'exam' ? 'exam' : activeTab === 'sync' ? 'Parent-Child Sync' : 'practice'} sessions right now.
                    </td>
                  </tr>
                ) : (
                  list.map(s => {
                    const stale = isStale(s.lastActive);
                    const progressPct = s.totalQuestions ? Math.round(((s.answeredCount || 0) / s.totalQuestions) * 100) : 0;

                    return (
                      <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)', background: stale ? 'rgba(184,134,11,0.04)' : 'transparent' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                          👤 {s.studentName || 'Student'}{(s as any).autonomous ? ' ⭐' : ''}
                          {s.micAvailable === false && (
                            <span style={{ marginLeft: '6px', color: '#d97706', background: 'rgba(217, 119, 6, 0.1)', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Offline / Bypassed">
                              🎙️ Offline
                            </span>
                          )}
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          {s.examName || s.examId} <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({s.examType})</span>
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: stale ? '#fbe8c6' : '#dbf3e1', color: stale ? '#b8860b' : '#1aa54e', fontWeight: 700 }}>
                            {stale ? '⚠️ Stale' : '🟢 In Progress'}
                          </span>
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          {s.totalQuestions ? (
                            <div>
                              <div style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '3px' }}>
                                Q{(s.currentQuestionIndex || 0) + 1}/{s.totalQuestions} ({s.answeredCount || 0} ans)
                              </div>
                              <div style={{ height: '5px', width: '100px', background: 'var(--bg-soft)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div style={{ height: '100%', background: 'var(--accent)', width: `${progressPct}%` }}></div>
                              </div>
                            </div>
                          ) : (
                            <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>n/a</span>
                          )}
                        </td>
                        <td style={{ padding: '12px 16px' }}>{renderViolationsBadge(s.violations)}</td>
                        <td style={{ padding: '12px 16px', color: 'var(--text-muted)', fontSize: '11px' }}>{timeAgo(s.lastActive)}</td>
                        <td style={{ padding: '12px 16px', textAlign: 'right' }}>
                          <button 
                            className="btn btn-secondary btn-sm" 
                            disabled={!s.cameraAvailable}
                            style={{ fontSize: '11px', padding: '4px 10px' }}
                            onClick={() => handleOpenVideoFeed(s.examId, s.studentCode, s.studentName || s.studentCode)}
                          >
                            📷 {s.cameraAvailable ? 'View Feed' : 'No Camera'}
                          </button>
                        </td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </main>

      {/* Video stream Modal Overlay */}
      {videoModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '90%', padding: '24px', border: '1px solid var(--border-light)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0 }}>📷 Live Feed: {videoModal.studentName}</h3>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={handleCloseVideoModal}>✕</button>
            </div>

            <div style={{ width: '100%', background: '#000', borderRadius: 'var(--radius-sm)', overflow: 'hidden', position: 'relative', aspectRatio: '4/3', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <video 
                ref={videoRef}
                autoPlay 
                playsInline 
                muted
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
              <div style={{ position: 'absolute', bottom: '10px', left: '10px', background: 'rgba(0,0,0,0.6)', padding: '4px 10px', borderRadius: '4px', fontSize: '10px', color: 'white', fontWeight: 600 }}>
                {videoModal.status}
              </div>
            </div>

            {/* Audio controllers: Separate Listen vs Talk */}
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px', marginTop: '16px' }}>
              <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', justifyContent: 'center' }}>
                {/* 1. Listen Mode (Speaker) */}
                <button 
                  className={`btn ${isSpeakerMuted ? 'btn-secondary' : 'btn-primary'} btn-sm`} 
                  disabled={!hasAudioTrack}
                  onClick={handleToggleSpeaker}
                  style={{ padding: '6px 14px', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '6px' }}
                >
                  {isSpeakerMuted ? '🔇 Listen (Unmute Student)' : '🔊 Listening to Student'}
                </button>

                {/* 2. Talk Mode (Microphone) */}
                <button 
                  className={`btn ${isTalking ? 'btn-danger' : 'btn-secondary'} btn-sm`} 
                  disabled={!hasAdminMic}
                  onClick={handleToggleTalk}
                  style={{ 
                    padding: '6px 14px', 
                    fontSize: '11px', 
                    display: 'flex', 
                    alignItems: 'center', 
                    gap: '6px',
                    background: isTalking ? '#dc2626' : undefined,
                    color: isTalking ? '#ffffff' : undefined,
                    borderColor: isTalking ? '#b91c1c' : undefined
                  }}
                >
                  {isTalking ? '🛑 Stop Talking' : '🎙️ Talk to Student'}
                </button>
              </div>

              {/* Status explanation pill */}
              <div style={{ fontSize: '11px', textAlign: 'center', display: 'flex', alignItems: 'center', gap: '6px' }}>
                {isTalking ? (
                  <span style={{ color: '#dc2626', fontWeight: 700 }}>
                    🔴 Your mic is LIVE — speaking to student
                  </span>
                ) : !isSpeakerMuted ? (
                  <span style={{ color: '#16a34a', fontWeight: 600 }}>
                    🟢 Listening to student audio (Your mic is muted)
                  </span>
                ) : (
                  <span style={{ color: 'var(--text-muted)' }}>
                    {hasAudioTrack ? '🔇 Audio muted for privacy' : 'No audio track found in stream'}
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
      <ExportPdfModal
        isOpen={pdfSelectorOpen}
        onClose={() => setPdfSelectorOpen(false)}
        title={`Live Proctor Monitor Audit Logs — ${activeTab === 'exam' ? 'Exams' : 'Practice'}`}
        filename={`Live_Proctoring_${activeTab}_Logs.pdf`}
        sections={[
          { id: 'info', name: 'Active Overview Stats', elementId: 'live-info-section' },
          { id: 'sessions', name: 'Live Proctoring Sessions Table', elementId: 'live-sessions-section' }
        ]}
      />
    </div>
  );
}
