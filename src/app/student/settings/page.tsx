'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { EmailAuthProvider, reauthenticateWithCredential, updatePassword } from 'firebase/auth';
import { usePushNotifications } from '@/hooks/usePushNotifications';
import dynamic from 'next/dynamic';
const HardwareCheckMockTestModal = dynamic(() => import('@/components/HardwareCheckMockTestModal'), { ssr: false });

interface ProfileData {
  name: string;
  email: string;
  parentEmail: string;
  dob: string;
}

interface StatsData {
  totalExams: number;
  avgScore: string;
  weakTopicsCount: number;
  masteredTopics: number;
}

export default function StudentSettingsPage() {
  const { firebaseUser, logout, user } = useAuth();
  const { toggleTheme } = useTheme();
  const { initFCM } = usePushNotifications();
  const [syncingPush, setSyncingPush] = useState(false);
  const [isMockTestOpen, setIsMockTestOpen] = useState(false);
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const renderCardSkeleton = (linesCount: number = 3) => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', height: '43px', display: 'flex', alignItems: 'center' }}>
        <div style={{ width: '120px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
      </div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {Array.from({ length: linesCount }).map((_, i) => (
          <div key={i} style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <div style={{ width: '80px', height: '10px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            <div style={{ width: '100%', height: '36px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)' }}></div>
          </div>
        ))}
        <div style={{ width: '110px', height: '34px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', marginTop: '10px' }}></div>
      </div>
    </div>
  );

  const renderDiagSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', height: '43px', display: 'flex', alignItems: 'center' }}>
        <div style={{ width: '220px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
      </div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div style={{ width: '100%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
        <div style={{ width: '60%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
        <div style={{ width: '140px', height: '30px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-sm)', marginTop: '6px' }}></div>
      </div>
    </div>
  );

  const renderPushSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', height: '43px', display: 'flex', alignItems: 'center' }}>
        <div style={{ width: '180px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
      </div>
      <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div style={{ width: '100%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
        <div style={{ width: '80%', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
      </div>
    </div>
  );

  const renderAppInfoSkeleton = () => (
    <div className="card skeleton-blink" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
      <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', height: '43px', display: 'flex', alignItems: 'center' }}>
        <div style={{ width: '130px', height: '14px', background: 'var(--border-light)', borderRadius: '4px' }}></div>
      </div>
      <div style={{ padding: '20px' }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '15px' }}>
          {[1, 2, 3, 4, 5, 6].map(i => (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <div style={{ width: '16px', height: '16px', background: 'var(--bg-soft)', borderRadius: '50%' }}></div>
              <div style={{ width: '120px', height: '12px', background: 'var(--bg-soft)', borderRadius: '2px' }}></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
  
  // Profile form state
  const [profile, setProfile] = useState<ProfileData>({
    name: '',
    email: '',
    parentEmail: '',
    dob: ''
  });
  
  // Stats state
  const [stats, setStats] = useState<StatsData>({
    totalExams: 0,
    avgScore: '0.0%',
    weakTopicsCount: 0,
    masteredTopics: 0
  });

  const [savingProfile, setSavingProfile] = useState(false);
  const [greeting, setGreeting] = useState('Hello');

  const [notificationPermission, setNotificationPermission] = useState<string>('default');
  const [notificationsSupported, setNotificationsSupported] = useState<boolean>(true);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const supported = 'Notification' in window;
      setNotificationsSupported(supported);
      if (supported) {
        setNotificationPermission(Notification.permission);
      }
    }
  }, []);

  const handleSyncPush = async () => {
    setSyncingPush(true);
    try {
      if (typeof window !== 'undefined' && 'Notification' in window) {
        const permission = await Notification.requestPermission();
        setNotificationPermission(permission);
        if (permission === 'granted') {
          await initFCM();
          const idToken = firebaseUser ? await firebaseUser.getIdToken() : null;
          if (idToken) {
            const res = await fetch('/api/auth/session', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${idToken}`
              },
              body: JSON.stringify({ action: 'get_profile' })
            });
            if (res.ok) {
              window.location.reload();
            }
          }
        }
      }
    } catch (err: any) {
      console.error('Manual push sync error:', err);
    } finally {
      setSyncingPush(false);
    }
  };

  const loadSettingsData = async () => {
    if (!firebaseUser) return;
    setLoading(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/settings', {
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (!res.ok) {
        throw new Error('Failed to load profile settings data.');
      }
      const data = await res.json();
      setProfile(data.profile);
      setStats(data.stats);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Error loading settings.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (firebaseUser) {
      loadSettingsData();
      
      const hour = new Date().getHours();
      if (hour < 12) setGreeting('Good Morning ☀️');
      else if (hour < 17) setGreeting('Good Afternoon 🌤️');
      else setGreeting('Good Evening 🌙');
    }
  }, [firebaseUser]);

  const handleSaveProfile = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!firebaseUser || savingProfile) return;

    if (!profile.name.trim()) {
      alert('Please enter your full name.');
      return;
    }

    setSavingProfile(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/student/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          name: profile.name,
          parentEmail: profile.parentEmail,
          dob: profile.dob
        })
      });

      if (!res.ok) {
        throw new Error('Failed to save profile changes.');
      }

      alert('✅ Profile changes saved successfully!');
    } catch (err: any) {
      alert(err.message || 'Error saving profile.');
    } finally {
      setSavingProfile(false);
    }
  };



  return (
    <div className="page-wrapper" style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', background: 'var(--bg)' }}>
      {/* Top Header Bar matching Review Page */}
      <div className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => router.push('/student')}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push('/student')}>YASHCOM</span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          
          <button className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </div>

      <style>{`
        @keyframes skeleton-blink {
          0% { opacity: 0.6; }
          50% { opacity: 1; }
          100% { opacity: 0.6; }
        }
        .skeleton-blink {
          animation: skeleton-blink 1.5s infinite ease-in-out;
        }
      `}</style>

      {/* Main Container */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '800px', width: '100%', margin: '0 auto' }}>
        {error && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
            {error}
          </div>
        )}

        <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          {loading ? (
            <>
              {/* Top forms split layout */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
                {renderCardSkeleton(4)}
                {renderCardSkeleton(3)}
              </div>
              {renderDiagSkeleton()}
              {renderPushSkeleton()}
              {renderAppInfoSkeleton()}
            </>
          ) : (
            <>
              {/* Top forms split layout */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
                {/* Profile form */}
                <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
                  <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontWeight: 600, fontSize: '13px' }}>
                    👤 Profile Information
                  </div>
              <form onSubmit={handleSaveProfile} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, marginBottom: '5px', color: 'var(--text-muted)' }}>Full Name</label>
                  <input 
                    type="text" 
                    value={profile.name} 
                    onChange={e => setProfile({ ...profile, name: e.target.value })}
                    style={{ width: '100%', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, marginBottom: '5px', color: 'var(--text-muted)' }}>Email Address</label>
                  <input 
                    type="email" 
                    value={profile.email} 
                    disabled 
                    style={{ width: '100%', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px', background: 'var(--bg-soft)', color: 'var(--text-muted)', cursor: 'not-allowed' }}
                  />
                  <small style={{ fontSize: '9px', color: 'var(--text-muted)', marginTop: '3px', display: 'block' }}>Registered email cannot be modified.</small>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, marginBottom: '5px', color: 'var(--text-muted)' }}>Parent Email</label>
                  <input 
                    type="email" 
                    value={profile.parentEmail} 
                    onChange={e => setProfile({ ...profile, parentEmail: e.target.value })}
                    style={{ width: '100%', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                  <small style={{ fontSize: '9px', color: 'var(--text-muted)', marginTop: '3px', display: 'block' }}>Required for parent approvals & metrics alerts.</small>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '11px', fontWeight: 600, marginBottom: '5px', color: 'var(--text-muted)' }}>Date of Birth</label>
                  <input 
                    type="date" 
                    value={profile.dob} 
                    onChange={e => setProfile({ ...profile, dob: e.target.value })}
                    style={{ width: '100%', padding: '8px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', fontSize: '13px', background: 'var(--surface)', color: 'var(--text)' }}
                  />
                </div>
                <button type="submit" className="btn btn-primary" disabled={savingProfile} style={{ marginTop: '10px' }}>
                  {savingProfile ? 'Saving Changes...' : '💾 Save Profile'}
                </button>
              </form>
            </div>


          </div>

          {/* Proctoring Hardware Diagnostic Card */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontWeight: 600, fontSize: '13px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span>🖥️ Hardware Diagnostic Mock Test</span>
              <span className="badge badge-info" style={{ fontSize: '10px', background: 'var(--accent)', color: '#fff', padding: '2px 8px', borderRadius: '4px' }}>
                Mock Test
              </span>
            </div>
            <div style={{ padding: '20px', fontSize: '12px', lineHeight: '1.5' }}>
              <p style={{ margin: '0 0 12px 0', color: 'var(--text-muted)' }}>
                Aapke system ka camera, microphone, aur online proctoring functions checking karne ke liye 5 general knowledge questions ka mock test design kiya gaya hai.
                Is mock test ke marks results me calculate nahi honge.
              </p>
              <button 
                type="button" 
                className="btn btn-primary btn-sm" 
                onClick={() => setIsMockTestOpen(true)}
                style={{ fontWeight: 700 }}
              >
                🚀 Run Hardware Check
              </button>
            </div>
          </div>

          {/* Push Notifications Card */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontWeight: 600, fontSize: '13px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span>🔔 Push Notifications Status</span>
              {!notificationsSupported ? (
                <span className="badge" style={{ fontSize: '10px', background: 'var(--danger)', color: '#fff', padding: '2px 8px', borderRadius: '4px' }}>
                  Unsupported
                </span>
              ) : (
                <span className={`badge ${notificationPermission === 'granted' ? (user?.hasPushRegistered ? 'badge-success' : 'badge-warning') : notificationPermission === 'denied' ? 'badge-danger' : 'badge-warning'}`} style={{ fontSize: '10px', background: notificationPermission === 'granted' ? (user?.hasPushRegistered ? 'var(--success)' : 'var(--warning)') : notificationPermission === 'denied' ? 'var(--danger)' : 'var(--warning)', color: '#fff', padding: '2px 8px', borderRadius: '4px' }}>
                  {notificationPermission === 'granted' ? (user?.hasPushRegistered ? 'Active' : 'Sync Pending') : notificationPermission === 'denied' ? 'Blocked' : 'Not Requested'}
                </span>
              )}
            </div>
            <div style={{ padding: '20px', fontSize: '12px', lineHeight: '1.5' }}>
              {!notificationsSupported ? (
                <div style={{ color: 'var(--danger)', fontWeight: 600 }}>
                  ❌ Push notifications are not supported on this browser/device. (iPhone/Safari users: please use the "Add to Home Screen" action to run this app as a PWA, or use Google Chrome/Microsoft Edge on your desktop/Android device).
                </div>
              ) : notificationPermission === 'granted' && user?.hasPushRegistered ? (
                <div style={{ color: 'var(--success)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span>✅ Your device is registered to receive notifications.</span>
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{ color: notificationPermission === 'denied' ? 'var(--danger)' : 'var(--warning)', fontWeight: 700 }}>
                    {notificationPermission === 'denied' 
                      ? '❌ Notifications are blocked! Please allow notifications in browser settings.' 
                      : notificationPermission === 'granted' && !user?.hasPushRegistered
                      ? '⚠️ Browser permission is granted, but your device is not registered on the server. Please click Sync Device below.'
                      : '⚠️ Notifications are not enabled yet.'}
                  </div>
                  <div style={{ background: 'var(--surface-3)', padding: '12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)', fontSize: '11px', color: 'var(--text-muted)' }}>
                    <div style={{ fontWeight: 800, color: 'var(--text)', marginBottom: '4px' }}>🔔 How to Enable Notifications:</div>
                    <ol style={{ margin: '0', paddingLeft: '16px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      <li>Click the lock icon (🔒) or settings icon in your browser URL bar.</li>
                      <li>Find the Notifications option and set it to "Allow".</li>
                      <li>If permissions are already allowed, click "Sync Device" below to register.</li>
                    </ol>
                  </div>
                  {notificationPermission !== 'denied' && (
                    <button 
                      type="button" 
                      className="btn btn-primary btn-sm" 
                      onClick={handleSyncPush}
                      disabled={syncingPush}
                      style={{ width: 'fit-content', alignSelf: 'flex-start', marginTop: '6px' }}
                    >
                      {syncingPush ? '🔄 Syncing Device...' : '🔔 Sync Device'}
                    </button>
                  )}
                </div>
              )}
            </div>
          </div>

          {/* App Info card */}
          <div className="card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', overflow: 'hidden' }}>
            <div style={{ padding: '12px 16px', background: 'var(--bg-soft)', borderBottom: '1px solid var(--border-light)', fontWeight: 600, fontSize: '13px' }}>
              ℹ️ App Information
            </div>
            <div style={{ padding: '20px' }}>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '15px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>📱</span> <span>Coaching App v5.0.0</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>🤖</span> <span>AI-Powered Questions</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>📅</span> <span>Weekly Adaptive Tests</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>🎯</span> <span>Truth Index Accuracy</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>🎥</span> <span>Proctored Exams</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '12px' }}>
                  <span>👪</span> <span>Parent Reporting</span>
                </div>
              </div>
            </div>
          </div>
            </>
          )}
        </div>
      </main>
      <HardwareCheckMockTestModal isOpen={isMockTestOpen} onClose={() => setIsMockTestOpen(false)} />
    </div>
  );
}
