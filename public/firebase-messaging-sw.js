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
  
  const data = payload.data || {};
  const actions = [];
  if (data.type === 'practice_review_pending' || data.type === 'review_pending') {
    actions.push({
      action: 'approve_practice',
      title: '✅ Approve'
    });
  }

  const notificationTitle = data.title || payload.notification?.title || 'YASHCOM';
  const notificationOptions = {
    body: data.body || payload.notification?.body || '',
    badge: '/icons/badge-96.png?v=4',
    icon: '/icons/icon-192.png',
    color: '#d97b38',
    data: data,
    tag: data.roomId || data.type || 'yashcom-notification',
    renotify: true,
    actions: actions
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  const data = event.notification.data || {};

  // Quick inline approve action for parents
  if (event.action === 'approve_practice') {
    const reviewId = data.reviewId;
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
              icon: '/icons/icon-192.png',
              color: '#d97b38'
            });
          }
        }).catch(err => {
          console.error('Failed to auto-approve practice via notification action:', err);
        })
      );
      return;
    }
  }

  // Resolve target deep link URL from notification payload
  let targetUrl = data.url;
  if (!targetUrl) {
    if (data.type === 'chat_message' && data.roomId) {
      targetUrl = `/chat?room=${encodeURIComponent(data.roomId)}`;
    } else if (data.type === 'practice_review_pending' || data.type === 'review_pending') {
      targetUrl = '/parent/review';
    } else if (data.type === 'new_exam') {
      targetUrl = data.examId ? `/student/take-exam?examId=${encodeURIComponent(data.examId)}` : '/student';
    } else if (data.type === 'announcement' || data.type === 'absent_notice') {
      targetUrl = '/student/notifications';
    } else {
      targetUrl = '/';
    }
  }

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      // 1. If an existing app window is open, focus and route it
      for (const client of clientList) {
        if ('focus' in client) {
          client.focus();
          
          let finalUrl = targetUrl;
          if (targetUrl.startsWith('/chat')) {
            const rolePrefix = client.url.includes('/parent') 
              ? '/parent' 
              : client.url.includes('/admin') 
                ? '/admin' 
                : '/student';
            finalUrl = targetUrl.replace(/^\/chat/, `${rolePrefix}/chat`);
          }

          if ('navigate' in client) {
            client.navigate(finalUrl);
          }
          client.postMessage({
            type: 'SELECT_CHAT_ROOM',
            roomId: data.roomId,
            url: finalUrl,
            data: data
          });
          return;
        }
      }

      // 2. If no window is open, launch a new window with the destination URL
      let finalOpenUrl = targetUrl;
      if (targetUrl.startsWith('/chat')) {
        finalOpenUrl = '/chat' + targetUrl.slice(5);
      }
      if (clients.openWindow) {
        return clients.openWindow(finalOpenUrl);
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
