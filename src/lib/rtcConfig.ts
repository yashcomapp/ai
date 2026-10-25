/**
 * Real-Time Communications (WebRTC) Configuration SSOT.
 * Reads STUN/TURN configuration from environment variables with fallback STUN servers.
 */

export function getRTCConfiguration(): RTCConfiguration {
  const turnServer = process.env.NEXT_PUBLIC_TURN_SERVER_URL;
  const turnUsername = process.env.NEXT_PUBLIC_TURN_USERNAME;
  const turnCredential = process.env.NEXT_PUBLIC_TURN_CREDENTIAL;

  const iceServers: RTCIceServer[] = [
    { urls: ['stun:stun.l.google.com:19302', 'stun:stun1.l.google.com:19302'] }
  ];

  if (turnServer) {
    const turnEntry: RTCIceServer = { urls: turnServer };
    if (turnUsername) turnEntry.username = turnUsername;
    if (turnCredential) turnEntry.credential = turnCredential;
    iceServers.push(turnEntry);
  } else {
    // Default fallback TURN servers
    iceServers.push(
      {
        urls: 'turn:openrelay.metered.ca:80',
        username: 'openrelayproject',
        credential: 'openrelayproject'
      },
      {
        urls: 'turn:openrelay.metered.ca:443',
        username: 'openrelayproject',
        credential: 'openrelayproject'
      }
    );
  }

  return { iceServers };
}

export const RTC_CONFIG: RTCConfiguration = getRTCConfiguration();
