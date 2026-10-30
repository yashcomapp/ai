import json
import re
import os

with open('scripts/mh10_mth2_ch1_t1.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions loaded: {len(questions)}")

errors = []
svg_count = 0

for q in questions:
    code = q['questionCode']
    text = q.get('text', '')
    diagram = q.get('diagram', '')
    combined = text + ' ' + diagram

    if '<svg' not in combined:
        continue

    svg_count += 1
    # Extract SVG
    m = re.search(r'<svg([^>]*)>([\s\S]*?)<\/svg>', combined)
    if not m:
        errors.append((code, "Malformed SVG tag"))
        continue

    attrs = m.group(1)
    body = m.group(2)

    vb = re.search(r'viewBox=["\']0 0 (\d+) (\d+)["\']', attrs)
    if not vb:
        errors.append((code, "Missing viewBox"))
        continue

    vw, vh = int(vb.group(1)), int(vb.group(2))

    w_match = re.search(r'width=["\'](\d+)["\']', attrs)
    h_match = re.search(r'height=["\'](\d+)["\']', attrs)
    if not w_match or not h_match:
        errors.append((code, "Missing width/height attribute"))
        continue

    w, h = int(w_match.group(1)), int(h_match.group(1))
    if w != vw or h != vh:
        errors.append((code, f"Width/Height mismatch: attr {w}x{h} vs vb {vw}x{vh}"))

    # Check for text elements with negative or overflowing coordinates
    texts = re.findall(r'<text[^>]*x=["\'](\d+)["\'][^>]*y=["\'](\d+)["\'][^>]*>([^<]*)<\/text>', body)
    for tx, ty, content in texts:
        ix, iy = int(tx), int(ty)
        if ix > vw or iy > vh:
            errors.append((code, f"Text '{content}' out of bounds at ({ix}, {iy}) in {vw}x{vh}"))
        if ix < 0 or iy < 0:
            errors.append((code, f"Text '{content}' negative coords at ({ix}, {iy})"))

    # Check for polygon points
    polys = re.findall(r'<polygon[^>]*points=["\']([^"\']*)["\']', body)
    for p in polys:
        coords = p.strip().split()
        for pair in coords:
            if ',' in pair:
                px, py = pair.split(',')
                ipx, ipy = int(px), int(py)
                if ipx > vw or ipy > vh or ipx < 0 or ipy < 0:
                    errors.append((code, f"Polygon point ({ipx}, {ipy}) out of bounds in {vw}x{vh}"))

    # Check for line coords
    lines = re.findall(r'<line[^>]*x1=["\'](\d+)["\'][^>]*y1=["\'](\d+)["\'][^>]*x2=["\'](\d+)["\'][^>]*y2=["\'](\d+)["\']', body)
    for x1, y1, x2, y2 in lines:
        for val, name in [(int(x1), 'x1'), (int(x2), 'x2')]:
            if val > vw:
                errors.append((code, f"Line {name}={val} > vw={vw}"))
        for val, name in [(int(y1), 'y1'), (int(y2), 'y2')]:
            if val > vh:
                errors.append((code, f"Line {name}={val} > vh={vh}"))

    # Check for circles
    circles = re.findall(r'<circle[^>]*cx=["\'](\d+)["\'][^>]*cy=["\'](\d+)["\']', body)
    for cx, cy in circles:
        icx, icy = int(cx), int(cy)
        if icx > vw or icy > vh:
            errors.append((code, f"Circle at ({icx}, {icy}) out of bounds in {vw}x{vh}"))

print(f"Audited {svg_count} diagram-based questions.")
if errors:
    print(f"Found {len(errors)} issues:")
    for code, msg in errors[:20]:
        print(f"  - {code}: {msg}")
else:
    print("ALL SVG DIAGRAMS PASSED BOUNDS AND SYNTAX CHECKS PERFECTLY!")
