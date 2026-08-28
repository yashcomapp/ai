'use client';

import React, { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { playNotificationSound } from '@/lib/audioUtils';

interface Batch {
  id: string;
  name: string;
}

interface Student {
  studentCode: string;
  name: string;
}

interface Parent {
  email: string;
  displayName: string;
  studentCodes: string[];
}

interface Notice {
  id: string;
  title: string;
  body: string;
  targetType: string;
  targetValues: string[];
  createdAt: string | null;
  createdBy: string;
  isOverlay?: boolean;
  type?: string;
}

export default function AdminNoticesPage() {
  const { firebaseUser } = useAuth();
  const { theme } = useTheme();
  const router = useRouter();

  const [loading, setLoading] = useState(true);
  const [publishing, setPublishing] = useState(false);
  const [batches, setBatches] = useState<Batch[]>([]);
  const [students, setStudents] = useState<Student[]>([]);
  const [parents, setParents] = useState<Parent[]>([]);
  const [notices, setNotices] = useState<Notice[]>([]);

  // Logs States
  const [selectedNoticeLogId, setSelectedNoticeLogId] = useState<string | null>(null);
  const [logLoading, setLogLoading] = useState(false);
  const [noticeLogData, setNoticeLogData] = useState<any | null>(null);
  const [noticeLogSort, setNoticeLogSort] = useState<'name' | 'seen_first' | 'unseen_first'>('name');

  // PDF Export Print Options States
  const [showPdfOptionsModal, setShowPdfOptionsModal] = useState(false);
  const [pdfPrintStudents, setPdfPrintStudents] = useState(true);
  const [pdfPrintParents, setPdfPrintParents] = useState(true);
  const [pdfPrintNotSeenOnly, setPdfPrintNotSeenOnly] = useState(false);

  const getSortedLogs = (list: any[]) => {
    if (!Array.isArray(list)) return [];
    return [...list].sort((a, b) => {
      if (noticeLogSort === 'seen_first') {
        if (a.seen !== b.seen) return a.seen ? -1 : 1;
      } else if (noticeLogSort === 'unseen_first') {
        if (a.seen !== b.seen) return a.seen ? 1 : -1;
      }
      const nameA = a.name || a.studentName || '';
      const nameB = b.name || b.studentName || '';
      return nameA.localeCompare(nameB);
    });
  };

  // Form States
  const [title, setTitle] = useState('');
  const [bodyText, setBodyText] = useState('');
  const [targetType, setTargetType] = useState<'all' | 'batch' | 'student' | 'parent'>('all');
  const [selectedBatchIds, setSelectedBatchIds] = useState<string[]>([]);
  const [selectedStudentCodes, setSelectedStudentCodes] = useState<string[]>([]);
  const [selectedParentEmails, setSelectedParentEmails] = useState<string[]>([]);
  const [isOverlay, setIsOverlay] = useState(true);
  const [noticeType, setNoticeType] = useState<'schedule' | 'fees' | 'general'>('general');
  const [noticeDate, setNoticeDate] = useState('');

  const applyFormat = (prefix: string, suffix: string = '') => {
    const el = document.getElementById('notice-body-textarea') as HTMLTextAreaElement | null;
    if (!el) {
      setBodyText(prev => prev + prefix + suffix);
      return;
    }
    const start = el.selectionStart;
    const end = el.selectionEnd;
    const selected = bodyText.substring(start, end);
    const replacement = selected ? `${prefix}${selected}${suffix}` : `${prefix}${suffix}`;
    const updated = bodyText.substring(0, start) + replacement + bodyText.substring(end);
    setBodyText(updated);
    setTimeout(() => {
      el.focus();
      el.setSelectionRange(start + prefix.length, start + prefix.length + selected.length);
    }, 0);
  };

  const renderNoticeHTML = (rawText: string) => {
    if (!rawText) return '';
    let html = rawText;
    // Prevent double spacing around block tags
    html = html.replace(/(<\/div>|<\/p>|<\/li>)\s*\r?\n/gi, '$1');
    html = html.replace(/\r?\n\s*(<div[^>]*>|<p[^>]*>|<ul[^>]*>|<ol[^>]*>|<li[^>]*>)/gi, '$1');
    html = html.replace(/\r?\n/g, '<br/>');
    return html;
  };

  // Maintenance / System Access States
  const [maintenanceMode, setMaintenanceMode] = useState(false);
  const [blockStudent, setBlockStudent] = useState(false);
  const [blockParent, setBlockParent] = useState(false);
  const [maintenanceMessage, setMaintenanceMessage] = useState('');
  const [maintenanceStart, setMaintenanceStart] = useState('');
  const [maintenanceEnd, setMaintenanceEnd] = useState('');
  const [savingAccess, setSavingAccess] = useState(false);

  const loadAccessConfig = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/system-access', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.config) {
          setMaintenanceMode(!!data.config.maintenanceMode);
          setBlockStudent(data.config.blockedRoles?.includes('student') || false);
          setBlockParent(data.config.blockedRoles?.includes('parent') || false);
          setMaintenanceMessage(data.config.message || '');
          if (data.config.scheduledStart) setMaintenanceStart(data.config.scheduledStart);
          if (data.config.scheduledEnd) setMaintenanceEnd(data.config.scheduledEnd);
        }
      }
    } catch (err) {
      console.error('Failed to load system access config:', err);
    }
  };

  const loadData = async () => {
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      
      // Load batches and students list from exams api
      const examsRes = await fetch('/api/admin/exams', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (examsRes.ok) {
        const examsData = await examsRes.json();
        setBatches(examsData.batches || []);
        const sorted = (examsData.students || []).sort((a: any, b: any) => (a.name || '').localeCompare(b.name || ''));
        setStudents(sorted);
        setParents(examsData.parents || []);
      }

      // Load notices history
      const noticesRes = await fetch('/api/admin/notices', {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (noticesRes.ok) {
        const noticesData = await noticesRes.json();
        setNotices(noticesData.notices || []);
      }

      // Load access config
      await loadAccessConfig();
    } catch (err) {
      console.error('Failed to load notices page data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveAccessConfig = async () => {
    if (!firebaseUser) return;
    setSavingAccess(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const blockedRoles = [];
      if (blockStudent) blockedRoles.push('student');
      if (blockParent) blockedRoles.push('parent');

      const res = await fetch('/api/admin/system-access', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          maintenanceMode,
          blockedRoles,
          message: maintenanceMessage,
          scheduledStart: maintenanceStart,
          scheduledEnd: maintenanceEnd
        })
      });

      if (res.ok) {
        alert('🛠️ System access configuration updated successfully!');
      } else {
        const errData = await res.json();
        alert(`❌ Failed to update access settings: ${errData.message || 'Unknown error'}`);
      }
    } catch (err: any) {
      alert(`❌ Error saving access settings: ${err.message}`);
    } finally {
      setSavingAccess(false);
    }
  };

  const handleDisableMaintenance = async () => {
    if (!confirm('Are you sure you want to disable Maintenance Mode? Access will be restored for all portals.')) return;
    if (!firebaseUser) return;
    setSavingAccess(true);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/system-access', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          maintenanceMode: false,
          blockedRoles: [],
          message: maintenanceMessage,
          scheduledStart: maintenanceStart,
          scheduledEnd: maintenanceEnd
        })
      });

      if (res.ok) {
        setMaintenanceMode(false);
        setBlockStudent(false);
        setBlockParent(false);
        alert('🟢 Maintenance Mode disabled successfully!');
      }
    } catch (err: any) {
      alert(`❌ Error disabling maintenance mode: ${err.message}`);
    } finally {
      setSavingAccess(false);
    }
  };

  const handleBroadcastMaintenanceSchedule = async () => {
    if (!maintenanceStart || !maintenanceEnd) {
      alert('Please select both Scheduled Start Time and End Time.');
      return;
    }
    const startDate = new Date(maintenanceStart).toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' });
    const endDate = new Date(maintenanceEnd).toLocaleString('en-IN', { dateStyle: 'medium', timeStyle: 'short' });

    if (!confirm(`Broadcast scheduled maintenance announcement from ${startDate} to ${endDate}?`)) return;
    if (!firebaseUser) return;

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/notices', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          title: '🛠️ Scheduled System Maintenance Announcement',
          body: `Please be informed that system maintenance is scheduled from ${startDate} to ${endDate}.\n\nDuring this window, student and parent portal access may be temporarily interrupted for code updates. Please complete your active tasks prior to this window.`,
          targetType: 'all',
          targetValues: [],
          type: 'schedule',
          isOverlay: true
        })
      });

      if (res.ok) {
        playNotificationSound();
        alert('📢 Maintenance Schedule Announcement published to all students & parents!');
        loadData();
      } else {
        const errData = await res.json();
        alert(`Failed to broadcast schedule notice: ${errData.message || 'Unknown error'}`);
      }
    } catch (err: any) {
      alert(`Error broadcasting notice: ${err.message}`);
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('Are you sure you want to delete this announcement? This will remove it for all roles.')) {
      return;
    }
    if (!firebaseUser) return;
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/notices?id=${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${idToken}`
        }
      });
      if (res.ok) {
        alert('Notice deleted successfully.');
        loadData();
      } else {
        const errorData = await res.json();
        alert(`Failed to delete notice: ${errorData.message || 'Unknown error'}`);
      }
    } catch (err: any) {
      alert(`Error deleting notice: ${err.message}`);
    }
  };

  useEffect(() => {
    loadData();
  }, [firebaseUser]);

  const handlePublish = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !bodyText.trim() || !firebaseUser) {
      alert('Please fill in title and body.');
      return;
    }

    setPublishing(true);

    let targetValues: string[] = [];
    if (targetType === 'batch') {
      targetValues = selectedBatchIds;
      if (targetValues.length === 0) {
        alert('Please select at least one batch.');
        setPublishing(false);
        return;
      }
    } else if (targetType === 'student') {
      targetValues = selectedStudentCodes;
      if (targetValues.length === 0) {
        alert('Please select at least one student.');
        setPublishing(false);
        return;
      }
    } else if (targetType === 'parent') {
      targetValues = selectedParentEmails;
      if (targetValues.length === 0) {
        alert('Please select at least one parent.');
        setPublishing(false);
        return;
      }
    }

    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch('/api/admin/notices', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify({
          title,
          bodyText,
          targetType,
          targetValues,
          isOverlay,
          type: noticeType,
          noticeDate: noticeType === 'schedule' ? noticeDate : null
        })
      });

      if (!res.ok) {
        throw new Error('Notice publishing endpoint failed.');
      }

      // Reset form
      setTitle('');
      setBodyText('');
      setTargetType('all');
      setSelectedBatchIds([]);
      setSelectedStudentCodes([]);
      setSelectedParentEmails([]);
      setIsOverlay(true);
      setNoticeType('general');
      setNoticeDate('');
      alert('📢 Notice published and broadcast successfully!');
      
      // Reload history
      loadData();
    } catch (err: any) {
      alert(`❌ Failed to publish notice: ${err.message}`);
    } finally {
      setPublishing(false);
    }
  };

  const handleViewLogs = async (noticeId: string) => {
    if (!firebaseUser) return;
    setSelectedNoticeLogId(noticeId);
    setLogLoading(true);
    setNoticeLogData(null);
    try {
      const idToken = await firebaseUser.getIdToken();
      const res = await fetch(`/api/admin/notices/logs?noticeId=${noticeId}`, {
        headers: { 'Authorization': `Bearer ${idToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setNoticeLogData(data);
      } else {
        alert('❌ Failed to load notice seen logs.');
      }
    } catch (err: any) {
      alert('❌ Error loading notice seen logs: ' + err.message);
    } finally {
      setLogLoading(false);
    }
  };

  const handleExportPDF = () => {
    if (!noticeLogData) return;
    const printWindow = window.open('', '_blank');
    if (!printWindow) return;

    const title = noticeLogData.title;
    const targetType = noticeLogData.targetType;
    
    let htmlContent = `
      <html>
        <head>
          <title>Notice Delivery & Seen Logs - ${title}</title>
          <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 30px; color: #222730; }
            h1 { font-size: 20px; font-weight: bold; margin-bottom: 5px; color: #171a1f; }
            h2 { font-size: 14px; color: #64748b; margin-top: 0; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 0.5px; }
            .info-box { background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 8px; margin-bottom: 25px; }
            .info-box p { margin: 4px 0; font-size: 13px; }
            .section-title { font-size: 14px; font-weight: bold; color: #334155; margin-top: 25px; margin-bottom: 10px; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 12.5px; }
            th { background: #f1f5f9; color: #475569; font-weight: 600; text-align: left; padding: 10px; border: 1px solid #cbd5e1; }
            td { padding: 10px; border: 1px solid #cbd5e1; color: #334155; }
            .status-seen { color: #16a34a; font-weight: 600; }
            .status-unseen { color: #dc2626; font-weight: 600; }
            @media print {
              body { padding: 0; }
              button { display: none; }
            }
          </style>
        </head>
        <body>
          <h1>📢 Notice Delivery & Seen Status Report</h1>
          <h2>YASHCOM Learning OS</h2>
          
          <div class="info-box">
            <p><strong>Notice Title:</strong> ${title}</p>
            <p><strong>Target Group:</strong> ${targetType.toUpperCase()}</p>
            <p><strong>Included Logs:</strong> ${[pdfPrintStudents && 'Students Log', pdfPrintParents && 'Parents Log', pdfPrintNotSeenOnly && 'Not Seen Log Only'].filter(Boolean).join(', ')}</p>
            <p><strong>Report Generated:</strong> ${new Date().toLocaleString('en-IN')}</p>
          </div>
    `;

    // 1. Add students list
    // 1. Add students list (segregated by batch with count)
    if (pdfPrintStudents) {
      htmlContent += `<div class="section-title">👥 Students Status (S)</div>`;
      const groups = noticeLogData.studentGroups;
      if (Object.keys(groups).length === 0) {
        htmlContent += `<p style="font-size: 12.5px; font-style: italic; color: #64748b;">No students targeted.</p>`;
      } else {
        Object.keys(groups).forEach(batchName => {
          let list = getSortedLogs(groups[batchName]);
          if (pdfPrintNotSeenOnly) {
            list = list.filter((s: any) => !s.seen);
          }

          if (list.length > 0) {
            htmlContent += `<h3 style="font-size: 13px; color: #4f46e5; margin-top: 15px; margin-bottom: 8px;">📦 ${batchName} (Students: ${list.length})</h3>`;
            htmlContent += `
              <table>
                <thead>
                  <tr>
                    <th style="width: 40%;">Student Name</th>
                    <th style="width: 20%;">Role</th>
                    <th style="width: 20%;">Push Status</th>
                    <th style="width: 20%;">Seen Status</th>
                  </tr>
                </thead>
                <tbody>
            `;
            list.forEach((stud: any) => {
              const pushStatus = stud.hasPushRegistered
                ? `<span style="color: #16a34a; font-weight: 600;">📲 Active</span>`
                : `<span style="color: #dc2626; font-weight: 600;">📴 Disabled</span>`;
              const seenStatus = stud.seen 
                ? `<span class="status-seen">🟢 Seen at ${new Date(stud.seenAt).toLocaleString('en-IN')}</span>` 
                : `<span class="status-unseen">❌ Not Seen yet</span>`;
              htmlContent += `
                <tr>
                  <td>${stud.autonomous ? '# ' : ''}${stud.name} (S)</td>
                  <td>Student (S)</td>
                  <td>${pushStatus}</td>
                  <td>${seenStatus}</td>
                </tr>
              `;
            });
            htmlContent += `</tbody></table>`;
          }
        });
      }
    }

    // 2. Add parents list (segregated by batch with count)
    if (pdfPrintParents && noticeLogData.parentGroups) {
      htmlContent += `<div class="section-title">👪 Parents Status (P)</div>`;
      const pGroups = noticeLogData.parentGroups;
      if (Object.keys(pGroups).length === 0) {
        htmlContent += `<p style="font-size: 12.5px; font-style: italic; color: #64748b;">No parents targeted.</p>`;
      } else {
        Object.keys(pGroups).forEach(batchName => {
          let pList = getSortedLogs(pGroups[batchName]);
          if (pdfPrintNotSeenOnly) {
            pList = pList.filter((p: any) => !p.seen);
          }

          if (pList.length > 0) {
            htmlContent += `<h3 style="font-size: 13px; color: #4f46e5; margin-top: 15px; margin-bottom: 8px;">📦 ${batchName} (Parents: ${pList.length})</h3>`;
            htmlContent += `
              <table>
                <thead>
                  <tr>
                    <th style="width: 50%;">Parent (Child Associated)</th>
                    <th style="width: 25%;">Push Status</th>
                    <th style="width: 25%;">Seen Status</th>
                  </tr>
                </thead>
                <tbody>
            `;
            pList.forEach((parent: any) => {
              const pushStatus = parent.hasPushRegistered
                ? `<span style="color: #16a34a; font-weight: 600;">📲 Active</span>`
                : `<span style="color: #dc2626; font-weight: 600;">📴 Disabled</span>`;
              const seenStatus = parent.seen 
                ? `<span class="status-seen">🟢 Seen at ${new Date(parent.seenAt).toLocaleString('en-IN')}</span>` 
                : `<span class="status-unseen">❌ Not Seen yet</span>`;
              htmlContent += `
                <tr>
                  <td>${parent.autonomous ? '# ' : ''}${parent.studentName} (P)</td>
                  <td>${pushStatus}</td>
                  <td>${seenStatus}</td>
                </tr>
              `;
            });
            htmlContent += `</tbody></table>`;
          }
        });
      }
    }

    htmlContent += `
        </body>
      </html>
    `;

    printWindow.document.write(htmlContent);
    printWindow.document.close();
    printWindow.focus();
    setTimeout(() => {
      printWindow.print();
    }, 250);
  };

  const handleBatchSelect = (batchId: string) => {
    setSelectedBatchIds(prev => 
      prev.includes(batchId) ? prev.filter(id => id !== batchId) : [...prev, batchId]
    );
  };

  const handleStudentSelect = (code: string) => {
    setSelectedStudentCodes(prev => 
      prev.includes(code) ? prev.filter(c => c !== code) : [...prev, code]
    );
  };

  const handleParentSelect = (email: string) => {
    setSelectedParentEmails(prev =>
      prev.includes(email) ? prev.filter(e => e !== email) : [...prev, email]
    );
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '80vh', color: 'var(--text)' }}>
        <h3>Loading Notice Board Manager...</h3>
      </div>
    );
  }

  return (
    <div style={{ padding: '16px 12px', maxWidth: '1200px', margin: '0 auto', color: 'var(--text)' }}>
      {/* Back to Dashboard Button on Top */}
      <div style={{ display: 'flex', justifyContent: 'flex-start', marginBottom: '12px' }}>
        <button 
          onClick={() => router.push('/admin')} 
          style={{
            background: 'none',
            border: 'none',
            color: 'var(--accent)',
            cursor: 'pointer',
            fontSize: '13px',
            fontWeight: 600,
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            padding: 0
          }}
        >
          ← Back to Dashboard
        </button>
      </div>

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
        <div>
          <h1 style={{ fontSize: '20px', fontWeight: 800, margin: 0, background: 'linear-gradient(135deg, var(--accent), #818cf8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', whiteSpace: 'nowrap' }}>
            📢 Notices & Announcements
          </h1>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px' }}>
        {/* Create Notice Form */}
        <div className="card" style={{ padding: '24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '2px solid var(--border-glass)', boxShadow: 'var(--shadow-glass)' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}>
            ✍️ Compose Notice
          </h3>
          
          <form onSubmit={handlePublish} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>Notice Title</label>
              <input 
                type="text" 
                placeholder="e.g. Test Schedule Modification" 
                value={title} 
                onChange={(e) => setTitle(e.target.value)}
                required
                style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--bg-soft)', color: 'var(--text)', outline: 'none' }}
              />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Notice Message / Body</label>
                <span style={{ fontSize: '10.5px', color: 'var(--accent)', fontWeight: 700 }}>✨ Rich Text Formatting</span>
              </div>

              {/* Rich Text Formatting Toolbar */}
              <div style={{
                display: 'flex',
                flexWrap: 'wrap',
                alignItems: 'center',
                gap: '6px',
                padding: '8px 10px',
                background: 'var(--bg-soft)',
                borderRadius: 'var(--radius-md) var(--radius-md) 0 0',
                border: '1px solid var(--border-light)',
                borderBottom: 'none'
              }}>
                {/* Font Size Selector */}
                <select
                  onChange={(e) => {
                    const size = e.target.value;
                    if (size) {
                      applyFormat(`<span style="font-size: ${size}; font-weight: ${size === '22px' ? 'bold' : 'normal'}; display: inline-block;">`, `</span>`);
                      e.target.value = '';
                    }
                  }}
                  defaultValue=""
                  style={{ padding: '3px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', outline: 'none', cursor: 'pointer' }}
                >
                  <option value="" disabled>Font Size</option>
                  <option value="12px">Small (12px)</option>
                  <option value="14px">Normal (14px)</option>
                  <option value="18px">Large (18px)</option>
                  <option value="22px">Header (22px)</option>
                </select>

                {/* Line Spacing Selector */}
                <select
                  onChange={(e) => {
                    const spacing = e.target.value;
                    if (spacing) {
                      applyFormat(`<div style="line-height: ${spacing}; margin: 0; padding: 0;">`, `</div>`);
                      e.target.value = '';
                    }
                  }}
                  defaultValue=""
                  style={{ padding: '3px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', outline: 'none', cursor: 'pointer' }}
                >
                  <option value="" disabled>Line Spacing</option>
                  <option value="1.0">Single (1.0)</option>
                  <option value="1.15">Compact (1.15)</option>
                  <option value="1.3">Normal (1.3)</option>
                  <option value="1.6">Relaxed (1.6)</option>
                </select>

                {/* Color Palette Swatches */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '3px', padding: '0 4px', borderLeft: '1px solid var(--border-light)', borderRight: '1px solid var(--border-light)' }}>
                  {[
                    { color: '#ffffff', label: 'White' },
                    { color: '#f87171', label: 'Red' },
                    { color: '#34d399', label: 'Green' },
                    { color: '#fbbf24', label: 'Yellow' },
                    { color: '#60a5fa', label: 'Blue' },
                    { color: '#c084fc', label: 'Purple' }
                  ].map(c => (
                    <button
                      key={c.color}
                      type="button"
                      title={`Color: ${c.label}`}
                      onClick={() => applyFormat(`<span style="color: ${c.color}; font-weight: bold;">`, `</span>`)}
                      style={{ width: '16px', height: '16px', borderRadius: '50%', background: c.color, border: '1px solid rgba(255,255,255,0.4)', cursor: 'pointer', flexShrink: 0 }}
                    />
                  ))}
                </div>

                {/* Alignment */}
                <button type="button" onClick={() => applyFormat('<div style="text-align: left; margin: 0; padding: 0;">', '</div>')} style={{ padding: '2px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Align Left">⬅️</button>
                <button type="button" onClick={() => applyFormat('<div style="text-align: center; margin: 0; padding: 0;">', '</div>')} style={{ padding: '2px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Align Center">↔️</button>
                <button type="button" onClick={() => applyFormat('<div style="text-align: right; margin: 0; padding: 0;">', '</div>')} style={{ padding: '2px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Align Right">➡️</button>

                {/* Text Styling */}
                <button type="button" onClick={() => applyFormat('<b>', '</b>')} style={{ padding: '2px 8px', fontSize: '11px', fontWeight: 800, borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Bold">B</button>
                <button type="button" onClick={() => applyFormat('<i>', '</i>')} style={{ padding: '2px 8px', fontSize: '11px', fontStyle: 'italic', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Italic">I</button>
                <button type="button" onClick={() => applyFormat('<u>', '</u>')} style={{ padding: '2px 8px', fontSize: '11px', textDecoration: 'underline', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Underline">U</button>

                {/* Bulleted & Numbered lists */}
                <button type="button" onClick={() => applyFormat('• ')} style={{ padding: '2px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Add Bullet Point">• List</button>
                <button type="button" onClick={() => applyFormat('1. ')} style={{ padding: '2px 6px', fontSize: '11px', borderRadius: '4px', border: '1px solid var(--border-light)', background: 'var(--surface)', color: 'var(--text)', cursor: 'pointer' }} title="Add Numbered Point">1. List</button>
              </div>

              <textarea 
                id="notice-body-textarea"
                placeholder="Write your announcement details here..." 
                value={bodyText} 
                onChange={(e) => setBodyText(e.target.value)}
                required
                rows={5}
                style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-light)', borderRadius: '0 0 var(--radius-md) var(--radius-md)', background: 'var(--bg-soft)', color: 'var(--text)', outline: 'none', resize: 'vertical', fontSize: '13px', fontFamily: 'inherit' }}
              />

              {/* Live Rich Text Notice Preview */}
              {bodyText.trim() && (
                <div style={{ marginTop: '10px', padding: '12px 14px', background: 'var(--bg)', border: '1px dashed var(--accent)', borderRadius: 'var(--radius-md)' }}>
                  <span style={{ fontSize: '10px', fontWeight: 800, color: 'var(--accent)', display: 'block', marginBottom: '6px', letterSpacing: '0.5px' }}>👁️ LIVE NOTICE PREVIEW</span>
                  <div 
                    style={{ fontSize: '13px', color: 'var(--text)', lineHeight: '1.25' }}
                    dangerouslySetInnerHTML={{ __html: renderNoticeHTML(bodyText) }} 
                  />
                </div>
              )}
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: noticeType === 'schedule' ? '1fr 1fr' : '1fr', gap: '16px' }}>
              <div>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>Notice Type</label>
                <select
                  value={noticeType}
                  onChange={(e) => setNoticeType(e.target.value as any)}
                  style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--bg-soft)', color: 'var(--text)', outline: 'none', fontSize: '13px' }}
                >
                  <option value="general">📢 General Announcement</option>
                  <option value="schedule">📅 Class Schedule</option>
                  <option value="fees">💰 Fees Reminder</option>
                </select>
              </div>

              {noticeType === 'schedule' && (
                <div>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>Schedule Date</label>
                  <input 
                    type="date" 
                    value={noticeDate} 
                    onChange={(e) => setNoticeDate(e.target.value)}
                    required
                    style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--bg-soft)', color: 'var(--text)', outline: 'none', fontSize: '13px' }}
                  />
                </div>
              )}
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '8px' }}>Select Target Audience</label>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '4px' }}>
                {(['all', 'batch', 'student', 'parent'] as const).map((type) => (
                  <button
                    key={type}
                    type="button"
                    onClick={() => setTargetType(type)}
                    style={{
                      padding: '8px 2px',
                      borderRadius: 'var(--radius-sm)',
                      border: '1px solid var(--border-light)',
                      fontSize: '11px',
                      fontWeight: 600,
                      cursor: 'pointer',
                      background: targetType === type ? 'var(--accent)' : 'var(--bg-soft)',
                      color: targetType === type ? '#ffffff' : 'var(--text)',
                      transition: 'all 0.2s',
                      textAlign: 'center',
                      whiteSpace: 'nowrap'
                    }}
                  >
                    {type === 'all' && '🌍 All'}
                    {type === 'batch' && '📦 Batch'}
                    {type === 'student' && '👥 Student'}
                    {type === 'parent' && '👪 Parent'}
                  </button>
                ))}
              </div>
            </div>

            {/* Target Selectors */}
            {targetType === 'batch' && (
              <div style={{ background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '8px' }}>Select Batches</label>
                {batches.length === 0 ? (
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>No active batches found.</div>
                ) : (
                  <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
                    gap: '8px',
                    maxHeight: '200px',
                    overflowY: 'auto',
                    padding: '8px',
                    background: 'var(--bg)',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--border-light)'
                  }}>
                    {batches.map(batch => (
                      <label key={batch.id} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', color: 'var(--text)' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedBatchIds.includes(batch.id)} 
                          onChange={() => handleBatchSelect(batch.id)} 
                        />
                        {batch.name}
                      </label>
                    ))}
                  </div>
                )}
              </div>
            )}

            {targetType === 'student' && (
              <div style={{ background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '8px' }}>Select Students</label>
                {students.length === 0 ? (
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>No active students found.</div>
                ) : (
                  <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
                    gap: '8px',
                    maxHeight: '220px',
                    overflowY: 'auto',
                    padding: '8px',
                    background: 'var(--bg)',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--border-light)'
                  }}>
                    {students.map(stud => (
                      <label key={stud.studentCode} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', color: 'var(--text)' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedStudentCodes.includes(stud.studentCode)} 
                          onChange={() => handleStudentSelect(stud.studentCode)} 
                        />
                        {stud.name}
                      </label>
                    ))}
                  </div>
                )}
              </div>
            )}

            {targetType === 'parent' && (
              <div style={{ background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '8px' }}>Select Parents</label>
                {parents.length === 0 ? (
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>No active parents found.</div>
                ) : (
                  <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
                    gap: '8px',
                    maxHeight: '220px',
                    overflowY: 'auto',
                    padding: '8px',
                    background: 'var(--bg)',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--border-light)'
                  }}>
                    {parents.map(p => (
                      <label key={p.email} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', color: 'var(--text)' }}>
                        <input 
                          type="checkbox" 
                          checked={selectedParentEmails.includes(p.email)} 
                          onChange={() => handleParentSelect(p.email)} 
                        />
                        {p.displayName}
                      </label>
                    ))}
                  </div>
                )}
              </div>
            )}

            <button
              type="submit"
              disabled={publishing}
              style={{
                width: '100%',
                padding: '12px',
                borderRadius: 'var(--radius-md)',
                background: 'var(--accent)',
                color: '#ffffff',
                border: 'none',
                fontWeight: 'bold',
                cursor: 'pointer',
                transition: 'opacity 0.2s',
                marginTop: '8px'
              }}
            >
              {publishing ? 'Publishing Announcement...' : '📢 Broadcast Announcement'}
            </button>
          </form>
        </div>

        {/* Notices History List */}
        <div className="card" style={{ padding: '24px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '2px solid var(--border-glass)', boxShadow: 'var(--shadow-glass)', display: 'flex', flexDirection: 'column' }}>
          <h3 style={{ margin: '0 0 16px 0', fontSize: '16px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}>
            ⏳ Sent Announcement History
          </h3>

          <div style={{ flex: 1, overflowY: 'auto', maxHeight: '520px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {notices.length === 0 ? (
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--text-muted)', fontSize: '14px' }}>
                No announcements published yet.
              </div>
            ) : (
              notices.map(notice => (
                <div key={notice.id} style={{ padding: '14px', background: 'var(--bg-soft)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                      <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold', color: 'var(--text)' }}>{notice.title}</h4>
                      {notice.type && (
                        <span style={{
                          fontSize: '9.5px',
                          background: notice.type === 'schedule' ? 'rgba(59, 130, 246, 0.15)' : notice.type === 'fees' ? 'rgba(245, 158, 11, 0.15)' : 'rgba(139, 92, 246, 0.15)',
                          color: notice.type === 'schedule' ? '#60a5fa' : notice.type === 'fees' ? '#fbbf24' : '#a78bfa',
                          padding: '1px 5px',
                          borderRadius: '4px',
                          fontWeight: 800,
                          textTransform: 'uppercase'
                        }}>
                          {notice.type === 'schedule' ? '📅 Schedule' : notice.type === 'fees' ? '💰 Fees' : '📢 General'}
                        </span>
                      )}
                      {notice.isOverlay && (
                        <span style={{ fontSize: '9px', background: 'rgba(239, 68, 68, 0.15)', color: '#f87171', padding: '1px 5px', borderRadius: '4px', fontWeight: 600 }}>🚨 OVERLAY</span>
                      )}
                    </div>
                    <span style={{ fontSize: '10px', color: 'var(--text-muted)' }}>
                      {notice.createdAt ? new Date(notice.createdAt).toLocaleDateString('en-IN') : 'Draft'}
                    </span>
                  </div>
                  
                  <div 
                    style={{ margin: '4px 0 10px 0', fontSize: '12.5px', color: 'var(--text)', lineHeight: '1.25' }}
                    dangerouslySetInnerHTML={{ __html: renderNoticeHTML(notice.body) }}
                  />

                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '10px', color: 'var(--text-muted)', borderTop: '1px solid var(--border-light)', paddingTop: '8px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span>By: <strong>{notice.createdBy}</strong></span>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                        <button 
                          onClick={() => handleViewLogs(notice.id)}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: 'var(--accent)',
                            cursor: 'pointer',
                            fontSize: '11px',
                            fontWeight: 600,
                            display: 'flex',
                            alignItems: 'center',
                            gap: '4px',
                            padding: '2px 4px',
                            borderRadius: 'var(--radius-sm)'
                          }}
                        >
                          👁️ Seen Logs
                        </button>
                        <button 
                          onClick={() => handleDelete(notice.id)}
                          title="Delete Announcement"
                          style={{ background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', fontSize: '12px', padding: '2px', display: 'flex', alignItems: 'center' }}
                        >
                          🗑️
                        </button>
                      </div>
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px' }}>
                      <span style={{ padding: '2px 6px', background: 'var(--accent-soft)', borderRadius: 'var(--radius-sm)', color: 'var(--accent)', fontWeight: 600, wordBreak: 'break-all', width: '100%' }}>
                        Target: {notice.targetType.toUpperCase()} {notice.targetValues.length > 0 && `(${notice.targetValues.join(', ')})`}
                      </span>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* 🛠️ System Access & Maintenance Mode Panel */}
      <div className="card" style={{ padding: '20px', background: 'var(--surface)', borderRadius: 'var(--radius-lg)', border: '2px solid var(--border-glass)', boxShadow: 'var(--shadow-glass)', marginTop: '24px', marginBottom: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '10px' }}>
          <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent)' }}>
            🛠️ System Access & Maintenance Mode
          </h3>
          <span style={{ fontSize: '11px', fontWeight: 700, padding: '4px 10px', borderRadius: '12px', background: maintenanceMode ? 'rgba(239, 68, 68, 0.15)' : 'rgba(16, 185, 129, 0.15)', color: maintenanceMode ? '#f87171' : '#34d399', border: maintenanceMode ? '1px solid rgba(239, 68, 68, 0.3)' : '1px solid rgba(16, 185, 129, 0.3)' }}>
            {maintenanceMode ? '🚨 Maintenance Mode ACTIVE' : '🟢 System Access ACTIVE'}
          </span>
        </div>
        
        <p style={{ margin: '0 0 16px 0', fontSize: '12px', color: 'var(--text-muted)' }}>
          Block students or parents from accessing the application workspace during code updates or system maintenance periods.
        </p>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {/* Row 1: Maintenance Toggles & Blocking Message */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '24px', alignItems: 'flex-start' }}>
            {/* Toggles */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', minWidth: '240px' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', cursor: 'pointer', fontWeight: 600 }}>
                <input 
                  type="checkbox" 
                  checked={maintenanceMode} 
                  onChange={(e) => setMaintenanceMode(e.target.checked)} 
                />
                ⚙️ Enable Maintenance Mode
              </label>

              <div style={{ paddingLeft: '24px', display: 'flex', flexDirection: 'column', gap: '8px', opacity: maintenanceMode ? 1 : 0.5 }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12.5px', cursor: maintenanceMode ? 'pointer' : 'default' }}>
                  <input 
                    type="checkbox" 
                    disabled={!maintenanceMode}
                    checked={blockStudent} 
                    onChange={(e) => setBlockStudent(e.target.checked)} 
                  />
                  👥 Block Student Portal
                </label>

                <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12.5px', cursor: maintenanceMode ? 'pointer' : 'default' }}>
                  <input 
                    type="checkbox" 
                    disabled={!maintenanceMode}
                    checked={blockParent} 
                    onChange={(e) => setBlockParent(e.target.checked)} 
                  />
                  👪 Block Parent Portal
                </label>
              </div>
            </div>

            {/* Message Textarea */}
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '6px', minWidth: '280px' }}>
              <label style={{ fontSize: '12px', fontWeight: 600, color: 'var(--text-muted)' }}>Custom Blocking Overlay Message</label>
              <textarea
                placeholder="e.g. System is undergoing scheduled maintenance. Access will be restored shortly."
                value={maintenanceMessage}
                onChange={(e) => setMaintenanceMessage(e.target.value)}
                disabled={!maintenanceMode}
                rows={2}
                style={{ width: '100%', padding: '8px 10px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-md)', background: 'var(--bg-soft)', color: 'var(--text)', fontSize: '12.5px', outline: 'none', resize: 'vertical', opacity: maintenanceMode ? 1 : 0.5 }}
              />
            </div>
          </div>

          {/* Row 2: Maintenance Schedule & Announcement Broadcast */}
          <div style={{ background: 'var(--bg-soft)', padding: '14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-light)', display: 'flex', flexWrap: 'wrap', gap: '14px', alignItems: 'center', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap', flex: 1 }}>
              <div>
                <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '4px' }}>📅 Scheduled Start Time</label>
                <input 
                  type="datetime-local" 
                  value={maintenanceStart}
                  onChange={(e) => setMaintenanceStart(e.target.value)}
                  style={{ padding: '6px 10px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>

              <div>
                <label style={{ display: 'block', fontSize: '10px', fontWeight: 800, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '4px' }}>🏁 Scheduled End Time</label>
                <input 
                  type="datetime-local" 
                  value={maintenanceEnd}
                  onChange={(e) => setMaintenanceEnd(e.target.value)}
                  style={{ padding: '6px 10px', border: '1px solid var(--border-light)', borderRadius: 'var(--radius-sm)', background: 'var(--surface)', color: 'var(--text)', fontSize: '12px' }}
                />
              </div>

              <div style={{ alignSelf: 'flex-end' }}>
                <button
                  type="button"
                  onClick={handleBroadcastMaintenanceSchedule}
                  className="btn btn-secondary"
                  style={{ height: '34px', fontSize: '11.5px', fontWeight: 700, background: 'rgba(99, 102, 241, 0.1)', color: 'var(--accent)', border: '1px solid rgba(99, 102, 241, 0.3)' }}
                >
                  📢 Broadcast Schedule Announcement
                </button>
              </div>
            </div>

            {/* Action Buttons: Save & Disable */}
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
              {maintenanceMode && (
                <button
                  type="button"
                  onClick={handleDisableMaintenance}
                  disabled={savingAccess}
                  className="btn btn-danger"
                  style={{ height: '38px', fontSize: '12px', fontWeight: 700, padding: '0 16px' }}
                >
                  🔴 Disable Maintenance
                </button>
              )}

              <button
                type="button"
                onClick={handleSaveAccessConfig}
                disabled={savingAccess}
                className="btn btn-primary"
                style={{ height: '38px', fontSize: '12px', fontWeight: 700, padding: '0 18px' }}
              >
                {savingAccess ? 'Saving...' : '💾 Save Access Settings'}
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Seen Logs Modal */}
      {selectedNoticeLogId && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(4px)', WebkitBackdropFilter: 'blur(4px)', zIndex: 9999 }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', maxWidth: '580px', width: '100%', margin: 'auto', display: 'flex', flexDirection: 'column', maxHeight: '80vh' }}>
            <div className="modal-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '16px 20px', borderBottom: '1px solid var(--border)' }}>
              <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 'bold', color: 'var(--text)' }}>
                📊 Notice Delivery & Seen Logs
              </h3>
              <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                {noticeLogData && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <select
                      value={noticeLogSort}
                      onChange={(e) => setNoticeLogSort(e.target.value as any)}
                      style={{
                        background: 'var(--surface)',
                        color: 'var(--text)',
                        border: '1px solid var(--border)',
                        borderRadius: 'var(--radius-sm)',
                        padding: '4px 8px',
                        fontSize: '11px',
                        fontWeight: 600,
                        cursor: 'pointer'
                      }}
                    >
                      <option value="name">Sort: Name (A-Z)</option>
                      <option value="seen_first">Sort: Seen First 🟢</option>
                      <option value="unseen_first">Sort: Not Seen First ❌</option>
                    </select>

                    <button 
                      onClick={() => setShowPdfOptionsModal(true)}
                      style={{
                        background: 'var(--accent)',
                        color: '#ffffff',
                        border: 'none',
                        borderRadius: 'var(--radius-sm)',
                        padding: '6px 12px',
                        fontSize: '11.5px',
                        fontWeight: 'bold',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '4px'
                      }}
                    >
                      📥 Export PDF
                    </button>
                  </div>
                )}
                <button onClick={() => setSelectedNoticeLogId(null)} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
              </div>
            </div>
            
            <div className="modal-body" style={{ padding: '20px', overflowY: 'auto', flex: 1, fontSize: '13px' }}>
              {logLoading ? (
                <div style={{ padding: '32px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  Loading seen receipts logs...
                </div>
              ) : !noticeLogData ? (
                <div style={{ padding: '32px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  Failed to load seen logs data.
                </div>
              ) : (
                <div>
                  <div style={{ background: 'var(--bg-soft)', padding: '12px 16px', borderRadius: 'var(--radius-md)', marginBottom: '16px', border: '1px solid var(--border)' }}>
                    <div style={{ fontWeight: 700, fontSize: '14px', marginBottom: '4px', color: 'var(--text)' }}>
                      {noticeLogData.title}
                    </div>
                    <div style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                      Target Group: <span style={{ textTransform: 'uppercase', fontWeight: 600, color: 'var(--accent)' }}>{noticeLogData.targetType}</span>
                    </div>
                  </div>

                  {/* Student Groups Section */}
                  <h4 style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)', margin: '0 0 8px 0', borderBottom: '1px solid var(--border)', paddingBottom: '4px' }}>
                    👥 Students Status (Batch-wise)
                  </h4>
                  {Object.keys(noticeLogData.studentGroups).length === 0 ? (
                    <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginBottom: '16px', fontStyle: 'italic' }}>
                      No students targeted.
                    </div>
                  ) : (
                    Object.keys(noticeLogData.studentGroups).map(batchName => (
                      <div key={batchName} style={{ marginBottom: '16px' }}>
                        <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', marginBottom: '6px' }}>
                          📦 {batchName} ({noticeLogData.studentGroups[batchName].length})
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', background: 'var(--bg)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', overflow: 'hidden' }}>
                          {getSortedLogs(noticeLogData.studentGroups[batchName]).map((stud: any, idx: number) => (
                            <div 
                              key={stud.studentCode} 
                              style={{ 
                                display: 'flex', 
                                justifyContent: 'space-between', 
                                alignItems: 'center', 
                                fontSize: '12px', 
                                padding: '8px 12px', 
                                background: idx % 2 === 0 ? 'var(--bg-soft)' : 'transparent',
                                borderBottom: idx < noticeLogData.studentGroups[batchName].length - 1 ? '1px solid var(--border)' : 'none'
                              }}
                            >
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span style={{ color: 'var(--text)', fontWeight: 500 }}>{stud.autonomous ? '# ' : ''}{stud.name} (S)</span>
                                {stud.hasPushRegistered ? (
                                  <span style={{ fontSize: '10px', background: 'rgba(16, 185, 129, 0.1)', color: '#059669', padding: '1px 5px', borderRadius: '4px', fontWeight: 600 }}>📲 Push Active</span>
                                ) : (
                                  <span style={{ fontSize: '10px', background: 'rgba(239, 68, 68, 0.1)', color: '#dc2626', padding: '1px 5px', borderRadius: '4px', fontWeight: 600 }}>📴 Push Disabled</span>
                                )}
                              </div>
                              {stud.seen ? (
                                <span style={{ color: 'var(--success)', fontWeight: 600, fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                  🟢 Seen at {new Date(stud.seenAt).toLocaleString('en-IN', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit', hour12: true })}
                                </span>
                              ) : (
                                <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>
                                  ❌ Not Seen yet
                                </span>
                              )}
                            </div>
                          ))}
                        </div>
                      </div>
                    ))
                  )}

                  {/* Parents Section */}
                  {noticeLogData.parentGroups && Object.keys(noticeLogData.parentGroups).length > 0 && (
                    <div style={{ marginTop: '20px' }}>
                      <h4 style={{ fontSize: '13px', fontWeight: 700, color: 'var(--text-muted)', margin: '0 0 8px 0', borderBottom: '1px solid var(--border)', paddingBottom: '4px' }}>
                        👪 Parents Status (Batch-wise)
                      </h4>
                      {Object.keys(noticeLogData.parentGroups).map(batchName => (
                        <div key={batchName} style={{ marginBottom: '16px' }}>
                          <div style={{ fontSize: '12px', fontWeight: 700, color: 'var(--accent)', marginBottom: '6px' }}>
                            📦 {batchName} ({noticeLogData.parentGroups[batchName].length})
                          </div>
                          <div style={{ display: 'flex', flexDirection: 'column', background: 'var(--bg)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border)', overflow: 'hidden' }}>
                            {getSortedLogs(noticeLogData.parentGroups[batchName]).map((parent: any, idx: number) => (
                              <div 
                                key={parent.email} 
                                style={{ 
                                  display: 'flex', 
                                  justifyContent: 'space-between', 
                                  alignItems: 'center', 
                                  fontSize: '12px', 
                                  padding: '8px 12px', 
                                  background: idx % 2 === 0 ? 'var(--bg-soft)' : 'transparent',
                                  borderBottom: idx < noticeLogData.parentGroups[batchName].length - 1 ? '1px solid var(--border)' : 'none'
                                }}
                              >
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                                  <span style={{ color: 'var(--text)', fontWeight: 500 }}>
                                    {parent.autonomous ? '# ' : ''}{parent.studentName} (P)
                                  </span>
                                  {parent.hasPushRegistered ? (
                                    <span style={{ fontSize: '10px', background: 'rgba(16, 185, 129, 0.1)', color: '#059669', padding: '1px 5px', borderRadius: '4px', fontWeight: 600 }}>📲 Push Active</span>
                                  ) : (
                                    <span style={{ fontSize: '10px', background: 'rgba(239, 68, 68, 0.1)', color: '#dc2626', padding: '1px 5px', borderRadius: '4px', fontWeight: 600 }}>📴 Push Disabled</span>
                                  )}
                                </div>
                                {parent.seen ? (
                                  <span style={{ color: 'var(--success)', fontWeight: 600, fontSize: '11px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                    🟢 Seen at {new Date(parent.seenAt).toLocaleString('en-IN', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit', hour12: true })}
                                  </span>
                                ) : (
                                  <span style={{ color: 'var(--text-muted)', fontSize: '11px' }}>
                                    ❌ Not Seen yet
                                  </span>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
            
            <div className="modal-footer" style={{ padding: '12px 16px', borderTop: '1px solid var(--border-light)', display: 'flex', justifyContent: 'flex-end', background: 'var(--surface-2)' }}>
              <button className="btn btn-secondary" onClick={() => setSelectedNoticeLogId(null)}>Close</button>
            </div>
          </div>
        </div>
      )}

      {/* PDF Export Print Options Modal */}
      {showPdfOptionsModal && (
        <div className="modal show" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.55)', backdropFilter: 'blur(5px)', WebkitBackdropFilter: 'blur(5px)', zIndex: 10000 }}>
          <div className="modal-content" style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', maxWidth: '440px', width: '100%', margin: 'auto', borderRadius: 'var(--radius-lg)', padding: '24px', boxShadow: 'var(--shadow-lg)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 'bold', color: 'var(--text)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                📄 Select What to Print (Export PDF)
              </h3>
              <button onClick={() => setShowPdfOptionsModal(false)} style={{ background: 'transparent', border: 'none', cursor: 'pointer', fontSize: '1.2rem', color: 'var(--text-muted)' }}>✕</button>
            </div>

            <p style={{ fontSize: '12.5px', color: 'var(--text-muted)', marginBottom: '16px', marginTop: 0 }}>
              Choose which log sections to include in the exported PDF report:
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginBottom: '24px' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: 'var(--text)', cursor: 'pointer', background: 'var(--bg-soft)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                <input 
                  type="checkbox" 
                  checked={pdfPrintStudents} 
                  onChange={(e) => setPdfPrintStudents(e.target.checked)} 
                  style={{ width: '16px', height: '16px', accentColor: 'var(--accent)' }}
                />
                <strong>1. Students Log</strong>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: 'var(--text)', cursor: 'pointer', background: 'var(--bg-soft)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                <input 
                  type="checkbox" 
                  checked={pdfPrintParents} 
                  onChange={(e) => setPdfPrintParents(e.target.checked)} 
                  style={{ width: '16px', height: '16px', accentColor: 'var(--accent)' }}
                />
                <strong>2. Parents Log</strong>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '13px', color: 'var(--text)', cursor: 'pointer', background: 'var(--bg-soft)', padding: '10px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-light)' }}>
                <input 
                  type="checkbox" 
                  checked={pdfPrintNotSeenOnly} 
                  onChange={(e) => setPdfPrintNotSeenOnly(e.target.checked)} 
                  style={{ width: '16px', height: '16px', accentColor: 'var(--accent)' }}
                />
                <div>
                  <strong>3. Not Seen Log Only ❌</strong>
                  <span style={{ display: 'block', fontSize: '10.5px', color: 'var(--danger)', marginTop: '2px' }}>
                    Filter report to only show recipients who have NOT seen the notice
                  </span>
                </div>
              </label>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button 
                className="btn btn-secondary" 
                onClick={() => setShowPdfOptionsModal(false)}
                style={{ fontSize: '12px', padding: '6px 14px' }}
              >
                Cancel
              </button>
              <button 
                className="btn btn-primary" 
                onClick={() => {
                  setShowPdfOptionsModal(false);
                  handleExportPDF();
                }}
                disabled={!pdfPrintStudents && !pdfPrintParents}
                style={{ fontSize: '12px', padding: '6px 16px', background: 'var(--accent)', color: '#ffffff', fontWeight: 'bold' }}
              >
                🖨️ Print / Export PDF
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
