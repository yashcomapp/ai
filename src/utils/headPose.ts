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

/**
 * Intelligent Heuristic for Second Mobile Phone / Secondary Screen Usage
 * Distinguishes between legitimate downward rough work vs. phone operation:
 * 1. Deep or sustained chin-down posture where screen/camera is aimed at desk/lap
 * 2. Unnatural rigid hand/wrist occlusion near chin or lower camera frame
 * 3. Extreme asymmetrical yaw combined with downward tilt (whispering/looking at hidden device)
 */
export interface DeviceSuspicionAssessment {
  isSuspicious: boolean;
  confidence: number; // 0 to 1
  reason: string;
}

export function assessSecondaryDeviceRisk(
  pose: HeadPose | null,
  landmarks: any[] | null,
  chinDownDurationMs: number,
  isNumerical: boolean
): DeviceSuspicionAssessment {
  if (!pose) {
    return { isSuspicious: false, confidence: 0, reason: '' };
  }

  // 1. Sustained Deep Chin-Down Desk Gaze (Operating phone on lap or table)
  // Honest rough work has natural micro-head oscillations (as pen writes); phone watching is static & frozen.
  const isDeepChinDown = pose.pitch > 16.5;
  const isExtremeChinDown = pose.pitch > 22.0;

  // Numerical tests allow more rough work time (e.g. 8-10s), but non-numerical shouldn't stay frozen chin-down for >4s
  const chinDownThreshold = isNumerical ? 8000 : 4500;
  if ((isExtremeChinDown && chinDownDurationMs > 3500) || (isDeepChinDown && chinDownDurationMs > chinDownThreshold)) {
    return {
      isSuspicious: true,
      confidence: 0.88,
      reason: `Sustained downward screen gaze (${Math.round(chinDownDurationMs / 1000)}s) - potential second phone on lap or desk`
    };
  }

  // 2. Off-Center Downward Glance (Device hidden to side of keyboard/screen)
  const isCornerGlance = Math.abs(pose.yaw) > 18.0 && pose.pitch > 12.0;
  if (isCornerGlance && chinDownDurationMs > 3000) {
    return {
      isSuspicious: true,
      confidence: 0.82,
      reason: 'Off-axis downward angle - potential secondary device to side of screen'
    };
  }

  // 3. Lower Face / Chin Occlusion (Hand raised holding second phone in front of camera/screen)
  if (landmarks && landmarks.length > 200) {
    const chin = landmarks[152];
    const lowerLip = landmarks[17];
    const nose = landmarks[1];
    if (chin && lowerLip && nose) {
      // If landmarks around chin/mouth collapse or get occluded by a raised object
      const lipToChinDist = Math.hypot(chin.x - lowerLip.x, chin.y - lowerLip.y);
      const noseToLipDist = Math.hypot(lowerLip.x - nose.x, lowerLip.y - nose.y);
      if (lipToChinDist < 0.008 || (lipToChinDist / (noseToLipDist || 0.01)) < 0.35) {
        return {
          isSuspicious: true,
          confidence: 0.79,
          reason: 'Lower face/chin occlusion detected - raised hand or device near screen'
        };
      }
    }
  }

  return { isSuspicious: false, confidence: 0, reason: '' };
}
