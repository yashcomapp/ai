import { useEffect, useRef, useState, useCallback } from 'react';
import { calculateHeadPose, checkLookingAway, checkExcessiveMovement, HeadPose, PROCTOR_THRESHOLDS } from '@/utils/headPose';

interface ProctoringConfig {
  videoRef: React.RefObject<HTMLVideoElement | null>;
  enabled?: boolean;
  
  // Lockdown behaviors
  lockdownShortcuts?: boolean;
  lockdownContextMenu?: boolean;
  lockdownWindowFocus?: boolean;
  lockdownFullscreen?: boolean;

  // Live Exam Actions
  startCameraStream: () => Promise<any>;
  stopCameraStream: () => void;
  cleanupLiveExam: () => void;

  // Custom Callbacks
  onViolation?: (type: 'gaze' | 'no_face' | 'movement' | 'multiple_faces' | 'tab_switch', details: string, screenshotDataUrl?: string | null) => void;
  onStatusChange?: (status: string, statusClass: 'success' | 'warning' | 'error') => void;
  isNumerical?: boolean;
}

export function useProctoring({
  videoRef,
  enabled = true,
  lockdownShortcuts = true,
  lockdownContextMenu = true,
  lockdownWindowFocus = true,
  lockdownFullscreen = true,
  startCameraStream,
  stopCameraStream,
  cleanupLiveExam,
  onViolation,
  onStatusChange,
  isNumerical = false
}: ProctoringConfig) {
  const [faceStatus, setFaceStatus] = useState('📷 Waiting for camera...');
  const [faceStatusClass, setFaceStatusClass] = useState<'success' | 'warning' | 'error'>('warning');
  const [noFaceDetected, setNoFaceDetected] = useState(false);
  const [isLookingAway, setIsLookingAway] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(true);
  const [isWindowFocused, setIsWindowFocused] = useState(true);
  const [permissionBlocked, setPermissionBlocked] = useState(false);
  const [micAttemptsRemaining, setMicAttemptsRemaining] = useState(1);

  const faceMeshRef = useRef<any>(null);
  const activeLoopRef = useRef(false);
  const baselinePoseRef = useRef<HeadPose | null>(null);
  const baselineFramesRef = useRef<any[]>([]);
  const lastSampledPoseRef = useRef<any>(null);
  const lastHeadPoseRef = useRef<HeadPose | null>(null);
  const isUnloadingRef = useRef(false);

  useEffect(() => {
    const handleBeforeUnload = () => {
      isUnloadingRef.current = true;
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => {
      window.removeEventListener('beforeunload', handleBeforeUnload);
    };
  }, []);
  
  const lookingAwayStartRef = useRef<number | null>(null);
  const headMovementStartRef = useRef<number | null>(null);
  const multipleFacesStartRef = useRef<number | null>(null);
  const noFaceStartRef = useRef<number | null>(null);
  
  const lastNoFaceLogRef = useRef<number>(0);
  const lastMultipleLogRef = useRef<number>(0);

  const isNumericalRef = useRef(isNumerical);
  useEffect(() => {
    isNumericalRef.current = isNumerical;
  }, [isNumerical]);

  const updateStatus = useCallback((status: string, statusClass: 'success' | 'warning' | 'error') => {
    setFaceStatus(status);
    setFaceStatusClass(statusClass);
    onStatusChange?.(status, statusClass);
  }, [onStatusChange]);

  const processGazeAndPose = useCallback((landmarks: any) => {
    const rawPose = calculateHeadPose(landmarks);
    if (!rawPose) return;

    if (!baselinePoseRef.current) {
      if (baselineFramesRef.current.length < 10) {
        baselineFramesRef.current.push(rawPose);
        return;
      }
      const avgYaw = baselineFramesRef.current.reduce((acc, p) => acc + p.yaw, 0) / 10;
      const avgPitch = baselineFramesRef.current.reduce((acc, p) => acc + p.pitch, 0) / 10;
      const avgRoll = baselineFramesRef.current.reduce((acc, p) => acc + p.roll, 0) / 10;
      baselinePoseRef.current = { yaw: avgYaw, pitch: avgPitch, roll: avgRoll };
    }

    const currentPose = calculateHeadPose(landmarks, baselinePoseRef.current);
    if (!currentPose) return;

    const { yaw, pitch, roll } = currentPose;
    const lastSampled = lastSampledPoseRef.current;
    const now = Date.now();

    let excessiveMovement = false;
    if (lastSampled) {
      if (now - lastSampled.timestamp > 1000) {
        excessiveMovement = checkExcessiveMovement(currentPose, lastSampled);
        lastSampledPoseRef.current = { yaw, pitch, roll, timestamp: now };
      }
    } else {
      lastSampledPoseRef.current = { yaw, pitch, roll, timestamp: now };
    }

    lastHeadPoseRef.current = currentPose;

    const lookingAway = checkLookingAway(currentPose);
    setIsLookingAway(lookingAway);

    if (lookingAway) {
      if (!lookingAwayStartRef.current) {
        lookingAwayStartRef.current = now;
      }
      const isLookingDown = currentPose.pitch > 10;
      const effectiveDebounce = (isLookingDown && isNumericalRef.current) ? 4500 : PROCTOR_THRESHOLDS.LOOKING_AWAY.DEBOUNCE_MS;
      if (now - lookingAwayStartRef.current > effectiveDebounce) {
        onViolation?.('gaze', 'Looking away from screen for too long', null);
        lookingAwayStartRef.current = now; // reset to throttle
      }
    } else {
      lookingAwayStartRef.current = null;
    }

    if (excessiveMovement && !lookingAway) {
      if (!headMovementStartRef.current) {
        headMovementStartRef.current = now;
      }
      if (now - headMovementStartRef.current > PROCTOR_THRESHOLDS.EXCESSIVE_MOVEMENT.DEBOUNCE_MS) {
        onViolation?.('movement', 'Too much head movement detected', null);
        headMovementStartRef.current = null;
      }
    } else {
      headMovementStartRef.current = null;
    }
  }, [onViolation]);

  const onFaceMeshResults = useCallback((results: any) => {
    let faceCount = results.multiFaceLandmarks ? results.multiFaceLandmarks.length : 0;
    const now = Date.now();

    // Size-based and overlap-based filtering to ignore ghost overlays and background elements
    if (faceCount > 1 && results.multiFaceLandmarks) {
      const facesWithWidths = results.multiFaceLandmarks.map((landmarks: any) => {
        const p1 = landmarks[33]; // outer left eye corner
        const p2 = landmarks[263]; // outer right eye corner
        const width = (p1 && p2) ? Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2)) : 0;
        return { landmarks, width };
      });

      facesWithWidths.sort((a: any, b: any) => b.width - a.width);
      const largestWidth = facesWithWidths[0]?.width || 0;

      const validFaces = facesWithWidths.filter((face: any, index: number) => {
        if (index === 0) return true; // Keep foreground student
        if (face.width < largestWidth * 0.45) return false;
        const nose0 = facesWithWidths[0].landmarks[1];
        const noseThis = face.landmarks[1];
        if (nose0 && noseThis) {
          const dist = Math.sqrt(Math.pow(nose0.x - noseThis.x, 2) + Math.pow(nose0.y - noseThis.y, 2));
          if (dist < 0.12) return false;
        }
        return true;
      });

      faceCount = validFaces.length;
    }

    if (faceCount === 0) {
      multipleFacesStartRef.current = null;
      updateStatus('⚠️ No Face Detected', 'warning');
      setNoFaceDetected(true);
      if (!noFaceStartRef.current) {
        noFaceStartRef.current = now;
      }
      const durationNoFace = now - noFaceStartRef.current;
      const wasLookingDown = lastHeadPoseRef.current && lastHeadPoseRef.current.pitch > 10;
      const allowedBuffer = (wasLookingDown && isNumericalRef.current) ? 35000 : 4500;
      
      if (durationNoFace >= allowedBuffer) {
        if (now - lastNoFaceLogRef.current > 15000) {
          lastNoFaceLogRef.current = now;
          onViolation?.('no_face', wasLookingDown ? 'No face detected (likely looking down calculating)' : 'No face detected in camera stream', null);
        }
      }
    } else if (faceCount === 1) {
      noFaceStartRef.current = null;
      multipleFacesStartRef.current = null;
      updateStatus('👤 Face Verified', 'success');
      setNoFaceDetected(false);
      const landmarks = results.multiFaceLandmarks[0];
      processGazeAndPose(landmarks);
    } else {
      noFaceStartRef.current = null;
      if (!multipleFacesStartRef.current) {
        multipleFacesStartRef.current = now;
      }
      const durationMultiple = now - multipleFacesStartRef.current;
      if (durationMultiple > 3000) {
        updateStatus(`⚠️ Multiple Faces Detected (${faceCount})`, 'warning');
        setNoFaceDetected(false);
        if (now - lastMultipleLogRef.current > 3000) {
          lastMultipleLogRef.current = now;
          onViolation?.('multiple_faces', `Multiple faces detected: ${faceCount}`, null);
        }
      } else {
        updateStatus('👤 Face Verified', 'success');
        setNoFaceDetected(false);
        const landmarks = results.multiFaceLandmarks[0];
        processGazeAndPose(landmarks);
      }
    }
  }, [onViolation, processGazeAndPose, updateStatus]);

  const onFaceMeshResultsRef = useRef(onFaceMeshResults);
  useEffect(() => {
    onFaceMeshResultsRef.current = onFaceMeshResults;
  }, [onFaceMeshResults]);

  const startProctoring = useCallback(() => {
    const w = window as any;
    if (!w.FaceMesh || !videoRef.current) {
      updateStatus('📷 Waiting for FaceMesh library...', 'warning');
      return;
    }

    if (faceMeshRef.current) {
      // Already running, do not re-create
      return;
    }

    try {
      const faceMesh = new w.FaceMesh({
        locateFile: (file: string) => `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`
      });

      faceMesh.setOptions({
        maxNumFaces: 2,
        refineLandmarks: true,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5
      });

      faceMesh.onResults((results: any) => {
        if (onFaceMeshResultsRef.current) {
          onFaceMeshResultsRef.current(results);
        }
      });

      activeLoopRef.current = true;
      let lastAnalysis = 0;
      let isProcessing = false;
      const tick = async () => {
        if (!activeLoopRef.current) return;
        if (document.hidden) {
          requestAnimationFrame(tick);
          return;
        }
        const now = Date.now();
        if (now - lastAnalysis >= 500 && !isProcessing) {
          if (faceMesh && videoRef.current && videoRef.current.readyState >= 2 && videoRef.current.videoWidth > 0) {
            try {
              isProcessing = true;
              await faceMesh.send({ image: videoRef.current });
              lastAnalysis = now;
            } catch (e) {
              console.warn('FaceMesh frame processing error:', e);
            } finally {
              isProcessing = false;
            }
          }
        }
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);

      faceMeshRef.current = faceMesh;
      updateStatus('👤 Face Detection Ready', 'success');
    } catch (err) {
      console.error(err);
      updateStatus('⚠️ Face proctoring unavailable', 'error');
    }
  }, [videoRef, updateStatus]);

  const stopProctoring = useCallback(() => {
    activeLoopRef.current = false;
    if (faceMeshRef.current) {
      try {
        faceMeshRef.current.close();
      } catch (e) {
        console.warn('Error closing FaceMesh:', e);
      }
      faceMeshRef.current = null;
    }
  }, []);

  const handleRunCheck = useCallback(async () => {
    const result = await startCameraStream();
    if (result && !result.success) {
      if (result.cameraDenied) {
        setPermissionBlocked(true);
        alert("❌ Camera permission is mandatory. You cannot take the exam without allowing camera access.");
      } else if (result.micDenied) {
        if (micAttemptsRemaining > 0) {
          setMicAttemptsRemaining(0);
          alert("⚠️ Microphone access is required. Please click the site settings lock icon in your browser URL bar, allow Microphone access, and click 'Test Camera & Microphone' again to retry.");
        } else {
          setPermissionBlocked(true);
          alert("❌ Microphone permission is mandatory. Since you denied microphone access twice, you are blocked from taking the exam.");
        }
      }
    } else if (result && result.success) {
      return true;
    }
    return false;
  }, [startCameraStream, micAttemptsRemaining]);

  const stopAllProctoring = useCallback(() => {
    cleanupLiveExam();
    stopCameraStream();
    stopProctoring();
  }, [cleanupLiveExam, stopCameraStream, stopProctoring]);

  useEffect(() => {
    if (enabled) {
      const timer = setTimeout(startProctoring, 1000);
      return () => clearTimeout(timer);
    } else {
      stopProctoring();
    }
  }, [enabled, startProctoring, stopProctoring]);

  const lastTabSwitchLogRef = useRef<number>(0);

  const triggerTabSwitchViolation = useCallback((reason: string) => {
    const now = Date.now();
    // 4.5-second cooldown throttle on tab switch events to prevent single switch/alert blur cascades
    if (now - lastTabSwitchLogRef.current < 4500) {
      return;
    }
    lastTabSwitchLogRef.current = now;
    onViolation?.('tab_switch', reason, null);
  }, [onViolation]);

  useEffect(() => {
    if (!enabled) return;

    const checkFullscreen = () => {
      const isFull = !!document.fullscreenElement;
      setIsFullscreen(isFull);
      if (lockdownFullscreen && !isFull) {
        triggerTabSwitchViolation('Exited fullscreen mode');
      }
    };

    const handleBlur = () => {
      setIsWindowFocused(false);
      if (lockdownWindowFocus && !isUnloadingRef.current) {
        triggerTabSwitchViolation('Focus lost/tab switch detected');
      }
    };

    const handleFocus = () => {
      setIsWindowFocused(true);
    };

    const preventContextMenu = (e: MouseEvent) => {
      if (lockdownContextMenu) {
        e.preventDefault();
      }
    };

    const preventShortcuts = (e: KeyboardEvent) => {
      if (!lockdownShortcuts) return;
      const isCmd = e.ctrlKey || e.metaKey;
      if (isCmd && ['c', 'v', 'x', 'p', 's'].includes(e.key.toLowerCase())) {
        e.preventDefault();
        alert('🚨 Copying, pasting, cutting, printing, and saving are strictly disabled during this exam.');
      }
      if (e.key === 'F12') {
        e.preventDefault();
      }
    };

    if (lockdownFullscreen) {
      document.addEventListener('fullscreenchange', checkFullscreen);
      document.addEventListener('webkitfullscreenchange', checkFullscreen);
    }
    if (lockdownWindowFocus) {
      window.addEventListener('blur', handleBlur);
      window.addEventListener('focus', handleFocus);
    }
    if (lockdownContextMenu) {
      document.addEventListener('contextmenu', preventContextMenu);
    }
    if (lockdownShortcuts) {
      document.addEventListener('keydown', preventShortcuts);
    }

    return () => {
      document.removeEventListener('fullscreenchange', checkFullscreen);
      document.removeEventListener('webkitfullscreenchange', checkFullscreen);
      window.removeEventListener('blur', handleBlur);
      window.removeEventListener('focus', handleFocus);
      document.removeEventListener('contextmenu', preventContextMenu);
      document.removeEventListener('keydown', preventShortcuts);
    };
  }, [enabled, lockdownShortcuts, lockdownContextMenu, lockdownWindowFocus, lockdownFullscreen, triggerTabSwitchViolation]);

  useEffect(() => {
    return () => {
      stopProctoring();
    };
  }, [stopProctoring]);

  const recalibrateBaseline = useCallback(() => {
    baselinePoseRef.current = null;
    baselineFramesRef.current = [];
  }, []);

  return {
    faceStatus,
    faceStatusClass,
    noFaceDetected,
    isLookingAway,
    isFullscreen,
    isWindowFocused,
    permissionBlocked,
    micAttemptsRemaining,
    setMicAttemptsRemaining,
    setPermissionBlocked,
    startProctoring,
    stopProctoring,
    handleRunCheck,
    stopAllProctoring,
    recalibrateBaseline,
    setIsWindowFocused,
    setIsFullscreen
  };
}
