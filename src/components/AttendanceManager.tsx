'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter, useSearchParams } from 'next/navigation';
import useSWR from 'swr';
import { fetchWithToken } from '@/lib/swrFetcher';
import { formatDateDMY as formatDateStr, getDateKeyIST } from '@/lib/dateUtils';

interface AttendanceManagerProps {
  role: 'student' | 'parent';
}

export default function AttendanceManager({ role }: AttendanceManagerProps) {
  const { firebaseUser, user, logout } = useAuth();
  const { toggleTheme } = useTheme();
  const router = useRouter();
  const searchParams = useSearchParams();

  const todayStr = getDateKeyIST();
  const getTomorrowStr = () => {
    const today = new Date(todayStr);
    today.setDate(today.getDate() + 1);
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  };
  const tomorrowStr = getTomorrowStr();

  // Resolve parent-specific children
  const parentCodes = (user as any)?.studentCodes || ((user as any)?.studentCode ? [(user as any)?.studentCode] : []);
  const defaultCode = searchParams.get('studentCode') || parentCodes[0] || '';
  const [selectedChildCode, setSelectedChildCode] = useState(defaultCode);

  useEffect(() => {
    if (defaultCode && defaultCode !== selectedChildCode) {
      setSelectedChildCode(defaultCode);
    }
  }, [defaultCode]);

  const fetcher = async (url: string) => {
    return fetchWithToken(url, firebaseUser);
  };

  // SWR for parent children name mapping
  const { data: parentDashboardData } = useSWR<any>(
    firebaseUser && role === 'parent' ? '/api/parent/dashboard' : null,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );
  const childrenList = parentDashboardData?.children || [];

  // Auto-select first child if not selected
  useEffect(() => {
    if (!selectedChildCode && childrenList.length > 0) {
      setSelectedChildCode(childrenList[0].studentCode);
    }
  }, [childrenList, selectedChildCode]);

  // Map studentCode -> name
  const childNameMap: Record<string, string> = {};
  childrenList.forEach((c: any) => {
    if (c.studentCode) {
      childNameMap[c.studentCode.toUpperCase()] = c.name || c.studentCode;
    }
  });

  const getChildName = (code: string) => {
    const upper = String(code).trim().toUpperCase();
    return childNameMap[upper] || upper;
  };

  const resolvedChildren = childrenList.length > 0 
    ? childrenList 
    : parentCodes.map((code: string) => ({ studentCode: code, name: getChildName(code) }));

  // Determine current active target student info
  const activeStudentCode = role === 'student' ? '' : selectedChildCode;
  const displayName = role === 'student' 
    ? (user?.name || 'Student')
    : getChildName(selectedChildCode);

  // SWR for attendance stats and logs
  const attendanceUrl = firebaseUser 
    ? (role === 'student' 
        ? '/api/student/attendance' 
        : `/api/student/attendance?studentCode=${selectedChildCode}`)
    : null;

  const { data: attendanceData, error: attendanceError, isLoading: attendanceLoading, mutate: mutateAttendance } = useSWR<any>(
    attendanceUrl,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );

  const stats = attendanceData?.stats || { totalDays: 0, presentDays: 0, absentDays: 0, leaveDays: 0, lateDays: 0, halfDays: 0, attendanceRate: 100 };
  const dailyLogs = attendanceData?.dailyLogs || [];
  const isCurrentlyOnLeaveToday = !!attendanceData?.isCurrentlyOnLeaveToday;

  // Voluntary check-in card states
  const [submittingVoluntary, setSubmittingVoluntary] = useState(false);
  const [voluntaryStatus, setVoluntaryStatus] = useState<'present' | 'half_day' | 'leave'>('present');
  const [voluntaryRemarks, setVoluntaryRemarks] = useState('');
  const [voluntaryError, setVoluntaryError] = useState('');
  const [voluntarySuccess, setVoluntarySuccess] = useState('');

  // Leave declaration state variables
  const [leaveDurationType, setLeaveDurationType] = useState<'single' | 'multiple'>('single');
  const [declStart, setDeclStart] = useState(tomorrowStr);
  const [declEnd, setDeclEnd] = useState(tomorrowStr);
  const [declRemarks, setDeclRemarks] = useState('');
  const [submittingDecl, setSubmittingDecl] = useState(false);
  const [declError, setDeclError] = useState('');
  const [declSuccess, setDeclSuccess] = useState('');

  // Reset voluntary statuses on child change
  useEffect(() => {
    setVoluntaryError('');
    setVoluntarySuccess('');
    setVoluntaryRemarks('');
  }, [selectedChildCode]);

  const handleMarkVoluntary = async () => {
    if (!firebaseUser) return;
    if (role === 'parent' && !selectedChildCode) return;

    setSubmittingVoluntary(true);
    setVoluntaryError('');
    setVoluntarySuccess('');
    try {
      const token = await firebaseUser.getIdToken();
      const postUrl = role === 'student' 
        ? '/api/student/attendance' 
        : `/api/student/attendance?studentCode=${selectedChildCode}`;

      const res = await fetch(postUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ 
          studentCode: selectedChildCode || undefined,
          status: voluntaryStatus, 
          remarks: voluntaryRemarks 
        })
      });
      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to submit attendance.');
      
      setVoluntarySuccess(`Voluntary attendance for ${displayName} has been marked successfully for today.`);
      mutateAttendance();
    } catch (e: any) {
      setVoluntaryError(e.message || 'An error occurred.');
    } finally {
      setSubmittingVoluntary(false);
    }
  };

  // Multi-day declaration states declared below todayStr

  // Fetch declarations via SWR
  const declUrl = firebaseUser
    ? (role === 'student' 
        ? '/api/student/attendance/declare' 
        : `/api/student/attendance/declare?studentCode=${selectedChildCode}`)
    : null;

  const { data: declData, mutate: mutateDecls } = useSWR<any>(
    declUrl,
    fetcher,
    { revalidateOnFocus: false, dedupingInterval: 60000 }
  );
  const declarations = declData?.declarations || [];

  // Reset declaration statuses on child change
  useEffect(() => {
    setDeclError('');
    setDeclSuccess('');
    setDeclStart(tomorrowStr);
    setDeclEnd(tomorrowStr);
    setDeclRemarks('');
    setLeaveDurationType('single');
  }, [selectedChildCode]);

  const handleCreateDeclaration = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!firebaseUser) return;
    if (role === 'parent' && !selectedChildCode) return;
    if (!declStart || !declEnd) {
      setDeclError('Please select both start and end dates.');
      return;
    }
    setSubmittingDecl(true);
    setDeclError('');
    setDeclSuccess('');
    try {
      const token = await firebaseUser.getIdToken();
      const postUrl = role === 'student' 
        ? '/api/student/attendance/declare' 
        : `/api/student/attendance/declare?studentCode=${selectedChildCode}`;

      const payload = { 
        studentCode: selectedChildCode || undefined, 
        status: 'leave', 
        startDate: declStart, 
        endDate: declEnd, 
        remarks: declRemarks 
      };

      const res = await fetch(postUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify(payload)
      });
      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to submit declaration.');
      
      const successMsg = `✅ Excused Leave Registered: excusing dates ${declStart} to ${declEnd} successfully.`;
      setDeclSuccess(successMsg);
      alert('✅ Leave Applied Successfully!');
      
      setDeclStart(tomorrowStr);
      setDeclEnd(tomorrowStr);
      setDeclRemarks('');
      setLeaveDurationType('single');
      mutateDecls();
      mutateAttendance();
    } catch (err: any) {
      setDeclError(err.message || 'An error occurred.');
    } finally {
      setSubmittingDecl(false);
    }
  };

  const handleDeleteDeclaration = async (declarationId: string) => {
    if (!firebaseUser) return;
    if (!confirm('Are you sure you want to cancel/delete this leave declaration? This will also remove the associated leave request.')) {
      return;
    }
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch(`/api/student/attendance/declare?id=${declarationId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const resData = await res.json();
      if (!res.ok) throw new Error(resData.error || 'Failed to delete declaration.');
      alert('🗑️ Leave declaration cancelled successfully!');
      mutateDecls();
      mutateAttendance();
    } catch (err: any) {
      alert(`Error cancelling leave: ${err.message}`);
    }
  };

  const todayLog = dailyLogs.find((log: any) => log.date === todayStr);

  // Calendar monthly states
  const [currentMonth, setCurrentMonth] = useState(new Date(todayStr).getMonth());
  const [currentYear, setCurrentYear] = useState(new Date(todayStr).getFullYear());
  const [selectedDate, setSelectedDate] = useState<string | null>(todayStr);

  return (
    <div style={{ background: 'var(--bg)', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>

      <div style={{ flex: 1, padding: '24px 12px 120px', overflowY: 'auto' }}>
        <div style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>

        {/* Child Selector for Parents */}
        {role === 'parent' && resolvedChildren.length > 1 && (
          <div className="card" style={{ padding: '12px 16px', background: 'var(--surface)', display: 'flex', alignItems: 'center', gap: '12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius)' }}>
            <span style={{ fontSize: '12px', fontWeight: 'bold' }}>Select Student:</span>
            <select
              value={selectedChildCode}
              onChange={(e) => setSelectedChildCode(e.target.value)}
              style={{ padding: '6px 12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12px', fontWeight: 600 }}
            >
              {resolvedChildren.map((c: any) => {
                const code = c.studentCode;
                const childName = c.name || getChildName(code);
                return (
                  <option key={code} value={code}>{childName}</option>
                );
              })}
            </select>
          </div>
        )}

        {/* Unified Attendance Check-In & Leave Declaration Card */}
        <div className="card" style={{ background: 'var(--surface)', padding: '20px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', display: 'flex', flexDirection: 'column', gap: '20px' }}>
          
          {/* Section 1: Today's Daily Check-In */}
          <div>
            <h3 style={{ margin: '0 0 10px 0', fontSize: '14px', fontWeight: 'bold' }}>✍️ Today's Daily Check-In for {displayName} ({formatDateStr(todayStr)})</h3>
            
            {isCurrentlyOnLeaveToday ? (
              <div style={{ padding: '12px', background: '#f3f4f6', border: '1px solid #d1d5db', color: '#374151', borderRadius: '6px', fontSize: '13px' }}>
                🌴 <strong>{displayName} is on approved leave today.</strong> No daily check-in is required.
              </div>
            ) : todayLog && todayLog.selfMarked ? (
              <div style={{ padding: '12px', background: '#ecfdf5', border: '1px solid #10b981', color: '#065f46', borderRadius: '6px', fontSize: '13px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ color: '#10b981', fontSize: '16px', fontWeight: 'bold' }}>✓</span> {role === 'student' ? 'You' : 'Parent/Student'} voluntarily marked today's attendance as <strong>{todayLog.status.toUpperCase()}</strong>. This submission is now locked.
              </div>
            ) : todayLog && todayLog.status !== 'not_marked' ? (
              <div style={{ padding: '12px', background: 'var(--accent-soft)', border: '1px solid var(--accent-ring)', color: 'var(--accent)', borderRadius: '6px', fontSize: '13px' }}>
                Verified Attendance marked by Teacher today: <strong>{todayLog.status.toUpperCase()}</strong>.
              </div>
            ) : (
              <div>
                {voluntaryError && <div className="alert-box alert-box-danger" style={{ marginBottom: '12px', padding: '10px' }}>{voluntaryError}</div>}
                {voluntarySuccess && <div className="alert-box alert-box-success" style={{ marginBottom: '12px', padding: '10px' }}>{voluntarySuccess}</div>}

                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px', alignItems: 'center' }}>
                  <div style={{ display: 'flex', gap: '6px' }}>
                    <button 
                      type="button"
                      onClick={() => setVoluntaryStatus('present')}
                      className={`btn ${voluntaryStatus === 'present' ? 'btn-primary' : 'btn-secondary'}`}
                      style={{ fontSize: '12px', padding: '6px 12px' }}
                    >
                      Present
                    </button>
                    <button 
                      type="button"
                      onClick={() => setVoluntaryStatus('half_day')}
                      className={`btn ${voluntaryStatus === 'half_day' ? 'btn-primary' : 'btn-secondary'}`}
                      style={{ fontSize: '12px', padding: '6px 12px' }}
                    >
                      Half Day
                    </button>
                    <button 
                      type="button"
                      onClick={() => setVoluntaryStatus('leave')}
                      className={`btn ${voluntaryStatus === 'leave' ? 'btn-primary' : 'btn-secondary'}`}
                      style={{ fontSize: '12px', padding: '6px 12px' }}
                    >
                      Absent
                    </button>
                  </div>
                  
                  <input 
                    type="text" 
                    value={voluntaryRemarks}
                    onChange={(e) => setVoluntaryRemarks(e.target.value)}
                    placeholder="Optional remarks"
                    style={{ flex: 1, minWidth: '200px', padding: '6px 12px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                  />

                  <button 
                    onClick={handleMarkVoluntary}
                    disabled={submittingVoluntary}
                    className="btn btn-primary"
                    style={{ fontSize: '12px', padding: '6px 16px', fontWeight: 'bold' }}
                  >
                    {submittingVoluntary ? 'Submitting...' : (voluntaryStatus === 'leave' ? '🙋 Report Absence Today' : '🙋 Mark Present Today')}
                  </button>
                </div>
              </div>
            )}
          </div>

          {role === 'parent' && (
            <>
              {/* Section 2: Leave Request (Future Dates) with Red Border */}
              <div style={{
                border: '2px solid #ef4444',
                borderRadius: 'var(--radius-md)',
                padding: '16px',
                background: 'rgba(239, 68, 68, 0.03)'
              }}>
                <h3 style={{ margin: '0 0 12px 0', fontSize: '14px', fontWeight: 'bold', color: '#ef4444' }}>📢 Leave Request</h3>

                {declError && <div className="alert-box alert-box-danger" style={{ marginBottom: '12px', padding: '10px' }}>{declError}</div>}
                {declSuccess && <div className="alert-box alert-box-success" style={{ marginBottom: '12px', padding: '10px' }}>{declSuccess}</div>}

                <form onSubmit={handleCreateDeclaration} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  
                  {/* Select Leave Duration Option */}
                  <div style={{ display: 'flex', gap: '20px', fontSize: '12px', marginBottom: '4px' }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', fontWeight: 600 }}>
                      <input 
                        type="radio" 
                        name="leaveDuration" 
                        value="single" 
                        checked={leaveDurationType === 'single'}
                        onChange={() => {
                          setLeaveDurationType('single');
                          setDeclStart(tomorrowStr);
                          setDeclEnd(tomorrowStr);
                        }}
                      />
                      Apply leave for tomorrow ({formatDateStr(tomorrowStr)})
                    </label>
                    <label style={{ display: 'flex', alignItems: 'center', gap: '6px', cursor: 'pointer', fontWeight: 600 }}>
                      <input 
                        type="radio" 
                        name="leaveDuration" 
                        value="multiple" 
                        checked={leaveDurationType === 'multiple'}
                        onChange={() => {
                          setLeaveDurationType('multiple');
                          setDeclStart(tomorrowStr);
                          setDeclEnd(tomorrowStr);
                        }}
                      />
                      Multiple Days
                    </label>
                  </div>

                  {leaveDurationType === 'multiple' && (
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '16px', alignItems: 'center', padding: '6px 0' }}>
                      {/* Start Date */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span style={{ fontSize: '12px', fontWeight: 600 }}>Start Date:</span>
                        <input 
                          type="date" 
                          value={declStart}
                          min={tomorrowStr}
                          onChange={(e) => setDeclStart(e.target.value)}
                          required
                          style={{ padding: '6px 10px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                        />
                      </div>

                      {/* End Date */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span style={{ fontSize: '12px', fontWeight: 600 }}>End Date:</span>
                        <input 
                          type="date" 
                          value={declEnd}
                          min={tomorrowStr || declStart}
                          onChange={(e) => setDeclEnd(e.target.value)}
                          required
                          style={{ padding: '6px 10px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                        />
                      </div>
                    </div>
                  )}

                  <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                    <input 
                      type="text" 
                      value={declRemarks}
                      onChange={(e) => setDeclRemarks(e.target.value)}
                      placeholder="Reason / Remarks (e.g. traveling, family function)"
                      style={{ flex: 1, padding: '6px 12px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--bg-soft)', color: 'var(--text)' }}
                    />

                    <button 
                      type="submit"
                      disabled={submittingDecl}
                      className="btn btn-primary"
                      style={{ fontSize: '12px', padding: '6px 16px', fontWeight: 'bold' }}
                    >
                      {submittingDecl ? 'Submitting...' : 'Submit Leave Declaration'}
                    </button>
                  </div>
                </form>
              </div>
            </>
          )}

          {/* Declarations List */}
          {declarations.length > 0 && (
            <div style={{ marginTop: '10px', borderTop: '1px solid var(--border-light)', paddingTop: '16px' }}>
              <h4 style={{ margin: '0 0 10px 0', fontSize: '13px', fontWeight: 'bold', color: 'var(--text-muted)' }}>Submitted Leave Declarations</h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {declarations.map((decl: any) => (
                  <div key={decl.declarationId} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', borderRadius: '6px', fontSize: '12px' }}>
                    <div>
                      <span className="badge badge-warning" style={{ marginRight: '8px', fontSize: '10px' }}>
                        Excused Leave
                      </span>
                      <strong>{formatDateStr(decl.startDate)}</strong> to <strong>{formatDateStr(decl.endDate)}</strong>
                      {decl.remarks && <span style={{ color: 'var(--text-muted)', marginLeft: '8px' }}>({decl.remarks})</span>}
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <span style={{ fontSize: '10px', color: 'var(--text-faint)' }}>
                        Submitted {formatDateStr(decl.createdAt)}
                      </span>
                      <button
                        onClick={() => handleDeleteDeclaration(decl.declarationId)}
                        style={{ border: 'none', background: 'transparent', color: 'var(--danger)', cursor: 'pointer', fontSize: '1.1rem', padding: '2px' }}
                        title="Delete/Cancel Leave"
                      >
                        🗑️
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {attendanceError && <div className="alert-box alert-box-danger">Failed to load attendance logs.</div>}

        {attendanceLoading ? (
          <div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>Loading logs...</div>
        ) : (
          <>
            {/* Stats Overview: One Bento Card with 5 chips in a single line */}
            <div className="card glass" style={{ background: 'var(--surface)', padding: '18px 24px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '11px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 800, letterSpacing: '0.05em' }}>📊 Attendance Statistics Overview</span>
                <span style={{ fontSize: '11.5px', color: 'var(--text-muted)', fontWeight: 500 }}>Target: Keep aiming above 90%!</span>
              </div>
              
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '12px', justifyContent: 'space-between', alignItems: 'center' }}>
                {/* Chip 1: Attendance Rate */}
                <div style={{ flex: '1 1 150px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'var(--accent-soft)', padding: '10px 16px', borderRadius: '30px', border: '1px solid var(--accent-ring)' }}>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>Rate</span>
                  <span style={{ fontSize: '15px', fontWeight: 900, color: 'var(--accent)' }}>{stats.attendanceRate}%</span>
                </div>

                {/* Chip 2: Present Days */}
                <div style={{ flex: '1 1 150px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'rgba(16, 185, 129, 0.08)', padding: '10px 16px', borderRadius: '30px', border: '1px solid rgba(16, 185, 129, 0.25)' }}>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>Present</span>
                  <span style={{ fontSize: '15px', fontWeight: 900, color: 'var(--success)' }}>{stats.presentDays} Days</span>
                </div>

                {/* Chip 3: Absent Days */}
                <div style={{ flex: '1 1 150px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: stats.absentDays > 0 ? 'rgba(239, 68, 68, 0.08)' : 'var(--bg-soft)', padding: '10px 16px', borderRadius: '30px', border: stats.absentDays > 0 ? '1px solid rgba(239, 68, 68, 0.25)' : '1px solid var(--border-light)' }}>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>Absent</span>
                  <span style={{ fontSize: '15px', fontWeight: 900, color: stats.absentDays > 0 ? 'var(--danger)' : 'var(--text-muted)' }}>{stats.absentDays} Days</span>
                </div>

                {/* Chip 4: Half Days */}
                <div style={{ flex: '1 1 150px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'rgba(249, 115, 22, 0.08)', padding: '10px 16px', borderRadius: '30px', border: '1px solid rgba(249, 115, 22, 0.25)' }}>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>Half Days</span>
                  <span style={{ fontSize: '15px', fontWeight: 900, color: '#f97316' }}>{stats.halfDays || 0} Days</span>
                </div>

                {/* Chip 5: Leaves */}
                <div style={{ flex: '1 1 150px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', background: 'rgba(107, 114, 128, 0.08)', padding: '10px 16px', borderRadius: '30px', border: '1px solid rgba(107, 114, 128, 0.25)' }}>
                  <span style={{ fontSize: '11.5px', fontWeight: 600, color: 'var(--text-muted)' }}>Leaves</span>
                  <span style={{ fontSize: '15px', fontWeight: 900, color: 'var(--text-muted)' }}>{stats.leaveDays} Days</span>
                </div>
              </div>
            </div>

            {/* Daily History Calendar logs */}
            {(() => {
              const monthNames = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
              ];

              const getDaysInMonth = (year: number, month: number) => {
                return new Date(year, month + 1, 0).getDate();
              };

              const getFirstDayOfMonth = (year: number, month: number) => {
                return new Date(year, month, 1).getDay();
              };

              const handlePrevMonth = () => {
                if (currentMonth === 0) {
                  setCurrentMonth(11);
                  setCurrentYear(prev => prev - 1);
                } else {
                  setCurrentMonth(prev => prev - 1);
                }
              };

              const handleNextMonth = () => {
                if (currentMonth === 11) {
                  setCurrentMonth(0);
                  setCurrentYear(prev => prev + 1);
                } else {
                  setCurrentMonth(prev => prev + 1);
                }
              };

              const getDayAttendance = (dateKey: string) => {
                const logsForDay = dailyLogs.filter((log: any) => log.date === dateKey);
                if (logsForDay.length === 0) return null;
                
                if (logsForDay.some((l: any) => l.status === 'present')) return { status: 'present', logs: logsForDay };
                if (logsForDay.some((l: any) => l.status === 'late')) return { status: 'late', logs: logsForDay };
                if (logsForDay.some((l: any) => l.status === 'half_day')) return { status: 'half_day', logs: logsForDay };
                if (logsForDay.some((l: any) => l.status === 'leave')) return { status: 'leave', logs: logsForDay };
                if (logsForDay.some((l: any) => l.status === 'absent')) return { status: 'absent', logs: logsForDay };
                return { status: 'not_marked', logs: logsForDay };
              };

              const daysInMonth = getDaysInMonth(currentYear, currentMonth);
              const firstDayIndex = getFirstDayOfMonth(currentYear, currentMonth);
              const dayNumbers = Array.from({ length: daysInMonth }, (_, i) => i + 1);
              const offsetCells = Array.from({ length: firstDayIndex });
              const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

              const selectedDayLogs = selectedDate ? dailyLogs.filter((log: any) => log.date === selectedDate) : [];

              return (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                  
                  {/* Calendar Card */}
                  <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', padding: '20px' }}>
                    
                    {/* Header: Month switcher */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
                      <button 
                        onClick={handlePrevMonth}
                        className="btn btn-secondary"
                        style={{ padding: '6px 12px', fontSize: '12px' }}
                      >
                        ◀ Prev
                      </button>
                      <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, color: 'var(--accent)' }}>
                        {monthNames[currentMonth]} {currentYear}
                      </h3>
                      <button 
                        onClick={handleNextMonth}
                        className="btn btn-secondary"
                        style={{ padding: '6px 12px', fontSize: '12px' }}
                      >
                        Next ▶
                      </button>
                    </div>

                    {/* Color Legend */}
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', justifyContent: 'center', fontSize: '11px', color: 'var(--text-muted)', marginBottom: '16px', background: 'var(--bg-soft)', padding: '8px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--success)' }} /> Present
                      </span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--danger)' }} /> Absent
                      </span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--info)' }} /> Leave
                      </span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#f97316' }} /> Half Day
                      </span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#94a3b8' }} /> Not Marked
                      </span>
                    </div>

                    {/* Calendar Grid */}
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                      
                      {/* Weekday headers */}
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: '6px', textAlign: 'center', fontWeight: 'bold', fontSize: '11.5px', color: 'var(--text-muted)', borderBottom: '1px solid var(--border-light)', paddingBottom: '6px' }}>
                        {weekdays.map(d => (
                          <div key={d}>{d}</div>
                        ))}
                      </div>

                      {/* Days grid */}
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: '6px' }}>
                        {/* Start offset */}
                        {offsetCells.map((_, idx) => (
                          <div key={`offset-${idx}`} />
                        ))}

                        {/* Days of month */}
                        {dayNumbers.map(day => {
                          const monthStr = String(currentMonth + 1).padStart(2, '0');
                          const dayStr = String(day).padStart(2, '0');
                          const dateKey = `${currentYear}-${monthStr}-${dayStr}`;

                          const attendanceInfo = getDayAttendance(dateKey);
                          let cellBg = 'transparent';
                          let cellColor = 'var(--text-muted)';
                          let bulletColor = null;

                          if (attendanceInfo) {
                            if (attendanceInfo.status === 'present') {
                              cellBg = 'rgba(16, 185, 129, 0.12)';
                              cellColor = 'var(--success)';
                              bulletColor = 'var(--success)';
                            } else if (attendanceInfo.status === 'absent') {
                              cellBg = 'rgba(239, 68, 68, 0.12)';
                              cellColor = 'var(--danger)';
                              bulletColor = 'var(--danger)';
                            } else if (attendanceInfo.status === 'leave') {
                              cellBg = 'var(--accent-soft)';
                              cellColor = 'var(--info)';
                              bulletColor = 'var(--info)';
                            } else if (attendanceInfo.status === 'half_day') {
                              cellBg = 'rgba(249, 115, 22, 0.12)';
                              cellColor = '#f97316';
                              bulletColor = '#f97316';
                            } else if (attendanceInfo.status === 'late') {
                              cellBg = 'rgba(234, 179, 8, 0.12)';
                              cellColor = '#eab308';
                              bulletColor = '#eab308';
                            } else {
                              cellBg = 'rgba(148, 163, 184, 0.08)';
                              cellColor = '#94a3b8';
                              bulletColor = '#94a3b8';
                            }
                          }

                          const isSelected = selectedDate === dateKey;

                          return (
                            <button
                              key={day}
                              onClick={() => setSelectedDate(dateKey)}
                              style={{
                                aspectRatio: '1',
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: 'center',
                                justifyContent: 'center',
                                borderRadius: 'var(--radius-sm)',
                                cursor: 'pointer',
                                border: isSelected ? '2px solid var(--accent)' : '1px solid var(--border-light)',
                                background: cellBg,
                                color: cellColor,
                                fontWeight: isSelected ? '800' : '500',
                                fontSize: '13px',
                                padding: '4px',
                                outline: 'none',
                              }}
                            >
                              <span>{day}</span>
                              {bulletColor && (
                                <span style={{ width: '4px', height: '4px', borderRadius: '50%', background: bulletColor, marginTop: '2px' }} />
                              )}
                            </button>
                          );
                        })}
                      </div>

                    </div>

                  </div>

                  {/* Selected Date Details Panel */}
                  {selectedDate && (
                    <div className="card" style={{ background: 'var(--surface)', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-lg)', padding: '20px' }}>
                      <h4 style={{ margin: '0 0 14px 0', fontSize: '13.5px', fontWeight: 800, color: 'var(--text)' }}>
                        📋 Logs for {selectedDate}
                      </h4>
                      {selectedDayLogs.length === 0 ? (
                        <div style={{ color: 'var(--text-faint)', fontSize: '12px', fontStyle: 'italic' }}>
                          No daily logs recorded for this day. (Future logs or not voluntarily declared ones)
                        </div>
                      ) : (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                          {selectedDayLogs.map((log: any, idx: number) => {
                            let statusColor = '#94a3b8';
                            let statusLabel = log.status.toUpperCase();
                            if (log.status === 'present') {
                              statusColor = 'var(--success)';
                            } else if (log.status === 'absent') {
                              statusColor = 'var(--danger)';
                            } else if (log.status === 'half_day') {
                              statusColor = '#f97316';
                              statusLabel = 'HALF DAY';
                            } else if (log.status === 'late') {
                              statusColor = '#eab308';
                              statusLabel = 'LATE CHECK-IN';
                            } else if (log.status === 'leave') {
                              statusColor = 'var(--info)';
                              statusLabel = 'EXCUSED LEAVE';
                            }

                            return (
                              <div key={idx} style={{ padding: '12px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-soft)', border: '1px solid var(--border-light)', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                  <strong style={{ fontSize: '13px', color: 'var(--text)' }}>{log.batchName}</strong>
                                  <span style={{ fontSize: '9px', background: `${statusColor}15`, color: statusColor, padding: '2px 8px', borderRadius: '12px', fontWeight: 800 }}>
                                    {statusLabel}
                                  </span>
                                </div>
                                {log.selfMarked && (
                                  <div style={{ fontSize: '11px', color: 'var(--success)', fontWeight: 600 }}>
                                    ✓ Voluntarily declared
                                  </div>
                                )}
                                {log.remarks && (
                                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', fontStyle: 'italic' }}>
                                    Remarks: "{log.remarks}"
                                  </div>
                                )}
                              </div>
                            );
                          })}
                        </div>
                      )}
                    </div>
                  )}

                </div>
              );
            })()}
          </>
        )}

        </div>
      </div>
    </div>
  );
}
