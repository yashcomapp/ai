/**
 * scripts/enrich_visual_figures.js
 * 
 * Enriches figure-based questions across Physics, Chemistry, Biology,
 * Mathematics 1 (Algebra), and Mathematics 2 (Geometry) where visual
 * diagrams are pedagogically critical.
 * 
 * Complies with:
 * - Rule Q: Mandatory atomic pre-mutation snapshot of targeted questions
 * - Rule T: 80 questions per leaf subtopic parity preserved
 * - Rule K: Valid KaTeX math formatting
 * - Zero question inflation: updates existing questions in place
 */

const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
const resolver = new dns.Resolver();
resolver.setServers(['8.8.8.8', '1.1.1.1']);
const origLookup = dns.lookup;
dns.lookup = function(hostname, options, callback) {
  if (typeof options === 'function') {
    callback = options;
    options = {};
  }
  if (hostname && (hostname.endsWith('googleapis.com') || hostname.endsWith('google.com'))) {
    return resolver.resolve4(hostname, (err, ips) => {
      if (!err && ips && ips.length > 0) {
        if (options && options.all) {
          return callback(null, ips.map(ip => ({ address: ip, family: 4 })));
        }
        return callback(null, ips[0], 4);
      }
      return origLookup(hostname, options, callback);
    });
  }
  return origLookup(hostname, options, callback);
};

const fs = require('fs');
const path = require('path');
const { registerTsHook } = require('./ts-loader.js');
registerTsHook();
const { adminDb } = require('../src/lib/firebase/admin.ts');

try {
  adminDb.settings({ ignoreUndefinedProperties: true });
} catch (e) {}

// ==========================================
// SVG TEMPLATES
// ==========================================

function wrapSvg(svgContent) {
  return `<div style="display: flex; justify-content: center; margin: 14px 0;">\n${svgContent}\n</div>\n`;
}

// 1. Histogram
const svgHistogram = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="24" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Histogram: Marks Distribution of Students</text>
  <line x1="55" y1="190" x2="390" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="55" y1="45" x2="55" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <text x="390" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Marks (Class Intervals)</text>
  <text x="20" y="45" fill="#94a3b8" font-size="10" font-family="sans-serif" transform="rotate(-90 20 45)" text-anchor="end">Frequency (Students)</text>
  <text x="45" y="194" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">0</text>
  <line x1="50" y1="162" x2="55" y2="162" stroke="#94a3b8" stroke-width="1"/>
  <text x="45" y="165" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">5</text>
  <line x1="50" y1="134" x2="55" y2="134" stroke="#94a3b8" stroke-width="1"/>
  <text x="45" y="137" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">10</text>
  <line x1="50" y1="106" x2="55" y2="106" stroke="#94a3b8" stroke-width="1"/>
  <text x="45" y="109" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">15</text>
  <line x1="50" y1="78" x2="55" y2="78" stroke="#94a3b8" stroke-width="1"/>
  <text x="45" y="81" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">20</text>
  <line x1="50" y1="50" x2="55" y2="50" stroke="#94a3b8" stroke-width="1"/>
  <text x="45" y="53" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">25</text>
  <rect x="55" y="145" width="60" height="45" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
  <text x="85" y="140" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">8</text>
  <rect x="115" y="112" width="60" height="78" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
  <text x="145" y="107" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">14</text>
  <rect x="175" y="67" width="60" height="123" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
  <text x="205" y="62" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">22</text>
  <rect x="235" y="100" width="60" height="90" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
  <text x="265" y="95" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">16</text>
  <rect x="295" y="134" width="60" height="56" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
  <text x="325" y="129" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">10</text>
  <text x="55" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">0</text>
  <text x="115" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">10</text>
  <text x="175" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">20</text>
  <text x="235" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">30</text>
  <text x="295" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">40</text>
  <text x="355" y="204" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">50</text>
</svg>`;

// 2. Frequency Polygon
const svgFreqPolygon = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="24" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Frequency Polygon: Connecting Class Midpoints</text>
  <line x1="55" y1="190" x2="390" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="55" y1="45" x2="55" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <text x="390" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Class Midpoints (Class Marks)</text>
  <polyline points="55,190 85,145 145,112 205,67 265,100 325,134 385,190" fill="none" stroke="#10b981" stroke-width="2.5"/>
  <circle cx="85" cy="145" r="4" fill="#34d399"/>
  <circle cx="145" cy="112" r="4" fill="#34d399"/>
  <circle cx="205" cy="67" r="4" fill="#34d399"/>
  <circle cx="265" cy="100" r="4" fill="#34d399"/>
  <circle cx="325" cy="134" r="4" fill="#34d399"/>
  <text x="85" y="137" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">(5, 8)</text>
  <text x="145" y="104" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">(15, 14)</text>
  <text x="205" y="59" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">(25, 22)</text>
  <text x="265" y="92" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">(35, 16)</text>
  <text x="325" y="126" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">(45, 10)</text>
  <text x="85" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">5</text>
  <text x="145" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">15</text>
  <text x="205" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">25</text>
  <text x="265" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">35</text>
  <text x="325" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">45</text>
</svg>`;

