"""
SVG Diagram Helpers for Maharashtra Board Class 10 Geometry (MH-10-MTH2)
Chapter 1: Similarity - Topic 1.1: Ratio of Areas of Two Triangles
"""

def wrap_svg(inner_svg, width=380, height=210):
    return (
        f'<div style="display: flex; justify-content: center; margin: 14px 0;">\n'
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
        f'  <rect width="{width}" height="{height}" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>\n'
        f'{inner_svg}\n'
        f'</svg>\n'
        f'</div>'
    )

def svg_two_triangles(
    t1_names=('A', 'B', 'C', 'D'),
    b1_label='b₁ = 9',
    h1_label='h₁ = 5',
    t2_names=('P', 'Q', 'R', 'S'),
    b2_label='b₂ = 10',
    h2_label='h₂ = 6',
    title=""
):
    """
    Renders two separate triangles side by side, each with an altitude and base label.
    t1: A(top), B(bot-left), C(bot-right), D(altitude foot)
    t2: P(top), Q(bot-left), R(bot-right), S(altitude foot)
    """
    a, b, c, d = t1_names
    p, q, r, s = t2_names
    title_xml = f'  <text x="190" y="24" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""

    inner = f"""{title_xml}  <!-- Triangle 1 (Left) -->
  <polygon points="90,45 25,165 155,165" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="90" y1="45" x2="90" y2="165" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <!-- Right angle marker D -->
  <polyline points="90,153 100,153 100,165" fill="none" stroke="#f43f5e" stroke-width="1.2"/>
  <!-- Vertices Triangle 1 -->
  <circle cx="90" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="25" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="155" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="90" cy="165" r="3" fill="#f43f5e"/>
  <text x="90" y="38" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{a}</text>
  <text x="16" y="172" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{b}</text>
  <text x="166" y="172" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{c}</text>
  <text x="90" y="180" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">{d}</text>
  <!-- Labels T1 -->
  <text x="68" y="105" fill="#fbbf24" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{h1_label}</text>
  <text x="90" y="196" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b1_label}</text>

  <!-- Triangle 2 (Right) -->
  <polygon points="290,45 215,165 365,165" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
  <line x1="290" y1="45" x2="290" y2="165" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <!-- Right angle marker S -->
  <polyline points="290,153 300,153 300,165" fill="none" stroke="#f43f5e" stroke-width="1.2"/>
  <!-- Vertices Triangle 2 -->
  <circle cx="290" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="215" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="365" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="290" cy="165" r="3" fill="#f43f5e"/>
  <text x="290" y="38" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{p}</text>
  <text x="206" y="172" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{q}</text>
  <text x="375" y="172" fill="#f8fafc" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{r}</text>
  <text x="290" y="180" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">{s}</text>
  <!-- Labels T2 -->
  <text x="268" y="105" fill="#fbbf24" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{h2_label}</text>
  <text x="290" y="196" fill="#34d399" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b2_label}</text>"""
    return wrap_svg(inner, 390, 215)


def svg_collinear_base(
    top='A',
    b_left='B',
    b_mid='D',
    b_right='C',
    len_bd='4',
    len_dc='6',
    show_alt=True,
    title=""
):
    """
    Triangle ABC with point D on BC. Common vertex A.
    Shows collinear bases BD and DC with common height.
    """
    title_xml = f'  <text x="180" y="24" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    alt_xml = ""
    if show_alt:
        alt_xml = """  <!-- Common Altitude AH -->
  <line x1="160" y1="45" x2="160" y2="165" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <polyline points="160,153 170,153 170,165" fill="none" stroke="#f43f5e" stroke-width="1.2"/>
  <circle cx="160" cy="165" r="3" fill="#f43f5e"/>
  <text x="160" y="180" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">H</text>
  <text x="145" y="105" fill="#fbbf24" font-size="10" font-weight="600" font-family="sans-serif">h</text>"""

    inner = f"""{title_xml}  <!-- Main Triangle ABC -->
  <polygon points="160,45 40,165 320,165" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Cevian line AD -->
  <line x1="160" y1="45" x2="200" y2="165" stroke="#a855f7" stroke-width="2"/>
{alt_xml}
  <!-- Vertices -->
  <circle cx="160" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="40" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="200" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="320" cy="165" r="3.5" fill="#f8fafc"/>
  <text x="160" y="36" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top}</text>
  <text x="28" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{b_left}</text>
  <text x="200" y="180" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{b_mid}</text>
  <text x="332" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{b_right}</text>
  <!-- Segment lengths -->
  <text x="110" y="194" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b_left}{b_mid} = {len_bd}</text>
  <text x="260" y="194" fill="#a855f7" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b_mid}{b_right} = {len_dc}</text>"""
    return wrap_svg(inner, 360, 210)


