'use client';

import React, { useState, useRef } from 'react';
import { useAuth } from '@/context/AuthContext';
import { t } from '@/lib/i18n';
import Link from 'next/link';
import { useSearchParams, useRouter } from 'next/navigation';
import Image from 'next/image';

export default function LoginModal() {
  const { login, sendResetEmail } = useAuth();
  const searchParams = useSearchParams();
  const router = useRouter();

  const showLoginModal = searchParams.get('login') === 'true';

  // Login Form States
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [isLoggingIn, setIsLoggingIn] = useState(false);
  const [redirecting, setRedirecting] = useState(false);

  // Failure and Popup States
  const [failureCount, setFailureCount] = useState(0);
  const [showErrorPopup, setShowErrorPopup] = useState(false);
  const [popupErrorMsg, setPopupErrorMsg] = useState('');

  // Forgot Password Panel State
  const [showForgotPanel, setShowForgotPanel] = useState(false);
  const [resetEmail, setResetEmail] = useState('');
  const [resetMsg, setResetMsg] = useState('');
  const [isResetError, setIsResetError] = useState(false);
  const [isSendingReset, setIsSendingReset] = useState(false);

  // Session Conflict Modal state
  const [showConflictModal, setShowConflictModal] = useState(false);
  const resolveSessionConflict = useRef<((value: boolean) => void) | null>(null);

  const showError = (msg: string) => {
    setFailureCount((prev) => prev + 1);
    setPopupErrorMsg(msg);
    setShowErrorPopup(true);
  };

  const handleClose = () => {
    // Clear the search param to hide the modal
    router.push('/');
  };

  const handleLoginSubmit = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (isLoggingIn || redirecting) return;

    setErrorMsg('');

    if (!email.trim() || !password) {
      showError(t('Please enter both email and password'));
      return;
    }

    setIsLoggingIn(true);

    try {
      await login(email.trim(), password, () => {
        return new Promise<boolean>((resolve) => {
          resolveSessionConflict.current = resolve;
          setShowConflictModal(true);
        });
      });
      setRedirecting(true);
    } catch (error: any) {
      console.error('Login submit error:', error);
      const isCurfew = typeof error?.message === 'string' && 
        (error.message.toLowerCase().includes('curfew') || error.message.includes('10:30 PM') || error.message.includes('Rest is crucial'));
      
      const errMsg = getHindiAuthErrorMessage(error);
      if (isCurfew) {
        setPopupErrorMsg(errMsg);
        setShowErrorPopup(true);
      } else {
        showError(errMsg);
      }
      setIsLoggingIn(false);
    }
  };

  const getHindiAuthErrorMessage = (error: any): string => {
    const code = error?.code || error?.message || '';
    if (typeof code === 'string' && (code.toLowerCase().includes('curfew') || code.includes('10:30 PM') || code.includes('Rest is crucial'))) {
      return '🌙 Yashcom Sleep Curfew: Rest is crucial for conceptual mastery! 10:30 PM se morning 5:00 AM tak student login locked rahega taaki aap healthy sleep le sakein. Learning kal subah continue hogi. Sleep well! 💤';
    }
    if (typeof code === 'string' && (code.includes('approval') || code.includes('cancelled'))) {
      return code;
    }

    const map: Record<string, string> = {
      'auth/wrong-password':            'Wrong password. / पासवर्ड गलत है। कृपया दोबारा जाँच कर डालें।',
      'auth/invalid-credential':        'Wrong email/username or password. / ईमेल/यूज़रनेम या पासवर्ड गलत है। कृपया दोबारा जाँच कर डालें।',
      'auth/user-not-found':            'No account found with this email/username. / इस ईमेल/यूज़रनेम से कोई खाता नहीं मिला। कृपया जाँच लें या पहले रजिस्टर करें।',
      'auth/invalid-email':             'Email/username format is incorrect. / ईमेल या यूज़रनेम सही प्रारूप में नहीं है।',
      'auth/missing-password':          'Please enter your password. / कृपया पासवर्ड दर्ज करें।',
      'auth/user-disabled':             'This account has been disabled. Please contact admin. / यह खाता बंद कर दिया गया है। कृपया एडमिन से संपर्क करें।',
      'auth/too-many-requests':         'Too many failed attempts. Please try again later. / बहुत बार गलत प्रयास हुए हैं। कृपया कुछ समय बाद दोबारा कोशिश करें।',
      'auth/network-request-failed':    'Internet connection problem. Please check your network and try again. / इंटरनेट कनेक्शन में समस्या है। कृपया अपना नेटवर्क जाँचें और दोबारा कोशिश करें।'
    };
    
    if (map[code]) return map[code];
    return 'Could not log in. Please check your email/username and password and try again. / लॉगिन नहीं हो सका। कृपया अपनी ईमेल/यूज़रनेम और पासवर्ड जाँचकर दोबारा कोशिश करें।';
  };

  const handleSendResetEmail = async () => {
    if (!resetEmail.trim()) {
      setResetMsg('Please enter your email or username.');
      setIsResetError(true);
      return;
    }
    
    setIsSendingReset(true);
    setResetMsg('');
    
    try {
      if (!resetEmail.includes('@')) {
        setResetMsg('Please enter your registered email address.');
        setIsResetError(true);
        return;
      }
      await sendResetEmail(resetEmail.trim());
      setResetMsg('✅ Reset link sent! Check your inbox (and spam folder).');
      setIsResetError(false);
    } catch (error: any) {
      setIsResetError(true);
      if (error.code === 'auth/user-not-found') {
        setResetMsg('No account found with that email.');
      } else if (error.code === 'auth/invalid-email') {
        setResetMsg('Invalid email format.');
      } else {
        setResetMsg(error.message || 'Could not send reset link. Please try again.');
      }
    } finally {
      setIsSendingReset(false);
    }
  };

  const handleConflictResolve = (terminate: boolean) => {
    setShowConflictModal(false);
    if (resolveSessionConflict.current) {
      resolveSessionConflict.current(terminate);
      resolveSessionConflict.current = null;
    }
  };

  if (!showLoginModal) return null;

  return (
    <>
      <div className="login-overlay" onClick={handleClose}>
        <div className="login-modal" onClick={(e) => e.stopPropagation()}>
          <button className="close-btn" onClick={handleClose}>×</button>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px', marginBottom: '8px' }}>
            <Image src="/logo.png" alt="YASHCOM Logo" width={28} height={28} style={{ borderRadius: '50%', objectFit: 'cover' }} priority />
            <h2>YASHCOM - LEARN OS</h2>
          </div>
          <div className="subtitle">Sign in to your learning dashboard profile</div>



          <form onSubmit={handleLoginSubmit}>
            <div className="role-badges">
              <span className="role-pill">👨‍💼 Admin</span>
              <span className="role-pill">👨‍🎓 Student</span>
              <span className="role-pill">👨‍👩‍👧 Parent</span>
            </div>

            <div className="form-group">
               <label>Email / Username</label>
              <input 
                type="text" 
                placeholder="Enter your email" 
                autoComplete="off"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                disabled={isLoggingIn || redirecting}
              />
            </div>

            <div className="form-group">
              <label>Password</label>
              <input 
                type="password" 
                placeholder="Enter password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={isLoggingIn || redirecting}
              />
            </div>

            <button 
              type="submit" 
              className="btn btn-primary btn-block" 
              disabled={isLoggingIn || redirecting}
              style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', cursor: 'pointer' }}
            >
              {redirecting ? 'Redirecting to Dashboard...' : (isLoggingIn ? 'Logging in...' : 'Login')}
            </button>
          </form>

          {(isLoggingIn || redirecting) && (
            <div className="loading" style={{ display: 'block', marginTop: '12px', textAlign: 'center' }}>
              <div className="spinner"></div> {redirecting ? 'Redirecting to dashboard... Please wait a moment.' : 'Logging in...'}
            </div>
          )}

          <div className="auth-foot" style={{ marginTop: '14px', display: 'flex', justifyContent: 'space-between', fontSize: '11px' }}>
            <a 
              href="#" 
              style={{ color: 'var(--text-accent)', textDecoration: 'none', fontWeight: '500' }}
              onClick={(e) => {
                e.preventDefault();
                setShowForgotPanel(!showForgotPanel);
              }}
            >
              Forgot password?
            </a>
          </div>

          {showForgotPanel && (
            <div style={{ marginTop: '14px', paddingTop: '14px', borderTop: '1px solid var(--card-border)', fontSize: '12px', color: 'var(--text-accent)', lineHeight: '1.5', textAlign: 'center' }}>
              💡 <strong>Password Hint:</strong> Student & parent passwords are the student's birthdate in 6-digit <strong>DDMMYY</strong> format (e.g., September 15th, 2011 &rarr; <strong>150911</strong>, February 1st, 2012 &rarr; <strong>010212</strong>).
            </div>
          )}

          <div className="auth-foot" style={{ marginTop: '18px', borderTop: '1px solid var(--card-border)', paddingTop: '12px', fontSize: '12px', textAlign: 'center', color: 'var(--text-sub)' }}>
            <div>🆕 New user? <Link href="/register" style={{ color: 'var(--text-accent)', fontWeight: '600', textDecoration: 'none' }}>Register as a Student</Link></div>
            <p style={{ margin: '4px 0 0', fontSize: '10px', color: 'var(--text-sub)' }}>Register once, then wait for admin approval</p>
          </div>
        </div>
      </div>

      {/* Concurrent Session Conflict Modal */}
      {showConflictModal && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 10000, position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, padding: '20px' }}>
          <div className="modal-content" style={{ maxWidth: '420px', margin: 'auto', background: 'var(--surface-popover)', borderRadius: '16px', padding: '24px', border: '1px solid var(--border-popover)', boxShadow: 'var(--shadow-lg)' }}>
            <div className="modal-header">
              <h4 style={{ margin: '0 0 12px', fontSize: '18px', color: 'var(--text)' }}>⚠️ Already Logged In Elsewhere</h4>
            </div>
            <div className="modal-body" style={{ fontSize: '14px', color: 'var(--text-sub)' }}>
              <p>This account is already logged in on another device or browser.</p>
              <p style={{ marginTop: '8px', color: 'var(--text-sub)' }}>If you continue, that session will be logged out automatically.</p>
            </div>
            <div className="modal-footer" style={{ display: 'flex', gap: '8px', padding: '12px 0 0', borderTop: '1px solid var(--card-border)', marginTop: '16px' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => handleConflictResolve(true)}
                style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', padding: '8px 16px', borderRadius: '8px', cursor: 'pointer' }}
              >
                Log Out Other Session &amp; Continue
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={() => handleConflictResolve(false)}
                style={{ padding: '8px 16px', borderRadius: '8px', cursor: 'pointer' }}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
      {/* Login Error Popup Modal */}
      {showErrorPopup && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 40000 }}>
          <div className="card" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '16px', boxShadow: '0 10px 25px rgba(0,0,0,0.2)' }}>
            <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--danger)', display: 'flex', alignItems: 'center', gap: '8px' }}>
              ⚠️ Login Error
            </h3>
            
            <p style={{ margin: 0, fontSize: '13px', color: 'var(--text)', lineHeight: '1.5', whiteSpace: 'pre-line' }}>
              {popupErrorMsg}
            </p>

            <div style={{ background: 'var(--surface-3)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                <strong>Failed Attempts:</strong> {failureCount} / 3
              </div>
              
              {failureCount >= 3 && (
                <div style={{ fontSize: '11px', color: 'var(--danger)', fontWeight: 700, borderTop: '1px solid var(--border-light)', paddingTop: '6px', marginTop: '4px' }}>
                  💡 3 or more failed attempts! Please use the 'Forgot password?' option below to reset your password.
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={() => {
                  setShowErrorPopup(false);
                  if (failureCount >= 3) {
                    setShowForgotPanel(true);
                  }
                }}
                style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', padding: '8px 20px', borderRadius: 'var(--radius-sm)', cursor: 'pointer', fontWeight: 'bold' }}
              >
                OK
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