// 3. Pie Diagram
const svgPieChart = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="24" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Pie Diagram: Monthly Household Expenditure</text>
  <path d="M 140 125 L 215 125 A 75 75 0 0 1 102.5 189.95 Z" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
  <path d="M 140 125 L 102.5 189.95 A 75 75 0 0 1 75.05 87.5 Z" fill="#10b981" stroke="#0f172a" stroke-width="2"/>
  <path d="M 140 125 L 75.05 87.5 A 75 75 0 0 1 177.5 60.05 Z" fill="#f59e0b" stroke="#0f172a" stroke-width="2"/>
  <path d="M 140 125 L 177.5 60.05 A 75 75 0 0 1 215 125 Z" fill="#a855f7" stroke="#0f172a" stroke-width="2"/>
  <circle cx="140" cy="125" r="3" fill="#f8fafc"/>
  <text x="160" y="160" fill="#0f172a" font-size="11" font-weight="bold" font-family="sans-serif">120°</text>
  <text x="100" y="130" fill="#0f172a" font-size="11" font-weight="bold" font-family="sans-serif">90°</text>
  <text x="115" y="85" fill="#0f172a" font-size="11" font-weight="bold" font-family="sans-serif">90°</text>
  <text x="165" y="95" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">60°</text>
  <g transform="translate(250, 65)">
    <rect x="0" y="0" width="14" height="14" rx="3" fill="#38bdf8"/>
    <text x="22" y="12" fill="#cbd5e1" font-size="11" font-family="sans-serif">Food (120°, ₹12,000)</text>
    <rect x="0" y="28" width="14" height="14" rx="3" fill="#10b981"/>
    <text x="22" y="40" fill="#cbd5e1" font-size="11" font-family="sans-serif">Education (90°, ₹9,000)</text>
    <rect x="0" y="56" width="14" height="14" rx="3" fill="#f59e0b"/>
    <text x="22" y="68" fill="#cbd5e1" font-size="11" font-family="sans-serif">Rent (90°, ₹9,000)</text>
    <rect x="0" y="84" width="14" height="14" rx="3" fill="#a855f7"/>
    <text x="22" y="96" fill="#cbd5e1" font-size="11" font-family="sans-serif">Savings (60°, ₹6,000)</text>
    <text x="0" y="125" fill="#94a3b8" font-size="10" font-family="sans-serif">Total Budget = ₹36,000 (360°)</text>
  </g>
</svg>`;

// 4. Linear Equations Graphical Method
const svgCartesianLines = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Graphical Solution of Simultaneous Linear Equations</text>
  <line x1="30" y1="130" x2="370" y2="130" stroke="#475569" stroke-width="1.5"/>
  <line x1="190" y1="35" x2="190" y2="210" stroke="#475569" stroke-width="1.5"/>
  <text x="375" y="134" fill="#94a3b8" font-size="11" font-family="sans-serif">X</text>
  <text x="190" y="30" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Y</text>
  <line x1="130" y1="70" x2="350" y2="170" stroke="#38bdf8" stroke-width="2"/>
  <text x="355" y="165" fill="#38bdf8" font-size="10" font-weight="bold" font-family="sans-serif">x + y = 6</text>
  <line x1="150" y1="210" x2="330" y2="30" stroke="#f43f5e" stroke-width="2"/>
  <text x="335" y="38" fill="#f43f5e" font-size="10" font-weight="bold" font-family="sans-serif">x - y = 2</text>
  <circle cx="270" cy="90" r="5" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
  <line x1="270" y1="90" x2="270" y2="130" stroke="#facc15" stroke-dasharray="3,3" stroke-width="1"/>
  <line x1="270" y1="90" x2="190" y2="90" stroke="#facc15" stroke-dasharray="3,3" stroke-width="1"/>
  <text x="280" y="85" fill="#facc15" font-size="11" font-weight="bold" font-family="sans-serif">P(4, 2)</text>
  <text x="270" y="145" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">x = 4</text>
  <text x="175" y="94" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">y = 2</text>
</svg>`;

// 5. Division of Line Segment
const svgLineDivision = `<svg width="420" height="210" viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="210" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Dividing Line Segment AB Internally in Ratio 3 : 2</text>
  <line x1="60" y1="140" x2="360" y2="140" stroke="#f8fafc" stroke-width="2.5"/>
  <line x1="60" y1="140" x2="310" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="318" y="42" fill="#38bdf8" font-size="11" font-family="sans-serif">X</text>
  <circle cx="110" cy="120" r="3" fill="#38bdf8"/>
  <text x="105" y="112" fill="#38bdf8" font-size="10" font-family="sans-serif">A₁</text>
  <circle cx="160" cy="100" r="3" fill="#38bdf8"/>
  <text x="155" y="92" fill="#38bdf8" font-size="10" font-family="sans-serif">A₂</text>
  <circle cx="210" cy="80" r="3" fill="#facc15"/>
  <text x="205" y="72" fill="#facc15" font-size="11" font-weight="bold" font-family="sans-serif">A₃</text>
  <circle cx="260" cy="60" r="3" fill="#38bdf8"/>
  <text x="255" y="52" fill="#38bdf8" font-size="10" font-family="sans-serif">A₄</text>
  <circle cx="310" cy="40" r="3" fill="#38bdf8"/>
  <text x="305" y="32" fill="#38bdf8" font-size="10" font-family="sans-serif">A₅</text>
  <line x1="310" y1="40" x2="360" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="210" y1="80" x2="240" y2="140" stroke="#10b981" stroke-width="2"/>
  <circle cx="60" cy="140" r="4" fill="#f8fafc"/>
  <text x="50" y="160" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">A</text>
  <circle cx="360" cy="140" r="4" fill="#f8fafc"/>
  <text x="365" y="160" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">B</text>
  <circle cx="240" cy="140" r="4.5" fill="#10b981"/>
  <text x="235" y="162" fill="#10b981" font-size="12" font-weight="bold" font-family="sans-serif">P</text>
  <text x="145" y="180" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">AP (3 parts)</text>
  <text x="300" y="180" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">PB (2 parts)</text>
  <text x="210" y="200" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">A₃P ∥ A₅B  ⇒  AP : PB = 3 : 2</text>
</svg>`;

