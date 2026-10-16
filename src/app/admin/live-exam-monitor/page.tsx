'use client';

import React, { useEffect, useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';

import { collection, query, where, onSnapshot, doc, updateDoc, arrayUnion } from 'firebase/firestore';
import { ref, push, set, onValue, off, remove, serverTimestamp } from 'firebase/database';
import { db } from '@/lib/firebase/firestore';
import { rtdb } from '@/lib/firebase/rtdb';

export interface ManualCapture {
  id: string;
  type: 'photo' | 'audio' | 'video' | 'both';
  timestamp: number | string;
  dataUrl: string;
  mimeType: string;
  durationSeconds?: number;
  recordedBy?: string;
}

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
  proctoringSnapshots?: Array<{
    id?: string;
    timestamp: number | string;
    reason: string;
    imageData?: string;
    imageBase64?: string;
    type?: string;
  }>;
  manualCaptures?: ManualCapture[];
  proctoringSnapshotsExpiresAt?: string;
  status: string;
  cameraAvailable: boolean;
  micAvailable?: boolean;
  isLate?: boolean;
  lastActive: any;
}

const getSnapshotImage = (snap: any): string => snap?.imageBase64 || snap?.imageData || '';

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
  const { firebaseUser } = useAuth();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'exam' | 'practice'>('exam');
  const [sessions, setSessions] = useState<{ [key: string]: Session }>({});

  // Sorting and PDF export states
  const [sortField, setSortField] = useState<'studentName' | 'status' | 'violations' | 'lastActive'>('lastActive');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');

  // Heartbeat staleness ticker
  const [tickerTime, setTickerTime] = useState(Date.now());

  // Proctoring & Evidence Modal State (includes auto-snapshots & manual captures)
  const [snapshotsModal, setSnapshotsModal] = useState<{
    show: boolean;
    studentName: string;
    examName: string;
    snapshots: Array<{ timestamp: number | string; reason: string; imageData?: string; imageBase64?: string; type?: string }>;
    manualCaptures: ManualCapture[];
    selectedMedia: { url: string; type: 'photo' | 'audio' | 'video' | 'both'; title?: string } | null;
    activeFilter: 'all' | 'photos' | 'videos' | 'audios';
  }>({
    show: false,
    studentName: '',
    examName: '',
    snapshots: [],
    manualCaptures: [],
    selectedMedia: null,
    activeFilter: 'all'
  });

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
  const remoteStreamRef = useRef<MediaStream | null>(null);

  // Manual Capture / Recording States & Refs
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const recordedChunksRef = useRef<Blob[]>([]);
  const recordingTimerRef = useRef<any>(null);
  const recordingSecondsRef = useRef<number>(0);
  const [isRecording, setIsRecording] = useState(false);
  const [recordingType, setRecordingType] = useState<'both' | 'video' | 'audio' | null>(null);
  const [recordingSeconds, setRecordingSeconds] = useState(0);
  const [captureFeedback, setCaptureFeedback] = useState<string | null>(null);
  const [isSavingCapture, setIsSavingCapture] = useState(false);

  // Periodic ticker to recalculate time-ago labels (pauses when tab is hidden)
  useEffect(() => {
    const timer = setInterval(() => {
      if (typeof document !== 'undefined' && document.hidden) return;
      setTickerTime(Date.now());
    }, 10000);
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
  const getFilteredList = (type: 'exam' | 'practice') => {
    const list = Object.values(sessions)
      .filter(s => {
        if (type === 'practice') return s.examType === 'practice' && !isAbandoned(s.lastActive);
        return s.examType !== 'practice' && !isAbandoned(s.lastActive);
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

  // Open snapshots & evidence modal
  const handleOpenSnapshotsModal = (session: Session) => {
    const snaps = (session.proctoringSnapshots || []).map(s => ({
      ...s,
      type: s.type || 'photo'
    }));
    const manuals = session.manualCaptures || [];
    
    // Select first available item
    let initialMedia: { url: string; type: 'photo' | 'audio' | 'video' | 'both'; title?: string } | null = null;
    if (manuals.length > 0) {
      initialMedia = { url: manuals[0].dataUrl, type: manuals[0].type, title: `Manual ${manuals[0].type}` };
    } else if (snaps.length > 0) {
      initialMedia = { url: getSnapshotImage(snaps[0]), type: 'photo', title: snaps[0].reason || 'Auto-snapshot' };
    }

    setSnapshotsModal({
      show: true,
      studentName: session.studentName || session.studentCode,
      examName: session.examName || session.examId,
      snapshots: snaps,
      manualCaptures: manuals,
      selectedMedia: initialMedia,
      activeFilter: 'all'
    });
  };

  const handleCloseSnapshotsModal = () => {
    setSnapshotsModal(prev => ({ ...prev, show: false, selectedMedia: null }));
  };

  // Helper to persist manual captures in Firestore session doc
  const saveManualCapture = async (capture: ManualCapture) => {
    const sId = getSessionDocId(videoModal.examId, videoModal.studentCode);
    try {
      const docRef = doc(db, 'liveExamSessions', sId);
      await updateDoc(docRef, {
        manualCaptures: arrayUnion(capture)
      });
      // Also update local state for instantaneous responsiveness
      setSessions(prev => {
        const current = prev[sId];
        if (!current) return prev;
        const updatedList = [...(current.manualCaptures || []), capture];
        return {
          ...prev,
          [sId]: { ...current, manualCaptures: updatedList }
        };
      });
    } catch (err: any) {
      console.error('[viewer] Failed to save manual capture to Firestore:', err);
      throw err;
    }
  };

  // 1. Instant Photo Snapshot Capture
  const handleCaptureSnapshot = async () => {
    if (!videoRef.current) return;
    try {
      setIsSavingCapture(true);
      const video = videoRef.current;
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth || 640;
      canvas.height = video.videoHeight || 480;
      const ctx = canvas.getContext('2d');
      if (!ctx) throw new Error('Canvas 2D context unavailable');
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
      const dataUrl = canvas.toDataURL('image/jpeg', 0.82);

      const captureItem: ManualCapture = {
        id: `manual_pic_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
        type: 'photo',
        timestamp: Date.now(),
        dataUrl,
        mimeType: 'image/jpeg',
        recordedBy: firebaseUser?.email || 'Teacher'
      };

      await saveManualCapture(captureItem);
      setCaptureFeedback('📸 Snapshot saved to evidence!');
      setTimeout(() => setCaptureFeedback(null), 3500);
    } catch (err: any) {
      console.error('[viewer] Error capturing snapshot:', err);
      setCaptureFeedback(`⚠️ Snapshot failed: ${err.message}`);
      setTimeout(() => setCaptureFeedback(null), 4000);
    } finally {
      setIsSavingCapture(false);
    }
  };

  // 2. Start Recording (Both A/V, Video Only, or Audio Only)
  const handleStartRecording = (type: 'both' | 'video' | 'audio') => {
    const stream = remoteStreamRef.current;
    if (!stream) {
      setCaptureFeedback('⚠️ No remote stream active yet.');
      setTimeout(() => setCaptureFeedback(null), 3000);
      return;
    }

    try {
      let recordingStream: MediaStream;
      const videoTracks = stream.getVideoTracks();
      const audioTracks = stream.getAudioTracks();

      if (type === 'audio') {
        if (audioTracks.length === 0) {
          setCaptureFeedback('⚠️ Student microphone is offline or no audio track present.');
          setTimeout(() => setCaptureFeedback(null), 3500);
          return;
        }
        recordingStream = new MediaStream(audioTracks);
      } else if (type === 'video') {
        if (videoTracks.length === 0) {
          setCaptureFeedback('⚠️ Student camera is offline or no video track present.');
          setTimeout(() => setCaptureFeedback(null), 3500);
          return;
        }
        recordingStream = new MediaStream(videoTracks);
      } else {
        // Both A/V
        const tracks = [...videoTracks, ...audioTracks];
        if (tracks.length === 0) {
          setCaptureFeedback('⚠️ No audio or video tracks available in stream.');
          setTimeout(() => setCaptureFeedback(null), 3500);
          return;
        }
        recordingStream = new MediaStream(tracks);
      }

      // Pick supported mime type
      let mimeType = '';
      if (type === 'audio') {
        const audioTypes = ['audio/webm;codecs=opus', 'audio/webm', 'audio/ogg;codecs=opus', 'audio/mp4'];
        mimeType = audioTypes.find(t => (window as any).MediaRecorder?.isTypeSupported?.(t)) || '';
      } else {
        const videoTypes = ['video/webm;codecs=vp8,opus', 'video/webm', 'video/mp4;codecs=avc1', 'video/mp4'];
        mimeType = videoTypes.find(t => (window as any).MediaRecorder?.isTypeSupported?.(t)) || '';
      }

      const options: MediaRecorderOptions = mimeType ? { mimeType } : {};
      const recorder = new MediaRecorder(recordingStream, options);
      mediaRecorderRef.current = recorder;
      recordedChunksRef.current = [];
      recordingSecondsRef.current = 0;
      setRecordingSeconds(0);

      recorder.ondataavailable = (event) => {
        if (event.data && event.data.size > 0) {
          recordedChunksRef.current.push(event.data);
        }
      };

      recorder.onstop = async () => {
        if (recordingTimerRef.current) {
          clearInterval(recordingTimerRef.current);
          recordingTimerRef.current = null;
        }
        setIsRecording(false);
        const durationSec = recordingSecondsRef.current;
        const activeType = recordingType || type;
        setRecordingType(null);

        const chunks = recordedChunksRef.current;
        if (chunks.length === 0) {
          setCaptureFeedback('⚠️ Recording had no data frames.');
          setTimeout(() => setCaptureFeedback(null), 3000);
          return;
        }

        setIsSavingCapture(true);
        setCaptureFeedback(`💾 Saving ${activeType} capture (${durationSec}s)...`);

        try {
          const finalMime = recorder.mimeType || (activeType === 'audio' ? 'audio/webm' : 'video/webm');
          const blob = new Blob(chunks, { type: finalMime });

          // Convert blob to DataURL for direct persistence and instant preview
          const reader = new FileReader();
          reader.onloadend = async () => {
            const dataUrl = reader.result as string;
            const captureItem: ManualCapture = {
              id: `manual_${activeType}_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
              type: activeType,
              timestamp: Date.now(),
              dataUrl,
              mimeType: finalMime,
              durationSeconds: durationSec,
              recordedBy: firebaseUser?.email || 'Teacher'
            };

            await saveManualCapture(captureItem);
            setCaptureFeedback(`✅ ${activeType.toUpperCase()} clip (${durationSec}s) saved to evidence!`);
            setTimeout(() => setCaptureFeedback(null), 3500);
            setIsSavingCapture(false);
          };
          reader.readAsDataURL(blob);
        } catch (err: any) {
          console.error('[viewer] Error finalizing recording:', err);
          setCaptureFeedback(`⚠️ Save failed: ${err.message}`);
          setIsSavingCapture(false);
          setTimeout(() => setCaptureFeedback(null), 4000);
        }
      };

      recorder.start(1000); // Collect slice every second
      setIsRecording(true);
      setRecordingType(type);

      recordingTimerRef.current = setInterval(() => {
        recordingSecondsRef.current += 1;
        setRecordingSeconds(recordingSecondsRef.current);

        // Auto-stop at 60s max to prevent enormous memory usage
        if (recordingSecondsRef.current >= 60) {
          handleStopRecording();
        }
      }, 1000);

    } catch (err: any) {
      console.error('[viewer] Error starting recording:', err);
      setCaptureFeedback(`⚠️ Could not start recording: ${err.message}`);
      setTimeout(() => setCaptureFeedback(null), 4000);
    }
  };

  // 3. Stop Recording
  const handleStopRecording = () => {
    if (recordingTimerRef.current) {
      clearInterval(recordingTimerRef.current);
      recordingTimerRef.current = null;
    }
    if (mediaRecorderRef.current && mediaRecorderRef.current.state !== 'inactive') {
      try {
        mediaRecorderRef.current.stop();
      } catch (e) {
        console.warn('[viewer] Error stopping recorder:', e);
      }
    }
  };

  // Close peer connection and modal
  const handleCloseVideoModal = () => {
    // If currently recording, stop it first
    if (isRecording) {
      handleStopRecording();
    }
    setVideoModal(prev => ({ ...prev, show: false }));
    if (activeCallRef.current) {
      activeCallRef.current.close();
      activeCallRef.current = null;
    }
    if (localAudioStreamRef.current) {
      localAudioStreamRef.current.getTracks().forEach(t => t.stop());
      localAudioStreamRef.current = null;
    }
    remoteStreamRef.current = null;
    setIsSpeakerMuted(true);
    setIsTalking(false);
    setHasAdminMic(false);
    setCaptureFeedback(null);
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
      remoteStreamRef.current = remoteStream;

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
        <span className={`viol-pill ${totalViol >= 5 ? 'high' : ''}`} style={{ background: totalViol >= 5 ? 'rgba(239, 68, 68, 0.15)' : 'var(--bg-soft)', color: totalViol >= 5 ? 'var(--danger)' : 'var(--text)', padding: '2px 8px', borderRadius: '10px', fontSize: '11px', whiteSpace: 'nowrap' }}>
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
    <div style={{ background: 'var(--bg)', flex: 1, display: 'flex', flexDirection: 'column' }}>
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '1000px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {/* Tabs Selection with Dynamic Active Badges */}
        <div className="tabs-container" style={{ display: 'flex', gap: '8px', borderBottom: '1.5px solid var(--border-light)', paddingBottom: '8px' }}>
          {(() => {
            const examCount = getFilteredList('exam').length;
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
                    <span style={{ fontSize: '11px', background: 'var(--danger)', color: 'var(--text-white)', padding: '1px 6px', borderRadius: '10px', fontWeight: 800 }}>
                      {examCount}
                    </span>
                  )}
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
                    <span style={{ fontSize: '11px', background: 'var(--accent)', color: 'var(--text-white)', padding: '1px 6px', borderRadius: '10px', fontWeight: 800 }}>
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
                  <th style={{ padding: '12px 16px' }}>{activeTab === 'exam' ? 'Exam' : 'Topic'}</th>
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
                      📭 No active {activeTab === 'exam' ? 'exam' : 'practice'} sessions right now.
                    </td>
                  </tr>
                ) : (
                  list.map(s => {
                    const stale = isStale(s.lastActive);
                    const progressPct = s.totalQuestions ? Math.round(((s.answeredCount || 0) / s.totalQuestions) * 100) : 0;

                    return (
                      <tr key={s.id} style={{ borderBottom: '1px solid var(--border-light)', background: stale ? 'rgba(245, 158, 11, 0.04)' : 'transparent' }}>
                        <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                          {s.isLate && (
                            <span style={{ marginRight: '6px', color: '#ef4444', background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', padding: '1px 5px', borderRadius: '4px', fontSize: '10px', fontWeight: 800 }}>
                              ⏰ LATE
                            </span>
                          )}
                          👤 {s.studentName || 'Student'}{(s as any).autonomous ? ' ⭐' : ''}
                          {s.micAvailable === false && (
                            <span style={{ marginLeft: '6px', color: 'var(--warning)', background: 'rgba(245, 158, 11, 0.1)', padding: '1px 6px', borderRadius: '4px', fontSize: '10px', fontWeight: 700 }} title="Microphone Offline / Bypassed">
                              🎙️ Offline
                            </span>
                          )}
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          {s.examName || s.examId} <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>({s.examType})</span>
                        </td>
                        <td style={{ padding: '12px 16px' }}>
                          <span style={{ fontSize: '10px', padding: '2px 8px', borderRadius: '10px', background: stale ? 'rgba(245, 158, 11, 0.15)' : 'rgba(16, 185, 129, 0.15)', color: stale ? 'var(--warning)' : 'var(--success)', fontWeight: 700 }}>
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
                          <div style={{ display: 'inline-flex', gap: '6px', alignItems: 'center', justifyContent: 'flex-end' }}>
                            {((s.proctoringSnapshots && s.proctoringSnapshots.length > 0) || (s.manualCaptures && s.manualCaptures.length > 0)) && (
                              <button 
                                className="btn btn-secondary btn-sm" 
                                style={{ fontSize: '11px', padding: '4px 8px', background: 'rgba(59, 130, 246, 0.12)', color: 'var(--accent)', borderColor: 'rgba(59, 130, 246, 0.3)', fontWeight: 700 }}
                                onClick={() => handleOpenSnapshotsModal(s)}
                                title="View auto-captured snapshots and manual evidence recordings"
                              >
                                📸 Evidence ({((s.proctoringSnapshots?.length || 0) + (s.manualCaptures?.length || 0))})
                                {s.manualCaptures && s.manualCaptures.length > 0 && (
                                  <span style={{ marginLeft: '4px', fontSize: '9.5px', background: 'var(--accent)', color: 'white', padding: '0 4px', borderRadius: '4px' }}>
                                    +{s.manualCaptures.length} rec
                                  </span>
                                )}
                              </button>
                            )}
                            <button 
                              className="btn btn-secondary btn-sm" 
                              disabled={!s.cameraAvailable}
                              style={{ fontSize: '11px', padding: '4px 10px' }}
                              onClick={() => handleOpenVideoFeed(s.examId, s.studentCode, s.studentName || s.studentCode)}
                            >
                              📷 {s.cameraAvailable ? 'Live Feed' : 'No Camera'}
                            </button>
                          </div>
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

      {/* Snapshots & Evidence Modal Overlay (Admin Confidential) */}
      {snapshotsModal.show && (() => {
        const autoSnaps = snapshotsModal.snapshots.map((s, idx) => ({
          id: s.reason || `auto_${idx}`,
          type: 'photo' as const,
          timestamp: s.timestamp,
          url: getSnapshotImage(s),
          title: `Auto Viol: ${s.reason || 'Movement'}`,
          isManual: false
        }));

        const manualItems = (snapshotsModal.manualCaptures || []).map((m, idx) => ({
          id: m.id || `manual_${idx}`,
          type: m.type,
          timestamp: m.timestamp,
          url: m.dataUrl,
          title: `Manual ${m.type.toUpperCase()}${m.durationSeconds ? ` (${m.durationSeconds}s)` : ''}`,
          isManual: true,
          mimeType: m.mimeType,
          durationSeconds: m.durationSeconds
        }));

        const allItems = [...manualItems, ...autoSnaps];

        const filteredItems = allItems.filter(item => {
          if (snapshotsModal.activeFilter === 'photos') return item.type === 'photo';
          if (snapshotsModal.activeFilter === 'videos') return item.type === 'video' || item.type === 'both';
          if (snapshotsModal.activeFilter === 'audios') return item.type === 'audio';
          return true;
        });

        const selected = snapshotsModal.selectedMedia;

        return (
          <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.88)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '16px' }}>
            <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '720px', width: '100%', maxHeight: '92vh', display: 'flex', flexDirection: 'column', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', padding: '14px 20px', background: 'var(--bg-soft)' }}>
                <div>
                  <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                    📸 Proctoring & Recorded Evidence: {snapshotsModal.studentName}
                  </h3>
                  <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                    {snapshotsModal.examName} • {allItems.length} total piece(s) of evidence ({snapshotsModal.manualCaptures.length} manual recordings, {snapshotsModal.snapshots.length} auto snapshots)
                  </span>
                </div>
                <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '12px' }} onClick={handleCloseSnapshotsModal}>✕</button>
              </div>

              <div style={{ padding: '16px 20px', overflowY: 'auto', flex: 1, display: 'flex', flexDirection: 'column', gap: '14px' }}>
                {/* Privacy & Retention Notice Banner */}
                <div style={{ background: 'rgba(59, 130, 246, 0.08)', border: '1px solid rgba(59, 130, 246, 0.25)', borderRadius: '6px', padding: '8px 12px', fontSize: '11px', color: 'var(--accent)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span>🔒</span>
                  <span>
                    <strong>Strictly Confidential (Admin Only):</strong> Automated snapshots and manual teacher recordings for academic integrity audits. Automatically purged 18 hours post-exam.
                  </span>
                </div>

                {/* Filter Tabs */}
                <div style={{ display: 'flex', gap: '6px', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
                  {(['all', 'photos', 'videos', 'audios'] as const).map(tab => (
                    <button
                      key={tab}
                      onClick={() => setSnapshotsModal(prev => ({ ...prev, activeFilter: tab }))}
                      style={{
                        padding: '4px 12px',
                        fontSize: '11px',
                        fontWeight: snapshotsModal.activeFilter === tab ? 700 : 500,
                        background: snapshotsModal.activeFilter === tab ? 'var(--accent)' : 'transparent',
                        color: snapshotsModal.activeFilter === tab ? '#fff' : 'var(--text-muted)',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        textTransform: 'capitalize'
                      }}
                    >
                      {tab} ({tab === 'all' ? allItems.length : tab === 'photos' ? allItems.filter(i => i.type === 'photo').length : tab === 'videos' ? allItems.filter(i => i.type === 'video' || i.type === 'both').length : allItems.filter(i => i.type === 'audio').length})
                    </button>
                  ))}
                </div>

                {/* Main Media Player / Preview */}
                {selected ? (
                  <div style={{ width: '100%', background: '#0a0a0a', borderRadius: '8px', overflow: 'hidden', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '260px', maxHeight: '360px', position: 'relative', border: '1px solid var(--border-light)' }}>
                    {selected.type === 'photo' && (
                      <img 
                        src={selected.url} 
                        alt="Evidence Preview" 
                        style={{ maxHeight: '320px', maxWidth: '100%', objectFit: 'contain' }}
                      />
                    )}

                    {(selected.type === 'video' || selected.type === 'both') && (
                      <video 
                        key={selected.url}
                        controls 
                        autoPlay 
                        playsInline
                        src={selected.url}
                        style={{ maxHeight: '320px', maxWidth: '100%', objectFit: 'contain' }}
                      />
                    )}

                    {selected.type === 'audio' && (
                      <div style={{ padding: '40px 20px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '14px', width: '100%' }}>
                        <div style={{ fontSize: '36px' }}>🎙️</div>
                        <div style={{ color: 'var(--text)', fontSize: '13px', fontWeight: 700 }}>
                          {selected.title || 'Audio Recording'}
                        </div>
                        <audio 
                          key={selected.url}
                          controls 
                          autoPlay 
                          src={selected.url}
                          style={{ width: '80%', maxWidth: '380px' }}
                        />
                      </div>
                    )}

                    {/* Download & Info Bar */}
                    <div style={{ position: 'absolute', bottom: '8px', right: '8px', display: 'flex', gap: '8px' }}>
                      <a
                        href={selected.url}
                        download={`evidence_${snapshotsModal.studentName.replace(/\s+/g, '_')}_${Date.now()}.${selected.type === 'photo' ? 'jpg' : selected.type === 'audio' ? 'webm' : 'webm'}`}
                        className="btn btn-secondary btn-sm"
                        style={{ fontSize: '10px', padding: '3px 8px', background: 'rgba(0,0,0,0.7)', color: '#fff', border: '1px solid rgba(255,255,255,0.2)' }}
                      >
                        ⬇️ Download
                      </a>
                    </div>
                  </div>
                ) : (
                  <div style={{ padding: '30px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '12px', background: 'var(--bg-soft)', borderRadius: '6px' }}>
                    Select an item from the gallery below to preview.
                  </div>
                )}

                {/* Thumbnails Strip */}
                <div>
                  <div style={{ fontSize: '11.5px', fontWeight: 700, marginBottom: '8px', color: 'var(--text-muted)' }}>
                    Evidence Gallery ({filteredItems.length} items):
                  </div>
                  {filteredItems.length === 0 ? (
                    <div style={{ fontSize: '11.5px', color: 'var(--text-muted)', textAlign: 'center', padding: '20px' }}>
                      No items matching this filter.
                    </div>
                  ) : (
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(115px, 1fr))', gap: '10px' }}>
                      {filteredItems.map((item, idx) => {
                        const isSelected = selected?.url === item.url;
                        const dateStr = item.timestamp ? new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }) : `#${idx + 1}`;
                        const badgeColor = item.isManual ? 'var(--accent)' : 'var(--warning)';

                        return (
                          <div 
                            key={idx} 
                            onClick={() => setSnapshotsModal(prev => ({ ...prev, selectedMedia: { url: item.url, type: item.type, title: item.title } }))}
                            style={{
                              border: isSelected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                              borderRadius: '6px',
                              overflow: 'hidden',
                              cursor: 'pointer',
                              background: 'var(--bg-soft)',
                              transition: 'all 0.15s ease'
                            }}
                          >
                            <div style={{ aspectRatio: '4/3', background: '#000', overflow: 'hidden', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
                              {item.type === 'photo' ? (
                                <img src={item.url} alt={item.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                              ) : item.type === 'audio' ? (
                                <div style={{ fontSize: '28px', color: '#38bdf8' }}>🎙️</div>
                              ) : (
                                <div style={{ fontSize: '28px', color: '#a855f7' }}>🎬</div>
                              )}
                              <span style={{ position: 'absolute', top: '3px', right: '3px', background: item.isManual ? 'var(--accent)' : 'rgba(0,0,0,0.7)', color: '#fff', fontSize: '8.5px', fontWeight: 800, padding: '1px 4px', borderRadius: '3px' }}>
                                {item.isManual ? 'MANUAL' : 'AUTO'}
                              </span>
                            </div>
                            <div style={{ padding: '4px 6px', fontSize: '9.5px', background: 'var(--surface)' }}>
                              <div style={{ fontWeight: 700, color: 'var(--text)' }}>⏱️ {dateStr}</div>
                              <div style={{ color: badgeColor, fontWeight: 600, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }} title={item.title}>
                                {item.title}
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              </div>

              <div style={{ borderTop: '1px solid var(--border-light)', padding: '10px 20px', background: 'var(--bg-soft)', display: 'flex', justifyContent: 'flex-end' }}>
                <button className="btn btn-secondary btn-sm" onClick={handleCloseSnapshotsModal}>
                  Close
                </button>
              </div>
            </div>
          </div>
        );
      })()}

      {/* Video stream Modal Overlay */}
      {videoModal.show && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.85)', zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', maxWidth: '480px', width: '90%', padding: '24px', border: '1px solid var(--border-light)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px', marginBottom: '15px' }}>
              <h3 style={{ fontSize: '14px', fontWeight: 800, margin: 0 }}>📷 Live Feed: {videoModal.studentName}</h3>
              <button className="btn btn-secondary" style={{ padding: '2px 8px', fontSize: '10px' }} onClick={handleCloseVideoModal}>✕</button>
            </div>

            <div style={{ width: '100%', background: 'var(--text-black)', borderRadius: 'var(--radius-sm)', overflow: 'hidden', position: 'relative', aspectRatio: '4/3', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
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

            {/* Evidence Manual Capture Toolbar */}
            <div style={{ marginTop: '14px', padding: '12px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '11px', fontWeight: 800, color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '5px' }}>
                  🎥 Capture Evidence (Admin Manual)
                </span>
                {videoModal.examId && (
                  <button
                    className="btn btn-secondary btn-sm"
                    style={{ fontSize: '10px', padding: '2px 8px' }}
                    onClick={() => {
                      const sId = getSessionDocId(videoModal.examId, videoModal.studentCode);
                      const current = sessions[sId];
                      if (current) handleOpenSnapshotsModal(current);
                    }}
                    title="Open all captured evidence for this student"
                  >
                    📂 View Saved ({((sessions[getSessionDocId(videoModal.examId, videoModal.studentCode)]?.manualCaptures?.length || 0) + (sessions[getSessionDocId(videoModal.examId, videoModal.studentCode)]?.proctoringSnapshots?.length || 0))})
                  </button>
                )}
              </div>

              {/* Action buttons or Live Recording status */}
              {isRecording ? (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'rgba(239, 68, 68, 0.12)', border: '1px solid rgba(239, 68, 68, 0.35)', borderRadius: '6px', padding: '8px 12px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ display: 'inline-block', width: '10px', height: '10px', borderRadius: '50%', background: 'red', animation: 'pulse 1s infinite' }} />
                    <span style={{ fontSize: '12px', fontWeight: 800, color: '#ef4444' }}>
                      RECORDING {recordingType?.toUpperCase()}: {String(Math.floor(recordingSeconds / 60)).padStart(2, '0')}:{String(recordingSeconds % 60).padStart(2, '0')}
                    </span>
                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>(max 60s)</span>
                  </div>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={handleStopRecording}
                    style={{ padding: '5px 12px', fontSize: '11px', fontWeight: 700 }}
                  >
                    ⏹️ Stop & Save
                  </button>
                </div>
              ) : (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '6px' }}>
                  {/* Photo snapshot */}
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={handleCaptureSnapshot}
                    disabled={isSavingCapture}
                    title="Take an instant high-res photo snapshot from student camera"
                    style={{ fontSize: '10.5px', padding: '6px 4px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '3px' }}
                  >
                    <span style={{ fontSize: '14px' }}>📷</span>
                    <span>Photo</span>
                  </button>

                  {/* Both Audio + Video */}
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => handleStartRecording('both')}
                    disabled={isSavingCapture}
                    title="Record Audio + Video clip of student"
                    style={{ fontSize: '10.5px', padding: '6px 4px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '3px' }}
                  >
                    <span style={{ fontSize: '14px' }}>🎬</span>
                    <span>Both (A/V)</span>
                  </button>

                  {/* Video Only */}
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => handleStartRecording('video')}
                    disabled={isSavingCapture}
                    title="Record Video-only clip (no audio track)"
                    style={{ fontSize: '10.5px', padding: '6px 4px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '3px' }}
                  >
                    <span style={{ fontSize: '14px' }}>📹</span>
                    <span>Video Only</span>
                  </button>

                  {/* Audio Only */}
                  <button
                    className="btn btn-secondary btn-sm"
                    onClick={() => handleStartRecording('audio')}
                    disabled={isSavingCapture || !hasAudioTrack}
                    title={hasAudioTrack ? "Record Audio-only clip from student mic" : "Microphone offline"}
                    style={{ fontSize: '10.5px', padding: '6px 4px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '3px' }}
                  >
                    <span style={{ fontSize: '14px' }}>🎙️</span>
                    <span>Audio Only</span>
                  </button>
                </div>
              )}

              {/* Feedback toast banner */}
              {captureFeedback && (
                <div style={{ fontSize: '11px', textAlign: 'center', fontWeight: 700, padding: '4px 8px', borderRadius: '4px', background: 'rgba(59, 130, 246, 0.12)', color: 'var(--accent)' }}>
                  {captureFeedback}
                </div>
              )}
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
                    background: isTalking ? 'var(--danger)' : undefined,
                    color: isTalking ? 'var(--text-white)' : undefined,
                    borderColor: isTalking ? 'var(--danger)' : undefined
                  }}
                >
                  {isTalking ? '🛑 Stop Talking' : '🎙️ Talk to Student'}
                </button>
              </div>

              {/* Status explanation pill */}
              <div style={{ fontSize: '11px', textAlign: 'center', display: 'flex', alignItems: 'center', gap: '6px' }}>
                {isTalking ? (
                  <span style={{ color: 'var(--danger)', fontWeight: 700 }}>
                    🔴 Your mic is LIVE — speaking to student
                  </span>
                ) : !isSpeakerMuted ? (
                  <span style={{ color: 'var(--success)', fontWeight: 600 }}>
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
    </div>
  );
}
