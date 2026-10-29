# -*- coding: utf-8 -*-
"""
Chapter 18 - Topic 18.1.1 Solution Generator (87 Qs)
"""
import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    all_qs = json.load(f)

t1_qs = [q for q in all_qs if q.get('topicCode') == 'MH-9-SCIT-18-18.1.1']

solutions = {}

# --- 16 OAR Questions ---
oar_map = {
    "MH-9-SCIT-18-18.1.1-OAR-001": ("""Earth's atmosphere possesses an optical window that transmits visible light wavelengths (400–800 nm) with minimal absorption, allowing ground-based optical telescopes to observe stars.""",
        "True — Optical telescopes can collect visible light at ground level because the atmosphere does not absorb optical frequencies.",
        "True — Diatomic nitrogen, oxygen, and trace gases are transparent to the visible light spectrum.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-002": ("""Gamma rays have extremely short wavelengths (< 0.001 nm) and high photon energy, causing them to be completely absorbed by nitrogen and oxygen molecules in Earth's upper atmosphere.""",
        "True — Ground-based observatories cannot detect direct cosmic gamma rays because none penetrate to sea level.",
        "True — Atmospheric gases absorb ionizing high-energy gamma rays through photoelectric absorption and Compton scattering.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-003": ("""Radio waves have long wavelengths (millimeters to meters) that easily diffract around and penetrate cloud droplets and atmospheric moisture without significant scattering or absorption.""",
        "True — Radio telescopes operate continuously in overcast weather and during daytime.",
        "True — Clouds do not scatter radio frequencies, and the sun's radio emission is distinct from optical glare.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-004": ("""Space telescopes orbit above the Earth's atmosphere, eliminating atmospheric turbulence (scintillation/twinkling), light pollution, and air absorption.""",
        "True — Telescopes in space achieve diffraction-limited resolution without atmospheric blurring.",
        "True — The absence of atmospheric air currents, weather, and scattering preserves pristine wavefront sharpness.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-005": ("""Cosmic bodies emit radiation across the entire electromagnetic spectrum depending on their temperature and physical energetic processes, from radio waves to gamma rays.""",
        "True — Celestial objects are multi-wavelength emitters radiating according to Planck's blackbody law and non-thermal emission.",
        "True — Diverse phenomena like nuclear fusion, magnetic reconnection, and thermal radiation generate different electromagnetic bands.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-006": ("""Rayleigh scattering of sunlight by atmospheric gas molecules creates bright diffuse sky luminance that overpowers the faint light of distant celestial bodies during daytime.""",
        "True — Ground optical telescopes cannot observe faint stellar objects against the brightly illuminated daytime sky.",
        "True — Blue light scattering by air molecules creates sky brightness millions of times brighter than faint stars.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-007": ("""The stratospheric ozone (\\(\\ce{O3}\\)) layer absorbs solar and stellar ultraviolet radiation (wavelengths below 310 nm), necessitating space telescopes for UV astronomy.""",
        "True — UV astronomy cannot be conducted from the ground because celestial UV photons are absorbed in the stratosphere.",
        "True — Photodissociation of ozone molecules absorbs high-energy UV-B and UV-C photons before they reach the ground.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-008": ("""The electromagnetic spectrum is ordered by wavelength; radio waves have the longest wavelengths (meters to kilometers), while visible light is restricted to 400–800 nm.""",
        "True — Radio wavelengths are orders of magnitude larger than sub-micron visible light waves.",
        "True — Radio wavelengths extend from millimeters to hundreds of kilometers in astronomical bands.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-009": ("""Liquid water droplets in dense clouds reflect and scatter optical photons (Mie scattering), making Earth's atmosphere opaque to visible light during stormy weather.""",
        "True — Cloudy and overcast nights prevent visible starlight from reaching ground telescope objectives.",
        "True — Water droplets scatter optical wavelengths randomly, blocking direct starlight transmission.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-010": ("""Multi-wavelength astronomy combines data across all electromagnetic bands (radio to gamma rays) to build a comprehensive physical model of celestial objects and events.""",
        "True — Combining observations across multiple wavebands reveals physical processes invisible in visible light alone.",
        "True — Cold molecular gas radiates in radio/IR, warm stars radiate in optical, and relativistic accretion disks radiate in X-rays/gamma rays.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-011": ("""Because radio wavelengths are thousands of times longer than optical wavelengths, the surface tolerance required for radio dishes is on the order of millimeters rather than nanometers.""",
        "True — Ground radio dishes can be constructed with diameters exceeding 45–100 meters, far larger than optical mirrors.",
        "True — Rayleigh's criterion requires surface accuracy of \\(\\sim \\lambda / 16\\); larger \\(\\lambda\\) permits larger fabrication tolerances.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-012": ("""Earth's atmosphere has an optical depth that completely blocks cosmic X-rays and gamma rays, shielding terrestrial biology but requiring space satellites for high-energy astronomy.""",
        "True — High-energy X-ray and gamma-ray astronomy was impossible before orbital satellites like Chandra and Fermi.",
        "True — The atmosphere provides an absorbing shielding column equivalent to a 10-meter thick water barrier.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-013": ("""Atmospheric dust and rain particles have sizes comparable to optical wavelengths (causing scattering), but are vastly smaller than radio wavelengths, which pass through unhindered.""",
        "True — Radio telescopes can observe celestial targets through rain, fog, and dust clouds.",
        "True — When wavelength is much larger than particle diameter (\\(\\lambda \\gg d\\)), scattering is negligible.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-014": ("""According to Wien's displacement law (\\(\\lambda_{\\text{max}} T = b\\)), the peak emission wavelength of a star's thermal spectrum is inversely proportional to its surface temperature.""",
        "True — Hot stars (30,000 K) appear blue, while cool stars (3,000 K) appear reddish.",
        "True — Higher temperature shifts the blackbody emission spectrum toward shorter, higher-energy wavelengths.",
        "A"),
    "MH-9-SCIT-18-18.1.1-OAR-015": ("""Directly observing the Sun through an unfiltered optical telescope focuses intense concentrated solar flux onto the retina, causing instantaneous and irreversible blindness.""",
        "False — Viewing the Sun through an optical telescope without specialized solar filters is extremely dangerous and strictly prohibited.",
        "True — Concentrated solar visible and infrared radiation causes thermal and photochemical retinal burns.",
        "D"),
    "MH-9-SCIT-18-18.1.1-OAR-016": ("""Positioning observatories on high mountaintops places them above the densest, most humid, and turbulent lower atmospheric layers, reducing optical distortion and seeing blur.""",
        "True — High-altitude observatories (e.g. Mauna Kea, Ladakh) achieve superior resolution and optical transparency.",
        "True — Elevation avoids lower atmospheric water vapor, clouds, and thermal turbulence cells.",
        "A")
}

for code, (concept, a_exp, r_exp, correct_let) in oar_map.items():
    sol = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical optical and atmospheric principles."""
    solutions[code] = sol

print(f"Generated {len(solutions)} OAR solutions.")

# Save temporary mapping
with open('scripts/ch18_t1_sol_data.json', 'w', encoding='utf-8') as f:
    json.dump(solutions, f, indent=2)