// 6. Tangents from External Point
const svgTangentsExternal = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Construction of Tangents to a Circle from an External Point</text>
  <circle cx="130" cy="120" r="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="130" cy="120" r="3" fill="#f8fafc"/>
  <text x="120" y="115" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif">O</text>
  <circle cx="340" cy="120" r="4" fill="#facc15"/>
  <text x="348" y="125" fill="#facc15" font-size="12" font-weight="bold" font-family="sans-serif">P</text>
  <line x1="130" y1="120" x2="340" y2="120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="235" cy="120" r="3" fill="#94a3b8"/>
  <text x="235" y="112" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">M</text>
  <circle cx="235" cy="120" r="105" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>
  <circle cx="142" cy="71.5" r="4" fill="#10b981"/>
  <text x="135" y="62" fill="#10b981" font-size="11" font-weight="bold" font-family="sans-serif">T₁</text>
  <circle cx="142" cy="168.5" r="4" fill="#10b981"/>
  <text x="135" y="185" fill="#10b981" font-size="11" font-weight="bold" font-family="sans-serif">T₂</text>
  <line x1="130" y1="120" x2="142" y2="71.5" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="130" y1="120" x2="142" y2="168.5" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="340" y1="120" x2="142" y2="71.5" stroke="#10b981" stroke-width="2"/>
  <line x1="340" y1="120" x2="142" y2="168.5" stroke="#10b981" stroke-width="2"/>
  <text x="210" y="215" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Tangents from external point are equal in length: PT₁ = PT₂  (OT₁ ⊥ PT₁)</text>
</svg>`;

// 7. Tangent to Circle using Center
const svgTangentCenter = `<svg width="420" height="210" viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="210" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Tangent to a Circle at a Point on It (Using Center)</text>
  <circle cx="180" cy="115" r="55" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="180" cy="115" r="3.5" fill="#f8fafc"/>
  <text x="168" y="112" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif">O</text>
  <line x1="180" y1="115" x2="310" y2="115" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="235" cy="115" r="4" fill="#facc15"/>
  <text x="235" y="105" fill="#facc15" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">P</text>
  <line x1="235" y1="35" x2="235" y2="195" stroke="#10b981" stroke-width="2.5"/>
  <text x="245" y="45" fill="#10b981" font-size="12" font-weight="bold" font-family="sans-serif">l</text>
  <polyline points="235,127 223,127 223,115" fill="none" stroke="#facc15" stroke-width="1.5"/>
  <text x="210" y="200" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Radius OP ⊥ Tangent line l at the point of contact P</text>
</svg>`;

// 8. Frustum of a Cone
const svgFrustum = `<svg width="420" height="220" viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="220" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Frustum of a Cone: Dimensions and Metrics</text>
  <ellipse cx="210" cy="65" rx="45" ry="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="210" y1="65" x2="255" y2="65" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="232" y="60" fill="#38bdf8" font-size="10" font-weight="bold" font-family="sans-serif">r₁</text>
  <ellipse cx="210" cy="165" rx="85" ry="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="210" y1="165" x2="295" y2="165" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="255" y="160" fill="#38bdf8" font-size="10" font-weight="bold" font-family="sans-serif">r₂</text>
  <line x1="165" y1="65" x2="125" y2="165" stroke="#10b981" stroke-width="2"/>
  <line x1="255" y1="65" x2="295" y2="165" stroke="#10b981" stroke-width="2"/>
  <text x="285" y="115" fill="#10b981" font-size="11" font-weight="bold" font-family="sans-serif">l</text>
  <line x1="210" y1="65" x2="210" y2="165" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="215" y="115" fill="#f59e0b" font-size="11" font-weight="bold" font-family="sans-serif">h</text>
  <text x="210" y="205" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Slant Height: l = √(h² + (r₂ - r₁)²)  •  CSA = π(r₁ + r₂)l</text>
