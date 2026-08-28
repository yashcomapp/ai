'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { auth } from '@/lib/firebase/client';
import { updatePassword } from 'firebase/auth';

interface Exam {
  examId: string;
  name: string;
  class: string;
  subjectCode: string;
  createdAt: any;
}

export default function AdminSettingsPage() {
  const { firebaseUser, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState<'password' | 'backup' | 'utils' | 'cleanup'>('password');

  // Password change states
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [passwordUpdating, setPasswordUpdating] = useState(false);

  // Backup / utility states
  const [processing, setProcessing] = useState(false);
  const [harmonizing, setHarmonizing] = useState(false);
  const [harmonizeResult, setHarmonizeResult] = useState<any>(null);
  const [restoreJson, setRestoreJson] = useState<any>(null);
  const [selectedProtected, setSelectedProtected] = useState<Record<string, boolean>>({
    syllabus: false,
    users: false,
    templates: false,
    config: false,
    batches: false
  });

  // Database Cleanup states
  const [cleanupStats, setCleanupStats] = useState<any>({
    objectiveExams: '-',
    subjectiveExams: '-',
    totalOrphaned: '-',
    objectiveAttempts: 0,
    objectiveReviews: 0,
    objectiveAssignments: 0,
    subjectiveAttempts: 0,
    subjectiveReviews: 0,
    subjectiveAssignments: 0,
    peerAssignments: 0,
    evaluations: 0,
    liveSessions: 0,
    masteryRecordsToClearLink: 0,
    orphanedProfiles: 0
  });
  const [cleanupLogs, setCleanupLogs] = useState<string[]>([]);
  const [orphanedData, setOrphanedData] = useState<any>(null);
  const [scanning, setScanning] = useState(false);
  const [cleaning, setCleaning] = useState(false);
  const [fixing, setFixing] = useState(false);

  const addCleanupLog = (msg: string, type: 'info' | 'success' | 'error' | 'warning' = 'info') => {
    const time = new Date().toLocaleTimeString();
    setCleanupLogs(prev => [...prev, `[${time}] ${msg}`]);
  };

  const handleFindOrphaned = async () => {
    if (!firebaseUser) return;
    setScanning(true);
    setCleanupLogs([]);
    addCleanupLog('🔍 Finding all orphaned references...', 'warning');

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/cleanup', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) throw new Error('Failed to fetch cleanup report.');
      const data = await res.json();
      if (!data.success) throw new Error(data.error || 'Unknown error');

      setCleanupStats(data.counts);
      setOrphanedData(data.orphanedData);

      addCleanupLog(`📊 Found ${data.counts.totalOrphaned} total orphaned items.`, data.counts.totalOrphaned > 0 ? 'warning' : 'success');
      
      const counts = data.counts;
      if (counts.objectiveAttempts > 0) addCleanupLog(`   - Objective Attempts: ${counts.objectiveAttempts}`, 'error');
      if (counts.objectiveReviews > 0) addCleanupLog(`   - Objective Reviews: ${counts.objectiveReviews}`, 'error');
      if (counts.objectiveAssignments > 0) addCleanupLog(`   - Objective Assignments: ${counts.objectiveAssignments}`, 'error');
      if (counts.subjectiveAttempts > 0) addCleanupLog(`   - Subjective Attempts: ${counts.subjectiveAttempts}`, 'error');
      if (counts.subjectiveReviews > 0) addCleanupLog(`   - Subjective Reviews: ${counts.subjectiveReviews}`, 'error');
      if (counts.subjectiveAssignments > 0) addCleanupLog(`   - Subjective Assignments: ${counts.subjectiveAssignments}`, 'error');
      if (counts.peerAssignments > 0) addCleanupLog(`   - Peer Assignments: ${counts.peerAssignments}`, 'error');
      if (counts.evaluations > 0) addCleanupLog(`   - Evaluations: ${counts.evaluations}`, 'error');
      if (counts.liveSessions > 0) addCleanupLog(`   - Live Proctoring Sessions: ${counts.liveSessions}`, 'error');
      if (counts.masteryRecordsToClearLink > 0) addCleanupLog(`   - Stale Exam Mastery Links: ${counts.masteryRecordsToClearLink}`, 'error');
      if (counts.orphanedProfiles > 0) addCleanupLog(`   - Stale Student Cache Profiles: ${counts.orphanedProfiles}`, 'error');

      if (data.counts.totalOrphaned > 0) {
        addCleanupLog('\n⚠️ Orphaned items found. Click "Clean Up All" to process.', 'warning');
      } else {
        addCleanupLog('\n✅ No orphaned items found!', 'success');
      }
    } catch (err: any) {
      addCleanupLog(`❌ Scan failed: ${err.message}`, 'error');
    } finally {
      setScanning(false);
    }
  };

  const handleCleanupAll = async () => {
    if (!firebaseUser || !orphanedData) return;
    const total = cleanupStats.totalOrphaned;
    if (total === 0 || total === '-') return;

    if (!confirm(`⚠️ Clean up ${total} orphaned items across all collections?\n\nThis will delete broken attempts, reviews, assignments, evaluations, and live proctor sessions, and clear stale exam links on mastery records.\n\nThis cannot be undone!`)) return;

    setCleaning(true);
    addCleanupLog('🧹 Cleaning up all orphaned references...', 'warning');

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/cleanup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'cleanup',
          payload: orphanedData
        })
      });

      if (!res.ok) throw new Error('Cleanup request failed.');
      const data = await res.json();
      if (!data.success) throw new Error(data.error || 'Unknown error');

      addCleanupLog(`✅ ${data.message}`, 'success');
      setOrphanedData(null);
      setCleanupStats((prev: any) => ({ ...prev, totalOrphaned: 0 }));
    } catch (err: any) {
      addCleanupLog(`❌ Cleanup failed: ${err.message}`, 'error');
    } finally {
      setCleaning(false);
    }
  };

  const handleFixSubjectiveRefs = async () => {
    if (!firebaseUser) return;
    setFixing(true);
    addCleanupLog('🔧 Fixing subjective exam references...', 'warning');

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/cleanup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'fixSubjectiveRefs'
        })
      });

      if (!res.ok) throw new Error('Repair request failed.');
      const data = await res.json();
      if (!data.success) throw new Error(data.error || 'Unknown error');

      addCleanupLog(`✅ ${data.message}`, 'success');
    } catch (err: any) {
      addCleanupLog(`❌ Repair failed: ${err.message}`, 'error');
    } finally {
      setFixing(false);
    }
  };



  const handleUpdatePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newPassword) {
      alert('Please enter a new password.');
      return;
    }
    if (newPassword !== confirmPassword) {
      alert('Passwords do not match.');
      return;
    }
    if (newPassword.length < 6) {
      alert('Password must be at least 6 characters.');
      return;
    }

    setPasswordUpdating(true);
    try {
      if (auth.currentUser) {
        await updatePassword(auth.currentUser, newPassword);
        alert('✅ Password updated successfully!');
        setNewPassword('');
        setConfirmPassword('');
      } else {
        throw new Error('No user is currently logged in.');
      }
    } catch (err: any) {
      console.error(err);
      if (err.code === 'auth/requires-recent-login') {
        alert('🔒 For security reasons, please log out and log back in, then try changing your password again.');
      } else {
        alert(`❌ Failed to update password: ${err.message}`);
      }
    } finally {
      setPasswordUpdating(false);
    }
  };

  // Backups download flow
  const handleDownloadBackup = async () => {
    setProcessing(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/settings', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (!res.ok) throw new Error('Backup request failed.');
      const data = await res.json();
      
      // Save local file download stream
      const jsonStr = JSON.stringify(data.backup, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `LOS_Backup_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      alert('✅ Database backup downloaded successfully.');
    } catch (err: any) {
      alert(`❌ Backup failed: ${err.message}`);
    } finally {
      setProcessing(false);
    }
  };

  // Restore parsing upload flow
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const parsed = JSON.parse(event.target?.result as string);
        setRestoreJson(parsed);
      } catch (err) {
        alert('❌ Invalid JSON backup file.');
        setRestoreJson(null);
      }
    };
    reader.readAsText(file);
  };

  const handleRestoreBackup = async () => {
    if (!restoreJson) return;
    if (!confirm('⚠️ Are you sure you want to restore the database from this backup? This merges or overwrites matching collections.')) return;

    setProcessing(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'restore',
          backupPayload: restoreJson
        })
      });
      if (!res.ok) throw new Error('Restore request failed.');
      alert('✅ Database successfully restored.');
      setRestoreJson(null);
    } catch (err: any) {
      alert(`❌ Restore failed: ${err.message}`);
    } finally {
      setProcessing(false);
    }
  };

  // Utility resets
  const handleRunUtility = async (utilityType: 'resetFlags' | 'systemReset' | 'purgeOrphans') => {
    const confirmMessages = {
      resetFlags: 'Reset all question usage count logs & flags in the Question Bank?',
      systemReset: '⚠️ DANGER: Purge all exam attempts, proctor reviews, and integrity scorecard records to begin a fresh academic session?',
      purgeOrphans: 'Purge orphaned questions not associated with any active subject syllabus?'
    };

    if (!confirm(confirmMessages[utilityType])) return;

    setProcessing(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'utility',
          utilityType
        })
      });
      if (!res.ok) throw new Error('Utility request failed.');
      alert('✅ Database utility completed successfully.');
    } catch (err: any) {
      alert(`❌ Utility execution failed: ${err.message}`);
    } finally {
      setProcessing(false);
    }
  };

  const handleHarmonizeQuestions = async (apply: boolean) => {
    if (apply && !confirm('⚡ Are you sure you want to run the Question Bank SSOT Harmonizer? This will update legacy subject codes (e.g. GANI -> MGP1), standardize document IDs, fix KaTeX formatting, and normalize question types.')) return;

    setHarmonizing(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/questions/harmonize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({ mode: apply ? 'apply' : 'dry_run' })
      });
      if (!res.ok) throw new Error('Harmonization request failed.');
      const data = await res.json();
      setHarmonizeResult(data);
      if (apply) {
        alert(`✅ Question Bank Harmonization Complete!\n• Scanned: ${data.stats.totalScanned}\n• Subject Codes Updated: ${data.stats.migratedSubjectCodes}\n• Doc IDs Migrated: ${data.stats.migratedDocIds}\n• Math Formatted: ${data.stats.mathFormatted}`);
      }
    } catch (err: any) {
      alert(`❌ Harmonization failed: ${err.message}`);
    } finally {
      setHarmonizing(false);
    }
  };

  const handleResetProtected = async () => {
    const selected = Object.keys(selectedProtected).filter(k => selectedProtected[k]);
    if (selected.length === 0) return;

    if (!confirm(`⚠️ WARNING: Are you sure you want to permanently delete the selected protected collections: ${selected.join(', ')}? This will delete all core configurations.`)) return;

    setProcessing(true);
    try {
      const idToken = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          action: 'utility',
          utilityType: 'resetProtected',
          selectedCollections: selected
        })
      });
      if (!res.ok) throw new Error('Reset request failed.');
      alert('✅ Selected protected collections successfully cleared.');
      setSelectedProtected({
        syllabus: false,
        users: false,
        templates: false,
        config: false,
        batches: false
      });
    } catch (err: any) {
      alert(`❌ Reset failed: ${err.message}`);
    } finally {
      setProcessing(false);
    }
  };

  // Launch browser printing preview
  const handlePrintExam = (examId: string) => {
    window.open(`/student/take-subjective-exam?examId=${examId}&print=true`, '_blank');
  };



  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', background: 'var(--bg)' }}>
        <div className="loading" style={{ display: 'block' }}>
          <div className="spinner"></div> Loading system configurations...
        </div>
      </div>
    );
  }

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <header className="page-header glass" style={{ padding: '8px 12px', borderBottom: '1px solid var(--border-light)' }}>
        <div className="page-header-left">
          <span className="brand" style={{ fontSize: '18px', fontWeight: 800 }}>⚙️ YASHCOM</span>
          <div>
            <h1 style={{ fontSize: '16px', margin: 0 }}>System Settings</h1>
            <div className="subtitle hide-mobile" style={{ fontSize: '11px', color: 'var(--text-muted)' }}>Purge database orphans, download JSON backups, and change system password</div>
          </div>
        </div>
        <div className="page-header-right" style={{ display: 'flex', gap: '10px' }}>
          
          <button className="btn btn-secondary" title="Logout" onClick={logout}>🚪</button>
        </div>
      </header>

      {/* Main Workspace */}
      <main style={{ flex: 1, padding: '24px 12px', maxWidth: '850px', width: '100%', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        
        {/* Navigation Tabs */}
        <div className="test-type-tabs" style={{ display: 'flex', gap: '4px', borderBottom: '1px solid var(--border-light)', paddingBottom: '8px' }}>
          <button className={`btn btn-sm ${activeTab === 'password' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setActiveTab('password')}>🔒 Change Password</button>
          <button className={`btn btn-sm ${activeTab === 'backup' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setActiveTab('backup')}>💾 JSON Backup & Restore</button>
          <button className={`btn btn-sm ${activeTab === 'utils' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setActiveTab('utils')}>🛠️ Database Utilities</button>
          <button className={`btn btn-sm ${activeTab === 'cleanup' ? 'btn-primary' : 'btn-secondary'}`} onClick={() => setActiveTab('cleanup')}>🧹 Cleanup Database</button>
        </div>

        {/* Tab content 1: Change Password */}
        {activeTab === 'password' && (
          <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
            <h3 style={{ fontSize: '14px', fontWeight: 800, margin: '0 0 4px', color: 'var(--accent)' }}>🔒 Change System Password</h3>
            <p style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '16px' }}>Update the password for the admin account: **a@c.com**.</p>
            
            <form onSubmit={handleUpdatePassword} style={{ display: 'flex', flexDirection: 'column', gap: '12px', maxWidth: '400px' }}>
              <div className="form-group">
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '4px' }}>New Password:</label>
                <input 
                  type="password" 
                  className="form-input" 
                  placeholder="Enter new password"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  style={{ width: '100%', fontSize: '12px' }}
                />
              </div>

              <div className="form-group">
                <label style={{ display: 'block', fontSize: '11px', fontWeight: 700, color: 'var(--text-muted)', marginBottom: '4px' }}>Confirm New Password:</label>
                <input 
                  type="password" 
                  className="form-input" 
                  placeholder="Confirm new password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  style={{ width: '100%', fontSize: '12px' }}
                />
              </div>

              <button 
                type="submit" 
                className="btn btn-primary" 
                disabled={passwordUpdating}
                style={{ width: 'fit-content', marginTop: '6px' }}
              >
                {passwordUpdating ? 'Updating password...' : 'Update Password'}
              </button>
            </form>
          </div>
        )}



        {/* Tab content 2: JSON Backup */}
        {activeTab === 'backup' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {/* Download Backup */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
              <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px' }}>📥 Download local database backup</h3>
              <p style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '12px' }}>Downloads all course batches, student accounts, and questions into a single structured JSON stream file.</p>
              <button className="btn btn-primary" onClick={handleDownloadBackup} disabled={processing}>
                {processing ? 'Downloading backup stream...' : 'Download JSON Backup'}
              </button>
            </div>

            {/* Upload Restore */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)' }}>
              <h3 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px' }}>📤 Restore database from backup</h3>
              <p style={{ fontSize: '11px', color: 'var(--text-muted)', marginBottom: '12px' }}>Restores collections from a previously saved JSON file.</p>
              <input type="file" accept=".json" onChange={handleFileChange} style={{ fontSize: '12px', marginBottom: '12px', display: 'block' }} />
              
              <button 
                className="btn btn-secondary" 
                onClick={handleRestoreBackup} 
                disabled={!restoreJson || processing}
                style={{ background: restoreJson ? 'var(--success)' : '#ccc', color: '#fff', border: 'none' }}
              >
                Restore Selected JSON File
              </button>
            </div>
          </div>
        )}

        {/* Tab content 3: Database Utilities */}
        {activeTab === 'utils' && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '16px' }}>
            {/* ⚡ SSOT Question Bank Harmonizer */}
            <div className="card" style={{ background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.08) 100%)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1.5px solid rgba(168, 85, 247, 0.3)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '12px' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                  <h4 style={{ fontSize: '13px', fontWeight: 800, margin: 0, color: '#a855f7' }}>⚡ Question Bank SSOT Harmonizer</h4>
                  <span style={{ fontSize: '10px', background: '#a855f7', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontWeight: 800 }}>SSOT</span>
                </div>
                <p style={{ fontSize: '11px', color: 'var(--text-muted)', lineHeight: 1.4, margin: '0 0 10px' }}>
                  Standardizes legacy subject codes (e.g. <code>GANI</code> &rarr; <code>MGP1</code>), aligns Firestore document IDs to canonical <code>questionCode</code>, fixes KaTeX math delimiters, and verifies syllabus topic mapping.
                </p>
                {harmonizeResult && (
                  <div style={{ background: 'var(--bg-soft)', padding: '8px 12px', borderRadius: '8px', fontSize: '11px', marginBottom: '10px', border: '1px solid var(--border-light)' }}>
                    <strong>Scan Results ({harmonizeResult.mode}):</strong>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '4px', marginTop: '4px', fontSize: '10px' }}>
                      <span>• Scanned: <strong>{harmonizeResult.stats.totalScanned}</strong></span>
                      <span>• Subject Codes: <strong>{harmonizeResult.stats.migratedSubjectCodes}</strong></span>
                      <span>• Doc IDs to Align: <strong>{harmonizeResult.stats.migratedDocIds}</strong></span>
                      <span>• KaTeX Math Fixed: <strong>{harmonizeResult.stats.mathFormatted}</strong></span>
                    </div>
                  </div>
                )}
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button 
                  className="btn btn-secondary btn-sm" 
                  onClick={() => handleHarmonizeQuestions(false)} 
                  disabled={harmonizing}
                  style={{ flex: 1, fontSize: '11px' }}
                >
                  {harmonizing ? 'Scanning...' : '🔍 Dry Run Scan'}
                </button>
                <button 
                  className="btn btn-primary btn-sm" 
                  onClick={() => handleHarmonizeQuestions(true)} 
                  disabled={harmonizing}
                  style={{ flex: 1, fontSize: '11px', background: 'linear-gradient(135deg, #a855f7, #6366f1)', border: 'none' }}
                >
                  {harmonizing ? 'Harmonizing...' : '⚡ Apply SSOT Upgrade'}
                </button>
              </div>
            </div>

            {/* Reset Counter Flags */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
              <div>
                <h4 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px', color: 'var(--accent)' }}>🧹 Reset usage counters</h4>
                <p style={{ fontSize: '11px', color: 'var(--text-muted)', lineHeight: 1.4 }}>Resets usedCount flags across all questions, restoring active repetitions logs to 0.</p>
              </div>
              <button className="btn btn-secondary btn-sm" onClick={() => handleRunUtility('resetFlags')} disabled={processing}>Execute Reset</button>
            </div>

            {/* Purge Orphans */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
              <div>
                <h4 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px', color: 'var(--accent)' }}>🗑️ Purge orphaned questions</h4>
                <p style={{ fontSize: '11px', color: 'var(--text-muted)', lineHeight: 1.4 }}>Searches and deletes question bank entries not assigned to active chapter syllabi.</p>
              </div>
              <button className="btn btn-secondary btn-sm" onClick={() => handleRunUtility('purgeOrphans')} disabled={processing}>Execute Purge</button>
            </div>

            {/* DANGER: Session System Reset */}
            <div className="card" style={{ background: '#fef2f2', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid #fee2e2', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
              <div>
                <h4 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px', color: 'var(--danger)' }}>🚨 New academic session reset</h4>
                <p style={{ fontSize: '11px', color: '#b91c1c', lineHeight: 1.4 }}>DANGER: Instantly purges all past proctor logs, student scores histories, and exam attempt sheets to prepare for a fresh term.</p>
              </div>
              <button className="btn btn-primary btn-sm" style={{ background: 'var(--danger)', border: 'none' }} onClick={() => handleRunUtility('systemReset')} disabled={processing}>DANGER: Reset Database</button>
            </div>

            {/* Reset Protected Collections Card */}
            <div className="card" style={{ background: '#fffbeb', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid #fef3c7', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
              <div>
                <h4 style={{ fontSize: '13px', fontWeight: 800, margin: '0 0 4px', color: '#d97706' }}>⚠️ Reset protected tables</h4>
                <p style={{ fontSize: '11px', color: '#b45309', lineHeight: 1.4, marginBottom: '8px' }}>
                  Select which protected database tables you want to clear:
                </p>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px 12px' }}>
                  {Object.keys(selectedProtected).map((col) => (
                    <label key={col} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '11px', cursor: 'pointer', color: '#78350f', fontWeight: 600 }}>
                      <input
                        type="checkbox"
                        checked={selectedProtected[col]}
                        onChange={(e) => setSelectedProtected({ ...selectedProtected, [col]: e.target.checked })}
                      />
                      <span>{col.toUpperCase()}</span>
                    </label>
                  ))}
                </div>
              </div>
              <button 
                className="btn btn-secondary" 
                style={{ background: '#f59e0b', color: '#fff', border: 'none', fontSize: '11px', padding: '6px 12px' }}
                onClick={handleResetProtected}
                disabled={processing || !Object.values(selectedProtected).some(Boolean)}
              >
                Reset Selected
              </button>
            </div>
          </div>
        )}

        {activeTab === 'cleanup' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {/* Stats Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '12px' }}>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{cleanupStats.objectiveExams}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Objective Exams</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{cleanupStats.subjectiveExams}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Subjective Exams</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800, color: cleanupStats.totalOrphaned > 0 ? 'var(--danger)' : 'var(--text)' }}>{cleanupStats.totalOrphaned}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Total Orphaned</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{cleanupStats.objectiveAttempts + cleanupStats.subjectiveAttempts}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Orphaned Attempts</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{cleanupStats.objectiveReviews + cleanupStats.subjectiveReviews}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Orphaned Reviews</div>
              </div>
              <div className="card" style={{ background: 'var(--surface)', padding: '16px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', textAlign: 'center' }}>
                <div style={{ fontSize: '20px', fontWeight: 800 }}>{cleanupStats.masteryRecordsToClearLink}</div>
                <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px' }}>Stale Mastery Links</div>
              </div>
            </div>

            {/* Actions Panel */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexWrap: 'wrap', gap: '12px' }}>
              <button 
                className="btn btn-primary" 
                onClick={handleFindOrphaned} 
                disabled={scanning || cleaning || fixing}
                style={{ flex: '1', minWidth: '160px' }}
              >
                {scanning ? '🔍 Scanning...' : '🔍 Find All Orphaned'}
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={handleCleanupAll} 
                disabled={scanning || cleaning || fixing || !orphanedData || cleanupStats.totalOrphaned === 0 || cleanupStats.totalOrphaned === '-'}
                style={{ flex: '1', minWidth: '160px', background: orphanedData && cleanupStats.totalOrphaned > 0 ? 'var(--danger)' : undefined, color: orphanedData && cleanupStats.totalOrphaned > 0 ? '#fff' : undefined }}
              >
                {cleaning ? '🧹 Cleaning...' : '🧹 Clean Up All'}
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={handleFixSubjectiveRefs} 
                disabled={scanning || cleaning || fixing}
                style={{ flex: '1', minWidth: '160px' }}
              >
                {fixing ? '🔧 Fixing...' : '🔧 Fix Subjective Refs'}
              </button>
            </div>

            {/* Log Panel */}
            <div className="card" style={{ background: 'var(--surface)', padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <h4 style={{ fontSize: '13px', fontWeight: 800, margin: '0', color: 'var(--accent)' }}>📋 Console Logs</h4>
              <div 
                style={{ 
                  background: '#1e1e1e', 
                  color: '#fff', 
                  padding: '12px', 
                  borderRadius: 'var(--radius-md)', 
                  fontFamily: 'monospace', 
                  fontSize: '11px', 
                  lineHeight: '1.6', 
                  maxHeight: '320px', 
                  overflowY: 'auto',
                  whiteSpace: 'pre-wrap',
                  wordBreak: 'break-word'
                }}
              >
                {cleanupLogs.length === 0 ? (
                  <span style={{ color: '#888' }}>Ready to start. Click "Find All Orphaned" to begin scanning.</span>
                ) : (
                  cleanupLogs.map((log, index) => {
                    let color = '#fff';
                    if (log.includes('❌') || log.includes('Failed') || log.includes('error')) color = '#f87171';
                    else if (log.includes('✅') || log.includes('Success') || log.includes('cleaned')) color = '#4ade80';
                    else if (log.includes('⚠️') || log.includes('warning') || log.includes('Finding') || log.includes('Scanning')) color = '#fbbf24';
                    return (
                      <div key={index} style={{ color }}>{log}</div>
                    );
                  })
                )}
              </div>
            </div>
          </div>
        )}

      </main>
    </div>
  );
}