def svg_practice_set_1_1_q2(bc_val='4', ad_val='8', title=""):
    """
    Practice Set 1.1 Q2:
    BC ⊥ AB, AD ⊥ AB, common base AB.
    """
    title_xml = f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Base AB -->
  <line x1="80" y1="160" x2="280" y2="160" stroke="#f8fafc" stroke-width="2.5"/>
  <!-- BC perpendicular up at B -->
  <line x1="280" y1="160" x2="280" y2="85" stroke="#34d399" stroke-width="2.2"/>
  <!-- AD perpendicular up at A -->
  <line x1="80" y1="160" x2="80" y2="40" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Triangles AC and BD hypotenuse / crossing lines -->
  <line x1="80" y1="160" x2="280" y2="85" stroke="#34d399" stroke-width="1.8" stroke-dasharray="4,3"/>
  <line x1="280" y1="160" x2="80" y2="40" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4,3"/>
  <!-- Right angle at B for BC ⊥ AB -->
  <polyline points="268,160 268,148 280,148" fill="none" stroke="#34d399" stroke-width="1.4"/>
  <!-- Right angle at A for AD ⊥ AB -->
  <polyline points="80,148 92,148 92,160" fill="none" stroke="#38bdf8" stroke-width="1.4"/>
  <!-- Vertices -->
  <circle cx="80" cy="160" r="3.5" fill="#f8fafc"/>
  <circle cx="280" cy="160" r="3.5" fill="#f8fafc"/>
  <circle cx="80" cy="40" r="3.5" fill="#38bdf8"/>
  <circle cx="280" cy="85" r="3.5" fill="#34d399"/>
  <text x="65" y="166" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">A</text>
  <text x="294" y="166" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="294" y="85" fill="#34d399" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="65" y="40" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif">D</text>
  <!-- Length annotations -->
  <text x="45" y="98" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif">AD = {ad_val}</text>
  <text x="305" y="125" fill="#34d399" font-size="11" font-weight="bold" font-family="sans-serif">BC = {bc_val}</text>
  <text x="180" y="180" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">Common Base AB</text>"""
    return wrap_svg(inner, 370, 200)


