import type { Metadata, Viewport } from 'next';
import { Inter } from 'next/font/google';
import '@/styles/theme.css';
import '@/styles/components.css';
import { ThemeProvider } from '@/context/ThemeContext';
import { AuthProvider } from '@/context/AuthContext';
import Script from 'next/script';

import TimeTracker from '@/components/TimeTracker';
import PushNotificationManager from '@/components/PushNotificationManager';
import ToastContainer from '@/components/ToastContainer';
import { SpeedInsights } from '@vercel/speed-insights/next';

const inter = Inter({ 
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export const viewport: Viewport = {
  themeColor: '#0d0f12',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  viewportFit: 'cover',
};

export const metadata: Metadata = {
  title: 'YASHCOM Learning OS - Dashboard',
  description: 'AI Powered Learning Journey and Exam System',
  manifest: '/manifest.json',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" data-theme="dark" className={`${inter.variable} dark`}>
      <head>
        <link rel="manifest" href="/manifest.json" />
        <meta name="theme-color" content="#0d0f12" />
        <link rel="icon" href="/icons/favicon-32.png?v=2" sizes="32x32" />
        <link rel="apple-touch-icon" href="/icons/apple-touch-icon.png?v=2" />
        <meta name="mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        <meta name="apple-mobile-web-app-title" content="YASHCOM-LOS" />
        {/* KaTeX stylesheet and scripts are loaded dynamically on demand in useMathRender hook to optimize LCP/FCP of other pages */}
      </head>
      <body>
        <Script id="register-sw" strategy="lazyOnload">
          {`
            if ('serviceWorker' in navigator) {
              window.addEventListener('load', function() {
                navigator.serviceWorker.register('/sw.js').then(function(reg) {
                  console.log('Service Worker registered successfully:', reg.scope);
                }).catch(function(err) {
                  console.warn('Service Worker registration failed:', err);
                });
              });
            }
          `}
        </Script>
        <ThemeProvider>
          <AuthProvider>
            <TimeTracker />
            <PushNotificationManager />
            <ToastContainer />
            <div className="app-shell">
              {children}
            </div>
            <SpeedInsights />
          </AuthProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