</svg>`;

// 9. Satellite Orbits
const svgSatelliteOrbits = `<svg width="420" height="240" viewBox="0 0 420 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="240" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Classification of Satellite Orbits by Altitude</text>
  <circle cx="160" cy="130" r="30" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
  <text x="160" y="134" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">Earth</text>
  <circle cx="160" cy="130" r="50" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="195" cy="95" r="3.5" fill="#38bdf8"/>
  <text x="202" y="93" fill="#38bdf8" font-size="9" font-family="sans-serif">ISS / Hubble</text>
  <circle cx="160" cy="130" r="75" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="213" cy="77" r="3.5" fill="#10b981"/>
  <text x="220" y="75" fill="#10b981" font-size="9" font-family="sans-serif">GPS (20,200 km)</text>
  <circle cx="160" cy="130" r="100" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="230" cy="60" r="4" fill="#f59e0b"/>
  <text x="238" y="58" fill="#f59e0b" font-size="9" font-weight="bold" font-family="sans-serif">INSAT / GSAT</text>
  <g transform="translate(265, 85)">
    <circle cx="6" cy="6" r="4" fill="#38bdf8"/>
    <text x="16" y="10" fill="#cbd5e1" font-size="10" font-family="sans-serif">LEO (180–2,000 km)</text>
    <text x="16" y="22" fill="#64748b" font-size="9" font-family="sans-serif">Period: ~90–120 min</text>
    <circle cx="6" cy="38" r="4" fill="#10b981"/>
    <text x="16" y="42" fill="#cbd5e1" font-size="10" font-family="sans-serif">MEO (2,000–35,786 km)</text>
    <text x="16" y="54" fill="#64748b" font-size="9" font-family="sans-serif">Period: 2–24 hours</text>
    <circle cx="6" cy="70" r="4" fill="#f59e0b"/>
    <text x="16" y="74" fill="#cbd5e1" font-size="10" font-family="sans-serif">GEO (35,786 km)</text>
    <text x="16" y="86" fill="#64748b" font-size="9" font-family="sans-serif">Period: 24 hours (Sync)</text>
  </g>
</svg>`;

// 10. PSLV Rocket Staging
const svgRocketStages = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">ISRO PSLV (Polar Satellite Launch Vehicle) Staging</text>
  <path d="M 360 115 L 320 90 L 320 140 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
  <text x="340" y="118" fill="#0f172a" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Satellite</text>
  <rect x="270" y="94" width="50" height="42" fill="#6366f1" stroke="#4f46e5" stroke-width="1.5"/>
  <text x="295" y="118" fill="#f8fafc" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">PS4 (Liq)</text>
  <rect x="210" y="92" width="60" height="46" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
  <text x="240" y="118" fill="#f8fafc" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">PS3 (Solid)</text>
  <rect x="140" y="90" width="70" height="50" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
  <text x="175" y="118" fill="#f8fafc" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">PS2 (Vikas)</text>
  <rect x="60" y="86" width="80" height="58" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
  <text x="100" y="118" fill="#f8fafc" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">PS1 (Solid)</text>
  <path d="M 50 115 L 20 100 L 25 115 L 20 130 Z" fill="#fb923c" opacity="0.8"/>
  <text x="100" y="170" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">1st: Solid (HTPB)</text>
  <text x="175" y="185" fill="#fbbf24" font-size="10" font-family="sans-serif" text-anchor="middle">2nd: Liquid (UDMH)</text>
  <text x="240" y="170" fill="#34d399" font-size="10" font-family="sans-serif" text-anchor="middle">3rd: Solid</text>
  <text x="295" y="185" fill="#818cf8" font-size="10" font-family="sans-serif" text-anchor="middle">4th: Liquid</text>
  <text x="210" y="212" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Stages separate successively after fuel burnout to reduce dead weight</text>
</svg>`;

// 11. Kepler's Equal Areas Law
const svgKepler = `<svg width="420" height="210" viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="210" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Kepler's Second Law: Law of Equal Areas</text>
  <ellipse cx="210" cy="115" rx="140" ry="65" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <circle cx="140" cy="115" r="8" fill="#f59e0b"/>
  <circle cx="140" cy="115" r="12" fill="#f59e0b" opacity="0.2"/>
  <text x="140" y="135" fill="#f59e0b" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">Sun (S)</text>
  <path d="M 140 115 L 75 95 A 140 65 0 0 0 75 135 Z" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="95" y="118" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif">Area A₁</text>
  <path d="M 140 115 L 340 100 A 140 65 0 0 1 340 130 Z" fill="#10b981" opacity="0.4" stroke="#10b981" stroke-width="1.5"/>
  <text x="285" y="118" fill="#10b981" font-size="11" font-weight="bold" font-family="sans-serif">Area A₂</text>
  <text x="210" y="195" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time: A₁ = A₂</text>
</svg>`;

// 12. Solenoid Magnetic Field
const svgSolenoid = `<svg width="420" height="200" viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="200" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Magnetic Field Lines of a Current-Carrying Solenoid</text>
  <g stroke="#f59e0b" stroke-width="2.5" fill="none">
    <ellipse cx="140" cy="100" rx="12" ry="35"/>
    <ellipse cx="175" cy="100" rx="12" ry="35"/>
    <ellipse cx="210" cy="100" rx="12" ry="35"/>
    <ellipse cx="245" cy="100" rx="12" ry="35"/>
    <ellipse cx="280" cy="100" rx="12" ry="35"/>
  </g>
  <line x1="110" y1="90" x2="310" y2="90" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="100" y1="100" x2="320" y2="100" stroke="#38bdf8" stroke-width="2"/>
  <line x1="110" y1="110" x2="310" y2="110" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 320 90 C 370 40, 50 40, 100 90" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <path d="M 320 110 C 370 160, 50 160, 100 110" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4,3"/>
  <text x="80" y="105" fill="#ef4444" font-size="13" font-weight="bold" font-family="sans-serif">S</text>
  <text x="330" y="105" fill="#10b981" font-size="13" font-weight="bold" font-family="sans-serif">N</text>
  <text x="210" y="185" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Inside the solenoid, the magnetic field is uniform, parallel, and strong</text>
</svg>`;

