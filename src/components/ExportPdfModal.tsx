import React, { useState } from 'react';
import { exportToPDF } from '@/lib/pdfExport';

interface ExportPdfModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  filename: string;
  sections: Array<{ id: string; name: string; elementId: string }>;
}

export const ExportPdfModal: React.FC<ExportPdfModalProps> = ({ isOpen, onClose, title, filename, sections }) => {
  const [selected, setSelected] = useState<Record<string, boolean>>(
    sections.reduce((acc, s) => ({ ...acc, [s.id]: true }), {})
  );
  const [exporting, setExporting] = useState(false);

  if (!isOpen) return null;

  const handleExport = async () => {
    setExporting(true);
    try {
      await exportToPDF({
        filename,
        title,
        sections: sections.map(s => ({
          id: s.id,
          name: s.name,
          elementId: s.elementId,
          checked: !!selected[s.id]
        }))
      });
      onClose();
    } catch (e: any) {
      alert(`Error exporting PDF: ${e.message}`);
    } finally {
      setExporting(false);
    }
  };

  const isAnySelected = Object.values(selected).some(Boolean);

  return (
    <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.45)', backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)', zIndex: 30000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
      <div style={{ background: 'var(--surface-popover)', border: '1px solid var(--border-popover)', padding: '24px', borderRadius: 'var(--radius-lg)', maxWidth: '440px', width: '90%', display: 'flex', flexDirection: 'column', gap: '15px', boxShadow: 'var(--shadow-lg)' }}>
        <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 800, color: 'var(--text)' }}>📄 Export to PDF</h3>
        <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: 0 }}>Select the sections you want to include in the exported PDF file:</p>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', margin: '10px 0' }}>
          {sections.map(s => (
            <label key={s.id} style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px', cursor: 'pointer', color: 'var(--text)' }}>
              <input 
                type="checkbox" 
                checked={!!selected[s.id]} 
                onChange={(e) => setSelected(prev => ({ ...prev, [s.id]: e.target.checked }))} 
              />
              <span>{s.name}</span>
            </label>
          ))}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px', borderTop: '1px solid var(--border-light)', paddingTop: '12px' }}>
          <button className="btn btn-secondary" onClick={onClose} disabled={exporting}>Cancel</button>
          <button className="btn btn-primary" onClick={handleExport} disabled={!isAnySelected || exporting}>
            {exporting ? 'Generating PDF...' : 'Generate PDF'}
          </button>
        </div>
      </div>
    </div>
  );
};
export default ExportPdfModal;
