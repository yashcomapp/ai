'use client';

import React from 'react';

export default function TVVisualizerPage() {
  return (
    <div className="w-full min-h-screen bg-slate-950 flex flex-col">
      <iframe 
        src="/tv_unit_visualizer.html" 
        className="w-full flex-1 border-none min-h-screen"
        title="TV Unit Dual-Tone Visualizer"
      />
    </div>
  );
}
