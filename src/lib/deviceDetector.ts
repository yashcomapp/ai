/**
 * Light-weight Client-Side Secondary Device (Cell Phone) Detection Engine
 * 
 * Dynamically loads TensorFlow.js + COCO-SSD from trusted high-speed CDN on demand.
 * Runs non-blocking background inference on the webcam stream every 1.5 - 2.5 seconds.
 * Triggers an instant snapshot when an unauthorized mobile phone, camera, or tablet is sighted.
 */

export interface DetectedObject {
  class: string;
  score: number;
  bbox: [number, number, number, number]; // [x, y, width, height]
}

export interface DeviceDetectionResult {
  hasPhone: boolean;
  score: number;
  detectedObjects: DetectedObject[];
}

let cocoModelPromise: Promise<any> | null = null;
let isScriptLoading = false;

// Target classes representing cheating devices
const SECONDARY_DEVICE_CLASSES = new Set([
  'cell phone',
  'remote',
  'book', // notes/books held up to camera
  'laptop'
]);

/**
 * Dynamically injects script tag if not already loaded in window
 */
function loadScriptAsync(src: string): Promise<void> {
  return new Promise((resolve, reject) => {
    if (typeof window === 'undefined') return resolve();
    const existing = document.querySelector(`script[src="${src}"]`);
    if (existing) {
      if ((existing as any).dataset.loaded === 'true') {
        return resolve();
      }
      existing.addEventListener('load', () => resolve());
      existing.addEventListener('error', (e) => reject(e));
      return;
    }

    const script = document.createElement('script');
    script.src = src;
    script.async = true;
    script.crossOrigin = 'anonymous';
    script.onload = () => {
      (script as any).dataset.loaded = 'true';
      resolve();
    };
    script.onerror = (e) => reject(e);
    document.head.appendChild(script);
  });
}

/**
 * Initializes and caches the COCO-SSD object detection model
 */
export async function getSecondaryDeviceModel(): Promise<any> {
  if (typeof window === 'undefined') return null;
  const w = window as any;

  if (w.__cocoSsdModel) {
    return w.__cocoSsdModel;
  }

  if (cocoModelPromise) {
    return cocoModelPromise;
  }

  cocoModelPromise = (async () => {
    try {
      // 1. Ensure TensorFlow.js is loaded
      if (!w.tf) {
        await loadScriptAsync('https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.22.0/dist/tf.min.js');
      }

      // 2. Ensure COCO-SSD is loaded
      if (!w.cocoSsd) {
        await loadScriptAsync('https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd@2.2.3/dist/coco-ssd.min.js');
      }

      if (!w.cocoSsd) {
        console.warn('[DeviceDetector] cocoSsd not found on window after loading scripts');
        return null;
      }

      // Load lite mobilenet_v2 version for optimal real-time browser performance
      const model = await w.cocoSsd.load({ base: 'mobilenet_v2' });
      w.__cocoSsdModel = model;
      return model;
    } catch (err) {
      console.warn('[DeviceDetector] Failed to load object detection model:', err);
      cocoModelPromise = null;
      return null;
    }
  })();

  return cocoModelPromise;
}

/**
 * Inspects a video element frame for secondary devices (e.g. mobile phones)
 */
export async function detectSecondaryDevice(videoEl: HTMLVideoElement | null): Promise<DeviceDetectionResult> {
  if (!videoEl || videoEl.readyState < 2 || videoEl.videoWidth === 0 || videoEl.videoHeight === 0) {
    return { hasPhone: false, score: 0, detectedObjects: [] };
  }

  try {
    const model = await getSecondaryDeviceModel();
    if (!model) {
      return { hasPhone: false, score: 0, detectedObjects: [] };
    }

    const predictions: DetectedObject[] = await model.detect(videoEl, 5, 0.45);
    if (!predictions || predictions.length === 0) {
      return { hasPhone: false, score: 0, detectedObjects: [] };
    }

    let topPhoneScore = 0;
    const phoneDetections = predictions.filter(pred => {
      const className = pred.class.toLowerCase();
      if (className === 'cell phone' && pred.score >= 0.50) {
        if (pred.score > topPhoneScore) topPhoneScore = pred.score;
        return true;
      }
      return false;
    });

    return {
      hasPhone: phoneDetections.length > 0,
      score: topPhoneScore,
      detectedObjects: predictions
    };
  } catch (err) {
    console.warn('[DeviceDetector] Error during device frame inference:', err);
    return { hasPhone: false, score: 0, detectedObjects: [] };
  }
}
