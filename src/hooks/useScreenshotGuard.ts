'use client';

import { useState, useEffect, useCallback, useRef } from 'react';

export interface UseScreenshotGuardOptions {
  enabled?: boolean;
  blurOnFocusLoss?: boolean;
  clearClipboardOnPrint?: boolean;
  onViolation?: (reason: string) => void;
}

export function useScreenshotGuard({
  enabled = true,
  blurOnFocusLoss = true,
  clearClipboardOnPrint = true,
  onViolation
}: UseScreenshotGuardOptions = {}) {
  const [isObscured, setIsObscured] = useState(false);
  const [alertMessage, setAlertMessage] = useState<string | null>(null);
  const alertTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const obscureTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const triggerAlert = useCallback((msg: string) => {
    setAlertMessage(msg);
    if (alertTimeoutRef.current) clearTimeout(alertTimeoutRef.current);
    alertTimeoutRef.current = setTimeout(() => {
      setAlertMessage(null);
    }, 3500);

    if (onViolation) {
      try {
        onViolation(msg);
      } catch (err) {
        console.warn('Screenshot violation callback error:', err);
      }
    }
  }, [onViolation]);

  const clearClipboard = useCallback(() => {
    if (!clearClipboardOnPrint) return;
    try {
      if (typeof navigator !== 'undefined' && navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText('[Confidential Proctored Exam Content Protected]').catch(() => null);
      }
    } catch {
      // Ignore clipboard permission rejections silently
    }
  }, [clearClipboardOnPrint]);

  useEffect(() => {
    if (!enabled) {
      setIsObscured(false);
      return;
    }

    // 1. Keyboard Interception
    const handleKeyDown = (e: KeyboardEvent) => {
      // PrintScreen / PrtScn
      if (e.key === 'PrintScreen' || e.code === 'PrintScreen' || e.keyCode === 44) {
        e.preventDefault();
        clearClipboard();
        setIsObscured(true);
        triggerAlert('Screenshot shortcut intercepted. Content is protected.');
        
        // Obscure for 2 seconds to spoil OS grab
        if (obscureTimeoutRef.current) clearTimeout(obscureTimeoutRef.current);
        obscureTimeoutRef.current = setTimeout(() => {
          if (document.hasFocus()) {
            setIsObscured(false);
          }
        }, 2000);
        return;
      }

      // Mac Screenshot Shortcuts: Cmd + Shift + 3 / 4 / 5
      if (e.metaKey && e.shiftKey && ['3', '4', '5'].includes(e.key)) {
        e.preventDefault();
        clearClipboard();
        setIsObscured(true);
        triggerAlert('Screen capture shortcut blocked.');
        return;
      }

      // Windows Snipping Tool shortcut indicator: Shift + Win + S (Shift+Meta+S or Ctrl+Shift+S)
      if (e.shiftKey && (e.metaKey || (e.ctrlKey && e.altKey)) && (e.key === 's' || e.key === 'S')) {
        e.preventDefault();
        clearClipboard();
        setIsObscured(true);
        triggerAlert('Snipping tool shortcut blocked.');
        return;
      }

      // Print: Ctrl + P / Cmd + P
      if ((e.ctrlKey || e.metaKey) && (e.key === 'p' || e.key === 'P')) {
        e.preventDefault();
        triggerAlert('Printing or saving as PDF is disabled during exams.');
        return;
      }

      // Save page: Ctrl + S / Cmd + S
      if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')) {
        e.preventDefault();
        triggerAlert('Saving exam pages is disabled.');
        return;
      }

      // DevTools: F12, Ctrl + Shift + I, Cmd + Option + I, Ctrl + Shift + J, Ctrl + U
      if (
        e.key === 'F12' ||
        ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'i' || e.key === 'I' || e.key === 'j' || e.key === 'J' || e.key === 'c' || e.key === 'C')) ||
        ((e.ctrlKey || e.metaKey) && (e.key === 'u' || e.key === 'U'))
      ) {
        e.preventDefault();
        triggerAlert('Developer tools and source inspection are disabled.');
        return;
      }
    };

    // 2. Window Blur / Focus Handling (Anti-Snipping & Background Cloak)
    // On mobile devices (Android/iOS), virtual keyboards, scrolling address bars, and system overlays
    // frequently fire window.blur and visibility changes. Mobile devices are exempt to prevent false blurs.
    const isMobile = typeof navigator !== 'undefined' && (/Mobi|Android|iPhone|iPad|iPod/i.test(navigator.userAgent) || ('ontouchstart' in window && window.innerWidth <= 1024));

    const handleBlur = () => {
      if (blurOnFocusLoss && !isMobile) {
        setIsObscured(true);
      }
    };

    const handleFocus = () => {
      if (obscureTimeoutRef.current) clearTimeout(obscureTimeoutRef.current);
      // Brief debounce on focus return
      obscureTimeoutRef.current = setTimeout(() => {
        setIsObscured(false);
      }, 300);
    };

    const handleVisibilityChange = () => {
      if (document.hidden && !isMobile) {
        setIsObscured(true);
      } else {
        if (obscureTimeoutRef.current) clearTimeout(obscureTimeoutRef.current);
        obscureTimeoutRef.current = setTimeout(() => {
          setIsObscured(false);
        }, 300);
      }
    };

    // 3. Right-Click Context Menu Prevention
    const handleContextMenu = (e: MouseEvent) => {
      // Only prevent inside exam question containers or whole document during exam
      e.preventDefault();
    };

    window.addEventListener('keydown', handleKeyDown, true);
    window.addEventListener('keyup', (e: KeyboardEvent) => {
      if (e.key === 'PrintScreen' || e.code === 'PrintScreen' || e.keyCode === 44) {
        clearClipboard();
      }
    }, true);

    window.addEventListener('blur', handleBlur);
    window.addEventListener('focus', handleFocus);
    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('contextmenu', handleContextMenu);

    return () => {
      window.removeEventListener('keydown', handleKeyDown, true);
      window.removeEventListener('blur', handleBlur);
      window.removeEventListener('focus', handleFocus);
      document.removeEventListener('visibilitychange', handleVisibilityChange);
      window.removeEventListener('contextmenu', handleContextMenu);
      if (alertTimeoutRef.current) clearTimeout(alertTimeoutRef.current);
      if (obscureTimeoutRef.current) clearTimeout(obscureTimeoutRef.current);
    };
  }, [enabled, blurOnFocusLoss, clearClipboard, triggerAlert]);

  return {
    isEnabled: enabled,
    isObscured,
    alertMessage,
    dismissAlert: () => setAlertMessage(null)
  };
}
