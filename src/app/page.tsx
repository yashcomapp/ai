import React, { Suspense } from 'react';
import Link from 'next/link';
import LoginModal from '@/components/LoginModal';
import Image from 'next/image';

export default function LoginPage() {
  return (
    <div className="landing-shell">
      <style dangerouslySetInnerHTML={{ __html: `
        .landing-shell {
          background-color: var(--bg);
          color: var(--text);
          min-height: 100vh;
          display: flex;
          flex-direction: column;
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          font-family: var(--font-family);
          position: relative;
        }

        /* Header Bar */
        .landing-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 8px 16px;
          background: var(--surface);
          border-bottom: 1px solid var(--border-light);
          box-shadow: var(--shadow-xs);
          box-sizing: border-box;
          height: 52px;
          position: sticky;
          top: 0;
          z-index: 100;
        }
        .brand-container {
          display: flex;
          align-items: center;
          gap: 8px;
          text-decoration: none;
          color: var(--text);
        }
        .brand-name {
          font-size: 14px;
          font-weight: 800;
          color: var(--text);
          letter-spacing: 0.2px;
        }
        .btn-pill-login {
          background: var(--accent-grad);
          color: #ffffff;
          border: none;
          padding: 6px 18px;
          border-radius: var(--radius-pill);
          font-weight: 800;
          font-size: 13px;
          cursor: pointer;
          transition: all 0.2s ease;
          box-shadow: var(--shadow-sm);
          text-decoration: none;
          display: inline-flex;
          align-items: center;
          justify-content: center;
        }
        .btn-pill-login:hover {
          transform: translateY(-1px);
          box-shadow: var(--shadow-md);
        }

        /* Hero Section */
        .hero-section {
          padding: 40px 16px 24px;
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items: center;
          box-sizing: border-box;
          max-width: 900px;
          margin: 0 auto;
          width: 100%;
        }
        .hero-badge {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          background: var(--accent-soft);
          border: 1px solid var(--accent-ring);
          color: var(--accent);
          font-size: 11px;
          font-weight: 700;
          padding: 4px 12px;
          border-radius: var(--radius-pill);
          margin-bottom: 16px;
        }
        .hero-title {
          font-size: 38px;
          font-weight: 900;
          line-height: 1.2;
          color: var(--text);
          letter-spacing: -0.5px;
          margin: 0 0 14px;
          max-width: 720px;
        }
        .hero-title-accent {
          background: var(--accent-grad);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
        .hero-desc {
          font-size: 14px;
          font-weight: 500;
          max-width: 620px;
          margin: 0 0 24px;
          line-height: 1.5;
          color: var(--text-secondary);
        }
        .hero-actions {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 12px;
          flex-wrap: wrap;
        }
        .btn-hero-primary {
          background: var(--accent-grad);
          color: #ffffff;
          border: none;
          padding: 10px 24px;
          border-radius: var(--radius);
          font-weight: 800;
          font-size: 14px;
          cursor: pointer;
          transition: all 0.2s ease;
          box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
          text-decoration: none;
          display: inline-flex;
          align-items: center;
          gap: 6px;
        }
        .btn-hero-primary:hover {
          transform: translateY(-1px);
          box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
        }
        .btn-hero-secondary {
          background: var(--surface);
          color: var(--text);
          border: 1.5px solid var(--border);
          padding: 10px 20px;
          border-radius: var(--radius);
          font-weight: 700;
          font-size: 14px;
          cursor: pointer;
          transition: all 0.2s ease;
          text-decoration: none;
          display: inline-flex;
          align-items: center;
          gap: 6px;
        }
        .btn-hero-secondary:hover {
          background: var(--surface-2);
          border-color: var(--border-light);
        }

        /* Features Section */
        .features-section {
          padding: 20px 16px 40px;
          max-width: 1000px;
          width: 100%;
          margin: 0 auto;
          box-sizing: border-box;
        }
        .features-header {
          text-align: center;
          margin-bottom: 20px;
        }
        .features-heading {
          font-size: 22px;
          font-weight: 800;
          color: var(--text);
          line-height: 1.3;
          margin: 0 0 6px;
        }
        .features-sub {
          font-size: 13px;
          color: var(--text-muted);
          margin: 0;
        }
        .cards-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 12px;
        }
        .landing-card {
          border-radius: var(--radius);
          padding: 16px;
          display: flex;
          flex-direction: column;
          gap: 8px;
          box-shadow: var(--shadow-sm);
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .landing-card:hover {
          transform: translateY(-2px);
          box-shadow: var(--shadow-md);
        }
        .landing-card-header {
          display: flex;
          align-items: center;
          gap: 6px;
        }
        .landing-card-title {
          font-size: 14px;
          font-weight: 800;
          margin: 0;
          line-height: 1.2;
        }
        .landing-card-desc {
          font-size: 12.5px;
          color: var(--text-secondary);
          line-height: 1.45;
          margin: 0;
        }

        /* Footer */
        .landing-footer {
          padding: 16px 20px;
          text-align: center;
          background: var(--surface);
          border-top: 1px solid var(--border-light);
          font-size: 11px;
          color: var(--text-muted);
          box-sizing: border-box;
          margin-top: auto;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        @media (max-width: 768px) {
          .hero-section {
            padding: 24px 16px 16px;
          }
          .hero-title {
            font-size: 26px;
            margin-bottom: 10px;
          }
          .hero-desc {
            font-size: 13px;
            margin-bottom: 20px;
          }
          .cards-grid {
            grid-template-columns: 1fr;
            gap: 10px;
          }
          .features-heading {
            font-size: 18px;
          }
        }
      ` }} />

      {/* Top Navigation Bar */}
      <header className="landing-header">
        <Link href="/" className="brand-container">
          <Image src="/logo.png" alt="YASHCOM Logo" width={26} height={26} style={{ borderRadius: '50%', objectFit: 'cover' }} priority />
          <span className="brand-name">YASHCOM — LEARN OS</span>
        </Link>
        
        <div>
          <Link href="?login=true" className="btn-pill-login">
            Login →
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-badge">
          ✨ AI-Powered Learning Operating System
        </div>
        <h1 className="hero-title">
          Learning, Reimagined for <span className="hero-title-accent">Every Mind</span>
        </h1>
        <p className="hero-desc">
          Built to empower students with autonomous daily practice, adaptive diagnostic analytics, and real-time parent-teacher synergy.
        </p>

        <div className="hero-actions">
          <Link href="?login=true" className="btn-hero-primary">
            <span>Sign In to Dashboard</span>
            <span>→</span>
          </Link>
          <Link href="/register" className="btn-hero-secondary">
            <span>New Student Registration</span>
          </Link>
        </div>
      </section>

      {/* Features Grid */}
      <section id="features" className="features-section">
        <div className="features-header">
          <h2 className="features-heading">Personalized Excellence for Every Learner</h2>
          <p className="features-sub">Engineered to replace one-size-fits-all education with precision diagnostic intelligence.</p>
        </div>

        <div className="cards-grid">
          {/* Card 1: Blue Accent Card */}
          <div className="landing-card card-blue">
            <div className="landing-card-header">
              <span style={{ fontSize: '16px' }}>🎯</span>
              <h3 className="landing-card-title" style={{ color: '#1e40af' }}>Adaptive Practice Engine</h3>
            </div>
            <p className="landing-card-desc">
              Dynamic topic-level question pools with intelligent recovery cycles, automated cooldowns, and mistake-analysis.
            </p>
          </div>

          {/* Card 2: Purple Accent Card */}
          <div className="landing-card card-purple">
            <div className="landing-card-header">
              <span style={{ fontSize: '16px' }}>⚡</span>
              <h3 className="landing-card-title" style={{ color: '#6b21a8' }}>Learning Quotient (LQ)</h3>
            </div>
            <p className="landing-card-desc">
              Real-time multi-dimensional scoring that measures mastery, consistency, effort, and integrity instead of raw marks.
            </p>
          </div>

          {/* Card 3: Cyan Accent Card */}
          <div className="landing-card card-cyan">
            <div className="landing-card-header">
              <span style={{ fontSize: '16px' }}>🤝</span>
              <h3 className="landing-card-title" style={{ color: '#115e59' }}>5-Min Daily Parent Sync</h3>
            </div>
            <p className="landing-card-desc">
              Structured nightly review rituals bringing parents, students, and teachers together on a shared progress ledger.
            </p>
          </div>
        </div>
      </section>

      {/* Minimal Clean Footer */}
      <footer className="landing-footer">
        <p style={{ margin: 0 }}>© 2026 Yashcom Foundation • AI-Powered Learning Operating System</p>
      </footer>

      {/* Client-side login modal overlay */}
      <Suspense fallback={null}>
        <LoginModal />
      </Suspense>
    </div>
  );
}
