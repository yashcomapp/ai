'use client';

import { useEffect } from 'react';
import { KATEX_AUTO_RENDER_OPTIONS, preprocessMathText } from '@/lib/questionTypes';

let katexLoadPromise: Promise<void> | null = null;

function loadKatexAssets(): Promise<void> {
  if (katexLoadPromise) return katexLoadPromise;

  katexLoadPromise = new Promise<void>((resolve, reject) => {
    if (typeof window === 'undefined') {
      resolve();
      return;
    }
    const win = window as any;
    if (win.renderMathInElement) {
      resolve();
      return;
    }

    // 1. Load KaTeX Stylesheet
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css';
    document.head.appendChild(link);

    // 2. Load KaTeX Core JS
    const scriptKatex = document.createElement('script');
    scriptKatex.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js';
    scriptKatex.async = true;
    scriptKatex.onload = () => {
      // 3. Load mhchem extension
      const scriptMhchem = document.createElement('script');
      scriptMhchem.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/mhchem.min.js';
      scriptMhchem.async = true;
      scriptMhchem.onload = () => {
        // 4. Load Auto-Render extension
        const scriptAuto = document.createElement('script');
        scriptAuto.src = 'https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js';
        scriptAuto.async = true;
        scriptAuto.onload = () => {
          resolve();
        };
        scriptAuto.onerror = (e) => reject(new Error('Failed to load KaTeX auto-render: ' + e));
        document.head.appendChild(scriptAuto);
      };
      scriptMhchem.onerror = (e) => reject(new Error('Failed to load KaTeX mhchem: ' + e));
      document.head.appendChild(scriptMhchem);
    };
    scriptKatex.onerror = (e) => reject(new Error('Failed to load KaTeX core script: ' + e));
    document.head.appendChild(scriptKatex);
  });

  return katexLoadPromise;
}

export function useMathRender(dependencyArray: any[] = []) {
  useEffect(() => {
    let active = true;
    let observer: MutationObserver | null = null;
    let t: any = null;
    let t2: any = null;

    const runAutoRender = () => {
      if (!active) return;
      try {
        const win = window as any;
        if (win.renderMathInElement) {
          // Temporarily disconnect the observer to avoid infinite mutation loops during math rendering
          if (observer) {
            observer.disconnect();
          }

          const containers = document.querySelectorAll('.math-container, [data-math="true"]');
          containers.forEach((container: any) => {
            // Avoid re-rendering if it already contains parsed KaTeX elements
            if (container.querySelector('.katex')) {
              return;
            }

            const walk = document.createTreeWalker(
              container,
              NodeFilter.SHOW_TEXT,
              null
            );
            let node;
            while ((node = walk.nextNode())) {
              if (node.parentElement && (node.parentElement.closest('.katex') || node.parentElement.closest('svg'))) {
                continue;
              }
              let text = node.nodeValue || '';
              if (text) {
                let newText = preprocessMathText(text);
                if (newText !== text) {
                  node.nodeValue = newText;
                }
              }
            }

            // Render math inside this container specifically rather than scanning document.body
            win.renderMathInElement(container, KATEX_AUTO_RENDER_OPTIONS);
            container.dataset.rendered = 'true';
          });

          // Reconnect the observer
          if (observer && active) {
            observer.observe(document.body, {
              childList: true,
              subtree: true
            });
          }
        }
      } catch (err) {
        console.warn('Auto-render math failed:', err);
      }
    };

    loadKatexAssets().then(() => {
      if (!active) return;
      runAutoRender();
      t = setTimeout(runAutoRender, 150);
      t2 = setTimeout(runAutoRender, 400);

      // Setup MutationObserver to watch for dynamic DOM insertions/updates (e.g. modals opening, API loads)
      // Strictly ignore timer ticks, audio level changes, or mutations without .math-container
      if (typeof window !== 'undefined' && typeof MutationObserver !== 'undefined') {
        let timeoutId: any = null;
        observer = new MutationObserver((mutations) => {
          try {
            let hasRelevantNode = false;
            for (let i = 0; i < mutations.length; i++) {
              const m = mutations[i];
              if (m.type === 'childList' && m.addedNodes) {
                for (let j = 0; j < m.addedNodes.length; j++) {
                  const node = m.addedNodes[j] as any;
                  if (node && node.nodeType === 1) {
                    const hasClass = typeof node.classList?.contains === 'function' && node.classList.contains('math-container');
                    const hasChild = typeof node.querySelector === 'function' && node.querySelector('.math-container') !== null;
                    if (hasClass || hasChild) {
                      hasRelevantNode = true;
                      break;
                    }
                  }
                }
              }
              if (hasRelevantNode) break;
            }

            if (!hasRelevantNode) return;

            if (timeoutId) clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
              try {
                runAutoRender();
              } catch (e) {
                console.warn('[useMathRender] auto render error:', e);
              }
            }, 80);
          } catch (e) {
            // Never let mutation inspection crash the app
            console.warn('[useMathRender] observer callback error:', e);
          }
        });
        observer.observe(document.body, {
          childList: true,
          subtree: true
        });
      }
    }).catch((err) => {
      console.warn('Failed to load KaTeX assets dynamically:', err);
    });

    return () => {
      active = false;
      if (t) clearTimeout(t);
      if (t2) clearTimeout(t2);
      if (observer) {
        observer.disconnect();
      }
    };
  }, dependencyArray);
}
