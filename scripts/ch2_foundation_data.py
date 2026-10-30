import json

def get_foundation_questions():
    foundation_data = [
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <rect x="40" y="160" width="260" height="15" fill="#334155"/>
  <rect x="120" y="110" width="70" height="50" rx="4" fill="#38bdf8"/>
  <text x="145" y="140" fill="#0f172a" font-size="12" font-weight="bold">m</text>
  <!-- Force at angle theta -->
  <line x1="190" y1="135" x2="270" y2="75" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="275,72 263,75 268,85" fill="#f59e0b"/>
  <text x="260" y="65" fill="#f59e0b" font-size="12" font-weight="bold">F</text>
  <!-- Horizontal displacement line -->
  <line x1="190" y1="135" x2="270" y2="135" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <path d="M 220 135 A 30 30 0 0 0 215 117" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="230" y="125" fill="#f59e0b" font-size="11">theta</text>
  <!-- Displacement vector -->
  <line x1="120" y1="185" x2="220" y2="185" stroke="#22c55e" stroke-width="2"/>
  <polygon points="225,185 215,180 215,190" fill="#22c55e"/>
  <text x="160" y="205" fill="#22c55e" font-size="11" font-weight="bold">Displacement (s)</text>
</svg>
</div>
A constant pulling force \(F\) acts on a block of mass \(m\) at an angle \(\theta\) to the horizontal surface as shown. What is the formula for the work done in moving the block horizontally through distance \(s\)?""",
            "options": [
                {"text": "\(W = F s \cos\theta\)", "isCorrect": True},
                {"text": "\(W = F s \sin\theta\)", "isCorrect": False},
                {"text": "\(W = F s \tan\theta\)", "isCorrect": False},
                {"text": "\(W = \frac{F s}{\cos\theta}\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The effective component of force in the direction of displacement is \(F \cos\theta\).\n• Therefore, Work done is \(W = (F \cos\theta) \times s = F s \cos\theta\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Porter carrying luggage -->
  <line x1="40" y1="180" x2="300" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="150" cy="90" r="12" fill="#e2e8f0"/>
  <!-- Luggage on head -->
  <rect x="135" y="60" width="30" height="18" rx="2" fill="#f59e0b"/>
  <text x="140" y="73" fill="#0f172a" font-size="9" font-weight="bold">25kg</text>
  <!-- Upward lifting force -->
  <line x1="150" y1="60" x2="150" y2="20" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="150,15 145,25 155,25" fill="#38bdf8"/>
  <text x="155" y="30" fill="#38bdf8" font-size="11" font-weight="bold">F_upward</text>
  <!-- Horizontal walk -->
  <line x1="150" y1="140" x2="230" y2="140" stroke="#22c55e" stroke-width="3"/>
  <polygon points="235,140 225,135 225,145" fill="#22c55e"/>
  <text x="175" y="130" fill="#22c55e" font-size="11" font-weight="bold">Displacement (s)</text>
  <text x="155" y="90" fill="#ef4444" font-size="12" font-weight="bold">theta = 90 deg</text>
</svg>
</div>
A railway porter carries a heavy 25 kg bag on his head and walks horizontally across the platform for 50 metres at steady speed. In the scientific physics sense, how much work is done by the porter's vertical supporting force on the bag?""",
            "options": [
                {"text": "0 Joules (zero work because force is perpendicular to displacement)", "isCorrect": True},
                {"text": "12,250 Joules", "isCorrect": False},
                {"text": "1,250 Joules", "isCorrect": False},
                {"text": "6,125 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The porter exerts a vertical upward force to support the bag against gravity.\n• The displacement is along the horizontal platform.\n• The angle between force and displacement is \(\theta = 90^\circ\).\n• \(W = F s \cos(90^\circ) = 0\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <rect x="40" y="170" width="260" height="15" fill="#334155"/>
  <!-- Braking vehicle -->
  <rect x="130" y="125" width="80" height="35" rx="4" fill="#ef4444"/>
  <text x="145" y="147" fill="#ffffff" font-size="11" font-weight="bold">Car skidding</text>
  <!-- Forward motion arrow -->
  <line x1="210" y1="142" x2="270" y2="142" stroke="#22c55e" stroke-width="3"/>
  <polygon points="275,142 265,137 265,147" fill="#22c55e"/>
  <text x="220" y="132" fill="#22c55e" font-size="10" font-weight="bold">Motion (s)</text>
  <!-- Backward friction arrow -->
  <line x1="130" y1="165" x2="70" y2="165" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="65,165 75,160 75,170" fill="#f59e0b"/>
  <text x="65" y="155" fill="#f59e0b" font-size="10" font-weight="bold">Friction (f)</text>
  <text x="140" y="205" fill="#94a3b8" font-size="11">theta = 180 deg</text>
</svg>
</div>
When brakes are slammed and a car skids forward along a road, what type of work is done by the kinetic friction force on the car?""",
            "options": [
                {"text": "Negative work (W < 0 because friction opposes displacement)", "isCorrect": True},
                {"text": "Positive work (W > 0)", "isCorrect": False},
                {"text": "Zero work (W = 0)", "isCorrect": False},
                {"text": "Infinite work", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Kinetic friction acts in the direction opposite to displacement (\(\theta = 180^\circ\)).\n• \(W = F s \cos(180^\circ) = -F s < 0\), which is negative work that dissipates kinetic energy into heat.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">F (N)</text>
  <!-- Force displacement rectangle -->
  <polygon points="40,180 40,80 200,80 200,180" fill="#38bdf8" fill-opacity="0.3"/>
  <line x1="40" y1="80" x2="200" y2="80" stroke="#38bdf8" stroke-width="3"/>
  <line x1="200" y1="80" x2="200" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="90" y="135" fill="#38bdf8" font-size="12" font-weight="bold">Work Done = Area</text>
  <text x="15" y="85" fill="#64748b" font-size="10">20 N</text>
  <text x="190" y="195" fill="#64748b" font-size="10">5 m</text>
</svg>
</div>
The figure displays a force versus displacement (F-s) graph for a body pushed along a straight track. What is the total work done on the body between \(s = 0\) and \(s = 5\text{ m}\)?""",
            "options": [
                {"text": "100 Joules", "isCorrect": True},
                {"text": "25 Joules", "isCorrect": False},
                {"text": "50 Joules", "isCorrect": False},
                {"text": "200 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Work done is the area under the force-displacement graph.\n• Area of rectangle \(= \text{Force} \times \text{Displacement} = 20\text{ N} \times 5\text{ m} = 100\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">F (N)</text>
  <!-- Linearly increasing force: Triangle -->
  <polygon points="40,180 200,60 200,180" fill="#10b981" fill-opacity="0.3"/>
  <line x1="40" y1="180" x2="200" y2="60" stroke="#10b981" stroke-width="3"/>
  <line x1="200" y1="60" x2="200" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="15" y="65" fill="#64748b" font-size="10">30 N</text>
  <text x="195" y="195" fill="#64748b" font-size="10">4 m</text>
  <text x="95" y="150" fill="#10b981" font-size="11" font-weight="bold">Triangle Area</text>
</svg>
</div>
A variable spring force increases uniformly from 0 to 30 N over a stretching distance of 4 m. What is the work performed in stretching the spring?""",
            "options": [
                {"text": "60 Joules", "isCorrect": True},
                {"text": "120 Joules", "isCorrect": False},
                {"text": "30 Joules", "isCorrect": False},
                {"text": "7.5 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• For a triangular force-displacement profile, \(\text{Work} = \text{Area of triangle} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 4 \times 30 = 60\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circular orbit -->
  <circle cx="170" cy="115" r="70" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
  <circle cx="170" cy="115" r="15" fill="#38bdf8"/>
  <text x="157" y="119" fill="#0f172a" font-size="9" font-weight="bold">Earth</text>
  <!-- Satellite at top -->
  <circle cx="170" cy="45" r="7" fill="#f59e0b"/>
  <!-- Radial gravitational force -->
  <line x1="170" y1="45" x2="170" y2="85" stroke="#ef4444" stroke-width="2.5"/>
  <polygon points="170,90 166,80 174,80" fill="#ef4444"/>
  <text x="175" y="75" fill="#ef4444" font-size="10">F_g</text>
  <!-- Tangential velocity/displacement -->
  <line x1="170" y1="45" x2="110" y2="45" stroke="#22c55e" stroke-width="2.5"/>
  <polygon points="105,45 115,40 115,50" fill="#22c55e"/>
  <text x="110" y="35" fill="#22c55e" font-size="10">Δs</text>
  <text x="175" y="40" fill="#94a3b8" font-size="11">theta = 90 deg</text>
</svg>
</div>
A telecommunication satellite revolves in a circular geostationary orbit around the Earth. What is the total work done by Earth's gravitational pull on the satellite during a 24-hour orbital cycle?""",
            "options": [
                {"text": "0 Joules", "isCorrect": True},
                {"text": "Positive work equal to satellite's potential energy", "isCorrect": False},
                {"text": "Negative work equal to satellite's kinetic energy", "isCorrect": False},
                {"text": "100,000 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In circular orbit, the gravitational pull acts as the centripetal force directed towards Earth's centre.\n• Instantaneous displacement is tangential, so \(\theta = 90^\circ\).\n• \(W = F s \cos(90^\circ) = 0\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Inclined plane -->
  <polygon points="40,180 260,180 260,80" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- Block on incline sliding down -->
  <rect x="135" y="105" width="45" height="28" rx="3" transform="rotate(22.6 157 119)" fill="#38bdf8"/>
  <text x="155" y="125" fill="#0f172a" font-size="10" font-weight="bold">m</text>
  <!-- Gravity component along incline -->
  <line x1="170" y1="130" x2="220" y2="152" stroke="#22c55e" stroke-width="2.5"/>
  <polygon points="225,154 214,148 219,158" fill="#22c55e"/>
  <text x="210" y="140" fill="#22c55e" font-size="10">mg sintheta</text>
  <text x="70" y="175" fill="#f59e0b" font-size="11">theta</text>
</svg>
</div>
A block of mass \(m\) slides down a frictionless incline of angle \(\theta\). What is the work done by the normal contact force exerted by the ramp on the block?""",
            "options": [
                {"text": "0 Joules (normal reaction is perpendicular to the inclined ramp)", "isCorrect": True},
                {"text": "\(m g h\)", "isCorrect": False},
                {"text": "\(m g s \sin\theta\)", "isCorrect": False},
                {"text": "\(-m g s \cos\theta\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The normal force acts strictly perpendicular to the ramp's surface (\(\theta = 90^\circ\) relative to displacement along the ramp).\n• Hence, work done by normal force is always zero: \(W_N = 0\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Stone thrown up -->
  <line x1="40" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="170" cy="150" r="10" fill="#38bdf8"/>
  <!-- Upward displacement arrow -->
  <line x1="170" y1="135" x2="170" y2="70" stroke="#22c55e" stroke-width="3"/>
  <polygon points="170,65 165,75 175,75" fill="#22c55e"/>
  <text x="180" y="90" fill="#22c55e" font-size="11" font-weight="bold">Displacement (s)</text>
  <!-- Downward gravity arrow -->
  <line x1="170" y1="165" x2="170" y2="215" stroke="#ef4444" stroke-width="3"/>
  <polygon points="170,220 165,210 175,210" fill="#ef4444"/>
  <text x="180" y="210" fill="#ef4444" font-size="11" font-weight="bold">Gravity (mg)</text>
</svg>
</div>
A 2 kg stone is thrown vertically upwards and ascends through a height of 5 metres. What is the work done by the gravitational force on the stone during this upward ascent? (Take \(g = 10\text{ m/s}^2\))""",
            "options": [
                {"text": "-100 Joules", "isCorrect": True},
                { "text": "+100 Joules", "isCorrect": False},
                {"text": "0 Joules", "isCorrect": False},
                {"text": "-50 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Force \(F = mg = 2 \times 10 = 20\text{ N}\) directed downwards.\n• Displacement \(s = 5\text{ m}\) directed upwards (\(\theta = 180^\circ\)).\n• \(W = F s \cos(180^\circ) = 20 \times 5 \times (-1) = -100\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Work sign summary dial -->
  <circle cx="170" cy="115" r="70" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <line x1="170" y1="115" x2="240" y2="115" stroke="#38bdf8" stroke-width="2"/>
  <line x1="170" y1="115" x2="170" y2="45" stroke="#94a3b8" stroke-width="2"/>
  <line x1="170" y1="115" x2="100" y2="115" stroke="#f43f5e" stroke-width="2"/>
  <text x="210" y="105" fill="#22c55e" font-size="10" font-weight="bold">theta=0 deg (W>0)</text>
  <text x="145" y="35" fill="#eab308" font-size="10" font-weight="bold">theta=90 deg (W=0)</text>
  <text x="75" y="105" fill="#f43f5e" font-size="10" font-weight="bold">theta=180 deg (W<0)</text>
</svg>
</div>
Under which condition of the angle \(\theta\) between force and displacement is the work done strictly positive?""",
            "options": [
                {"text": "When theta is an acute angle (0 deg ≤ theta < 90 deg)", "isCorrect": True},
                {"text": "When theta = 90 deg exactly", "isCorrect": False},
                {"text": "When theta is an obtuse angle (90 deg < theta ≤ 180 deg)", "isCorrect": False},
                {"text": "When theta = 180 deg exactly", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \(\cos\theta > 0\) for \(0^\circ \le \theta < 90^\circ\) (acute angles), yielding positive work.\n• At \(\theta = 90^\circ\), \(W = 0\).\n• For \(90^\circ < \theta \le 180^\circ\), \(\cos\theta < 0\), yielding negative work.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Simple pendulum -->
  <line x1="170" y1="30" x2="170" y2="180" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="170" y1="30" x2="225" y2="150" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="225" cy="150" r="10" fill="#38bdf8"/>
  <!-- Tangent velocity arrow -->
  <line x1="225" y1="150" x2="255" y2="110" stroke="#22c55e" stroke-width="2.5"/>
  <polygon points="258,106 248,112 255,119" fill="#22c55e"/>
  <text x="245" y="95" fill="#22c55e" font-size="10">Velocity</text>
  <text x="180" y="100" fill="#f59e0b" font-size="10">Tension (T)</text>
</svg>
</div>
During the swing of a simple pendulum, what is the work done by the tension in the string on the bob?""",
            "options": [
                {"text": "0 Joules (tension is always perpendicular to the instantaneous tangential displacement)", "isCorrect": True},
                {"text": "Equal to kinetic energy at lowest point", "isCorrect": False},
                {"text": "Equal to gravitational potential energy at highest point", "isCorrect": False},
                {"text": "Negative work proportional to string length", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Tension always acts along the string towards the suspension pivot (radial).\n• The bob's displacement is along the circular arc (tangential).\n• Since radial and tangential directions are mutually perpendicular (\(\theta = 90^\circ\)), work done by tension is identically zero throughout the swing.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">F (N)</text>
  <!-- Trapezium force-displacement -->
  <polygon points="40,180 40,100 140,60 260,60 260,180" fill="#a855f7" fill-opacity="0.3"/>
  <line x1="40" y1="100" x2="140" y2="60" stroke="#a855f7" stroke-width="3"/>
  <line x1="140" y1="60" x2="260" y2="60" stroke="#a855f7" stroke-width="3"/>
  <line x1="140" y1="60" x2="140" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <line x1="260" y1="60" x2="260" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="15" y="105" fill="#64748b" font-size="10">10</text>
  <text x="15" y="65" fill="#64748b" font-size="10">20</text>
  <text x="135" y="195" fill="#64748b" font-size="10">2</text>
  <text x="255" y="195" fill="#64748b" font-size="10">5</text>
</svg>
</div>
From the force-displacement graph above, what is the total work done on the object from \(s = 0\) to \(s = 5\text{ m}\)?""",
            "options": [
                {"text": "90 Joules", "isCorrect": True},
                {"text": "100 Joules", "isCorrect": False},
                {"text": "80 Joules", "isCorrect": False},
                {"text": "60 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Area from 0 to 2 m (trapezium) \(= \frac{10 + 20}{2} \times 2 = 30\text{ J}\).\n• Area from 2 to 5 m (rectangle) \(= (5 - 2) \times 20 = 3 \times 20 = 60\text{ J}\).\n• Total Work \(= 30 + 60 = 90\text{ J}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <rect x="50" y="170" width="240" height="20" fill="#334155"/>
  <!-- Pushing a solid concrete wall -->
  <rect x="220" y="60" width="40" height="110" fill="#64748b"/>
  <circle cx="150" cy="115" r="12" fill="#38bdf8"/>
  <!-- Arms pushing wall -->
  <line x1="160" y1="120" x2="220" y2="120" stroke="#38bdf8" stroke-width="4"/>
  <text x="120" y="100" fill="#38bdf8" font-size="11">Pushing F = 500 N</text>
  <text x="225" y="50" fill="#f43f5e" font-size="11" font-weight="bold">Rigid Wall (s = 0)</text>
</svg>
</div>
A person pushes against a solid concrete wall with a large force of 500 N for 10 minutes until completely exhausted. The wall does not move at all (\(s = 0\)). What is the scientific work done on the wall?""",
            "options": [
                {"text": "0 Joules (no displacement means zero work performed on the wall)", "isCorrect": True},
                {"text": "500 Joules", "isCorrect": False},
                {"text": "5,000 Joules", "isCorrect": False},
                {"text": "300,000 Joules", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In physics, \(W = F \times s\).\n• Because the wall is completely stationary, \(s = 0\), so \(W = 500 \times 0 = 0\text{ J}\).\n• (Muscles tire because of internal physiological work, but external work on the wall is zero).\nCorrect Choice is (A)."
        }
    ]
    return foundation_data
