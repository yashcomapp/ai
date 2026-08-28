importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.12.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyAV2-YqCyBURq2uzB-X8vJnAGpZQSj3SVg",
  authDomain: "ai-yashcom.firebaseapp.com",
  projectId: "ai-yashcom",
  storageBucket: "ai-yashcom.firebasestorage.app",
  messagingSenderId: "236075352424",
  appId: "1:236075352424:web:665d88c97bdf117cfe56dd"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  
  const actions = [];
  if (payload.data?.type === 'practice_review_pending' || payload.data?.type === 'review_pending') {
    actions.push({
      action: 'approve_practice',
      title: '✅ Approve'
    });
  }

  const notificationTitle = payload.data?.title || payload.notification?.title || 'YASHCOM';
  const notificationOptions = {
    body: payload.data?.body || payload.notification?.body || '',
    badge: '/icons/badge-96.png?v=4',
    color: '#1e3a8a',
    data: payload.data || {},
    actions: actions
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  if (event.action === 'approve_practice') {
    const reviewId = event.notification.data?.reviewId;
    if (reviewId) {
      event.waitUntil(
        fetch('/api/parent/review', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ reviewId, action: 'approve', reviewedByActor: 'parent' })
        }).then(res => {
          if (res.ok) {
            return self.registration.showNotification('YASHCOM', {
              body: '✅ Practice review approved successfully!',
              badge: '/icons/badge-96.png?v=4',
              color: '#1e3a8a'
            });
          }
        }).catch(err => {
          console.error('Failed to auto-approve practice via notification action:', err);
        })
      );
      return;
    }
  }

  // Default click opens parent review page
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if (client.url.includes('/parent') && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow('/parent/review');
      }
    })
  );
});

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});
