'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';

interface Batch {
  id: string;
  name: string;
  subject: string;
  description: string;
}

const NAME_RE     = /^[A-Za-z][A-Za-z\s'-]{1,}$/;
const MOBILE_RE   = /^[6-9]\d{9}$/;
const EMAIL_RE    = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PASSWORD_RE = /^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]).{8,}$/;

export default function RegisterPage() {
  const [batches, setBatches] = useState<Batch[]>([]);
  const [loadingBatches, setLoadingBatches] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  // Form Fields
  const [formData, setFormData] = useState({
    batchId: '',
    studentName: '',
    dob: '',
    gender: '',
    studentEmail: '',
    studentMobile: '',
    bloodGroup: '',
    address: '',
    parentName: '',
    parentRelation: '',
    parentMobile: '',
    parentEmail: '',
    parentOccupation: '',
    password: 'Yashcom@26',
    confirmPassword: 'Yashcom@26'
  });

  // Validation messages state
  const [validationErrors, setValidationErrors] = useState<Record<string, string>>({});

  useEffect(() => {
    async function fetchBatches() {
      try {
        const res = await fetch('/api/batches');
        if (res.ok) {
          const data = await res.json();
          setBatches(data.batches || []);
        }
      } catch (err) {
        console.error('Failed to load batches:', err);
      } finally {
        setLoadingBatches(false);
      }
    }
    fetchBatches();
  }, []);

  const validateDob = (v: string): string => {
    if (!v) return 'Date of birth is required.';
    const d = new Date(v + 'T00:00:00');
    const today = new Date(); today.setHours(0,0,0,0);
    if (d >= today) return 'Date of birth cannot be today or in the future.';
    const age = (today.getTime() - d.getTime()) / (1000*60*60*24*365.25);
    if (age < 5)  return 'Student must be at least 5 years old.';
    if (age > 25) return 'Please check the date of birth.';
    return '';
  };

  const validateField = (name: string, value: string): string => {
    let msg = '';
    switch (name) {
      case 'studentName':
        msg = !NAME_RE.test(value.trim()) || value.trim().split(/\s+/).length < 2 
          ? 'Enter first and last name (letters only).' : '';
        break;
      case 'dob':
        msg = validateDob(value);
        break;
      case 'studentEmail':
        msg = !EMAIL_RE.test(value.trim()) ? 'Enter a valid email address.' : '';
        break;
      case 'studentMobile':
        msg = !MOBILE_RE.test(value.trim()) ? 'Enter a valid 10-digit mobile number.' : '';
        break;
      case 'parentMobile':
        msg = !MOBILE_RE.test(value.trim()) ? 'Enter a valid 10-digit mobile number.' : '';
        break;
      case 'parentEmail':
        msg = !EMAIL_RE.test(value.trim()) ? 'Parent email is required for parent login.' : '';
        break;
      case 'password':
        msg = !PASSWORD_RE.test(value) ? 'Min 8 characters, 1 uppercase letter, 1 special character.' : '';
        break;
      case 'confirmPassword':
        msg = value !== formData.password ? 'Passwords do not match.' : '';
        break;
      case 'batchId':
        msg = !value ? 'Please select a batch.' : '';
        break;
      case 'gender':
        msg = !value ? 'Please select gender.' : '';
        break;
      case 'bloodGroup':
        msg = !value ? 'Please select blood group.' : '';
        break;
      case 'address':
        msg = !value.trim() ? 'Address is required.' : '';
        break;
      case 'parentName':
        msg = !NAME_RE.test(value.trim()) ? 'Enter a valid parent name (letters only).' : '';
        break;
      default:
        break;
    }
    return msg;
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    let sanitizedValue = value;

    if (name === 'studentMobile' || name === 'parentMobile') {
      sanitizedValue = value.replace(/\D/g, '').slice(0, 10);
    }

    setFormData(prev => {
      const updated = { ...prev, [name]: sanitizedValue };
      // If password is updated, check confirmPassword
      if (name === 'password' && prev.confirmPassword) {
        const confirmErr = updated.confirmPassword !== sanitizedValue ? 'Passwords do not match.' : '';
        setValidationErrors(errors => ({ ...errors, confirmPassword: confirmErr }));
      }
      return updated;
    });

    const errorMsg = validateField(name, sanitizedValue);
    setValidationErrors(prev => ({ ...prev, [name]: errorMsg }));
  };

  const handleBlur = (e: React.FocusEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    const errorMsg = validateField(name, value);
    setValidationErrors(prev => ({ ...prev, [name]: errorMsg }));
  };

  const getSelectedBatchDescription = () => {
    const selected = batches.find(b => b.id === formData.batchId);
    return selected ? selected.description : '';
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMsg('');

    // Trigger all validations
    const errors: Record<string, string> = {};
    let hasErrors = false;

    Object.keys(formData).forEach((key) => {
      // Skip optional fields and auto-filled passwords
      if (key === 'parentOccupation' || key === 'parentRelation' || key === 'password' || key === 'confirmPassword') return;
      
      const val = formData[key as keyof typeof formData];
      const err = validateField(key, val);
      if (err) {
        errors[key] = err;
        hasErrors = true;
      }
    });

    setValidationErrors(errors);

    if (hasErrors) {
      setErrorMsg('Please fix the highlighted fields.');
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    setSubmitting(true);

    try {
      const res = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.message || 'Registration failed. Please try again.');
      }

      setSuccess(true);
    } catch (err: any) {
      console.error(err);
      setErrorMsg(err.message || 'Registration failed. Please try again.');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="reg-shell" style={{ minHeight: '100vh', display: 'flex', justifyContent: 'center', padding: '24px 16px 80px' }}>
      <div className="reg-card" style={{ background: 'var(--surface)', borderRadius: 'var(--radius-lg)', boxShadow: 'var(--shadow-lg)', padding: '32px 28px', width: '100%', maxWidth: '520px' }}>
        <h1>AI @ YASHCOM</h1>
        <div className="reg-subtitle" style={{ textAlign: 'center', color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '24px' }}>
          Student Registration — Fill in your details and wait for admin approval
        </div>

        {errorMsg && (
          <div className="alert-box alert-box-danger" style={{ display: 'block', marginBottom: '20px' }}>
            {errorMsg}
          </div>
        )}

        {success ? (
          <div className="success-state" style={{ textAlign: 'center', padding: '40px 20px' }}>
            <div className="success-icon" style={{ fontSize: '3rem', marginBottom: '16px' }}>🎉</div>
            <h2>Registration Submitted!</h2>
            <p>Your registration has been sent to the admin for approval.<br />You will be notified once your account is approved.</p>
            <Link className="btn btn-primary" style={{ display: 'inline-block', marginTop: '16px' }} href="/">
              ← Back to Login
            </Link>
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            {/* BATCH / CLASS */}
            <div className="section-title" style={{ fontSize: '0.8rem', fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.06em', margin: '20px 0 10px', paddingBottom: '6px', borderBottom: '1px solid var(--border-light)' }}>
              🎓 Batch / Class
            </div>

            <div className="form-group">
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '4px' }}>
                Select Batch <span className="req" style={{ color: 'var(--danger)' }}>*</span>
              </label>
              <select 
                name="batchId"
                value={formData.batchId}
                onChange={handleInputChange}
                onBlur={handleBlur}
                className={validationErrors.batchId ? 'invalid' : ''}
              >
                <option value="">{loadingBatches ? '-- Loading Batches... --' : '-- Select Batch --'}</option>
                {batches.map(b => (
                  <option key={b.id} value={b.id}>{b.name}{b.subject ? ' — ' + b.subject : ''}</option>
                ))}
              </select>
              {formData.batchId && (
                <div className="batch-note" style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
                  {getSelectedBatchDescription()}
                </div>
              )}
              {validationErrors.batchId && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.batchId}</div>}
            </div>

            {/* STUDENT DETAILS */}
            <div className="section-title" style={{ fontSize: '0.8rem', fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.06em', margin: '20px 0 10px', paddingBottom: '6px', borderBottom: '1px solid var(--border-light)' }}>
              🧑 Student Details
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Full Name (First & Last) <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="text" 
                  name="studentName"
                  placeholder="e.g. Rahul Sharma" 
                  autoComplete="off"
                  value={formData.studentName}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.studentName ? 'invalid' : ''}
                />
                {validationErrors.studentName && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.studentName}</div>}
              </div>
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Date of Birth <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="date" 
                  name="dob"
                  value={formData.dob}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.dob ? 'invalid' : ''}
                />
                {validationErrors.dob && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.dob}</div>}
              </div>
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Gender <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <select 
                  name="gender"
                  value={formData.gender}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.gender ? 'invalid' : ''}
                >
                  <option value="">Select gender</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                  <option value="Other">Other</option>
                </select>
                {validationErrors.gender && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.gender}</div>}
              </div>
              <div className="form-group">
                <label>Email Address <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="email" 
                  name="studentEmail"
                  placeholder="student@email.com" 
                  autoComplete="off"
                  value={formData.studentEmail}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.studentEmail ? 'invalid' : ''}
                />
                <div className="batch-note" style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>This will be your login username</div>
                {validationErrors.studentEmail && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.studentEmail}</div>}
              </div>
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Mobile Number <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="tel" 
                  name="studentMobile"
                  placeholder="10-digit mobile number" 
                  maxLength={10} 
                  inputMode="numeric"
                  value={formData.studentMobile}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.studentMobile ? 'invalid' : ''}
                />
                {validationErrors.studentMobile && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.studentMobile}</div>}
              </div>
              <div className="form-group">
                <label>Blood Group <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <select 
                  name="bloodGroup"
                  value={formData.bloodGroup}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.bloodGroup ? 'invalid' : ''}
                >
                  <option value="">Select</option>
                  <option value="A+">A+</option><option value="A-">A-</option>
                  <option value="B+">B+</option><option value="B-">B-</option>
                  <option value="O+">O+</option><option value="O-">O-</option>
                  <option value="AB+">AB+</option><option value="AB-">AB-</option>
                </select>
                {validationErrors.bloodGroup && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.bloodGroup}</div>}
              </div>
            </div>

            <div className="form-group">
              <label>Address <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
              <textarea 
                name="address"
                rows={2} 
                placeholder="Home address"
                value={formData.address}
                onChange={handleInputChange}
                onBlur={handleBlur}
                className={validationErrors.address ? 'invalid' : ''}
              />
              {validationErrors.address && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.address}</div>}
            </div>

            {/* PARENT INFO */}
            <div className="section-title" style={{ fontSize: '0.8rem', fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.06em', margin: '20px 0 10px', paddingBottom: '6px', borderBottom: '1px solid var(--border-light)' }}>
              👨‍👩‍👧 Parent / Guardian Information
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Parent Name <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="text" 
                  name="parentName"
                  placeholder="Parent's full name"
                  value={formData.parentName}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.parentName ? 'invalid' : ''}
                />
                {validationErrors.parentName && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.parentName}</div>}
              </div>
              <div className="form-group">
                <label>Relation</label>
                <select 
                  name="parentRelation"
                  value={formData.parentRelation}
                  onChange={handleInputChange}
                >
                  <option value="">Select...</option>
                  <option value="Father">Father</option>
                  <option value="Mother">Mother</option>
                  <option value="Guardian">Guardian</option>
                </select>
              </div>
            </div>

            <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
              <div className="form-group">
                <label>Parent Mobile <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="tel" 
                  name="parentMobile"
                  placeholder="10-digit mobile" 
                  maxLength={10} 
                  inputMode="numeric"
                  value={formData.parentMobile}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.parentMobile ? 'invalid' : ''}
                />
                {validationErrors.parentMobile && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.parentMobile}</div>}
              </div>
              <div className="form-group">
                <label>Parent Email <span className="req" style={{ color: 'var(--danger)' }}>*</span></label>
                <input 
                  type="email" 
                  name="parentEmail"
                  placeholder="parent@email.com"
                  value={formData.parentEmail}
                  onChange={handleInputChange}
                  onBlur={handleBlur}
                  className={validationErrors.parentEmail ? 'invalid' : ''}
                />
                <div className="batch-note" style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>Used for parent login</div>
                {validationErrors.parentEmail && <div className="field-error show" style={{ fontSize: '0.75rem', color: '#dc2626', marginTop: '4px' }}>{validationErrors.parentEmail}</div>}
              </div>
            </div>

            <div className="form-group">
              <label>Parent Occupation</label>
              <input 
                type="text" 
                name="parentOccupation"
                placeholder="Optional"
                value={formData.parentOccupation}
                onChange={handleInputChange}
              />
            </div>



            <button 
              type="submit"
              className="btn btn-primary btn-block" 
              disabled={submitting}
              style={{ marginTop: '24px' }}
            >
              {submitting ? 'Submitting Registration...' : '📤 Submit Registration'}
            </button>
          </form>
        )}

        <div style={{ textAlign: 'center', marginTop: '20px' }}>
          <Link className="back-link" style={{ fontSize: '0.85rem', color: 'var(--accent)' }} href="/">
            ← Already have an account? Login
          </Link>
        </div>
      </div>
    </div>
  );
}