// 13. Froth Floatation Process
const svgFrothFloatation = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Froth Floatation Method for Sulphide Ores Concentration</text>
  <rect x="80" y="55" width="260" height="135" rx="4" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <rect x="82" y="85" width="256" height="103" fill="#0369a1" opacity="0.35"/>
  <rect x="82" y="65" width="256" height="25" fill="#fef08a" opacity="0.75"/>
  <text x="210" y="81" fill="#78350f" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">Froth with Hydrophobic Sulphide Ore</text>
  <rect x="205" y="40" width="10" height="110" fill="#94a3b8"/>
  <path d="M 185 150 L 235 150 L 225 160 L 195 160 Z" fill="#cbd5e1"/>
  <text x="210" y="36" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Compressed Air Inflow</text>
  <circle cx="130" cy="110" r="5" fill="#f8fafc" opacity="0.7"/>
  <circle cx="260" cy="115" r="6" fill="#f8fafc" opacity="0.7"/>
  <ellipse cx="210" cy="183" rx="110" ry="6" fill="#78350f" opacity="0.9"/>
  <text x="210" y="184" fill="#fef3c7" font-size="10" font-family="sans-serif" text-anchor="middle">Gangue (Hydrophilic Earthy Impurities)</text>
  <text x="210" y="212" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Pine oil wets sulphide ore (floats) • Water wets gangue (sinks)</text>
</svg>`;

// 14. Magnetic Separation Conveyor Belt
const svgMagneticSeparator = `<svg width="420" height="220" viewBox="0 0 420 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="220" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Magnetic Separation Method for Ores</text>
  <polygon points="60,40 100,40 85,80 75,80" fill="#64748b" stroke="#94a3b8" stroke-width="1"/>
  <text x="80" y="35" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Powdered Ore</text>
  <circle cx="100" cy="110" r="22" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
  <circle cx="280" cy="110" r="22" fill="#dc2626" stroke="#f87171" stroke-width="2"/>
  <text x="280" y="114" fill="#f8fafc" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Magnetic</text>
  <line x1="100" y1="88" x2="280" y2="88" stroke="#f8fafc" stroke-width="3"/>
  <line x1="100" y1="132" x2="280" y2="132" stroke="#f8fafc" stroke-width="3"/>
  <path d="M 285 88 Q 340 110 350 160" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="330" y="160" width="55" height="35" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="357" y="178" fill="#38bdf8" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Non-Magnetic</text>
  <text x="357" y="190" fill="#94a3b8" font-size="8" font-family="sans-serif" text-anchor="middle">Collector</text>
  <path d="M 280 132 Q 275 145 270 160" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="245" y="160" width="55" height="35" rx="3" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
  <text x="272" y="178" fill="#ef4444" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Magnetic</text>
  <text x="272" y="190" fill="#94a3b8" font-size="8" font-family="sans-serif" text-anchor="middle">Collector</text>
  <text x="210" y="210" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">E.g., Cassiterite ore (non-magnetic SnO₂) separated from wolframite (magnetic FeWO₄)</text>
</svg>`;

// 15. Hall-Héroult Electrolytic Cell
const svgHallHeroult = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Hall-Héroult Electrolytic Reduction of Alumina</text>
  <rect x="70" y="60" width="280" height="130" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <rect x="75" y="65" width="270" height="120" fill="#1e293b"/>
  <rect x="75" y="175" width="270" height="10" fill="#0f172a"/>
  <text x="350" y="183" fill="#38bdf8" font-size="9" font-weight="bold" font-family="sans-serif">Cathode (-)</text>
  <rect x="75" y="90" width="270" height="70" fill="#f59e0b" opacity="0.35"/>
  <text x="210" y="125" fill="#fef08a" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">Molten Alumina + Cryolite + Fluorspar (~950°C)</text>
  <rect x="75" y="160" width="270" height="15" fill="#94a3b8" opacity="0.9"/>
  <text x="210" y="171" fill="#0f172a" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Molten Aluminium (Al)</text>
  <rect x="120" y="45" width="18" height="65" fill="#0f172a" stroke="#f8fafc" stroke-width="1"/>
  <rect x="170" y="45" width="18" height="65" fill="#0f172a" stroke="#f8fafc" stroke-width="1"/>
  <rect x="220" y="45" width="18" height="65" fill="#0f172a" stroke="#f8fafc" stroke-width="1"/>
  <rect x="270" y="45" width="18" height="65" fill="#0f172a" stroke="#f8fafc" stroke-width="1"/>
  <text x="210" y="40" fill="#10b981" font-size="10" font-weight="bold" font-family="sans-serif" text-anchor="middle">Graphite Anodes (+)</text>
  <rect x="50" y="162" width="25" height="10" fill="#94a3b8"/>
  <text x="210" y="215" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Cathode: Al³⁺ + 3e⁻ → Al(l)  •  Anode: 2O²⁻ → O₂ + 4e⁻ (attacks carbon rods to form CO₂)</text>
</svg>`;

