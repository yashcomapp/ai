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
  
  const onTimeUpRef = useRef(onTimeUp);
  const onTickRef = useRef(onTick);

  // Sync callbacks to avoid recreation triggers
  useEffect(() => {
    onTimeUpRef.current = onTimeUp;
    onTickRef.current = onTick;
  }, [onTimeUp, onTick]);

  // Sync initial seconds if it loads later
  useEffect(() => {
    setTimeRemaining(initialSeconds);
  }, [initialSeconds]);

  useEffect(() => {
    if (isPaused) return;

    timerRef.current = setInterval(() => {
      setTimeRemaining(prev => {
        if (prev <= 0) {
          if (timerRef.current) clearInterval(timerRef.current);
          return 0;
        }
        if (prev <= 1) {
          if (timerRef.current) clearInterval(timerRef.current);
          onTimeUpRef.current();
          return 0;
        }

        if (onTickRef.current) onTickRef.current();
        return prev - 1;
      });
    }, 1000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [isPaused]);

  const addExtraTime = (seconds: number) => {
    setTimeRemaining(prev => prev + seconds);
  };

  return {
    timeRemaining,
    setTimeRemaining,
    formattedTime: formatDuration(timeRemaining),
    addExtraTime
  };
}
