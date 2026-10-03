export class FetchError extends Error {
  status?: number;
  info?: any;

  constructor(message: string, status?: number, info?: any) {
    super(message);
    this.name = 'FetchError';
    this.status = status;
    this.info = info;
  }
}

export async function fetchWithToken(url: string, firebaseUser: any) {
  if (!firebaseUser) return null;
  const idToken = await firebaseUser.getIdToken();
  const res = await fetch(url, {
    headers: {
      'Authorization': `Bearer ${idToken}`
    }
  });
  if (!res.ok) {
    const errData = await res.json().catch(() => ({}));
    const errorMessage = errData.message || errData.error || `Failed to fetch data from ${url} (Status: ${res.status})`;
    throw new FetchError(errorMessage, res.status, errData);
  }
  return res.json();
}
