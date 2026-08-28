import crypto from 'crypto';

const ALGORITHM = 'aes-256-cbc';
// Safe fallback key for local dev if env is not defined (must be exactly 32 bytes)
const IV_LENGTH = 16; 

function getEncryptionKey(): string {
  const key = process.env.ENCRYPTION_KEY;
  if (process.env.NODE_ENV === 'production') {
    if (!key || key === 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6') {
      console.warn('⚠️ WARNING: ENCRYPTION_KEY environment variable is missing or insecure in production mode. Using default fallback key.');
    }
  }
  return key || 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6';
}

export function encrypt(text: string): string {
  if (!text) return '';
  const key = getEncryptionKey();
  const iv = crypto.randomBytes(IV_LENGTH);
  const cipher = crypto.createCipheriv(ALGORITHM, Buffer.from(key), iv);
  let encrypted = cipher.update(text);
  encrypted = Buffer.concat([encrypted, cipher.final()]);
  return iv.toString('hex') + ':' + encrypted.toString('hex');
}

export function decrypt(text: string): string {
  if (!text) return '';
  try {
    const textParts = text.split(':');
    if (textParts.length < 2) {
      // Not encrypted format (legacy plain text registrations fallback)
      return text;
    }
    const iv = Buffer.from(textParts.shift()!, 'hex');
    const encryptedText = Buffer.from(textParts.join(':'), 'hex');
    const key = getEncryptionKey();
    const decipher = crypto.createDecipheriv(ALGORITHM, Buffer.from(key), iv);
    let decrypted = decipher.update(encryptedText);
    decrypted = Buffer.concat([decrypted, decipher.final()]);
    return decrypted.toString();
  } catch (err) {
    console.error('Failed to decrypt password, throwing error to prevent credentials exposure:', err);
    throw new Error('Decryption Failed: Insecure or corrupted ciphertext data.');
  }
}