def svg_practice_set_1_1_q3(rq_val='6', ps_val='6', pr_val='12', qt_label='QT = ?', title=""):
    """
    Practice Set 1.1 Q3:
    In ΔPQR, PS ⊥ ray RQ, QT ⊥ PR.
    Obtuse angle at Q.
    """
    title_xml = f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Main Triangle PQR (obtuse at Q) -->
  <polygon points="120,45 160,140 310,140" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Extended ray RQ to S -->
  <line x1="160" y1="140" x2="80" y2="140" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,4"/>
  <!-- Altitude PS ⊥ ray RQ -->
  <line x1="120" y1="45" x2="80" y2="140" stroke="#f43f5e" stroke-width="2"/>
  <!-- Right angle at S -->
  <polyline points="80,128 92,128 92,140" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <!-- Altitude QT ⊥ PR -->
  <line x1="160" y1="140" x2="225" y2="98" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
  <!-- Right angle at T -->
  <polyline points="218,103 223,110 229,105" fill="none" stroke="#fbbf24" stroke-width="1.3"/>
  <!-- Vertices -->
  <circle cx="120" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="160" cy="140" r="3.5" fill="#f8fafc"/>
  <circle cx="310" cy="140" r="3.5" fill="#f8fafc"/>
  <circle cx="80" cy="140" r="3.5" fill="#f43f5e"/>
  <circle cx="225" cy="98" r="3" fill="#fbbf24"/>
  <text x="120" y="36" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">P</text>
  <text x="160" y="158" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">Q</text>
  <text x="322" y="145" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">R</text>
  <text x="68" y="145" fill="#f43f5e" font-size="13" font-weight="bold" font-family="sans-serif">S</text>
  <text x="238" y="94" fill="#fbbf24" font-size="12" font-weight="bold" font-family="sans-serif">T</text>
  <!-- Dimension labels -->
  <text x="60" y="90" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif">PS = {ps_val}</text>
  <text x="230" y="158" fill="#38bdf8" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">RQ = {rq_val}</text>
  <text x="245" y="65" fill="#a855f7" font-size="11" font-weight="bold" font-family="sans-serif">PR = {pr_val}</text>
  <text x="190" y="118" fill="#fbbf24" font-size="10" font-weight="600" font-family="sans-serif">{qt_label}</text>"""
    return wrap_svg(inner, 360, 200)


def svg_parallel_lines_triangles(top_l='A', top_r='D', bot_l='B', bot_r='C', title=""):
    """
    Practice Set 1.1 Q4:
    AP ⊥ BC, seg AD || seg BC.
    ΔABC and ΔBCD share base BC and lie between parallel lines AD and BC.
    """
    title_xml = f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Parallel line top (containing A and D) -->
  <line x1="30" y1="50" x2="330" y2="50" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5,5"/>
  <text x="345" y="54" fill="#64748b" font-size="11" font-family="sans-serif">line l₁</text>
  <!-- Parallel line bottom (containing B and C) -->
  <line x1="30" y1="150" x2="330" y2="150" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5,5"/>
  <text x="345" y="154" fill="#64748b" font-size="11" font-family="sans-serif">line l₂</text>
  <!-- Base BC -->
  <line x1="90" y1="150" x2="270" y2="150" stroke="#f8fafc" stroke-width="2.5"/>
  <!-- Triangle ABC -->
  <line x1="110" y1="50" x2="90" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <line x1="110" y1="50" x2="270" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <!-- Triangle DBC -->
  <line x1="220" y1="50" x2="90" y2="150" stroke="#34d399" stroke-width="2"/>
  <line x1="220" y1="50" x2="270" y2="150" stroke="#34d399" stroke-width="2"/>
  <!-- Altitude AP ⊥ BC -->
  <line x1="110" y1="50" x2="110" y2="150" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <polyline points="110,138 122,138 122,150" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <!-- Altitude DQ ⊥ BC (equal height) -->
  <line x1="220" y1="50" x2="220" y2="150" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <polyline points="220,138 232,138 232,150" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <!-- Vertices -->
  <circle cx="110" cy="50" r="3.5" fill="#38bdf8"/>
  <circle cx="220" cy="50" r="3.5" fill="#34d399"/>
  <circle cx="90" cy="150" r="3.5" fill="#f8fafc"/>
  <circle cx="270" cy="150" r="3.5" fill="#f8fafc"/>
  <circle cx="110" cy="150" r="3" fill="#f43f5e"/>
  <circle cx="220" cy="150" r="3" fill="#f43f5e"/>
  <text x="110" y="38" fill="#38bdf8" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top_l}</text>
  <text x="220" y="38" fill="#34d399" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top_r}</text>
  <text x="75" y="155" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{bot_l}</text>
  <text x="282" y="155" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{bot_r}</text>
  <text x="110" y="166" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">P</text>
  <text x="220" y="166" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif" text-anchor="middle">Q</text>
  <text x="180" y="186" fill="#fbbf24" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">seg {top_l}{top_r} ∥ seg {bot_l}{bot_r}  (h₁ = h₂)</text>"""
    return wrap_svg(inner, 380, 200)


