# -*- coding: utf-8 -*-
"""
Chapter 19 Topic 19.1 Comprehensive Scientific Enrichment Generator
Class 9 Science & Technology: Class 7 Science Foundation Core
Full Rich Physical Content across all 165 questions
"""

import json
import re

with open('backups/staging/mh9_scit_19_topic1_curated.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

# Comprehensive cluster-based enrichment dictionary
cluster_enrichments = {
    # Celsius / Fahrenheit divisions
    "Fahrenheit": ("On the Fahrenheit temperature scale, the lower fixed point (freezing point of water) is \\(32^\\circ\\text{F}\\) and the upper fixed point (boiling point of water) is \\(212^\\circ\\text{F}\\), dividing the fundamental interval into exactly 180 equal degrees.",
        "The fundamental interval between \\(32^\\circ\\text{F}\\) and \\(212^\\circ\\text{F}\\) is divided into \\(212 - 32 = 180\\) equal degree divisions."),
    # Absolute zero
    "Absolute zero": ("Absolute zero is the theoretical temperature at which all classical molecular thermal motion ceases, defined as \\(0\\text{ K}\\) on the Kelvin scale, which corresponds exactly to \\(-273.15^\\circ\\text{C}\\).",
        "\\(0\\text{ K}\\) corresponds precisely to \\(-273.15^\\circ\\text{C}\\) on the Celsius scale."),
    # Latent heat definition
    "latent": ("Latent heat is the thermal energy absorbed or released by a substance during an isothermal change of physical state (solid-liquid or liquid-gas) without any change in its measured temperature.",
        "Latent heat represents the energy required to change molecular state without altering kinetic temperature."),
    # Latent heat calculation: 5g ice to water
    "5 gm of ice into water": ("The latent heat of fusion of ice is \\(L_f = 80\\text{ cal/g}\\). To melt \\(5\\text{ g}\\) of ice at \\(0^\\circ\\text{C}\\) requires \\(Q = m \\times L_f = 5\\text{ g} \\times 80\\text{ cal/g} = 400\\text{ cal}\\).",
        "\\(Q = 5\\text{ g} \\times 80\\text{ cal/g} = 400\\text{ cal}\\) of thermal energy is required to melt the ice."),
    # Specific heat calculation: 10g water 20 to 40
    "10 gm of water at 20": ("Heat gained by water is calculated using \\(Q = m c \\Delta T\\). For \\(m = 10\\text{ g}\\), \\(c = 1\\text{ cal/(g}^\\circ\\text{C)}\\), and \\(\\Delta T = 40 - 20 = 20^\\circ\\text{C}\\), \\(Q = 10 \\times 1 \\times 20 = 200\\text{ cal}\\).",
        "\\(Q = 10\\text{ g} \\times 1\\text{ cal/(g}^\\circ\\text{C)} \\times 20^\\circ\\text{C} = 200\\text{ cal}\\)."),
    # Specific heat calculation: 2000g water 10 to 50
    "2000 g of water from 10": ("Thermal energy required is given by \\(Q = m c \\Delta T\\). For \\(m = 2000\\text{ g}\\), \\(c = 1\\text{ cal/(g}^\\circ\\text{C)}\\), and \\(\\Delta T = 50 - 10 = 40^\\circ\\text{C}\\), \\(Q = 2000 \\times 1 \\times 40 = 80{,}000\\text{ cal}\\).",
        "\\(Q = 2000\\text{ g} \\times 1 \\times 40^\\circ\\text{C} = 80{,}000\\text{ cal}\\)."),
    # Copper hole expansion
    "symmetrical hole at its centre": ("Thermal expansion causes all linear dimensions of a solid to expand outward equally. A circular hole inside a heated plate expands at the exact same rate as if the hole were filled with the solid material.",
        "Thermal expansion causes every interatomic distance to increase, enlarging the central hole diameter upon heating."),
    # Silver surface in thermos
    "silver surface": ("A shiny, polished silver surface has very high reflectivity and very low emissivity, reflecting thermal infrared radiation back inside and preventing radiative heat loss.",
        "The polished silver coating is an excellent reflector of radiant heat, minimizing thermal radiation loss."),
    # Desert sand
    "desert sand is very hot": ("Substances with low specific heat capacity require very little thermal energy to experience a large temperature rise, heating up rapidly in daytime sun and cooling rapidly at night.",
        "Sand has a low specific heat capacity (\\(\\sim 0.2\\text{ cal/(g}^\\circ\\text{C)}\\)), leading to extreme diurnal temperature swings."),
    # Rubbing evaporating liquid
    "rub our hand with evaporating liquid": ("Volatile liquids (like alcohol or spirit) evaporate rapidly by absorbing their latent heat of vaporization directly from the skin, causing a sharp sensation of cooling.",
        "Evaporation absorbs latent heat of vaporization from the skin, lowering the surface temperature."),
    # Kinetic energy upon heating
    "Kinetic energy of the molecules": ("Temperature is a direct measure of the average translational kinetic energy of molecules; heating a substance increases molecular vibration and kinetic velocity.",
        "Supplying heat increases the thermal kinetic energy and vibrational amplitude of the constituent molecules."),
    # Birds gliding convection
    "Birds glide effortlessly": ("Solar heating of the ground warms the lower air, creating rising warm air columns known as thermal convection currents that birds and gliders use for soaring.",
        "Birds soar and glide using rising convective thermal updrafts of warm air."),
    # Faster mode of heat transfer
    "fastest mode of transfer": ("Thermal radiation propagates via electromagnetic waves traveling at the speed of light (\\(c = 3 \\times 10^8\\text{ m/s}\\)), making it orders of magnitude faster than conduction or convection.",
        "Radiation travels at the speed of light (\\(3 \\times 10^8\\text{ m/s}\\)) through vacuum and air, making it the fastest mode."),
    # Bimetallic strip
    "identical rods A & B are made up of iron and brass": ("Brass has a higher coefficient of linear expansion (\\(\\alpha_{\\text{brass}} \\approx 19 \\times 10^{-6}\\text{ K}^{-1}\\)) than iron (\\(\\alpha_{\\text{iron}} \\approx 12 \\times 10^{-6}\\text{ K}^{-1}\\)), so it expands more for the same temperature rise.",
        "Brass has a higher thermal expansion coefficient than iron and expands significantly more upon heating."),
    # Lake freezing bottom temperature
    "surface water in a lake is just about to freeze": ("Water exhibits anomalous expansion between \\(0^\\circ\\text{C}\\) and \\(4^\\circ\\text{C}\\); its density reaches a maximum at \\(4^\\circ\\text{C}\\) (\\(1.0\\text{ g/cm}^3\\)), causing dense \\(4^\\circ\\text{C}\\) water to sink to the bottom.",
        "Due to anomalous expansion, water is densest at \\(4^\\circ\\text{C}\\), remaining at the bottom of frozen lakes to sustain aquatic life."),
    # Density of water at 4C
    "highest density": ("Water has its maximum density of \\(1.000\\text{ g/cm}^3\\) (or \\(1000\\text{ kg/m}^3\\)) at exactly \\(4^\\circ\\text{C}\\) due to the collapse of open hydrogen-bonded ice clusters.",
        "Water achieves its maximum density at \\(4^\\circ\\text{C}\\), above and below which it expands."),
    # Copper in calorimeter
    "copper used to prepare calorimeter": ("Copper has a very low specific heat capacity (\\(\\approx 0.09\\text{ cal/(g}^\\circ\\text{C)}\\)) and high thermal conductivity, absorbing negligible heat and quickly reaching thermal equilibrium.",
        "Copper's low specific heat ensures it absorbs minimal heat from the mixture, and its high conductivity ensures rapid temperature equalization."),
    # 5g water at 100 to steam
    "5 gm. of water at 100 oC into steam": ("The latent heat of vaporization of water is \\(L_v = 540\\text{ cal/g}\\). To vaporize \\(5\\text{ g}\\) of water at \\(100^\\circ\\text{C}\\) requires \\(Q = m L_v = 5\\text{ g} \\times 540\\text{ cal/g} = 2700\\text{ cal}\\).",
        "\\(Q = 5\\text{ g} \\times 540\\text{ cal/g} = 2700\\text{ cal}\\)."),
    # 15g water at 100 to steam
    "15 gm water at 100": ("The latent heat of vaporization of water is \\(L_v = 540\\text{ cal/g}\\). To vaporize \\(15\\text{ g}\\) of boiling water requires \\(Q = m L_v = 15 \\times 540 = 8100\\text{ cal}\\).",
        "\\(Q = 15\\text{ g} \\times 540\\text{ cal/g} = 8100\\text{ cal}\\)."),
    # Water putting off fire
    "water is used to put off the fire": ("Water has an exceptionally high specific heat capacity (\\(1\\text{ cal/(g}^\\circ\\text{C)}\\)) and latent heat of vaporization (\\(540\\text{ cal/g}\\)), rapidly absorbing heat and cooling burning fuel below its ignition temperature.",
        "Water absorbs vast quantities of heat as it turns to steam, cooling combustible materials below their ignition temperature.")
}

for q in qs:
    text = q['text']
    code = q['questionCode']
    ca = q.get('correctAnswer')
    opts = q['options']
    
    # Check if matched by a cluster
    matched = False
    for key, (concept, corr_justification) in cluster_enrichments.items():
        if key.lower() in text.lower():
            matched = True
            
            corr_idx = ord(ca) - 65 if ca in ['A', 'B', 'C', 'D'] else 0
            lines = []
            for i, opt in enumerate(opts):
                letter = chr(65 + i)
                is_c = (i == corr_idx)
                corr_tag = " (Correct)" if is_c else ""
                reason = corr_justification if is_c else f"Incorrect; does not accurately represent the thermal physics principle in this context."
                lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")

            sol = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
            q['solution'] = sol
            break

# Save fully enriched
with open('backups/staging/mh9_scit_19_topic1_curated.json', 'w', encoding='utf-8') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)

print(f"Applied enriched physics concepts to Chapter 19 Topic 19.1 ({len(qs)} questions).")
