import * as admin from 'firebase-admin';

const projectId = process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID || "ai-yashcom";

if (!admin.apps.length) {
  const serviceAccount = process.env.FIREBASE_SERVICE_ACCOUNT_KEY;
  
  if (serviceAccount) {
    try {
      const credential = JSON.parse(
        serviceAccount.startsWith('{')
          ? serviceAccount
          : Buffer.from(serviceAccount, 'base64').toString('utf-8')
      );
      admin.initializeApp({
        credential: admin.credential.cert(credential),
        databaseURL: `https://${projectId}-default-rtdb.asia-southeast1.firebasedatabase.app/`
      });
      console.log("Firebase Admin SDK initialized successfully via service account cert.");
    } catch (err: any) {
      console.error("Error parsing FIREBASE_SERVICE_ACCOUNT_KEY, falling back to projectId init:", err.message);
      admin.initializeApp({
        projectId: projectId,
        databaseURL: `https://${projectId}-default-rtdb.asia-southeast1.firebasedatabase.app/`
      });
    }
  } else {
    console.warn("FIREBASE_SERVICE_ACCOUNT_KEY env variable is missing. Initializing admin with projectId only.");
    admin.initializeApp({
      projectId: projectId,
      databaseURL: `https://${projectId}-default-rtdb.asia-southeast1.firebasedatabase.app/`
    });
  }
}

const adminDb = admin.firestore();
const adminAuth = admin.auth();

export { adminDb, adminAuth };
