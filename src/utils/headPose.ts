export interface HeadPose {
  yaw: number;
  pitch: number;
  roll: number;
}

export const PROCTOR_THRESHOLDS = {
  LOOKING_AWAY: {
    YAW: 20,          // 20 degree side turn (user requested)
    PITCH: 19,        // 19 degree up/down tilt (user requested)
    ROLL: 17,         // 17 degree head tilt (user requested)
    DEBOUNCE_MS: 1500 // 1.5 seconds threshold (faster alert trigger)
  },
  EXCESSIVE_MOVEMENT: {
    YAW: 18,
    PITCH: 16,
    ROLL: 15,
    DEBOUNCE_MS: 1500
  }
};

/**
 * Calculates head pose angles (yaw, pitch, roll) from face landmarks,
 * optionally offset by a resting baseline pose.
 */
export function calculateHeadPose(landmarks: any[], baseline?: HeadPose | null): HeadPose | null {
  if (!landmarks || landmarks.length < 400) return null;

  const NOSE_TIP = 1;
  const LEFT_EYE_OUTER = 33;
  const RIGHT_EYE_OUTER = 263;
  const CHIN = 152;

  const nose = landmarks[NOSE_TIP];
  const leftEye = landmarks[LEFT_EYE_OUTER];
  const rightEye = landmarks[RIGHT_EYE_OUTER];
  const chin = landmarks[CHIN];

  if (!nose || !leftEye || !rightEye || !chin) return null;

  const faceCenterX = (leftEye.x + rightEye.x) / 2;
  const eyeDistance = Math.hypot(leftEye.x - rightEye.x, leftEye.y - rightEye.y) || 0.01;
  const noseToChin = Math.hypot(nose.x - chin.x, nose.y - chin.y) || 0.01;

  const noseOffsetX = nose.x - faceCenterX;
  const noseOffsetY = nose.y - (leftEye.y + rightEye.y) / 2;

  let yaw = (noseOffsetX / eyeDistance) * 60;
  let pitch = (noseOffsetY / noseToChin) * 45;
  let roll = Math.atan2(leftEye.y - rightEye.y, Math.abs(leftEye.x - rightEye.x)) * 180 / Math.PI;

  if (baseline) {
    yaw -= baseline.yaw;
    pitch -= baseline.pitch;
    roll -= baseline.roll;
  }

  return { yaw, pitch, roll };
}

/**
 * Validates whether the student's head pose constitutes looking away
 */
export function checkLookingAway(pose: HeadPose): boolean {
  return Math.abs(pose.yaw) > PROCTOR_THRESHOLDS.LOOKING_AWAY.YAW || 
         Math.abs(pose.pitch) > PROCTOR_THRESHOLDS.LOOKING_AWAY.PITCH || 
         Math.abs(pose.roll) > PROCTOR_THRESHOLDS.LOOKING_AWAY.ROLL;
}

/**
 * Validates whether the student's head movement is excessive relative to a previous pose sample
 */
export function checkExcessiveMovement(pose: HeadPose, lastPose: HeadPose): boolean {
  return Math.abs(pose.yaw - lastPose.yaw) > PROCTOR_THRESHOLDS.EXCESSIVE_MOVEMENT.YAW || 
         Math.abs(pose.pitch - lastPose.pitch) > PROCTOR_THRESHOLDS.EXCESSIVE_MOVEMENT.PITCH || 
         Math.abs(pose.roll - lastPose.roll) > PROCTOR_THRESHOLDS.EXCESSIVE_MOVEMENT.ROLL;
}