def svg_practice_set_1_1_q5():
    """
    Practice Set 1.1 Q5:
    In ΔABC, PQ ⊥ BC, AD ⊥ BC.
    P on AB, Q and D on BC.
    Shows ΔPQB, ΔPBC, ΔABC, ΔADC.
    """
    inner = """  <!-- Main Triangle ABC -->
  <polygon points="170,40 50,160 310,160" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Altitude AD ⊥ BC -->
  <line x1="170" y1="40" x2="170" y2="160" stroke="#f43f5e" stroke-width="2"/>
  <polyline points="170,148 182,148 182,160" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <!-- Point P on AB -->
  <!-- AB runs from (170,40) to (50,160), dx=-120, dy=120. Midpoint at (110,100) -->
  <!-- Perpendicular PQ ⊥ BC from (110,100) down to (110,160) -->
  <line x1="110" y1="100" x2="110" y2="160" stroke="#34d399" stroke-width="2"/>
  <polyline points="110,148 122,148 122,160" fill="none" stroke="#34d399" stroke-width="1.3"/>
  <!-- Segment PC to show ΔPBC -->
  <line x1="110" y1="100" x2="310" y2="160" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Vertices -->
  <circle cx="170" cy="40" r="3.5" fill="#f8fafc"/>
  <circle cx="50" cy="160" r="3.5" fill="#f8fafc"/>
  <circle cx="310" cy="160" r="3.5" fill="#f8fafc"/>
  <circle cx="110" cy="100" r="3.5" fill="#34d399"/>
  <circle cx="110" cy="160" r="3" fill="#34d399"/>
  <circle cx="170" cy="160" r="3" fill="#f43f5e"/>
  <text x="170" y="30" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="35" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="322" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="96" y="98" fill="#34d399" font-size="13" font-weight="bold" font-family="sans-serif">P</text>
  <text x="110" y="176" fill="#34d399" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Q</text>
  <text x="170" y="176" fill="#f43f5e" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">D</text>
  <!-- Summary badge -->
  <text x="180" y="196" fill="#94a3b8" font-size="10" font-weight="600" font-family="sans-serif" text-anchor="middle">PQ ⊥ BC  and  AD ⊥ BC</text>"""
    return wrap_svg(inner, 360, 210)


def svg_median_triangle(top='A', b_left='B', mid='M', b_right='C', title=""):
    """
    Triangle with median AM dividing base BC into two equal halves BM = MC.
    """
    title_xml = f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Main Triangle ABC -->
  <polygon points="180,45 50,165 310,165" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Median AM to midpoint M(180,165) -->
  <line x1="180" y1="45" x2="180" y2="165" stroke="#f59e0b" stroke-width="2.2"/>
  <!-- Equal tick marks on BM and MC -->
  <line x1="112" y1="160" x2="118" y2="170" stroke="#f8fafc" stroke-width="2"/>
  <line x1="242" y1="160" x2="248" y2="170" stroke="#f8fafc" stroke-width="2"/>
  <!-- Vertices -->
  <circle cx="180" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="50" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="310" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="180" cy="165" r="3.5" fill="#f59e0b"/>
  <text x="180" y="34" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top}</text>
  <text x="35" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{b_left}</text>
  <text x="322" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{b_right}</text>
  <text x="180" y="182" fill="#f59e0b" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{mid}</text>
  <!-- Labels -->
  <text x="115" y="196" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b_left}{mid} = {mid}{b_right}</text>
  <text x="245" y="196" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">seg {top}{mid} is Median</text>"""
    return wrap_svg(inner, 360, 210)


def svg_trapezium_diagonals(title=""):
    """
    Trapezium ABCD with AB || CD and diagonals AC and BD intersecting at P.
    """
    title_xml = f'  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Trapezium ABCD (AB || CD) -->
  <polygon points="120,50 240,50 310,160 50,160" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Diagonals AC and BD intersecting at P(180, 105) -->
  <line x1="120" y1="50" x2="310" y2="160" stroke="#f472b6" stroke-width="1.8"/>
  <line x1="240" y1="50" x2="50" y2="160" stroke="#f472b6" stroke-width="1.8"/>
  <!-- Intersection P -->
  <circle cx="180" cy="105" r="3.5" fill="#fbbf24"/>
  <!-- Vertices -->
  <circle cx="120" cy="50" r="3.5" fill="#f8fafc"/>
  <circle cx="240" cy="50" r="3.5" fill="#f8fafc"/>
  <circle cx="50" cy="160" r="3.5" fill="#f8fafc"/>
  <circle cx="310" cy="160" r="3.5" fill="#f8fafc"/>
  <text x="115" y="40" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">A</text>
  <text x="245" y="40" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="35" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">D</text>
  <text x="325" y="165" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="195" y="105" fill="#fbbf24" font-size="13" font-weight="bold" font-family="sans-serif">P</text>
  <text x="180" y="185" fill="#38bdf8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">seg AB ∥ seg DC</text>"""
    return wrap_svg(inner, 360, 200)


def svg_collinear_three_segments(top='A', b_left='B', d='D', e='E', b_right='C', len_bd='2', len_de='3', len_ec='4', title=""):
    """
    Triangle ABC with points D and E on base BC.
    Cevians AD and AE divide BC into three segments.
    """
    title_xml = f'  <text x="180" y="22" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Main Triangle ABC -->
  <polygon points="170,42 40,165 320,165" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Cevians AD and AE -->
  <line x1="170" y1="42" x2="110" y2="165" stroke="#34d399" stroke-width="1.8"/>
  <line x1="170" y1="42" x2="220" y2="165" stroke="#f472b6" stroke-width="1.8"/>
  <!-- Vertices -->
  <circle cx="170" cy="42" r="3.5" fill="#f8fafc"/>
  <circle cx="40" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="110" cy="165" r="3.5" fill="#34d399"/>
  <circle cx="220" cy="165" r="3.5" fill="#f472b6"/>
  <circle cx="320" cy="165" r="3.5" fill="#f8fafc"/>
  <text x="170" y="32" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top}</text>
  <text x="28" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{b_left}</text>
  <text x="110" y="180" fill="#34d399" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{d}</text>
  <text x="220" y="180" fill="#f472b6" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">{e}</text>
  <text x="332" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{b_right}</text>
  <!-- Length markings -->
  <text x="75" y="196" fill="#34d399" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{b_left}{d} = {len_bd}</text>
  <text x="165" y="196" fill="#f59e0b" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{d}{e} = {len_de}</text>
  <text x="270" y="196" fill="#f472b6" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{e}{b_right} = {len_ec}</text>"""
    return wrap_svg(inner, 360, 210)


