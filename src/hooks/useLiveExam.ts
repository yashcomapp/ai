import { useEffect, useRef, useState } from 'react';
import { rtdb } from '@/lib/firebase/rtdb';
import { getLiveSessionRef, createLiveSession, updateLiveSession } from '@/lib/proctoring';
import { ref, onValue, set, push, off, remove } from 'firebase/database';

interface UseLiveExamProps {
  examId: string;
  examName: string;
  studentCode: string;
  studentName: string;
  examType: 'mcq' | 'subjective' | 'practice';
  totalQuestions: number | null;
  currentQuestionIndex: number | null;
  answeredCount: number | null;
  cameraVideoRef: React.RefObject<HTMLVideoElement | null>;
  autonomous?: boolean;
  started?: boolean;
  mock?: boolean;
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

export function useLiveExam({
  examId,
  examName,
  studentCode,
  studentName,
  examType,
  totalQuestions,
  currentQuestionIndex,
  answeredCount,
  cameraVideoRef,
  autonomous,
  started = true,
  mock = false
}: UseLiveExamProps) {
  const [tabViolations, setTabViolations] = useState(0);
  const [awayTimeTotal, setAwayTimeTotal] = useState(0);
  const lastActiveRef = useRef<number>(Date.now());
  const lastViolationTimeRef = useRef<number>(0);
  const startTimeRef = useRef<number>(0);

  const [proctoringViolations, setProctoringViolations] = useState({
    noFace: 0,
    multipleFaces: 0,
    lookingAway: 0,
    headMovement: 0
  });

  const [cameraStatus, setCameraStatus] = useState('');
  const [cameraStream, setCameraStream] = useState<MediaStream | null>(null);
  const [micBypassed, setMicBypassed] = useState(false);

  useEffect(() => {
    if (!started) return;
    if (!examId || !studentCode) return;

    if (!startTimeRef.current) {
      startTimeRef.current = Date.now();
    }

    const recordViolation = (type: string) => {
      const now = Date.now();
      if (now - startTimeRef.current < 5000) {
        // Ignore transient setup-phase blurs in the first 5 seconds
        return;
      }
      if (now - lastViolationTimeRef.current < 1500) {
        // Coalesce events within 1.5 seconds to avoid double-counting
        return;
      }
      lastViolationTimeRef.current = now;
      setTabViolations(prev => prev + 1);
      lastActiveRef.current = now;
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        recordViolation('tab-hidden');
      } else {
        const awayMs = Date.now() - lastActiveRef.current;
        setAwayTimeTotal(prev => prev + Math.round(awayMs / 1000));
      }
    };

    const handleBlur = () => {
      recordViolation('window-blur');
    };

    const handleFocus = () => {
      const awayMs = Date.now() - lastActiveRef.current;
      setAwayTimeTotal(prev => prev + Math.round(awayMs / 1000));
    };

    const handleFullscreenChange = () => {
      if (!document.fullscreenElement) {
        recordViolation('fullscreen-exit');
      }
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('blur', handleBlur);
    window.addEventListener('focus', handleFocus);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);

    if (!liveSessionActiveRef.current) {
      initLiveProctoringSession(activeStreamRef.current).catch(err => console.warn('Live proctoring init error:', err));
    }

    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('blur', handleBlur);
      window.removeEventListener('focus', handleFocus);
      document.removeEventListener('fullscreenchange', handleFullscreenChange);
      document.removeEventListener('webkitfullscreenchange', handleFullscreenChange);
    };
  }, [started, examId, studentCode]);

  const liveSessionDocRef = useRef<any>(null);
  const liveSessionActiveRef = useRef<boolean>(false);
  const rtcConnectionRef = useRef<RTCPeerConnection | null>(null);
  const candidatesUnsubscribeRef = useRef<(() => void) | null>(null);
  const activeStreamRef = useRef<MediaStream | null>(null);

  const sanitizeForRtdbPath = (s: string) => {
    return String(s).replace(/[.$#\[\]/]/g, '_');
  };

  const getSessionDocId = () => {
    return `${sanitizeForRtdbPath(examId || '')}_${sanitizeForRtdbPath(studentCode || '')}`;
  };

  const initLiveProctoringSession = async (stream?: MediaStream | null) => {
    if (mock) return;
    if (!studentCode || !examId) return;

    const sId = getSessionDocId();
    const docRef = getLiveSessionRef(sId);
    liveSessionDocRef.current = docRef;
    liveSessionActiveRef.current = true;

    const initialData = {
      id: sId,
      examId,
      examName,
      examType,
      studentCode,
      studentName,
      currentQuestionIndex,
      totalQuestions,
      answeredCount,
      autonomous: autonomous || false,
      status: 'in-progress',
      cameraAvailable: !!stream,
      micAvailable: stream ? stream.getAudioTracks().length > 0 && stream.getAudioTracks()[0].enabled : false,
      violations: {
        tabViolations: 0,
        noFaceCount: 0,
        multipleFacesCount: 0,
        lookingAwayCount: 0,
        headMovementCount: 0,
        awayTimeTotal: 0
      }
    };

    try {
      await createLiveSession(sId, initialData);
      
      const heartbeatInterval = setInterval(async () => {
        if (!liveSessionActiveRef.current) {
          clearInterval(heartbeatInterval);
          return;
        }
        try {
          await updateLiveSession(docRef, {});
        } catch (e) {
          console.warn('Heartbeat update failed:', e);
        }
      }, 10000);

      if (stream) {
        setupWebRTCSignaling(stream);
      }
    } catch (err: any) {
      console.error('Error starting live proctoring session:', err.message);
    }
  };

  const updateLiveProctoringSession = async (updates: any) => {
    if (mock) return;
    if (!liveSessionDocRef.current || !liveSessionActiveRef.current) return;
    try {
      await updateLiveSession(liveSessionDocRef.current, updates);
    } catch (err: any) {
      console.warn('Failed to update live session:', err.message);
    }
  };

  // Keep live metrics updated periodically when props change
  useEffect(() => {
    if (liveSessionActiveRef.current) {
      updateLiveProctoringSession({
        currentQuestionIndex,
        answeredCount,
        violations: {
          tabViolations,
          noFaceCount: proctoringViolations.noFace,
          multipleFacesCount: proctoringViolations.multipleFaces,
          lookingAwayCount: proctoringViolations.lookingAway,
          headMovementCount: proctoringViolations.headMovement,
          awayTimeTotal
        }
      });
    }
  }, [currentQuestionIndex, answeredCount, tabViolations, proctoringViolations, awayTimeTotal]);

  const setupWebRTCSignaling = async (stream: MediaStream) => {
    if (mock) return;
    if (!rtdb) return;
    const sId = getSessionDocId();
    const sigRef = ref(rtdb, `webrtcSignaling/${sId}`);

    // Listen for WebRTC offers from proctor dashboard
    onValue(sigRef, async (snapshot) => {
      const data = snapshot.val();
      if (!data) {
        cleanupWebRTC();
        return;
      }

      // Handle offer
      if (data.offer && !rtcConnectionRef.current) {
        setCameraStatus('Incoming WebRTC stream request...');
        const peerConnection = new RTCPeerConnection(RTC_CONFIG);
        rtcConnectionRef.current = peerConnection;

        // Listen for incoming track from admin (two-way audio support)
        const remoteStream = new MediaStream();
        peerConnection.ontrack = (event) => {
          console.log('[student] WebRTC track received from admin:', event.track.kind);
          if (event.track.kind === 'audio') {
            remoteStream.addTrack(event.track);
            const audio = new Audio();
            audio.srcObject = remoteStream;
            audio.play().catch(e => console.warn('[student] Error playing remote admin audio:', e));
          }
        };

        // Add tracks
        stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));

        // Candidates logic
        peerConnection.onicecandidate = (event) => {
          if (event.candidate) {
            const calleeRef = ref(rtdb, `webrtcSignaling/${sId}/calleeCandidates`);
            push(calleeRef, event.candidate.toJSON());
          }
        };

        // Set remote description
        await peerConnection.setRemoteDescription(new RTCSessionDescription(data.offer));
        const answer = await peerConnection.createAnswer();
        await peerConnection.setLocalDescription(answer);

        await set(ref(rtdb, `webrtcSignaling/${sId}/answer`), {
          type: answer.type,
          sdp: answer.sdp
        });

        // Add caller ICE candidates
        const callerCandidatesRef = ref(rtdb, `webrtcSignaling/${sId}/callerCandidates`);
        const unsub = onValue(callerCandidatesRef, (cSnap) => {
          cSnap.forEach((candidateDoc) => {
            const candidate = candidateDoc.val();
            if (candidate) {
              peerConnection.addIceCandidate(new RTCIceCandidate(candidate)).catch(() => {});
            }
          });
        });
        candidatesUnsubscribeRef.current = unsub;

        setCameraStatus('WebRTC Live Stream Connected');
      }

      // Handle call termination
      if (data.terminate) {
        cleanupWebRTC();
      }
    });
  };

  const cleanupWebRTC = () => {
    if (candidatesUnsubscribeRef.current) {
      try {
        candidatesUnsubscribeRef.current();
      } catch (e) {}
      candidatesUnsubscribeRef.current = null;
    }
    if (rtcConnectionRef.current) {
      rtcConnectionRef.current.close();
      rtcConnectionRef.current = null;
    }
    
    // Restore local hardware status instead of hardcoding 'WebRTC disconnected'
    if (activeStreamRef.current) {
      const hasAudio = activeStreamRef.current.getAudioTracks().some(t => t.enabled);
      if (hasAudio) {
        setCameraStatus('Webcam and Microphone active.');
      } else {
        setCameraStatus('⚠️ Camera active. Microphone bypassed.');
      }
    } else {
      setCameraStatus('Webcam Offline');
    }
  };

  const cleanupProctoring = () => {
    liveSessionActiveRef.current = false;
    cleanupWebRTC();
    if (mock) return;

    if (liveSessionDocRef.current) {
      updateLiveSession(liveSessionDocRef.current, {
        status: 'completed'
      }).catch(err => console.warn('Could not update live proctoring status:', err.message));
    }

    if (rtdb) {
      const sId = getSessionDocId();
      off(ref(rtdb, `webrtcSignaling/${sId}`));
      off(ref(rtdb, `webrtcSignaling/${sId}/callerCandidates`));
      remove(ref(rtdb, `webrtcSignaling/${sId}`)).catch(() => {});
    }
  };

  const startCameraStream = async () => {
    setCameraStatus('Accessing webcam and microphone...');
    
    // Stop any existing tracks first to ensure camera is released
    if (cameraStream) {
      try {
        cameraStream.getTracks().forEach(track => track.stop());
      } catch (e) {
        console.warn('Error stopping previous tracks:', e);
      }
    }

    let stream: MediaStream | null = null;
    let cameraWorks = false;
    let micWorks = false;
    let cameraErrorName = '';
    let micErrorName = '';

    // Test Video
    try {
      const vStream = await navigator.mediaDevices.getUserMedia({ video: true });
      cameraWorks = true;
      vStream.getTracks().forEach(t => t.stop());
    } catch (err: any) {
      cameraErrorName = err.name;
    }

    // Test Audio
    try {
      const aStream = await navigator.mediaDevices.getUserMedia({ audio: true });
      micWorks = true;
      aStream.getTracks().forEach(t => t.stop());
    } catch (err: any) {
      micErrorName = err.name;
    }

    if (!cameraWorks) {
      const isDenied = cameraErrorName === 'NotAllowedError' || cameraErrorName === 'PermissionDeniedError';
      setCameraStatus(isDenied ? '❌ Camera access was denied. You must allow camera access in browser settings to take the exam.' : `❌ Camera error: ${cameraErrorName}`);
      return { success: false, cameraDenied: true, micDenied: false };
    }

    if (!micWorks) {
      console.warn("Microphone access failed/denied, bypassing. Error:", micErrorName);
    }

    // Request optimal combined stream
    try {
      stream = await navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: "user",
          width: { ideal: 320 },
          height: { ideal: 240 },
          frameRate: { ideal: 10, max: 15 }
        },
        audio: micWorks
      });
    } catch (err: any) {
      // Fallback combined minimal stream
      try {
        stream = await navigator.mediaDevices.getUserMedia({
          video: true,
          audio: micWorks
        });
      } catch (err2: any) {
        // Fallback video only if audio still fails combined call
        try {
          stream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
          });
        } catch (err3: any) {}
      }
    }

    if (stream) {
      activeStreamRef.current = stream;
      setCameraStream(stream);
      if (cameraVideoRef.current) {
        cameraVideoRef.current.srcObject = stream;
      }
      if (!micWorks) {
        setCameraStatus('⚠️ Camera active. Microphone bypassed.');
        setMicBypassed(true);
      } else {
        setCameraStatus('Webcam and Microphone active.');
        setMicBypassed(false);
      }
      
      // Initialize/update proctoring session with active stream
      await initLiveProctoringSession(stream);
      return { success: true, cameraDenied: false, micDenied: false, stream, micBypassed: !micWorks };
    }

    // Ensure session is registered even if video failed
    await initLiveProctoringSession(null);
    return { success: false, cameraDenied: true, micDenied: true };
  };

  const stopCameraStream = () => {
    cleanupProctoring();
    activeStreamRef.current = null;
    if (cameraStream) {
      cameraStream.getTracks().forEach(track => track.stop());
      setCameraStream(null);
    }
  };

  return {
    tabViolations,
    setTabViolations,
    awayTimeTotal,
    setAwayTimeTotal,
    proctoringViolations,
    setProctoringViolations,
    cameraStatus,
    cameraStream,
    micBypassed,
    startCameraStream,
    stopCameraStream,
    cleanupProctoring
  };
}
