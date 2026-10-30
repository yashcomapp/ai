import json

with open('scripts/mh10_mth2_ch1_t1.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Sample one from each category
samples = [
    'MH-10-MTH2-1-1.1-OSC-001', # Two triangles with bases and heights
    'MH-10-MTH2-1-1.1-OSC-002', # Common base AB with perpendiculars
    'MH-10-MTH2-1-1.1-OSC-003', # Obtuse triangle with external altitude
    'MH-10-MTH2-1-1.1-OSC-004', # Triangles between parallel lines
    'MH-10-MTH2-1-1.1-OSC-005', # Nested heights PQ and AD
    'MH-10-MTH2-1-1.1-OSC-011', # Median triangle
    'MH-10-MTH2-1-1.1-OSC-012', # Trapezium with diagonals
    'MH-10-MTH2-1-1.1-OSC-013', # Quadrilateral with common diagonal
    'MH-10-MTH2-1-1.1-OSC-014', # Three collinear base segments
    'MH-10-MTH2-1-1.1-OMC-023', # Parallel lines multi-choice
    'MH-10-MTH2-1-1.1-OTF-028', # Median bisects area true/false
    'MH-10-MTH2-1-1.1-ONE-037', # Numerical calculation of QT
    'MH-10-MTH2-1-1.1-OAR-064', # Assertion & Reason with diagram
]

for code in samples:
    q = next((item for item in questions if item['questionCode'] == code), None)
    if not q:
        continue
    print("=" * 60)
    print(f"CODE: {q['questionCode']} | TYPE: {q['type']} | VAULT: {q['vault']}")
    print("-" * 60)
    # Strip SVG for clean printing of the text
    t = q['text']
    svg_idx = t.find('</svg>')
    stem = t[svg_idx + 12:].strip() if svg_idx != -1 else t
    print("STEM:\n", stem[:200])
    print("\nOPTIONS:", q['options'])
    print("CORRECT ANSWER:", q['correctAnswer'])
    print("\nEXPLANATION SNIPPET:\n", q['explanation'][:180].replace('\n', ' '))
    print("=" * 60 + "\n")