def svg_quadrilateral_common_diagonal(top='B', bot='D', left='A', right='C', h_top='6', h_bot='9', title=""):
    """
    Quadrilateral ABCD with common diagonal AC.
    Altitudes BP ⊥ AC (from top B) and DQ ⊥ AC (from bottom D).
    """
    title_xml = f'  <text x="180" y="20" fill="#94a3b8" font-size="11" font-weight="600" font-family="sans-serif" text-anchor="middle">{title}</text>\n' if title else ""
    inner = f"""{title_xml}  <!-- Quadrilateral ABCD -->
  <polygon points="40,105 160,40 320,105 180,175" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Common Diagonal AC -->
  <line x1="40" y1="105" x2="320" y2="105" stroke="#f8fafc" stroke-width="2.2"/>
  <!-- Altitude BP ⊥ AC from B(160,40) down to (160,105) -->
  <line x1="160" y1="40" x2="160" y2="105" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="3,3"/>
  <polyline points="160,93 172,93 172,105" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <!-- Altitude DQ ⊥ AC from D(180,175) up to (180,105) -->
  <line x1="180" y1="175" x2="180" y2="105" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="3,3"/>
  <polyline points="180,117 192,117 192,105" fill="none" stroke="#fbbf24" stroke-width="1.3"/>
  <!-- Vertices -->
  <circle cx="40" cy="105" r="3.5" fill="#f8fafc"/>
  <circle cx="160" cy="40" r="3.5" fill="#f8fafc"/>
  <circle cx="320" cy="105" r="3.5" fill="#f8fafc"/>
  <circle cx="180" cy="175" r="3.5" fill="#f8fafc"/>
  <circle cx="160" cy="105" r="3" fill="#f43f5e"/>
  <circle cx="180" cy="105" r="3" fill="#fbbf24"/>
  <text x="25" y="109" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{left}</text>
  <text x="160" y="30" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{top}</text>
  <text x="332" y="109" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">{right}</text>
  <text x="180" y="195" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">{bot}</text>
  <text x="146" y="100" fill="#f43f5e" font-size="11" font-weight="bold" font-family="sans-serif">P</text>
  <text x="194" y="120" fill="#fbbf24" font-size="11" font-weight="bold" font-family="sans-serif">Q</text>
  <!-- Labels -->
  <text x="135" y="70" fill="#f43f5e" font-size="11" font-weight="600" font-family="sans-serif">BP = {h_top}</text>
  <text x="205" y="150" fill="#fbbf24" font-size="11" font-weight="600" font-family="sans-serif">DQ = {h_bot}</text>
  <text x="75" y="125" fill="#f8fafc" font-size="11" font-weight="600" font-family="sans-serif">Common base AC</text>"""
    return wrap_svg(inner, 360, 205)
