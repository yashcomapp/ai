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
      <style jsx>{`
        .login-overlay {
          position: fixed;
          inset: 0;
          background: rgba(15, 23, 42, 0.45);
          backdrop-filter: blur(10px);
          -webkit-backdrop-filter: blur(10px);
          display: flex;
          align-items: center;
          justify-content: center;
          z-index: 9999;
          padding: 16px;
          animation: modalFadeIn 0.2s ease-out;
        }
        .login-modal {
          background: var(--surface);
          padding: 24px 28px;
          border-radius: var(--radius-lg);
          box-shadow: var(--shadow-lg);
          width: 100%;
          max-width: 380px;
          border: 1px solid var(--border-light);
          position: relative;
          box-sizing: border-box;
          animation: modalSlideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .close-btn {
          position: absolute;
          top: 14px;
          right: 14px;
          background: var(--surface-2);
          border: 1px solid var(--border-light);
          border-radius: 50%;
          width: 28px;
          height: 28px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 16px;
          cursor: pointer;
          color: var(--text-muted);
          transition: all 0.15s ease;
        }
        .close-btn:hover {
          color: var(--text);
          background: var(--surface-3);
        }
        .login-modal-header {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          margin-bottom: 4px;
        }
        .login-modal-title {
          font-size: 15px;
          font-weight: 800;
          color: var(--text);
          margin: 0;
          letter-spacing: 0.2px;
        }
        .login-modal-subtitle {
          font-size: 12px;
          color: var(--text-muted);
          margin: 0 0 16px;
          text-align: center;
        }
        .role-badges {
          display: flex;
          justify-content: center;
          gap: 6px;
          margin-bottom: 16px;
        }
        .role-pill {
          background: var(--bg-soft);
          border: 1px solid var(--border-light);
          color: var(--text-secondary);
          font-size: 11px;
          font-weight: 700;
          padding: 3px 10px;
          border-radius: var(--radius-pill);
        }
        .form-group {
          margin-bottom: 12px;
          text-align: left;
        }
        .form-group label {
          display: block;
          font-size: 11px;
          font-weight: 700;
          color: var(--text-secondary);
          margin-bottom: 4px;
          text-transform: uppercase;
          letter-spacing: 0.3px;
        }
        .form-group input {
          width: 100%;
          padding: 9px 12px;
          border: 1.5px solid var(--border);
          border-radius: var(--radius-sm);
          background: var(--surface-2);
          font-size: 13px;
          color: var(--text);
          box-sizing: border-box;
          outline: none;
          transition: all 0.2s ease;
        }
        .form-group input:focus {
          border-color: var(--accent);
          background: var(--surface);
          box-shadow: 0 0 0 3px var(--accent-ring);
        }
        .btn-login-submit {
          width: 100%;
          padding: 10px;
          border-radius: var(--radius-sm);
          font-weight: 800;
          font-size: 14px;
          background: var(--accent-grad);
          color: #ffffff;
          border: none;
          cursor: pointer;
          box-shadow: var(--shadow-sm);
          transition: all 0.2s ease;
          margin-top: 4px;
        }
        .btn-login-submit:hover:not(:disabled) {
          transform: translateY(-1px);
          box-shadow: var(--shadow-md);
        }
        .btn-login-submit:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }
        @keyframes modalFadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes modalSlideUp {
          from { transform: translateY(16px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
      `}</style>

      <div className="login-overlay" onClick={handleClose}>
        <div className="login-modal" onClick={(e) => e.stopPropagation()}>
          <button className="close-btn" onClick={handleClose}>×</button>
          
          <div className="login-modal-header">
            <Image src="/logo.png" alt="YASHCOM Logo" width={26} height={26} style={{ borderRadius: '50%', objectFit: 'cover' }} priority />
            <h2 className="login-modal-title">YASHCOM — LEARN OS</h2>
          </div>
          <div className="login-modal-subtitle">Sign in to your learning dashboard profile</div>

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
                placeholder="Enter your registered email" 
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
              className="btn-login-submit" 
              disabled={isLoggingIn || redirecting}
            >
              {redirecting ? 'Redirecting to Dashboard...' : (isLoggingIn ? 'Logging in...' : 'Sign In →')}
            </button>
          </form>

          {(isLoggingIn || redirecting) && (
            <div className="loading" style={{ display: 'block', marginTop: '12px', textAlign: 'center', fontSize: '12px' }}>
              <div className="spinner"></div> {redirecting ? 'Redirecting to dashboard... Please wait a moment.' : 'Logging in...'}
            </div>
          )}

          <div style={{ marginTop: '12px', display: 'flex', justifyContent: 'center', fontSize: '11.5px' }}>
            <a 
              href="#" 
              style={{ color: 'var(--accent)', textDecoration: 'none', fontWeight: '600' }}
              onClick={(e) => {
                e.preventDefault();
                setShowForgotPanel(!showForgotPanel);
              }}
            >
              Forgot password?
            </a>
          </div>

          {showForgotPanel && (
            <div style={{ marginTop: '12px', padding: '10px 12px', background: 'var(--surface-2)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '11.5px', color: 'var(--text-secondary)', lineHeight: '1.45', textAlign: 'center' }}>
              💡 <strong>Password Hint:</strong> Student &amp; parent passwords are the student's birthdate in 6-digit <strong>DDMMYY</strong> format (e.g., September 15th, 2011 &rarr; <strong>150911</strong>).
            </div>
          )}

          <div style={{ marginTop: '16px', borderTop: '1px solid var(--border-light)', paddingTop: '12px', fontSize: '12px', textAlign: 'center', color: 'var(--text-secondary)' }}>
            <div>🆕 New user? <Link href="/register" style={{ color: 'var(--accent)', fontWeight: '700', textDecoration: 'none' }}>Register as a Student</Link></div>
            <p style={{ margin: '4px 0 0', fontSize: '10.5px', color: 'var(--text-muted)' }}>Register once, then wait for admin approval</p>
          </div>
        </div>
      </div>

      {/* Concurrent Session Conflict Modal */}
      {showConflictModal && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(15, 23, 42, 0.45)', backdropFilter: 'blur(10px)', WebkitBackdropFilter: 'blur(10px)', zIndex: 10000, position: 'fixed', inset: 0, padding: '16px' }}>
          <div className="modal-content" style={{ maxWidth: '400px', width: '100%', margin: 'auto', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', padding: '20px', border: '1px solid var(--border-light)', boxShadow: 'var(--shadow-lg)' }}>
            <div className="modal-header">
              <h4 style={{ margin: '0 0 10px', fontSize: '15px', fontWeight: 800, color: 'var(--text)' }}>⚠️ Already Logged In Elsewhere</h4>
            </div>
            <div className="modal-body" style={{ fontSize: '13px', color: 'var(--text-secondary)', lineHeight: '1.45' }}>
              <p style={{ margin: 0 }}>This account is currently active on another device or browser session.</p>
              <p style={{ marginTop: '6px', color: 'var(--text-secondary)' }}>If you continue, that session will be logged out automatically.</p>
            </div>
            <div className="modal-footer" style={{ display: 'flex', gap: '8px', padding: '12px 0 0', borderTop: '1px solid var(--border-light)', marginTop: '14px', justifyContent: 'flex-end' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => handleConflictResolve(false)}
                style={{ padding: '6px 14px', borderRadius: 'var(--radius-sm)', fontSize: '12px', fontWeight: 600, cursor: 'pointer' }}
              >
                Cancel
              </button>
              <button 
                className="btn btn-primary" 
                onClick={() => handleConflictResolve(true)}
                style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', padding: '6px 14px', borderRadius: 'var(--radius-sm)', fontSize: '12px', fontWeight: 700, cursor: 'pointer' }}
              >
                Log Out Other &amp; Continue
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Login Error Popup Modal */}
      {showErrorPopup && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(15, 23, 42, 0.45)', backdropFilter: 'blur(10px)', WebkitBackdropFilter: 'blur(10px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 40000, padding: '16px' }}>
          <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', padding: '20px', borderRadius: 'var(--radius-lg)', maxWidth: '400px', width: '100%', display: 'flex', flexDirection: 'column', gap: '12px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ margin: 0, fontSize: '14px', fontWeight: 800, color: 'var(--danger)', display: 'flex', alignItems: 'center', gap: '6px' }}>
              ⚠️ Login Error
            </h3>
            
            <p style={{ margin: 0, fontSize: '12.5px', color: 'var(--text)', lineHeight: '1.5', whiteSpace: 'pre-line' }}>
              {popupErrorMsg}
            </p>

            <div style={{ background: 'var(--surface-2)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '4px' }}>
              <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                <strong>Failed Attempts:</strong> {failureCount} / 3
              </div>
              
              {failureCount >= 3 && (
                <div style={{ fontSize: '11px', color: 'var(--danger)', fontWeight: 700, borderTop: '1px solid var(--border-light)', paddingTop: '4px', marginTop: '2px' }}>
                  💡 3 or more failed attempts! Please use the 'Forgot password?' option to reset your password.
                </div>
              )}
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
              <button 
                type="button" 
                className="btn btn-primary" 
                onClick={() => {
                  setShowErrorPopup(false);
                  if (failureCount >= 3) {
                    setShowForgotPanel(true);
                  }
                }}
                style={{ background: 'var(--accent-grad)', color: '#fff', border: 'none', padding: '6px 18px', borderRadius: 'var(--radius-sm)', cursor: 'pointer', fontWeight: 800, fontSize: '12.5px' }}
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