// 16. Modern Sanitary Landfill
const svgSanitaryLandfill = `<svg width="420" height="235" viewBox="0 0 420 235" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="235" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Cross-Section of a Modern Sanitary Landfill</text>
  <rect x="50" y="180" width="320" height="15" fill="#78350f" opacity="0.8"/>
  <text x="210" y="192" fill="#fef3c7" font-size="9" font-family="sans-serif" text-anchor="middle">Impermeable Clay Liner (Prevents Groundwater Contamination)</text>
  <line x1="50" y1="178" x2="370" y2="178" stroke="#38bdf8" stroke-width="3"/>
  <line x1="60" y1="170" x2="360" y2="170" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6,4"/>
  <text x="365" y="165" fill="#f59e0b" font-size="9" font-family="sans-serif">Leachate Pipe</text>
  <rect x="60" y="125" width="300" height="40" fill="#334155"/>
  <text x="210" y="148" fill="#cbd5e1" font-size="10" font-weight="600" font-family="sans-serif" text-anchor="middle">Compacted Solid Waste Layer</text>
  <rect x="60" y="118" width="300" height="7" fill="#b45309"/>
  <rect x="60" y="75" width="300" height="43" fill="#334155"/>
  <text x="210" y="98" fill="#cbd5e1" font-size="10" font-weight="600" font-family="sans-serif" text-anchor="middle">Solid Waste Layer</text>
  <rect x="50" y="68" width="320" height="7" fill="#15803d"/>
  <text x="210" y="62" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Top Soil & Vegetation Cap</text>
  <line x1="120" y1="40" x2="120" y2="150" stroke="#f87171" stroke-width="3"/>
  <circle cx="120" cy="40" r="5" fill="#ef4444"/>
  <text x="130" y="44" fill="#f87171" font-size="10" font-weight="bold" font-family="sans-serif">Methane (CH₄) Vent</text>
  <text x="210" y="222" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Biochemical degradation produces methane gas (fuel) & slurry</text>
</svg>`;

// 17. Biogas Plant Digester
const svgBiogasPlant = `<svg width="420" height="230" viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="230" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Fixed Dome Biogas Plant (Gobar Gas)</text>
  <rect x="40" y="80" width="50" height="45" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="65" y="105" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Slurry Inlet</text>
  <line x1="85" y1="125" x2="130" y2="160" stroke="#94a3b8" stroke-width="6"/>
  <rect x="130" y="110" width="160" height="85" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="210" y="160" fill="#f8fafc" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">Anaerobic Digester</text>
  <path d="M 130 110 Q 210 50 290 110 Z" fill="#0284c7" opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
  <text x="210" y="95" fill="#fef08a" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">Biogas (CH₄ + CO₂)</text>
  <line x1="210" y1="65" x2="210" y2="35" stroke="#f59e0b" stroke-width="4"/>
  <circle cx="210" cy="40" r="4" fill="#f59e0b"/>
  <text x="218" y="38" fill="#f59e0b" font-size="10" font-weight="bold" font-family="sans-serif">Gas Valve</text>
  <line x1="290" y1="160" x2="335" y2="125" stroke="#94a3b8" stroke-width="6"/>
  <rect x="330" y="80" width="55" height="45" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="357" y="100" fill="#4ade80" font-size="9" font-weight="bold" font-family="sans-serif" text-anchor="middle">Spent Slurry</text>
  <text x="357" y="113" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Biofertilizer)</text>
  <text x="210" y="215" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Anaerobic microbes decompose organic matter to generate clean combustible fuel</text>
</svg>`;

// 18. Agarose Gel Electrophoresis
const svgGelElectrophoresis = `<svg width="420" height="225" viewBox="0 0 420 225" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="225" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Agarose Gel Electrophoresis for DNA Separation</text>
  <rect x="70" y="45" width="280" height="145" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="40" y="70" fill="#f43f5e" font-size="13" font-weight="bold" font-family="sans-serif">Cathode (-)</text>
  <text x="40" y="175" fill="#10b981" font-size="13" font-weight="bold" font-family="sans-serif">Anode (+)</text>
  <rect x="100" y="55" width="22" height="6" fill="#0f172a" stroke="#94a3b8"/>
  <text x="111" y="48" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">Ladder</text>
  <rect x="100" y="75" width="22" height="3" fill="#facc15"/>
  <text x="127" y="79" fill="#facc15" font-size="8" font-family="sans-serif">1000 bp</text>
  <rect x="100" y="98" width="22" height="3" fill="#facc15"/>
  <text x="127" y="102" fill="#facc15" font-size="8" font-family="sans-serif">750 bp</text>
  <rect x="100" y="122" width="22" height="3" fill="#facc15"/>
  <text x="127" y="126" fill="#facc15" font-size="8" font-family="sans-serif">500 bp</text>
  <rect x="100" y="150" width="22" height="3" fill="#facc15"/>
  <text x="127" y="154" fill="#facc15" font-size="8" font-family="sans-serif">250 bp</text>
  <rect x="180" y="55" width="22" height="6" fill="#0f172a" stroke="#94a3b8"/>
  <text x="191" y="48" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Sample 1</text>
  <rect x="180" y="98" width="22" height="3" fill="#38bdf8"/>
  <rect x="180" y="150" width="22" height="3" fill="#38bdf8"/>
  <rect x="260" y="55" width="22" height="6" fill="#0f172a" stroke="#94a3b8"/>
  <text x="271" y="48" fill="#34d399" font-size="9" font-family="sans-serif" text-anchor="middle">Sample 2</text>
  <rect x="260" y="75" width="22" height="3" fill="#34d399"/>
  <rect x="260" y="122" width="22" height="3" fill="#34d399"/>
  <text x="210" y="210" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">DNA is negatively charged (PO₄³⁻) • Smaller fragments travel faster & farther towards (+)</text>
</svg>`;

