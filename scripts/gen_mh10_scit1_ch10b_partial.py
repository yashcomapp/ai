"""
SSOT Top-Up Generator: MH Class 10 Science & Technology Part 1 (MH-10-SCIT1)
Chapter 10 Space Missions — Part B (7 partial subtopics x 80 = 560 Qs)
Subtopics: 10.3.2, 10.3.3, 10.4.1, 10.4.2, 10.5.1, 10.5.2, 10.5.3
"""
import json
from pathlib import Path
from ssot_mh10_scit_builder import validate_pack_collection
from gen_mh10_scit1_ch10a_partial import _sat_pack


def main():
    specs = [
        ("MH-10-SCIT1-10-10.3.2", "Medium Earth Orbits (MEO)",
         "Host global navigation constellations (like GPS) and polar/elliptical communications",
         "GPS (20,200 km) and Galileo / GLONASS navigation satellites",
         "Height between 2,000 km and 35,786 km above Earth's surface, period ~2 to 24 hours",
         "Atomic clocks and L-band navigation transmitters", 1032),
        ("MH-10-SCIT1-10-10.3.3", "Low Earth Orbits (LEO)",
         "Host space stations, telescopes, and high-resolution Earth observation satellites",
         "International Space Station (ISS), Hubble Space Telescope, and IRS / Cartosat",
         "Height between 180 km and 2,000 km above Earth's surface, orbital period ~90 minutes",
         "High-resolution optical/IR telescopes, microgravity labs, and SAR imagers", 1033),
        ("MH-10-SCIT1-10-10.4.1", "Rocket Propulsion (Newton 3rd Law & Momentum Conservation)",
         "Generate upward thrust by expelling high-velocity hot exhaust gases downward (Newton's 3rd Law & conservation of momentum)",
         "PSLV, GSLV Mk-III (LVM3), and Sounding Rockets",
         "Vertical ascent through atmosphere into LEO/GTO/deep space",
         "Solid, liquid, and cryogenic (LH2 + LOX) rocket engines and oxidizers", 1041),
        ("MH-10-SCIT1-10-10.4.2", "Multi-Stage Rocket Fuel Stages Detachment",
         "Drop empty spent fuel tanks/stages sequentially to reduce dead mass and achieve orbital velocity (~7.8–11.2 km/s)",
         "PSLV (4-stage rocket) and LVM3 (3-stage rocket)",
         "Sequential stage separation during ascent to LEO, GTO, or escape trajectory",
         "Interstage separation pyrotechnics, strap-on boosters, and upper cryogenic stage", 1042),
        ("MH-10-SCIT1-10-10.5.1", "Chandrayaan Lunar Missions (Chandrayaan-1, 2, and 3)",
         "Explore the Moon's surface, south pole, and water/ice molecules (Chandrayaan-1 discovered lunar water molecules; Chandrayaan-3 achieved historic lunar south-pole soft landing)",
         "Chandrayaan-1 (2008), Chandrayaan-2 (2019), and Chandrayaan-3 (2023 Vikram lander + Pragyan rover)",
         "Lunar Polar Orbit (~100 km) and Lunar South Pole surface",
         "Moon Mineralogy Mapper (M3), Moon Impact Probe, Vikram lander, and Pragyan rover", 1051),
        ("MH-10-SCIT1-10-10.5.2", "Mangalyaan (Mars Orbiter Mission — MOM, 2013)",
         "Study Martian atmosphere, methane, and surface morphology — making India the first nation to reach Mars orbit on its maiden attempt",
         "Mangalyaan / Mars Orbiter Mission (MOM, launched Nov 2013 via PSLV-XL C25)",
         "Highly elliptical Mars Orbit around the Red Planet",
         "Mars Colour Camera (MCC), Methane Sensor for Mars (MSM), and Thermal Infrared Spectrometer", 1052),
        ("MH-10-SCIT1-10-10.5.3", "Space Debris Hazards & Mitigation",
         "Assess collision risks from defunct satellites, spent rocket stages, and paint flecks (~28,000 km/h) and apply mitigation (de-orbiting, graveyard orbits, passivation)",
         "ISRO's NETRA (Network for Space Object Tracking and Analysis) and IADC guidelines",
         "Congested LEO (~700–1,000 km) and GEO graveyard orbits",
         "Ground tracking radars/telescopes, collision-avoidance thrusters, and de-orbit drag sails", 1053),
    ]
    all_qs = []
    for sp in specs:
        all_qs.extend(_sat_pack(*sp))
    validate_pack_collection(all_qs)
    out_path = Path(__file__).parent / "audit_data" / "mh10_scit1_ch10b_partial.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(all_qs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"SUCCESS SCIT1 Ch.10b partial pool: {len(all_qs)} questions across 7 subtopics -> {out_path}")


if __name__ == "__main__":
    main()
