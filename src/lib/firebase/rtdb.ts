import { getDatabase } from 'firebase/database';
import { app } from './client';

let rtdb: any = null;
try {
  rtdb = getDatabase(app, "https://ai-yashcom-default-rtdb.asia-southeast1.firebasedatabase.app/");
} catch (e: any) {
  console.warn("RTDB not available (soft fail):", e.message);
}

export { rtdb };