// 19. Mitochondrion & Cellular Respiration
const svgMitochondrion = `<svg width="420" height="215" viewBox="0 0 420 215" xmlns="http://www.w3.org/2000/svg">
  <rect width="420" height="215" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="210" y="22" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Mitochondrion: Structure and Cellular Respiration</text>
  <ellipse cx="210" cy="110" rx="140" ry="60" fill="#0f766e" opacity="0.3" stroke="#14b8a6" stroke-width="2.5"/>
  <text x="210" y="45" fill="#2dd4bf" font-size="10" font-family="sans-serif" text-anchor="middle">Outer Membrane (Permeable to small molecules)</text>
  <path d="M 90 110 Q 110 80, 130 110 T 170 110 T 210 110 T 250 110 T 290 110 T 330 110" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="280" y="85" fill="#f59e0b" font-size="10" font-weight="bold" font-family="sans-serif">Cristae (ETC & ATP Synthase)</text>
  <text x="140" y="140" fill="#38bdf8" font-size="10" font-weight="bold" font-family="sans-serif">Matrix (Krebs Cycle / TCA)</text>
  <text x="210" y="195" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Aerobic Respiration: Glycolysis (Cytoplasm) → Krebs Cycle (Matrix) → ETC (Cristae)</text>
</svg>`;

// ==========================================
// TARGET CONFIGURATION
// ==========================================

const ENRICHMENT_CONFIG = [
  // --- Mathematics 1 (Algebra) ---
  {
    topicCode: 'MH-10-MTH1-6-6.5.1',
    svg: svgHistogram,
    count: 8,
    domain: 'Mathematics 1 (Algebra)',
    desc: 'Histogram marks distribution diagram'
  },
  {
    topicCode: 'MH-10-MTH1-6-6.5.2',
    svg: svgFreqPolygon,
    count: 8,
    domain: 'Mathematics 1 (Algebra)',
    desc: 'Frequency polygon midpoints diagram'
  },
  {
    topicCode: 'MH-10-MTH1-6-6.6.1',
    svg: svgPieChart,
    count: 8,
    domain: 'Mathematics 1 (Algebra)',
    desc: 'Pie diagram monthly expenditure sectors'
  },
  {
    topicCode: 'MH-10-MTH1-6-6.6.2',
    svg: svgPieChart,
    count: 8,
    domain: 'Mathematics 1 (Algebra)',
    desc: 'Pie diagram budget interpretation'
  },
  {
    topicCode: 'MH-10-MTH1-1-1.2.2',
    svg: svgCartesianLines,
    count: 8,
    domain: 'Mathematics 1 (Algebra)',
    desc: 'Cartesian linear equation intersection graph'
  },

  // --- Mathematics 2 (Geometry) ---
  {
    topicCode: 'MH-10-MTH2-4-4.1.1',
    svg: svgLineDivision,
    count: 8,
    domain: 'Mathematics 2 (Geometry)',
    desc: 'Dividing line segment in ratio 3:2 construction'
  },
  {
    topicCode: 'MH-10-MTH2-4-4.2.1',
    svg: svgTangentCenter,
    count: 8,
    domain: 'Mathematics 2 (Geometry)',
    desc: 'Tangent to circle with center construction'
  },
  {
    topicCode: 'MH-10-MTH2-4-4.4.1',
    svg: svgTangentsExternal,
    count: 8,
    domain: 'Mathematics 2 (Geometry)',
    desc: 'Tangents to circle from external point construction'
  },
  {
    topicCode: 'MH-10-MTH2-7-7.2.1',
    svg: svgFrustum,
    count: 8,
    domain: 'Mathematics 2 (Geometry)',
    desc: 'Frustum of a cone dimensions'
  },

  // --- Physics ---
  {
    topicCode: 'MH-10-SCIT1-1-1.1.1',
    svg: svgKepler,
    count: 8,
    domain: 'Physics',
    desc: "Kepler's second law of planetary motion"
  },
  {
    topicCode: 'MH-10-SCIT1-4-4.2.1',
    svg: svgSolenoid,
    count: 8,
    domain: 'Physics',
    desc: 'Magnetic field lines of a solenoid'
  },
  {
    topicCode: 'MH-10-SCIT1-10-10.3.1',
    svg: svgSatelliteOrbits,
    count: 8,
    domain: 'Physics',
    desc: 'Satellite orbit tiers LEO/MEO/GEO'
  },
  {
    topicCode: 'MH-10-SCIT1-10-10.4.1',
    svg: svgRocketStages,
    count: 8,
    domain: 'Physics',
    desc: 'PSLV rocket staging and structure'
  },

  // --- Chemistry ---
  {
    topicCode: 'MH-10-SCIT1-8-8.2.1',
    svg: svgFrothFloatation,
    count: 8,
    domain: 'Chemistry',
    desc: 'Froth floatation tank apparatus'
  },
  {
    topicCode: 'MH-10-SCIT1-8-8.2.2',
    svg: svgMagneticSeparator,
    count: 8,
    domain: 'Chemistry',
    desc: 'Magnetic separator conveyor belt'
  },
  {
    topicCode: 'MH-10-SCIT1-8-8.3.1',
    svg: svgHallHeroult,
    count: 8,
    domain: 'Chemistry',
    desc: 'Hall-Heroult electrolytic reduction cell'
  },

  // --- Biology ---
  {
    topicCode: 'MH-10-SCIT2-2-2.1.2',
    svg: svgMitochondrion,
    count: 8,
    domain: 'Biology',
    desc: 'Mitochondrion respiration and ATP production'
  },
  {
    topicCode: 'MH-10-SCIT2-7-7.2.1',
    svg: svgSanitaryLandfill,
    count: 8,
    domain: 'Biology',
    desc: 'Modern sanitary landfill cross-section'
  },
  {
    topicCode: 'MH-10-SCIT2-7-7.2.2',
    svg: svgBiogasPlant,
    count: 8,
    domain: 'Biology',
    desc: 'Biogas plant anaerobic digester'
  },
  {
    topicCode: 'MH-10-SCIT2-8-8.2.1',
    svg: svgGelElectrophoresis,
    count: 8,
    domain: 'Biology',
    desc: 'Agarose gel electrophoresis DNA ladder'
  }
];

