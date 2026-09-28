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
    throw new Error(errData.message || `Failed to fetch data from ${url}`);
  }
  return res.json();
}
