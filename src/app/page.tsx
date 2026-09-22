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
          padding: 10px 24px;
          background: var(--surface);
          border-bottom: 1px solid var(--border-light);
          box-shadow: var(--shadow-xs);
          box-sizing: border-box;
          height: 60px;
          position: sticky;
          top: 0;
          z-index: 100;
          backdrop-filter: blur(12px);
        }
        .header-inner {
          max-width: 1200px;
          margin: 0 auto;
          width: 100%;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        .brand-container {
          display: flex;
          align-items: center;
          gap: 10px;
          text-decoration: none;
          color: var(--text);
          transition: transform 0.2s ease;
        }
        .brand-container:hover {
          transform: translateY(-1px);
        }
        .brand-name {
          font-size: 15px;
          font-weight: 800;
          color: var(--text);
          letter-spacing: 0.3px;
        }
        .btn-pill-login {
          background: var(--accent-grad);
          color: var(--text-white);
          border: none;
          padding: 8px 22px;
          border-radius: var(--radius-pill);
          font-weight: 800;
          font-size: 13.5px;
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
          opacity: 0.95;
        }

        /* Hero Section */
        .hero-section {
          padding: 48px 24px 32px;
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items: center;
          box-sizing: border-box;
          max-width: 960px;
          margin: 0 auto;
          width: 100%;
        }
        .hero-badge {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          background: var(--accent-soft);
          border: 1px solid var(--accent-ring);
          color: var(--accent);
          font-size: 12px;
          font-weight: 700;
          padding: 6px 16px;
          border-radius: var(--radius-pill);
          margin-bottom: 20px;
          box-shadow: 0 2px 8px rgba(37, 99, 235, 0.12);
        }
        .hero-title {
          font-size: clamp(32px, 4.5vw, 54px);
          font-weight: 900;
          line-height: 1.15;
          color: var(--text);
          letter-spacing: -0.8px;
          margin: 0 0 18px;
          max-width: 820px;
        }
        .hero-title-accent {
          background: var(--accent-grad);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }
        .hero-desc {
          font-size: clamp(14px, 1.4vw, 17px);
          font-weight: 500;
          max-width: 680px;
          margin: 0 0 28px;
          line-height: 1.6;
          color: var(--text-secondary);
        }
        .hero-actions {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 16px;
          flex-wrap: wrap;
        }
        .btn-hero-primary {
          background: var(--accent-grad);
          color: var(--text-white);
          border: none;
          padding: 12px 28px;
          border-radius: var(--radius);
          font-weight: 800;
          font-size: 15px;
          cursor: pointer;
          transition: all 0.2s ease;
          box-shadow: 0 6px 18px rgba(37, 99, 235, 0.3);
          text-decoration: none;
          display: inline-flex;
          align-items: center;
          gap: 8px;
        }
        .btn-hero-primary:hover {
          transform: translateY(-2px);
          box-shadow: 0 8px 24px rgba(37, 99, 235, 0.42);
        }
        .btn-hero-secondary {
          background: var(--surface);
          color: var(--text);
          border: 1.5px solid var(--border);
          padding: 12px 24px;
          border-radius: var(--radius);
          font-weight: 700;
          font-size: 15px;
          cursor: pointer;
          transition: all 0.2s ease;
          text-decoration: none;
          display: inline-flex;
          align-items: center;
          gap: 8px;
        }
        .btn-hero-secondary:hover {
          background: var(--surface-2);
          border-color: var(--border-focus);
          transform: translateY(-1px);
        }

        /* Features Section */
        .features-section {
          padding: 24px 24px 64px;
          max-width: 1180px;
          margin: 0 auto;
          width: 100%;
          box-sizing: border-box;
          flex: 1;
        }
        .features-header {
          text-align: center;
          margin-bottom: 36px;
        }
        .features-heading {
          font-size: clamp(20px, 2.4vw, 28px);
          font-weight: 800;
          color: var(--text);
          margin: 0 0 10px;
          letter-spacing: -0.4px;
        }
        .features-sub {
          font-size: 14.5px;
          color: var(--text-secondary);
          max-width: 640px;
          margin: 0 auto;
          line-height: 1.5;
        }
        .cards-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 24px;
        }
        .landing-card {
          background: var(--surface);
          border: 1px solid var(--border);
          border-radius: 18px;
          padding: 28px 24px;
          box-shadow: var(--shadow-sm);
          transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
          display: flex;
          flex-direction: column;
          gap: 14px;
          position: relative;
          overflow: hidden;
        }
        .landing-card:hover {
          transform: translateY(-4px);
          box-shadow: 0 14px 32px rgba(0,0,0,0.16);
          border-color: var(--border-focus);
        }
        .landing-card-header {
          display: flex;
          align-items: center;
          gap: 14px;
        }
        .landing-card-icon-box {
          width: 46px;
          height: 46px;
          border-radius: 12px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 22px;
          flex-shrink: 0;
        }
        .card-blue .landing-card-icon-box {
          background: rgba(37, 99, 235, 0.12);
          border: 1px solid rgba(37, 99, 235, 0.25);
        }
        .card-purple .landing-card-icon-box {
          background: rgba(147, 51, 234, 0.12);
          border: 1px solid rgba(147, 51, 234, 0.25);
        }
        .card-cyan .landing-card-icon-box {
          background: rgba(16, 185, 129, 0.12);
          border: 1px solid rgba(16, 185, 129, 0.25);
        }
        .landing-card-title {
          font-size: 17px;
          font-weight: 800;
          color: var(--text);
          margin: 0;
          line-height: 1.3;
        }
        .landing-card-desc {
          font-size: 13.5px;
          color: var(--text-secondary);
          line-height: 1.55;
          margin: 0;
        }
        .landing-card-tags {
          display: flex;
          gap: 8px;
          flex-wrap: wrap;
          margin-top: auto;
          padding-top: 8px;
        }
        .landing-tag {
          font-size: 11px;
          font-weight: 700;
          padding: 4px 10px;
          border-radius: var(--radius-pill);
          background: var(--surface-2);
          color: var(--text-muted);
          border: 1px solid var(--border-light);
        }

        /* Footer */
        .landing-footer {
          padding: 16px 24px;
          text-align: center;
          background: var(--surface);
          border-top: 1px solid var(--border-light);
          font-size: 12px;
          color: var(--text-muted);
          box-sizing: border-box;
          margin-top: auto;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        @media (max-width: 900px) {
          .cards-grid {
            grid-template-columns: 1fr;
            gap: 16px;
          }
          .hero-section {
            padding: 32px 16px 24px;
          }
          .features-section {
            padding: 16px 16px 40px;
          }
        }
      ` }} />

      {/* Top Navigation Bar */}
      <header className="landing-header">
        <div className="header-inner">
          <Link href="/" className="brand-container">
            <Image src="/logo.png" alt="YASHCOM Logo" width={28} height={28} style={{ borderRadius: '50%', objectFit: 'cover' }} priority />
            <span className="brand-name">YASHCOM — LEARN OS</span>
          </Link>
          
          <div>
            <Link href="?login=true" className="btn-pill-login">
              Login →
            </Link>
          </div>
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
              <div className="landing-card-icon-box">🎯</div>
              <h3 className="landing-card-title">Adaptive Practice Engine</h3>
            </div>
            <p className="landing-card-desc">
              Dynamic topic-level question pools with intelligent recovery cycles, automated cooldowns, and mistake-analysis.
            </p>
            <div className="landing-card-tags">
              <span className="landing-tag">⚡ Instant Recovery</span>
              <span className="landing-tag">🎯 Dynamic Difficulty</span>
            </div>
          </div>

          {/* Card 2: Purple Accent Card */}
          <div className="landing-card card-purple">
            <div className="landing-card-header">
              <div className="landing-card-icon-box">⚡</div>
              <h3 className="landing-card-title">Learning Quotient (LQ)</h3>
            </div>
            <p className="landing-card-desc">
              Real-time multi-dimensional scoring that measures mastery, consistency, effort, and integrity instead of raw marks.
            </p>
            <div className="landing-card-tags">
              <span className="landing-tag">🧠 SRS Retention</span>
              <span className="landing-tag">📈 Multi-Dimensional</span>
            </div>
          </div>

          {/* Card 3: Cyan Accent Card */}
          <div className="landing-card card-cyan">
            <div className="landing-card-header">
              <div className="landing-card-icon-box">🤝</div>
              <h3 className="landing-card-title">5-Min Daily Parent Sync</h3>
            </div>
            <p className="landing-card-desc">
              Structured nightly review rituals bringing parents, students, and teachers together on a shared progress ledger.
            </p>
            <div className="landing-card-tags">
              <span className="landing-tag">📸 Verified Proof</span>
              <span className="landing-tag">🛡️ Full Visibility</span>
            </div>
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
