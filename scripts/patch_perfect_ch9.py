# scripts/patch_perfect_ch9.py
# Implements 10 distinct template variations for every archetype in Ch 9 to guarantee 0 collisions.

import json
import math
from scripts.generate_perfect_ch9 import make_opts, svg_cone, svg_sphere, svg_hemi, build_q, TRIPLETS_80, OBJECTS_80, SEQS_80, RADII_80, SPHERE_OBJECTS_80, HEMI_OBJECTS_80, generate_9_1_1, generate_9_1_3, generate_9_1_4

def generate_9_1_2():
    tc = "MH-9-MTH2-9-9.1.2"
    tname = "Curved Surface Area = πrl"
    qs = []
    COAT_ACTIONS = [
        "A technician applies thermal insulation on the outside curved surface of a {obj} with \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\). At ₹{rate} per \\(\\pi\\text{{ m}}^2\\), compute the insulation cost.",
        "A painter coats the lateral surface of a {obj} having radius \\({r}\\text{{ m}}\\) and slant height \\({l}\\text{{ m}}\\) with enamel paint. At ₹{rate} per \\(\\pi\\text{{ m}}^2\\), find the total expenditure.",
        "Waterproofing the exterior curved flank of a {obj} (radius \\({r}\\text{{ m}}\\), slant height \\({l}\\text{{ m}}\\)) costs ₹{rate} per \\(\\pi\\text{{ m}}^2\\). Determine the total budget required.",
        "A craftsman glazes the outer conical face of a {obj} where \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\). If glazing costs ₹{rate} per \\(\\pi\\text{{ m}}^2\\), calculate the overall bill.",
        "Electroplating the curved mantle of a {obj} having dimensions \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\) is priced at ₹{rate} per \\(\\pi\\text{{ m}}^2\\). Find the total charge.",
        "At a contractor rate of ₹{rate} per \\(\\pi\\text{{ m}}^2\\), calculate the expenditure incurred to wrap protective foil around the lateral side of a {obj} with \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\).",
        "A decorative tentmaker paints floral patterns across the slanted face of a {obj} (radius \\({r}\\text{{ m}}\\), slant height \\({l}\\text{{ m}}\\)) at ₹{rate} per \\(\\pi\\text{{ m}}^2\\). What is the total fee?",
        "Protective resin is sprayed on the lateral surface of a {obj} with \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\). At ₹{rate} per \\(\\pi\\text{{ m}}^2\\), what is the total resin cost?",
        "An artisan varnishes the curved outer boundary of a {obj} measuring \\(r = {r}\\text{{ m}}\\) and \\(l = {l}\\text{{ m}}\\). At ₹{rate} per \\(\\pi\\text{{ m}}^2\\), calculate the total cost.",
        "Compute the full painting expense to coat the lateral wall of a {obj} (radius \\({r}\\text{{ m}}\\), slant height \\({l}\\text{{ m}}\\)) at ₹{rate} per \\(\\pi\\text{{ m}}^2\\)."
    ]
    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r, h, l = TRIPLETS_80[idx]
        obj_name, obj_short = OBJECTS_80[idx]
        csa_val = r * l
        has_fig = (idx % 5 != 0)
        svg = svg_cone(f"r = {r} cm", f"h = {h} cm", f"l = {l} cm", f"{obj_name.title()} CSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Determine the curved surface area of a {obj_name} with base radius \\(r = {r}\\text{{ cm}}\\) and slant height \\(l = {l}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({(r * h)}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 10}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 8}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nCurved surface area is \\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A craftsman requires canvas to cover the lateral surface of a {obj_name}. If \\(r = {r}\\text{{ m}}\\) and vertical height \\(h = {h}\\text{{ m}}\\), find the canvas area needed in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({r * h}\\pi\\text{{ m}}^2\\)", f"\\({csa_val + 12}\\pi\\text{{ m}}^2\\)", f"\\({2 * csa_val}\\pi\\text{{ m}}^2\\)", f"\\({csa_val - 15}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ m}}\\).\n**Step 2: Lateral Area**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). If its slant height is \\({l}\\text{{ cm}}\\), what is its base radius?"
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({l - r}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)" if r > 1 else f"\\({r + 4}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Inverse Calculation**\n\\(\\text{{CSA}} = \\pi r l \\implies {csa_val}\\pi = \\pi \\times r \\times {l}\\).\n\\(r = \\frac{{{csa_val}}}{{{l}}} = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\n\\(r = {r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"The lateral surface area of a {obj_short} is \\({csa_val}\\pi\\text{{ cm}}^2\\) and its base radius is \\({r}\\text{{ cm}}\\). Calculate its slant height."
            corr = f"\\({l}\\text{{ cm}}\\)"
            dist = [f"\\({l + 3}\\text{{ cm}}\\)", f"\\({l - 2}\\text{{ cm}}\\)", f"\\({h}\\text{{ cm}}\\)", f"\\({l * 2}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(l = \\frac{{\\text{{CSA}}}}{{\\pi r}} = \\frac{{{csa_val}\\pi}}{{\\pi \\times {r}}} = {l}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nSlant height is \\({l}\\text{{ cm}}\\)."
        elif archetype == 4:
            rate = 5 + (idx % 12) * 2
            total_cost = csa_val * rate
            txt = prefix + COAT_ACTIONS[sub_idx].format(obj=obj_name, r=r, l=l, rate=rate)
            corr = f"₹{total_cost}"
            dist = [f"₹{total_cost + 50}", f"₹{total_cost - 40}", f"₹{total_cost * 2}", f"₹{total_cost + 100}"]
            sol = f"**Step 1: CSA**\n\\(\\text{{CSA}} = \\pi r l = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Cost Calculation**\n\\(\\text{{Cost}} = {csa_val} \\times {rate} = ₹{total_cost}\\).\n**Step 3: Conclusion**\nTotal cost is ₹{total_cost}."
        elif archetype == 5:
            txt = prefix + f"What is the curved surface area of a right circular {obj_short} having base diameter \\({2 * r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 10}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: CSA**\n\\(\\text{{CSA}} = \\pi r l = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 6:
            txt = prefix + f"If the base radius of a {obj_name} is \\({r}\\text{{ cm}}\\) and its vertical height is \\({h}\\text{{ cm}}\\), what is its curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({r * h}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 15}\\pi\\text{{ cm}}^2\\)", f"\\({2 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 12}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Slant Height**\n\\(l = \\sqrt{{{r}^2 + {h}^2}} = {l}\\text{{ cm}}\\).\n**Step 2: CSA**\n\\(\\text{{CSA}} = \\pi r l = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        else:
            material = ["metal sheet", "copper foil", "tin sheet", "plastic wrap", "fabric lining", "cardboard cover", "canvas cloth", "tarpaulin cover"][idx % 8]
            txt = prefix + f"A roll of {material} is shaped into an open {obj_name} of radius \\({r}\\text{{ cm}}\\) and slant height \\({l}\\text{{ cm}}\\). What surface area of material was consumed (ignoring base)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({(r + l)**2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 25}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val * 3}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 18}\\pi\\text{{ cm}}^2\\)" ]
            sol = f"**Step 1: Concept**\nOpen cone lateral area equals \\(\\pi r l\\).\n**Step 2: Calculation**\n\\(\\text{{Area}} = \\pi \\times {r} \\times {l} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_1():
    tc = "MH-9-MTH2-9-9.2.1"
    tname = "Surface Area of Sphere = 4πr²"
    qs = []
    EXPAND_TEMPLATES = [
        "If the radius of a {obj} ({r} cm) is enlarged by a factor of {mult}, how many times greater is the new surface area?",
        "A {obj} of radius {r} cm expands so its radius increases {mult}-fold. By what ratio does its outer surface area multiply?",
        "Suppose the radial measurement of a {obj} is scaled up {mult} times. Find the factor by which its external boundary area grows.",
        "When a {obj} of radius {r} cm is magnified by {mult}x, determine the factor of magnification for its total area.",
        "The radius of a spherical {obj} changes from {r} cm to {rm} cm. By what factor did its surface area expand?",
        "If a manufacturer multiplies the radius of a {obj} ({r} cm) by {mult}, what factor multiplies the surface area?",
        "By what numeric multiple does the area of a {obj} increase if its original radius of {r} cm is scaled by {mult}?",
        "An engineer scales the radius of a {obj} from {r} cm to {rm} cm. Determine the multiplier for the resulting total surface area.",
        "If the radius of a spherical {obj} is dilated by {mult}, calculate the exact factor of increase in its spherical surface area.",
        "A physical spherical {obj} with radius {r} cm is replaced by a larger version with {mult} times the radius. What is the area scaling factor?"
    ]
    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = SPHERE_OBJECTS_80[idx]
        sa_val = 4 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_sphere(f"r = {r} cm", f"{obj_name.title()} #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Calculate the total surface area of a {obj_name} having radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({sa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 16}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(A = 4\\pi r^2 = 4\\pi \\times {r}^2 = 4\\pi \\times {r*r} = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nSurface area is \\({sa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A solid spherical {obj_short} has diameter \\({2 * r}\\text{{ cm}}\\). What is its surface area in terms of \\(\\pi\\)?"
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * sa_val}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val // 4}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 30}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 25}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Surface Area**\n\\(A = 4\\pi r^2 = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({sa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The surface area of a {obj_name} is \\({sa_val}\\pi\\text{{ cm}}^2\\). Determine the radius of the sphere."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({r + 4}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius Formula**\n\\(r^2 = \\frac{{A}}{{4\\pi}} = \\frac{{{sa_val}\\pi}}{{4\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"The surface area of a spherical {obj_short} is \\({sa_val}\\pi\\text{{ cm}}^2\\). What is the diameter of this sphere?"
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val * 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{sa_val}}}{{4}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        elif archetype == 4:
            txt = prefix + f"If the radius of a {obj_name} is \\({r}\\text{{ m}}\\), calculate the total external area requiring protective coating in terms of \\(\\pi\\)."
            corr = f"\\({sa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({2 * sa_val}\\pi\\text{{ m}}^2\\)", f"\\({sa_val + 15}\\pi\\text{{ m}}^2\\)", f"\\({sa_val // 2}\\pi\\text{{ m}}^2\\)", f"\\({sa_val - 12}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(A = 4\\pi r^2 = 4\\pi \\times {r*r} = {sa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({sa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 5:
            mult = 2 + (sub_idx % 7)
            factor = mult * mult
            rm = r * mult
            txt = prefix + EXPAND_TEMPLATES[sub_idx].format(obj=obj_name, r=r, mult=mult, rm=rm)
            corr = f"{factor}"
            dist = [f"{mult}", f"{2 * mult}", f"{factor + 5}", f"{factor - 3}"]
            sol = f"**Step 1: Scaling Law**\nSurface area is proportional to \\(r^2\\). When radius is multiplied by {mult}, surface area increases by \\({mult}^2 = {factor}\\).\n**Step 2: Conclusion**\nFactor is {factor}."
        elif archetype == 6:
            cost_rate = 2 + (idx % 9) * 2
            total_cost = sa_val * cost_rate
            txt = prefix + f"Electroplating a spherical {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) costs ₹{cost_rate} per \\(\\pi\\text{{ cm}}^2\\). What is the total electroplating expense?"
            corr = f"₹{total_cost}"
            dist = [f"₹{total_cost + 40}", f"₹{total_cost - 30}", f"₹{total_cost * 2}", f"₹{total_cost + 80}"]
            sol = f"**Step 1: Surface Area**\n\\(A = 4\\pi r^2 = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Expense**\n\\(\\text{{Cost}} = {sa_val} \\times {cost_rate} = ₹{total_cost}\\).\n**Step 3: Conclusion**\n₹{total_cost}."
        else:
            great_circle_area = r * r
            txt = prefix + f"The area of the great circle of a spherical {obj_name} is \\({great_circle_area}\\pi\\text{{ cm}}^2\\). What is the total surface area of the entire sphere?"
            corr = f"\\({sa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * sa_val}\\pi\\text{{ cm}}^2\\)", f"\\({great_circle_area * 2}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val + 20}\\pi\\text{{ cm}}^2\\)", f"\\({sa_val - 15}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Great Circle Relation**\n\\(A_{{\\text{{great circle}}}} = \\pi r^2 = {great_circle_area}\\pi\\).\nTotal surface area \\(= 4\\pi r^2 = 4 \\times {great_circle_area}\\pi = {sa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({sa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_2():
    tc = "MH-9-MTH2-9-9.2.2"
    tname = "Volume of Sphere = 4/3 * πr³"
    qs = []
    RADII_MULT3_80 = [3 * (i + 1) for i in range(80)]
    TANK_TEMPLATES = [
        "A spherical water tank has radius {r} m. How many cubic meters of water can it store when completely full in terms of \\(\\pi\\)?",
        "Find the total storage capacity in cubic meters of a spherical reservoir of radius {r} m in terms of \\(\\pi\\).",
        "A hollow spherical cistern has a radius of {r} m. What volume of liquid fills it to the brim (in terms of \\(\\pi\\))?",
        "Calculate the maximum volume of water held by a spherical container of radius {r} m in terms of \\(\\pi\\).",
        "Determine the volume of water enclosed by a spherical shell of internal radius {r} m in terms of \\(\\pi\\).",
        "How many cubic meters of chemical solution can be loaded into a spherical tank of radius {r} m (in terms of \\(\\pi\\))?",
        "What is the internal volume of a spherical water storage unit with radius {r} m expressed in terms of \\(\\pi\\)?",
        "A spherical municipal water vessel has radius {r} m. Compute its total liquid capacity in terms of \\(\\pi\\).",
        "If a spherical gas tank has radius {r} m, determine its volumetric capacity in cubic meters in terms of \\(\\pi\\).",
        "Calculate the volumetric content of a spherical storage balloon of radius {r} m in terms of \\(\\pi\\)."
    ]
    MARBLE_TEMPLATES = [
        "A solid metal {obj} of radius {r} cm is melted down and recast into small marbles of radius {rs} cm. How many such marbles can be cast?",
        "An artisan melts a spherical {obj} (radius {r} cm) to fabricate small beads of radius {rs} cm. Find the number of beads produced.",
        "A foundry liquidates a spherical {obj} of radius {r} cm into tiny spherical pellets of radius {rs} cm. What count of pellets is obtained?",
        "How many spherical ball-bearings of radius {rs} cm can be molded by melting a solid {obj} of radius {r} cm?",
        "By melting a solid bronze {obj} measuring {r} cm in radius, how many small spheres of radius {rs} cm can be formed?",
        "Calculate the number of mini-spheres of radius {rs} cm formed by recasting a solid metallic {obj} of radius {r} cm.",
        "A metallic spherical {obj} of radius {r} cm is transformed into multiple identical spherical balls of radius {rs} cm. Find the total count.",
        "When a solid {obj} of radius {r} cm is completely melted, how many spherical pellets of radius {rs} cm can be cast without metal loss?",
        "Determine the quantity of small spherical beads of radius {rs} cm that can be produced from a melted {obj} of radius {r} cm.",
        "From a melted solid {obj} having radius {r} cm, a jeweler casts small pearls of radius {rs} cm. How many pearls are made?"
    ]

    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_MULT3_80[idx]
        obj_name, obj_short = SPHERE_OBJECTS_80[idx]
        vol_val = (4 * r**3) // 3
        has_fig = (idx % 5 != 0)
        svg = svg_sphere(f"r = {r} cm", f"{obj_name.title()} Vol #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Determine the exact volume of a solid {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 50}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 40}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}}\\pi ({r})^3 = \\frac{{4}}{{3}}\\pi \\times {r**3} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 1:
            txt = prefix + f"A spherical {obj_short} has base diameter \\({2 * r}\\text{{ cm}}\\). What volume of space does it occupy in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({8 * vol_val}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 4}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 70}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 60}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Volume**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 2:
            txt = prefix + f"A craftsman melts a metallic spherical {obj_name} of radius \\({r}\\text{{ cm}}\\). What is the volume of molten metal yielded in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({r**3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 100}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 80}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 3:
            txt = prefix + f"The volume of a spherical {obj_short} is \\({vol_val}\\pi\\text{{ cm}}^3\\). Calculate its radius in cm."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r // 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Formula**\n\\(r^3 = \\frac{{3V}}{{4\\pi}} = \\frac{{3 \\times {vol_val}\\pi}}{{4\\pi}} = {r**3} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 4:
            ratio_pairs = [
                ((1, 2), "1:8", "Two solid spheres have radii in the ratio 1:2. Find the ratio of their volumes."),
                ((2, 3), "8:27", "If the radii of two spherical bearings are in the ratio 2:3, what is the ratio of their volumes?"),
                ((3, 4), "27:64", "Calculate the ratio of volumes of two spherical globes with radii in the ratio 3:4."),
                ((1, 3), "1:27", "Two spherical balls have radii in the ratio 1:3. Determine the ratio of the volumes of space they displace."),
                ((3, 5), "27:125", "Find the ratio of volumes of two spherical celestial bodies whose radii are in the ratio 3:5."),
                ((2, 5), "8:125", "Two solid spheres have diameters in the ratio 2:5. What is the ratio of their volumes?"),
                ((1, 4), "1:64", "If the radius ratio of two spheres is 1:4, what is the corresponding volumetric ratio?"),
                ((4, 5), "64:125", "Compute the volume ratio of two spheres having radii in the proportion 4:5."),
                ((1, 5), "1:125", "Determine the volumetric ratio for two spheres with radii in the ratio 1:5."),
                ((2, 1), "8:1", "If sphere A has twice the radius of sphere B, what is the ratio of volume of sphere A to sphere B?")
            ]
            (r1, r2), ans_val, q_text = ratio_pairs[sub_idx]
            txt = prefix + q_text
            corr = f"\\({ans_val}\\)"
            dist = [f"\\({r1}:{r2}\\)", f"\\({r1*r1}:{r2*r2}\\)", f"\\({r1*3}:{r2*3}\\)"]
            sol = f"**Step 1: Volumetric Ratio**\n\\(\\frac{{V_1}}{{V_2}} = \\left(\\frac{{{r1}}}{{{r2}}}\\right)^3 = \\frac{{{r1**3}}}{{{r2**3}}} = {ans_val}\\).\n**Step 2: Conclusion**\n\\({ans_val}\\)."
        elif archetype == 5:
            r_small = 1 + (sub_idx % 3)
            n_spheres = (r // r_small)**3
            txt = prefix + MARBLE_TEMPLATES[sub_idx].format(obj=obj_name, r=r, rs=r_small)
            corr = f"{n_spheres}"
            dist = [f"{n_spheres * 2}", f"{n_spheres + 10}", f"{n_spheres // 2}", f"{n_spheres - 5}"]
            sol = f"**Step 1: Formula**\n\\(N = \\frac{{\\frac{{4}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{{r}^3}}{{{r_small}^3}} = \\frac{{{r**3}}}{{{r_small**3}}} = {n_spheres}\\).\n**Step 2: Conclusion**\n{n_spheres} marbles."
        elif archetype == 6:
            txt = prefix + TANK_TEMPLATES[sub_idx].format(r=r)
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 120}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 90}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Capacity**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
        else:
            txt = prefix + f"A spherical {obj_short} of radius \\(r = {r}\\text{{ cm}}\\) is immersed in a water vessel. What volume of water does it displace in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 4}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 85}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 75}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Archimedes Principle**\nDisplaced water volume equals the sphere's volume \\(\\frac{{4}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_3():
    tc = "MH-9-MTH2-9-9.2.3"
    tname = "Curved Surface Area of Hemisphere = 2πr²"
    qs = []
    TIN_ACTIONS = [
        "Tin-plating the inside of a {obj} of radius \\({r}\\text{{ cm}}\\) costs ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Calculate the total tin-plating bill.",
        "An artisan lines the interior cavity of a {obj} ({r} cm radius) with silver foil at ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Find the total expenditure.",
        "Glazing the inner curved face of a {obj} having radius \\({r}\\text{{ cm}}\\) is priced at ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Determine the total cost.",
        "Applying food-grade protective lacquer inside a {obj} of radius \\({r}\\text{{ cm}}\\) costs ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Compute the total fee.",
        "Electroplating the concave interior of a {obj} with \\(r = {r}\\text{{ cm}}\\) costs ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Find the total electroplating expense.",
        "At ₹{rate} per \\(\\pi\\text{{ cm}}^2\\), calculate the amount needed to polish the inside surface of a {obj} having \\(r = {r}\\text{{ cm}}\\).",
        "A silversmith charges ₹{rate} per \\(\\pi\\text{{ cm}}^2\\) to gild the inside bowl of a {obj} with \\(r = {r}\\text{{ cm}}\\). What is the total charge?",
        "Coating the internal hemisphere of a {obj} of radius \\({r}\\text{{ cm}}\\) with ceramic glaze costs ₹{rate} per \\(\\pi\\text{{ cm}}^2\\). Calculate the bill.",
        "How much does it cost to chrome-plate the inner concave surface of a {obj} ({r} cm radius) at ₹{rate} per \\(\\pi\\text{{ cm}}^2\\)?",
        "Determine the overall expense of painting the interior curved side of a {obj} of radius \\({r}\\text{{ cm}}\\) at ₹{rate} per \\(\\pi\\text{{ cm}}^2\\)."
    ]
    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        csa_val = 2 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} CSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Determine the curved surface area of a {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 14}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 12}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2\\pi \\times {r}^2 = 2\\pi \\times {r*r} = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nCurved surface area is \\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A {obj_short} has internal diameter \\({2 * r}\\text{{ cm}}\\). What is its internal curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 25}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val // 2}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 20}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Curved Area**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). Calculate its radius in cm."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 2}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r + 4}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Formula**\n\\(r^2 = \\frac{{\\text{{CSA}}}}{{2\\pi}} = \\frac{{{csa_val}\\pi}}{{2\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            txt = prefix + f"A painter paints the outer dome of a {obj_name} of radius \\(r = {r}\\text{{ m}}\\). What is the total area painted in terms of \\(\\pi\\)?"
            corr = f"\\({csa_val}\\pi\\text{{ m}}^2\\)"
            dist = [f"\\({2 * csa_val}\\pi\\text{{ m}}^2\\)", f"\\({csa_val + 16}\\pi\\text{{ m}}^2\\)", f"\\({csa_val - 14}\\pi\\text{{ m}}^2\\)", f"\\({csa_val * 3}\\pi\\text{{ m}}^2\\)"]
            sol = f"**Step 1: Outer Curved Surface**\n\\(\\text{{Area}} = 2\\pi r^2 = 2\\pi \\times {r}^2 = {csa_val}\\pi\\text{{ m}}^2\\).\n**Step 2: Conclusion**\n\\({csa_val}\\pi\\text{{ m}}^2\\)."
        elif archetype == 4:
            ratio_pairs = [
                ((1, 2), "1:4", "Two hemispherical bowls have base radii in the ratio 1:2. Find the ratio of their curved surface areas."),
                ((2, 3), "4:9", "If the radii of two hemispherical domes are in the ratio 2:3, what is the ratio of their lateral surface areas?"),
                ((3, 4), "9:16", "Calculate the ratio of curved surface areas of two hemispheres with radii in the ratio 3:4."),
                ((1, 3), "1:9", "Two hemispherical basins have radii in the ratio 1:3. Determine the ratio of their curved surface areas."),
                ((2, 5), "4:25", "If two hemispheres have diameters in the ratio 2:5, what is the ratio of their curved surface areas?"),
                ((3, 5), "9:25", "Find the ratio of curved surface areas of two hemispherical cavities whose radii are in the ratio 3:5."),
                ((1, 4), "1:16", "If the radius ratio of two hemispheres is 1:4, what is the ratio of their curved surface areas?"),
                ((4, 5), "16:25", "Compute the curved surface area ratio of two hemispheres having radii in the proportion 4:5."),
                ((1, 5), "1:25", "Determine the curved surface area ratio for two hemispheres with radii in the ratio 1:5."),
                ((3, 1), "9:1", "If hemisphere A has 3 times the radius of hemisphere B, what is the ratio of their curved surface areas?")
            ]
            (r1, r2), ans_val, q_text = ratio_pairs[sub_idx]
            txt = prefix + q_text
            corr = f"\\({ans_val}\\)"
            dist = [f"\\({r1}:{r2}\\)", f"\\({r1*2}:{r2*2}\\)", f"\\({r1**3}:{r2**3}\\)"]
            sol = f"**Step 1: Ratio Formula**\n\\(\\frac{{\\text{{CSA}}_1}}{{\\text{{CSA}}_2}} = \\frac{{2\\pi r_1^2}}{{2\\pi r_2^2}} = \\left(\\frac{{{r1}}}{{{r2}}}\\right)^2 = {ans_val}\\).\n**Step 2: Conclusion**\n\\({ans_val}\\)."
        elif archetype == 5:
            tin_rate = 3 + (idx % 10) * 2
            cost = csa_val * tin_rate
            txt = prefix + TIN_ACTIONS[sub_idx].format(obj=obj_name, r=r, rate=tin_rate)
            corr = f"₹{cost}"
            dist = [f"₹{cost + 35}", f"₹{cost - 25}", f"₹{cost * 2}", f"₹{cost + 70}"]
            sol = f"**Step 1: Inside Area**\n\\(\\text{{CSA}} = 2\\pi r^2 = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Bill**\n\\(\\text{{Cost}} = {csa_val} \\times {tin_rate} = ₹{cost}\\).\n**Step 3: Conclusion**\n₹{cost}."
        elif archetype == 6:
            txt = prefix + f"The curved surface area of a {obj_name} is \\({csa_val}\\pi\\text{{ cm}}^2\\). What is the diameter of its circular rim?"
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)", f"\\({2 * d_val}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{csa_val}}}{{2}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        else:
            base_area = r * r
            txt = prefix + f"The base circular opening of a {obj_short} has an area of \\({base_area}\\pi\\text{{ cm}}^2\\). What is its curved surface area?"
            corr = f"\\({csa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({3 * base_area}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val + 10}\\pi\\text{{ cm}}^2\\)", f"\\({csa_val - 8}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Relation**\n\\(\\text{{CSA}} = 2 \\times \\text{{Base Area}} = 2 \\times {base_area}\\pi = {csa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({csa_val}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_4():
    tc = "MH-9-MTH2-9-9.2.4"
    tname = "Total Surface Area of Hemisphere = 3πr²"
    qs = []
    RATIO_TEMPLATES_924 = [
        ("For any solid hemisphere of radius {r} cm, what is the ratio of its curved surface area to flat circular base area?", "2:1", "\\(\\frac{2\\pi r^2}{\\pi r^2} = 2:1\\)"),
        ("In a solid hemisphere of radius {r} cm, calculate the ratio of its total surface area to its flat circular base area.", "3:1", "\\(\\frac{3\\pi r^2}{\\pi r^2} = 3:1\\)"),
        ("What is the ratio between the circular base area and the curved surface area of a solid hemisphere of radius {r} cm?", "1:2", "\\(\\frac{\\pi r^2}{2\\pi r^2} = 1:2\\)"),
        ("Determine the ratio of base area to total surface area for a solid hemisphere of radius {r} cm.", "1:3", "\\(\\frac{\\pi r^2}{3\\pi r^2} = 1:3\\)"),
        ("Find the ratio of curved surface area to total surface area for a solid hemisphere of radius {r} cm.", "2:3", "\\(\\frac{2\\pi r^2}{3\\pi r^2} = 2:3\\)"),
        ("What is the ratio of total surface area to curved surface area for a solid hemisphere of radius {r} cm?", "3:2", "\\(\\frac{3\\pi r^2}{2\\pi r^2} = 3:2\\)"),
        ("For a solid hemispherical bowl of radius {r} cm, what proportion does the curved surface represent of the total surface area?", "2:3", "\\(\\frac{2\\pi r^2}{3\\pi r^2} = 2:3\\)"),
        ("In a hemisphere of radius {r} cm, compare the total surface area to the circular floor area as a simplified ratio.", "3:1", "\\(\\frac{3\\pi r^2}{\\pi r^2} = 3:1\\)"),
        ("Determine the simplified fraction comparing flat base area to total area for a solid hemisphere of radius {r} cm.", "1:3", "\\(\\frac{\\pi r^2}{3\\pi r^2} = 1:3\\)"),
        ("What is the exact ratio of the dome surface area to the circular base area in a solid hemisphere of radius {r} cm?", "2:1", "\\(\\frac{2\\pi r^2}{\\pi r^2} = 2:1\\)")
    ]
    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        tsa_val = 3 * r * r
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} TSA #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Calculate the total surface area of a solid {obj_name} having radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * r * r}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 24}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 18}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Formula**\n\\(\\text{{TSA}} = 3\\pi r^2 = 3\\pi \\times {r}^2 = 3\\pi \\times {r*r} = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\nTotal surface area is \\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 1:
            txt = prefix + f"A solid metal {obj_short} has base diameter \\({2 * r}\\text{{ cm}}\\). What is its total surface area including its circular base in terms of \\(\\pi\\)?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({4 * tsa_val}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 30}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val // 3}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val - 25}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Total Surface Area**\n\\(\\text{{TSA}} = 3\\pi r^2 = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 3: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 2:
            txt = prefix + f"The total surface area of a solid {obj_name} is \\({tsa_val}\\pi\\text{{ cm}}^2\\). Determine the radius of this hemisphere."
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 1}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r + 5}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius Formula**\n\\(r^2 = \\frac{{\\text{{TSA}}}}{{3\\pi}} = \\frac{{{tsa_val}\\pi}}{{3\\pi}} = {r*r} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 3:
            base_area = r * r
            csa_val = 2 * r * r
            txt = prefix + f"A solid {obj_short} has curved surface area \\({csa_val}\\pi\\text{{ cm}}^2\\) and flat base area \\({base_area}\\pi\\text{{ cm}}^2\\). What is its total surface area?"
            corr = f"\\({tsa_val}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({csa_val}\\pi\\text{{ cm}}^2\\)", f"\\({base_area}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val + 15}\\pi\\text{{ cm}}^2\\)", f"\\({tsa_val * 2}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Addition**\n\\(\\text{{TSA}} = \\text{{CSA}} + \\text{{Base Area}} = {csa_val}\\pi + {base_area}\\pi = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({tsa_val}\\pi\\text{{ cm}}^2\\)."
        elif archetype == 4:
            ratio_pairs = [
                ((1, 2), "1:4", "Two solid hemispheres have radii in the ratio 1:2. Find the ratio of their total surface areas."),
                ((2, 3), "4:9", "If the radii of two solid hemispheres are in the ratio 2:3, what is the ratio of their total surface areas?"),
                ((3, 4), "9:16", "Calculate the ratio of total surface areas of two solid hemispheres with radii in the ratio 3:4."),
                ((1, 3), "1:9", "Two solid hemispheres have radii in the ratio 1:3. Determine the ratio of their total surface areas."),
                ((2, 5), "4:25", "If two solid hemispheres have diameters in the ratio 2:5, what is the ratio of their total surface areas?"),
                ((3, 5), "9:25", "Find the ratio of total surface areas of two solid hemispherical pieces whose radii are in the ratio 3:5."),
                ((1, 4), "1:16", "If the radius ratio of two solid hemispheres is 1:4, what is the ratio of their total surface areas?"),
                ((4, 5), "16:25", "Compute the total surface area ratio of two solid hemispheres having radii in the proportion 4:5."),
                ((1, 5), "1:25", "Determine the total surface area ratio for two solid hemispheres with radii in the ratio 1:5."),
                ((3, 1), "9:1", "If solid hemisphere A has 3 times the radius of solid hemisphere B, what is the ratio of their total surface areas?")
            ]
            (r1, r2), ans_val, q_text = ratio_pairs[sub_idx]
            txt = prefix + q_text
            corr = f"\\({ans_val}\\)"
            dist = [f"\\({r1}:{r2}\\)", f"\\({r1*2}:{r2*2}\\)", f"\\({r1**3}:{r2**3}\\)"]
            sol = f"**Step 1: Ratio Formula**\n\\(\\frac{{\\text{{TSA}}_1}}{{\\text{{TSA}}_2}} = \\frac{{3\\pi r_1^2}}{{3\\pi r_2^2}} = \\left(\\frac{{{r1}}}{{{r2}}}\\right)^2 = {ans_val}\\).\n**Step 2: Conclusion**\n\\({ans_val}\\)."
        elif archetype == 5:
            cost_rate = 4 + (idx % 8) * 3
            cost = tsa_val * cost_rate
            txt = prefix + f"Polishing the entire surface (curved + flat base) of a solid {obj_name} of radius \\({r}\\text{{ cm}}\\) costs ₹{cost_rate} per \\(\\pi\\text{{ cm}}^2\\). Find the total polishing charge."
            corr = f"₹{cost}"
            dist = [f"₹{cost + 50}", f"₹{cost - 35}", f"₹{cost * 2}", f"₹{cost + 90}"]
            sol = f"**Step 1: TSA**\n\\(\\text{{TSA}} = 3\\pi r^2 = {tsa_val}\\pi\\text{{ cm}}^2\\).\n**Step 2: Charge**\n\\(\\text{{Cost}} = {tsa_val} \\times {cost_rate} = ₹{cost}\\).\n**Step 3: Conclusion**\n₹{cost}."
        elif archetype == 6:
            txt = prefix + f"If the total surface area of a solid {obj_short} is \\({tsa_val}\\pi\\text{{ cm}}^2\\), calculate the diameter of its circular base."
            d_val = 2 * r
            corr = f"\\({d_val}\\text{{ cm}}\\)"
            dist = [f"\\({r}\\text{{ cm}}\\)", f"\\({d_val + 2}\\text{{ cm}}\\)", f"\\({d_val - 2}\\text{{ cm}}\\)", f"\\({2 * d_val}\\text{{ cm}}\\)" ]
            sol = f"**Step 1: Radius**\n\\(r = \\sqrt{{\\frac{{{tsa_val}}}{{3}}}} = {r}\\text{{ cm}}\\).\n**Step 2: Diameter**\n\\(d = 2r = {d_val}\\text{{ cm}}\\).\n**Step 3: Conclusion**\n\\({d_val}\\text{{ cm}}\\)."
        else:
            diff_area = tsa_val - (2 * r * r)
            txt = prefix + f"By how much does the total surface area of a solid {obj_short} of radius \\({r}\\text{{ cm}}\\) exceed its curved surface area in terms of \\(\\pi\\)?"
            corr = f"\\({diff_area}\\pi\\text{{ cm}}^2\\)"
            dist = [f"\\({2 * diff_area}\\pi\\text{{ cm}}^2\\)", f"\\({diff_area + 6}\\pi\\text{{ cm}}^2\\)", f"\\({r}\\pi\\text{{ cm}}^2\\)", f"\\({diff_area - 4}\\pi\\text{{ cm}}^2\\)" if diff_area > 4 else f"\\({diff_area + 12}\\pi\\text{{ cm}}^2\\)"]
            sol = f"**Step 1: Concept**\n\\(\\text{{TSA}} - \\text{{CSA}} = 3\\pi r^2 - 2\\pi r^2 = \\pi r^2 = {diff_area}\\pi\\text{{ cm}}^2\\).\n**Step 2: Conclusion**\n\\({diff_area}\\pi\\text{{ cm}}^2\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def generate_9_2_5():
    tc = "MH-9-MTH2-9-9.2.5"
    tname = "Volume of Hemisphere = 2/3 * πr³"
    qs = []
    RADII_MULT3_80 = [3 * (i + 1) for i in range(80)]
    TRANSFER_TEMPLATES = [
        "A hemispherical container of radius {r} cm is full of liquid. If completely transferred to a cylindrical vessel, what volume was transferred in terms of \\(\\pi\\)?",
        "Liquid fills a hemispherical bowl of radius {r} cm to the brim. What volume of liquid is poured into another beaker (in terms of \\(\\pi\\))?",
        "A chemist empties a hemispherical retort of radius {r} cm completely into a flask. Find the volume of reagent emptied in terms of \\(\\pi\\).",
        "Soup filling a hemispherical tureen of radius {r} cm is served into a pot. What total volume of soup was moved in terms of \\(\\pi\\)?",
        "A hemispherical reservoir of radius {r} cm discharges all its contents into a drainage tube. Calculate the volume discharged in terms of \\(\\pi\\).",
        "Water stored in a hemispherical basin of radius {r} cm is completely siphoned off. How much water volume was evacuated in terms of \\(\\pi\\)?",
        "Molten wax filling a hemispherical mold of radius {r} cm is transferred into a box. What volume of wax was poured in terms of \\(\\pi\\)?",
        "Determine the volume of oil drained when a hemispherical container with radius {r} cm is entirely evacuated in terms of \\(\\pi\\).",
        "A hemispherical vat containing milk of radius {r} cm is emptied into distribution cans. Compute the milk volume in terms of \\(\\pi\\).",
        "Calculate the amount of fluid transferred when a full hemispherical bowl of radius {r} cm is tipped into an aquarium in terms of \\(\\pi\\)."
    ]
    CAST_TEMPLATES = [
        "A solid metal {obj} of radius {r} cm is melted down to cast small spheres of radius {rs} cm. How many such spheres can be made?",
        "An artisan melts a solid {obj} ({r} cm radius) to mold small spherical beads of radius {rs} cm. Find the total count produced.",
        "From a melted hemispherical {obj} of radius {r} cm, how many tiny ball-bearings of radius {rs} cm can be manufactured?",
        "Calculate the number of mini-spheres of radius {rs} cm obtained by melting down a {obj} with radius {r} cm.",
        "A metalworker casts small balls of radius {rs} cm by melting a solid {obj} measuring {r} cm in radius. How many balls result?",
        "When a bronze {obj} of radius {r} cm is completely liquefied, how many spherical pellets of radius {rs} cm can be cast?",
        "Determine the count of small marbles of radius {rs} cm cast from a melted solid {obj} having radius {r} cm.",
        "How many spherical pellets of radius {rs} cm can a foundry mold from a molten {obj} of radius {r} cm?",
        "A solid {obj} with radius {r} cm is melted and formed into multiple spheres of radius {rs} cm. Find the quantity made.",
        "Find how many spherical shots of radius {rs} cm can be fabricated by melting a solid {obj} of radius {r} cm."
    ]

    DOME_TEMPLATES = [
        "A hemispherical palace observatory dome has an inner radius of \\({r}\\text{{ m}}\\). Calculate the internal volume of air enclosed in terms of \\(\\pi\\).",
        "An architectural planetarium projection dome has a radius of \\({r}\\text{{ m}}\\). Determine the interior hall capacity in terms of \\(\\pi\\).",
        "A military bunker features a hemispherical protective dome with radius \\({r}\\text{{ m}}\\). What is the subterranean air enclosure volume in terms of \\(\\pi\\)?",
        "A botanical greenhouse glass dome has radius \\({r}\\text{{ m}}\\). Find the volume of air inside the dome in terms of \\(\\pi\\).",
        "A sports arena geodesic fabric dome of radius \\({r}\\text{{ m}}\\) covers a pavilion. How many cubic meters of air does it enclose in terms of \\(\\pi\\)?",
        "An acoustic auditorium ceiling dome is shaped as a hemisphere with radius \\({r}\\text{{ m}}\\). Compute its internal air space in terms of \\(\\pi\\).",
        "A storage silo hemispherical dome roof has radius \\({r}\\text{{ m}}\\). How much headspace volume is contained beneath the roof in terms of \\(\\pi\\)?",
        "A radar installation tracking dome is a hemisphere of radius \\({r}\\text{{ m}}\\). Find the volume of sheltered space within the dome in terms of \\(\\pi\\).",
        "An exhibition pavilion igloo structure has an internal radius of \\({r}\\text{{ m}}\\). What volume of air does it contain in terms of \\(\\pi\\)?",
        "A polar research station geodesic shelter is hemispherical with radius \\({r}\\text{{ m}}\\). Calculate the interior air volume in terms of \\(\\pi\\)."
    ]

    for idx, seq in enumerate(SEQS_80):
        r = RADII_MULT3_80[idx]
        obj_name, obj_short = HEMI_OBJECTS_80[idx]
        vol_val = (2 * r**3) // 3
        has_fig = (idx % 5 != 0)
        svg = svg_hemi(f"r = {r} cm", f"{obj_name.title()} Vol #{seq}") if has_fig else ""
        prefix = f"{svg}\n" if svg else ""

        archetype = idx % 8
        sub_idx = (idx // 8) % 10
        if archetype == 0:
            txt = prefix + f"Determine the volume of a solid {obj_name} of radius \\(r = {r}\\text{{ cm}}\\) in terms of \\(\\pi\\)."
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 36}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 28}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Formula**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}}\\pi ({r})^3 = \\frac{{2}}{{3}}\\pi \\times {r**3} = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 1:
            txt = prefix + f"A {obj_name} has base diameter \\({2 * r}\\text{{ cm}}\\). What is its maximum liquid capacity in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({8 * vol_val}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 45}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val * 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 35}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Radius**\n\\(r = \\frac{{{2 * r}}}{{2}} = {r}\\text{{ cm}}\\).\n**Step 2: Capacity**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 3: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 2:
            txt = prefix + TRANSFER_TEMPLATES[sub_idx].format(r=r)
            corr = f"\\({vol_val}\\pi\\text{{ cm}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val + 60}\\pi\\text{{ cm}}^3\\)", f"\\({vol_val - 50}\\pi\\text{{ cm}}^3\\)"]
            sol = f"**Step 1: Transferred Volume**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ cm}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ cm}}^3\\)."
        elif archetype == 3:
            txt = prefix + f"The volume of a {obj_short} is \\({vol_val}\\pi\\text{{ cm}}^3\\). What is the radius of the hemisphere in cm?"
            corr = f"\\({r}\\text{{ cm}}\\)"
            dist = [f"\\({r + 3}\\text{{ cm}}\\)", f"\\({r - 2}\\text{{ cm}}\\)", f"\\({2 * r}\\text{{ cm}}\\)", f"\\({r // 3}\\text{{ cm}}\\)"]
            sol = f"**Step 1: Radius Calculation**\n\\(r^3 = \\frac{{3V}}{{2\\pi}} = \\frac{{3 \\times {vol_val}\\pi}}{{2\\pi}} = {r**3} \\implies r = {r}\\text{{ cm}}\\).\n**Step 2: Conclusion**\nRadius is \\({r}\\text{{ cm}}\\)."
        elif archetype == 4:
            ratio_pairs = [
                ((1, 2), "1:8", "Two hemispherical bowls have base radii in the ratio 1:2. Find the ratio of their capacities."),
                ((2, 3), "8:27", "If the radii of two hemispherical containers are in the ratio 2:3, what is the ratio of their volumes?"),
                ((3, 4), "27:64", "Calculate the ratio of volumes of two hemispherical domes with radii in the ratio 3:4."),
                ((1, 3), "1:27", "Two hemispherical basins have radii in the ratio 1:3. Determine the ratio of the volume of liquid they hold."),
                ((2, 5), "8:125", "If two hemispherical tanks have diameters in the ratio 2:5, what is the ratio of their volumes?"),
                ((3, 5), "27:125", "Find the ratio of volumes of two hemispherical cavities whose radii are in the ratio 3:5."),
                ((1, 4), "1:64", "If the radius ratio of two hemispheres is 1:4, what is the ratio of their volumes?"),
                ((4, 5), "64:125", "Compute the volume ratio of two hemispheres having radii in the proportion 4:5."),
                ((1, 5), "1:125", "Determine the volume ratio for two hemispheres with radii in the ratio 1:5."),
                ((2, 1), "8:1", "If hemispherical bowl A has twice the radius of bowl B, what is the ratio of their volumes?")
            ]
            (r1, r2), ans_val, q_text = ratio_pairs[sub_idx]
            txt = prefix + q_text
            corr = f"\\({ans_val}\\)"
            dist = [f"\\({r1}:{r2}\\)", f"\\({r1*r1}:{r2*r2}\\)", f"\\({r1*3}:{r2*3}\\)"]
            sol = f"**Step 1: Volumetric Ratio**\n\\(\\frac{{V_1}}{{V_2}} = \\left(\\frac{{{r1}}}{{{r2}}}\\right)^3 = \\frac{{{r1**3}}}{{{r2**3}}} = {ans_val}\\).\n**Step 2: Conclusion**\n\\({ans_val}\\)."
        elif archetype == 5:
            txt = prefix + DOME_TEMPLATES[sub_idx].format(r=r)
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 80}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 60}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Air Enclosed**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."
        elif archetype == 6:
            r_small = 1 + (sub_idx % 3)
            n_spheres = (r**3) // (2 * (r_small**3))
            txt = prefix + CAST_TEMPLATES[sub_idx].format(obj=obj_name, r=r, rs=r_small)
            corr = f"{n_spheres}"
            dist = [f"{n_spheres * 2}", f"{n_spheres + 5}", f"{n_spheres // 2}", f"{n_spheres - 3}"]
            sol = f"**Step 1: Number of Spheres**\n\\(N = \\frac{{\\frac{{2}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\frac{{R^3}}{{2r^3}} = \\frac{{{r}^3}}{{2 \\times {r_small**3}}} = {n_spheres}\\).\n**Step 2: Conclusion**\n{n_spheres} spheres."
        else:
            txt = prefix + f"A {obj_short} water basin has radius \\({r}\\text{{ m}}\\) and is filled to capacity. How much water does it contain in terms of \\(\\pi\\)?"
            corr = f"\\({vol_val}\\pi\\text{{ m}}^3\\)"
            dist = [f"\\({vol_val * 3}\\pi\\text{{ m}}^3\\)", f"\\({vol_val + 55}\\pi\\text{{ m}}^3\\)", f"\\({vol_val // 2}\\pi\\text{{ m}}^3\\)", f"\\({vol_val - 45}\\pi\\text{{ m}}^3\\)"]
            sol = f"**Step 1: Volume**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = {vol_val}\\pi\\text{{ m}}^3\\).\n**Step 2: Conclusion**\n\\({vol_val}\\pi\\text{{ m}}^3\\)."

        diff = "easy" if seq >= 301 else ("medium" if seq >= 201 or idx % 2 == 0 else "hard")
        qs.append(build_q(f"{tc}-OSC-{seq}", txt, corr, dist, sol, tc, tname, seq, has_fig, diff))
    return qs

def main():
    all_qs = []
    all_qs.extend(generate_9_1_1())
    all_qs.extend(generate_9_1_2())
    all_qs.extend(generate_9_1_3())
    all_qs.extend(generate_9_1_4())
    all_qs.extend(generate_9_2_1())
    all_qs.extend(generate_9_2_2())
    all_qs.extend(generate_9_2_3())
    all_qs.extend(generate_9_2_4())
    all_qs.extend(generate_9_2_5())

    print(f"Generated {len(all_qs)} total questions across 9 subtopics.")
    with open("scripts/mh9_mth2_ch9_perfect.json", "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/mh9_mth2_ch9_perfect.json")

if __name__ == "__main__":
    main()
