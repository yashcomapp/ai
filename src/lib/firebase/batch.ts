import * as admin from 'firebase-admin';

export class ChunkedBatch {
  private db: admin.firestore.Firestore;
  private currentBatch: admin.firestore.WriteBatch;
  private opCount: number = 0;
  private commitPromises: Promise<any>[] = [];

  constructor(db: admin.firestore.Firestore) {
    this.db = db;
    this.currentBatch = db.batch();
  }

  delete(ref: admin.firestore.DocumentReference) {
    this.currentBatch.delete(ref);
    this.incrementOps();
    return this;
  }

  set(ref: admin.firestore.DocumentReference, data: any, options?: admin.firestore.SetOptions) {
    if (options) {
      this.currentBatch.set(ref, data, options);
    } else {
      this.currentBatch.set(ref, data);
    }
    this.incrementOps();
    return this;
  }

  update(ref: admin.firestore.DocumentReference, data: any) {
    this.currentBatch.update(ref, data);
    this.incrementOps();
    return this;
  }

  private incrementOps() {
    this.opCount++;
    if (this.opCount >= 400) {
      this.commitPromises.push(this.currentBatch.commit());
      this.currentBatch = this.db.batch();
      this.opCount = 0;
    }
  }

  async commit(): Promise<void> {
    if (this.opCount > 0) {
      this.commitPromises.push(this.currentBatch.commit());
    }
    await Promise.all(this.commitPromises);
  }
}
