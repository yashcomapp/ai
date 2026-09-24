import { useEffect, useRef, useState } from 'react';
import { formatDuration } from '@/lib/dateUtils';

interface UseExamTimerProps {
  initialSeconds: number;
  isPaused: boolean;
  onTimeUp: () => void;
  onTick?: () => void;
}

export function useExamTimer({ initialSeconds, isPaused, onTimeUp, onTick }: UseExamTimerProps) {
  const [timeRemaining, setTimeRemaining] = useState<number>(initialSeconds);
  const timerRef = useRef<NodeJS.Timeout | null>(null);
  const endTimeRef = useRef<number>(Date.now() + initialSeconds * 1000);
  const isPausedRef = useRef<boolean>(isPaused);
  const timeRemainingRef = useRef<number>(initialSeconds);
  
  const onTimeUpRef = useRef(onTimeUp);
  const onTickRef = useRef(onTick);

  // Sync callbacks to avoid recreation triggers
  useEffect(() => {
    onTimeUpRef.current = onTimeUp;
    onTickRef.current = onTick;
  }, [onTimeUp, onTick]);

  useEffect(() => {
    isPausedRef.current = isPaused;
  }, [isPaused]);

  useEffect(() => {
    timeRemainingRef.current = timeRemaining;
  }, [timeRemaining]);

  // Sync initial seconds if it loads later or changes
  useEffect(() => {
    setTimeRemaining(initialSeconds);
    timeRemainingRef.current = initialSeconds;
    endTimeRef.current = Date.now() + initialSeconds * 1000;
  }, [initialSeconds]);

  useEffect(() => {
    if (isPaused) {
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
      return;
    }

    // When starting or resuming, set authoritative end time from current remaining seconds
    endTimeRef.current = Date.now() + timeRemainingRef.current * 1000;

    const checkWallClock = () => {
      if (isPausedRef.current) return;
      const now = Date.now();
      const remaining = Math.max(0, Math.ceil((endTimeRef.current - now) / 1000));
      
      if (remaining <= 0) {
        if (timerRef.current) {
          clearInterval(timerRef.current);
          timerRef.current = null;
        }
        setTimeRemaining(0);
        timeRemainingRef.current = 0;
        onTimeUpRef.current();
        return;
      }

      setTimeRemaining(remaining);
      timeRemainingRef.current = remaining;
      if (onTickRef.current) {
        onTickRef.current();
      }
    };

    // Immediate check on start/resume
    checkWallClock();

    timerRef.current = setInterval(checkWallClock, 1000);

    // Event listeners to immediately catch up when tab visibility changes or window is focused
    const handleVisibilityOrFocus = () => {
      checkWallClock();
    };

    document.addEventListener('visibilitychange', handleVisibilityOrFocus);
    window.addEventListener('focus', handleVisibilityOrFocus);

    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }
      document.removeEventListener('visibilitychange', handleVisibilityOrFocus);
      window.removeEventListener('focus', handleVisibilityOrFocus);
    };
  }, [isPaused]);

  const addExtraTime = (seconds: number) => {
    endTimeRef.current += seconds * 1000;
    setTimeRemaining(prev => {
      const next = prev + seconds;
      timeRemainingRef.current = next;
      return next;
    });
  };

  return {
    timeRemaining,
    setTimeRemaining: (val: number | ((prev: number) => number)) => {
      setTimeRemaining(prev => {
        const next = typeof val === 'function' ? val(prev) : val;
        timeRemainingRef.current = next;
        endTimeRef.current = Date.now() + next * 1000;
        return next;
      });
    },
    formattedTime: formatDuration(timeRemaining),
    addExtraTime
  };
}