async function main() {
  const isDryRun = process.argv.includes('--dry-run');
  console.log('====================================================');
  console.log(`FIGURE-BASED QUESTION ENRICHMENT (${isDryRun ? 'DRY RUN' : 'LIVE COMMIT'})`);
  console.log('====================================================');

  const allUpdates = [];

  for (const cfg of ENRICHMENT_CONFIG) {
    console.log(`Auditing ${cfg.domain} | ${cfg.topicCode} (${cfg.desc})...`);
    
    // Fetch questions in topic
    const qSnap = await adminDb.collection('questions')
      .where('topicCode', '==', cfg.topicCode)
      .get();
      
    if (qSnap.empty) {
      console.warn(`  ⚠️ No questions found for topicCode: ${cfg.topicCode}`);
      continue;
    }

    // Filter questions that don't already have an SVG
    const candidateDocs = [];
    qSnap.forEach(doc => {
      const d = doc.data();
      if (!d.text || !d.text.includes('<svg')) {
        candidateDocs.push({ id: doc.id, ref: doc.ref, data: d });
      }
    });

    console.log(`  Found ${qSnap.size} total questions, ${candidateDocs.length} candidates without SVG.`);
    const toEnrich = candidateDocs.slice(0, cfg.count);

    if (toEnrich.length === 0) {
      console.log(`  All questions already have SVGs or target count reached.`);
      continue;
    }

    toEnrich.forEach(item => {
      allUpdates.push({
        item,
        cfg
      });
    });
  }

  console.log(`\nTotal questions queued for enrichment: ${allUpdates.length}`);

  if (allUpdates.length === 0) {
    console.log('No updates needed. Exiting.');
    return;
  }

  if (isDryRun) {
    console.log(`[DRY RUN] Would update ${allUpdates.length} questions across 20 topics.`);
    return;
  }

  // Rule Q: Create atomic pre-mutation snapshot of the targeted questions
  const targetDir = path.join(__dirname, '..', 'backups', 'snapshots');
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const now = new Date();
  const dateKey = now.toISOString().split('T')[0];
  const timeStr = now.toTimeString().split(' ')[0].replace(/:/g, '-');
  const snapshotId = `snapshot_${dateKey}_${timeStr}_enrich_visual_figures`;
  const filePath = path.join(targetDir, `${snapshotId}.json`);

  const snapshotData = {
    metadata: {
      snapshotId,
      timestamp: now.toISOString(),
      reason: 'enrich_visual_figures_across_5_domains',
      totalDocuments: allUpdates.length,
      filePath
    },
    documents: allUpdates.map(u => ({
      id: u.item.id,
      topicCode: u.cfg.topicCode,
      data: u.item.data
    }))
  };

  fs.writeFileSync(filePath, JSON.stringify(snapshotData, null, 2), 'utf8');
  console.log(`✓ Rule Q: Atomic pre-mutation snapshot saved: ${snapshotId} (${allUpdates.length} docs)\n`);

  // Execute batched commit (batch size 400 max, here 160 docs in 1 batch)
  console.log(`Committing ${allUpdates.length} enriched questions to Firestore...`);
  const batch = adminDb.batch();

  for (const u of allUpdates) {
    const wrappedSvg = wrapSvg(u.cfg.svg);
    const enrichedText = wrappedSvg + u.item.data.text;
    batch.update(u.item.ref, {
      text: enrichedText,
      requiresFigure: true,
      updatedAt: new Date().toISOString()
    });
  }

  await batch.commit();
  console.log(`✓ Successfully updated ${allUpdates.length} questions in Firestore!`);

  console.log('\n====================================================');
  console.log(`Total figure-based questions enriched: ${allUpdates.length}`);
  console.log('====================================================');
}

main().then(() => process.exit(0)).catch(err => {
  console.error('Fatal error during figure enrichment:', err);
  process.exit(1);
});
