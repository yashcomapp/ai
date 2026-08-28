import React, { Suspense } from 'react';
import Link from 'next/link';
import LoginModal from '@/components/LoginModal';
import Image from 'next/image';
import { Outfit } from 'next/font/google';

const outfit = Outfit({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-outfit',
});

export default function LoginPage() {
  return (
    <div className={`landing-shell ${outfit.variable}`}>
      <style dangerouslySetInnerHTML={{ __html: `
        .landing-shell {
          font-family: var(--font-outfit), sans-serif;
          background-color: #1a1e24;
          background-image: linear-gradient(rgba(26, 30, 36, 0.7), rgba(26, 30, 36, 0.8)), url('/chalkboard.webp');
          background-size: cover;
          background-position: center;
          background-repeat: no-repeat;
          background-attachment: scroll;
          color: #f1f5f9;
          min-height: 100vh;
          display: flex;
          flex-direction: column;
          margin: 0;
          padding: 0;
          box-sizing: border-box;
          justify-content: flex-start;
          gap: 24px;
          transition: background-color 0.3s ease, color 0.3s ease;

          --bg-color: transparent;
          --text-color: #f1f5f9;
          --bg-grad: linear-gradient(rgba(26, 30, 36, 0.7), rgba(26, 30, 36, 0.8)), url('/chalkboard.webp');
          --card-bg: rgba(30, 41, 59, 0.45);
          --card-border: rgba(255, 255, 255, 0.15);
          --accent-grad: linear-gradient(135deg, #cbd5e1, #94a3b8);
          --text-accent: #e2e8f0;
          --icon-color: #cbd5e1;
          --text-sub: #e2e8f0;
          --btn-shadow: rgba(255, 255, 255, 0.05);
          --badge-bg: rgba(255, 255, 255, 0.08);
          --badge-border: rgba(255, 255, 255, 0.1);
          --badge-text: #f1f5f9;
          --badge-dot: #ffffff;
        }

        /* Header Style */
        .landing-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 10px 24px;
          background: rgba(26, 30, 36, 0.45);
          border-bottom: 1px solid var(--card-border);
          backdrop-filter: blur(8px);
          box-sizing: border-box;
          height: 54px;
          transition: border-color 0.3s ease;
        }
        .brand-container {
          display: flex;
          align-items: center;
          gap: 8px;
          text-decoration: none;
          color: var(--text-color);
        }
        .brand-name {
          font-family: var(--font-outfit), sans-serif;
          font-size: 15px;
          font-weight: 800;
          letter-spacing: 1px;
        }
        .btn-pill {
          background: var(--accent-grad);
          color: #ffffff;
          border: none;
          padding: 8px 18px;
          border-radius: 30px;
          font-weight: 600;
          font-size: 13px;
          cursor: pointer;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
          box-shadow: 0 4px 10px var(--btn-shadow);
        }
        .btn-pill:hover {
          transform: translateY(-1px);
          box-shadow: 0 6px 14px var(--btn-shadow);
        }

        /* Hero Section */
        .hero-section {
          background: transparent;
          color: #ffffff;
          padding: 40px 20px 0px;
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items: center;
          box-sizing: border-box;
          transition: background 0.3s ease;
          position: relative;
          overflow: hidden;
        }
        .hero-title {
          font-family: var(--font-outfit), sans-serif;
          font-size: 54px;
          font-weight: 700;
          line-height: 1.25;
          max-width: 750px;
          margin: 0 0 12px;
          color: rgba(255, 255, 255, 0.95);
          text-shadow: 0 0 2px rgba(255, 255, 255, 0.4), 0 0 6px rgba(255, 255, 255, 0.2);
          letter-spacing: 0.5px;
        }
        .hero-desc {
          font-size: 14pt;
          font-weight: 400;
          max-width: 680px;
          margin: 0 0 20px;
          opacity: 0.9;
          line-height: 1.5;
          color: var(--text-sub);
        }

        /* Feature Section */
        .features-section {
          padding: 0px 24px 30px;
          text-align: center;
          background-color: var(--bg-color);
          box-sizing: border-box;
          transition: background-color 0.3s ease;
        }
        .features-heading {
          font-family: var(--font-outfit), sans-serif;
          font-size: 40px;
          font-weight: 700;
          color: rgba(255, 255, 255, 0.95);
          line-height: 1.25;
          margin: 0;
          text-shadow: 0 0 2px rgba(255, 255, 255, 0.4), 0 0 6px rgba(255, 255, 255, 0.2);
        }
        .cards-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 16px;
          max-width: 1000px;
          margin: 16px auto 0;
        }
        .feature-card {
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: 16px;
          padding: 16px 20px;
          box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
          text-align: left;
          box-sizing: border-box;
          transition: background 0.3s ease, border-color 0.3s ease;
        }
        .feature-card:hover {
          transform: translateY(-2px);
          box-shadow: 0 12px 30px var(--btn-shadow);
        }
        .card-title {
          font-family: var(--font-outfit), sans-serif;
          font-size: 26px;
          font-weight: 800;
          color: var(--text-accent);
          margin-bottom: 6px;
        }
        .card-desc {
          font-size: 13pt;
          color: var(--text-sub);
          line-height: 1.4;
        }

        /* Footer */
        .landing-footer {
          padding: 12px 24px;
          text-align: center;
          background: var(--bg-color);
          border-top: 1px solid var(--card-border);
          font-size: 11pt;
          color: var(--text-sub);
          box-sizing: border-box;
          height: 38px;
          transition: background-color 0.3s ease, border-color 0.3s ease;
          margin-top: auto;
        }

        /* Floating Login Modal Dialog Overlay */
        .login-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(11, 16, 32, 0.65);
          backdrop-filter: blur(8px);
          display: flex;
          align-items: center;
          justify-content: center;
          z-index: 9999;
          animation: fadeIn 0.25s ease-out;
        }
        .login-modal {
          background: var(--card-bg);
          padding: 30px;
          border-radius: 24px;
          box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
          width: 100%;
          max-width: 400px;
          border: 1px solid var(--card-border);
          position: relative;
          box-sizing: border-box;
          animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .close-btn {
          position: absolute;
          top: 16px;
          right: 16px;
          background: none;
          border: none;
          font-size: 20px;
          cursor: pointer;
          color: var(--text-sub);
        }

        .login-modal h2 {
          font-family: var(--font-outfit), sans-serif;
          font-size: 20px;
          font-weight: 800;
          margin: 0;
          color: #ffffff;
          letter-spacing: 0.5px;
        }
        .login-modal .subtitle {
          font-size: 12px;
          color: var(--text-sub);
          margin-bottom: 18px;
          text-align: center;
        }
        .form-group {
          margin-bottom: 14px;
          text-align: left;
        }
        .form-group label {
          display: block;
          font-size: 11px;
          font-weight: 600;
          color: var(--text-sub);
          margin-bottom: 4px;
          text-transform: uppercase;
          letter-spacing: 0.5px;
        }
        .form-group input {
          width: 100%;
          padding: 10px 14px;
          border: 1.5px solid var(--card-border);
          border-radius: 10px;
          background-color: var(--bg-color);
          font-family: inherit;
          font-size: 13px;
          color: var(--text-color);
          box-sizing: border-box;
        }
        .form-group input:focus {
          outline: none;
          border-color: var(--accent);
        }
        .role-badges {
          display: flex;
          justify-content: center;
          gap: 6px;
          margin-bottom: 14px;
        }
        .role-pill {
          background-color: var(--bg-color);
          border: 1px solid var(--card-border);
          color: var(--text-accent);
          font-size: 10px;
          font-weight: 600;
          padding: 3px 8px;
          border-radius: 20px;
        }
        .btn-block {
          width: 100%;
          padding: 10px;
          border-radius: 10px;
          font-weight: 700;
          font-size: 14px;
        }

        /* Animations */
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes slideUp {
          from { transform: translateY(20px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }

        /* Responsive Design Media Queries */
        @media (max-width: 768px) {
          .landing-shell {
            height: auto;
            max-height: none;
            overflow: auto;
            background-attachment: scroll !important;
            background-size: cover !important;
            background-repeat: repeat-y !important;
            background-position: top center !important;
            gap: 16px !important;
          }
          .hero-section {
            padding: 20px 16px 0px !important;
          }
          .hero-title {
            font-size: 32px !important;
            margin-bottom: 8px !important;
          }
          .hero-desc {
            font-size: 13pt !important;
            margin-bottom: 12px !important;
            line-height: 1.4 !important;
          }
          .features-heading {
            font-size: 26px !important;
          }
          .cards-grid {
            grid-template-columns: 1fr;
            gap: 10px !important;
            margin-top: 12px !important;
          }
          .feature-card {
            padding: 14px 16px !important;
          }
          .card-title {
            font-size: 20px !important;
            margin-bottom: 4px !important;
          }
          .card-desc {
            font-size: 12pt !important;
            line-height: 1.4 !important;
          }
          .features-section {
            padding: 0px 16px 20px !important;
          }
          .login-modal {
            padding: 20px;
            margin: 16px;
          }
        }
      ` }} />

      {/* Header Navigation */}
      <header className="landing-header">
        <Link href="#" className="brand-container">
          <Image src="/logo.png" alt="YASHCOM Logo" width={28} height={28} style={{ borderRadius: '50%', objectFit: 'cover' }} priority />
          <span className="brand-name">YASHCOM - LEARN OS</span>
        </Link>
        
        <div className="header-actions-group">
          <Link href="?login=true" className="btn-pill" style={{ textDecoration: 'none' }}>
            Login
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero-section">
        <h1 className="hero-title">Learning, Reimagined for Every Mind</h1>
        <p className="hero-desc">
          The world's first AI-powered Learning Operating System — built to help every student learn and excel in their own unique way.
        </p>
      </section>

      {/* Feature / Stats Cards Section */}
      <section id="features" className="features-section">
        <h2 className="features-heading">
          Every student learns <em style={{ fontStyle: 'italic' }}>differently.</em>
        </h2>
        <h2 className="features-heading" style={{ color: 'var(--text-accent)', marginTop: '2px' }}>Until now, education didn't.</h2>

        <div className="cards-grid">
          <div className="feature-card">
            <div className="card-title">1 Billion+</div>
            <div className="card-desc">learners underserved by one-size-fits-all education globally.</div>
          </div>
          <div className="feature-card">
            <div className="card-title">Your style.</div>
            <div className="card-desc">Your style is unique — your operating system should be too.</div>
          </div>
          <div className="feature-card">
            <div className="card-title">AI for you.</div>
            <div className="card-desc">AI that adapts to YOU, not the other way around. Live diagnostics.</div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="landing-footer" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '6px' }}>
        <p>© 2026 Yashcom LearnOS. Empowering different minds to learn and grow.</p>
      </footer>

      {/* Suspended Client-side login modal overlay */}
      <Suspense fallback={null}>
        <LoginModal />
      </Suspense>
    </div>
  );
}
