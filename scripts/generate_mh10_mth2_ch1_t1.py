# -*- coding: utf-8 -*-
"""
Canonical 3-Pool Question Bank Generator for MH Board Class 10 Mathematics Part 2 (Geometry)
Chapter 1: Similarity
Topic 1.1: Ratio of Areas of Two Triangles (Base & Height Properties) (MH-10-MTH2-1-1.1)

Delivers exactly 82 canonical questions:
  - 40 Exam questions (001 - 040)
  - 30 Practice questions (041 - 070)
  - 12 Mock/Foundation questions (071 - 082)
Includes rich inline geometric SVG diagrams for geometry problems.
"""

import json
import os
import sys

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mh10_mth2_svg_helpers import (
    wrap_svg,
    svg_two_triangles,
    svg_collinear_base,
    svg_practice_set_1_1_q2,
    svg_practice_set_1_1_q3,
    svg_parallel_lines_triangles,
    svg_practice_set_1_1_q5,
    svg_median_triangle,
    svg_trapezium_diagonals,
    svg_collinear_three_segments,
    svg_quadrilateral_common_diagonal
)

TOPIC_CODE = "MH-10-MTH2-1-1.1"

def make_q(qcode, topic, text, options, answer_val, qtype, difficulty, vault, category, explanation, assertion=None, reason=None, diagram=None):
    q = {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_val,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation,
        "solution": explanation
    }
    if assertion:
        q["assertion"] = assertion
    if reason:
        q["reason"] = reason
    if diagram:
        q["diagram"] = diagram
    return q

# =========================================================================
# EXAM POOL (40 Questions: 001 - 040)
# =========================================================================
exam_data = []

# Q1 (OSC) - Textbook Practice Set 1.1 Q1 with SVG
q1_svg = svg_two_triangles(('A','B','C','D'), 'b₁ = 9', 'h₁ = 5', ('P','Q','R','S'), 'b₂ = 10', 'h₂ = 6', title="Practice Set 1.1 - Q1")
q1_text = (
    f"{q1_svg}\n"
    r"In the figure above, base of $\triangle ABC$ is $9$ and height is $5$. Base of another triangle $\triangle PQR$ is $10$ and height is $6$. "
    r"Find the ratio of areas of these two triangles, $\frac{A(\triangle ABC)}{A(\triangle PQR)}$."
)
q1_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **State the Property:** The ratio of areas of two triangles is equal to the ratio of the products of their bases and corresponding heights:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle PQR)} = \frac{b_1 \times h_1}{b_2 \times h_2} \]" "\n"
    r"2. **Substitute Given Values:**" "\n"
    r"Here, $b_1 = 9$, $h_1 = 5$, $b_2 = 10$, $h_2 = 6$." "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle PQR)} = \frac{9 \times 5}{10 \times 6} = \frac{45}{60} \]" "\n"
    r"3. **Simplify the Fraction:**" "\n"
    r"Dividing numerator and denominator by $15$:" "\n"
    r"\[ \frac{45 \div 15}{60 \div 15} = \frac{3}{4} \]" "\n"
    r"Thus, the ratio of areas of the two triangles is $3 : 4$."
)
exam_data.append((q1_text, [r"\(3 : 4\)", r"\(2 : 3\)", r"\(4 : 5\)", r"\(9 : 10\)"], "A", "OSC", "easy", q1_exp))

# Q2 (OSC) - Practice Set 1.1 Q2 with SVG
q2_svg = svg_practice_set_1_1_q2(bc_val='4', ad_val='8', title="Practice Set 1.1 - Q2")
q2_text = (
    f"{q2_svg}\n"
    r"In the given figure, $BC \perp AB$, $AD \perp AB$, $BC = 4$, and $AD = 8$. "
    r"Find the ratio $\frac{A(\triangle ABC)}{A(\triangle ADB)}$."
)
q2_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Identify the Common Element:** Both $\triangle ABC$ and $\triangle ADB$ have the common base segment $AB$." "\n"
    r"2. **Apply the Property of Triangles with Equal Bases:** The ratio of the areas of two triangles having equal bases is equal to the ratio of their corresponding heights:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD} \]" "\n"
    r"3. **Substitute the Given Values:**" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{4}{8} = \frac{1}{2} \]" "\n"
    r"Hence, $\frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{1}{2}$."
)
exam_data.append((q2_text, [r"\(\frac{1}{2}\)", r"\(\frac{1}{4}\)", r"\(2\)", r"\(\frac{3}{4}\)"], "A", "OSC", "easy", q2_exp))

# Q3 (OSC) - Practice Set 1.1 Q3 with SVG
q3_svg = svg_practice_set_1_1_q3(rq_val='6', ps_val='6', pr_val='12', qt_label='QT = ?', title="Practice Set 1.1 - Q3")
q3_text = (
    f"{q3_svg}\n"
    r"In the adjoining figure, segment $PS \perp \text{ray } RQ$, and segment $QT \perp \text{segment } PR$. "
    r"If $RQ = 6$, $PS = 6$, and $PR = 12$, then find the length of segment $QT$."
)
q3_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Express Area with Base $RQ$ and Altitude $PS$:**" "\n"
    r"In obtuse-angled $\triangle PQR$, considering base as $RQ$, the corresponding altitude is $PS$:" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times RQ \times PS \]" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times 6 \times 6 = 18 \]" "\n"
    r"2. **Express Area with Base $PR$ and Altitude $QT$:**" "\n"
    r"Considering base as $PR$, the corresponding altitude is $QT$:" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times PR \times QT \]" "\n"
    r"\[ 18 = \frac{1}{2} \times 12 \times QT \]" "\n"
    r"\[ 18 = 6 \times QT \]" "\n"
    r"3. **Solve for $QT$:**" "\n"
    r"\[ QT = \frac{18}{6} = 3 \]" "\n"
    r"Therefore, the length of segment $QT$ is $3$ units."
)
exam_data.append((q3_text, [r"\(3\)", r"\(4\)", r"\(6\)", r"\(2.5\)"], "A", "OSC", "medium", q3_exp))

# Q4 (OSC) - Practice Set 1.1 Q4 with SVG
q4_svg = svg_parallel_lines_triangles(top_l='A', top_r='D', bot_l='B', bot_r='C', title="Practice Set 1.1 - Q4")
q4_text = (
    f"{q4_svg}\n"
    r"In the figure, segment $AP \perp \text{seg } BC$, and segment $AD \parallel \text{segment } BC$. "
    r"Find the ratio $A(\triangle ABC) : A(\triangle BCD)$."
)
q4_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Analyze Bases:** Both $\triangle ABC$ and $\triangle BCD$ share the common base segment $BC$." "\n"
    r"2. **Analyze Heights:** Since segment $AD \parallel \text{seg } BC$, both triangles lie between the same two parallel lines. The perpendicular distance between two parallel lines is constant everywhere, so their heights are equal ($h_1 = h_2$)." "\n"
    r"3. **Apply the Property:** Triangles having equal bases and equal heights have equal areas:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle BCD)} = \frac{BC \times h}{BC \times h} = 1 \]" "\n"
    r"Thus, $A(\triangle ABC) : A(\triangle BCD) = 1 : 1$."
)
exam_data.append((q4_text, [r"\(1 : 1\)", r"\(1 : 2\)", r"\(2 : 1\)", r"\(1 : 4\)"], "A", "OSC", "easy", q4_exp))

# Q5 (OSC) - Practice Set 1.1 Q5 part (i) with SVG
q5_svg = svg_practice_set_1_1_q5()
q5_text = (
    f"{q5_svg}\n"
    r"In the adjoining figure, $PQ \perp BC$ and $AD \perp BC$. "
    r"Find the ratio of $\frac{A(\triangle PQB)}{A(\triangle PBC)}$."
)
q5_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Examine the Two Triangles:** In $\triangle PQB$ and $\triangle PBC$, both triangles have the common height $PQ$ (as $PQ \perp BC$, and points $B, Q, C$ are collinear)." "\n"
    r"2. **Apply the Property of Triangles with Equal Heights:** Areas of triangles having equal heights are proportional to their corresponding bases:" "\n"
    r"\[ \frac{A(\triangle PQB)}{A(\triangle PBC)} = \frac{\text{base of } \triangle PQB}{\text{base of } \triangle PBC} = \frac{BQ}{BC} \]" "\n"
    r"Hence, $\frac{A(\triangle PQB)}{A(\triangle PBC)} = \frac{BQ}{BC}$."
)
exam_data.append((q5_text, [r"\(\frac{BQ}{BC}\)", r"\(\frac{PQ}{AD}\)", r"\(\frac{BQ}{CD}\)", r"\(\frac{BC}{CD}\)"], "A", "OSC", "easy", q5_exp))

# Q6 (OSC) - Practice Set 1.1 Q5 part (ii) with SVG
q6_text = (
    f"{q5_svg}\n"
    r"In the adjoining figure, $PQ \perp BC$ and $AD \perp BC$. "
    r"Find the ratio of $\frac{A(\triangle PBC)}{A(\triangle ABC)}$."
)
q6_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Identify the Common Base:** $\triangle PBC$ and $\triangle ABC$ share the common base $BC$." "\n"
    r"2. **Apply the Property of Triangles with Equal Bases:** Areas of triangles having equal bases are proportional to their corresponding heights:" "\n"
    r"The height of $\triangle PBC$ corresponding to base $BC$ is $PQ$." "\n"
    r"The height of $\triangle ABC$ corresponding to base $BC$ is $AD$." "\n"
    r"\[ \frac{A(\triangle PBC)}{A(\triangle ABC)} = \frac{PQ}{AD} \]" "\n"
    r"Hence, the ratio is $\frac{PQ}{AD}$."
)
exam_data.append((q6_text, [r"\(\frac{PQ}{AD}\)", r"\(\frac{BQ}{BC}\)", r"\(\frac{AD}{PQ}\)", r"\(\frac{CD}{BC}\)"], "A", "OSC", "easy", q6_exp))

# Q7 (OSC) - Practice Set 1.1 Q5 part (iii) with SVG
q7_text = (
    f"{q5_svg}\n"
    r"In the adjoining figure, $PQ \perp BC$ and $AD \perp BC$. "
    r"Find the ratio of $\frac{A(\triangle ABC)}{A(\triangle ADC)}$."
)
q7_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Identify the Common Height:** $\triangle ABC$ and $\triangle ADC$ share the common vertex $A$ and have their bases $BC$ and $DC$ along the same line $BC$. Their common perpendicular altitude is $AD$." "\n"
    r"2. **Apply Property:** Areas of triangles having equal heights are proportional to their bases:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{BC}{DC} \]" "\n"
    r"Hence, the ratio is $\frac{BC}{DC}$ (or $\frac{BC}{CD}$)."
)
exam_data.append((q7_text, [r"\(\frac{BC}{CD}\)", r"\(\frac{PQ}{AD}\)", r"\(\frac{CD}{BC}\)", r"\(\frac{AD}{CD}\)"], "A", "OSC", "medium", q7_exp))

# Q8 (OSC) - Practice Set 1.1 Q5 part (iv) with SVG
q8_text = (
    f"{q5_svg}\n"
    r"In the adjoining figure, $PQ \perp BC$ and $AD \perp BC$. "
    r"Find the ratio of $\frac{A(\triangle ADC)}{A(\triangle PQC)}$."
)
q8_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Check Bases and Heights:** In $\triangle ADC$, base is $DC$ and height is $AD$. In $\triangle PQC$, base is $QC$ and height is $PQ$." "\n"
    r"Neither the bases nor the heights are equal." "\n"
    r"2. **Apply General Ratio Formula:**" "\n"
    r"\[ \frac{A(\triangle ADC)}{A(\triangle PQC)} = \frac{\text{base}_1 \times \text{height}_1}{\text{base}_2 \times \text{height}_2} = \frac{DC \times AD}{QC \times PQ} \]" "\n"
    r"Thus, the ratio is $\frac{DC \times AD}{QC \times PQ}$."
)
exam_data.append((q8_text, [r"\(\frac{DC \times AD}{QC \times PQ}\)", r"\(\frac{DC}{QC}\)", r"\(\frac{AD}{PQ}\)", r"\(\frac{AD \times QC}{DC \times PQ}\)"], "A", "OSC", "medium", q8_exp))

# Q9 (OSC) - Collinear Base Cevian with SVG
q9_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='4', len_dc='6', show_alt=True, title="Collinear Bases with Common Vertex")
q9_text = (
    f"{q9_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD = 4\text{ cm}$ and $DC = 6\text{ cm}$. "
    r"Find the ratio $\frac{A(\triangle ABD)}{A(\triangle ADC)}$."
)
q9_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Observe the Geometric Structure:** $\triangle ABD$ and $\triangle ADC$ have a common vertex $A$, and their bases $BD$ and $DC$ lie on the same straight line $BC$." "\n"
    r"2. **Recognize Equal Heights:** Since both triangles have the same vertex $A$ and collinear bases, the perpendicular altitude $AH$ drawn from $A$ to $BC$ is common to both triangles." "\n"
    r"3. **Apply Property:** The ratio of the areas of two triangles with equal heights is equal to the ratio of their corresponding bases:" "\n"
    r"\[ \frac{A(\triangle ABD)}{A(\triangle ADC)} = \frac{BD}{DC} = \frac{4}{6} = \frac{2}{3} \]" "\n"
    r"Therefore, $A(\triangle ABD) : A(\triangle ADC) = 2 : 3$."
)
exam_data.append((q9_text, [r"\(2 : 3\)", r"\(3 : 2\)", r"\(2 : 5\)", r"\(4 : 9\)"], "A", "OSC", "easy", q9_exp))

# Q10 (OSC) - Collinear Base ratio to full triangle with SVG
q10_text = (
    f"{q9_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD = 4\text{ cm}$ and $DC = 6\text{ cm}$. "
    r"Find the ratio $\frac{A(\triangle ABD)}{A(\triangle ABC)}$."
)
q10_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Find Total Base $BC$:**" "\n"
    r"Since $B-D-C$ are collinear, $BC = BD + DC = 4 + 6 = 10\text{ cm}$." "\n"
    r"2. **Examine Heights:** $\triangle ABD$ and $\triangle ABC$ share vertex $A$ and collinear bases on line $BC$. Hence, they have equal heights." "\n"
    r"3. **Calculate Ratio:**" "\n"
    r"\[ \frac{A(\triangle ABD)}{A(\triangle ABC)} = \frac{BD}{BC} = \frac{4}{10} = \frac{2}{5} \]" "\n"
    r"Thus, the ratio is $2 : 5$."
)
exam_data.append((q10_text, [r"\(2 : 5\)", r"\(2 : 3\)", r"\(3 : 5\)", r"\(4 : 7\)"], "A", "OSC", "medium", q10_exp))

# Q11 (OSC) - Median Property with SVG
q11_svg = svg_median_triangle(top='A', b_left='B', mid='M', b_right='C', title="Median of a Triangle")
q11_text = (
    f"{q11_svg}\n"
    r"In $\triangle ABC$, segment $AM$ is a median on side $BC$. "
    r"If the area of $\triangle ABC$ is $64\text{ cm}^2$, find the area of $\triangle ABM$."
)
q11_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Definition of Median:** A median connects a vertex to the midpoint of the opposite side. Hence, $M$ is the midpoint of $BC$, which means $BM = MC = \frac{1}{2} BC$." "\n"
    r"2. **Apply Equal Height Property:** $\triangle ABM$ and $\triangle AMC$ share common vertex $A$ and have bases $BM$ and $MC$ along the same line $BC$. Therefore, their heights are equal." "\n"
    r"\[ \frac{A(\triangle ABM)}{A(\triangle AMC)} = \frac{BM}{MC} = 1 \implies A(\triangle ABM) = A(\triangle AMC) \]" "\n"
    r"3. **Relate to Whole Triangle:**" "\n"
    r"\[ A(\triangle ABM) = \frac{1}{2} \times A(\triangle ABC) = \frac{1}{2} \times 64 = 32\text{ cm}^2 \]" "\n"
    r"Thus, $A(\triangle ABM) = 32\text{ cm}^2$."
)
exam_data.append((q11_text, [r"\(32\text{ cm}^2\)", r"\(16\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(64\text{ cm}^2\)"], "A", "OSC", "easy", q11_exp))

# Q12 (OSC) - Trapezium Diagonals with SVG
q12_svg = svg_trapezium_diagonals(title="Trapezium Diagonals Intersection")
q12_text = (
    f"{q12_svg}\n"
    r"In trapezium $ABCD$, side $AB \parallel \text{side } DC$. The diagonals $AC$ and $BD$ intersect at point $P$. "
    r"Which of the following statements about areas is TRUE?"
)
q12_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Consider $\triangle ADC$ and $\triangle BDC$:** Both triangles share the common base $DC$." "\n"
    r"2. Since $AB \parallel DC$, both vertices $A$ and $B$ lie on a line parallel to the base $DC$. Hence, their perpendicular distances from line $DC$ are equal ($h_1 = h_2$)." "\n"
    r"3. Therefore, $A(\triangle ADC) = A(\triangle BDC)$." "\n"
    r"4. **Subtract Common Region $\triangle DPC$ from Both Sides:**" "\n"
    r"\[ A(\triangle ADC) - A(\triangle DPC) = A(\triangle BDC) - A(\triangle DPC) \]" "\n"
    r"\[ A(\triangle APD) = A(\triangle BPC) \]" "\n"
    r"Thus, the areas of the two non-parallel side triangles $\triangle APD$ and $\triangle BPC$ are equal."
)
exam_data.append((q12_text, [r"\(A(\triangle APD) = A(\triangle BPC)\)", r"\(A(\triangle APB) = A(\triangle DPC)\)", r"\(A(\triangle ADC) > A(\triangle BDC)\)", r"\(A(\triangle APD) = A(\triangle APB)\)"], "A", "OSC", "medium", q12_exp))

# Q13 (OSC) - Quadrilateral Common Diagonal with SVG
q13_svg = svg_quadrilateral_common_diagonal(top='B', bot='D', left='A', right='C', h_top='6', h_bot='9', title="Quadrilateral with Common Diagonal")
q13_text = (
    f"{q13_svg}\n"
    r"In the figure, quadrilateral $ABCD$ has common diagonal $AC$. $BP \perp AC$ and $DQ \perp AC$. "
    r"If $BP = 6\text{ cm}$ and $DQ = 9\text{ cm}$, find the ratio $\frac{A(\triangle ABC)}{A(\triangle ADC)}$."
)
q13_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Common Base:** Both $\triangle ABC$ and $\triangle ADC$ share the common base $AC$." "\n"
    r"2. **Heights:** The corresponding heights drawn to base $AC$ are $BP = 6\text{ cm}$ and $DQ = 9\text{ cm}$." "\n"
    r"3. **Apply Property of Equal Bases:** The ratio of the areas of two triangles having equal bases is equal to the ratio of their corresponding heights:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{BP}{DQ} = \frac{6}{9} = \frac{2}{3} \]" "\n"
    r"Thus, the ratio is $2 : 3$."
)
exam_data.append((q13_text, [r"\(2 : 3\)", r"\(3 : 2\)", r"\(4 : 9\)", r"\(1 : 3\)"], "A", "OSC", "easy", q13_exp))

# Q14 (OSC) - Three Collinear Segments with SVG
q14_svg = svg_collinear_three_segments(top='A', b_left='B', d='D', e='E', b_right='C', len_bd='2', len_de='3', len_ec='4', title="Three Collinear Base Segments")
q14_text = (
    f"{q14_svg}\n"
    r"In $\triangle ABC$, points $D$ and $E$ lie on side $BC$ such that $BD = 2$, $DE = 3$, and $EC = 4$. "
    r"Find the continued ratio of their areas: $A(\triangle ABD) : A(\triangle ADE) : A(\triangle AEC)$."
)
q14_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Identify Common Vertex and Line:** Triangles $\triangle ABD$, $\triangle ADE$, and $\triangle AEC$ all share the common vertex $A$ and have their bases on the same straight line $BC$." "\n"
    r"2. **Equal Heights:** The perpendicular distance from $A$ to line $BC$ is common to all three triangles, so $h_1 = h_2 = h_3$." "\n"
    r"3. **Ratio of Areas:** Areas are directly proportional to their corresponding bases:" "\n"
    r"\[ A(\triangle ABD) : A(\triangle ADE) : A(\triangle AEC) = BD : DE : EC = 2 : 3 : 4 \]" "\n"
    r"Thus, the ratio is $2 : 3 : 4$."
)
exam_data.append((q14_text, [r"\(2 : 3 : 4\)", r"\(4 : 9 : 16\)", r"\(2 : 5 : 9\)", r"\(1 : 2 : 3\)"], "A", "OSC", "easy", q14_exp))

# Q15 (OSC) - Obtuse triangle altitude outside variation with SVG
q15_svg = svg_practice_set_1_1_q3(rq_val='8', ps_val='9', pr_val='12', qt_label='QT = ?', title="Altitude to Base and Extended Ray")
q15_text = (
    f"{q15_svg}\n"
    r"In $\triangle PQR$, segment $PS \perp \text{ray } RQ$ with $PS = 9$, and segment $QT \perp PR$ with $PR = 12$. "
    r"If $RQ = 8$, find the length of altitude $QT$."
)
q15_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Calculate Area of $\triangle PQR$ using Base $RQ$:**" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times RQ \times PS = \frac{1}{2} \times 8 \times 9 = 36 \]" "\n"
    r"2. **Equate with Area using Base $PR$:**" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times PR \times QT \]" "\n"
    r"\[ 36 = \frac{1}{2} \times 12 \times QT \implies 36 = 6 \times QT \]" "\n"
    r"3. **Solve for $QT$:**" "\n"
    r"\[ QT = \frac{36}{6} = 6 \]" "\n"
    r"Thus, the length of segment $QT$ is $6$."
)
exam_data.append((q15_text, [r"\(6\)", r"\(5\)", r"\(4.5\)", r"\(8\)"], "A", "OSC", "medium", q15_exp))

# Q16 (OSC) - General Ratio of Areas with Two Triangles SVG
q16_svg = svg_two_triangles(('X','Y','Z','M'), 'b₁ = 12', 'h₁ = 7', ('U','V','W','N'), 'b₂ = 14', 'h₂ = 6', title="Two Triangles Area Ratio")
q16_text = (
    f"{q16_svg}\n"
    r"In the figure, $\triangle XYZ$ has base $YZ = 12$ and height $XM = 7$. "
    r"$\triangle UVW$ has base $VW = 14$ and height $UN = 6$. "
    r"Find the ratio $\frac{A(\triangle XYZ)}{A(\triangle UVW)}$."
)
q16_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Use General Property:**" "\n"
    r"\[ \frac{A(\triangle XYZ)}{A(\triangle UVW)} = \frac{b_1 \times h_1}{b_2 \times h_2} \]" "\n"
    r"2. **Substitute Values:**" "\n"
    r"\[ \frac{A(\triangle XYZ)}{A(\triangle UVW)} = \frac{12 \times 7}{14 \times 6} = \frac{84}{84} = 1 \]" "\n"
    r"3. **Conclusion:** Both triangles have equal areas, so the ratio is $1 : 1$."
)
exam_data.append((q16_text, [r"\(1 : 1\)", r"\(2 : 1\)", r"\(3 : 2\)", r"\(6 : 7\)"], "A", "OSC", "medium", q16_exp))

# Q17 (OSC) - Equal Heights Finding Area
q17_svg = svg_collinear_base(top='P', b_left='Q', b_mid='S', b_right='R', len_bd='3', len_dc='5', show_alt=True, title="Equal Heights - Area Computation")
q17_text = (
    f"{q17_svg}\n"
    r"In $\triangle PQR$, point $S$ lies on side $QR$ such that $QS : SR = 3 : 5$. "
    r"If the area of $\triangle PQS$ is $24\text{ cm}^2$, what is the area of $\triangle PSR$?"
)
q17_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Property of Triangles with Equal Heights:** $\triangle PQS$ and $\triangle PSR$ share common vertex $P$ and collinear bases on line $QR$. Hence, their heights are equal:" "\n"
    r"\[ \frac{A(\triangle PQS)}{A(\triangle PSR)} = \frac{QS}{SR} \]" "\n"
    r"2. **Substitute Given Values:**" "\n"
    r"\[ \frac{24}{A(\triangle PSR)} = \frac{3}{5} \]" "\n"
    r"3. **Solve for $A(\triangle PSR)$:**" "\n"
    r"\[ A(\triangle PSR) = \frac{24 \times 5}{3} = 8 \times 5 = 40\text{ cm}^2 \]" "\n"
    r"Thus, the area of $\triangle PSR$ is $40\text{ cm}^2$."
)
exam_data.append((q17_text, [r"\(40\text{ cm}^2\)", r"\(30\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(64\text{ cm}^2\)"], "A", "OSC", "medium", q17_exp))

# Q18 (OSC) - Equal Bases Finding Unknown Height
q18_svg = svg_practice_set_1_1_q2(bc_val='6', ad_val='h', title="Common Base - Finding Height")
q18_text = (
    f"{q18_svg}\n"
    r"Two triangles $\triangle ABC$ and $\triangle ADB$ share a common base $AB$. $BC \perp AB$ and $AD \perp AB$. "
    r"If $BC = 6\text{ cm}$ and $\frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{2}{5}$, find the height $AD$."
)
q18_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Apply Equal Base Property:**" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD} \]" "\n"
    r"2. **Substitute Known Values:**" "\n"
    r"\[ \frac{2}{5} = \frac{6}{AD} \]" "\n"
    r"3. **Cross Multiply:**" "\n"
    r"\[ 2 \times AD = 6 \times 5 = 30 \implies AD = \frac{30}{2} = 15\text{ cm} \]" "\n"
    r"Therefore, the height $AD$ is $15\text{ cm}$."
)
exam_data.append((q18_text, [r"\(15\text{ cm}\)", r"\(12\text{ cm}\)", r"\(10\text{ cm}\)", r"\(18\text{ cm}\)"], "A", "OSC", "medium", q18_exp))

# Q19 (OSC) - Midpoint of Median
q19_svg = svg_median_triangle(top='A', b_left='B', mid='D', b_right='C', title="Triangle with Median")
q19_text = (
    f"{q19_svg}\n"
    r"In $\triangle ABC$, $AD$ is a median. If $P$ is the midpoint of segment $AD$, "
    r"what fraction of the total area $A(\triangle ABC)$ is the area of $\triangle BPD$?"
)
q19_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Median $AD$ Property:** Since $AD$ is a median of $\triangle ABC$:" "\n"
    r"\[ A(\triangle ABD) = \frac{1}{2} A(\triangle ABC) \]" "\n"
    r"2. **In $\triangle ABD$, $BP$ is a Cevian to Midpoint $P$ of $AD$:**" "\n"
    r"$\triangle BPD$ and $\triangle BPA$ share vertex $B$ and have bases $PD$ and $AP$ along the line $AD$. Since $P$ is the midpoint of $AD$, $PD = AP$." "\n"
    r"Therefore, $BP$ acts as a median in $\triangle ABD$:" "\n"
    r"\[ A(\triangle BPD) = \frac{1}{2} A(\triangle ABD) \]" "\n"
    r"3. **Combine Ratios:**" "\n"
    r"\[ A(\triangle BPD) = \frac{1}{2} \times \left(\frac{1}{2} A(\triangle ABC)\right) = \frac{1}{4} A(\triangle ABC) \]" "\n"
    r"Thus, the area is $\frac{1}{4}$ of the total area."
)
exam_data.append((q19_text, [r"\(\frac{1}{4}\)", r"\(\frac{1}{2}\)", r"\(\frac{1}{3}\)", r"\(\frac{1}{8}\)"], "A", "OSC", "hard", q19_exp))

# Q20 (OSC) - Ratio of Bases and Heights Algebraic
q20_text = (
    r"The ratio of the bases of two triangles is $3 : 4$ and the ratio of their corresponding heights is $8 : 9$. "
    r"What is the ratio of their areas?"
)
q20_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Formula:** For any two triangles, the ratio of areas is:" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2} = \left(\frac{b_1}{b_2}\right) \times \left(\frac{h_1}{h_2}\right) \]" "\n"
    r"2. **Substitute Given Ratios:**" "\n"
    r"\[ \frac{b_1}{b_2} = \frac{3}{4}, \quad \frac{h_1}{h_2} = \frac{8}{9} \]" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{3}{4} \times \frac{8}{9} = \frac{24}{36} \]" "\n"
    r"3. **Simplify:**" "\n"
    r"Dividing numerator and denominator by $12$:" "\n"
    r"\[ \frac{24 \div 12}{36 \div 12} = \frac{2}{3} \]" "\n"
    r"Therefore, the ratio of areas is $2 : 3$."
)
exam_data.append((q20_text, [r"\(2 : 3\)", r"\(3 : 2\)", r"\(1 : 2\)", r"\(4 : 3\)"], "A", "OSC", "medium", q20_exp))

# Q21 (OMC) - Multiple Correct: Properties of Triangle Areas
q21_text = (
    r"Which of the following statements are **TRUE** regarding the ratio of areas of two triangles? (Select all that apply)"
)
q21_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"- **Statement A:** 'If heights of two triangles are equal, the ratio of their areas equals the ratio of their corresponding bases.' $\rightarrow$ **TRUE** (Standard property: $\frac{A_1}{A_2} = \frac{b_1}{b_2}$ when $h_1 = h_2$)." "\n"
    r"- **Statement B:** 'If bases of two triangles are equal, the ratio of their areas equals the ratio of their corresponding heights.' $\rightarrow$ **TRUE** (Standard property: $\frac{A_1}{A_2} = \frac{h_1}{h_2}$ when $b_1 = b_2$)." "\n"
    r"- **Statement C:** 'Two triangles with equal areas are always congruent.' $\rightarrow$ **FALSE** (Two triangles can have base $6, \text{height } 4$ (area 12) and base $8, \text{height } 3$ (area 12) without being congruent)." "\n"
    r"- **Statement D:** 'If both bases and heights of two triangles are equal, their areas are equal.' $\rightarrow$ **TRUE** ($\frac{A_1}{A_2} = \frac{b \times h}{b \times h} = 1 \implies A_1 = A_2$)." "\n"
    r"Thus, statements A, B, and D are correct."
)
exam_data.append((q21_text, [
    "If heights are equal, ratio of areas is equal to the ratio of bases",
    "If bases are equal, ratio of areas is equal to the ratio of heights",
    "Two triangles having equal areas must always be congruent",
    "If both bases and heights are equal, their areas are equal"
], ["A", "B", "D"], "OMC", "medium", q21_exp))

# Q22 (OMC) - Multiple Correct with SVG
q22_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='3', len_dc='5', show_alt=False, title="Cevian AD on Base BC")
q22_text = (
    f"{q22_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD : DC = 3 : 5$. "
    r"Which of the following area ratios are **CORRECT**? (Select all that apply)"
)
q22_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"Both $\triangle ABD$ and $\triangle ADC$ share common vertex $A$ and have collinear bases on line $BC$. Therefore, their heights are equal." "\n"
    r"1. $\frac{A(\triangle ABD)}{A(\triangle ADC)} = \frac{BD}{DC} = \frac{3}{5}$. (Option A is correct)." "\n"
    r"2. Since $BC = BD + DC = 3 + 5 = 8$ parts:" "\n"
    r"$\frac{A(\triangle ABD)}{A(\triangle ABC)} = \frac{BD}{BC} = \frac{3}{8}$. (Option B is correct)." "\n"
    r"3. $\frac{A(\triangle ADC)}{A(\triangle ABC)} = \frac{DC}{BC} = \frac{5}{8}$. (Option C is correct)." "\n"
    r"4. $\frac{A(\triangle ABC)}{A(\triangle ABD)} = \frac{8}{3} \neq \frac{5}{3}$. (Option D is incorrect)." "\n"
    r"Thus, options A, B, and C are correct."
)
exam_data.append((q22_text, [
    r"\(\frac{A(\triangle ABD)}{A(\triangle ADC)} = \frac{3}{5}\)",
    r"\(\frac{A(\triangle ABD)}{A(\triangle ABC)} = \frac{3}{8}\)",
    r"\(\frac{A(\triangle ADC)}{A(\triangle ABC)} = \frac{5}{8}\)",
    r"\(\frac{A(\triangle ABC)}{A(\triangle ABD)} = \frac{5}{3}\)"
], ["A", "B", "C"], "OMC", "medium", q22_exp))

# Q23 (OMC) - Parallel Lines Triangles Multi-Select with SVG
q23_svg = svg_parallel_lines_triangles(top_l='A', top_r='D', bot_l='B', bot_r='C', title="Triangles Between Parallel Lines")
q23_text = (
    f"{q23_svg}\n"
    r"In the figure, line $AD \parallel \text{line } BC$. Points $A, D$ lie on the upper line and $B, C$ lie on the lower line. "
    r"Which of the following statements are **TRUE**? (Select all that apply)"
)
q23_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Equal Heights:** Because line $AD \parallel \text{line } BC$, the perpendicular distance between the lines is constant. Thus, any triangle with base on $BC$ and vertex on line $AD$ has the same height $h$. (Option A is TRUE)." "\n"
    r"2. **Equal Base and Height:** $\triangle ABC$ and $\triangle DBC$ share base $BC$ and have the same height $h$. Hence, $A(\triangle ABC) = A(\triangle DBC)$. (Option B is TRUE)." "\n"
    r"3. **Ratio of Areas:** $\frac{A(\triangle ABC)}{A(\triangle DBC)} = 1 : 1$. (Option C is TRUE)." "\n"
    r"4. **Congruence:** Equal area does not necessarily mean $\triangle ABC \cong \triangle DBC$ unless corresponding sides and angles are proven equal. (Option D is FALSE)." "\n"
    r"Thus, A, B, and C are true."
)
exam_data.append((q23_text, [
    "Heights of all triangles having base on line BC and vertex on line AD are equal",
    r"\(A(\triangle ABC) = A(\triangle DBC)\)",
    r"The ratio \(A(\triangle ABC) : A(\triangle DBC) = 1 : 1\)",
    r"\(\triangle ABC \cong \triangle DBC\) necessarily in every case"
], ["A", "B", "C"], "OMC", "medium", q23_exp))

# Q24 (OMC) - Conditions for Equal Areas
q24_text = (
    r"Under which of the following geometric conditions do two triangles $\triangle_1$ and $\triangle_2$ have **EQUAL AREAS** ($A_1 = A_2$)? (Select all that apply)"
)
q24_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"- **Case A:** $b_1 = b_2$ and $h_1 = h_2 \implies \frac{1}{2} b_1 h_1 = \frac{1}{2} b_2 h_2 \implies A_1 = A_2$. (TRUE)" "\n"
    r"- **Case B:** $b_1 h_1 = b_2 h_2$ (e.g. $b_1 = 6, h_1 = 4$ and $b_2 = 8, h_2 = 3$) $\implies A_1 = A_2$. (TRUE)" "\n"
    r"- **Case C:** Two triangles formed by drawing a median from any vertex of a triangle. (TRUE, since median creates equal bases and common height)." "\n"
    r"- **Case D:** Triangles having equal perimeters. (FALSE, equal perimeter does not guarantee equal area)." "\n"
    r"Thus, options A, B, and C are correct."
)
exam_data.append((q24_text, [
    "When both their bases and corresponding heights are equal",
    "When the product of base and height is the same for both triangles",
    "When the two triangles are formed by drawing a median of a triangle",
    "Whenever the two triangles have equal perimeters"
], ["A", "B", "C"], "OMC", "medium", q24_exp))

# Q25 (OMC) - Quadrilateral Diagonals with SVG
q25_svg = svg_quadrilateral_common_diagonal(top='B', bot='D', left='A', right='C', h_top='h₁', h_bot='h₂', title="Quadrilateral Properties")
q25_text = (
    f"{q25_svg}\n"
    r"In quadrilateral $ABCD$, diagonal $AC$ is drawn. $BP \perp AC$ with length $h_1$, and $DQ \perp AC$ with length $h_2$. "
    r"Which of the following relations are **TRUE**? (Select all that apply)"
)
q25_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Area of $\triangle ABC$:** $A(\triangle ABC) = \frac{1}{2} \times AC \times h_1$. (TRUE)" "\n"
    r"2. **Area of $\triangle ADC$:** $A(\triangle ADC) = \frac{1}{2} \times AC \times h_2$. (TRUE)" "\n"
    r"3. **Ratio of Areas:** Since base $AC$ is common:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{h_1}{h_2} \]" "\n"
    r"4. **Total Area of Quadrilateral:**" "\n"
    r"\[ A(\square ABCD) = A(\triangle ABC) + A(\triangle ADC) = \frac{1}{2} \times AC \times (h_1 + h_2) \]" "\n"
    r"All given options are geometrically sound and correct."
)
exam_data.append((q25_text, [
    r"\(\frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{h_1}{h_2}\)",
    r"\(A(\square ABCD) = \frac{1}{2} \times AC \times (h_1 + h_2)\)",
    r"\(A(\triangle ABC) = \frac{1}{2} \times AC \times h_1\)",
    r"\(\frac{A(\triangle ABC)}{A(\square ABCD)} = \frac{h_1}{h_1 + h_2}\)"
], ["A", "B", "C", "D"], "OMC", "hard", q25_exp))

# Q26 (OMC) - Practice Set 1.1 Q3 Equations with SVG
q26_svg = svg_practice_set_1_1_q3(rq_val='RQ', ps_val='PS', pr_val='PR', qt_label='QT', title="Two Expressions for Area")
q26_text = (
    f"{q26_svg}\n"
    r"In $\triangle PQR$, segment $PS \perp \text{ray } RQ$ and segment $QT \perp PR$. "
    r"Which of the following equations correctly express the area of $\triangle PQR$? (Select all that apply)"
)
q26_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Taking $RQ$ as base, the corresponding height is altitude $PS$: $\text{Area} = \frac{1}{2} \times RQ \times PS$. (Option A is TRUE)." "\n"
    r"2. Taking $PR$ as base, the corresponding height is altitude $QT$: $\text{Area} = \frac{1}{2} \times PR \times QT$. (Option B is TRUE)." "\n"
    r"3. Equating both expressions: $\frac{1}{2} \times RQ \times PS = \frac{1}{2} \times PR \times QT \implies RQ \times PS = PR \times QT$. (Option C is TRUE)." "\n"
    r"4. $RQ \times PR = PS \times QT$ is incorrect. (Option D is FALSE)." "\n"
    r"Thus, A, B, and C are correct."
)
exam_data.append((q26_text, [
    r"\(A(\triangle PQR) = \frac{1}{2} \times RQ \times PS\)",
    r"\(A(\triangle PQR) = \frac{1}{2} \times PR \times QT\)",
    r"\(RQ \times PS = PR \times QT\)",
    r"\(RQ \times PR = PS \times QT\)"
], ["A", "B", "C"], "OMC", "medium", q26_exp))

# Q27 (OTF) - Equal area vs Congruence
q27_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'If two triangles have equal areas, they must always be congruent.'**"
)
q27_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Definition of Congruence:** Congruent triangles must have identical shapes and sizes (corresponding sides equal and corresponding angles equal)." "\n"
    r"2. **Counterexample:** Consider triangle $T_1$ with base $6$ and height $4$, area $= \frac{1}{2} \times 6 \times 4 = 12$. Consider triangle $T_2$ with base $8$ and height $3$, area $= \frac{1}{2} \times 8 \times 3 = 12$." "\n"
    r"Both have equal area ($12$), but their side lengths and shapes differ, so they are not congruent." "\n"
    r"Therefore, the statement is **False**."
)
exam_data.append((q27_text, ["True", "False"], "B", "OTF", "easy", q27_exp))

# Q28 (OTF) - Median Bisects Area with SVG
q28_svg = svg_median_triangle(top='P', b_left='Q', mid='D', b_right='R', title="Median Divides Area Equally")
q28_text = (
    f"{q28_svg}\n"
    r"State whether the following statement is True or False:" "\n\n"
    r"**'A median of a triangle divides it into two triangles of equal area.'**"
)
q28_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. In $\triangle PQR$, let $PD$ be the median drawn to side $QR$." "\n"
    r"2. By definition of median, $D$ is the midpoint of $QR$, so $QD = DR$." "\n"
    r"3. Both $\triangle PQD$ and $\triangle PDR$ share the common vertex $P$ and have collinear bases on line $QR$, which means they have the exact same perpendicular height $h$." "\n"
    r"4. Therefore, $\frac{A(\triangle PQD)}{A(\triangle PDR)} = \frac{QD}{DR} = \frac{QD}{QD} = 1 \implies A(\triangle PQD) = A(\triangle PDR)$." "\n"
    r"Hence, the statement is **True**."
)
exam_data.append((q28_text, ["True", "False"], "A", "OTF", "easy", q28_exp))

# Q29 (OTF) - Constant Distance of Parallel Lines
q29_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'Triangles having a common base and situated between the same two parallel lines always have equal areas.'**"
)
q29_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. The perpendicular distance between two parallel lines is constant everywhere." "\n"
    r"2. If two triangles share a common base $b$ and their third vertices lie on a line parallel to the base, their heights $h$ are identical." "\n"
    r"3. Consequently, both have area $\frac{1}{2} \times b \times h$, which makes their areas equal." "\n"
    r"Thus, the statement is **True**."
)
exam_data.append((q29_text, ["True", "False"], "A", "OTF", "easy", q29_exp))

# Q30 (OTF) - Triangles with Equal Bases Property
q30_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'The ratio of areas of two triangles having equal bases is equal to the ratio of their corresponding heights.'**"
)
q30_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Formula for ratio of areas: $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2}$." "\n"
    r"2. When bases are equal ($b_1 = b_2 = b$):" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{b \times h_1}{b \times h_2} = \frac{h_1}{h_2} \]" "\n"
    r"This is one of the fundamental theorems of Topic 1.1 in Maharashtra Board Class 10 Geometry." "\n"
    r"Therefore, the statement is **True**."
)
exam_data.append((q30_text, ["True", "False"], "A", "OTF", "easy", q30_exp))

# Q31 (OAR) - Assertion Reason Median with SVG
q31_svg = svg_median_triangle(top='A', b_left='B', mid='D', b_right='C', title="Median Area Property")
q31_assertion = r"In $\triangle ABC$, median $AD$ divides the triangle into $\triangle ABD$ and $\triangle ADC$ such that $A(\triangle ABD) = A(\triangle ADC)$."
q31_reason = r"Triangles having equal bases on the same straight line and sharing a common vertex have equal heights."
q31_text = f"{q31_svg}\nAssertion (A): {q31_assertion}\nReason (R): {q31_reason}"
q31_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Check Assertion (A):** In $\triangle ABC$, median $AD$ divides $BC$ into two equal parts ($BD = DC$). Both $\triangle ABD$ and $\triangle ADC$ share the vertex $A$ and have bases on line $BC$. Hence, their areas are equal. Assertion (A) is **True**." "\n"
    r"2. **Check Reason (R):** Since the vertices coincide at $A$ and the bases lie on the same line $BC$, the perpendicular distance from $A$ to $BC$ is identical for both triangles. Reason (R) is **True**." "\n"
    r"3. **Check Explanation:** Because their heights are equal and their bases are equal ($BD = DC$), their areas are equal: $\frac{A_1}{A_2} = \frac{BD}{DC} = 1$. Reason (R) correctly explains Assertion (A)." "\n"
    r"Therefore, both Assertion and Reason are true, and Reason is the correct explanation of Assertion (Option A)."
)
exam_data.append((q31_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "medium", q31_exp, q31_assertion, q31_reason, q31_svg))

# Q32 (OAR) - Parallel Lines Assertion Reason with SVG
q32_svg = svg_parallel_lines_triangles(top_l='A', top_r='D', bot_l='B', bot_r='C', title="Triangles Between Parallel Lines")
q32_assertion = r"If line segment $AD \parallel \text{segment } BC$, then $A(\triangle ABC) = A(\triangle DBC)$."
q32_reason = r"The perpendicular distance between two parallel lines is constant throughout, so triangles having a common base and vertices on a parallel line have equal heights."
q32_text = f"{q32_svg}\nAssertion (A): {q32_assertion}\nReason (R): {q32_reason}"
q32_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Assertion (A):** $\triangle ABC$ and $\triangle DBC$ share the common base $BC$. Since $AD \parallel BC$, both vertices $A$ and $D$ are on the parallel line, making their heights equal. Hence $A(\triangle ABC) = A(\triangle DBC)$. Assertion (A) is **True**." "\n"
    r"2. **Reason (R):** By geometric definition, the distance between two parallel lines is constant everywhere. Thus, heights of triangles between parallel lines are equal. Reason (R) is **True**." "\n"
    r"3. **Explanation Check:** Since both triangles share the base $BC$ and have equal heights (as stated in R), their areas are equal. Thus, Reason (R) is the correct explanation of Assertion (A)."
)
exam_data.append((q32_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "medium", q32_exp, q32_assertion, q32_reason, q32_svg))

# Q33 (OAR) - Reciprocal Base and Height Ratio
q33_assertion = r"If the bases of two triangles are in the ratio $2 : 3$ and their heights are in the ratio $3 : 2$, then the two triangles have equal areas."
q33_reason = r"The ratio of the areas of two triangles is given by $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2}$, and $\frac{2 \times 3}{3 \times 2} = 1$."
q33_text = f"Assertion (A): {q33_assertion}\nReason (R): {q33_reason}"
q33_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Check Assertion (A):** Area ratio is $\frac{A_1}{A_2} = \left(\frac{b_1}{b_2}\right) \times \left(\frac{h_1}{h_2}\right) = \frac{2}{3} \times \frac{3}{2} = 1$. Since the ratio is $1$, $A_1 = A_2$. Assertion (A) is **True**." "\n"
    r"2. **Check Reason (R):** The general property for area ratio of two triangles is $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2}$, and substituting the values gives $\frac{6}{6} = 1$. Reason (R) is **True**." "\n"
    r"3. **Explanation:** Reason (R) gives the precise mathematical calculation that proves Assertion (A)." "\n"
    r"Therefore, both Assertion and Reason are true, and Reason is the correct explanation."
)
exam_data.append((q33_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "medium", q33_exp, q33_assertion, q33_reason, None))

# Q34 (OAR) - Equal Area Does Not Imply Equal Perimeters
q34_assertion = r"Two triangles having equal areas always have equal perimeters."
q34_reason = r"The area of a triangle depends only on its base and corresponding height ($A = \frac{1}{2} b h$), whereas perimeter depends on the sum of all three side lengths."
q34_text = f"Assertion (A): {q34_assertion}\nReason (R): {q34_reason}"
q34_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Check Assertion (A):** Two triangles can have identical areas with completely different side lengths (e.g. a right triangle with sides $3, 4, 5$ has area $6$ and perimeter $12$; a triangle with base $12$ and height $1$ has area $6$ but perimeter $> 24$). Thus, Assertion (A) is **False**." "\n"
    r"2. **Check Reason (R):** Area depends on base and height, while perimeter is the sum of the three sides. This statement is scientifically and geometrically **True**." "\n"
    r"Hence, Assertion (A) is false, but Reason (R) is true (Option D)."
)
exam_data.append((q34_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "D", "OAR", "medium", q34_exp, q34_assertion, q34_reason, None))

# Q35 (ONE) - Practice Set 1.1 Q1 Value of k with SVG
q35_svg = svg_two_triangles(('A','B','C','D'), 'b₁ = 9', 'h₁ = 5', ('P','Q','R','S'), 'b₂ = 10', 'h₂ = 6', title="Find Value of k")
q35_text = (
    f"{q35_svg}\n"
    r"The base of $\triangle_1$ is $9$ and height is $5$. The base of $\triangle_2$ is $10$ and height is $6$. "
    r"If the ratio of their areas in simplest form is written as $\frac{A(\triangle_1)}{A(\triangle_2)} = \frac{3}{k}$, find the value of $k$."
)
q35_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Calculate Area Ratio:**" "\n"
    r"\[ \frac{A(\triangle_1)}{A(\triangle_2)} = \frac{b_1 \times h_1}{b_2 \times h_2} = \frac{9 \times 5}{10 \times 6} = \frac{45}{60} \]" "\n"
    r"2. **Simplify the Fraction:**" "\n"
    r"\[ \frac{45 \div 15}{60 \div 15} = \frac{3}{4} \]" "\n"
    r"3. **Compare with $\frac{3}{k}$:**" "\n"
    r"\[ \frac{3}{4} = \frac{3}{k} \implies k = 4 \]" "\n"
    r"Thus, the value of $k$ is $4$."
)
exam_data.append((q35_text, [], "4", "ONE", "easy", q35_exp))

# Q36 (ONE) - Numerical Decimal Practice Set 1.1 Q2 with SVG
q36_svg = svg_practice_set_1_1_q2(bc_val='4', ad_val='8', title="Decimal Area Ratio")
q36_text = (
    f"{q36_svg}\n"
    r"In the figure, $BC \perp AB$, $AD \perp AB$, $BC = 4$, and $AD = 8$. "
    r"Calculate the value of the ratio $\frac{A(\triangle ABC)}{A(\triangle ADB)}$ expressed as a decimal."
)
q36_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since base $AB$ is common to both triangles:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD} \]" "\n"
    r"2. Substitute values:" "\n"
    r"\[ \frac{BC}{AD} = \frac{4}{8} = 0.5 \]" "\n"
    r"Thus, the decimal value of the ratio is $0.5$."
)
exam_data.append((q36_text, [], "0.5", "ONE", "easy", q36_exp))

# Q37 (ONE) - Practice Set 1.1 Q3 Find QT with SVG
q37_svg = svg_practice_set_1_1_q3(rq_val='6', ps_val='6', pr_val='12', qt_label='QT = ?', title="Find Segment QT")
q37_text = (
    f"{q37_svg}\n"
    r"In $\triangle PQR$, segment $PS \perp \text{ray } RQ$ with $PS = 6$, and segment $QT \perp PR$ with $PR = 12$. "
    r"If $RQ = 6$, calculate the length of segment $QT$."
)
q37_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Area of $\triangle PQR$ using base $RQ$ and height $PS$:" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times 6 \times 6 = 18 \]" "\n"
    r"2. Area of $\triangle PQR$ using base $PR$ and height $QT$:" "\n"
    r"\[ A(\triangle PQR) = \frac{1}{2} \times 12 \times QT = 6 \times QT \]" "\n"
    r"3. Equating both expressions:" "\n"
    r"\[ 6 \times QT = 18 \implies QT = 3 \]" "\n"
    r"Thus, $QT = 3$."
)
exam_data.append((q37_text, [], "3", "ONE", "medium", q37_exp))

# Q38 (ONE) - Collinear Base Find Area with SVG
q38_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='5', len_dc='10', show_alt=True, title="Compute Triangle Area")
q38_text = (
    f"{q38_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD = 5\text{ cm}$ and $DC = 10\text{ cm}$. "
    r"If the area of $\triangle ABD$ is $20\text{ cm}^2$, find the area of $\triangle ADC$ in $\text{cm}^2$."
)
q38_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $\triangle ABD$ and $\triangle ADC$ share common vertex $A$ and have bases on line $BC$. Hence, their heights are equal." "\n"
    r"2. Ratio of areas equals ratio of bases:" "\n"
    r"\[ \frac{A(\triangle ABD)}{A(\triangle ADC)} = \frac{BD}{DC} \]" "\n"
    r"3. Substitute given numbers:" "\n"
    r"\[ \frac{20}{A(\triangle ADC)} = \frac{5}{10} = \frac{1}{2} \]" "\n"
    r"\[ A(\triangle ADC) = 20 \times 2 = 40\text{ cm}^2 \]" "\n"
    r"Thus, the area of $\triangle ADC$ is $40\text{ cm}^2$."
)
exam_data.append((q38_text, [], "40", "ONE", "easy", q38_exp))

# Q39 (ONE) - Median Half Area with SVG
q39_svg = svg_median_triangle(top='A', b_left='B', mid='M', b_right='C', title="Median Half Area")
q39_text = (
    f"{q39_svg}\n"
    r"In $\triangle ABC$, segment $AM$ is a median to side $BC$. "
    r"If the total area of $\triangle ABC$ is $76\text{ cm}^2$, find the area of $\triangle ABM$ in $\text{cm}^2$."
)
q39_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since $AM$ is a median, $M$ is the midpoint of $BC$, so $BM = MC$." "\n"
    r"2. Triangles $\triangle ABM$ and $\triangle AMC$ share vertex $A$ and have collinear equal bases, so their heights and bases are equal." "\n"
    r"\[ A(\triangle ABM) = \frac{1}{2} \times A(\triangle ABC) = \frac{76}{2} = 38\text{ cm}^2 \]" "\n"
    r"Thus, the area is $38\text{ cm}^2$."
)
exam_data.append((q39_text, [], "38", "ONE", "easy", q39_exp))

# Q40 (ONE) - Equal Bases Ratio of Heights
q40_text = (
    r"Two triangles have equal bases. The height of the first triangle is $8\text{ cm}$ and the height of the second triangle is $12\text{ cm}$. "
    r"If the area of the first triangle is $24\text{ cm}^2$, find the area of the second triangle in $\text{cm}^2$."
)
q40_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since both triangles have equal bases ($b_1 = b_2$):" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{h_1}{h_2} \]" "\n"
    r"2. Substitute $A_1 = 24$, $h_1 = 8$, $h_2 = 12$:" "\n"
    r"\[ \frac{24}{A_2} = \frac{8}{12} = \frac{2}{3} \]" "\n"
    r"3. Solve for $A_2$:" "\n"
    r"\[ 2 \times A_2 = 24 \times 3 = 72 \implies A_2 = \frac{72}{2} = 36\text{ cm}^2 \]" "\n"
    r"Thus, the area of the second triangle is $36\text{ cm}^2$."
)
exam_data.append((q40_text, [], "36", "ONE", "medium", q40_exp))

print(f"Loaded {len(exam_data)} Exam questions.")

# =========================================================================
# PRACTICE POOL (30 Questions: 041 - 070)
# =========================================================================
prac_data = []

# Q41 (OSC) - Practice Set 1.1 Q1 variation with SVG
q41_svg = svg_two_triangles(('D','E','F','G'), 'b₁ = 12', 'h₁ = 8', ('P','Q','R','S'), 'b₂ = 16', 'h₂ = 6', title="Practice 1.1 - Variation")
q41_text = (
    f"{q41_svg}\n"
    r"In the figure, $\triangle DEF$ has base $EF = 12$ and height $DG = 8$. "
    r"$\triangle PQR$ has base $QR = 16$ and height $PS = 6$. "
    r"Find the ratio of their areas: $\frac{A(\triangle DEF)}{A(\triangle PQR)}$."
)
q41_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Ratio of areas: $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2}$." "\n"
    r"2. Substitute values: $\frac{12 \times 8}{16 \times 6} = \frac{96}{96} = 1$." "\n"
    r"Thus, the ratio is $1 : 1$."
)
prac_data.append((q41_text, [r"\(1 : 1\)", r"\(2 : 3\)", r"\(3 : 4\)", r"\(4 : 3\)"], "A", "OSC", "easy", q41_exp))

# Q42 (OSC) - Practice Set 1.1 Q2 variation with SVG
q42_svg = svg_practice_set_1_1_q2(bc_val='6', ad_val='9', title="Practice Set 1.1 Q2 Variation")
q42_text = (
    f"{q42_svg}\n"
    r"In the figure, $BC \perp AB$, $AD \perp AB$. If $BC = 6$ and $AD = 9$, "
    r"find the ratio $\frac{A(\triangle ABC)}{A(\triangle ADB)}$."
)
q42_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Base $AB$ is common to both triangles." "\n"
    r"2. $\frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD} = \frac{6}{9} = \frac{2}{3}$." "\n"
    r"Thus, the ratio is $2 : 3$."
)
prac_data.append((q42_text, [r"\(2 : 3\)", r"\(3 : 2\)", r"\(1 : 2\)", r"\(4 : 9\)"], "A", "OSC", "easy", q42_exp))

# Q43 (OSC) - Practice Set 1.1 Q3 variation with SVG
q43_svg = svg_practice_set_1_1_q3(rq_val='10', ps_val='6', pr_val='15', qt_label='QT = ?', title="Practice Set 1.1 Q3 Variation")
q43_text = (
    f"{q43_svg}\n"
    r"In $\triangle PQR$, segment $PS \perp \text{ray } RQ$ with $PS = 6$, and segment $QT \perp PR$ with $PR = 15$. "
    r"If $RQ = 10$, find the length of segment $QT$."
)
q43_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Area using base $RQ$: $A = \frac{1}{2} \times 10 \times 6 = 30$." "\n"
    r"2. Area using base $PR$: $A = \frac{1}{2} \times 15 \times QT = 7.5 \times QT$." "\n"
    r"3. Solve: $7.5 \times QT = 30 \implies QT = \frac{30}{7.5} = 4$." "\n"
    r"Therefore, $QT = 4$."
)
prac_data.append((q43_text, [r"\(4\)", r"\(5\)", r"\(3\)", r"\(6\)"], "A", "OSC", "medium", q43_exp))

# Q44 (OSC) - Practice Set 1.1 Q4 variation with SVG
q44_svg = svg_parallel_lines_triangles(top_l='P', top_r='S', bot_l='Q', bot_r='R', title="Parallel Lines Area Equality")
q44_text = (
    f"{q44_svg}\n"
    r"In the figure, line $PS \parallel \text{line } QR$. "
    r"If the area of $\triangle PQR$ is $45\text{ cm}^2$, what is the area of $\triangle SQR$?"
)
q44_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Both triangles $\triangle PQR$ and $\triangle SQR$ share the common base $QR$." "\n"
    r"2. Both vertices $P$ and $S$ lie on the line parallel to base $QR$, so their perpendicular heights are equal ($h_1 = h_2$)." "\n"
    r"3. Areas are equal: $A(\triangle SQR) = A(\triangle PQR) = 45\text{ cm}^2$."
)
prac_data.append((q44_text, [r"\(45\text{ cm}^2\)", r"\(90\text{ cm}^2\)", r"\(22.5\text{ cm}^2\)", r"\(60\text{ cm}^2\)"], "A", "OSC", "easy", q44_exp))

# Q45 (OSC) - Collinear Base ratio 1:3 with SVG
q45_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='3', len_dc='9', show_alt=False, title="Collinear Base 1:3")
q45_text = (
    f"{q45_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD = 3\text{ cm}$ and $DC = 9\text{ cm}$. "
    r"Find the ratio $\frac{A(\triangle ABD)}{A(\triangle ABC)}$."
)
q45_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Total base $BC = BD + DC = 3 + 9 = 12\text{ cm}$." "\n"
    r"2. Triangles $\triangle ABD$ and $\triangle ABC$ share vertex $A$ and have collinear bases on line $BC$, so heights are equal." "\n"
    r"3. $\frac{A(\triangle ABD)}{A(\triangle ABC)} = \frac{BD}{BC} = \frac{3}{12} = \frac{1}{4}$."
)
prac_data.append((q45_text, [r"\(1 : 4\)", r"\(1 : 3\)", r"\(3 : 4\)", r"\(1 : 2\)"], "A", "OSC", "easy", q45_exp))

# Q46 (OSC) - Median and Sub-triangle with SVG
q46_svg = svg_median_triangle(top='A', b_left='B', mid='D', b_right='C', title="Median Area Split")
q46_text = (
    f"{q46_svg}\n"
    r"In $\triangle ABC$, $AD$ is a median to side $BC$. "
    r"If the area of $\triangle ABD$ is $28\text{ cm}^2$, what is the total area of $\triangle ABC$?"
)
q46_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since $AD$ is a median, it bisects the area of $\triangle ABC$ into two equal halves:" "\n"
    r"\[ A(\triangle ABD) = A(\triangle ADC) = \frac{1}{2} A(\triangle ABC) \]" "\n"
    r"2. Total area: $A(\triangle ABC) = 2 \times A(\triangle ABD) = 2 \times 28 = 56\text{ cm}^2$."
)
prac_data.append((q46_text, [r"\(56\text{ cm}^2\)", r"\(42\text{ cm}^2\)", r"\(84\text{ cm}^2\)", r"\(28\text{ cm}^2\)"], "A", "OSC", "easy", q46_exp))

# Q47 (OSC) - Practice Set 1.1 Q5 variation with SVG
q47_svg = svg_practice_set_1_1_q5()
q47_text = (
    f"{q47_svg}\n"
    r"In the adjoining figure, $PQ \perp BC$ and $AD \perp BC$. "
    r"If $PQ = 4$ and $AD = 10$, find the ratio $\frac{A(\triangle PBC)}{A(\triangle ABC)}$."
)
q47_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Both triangles $\triangle PBC$ and $\triangle ABC$ have the common base $BC$." "\n"
    r"2. $\frac{A(\triangle PBC)}{A(\triangle ABC)} = \frac{PQ}{AD} = \frac{4}{10} = \frac{2}{5}$."
)
prac_data.append((q47_text, [r"\(2 : 5\)", r"\(1 : 2\)", r"\(4 : 5\)", r"\(2 : 3\)"], "A", "OSC", "easy", q47_exp))

# Q48 (OSC) - Trapezium with Diagonals with SVG
q48_svg = svg_trapezium_diagonals(title="Trapezium Diagonals Area")
q48_text = (
    f"{q48_svg}\n"
    r"In trapezium $ABCD$, $AB \parallel CD$, and diagonals intersect at $P$. "
    r"If the area of $\triangle APD$ is $18\text{ cm}^2$, what is the area of $\triangle BPC$?"
)
q48_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. As proven from $A(\triangle ADC) = A(\triangle BDC)$ (triangles on common base $DC$ between parallel lines $AB \parallel DC$):" "\n"
    r"\[ A(\triangle ADC) - A(\triangle DPC) = A(\triangle BDC) - A(\triangle DPC) \]" "\n"
    r"\[ A(\triangle APD) = A(\triangle BPC) \]" "\n"
    r"2. Given $A(\triangle APD) = 18\text{ cm}^2$, it directly follows that $A(\triangle BPC) = 18\text{ cm}^2$."
)
prac_data.append((q48_text, [r"\(18\text{ cm}^2\)", r"\(36\text{ cm}^2\)", r"\(9\text{ cm}^2\)", r"\(24\text{ cm}^2\)"], "A", "OSC", "medium", q48_exp))

# Q49 (OSC) - Three Collinear Segments with SVG
q49_svg = svg_collinear_three_segments(top='A', b_left='B', d='D', e='E', b_right='C', len_bd='3', len_de='5', len_ec='7', title="Collinear Bases 3:5:7")
q49_text = (
    f"{q49_svg}\n"
    r"In $\triangle ABC$, points $D$ and $E$ lie on $BC$ such that $BD : DE : EC = 3 : 5 : 7$. "
    r"If $A(\triangle ADE) = 25\text{ cm}^2$, find the area of $\triangle AEC$."
)
q49_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since $\triangle ADE$ and $\triangle AEC$ have common vertex $A$ and collinear bases, heights are equal." "\n"
    r"2. $\frac{A(\triangle ADE)}{A(\triangle AEC)} = \frac{DE}{EC} = \frac{5}{7}$." "\n"
    r"3. $\frac{25}{A(\triangle AEC)} = \frac{5}{7} \implies A(\triangle AEC) = \frac{25 \times 7}{5} = 35\text{ cm}^2$."
)
prac_data.append((q49_text, [r"\(35\text{ cm}^2\)", r"\(49\text{ cm}^2\)", r"\(30\text{ cm}^2\)", r"\(42\text{ cm}^2\)"], "A", "OSC", "medium", q49_exp))

# Q50 (OSC) - Quadrilateral Common Diagonal with SVG
q50_svg = svg_quadrilateral_common_diagonal(top='B', bot='D', left='A', right='C', h_top='5', h_bot='7', title="Quadrilateral Area Ratio")
q50_text = (
    f"{q50_svg}\n"
    r"In quadrilateral $ABCD$, diagonal $AC$ is a common base for $\triangle ABC$ and $\triangle ADC$. "
    r"The perpendicular from $B$ to $AC$ is $5\text{ cm}$ and from $D$ to $AC$ is $7\text{ cm}$. "
    r"Find $\frac{A(\triangle ABC)}{A(\triangle ADC)}$."
)
q50_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since base $AC$ is common to both triangles:" "\n"
    r"\[ \frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{h_1}{h_2} = \frac{5}{7} \]" "\n"
    r"Thus, the ratio is $5 : 7$."
)
prac_data.append((q50_text, [r"\(5 : 7\)", r"\(7 : 5\)", r"\(25 : 49\)", r"\(5 : 12\)"], "A", "OSC", "easy", q50_exp))

# Q51 (OSC) - Two triangles ratio
q51_text = (
    r"The bases of two triangles are $8\text{ cm}$ and $10\text{ cm}$ respectively. Their corresponding heights are $15\text{ cm}$ and $12\text{ cm}$. "
    r"Find the ratio of their areas."
)
q51_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2} = \frac{8 \times 15}{10 \times 12} = \frac{120}{120} = 1$." "\n"
    r"Thus, the ratio is $1 : 1$."
)
prac_data.append((q51_text, [r"\(1 : 1\)", r"\(2 : 3\)", r"\(4 : 5\)", r"\(5 : 4\)"], "A", "OSC", "easy", q51_exp))

# Q52 (OSC) - Base ratio given area and height ratio
q52_text = (
    r"The ratio of the areas of two triangles is $5 : 6$ and the ratio of their heights is $2 : 3$. "
    r"What is the ratio of their bases?"
)
q52_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $\frac{A_1}{A_2} = \left(\frac{b_1}{b_2}\right) \times \left(\frac{h_1}{h_2}\right)$." "\n"
    r"2. $\frac{5}{6} = \left(\frac{b_1}{b_2}\right) \times \frac{2}{3} \implies \frac{b_1}{b_2} = \frac{5}{6} \times \frac{3}{2} = \frac{15}{12} = \frac{5}{4}$." "\n"
    r"Therefore, the ratio of bases is $5 : 4$."
)
prac_data.append((q52_text, [r"\(5 : 4\)", r"\(4 : 5\)", r"\(5 : 9\)", r"\(3 : 5\)"], "A", "OSC", "medium", q52_exp))

# Q53 (OSC) - Ratio of areas with collinear midpoints
q53_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='x', len_dc='2x', show_alt=False, title="Collinear Base 1:2 Ratio")
q53_text = (
    f"{q53_svg}\n"
    r"In $\triangle ABC$, $D$ is a point on $BC$ such that $DC = 2 BD$. "
    r"What fraction of the area of $\triangle ABC$ is the area of $\triangle ADC$?"
)
q53_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $BC = BD + DC = BD + 2 BD = 3 BD$." "\n"
    r"2. Triangles $\triangle ADC$ and $\triangle ABC$ have equal heights." "\n"
    r"3. $\frac{A(\triangle ADC)}{A(\triangle ABC)} = \frac{DC}{BC} = \frac{2 BD}{3 BD} = \frac{2}{3}$." "\n"
    r"Thus, the area is $\frac{2}{3}$ of the total area."
)
prac_data.append((q53_text, [r"\(\frac{2}{3}\)", r"\(\frac{1}{3}\)", r"\(\frac{1}{2}\)", r"\(\frac{3}{4}\)"], "A", "OSC", "easy", q53_exp))

# Q54 (OSC) - Height ratio given area and base ratio
q54_text = (
    r"Two triangles have areas in the ratio $3 : 2$. If their bases are in the ratio $9 : 8$, "
    r"find the ratio of their heights."
)
q54_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2} \implies \frac{3}{2} = \frac{9}{8} \times \frac{h_1}{h_2}$." "\n"
    r"2. $\frac{h_1}{h_2} = \frac{3}{2} \times \frac{8}{9} = \frac{24}{18} = \frac{4}{3}$." "\n"
    r"Thus, the ratio of heights is $4 : 3$."
)
prac_data.append((q54_text, [r"\(4 : 3\)", r"\(3 : 4\)", r"\(2 : 3\)", r"\(16 : 27\)"], "A", "OSC", "medium", q54_exp))

# Q55 (OSC) - Collinear points 3 parts with SVG
q55_svg = svg_collinear_three_segments(top='P', b_left='Q', d='X', e='Y', b_right='R', len_bd='1', len_de='2', len_ec='3', title="Cevians Ratio 1:2:3")
q55_text = (
    f"{q55_svg}\n"
    r"In $\triangle PQR$, points $X, Y$ lie on $QR$ such that $QX : XY : YR = 1 : 2 : 3$. "
    r"Find the ratio $\frac{A(\triangle PXY)}{A(\triangle PQR)}$."
)
q55_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Total base $QR = 1 + 2 + 3 = 6$ units." "\n"
    r"2. Since $\triangle PXY$ and $\triangle PQR$ share vertex $P$ and collinear bases, heights are equal." "\n"
    r"3. $\frac{A(\triangle PXY)}{A(\triangle PQR)} = \frac{XY}{QR} = \frac{2}{6} = \frac{1}{3}$."
)
prac_data.append((q55_text, [r"\(\frac{1}{3}\)", r"\(\frac{1}{6}\)", r"\(\frac{1}{2}\)", r"\(\frac{2}{5}\)"], "A", "OSC", "medium", q55_exp))

# Q56 (OSC) - Equal heights word problem
q56_text = (
    r"Two triangles on the same base line have a common vertex. The base of the first triangle is $14\text{ cm}$ and that of the second is $21\text{ cm}$. "
    r"If the area of the second triangle is $63\text{ cm}^2$, find the area of the first triangle."
)
q56_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since they share a common vertex and have bases on the same line, their heights are equal." "\n"
    r"2. $\frac{A_1}{A_2} = \frac{b_1}{b_2} \implies \frac{A_1}{63} = \frac{14}{21} = \frac{2}{3}$." "\n"
    r"3. $A_1 = \frac{63 \times 2}{3} = 21 \times 2 = 42\text{ cm}^2$."
)
prac_data.append((q56_text, [r"\(42\text{ cm}^2\)", r"\(36\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(54\text{ cm}^2\)"], "A", "OSC", "easy", q56_exp))

# Q57 (OMC) - Multi-select on Practice Set 1.1 Q2 with SVG
q57_svg = svg_practice_set_1_1_q2(bc_val='BC', ad_val='AD', title="Common Base AB Geometry")
q57_text = (
    f"{q57_svg}\n"
    r"In the figure, $BC \perp AB$ and $AD \perp AB$. Which of the following statements are **TRUE**? (Select all that apply)"
)
q57_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"- A: Both triangles $\triangle ABC$ and $\triangle ADB$ share common base $AB$. $\rightarrow$ **TRUE**." "\n"
    r"- B: Since base $AB$ is common, $\frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD}$. $\rightarrow$ **TRUE**." "\n"
    r"- C: Line segments $AD$ and $BC$ are parallel (both perpendicular to line $AB$). $\rightarrow$ **TRUE**." "\n"
    r"- D: $\triangle ABC \cong \triangle ADB$ necessarily. $\rightarrow$ **FALSE** (their heights $BC$ and $AD$ can be different)." "\n"
    r"Thus, A, B, and C are correct."
)
prac_data.append((q57_text, [
    r"Both \(\triangle ABC\) and \(\triangle ADB\) share the common base \(AB\)",
    r"\(\frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD}\)",
    r"Segments \(AD\) and \(BC\) are parallel because both are perpendicular to the same line \(AB\)",
    r"\(\triangle ABC\) and \(\triangle ADB\) are always congruent"
], ["A", "B", "C"], "OMC", "medium", q57_exp))

# Q58 (OMC) - Multi-select on Practice Set 1.1 Q5 with SVG
q58_svg = svg_practice_set_1_1_q5()
q58_text = (
    f"{q58_svg}\n"
    r"In the figure, $PQ \perp BC$ and $AD \perp BC$. Which of the following ratios are **CORRECTLY PAIRED** with their reason? (Select all that apply)"
)
q58_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"- A: $\frac{A(\triangle PQB)}{A(\triangle PBC)} = \frac{BQ}{BC}$ (Reason: Common height $PQ$). $\rightarrow$ **TRUE**." "\n"
    r"- B: $\frac{A(\triangle PBC)}{A(\triangle ABC)} = \frac{PQ}{AD}$ (Reason: Common base $BC$). $\rightarrow$ **TRUE**." "\n"
    r"- C: $\frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{BC}{CD}$ (Reason: Common height $AD$). $\rightarrow$ **TRUE**." "\n"
    r"All three statements correctly pair the ratio with the geometrical property from Balbharti textbook Practice Set 1.1 Q5."
)
prac_data.append((q58_text, [
    r"\(\frac{A(\triangle PQB)}{A(\triangle PBC)} = \frac{BQ}{BC}\) (Triangles with common height \(PQ\))",
    r"\(\frac{A(\triangle PBC)}{A(\triangle ABC)} = \frac{PQ}{AD}\) (Triangles with common base \(BC\))",
    r"\(\frac{A(\triangle ABC)}{A(\triangle ADC)} = \frac{BC}{CD}\) (Triangles with common height \(AD\))",
    r"\(\frac{A(\triangle ADC)}{A(\triangle PQC)} = 1\) (Triangles with equal areas)"
], ["A", "B", "C"], "OMC", "medium", q58_exp))

# Q59 (OMC) - Medians in a Triangle
q59_text = (
    r"In any triangle $\triangle ABC$, if all three medians $AD, BE, CF$ intersect at the centroid $G$, which of the following statements about areas are **TRUE**? (Select all that apply)"
)
q59_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. The three medians of a triangle divide it into 6 smaller triangles of equal area: $A(\triangle GBD) = A(\triangle GCD) = A(\triangle GCE) = A(\triangle GAE) = A(\triangle GAF) = A(\triangle GBF) = \frac{1}{6} A(\triangle ABC)$." "\n"
    r"2. The centroid divides each median in the ratio $2 : 1$." "\n"
    r"3. The three triangles formed by connecting the centroid to the three vertices have equal areas: $A(\triangle GAB) = A(\triangle GBC) = A(\triangle GCA) = \frac{1}{3} A(\triangle ABC)$." "\n"
    r"Thus, options A, B, and C are true."
)
prac_data.append((q59_text, [
    r"The three medians divide the triangle into 6 smaller triangles of equal area",
    r"\(A(\triangle GAB) = A(\triangle GBC) = A(\triangle GCA) = \frac{1}{3} A(\triangle ABC)\)",
    r"Each median bisects the total area of the triangle into two equal halves",
    r"All 6 smaller triangles are congruent to each other"
], ["A", "B", "C"], "OMC", "hard", q59_exp))

# Q60 (OMC) - Parallel lines multi-select
q60_text = (
    r"If two lines $l_1$ and $l_2$ are parallel, which of the following statements must hold? (Select all that apply)"
)
q60_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"- A: The perpendicular distance between $l_1$ and $l_2$ is constant at every point. $\rightarrow$ **TRUE**." "\n"
    r"- B: Triangles on the same base lying between $l_1$ and $l_2$ have equal areas. $\rightarrow$ **TRUE**." "\n"
    r"- C: Triangles on equal bases lying between $l_1$ and $l_2$ have equal areas. $\rightarrow$ **TRUE**." "\n"
    r"- D: All triangles between $l_1$ and $l_2$ are congruent. $\rightarrow$ **FALSE**." "\n"
    r"Thus, A, B, and C are true."
)
prac_data.append((q60_text, [
    "Perpendicular distance between the two lines is constant throughout",
    "Triangles having the same base and situated between the lines have equal areas",
    "Triangles having equal bases and situated between the lines have equal areas",
    "All triangles situated between the lines are congruent"
], ["A", "B", "C"], "OMC", "easy", q60_exp))

# Q61 (OTF) - Ratio of areas when h is constant
q61_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'If the heights of two triangles are equal, their areas are directly proportional to their corresponding bases.'**"
)
q61_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. When $h_1 = h_2$, $\frac{A_1}{A_2} = \frac{b_1 \times h}{b_2 \times h} = \frac{b_1}{b_2}$." "\n"
    r"2. This directly establishes that area is directly proportional to base." "\n"
    r"Hence, the statement is **True**."
)
prac_data.append((q61_text, ["True", "False"], "A", "OTF", "easy", q61_exp))

# Q62 (OTF) - Collinear points common height
q62_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'Two triangles having a common vertex and collinear bases have equal heights.'**"
)
q62_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. A perpendicular dropped from the common vertex to the common line containing the bases represents the unique altitude for both triangles." "\n"
    r"2. Therefore, both triangles share the exact same height." "\n"
    r"Hence, the statement is **True**."
)
prac_data.append((q62_text, ["True", "False"], "A", "OTF", "easy", q62_exp))

# Q63 (OTF) - Inverse proportionality false
q63_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'For triangles with equal bases, their areas are inversely proportional to their heights.'**"
)
q63_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. For equal bases ($b_1 = b_2$), $\frac{A_1}{A_2} = \frac{h_1}{h_2}$." "\n"
    r"2. This is **direct proportionality** ($\text{Area} \propto \text{height}$), NOT inverse proportionality." "\n"
    r"Therefore, the statement is **False**."
)
prac_data.append((q63_text, ["True", "False"], "B", "OTF", "easy", q63_exp))

# Q64 (OAR) - Trapezium Diagonals Assertion Reason with SVG
q64_svg = svg_trapezium_diagonals(title="Trapezium Non-Parallel Triangles")
q64_assertion = r"In trapezium $ABCD$ with $AB \parallel CD$ and diagonals intersecting at $P$, $A(\triangle APD) = A(\triangle BPC)$."
q64_reason = r"Subtracting the area of the common sub-triangle $\triangle DPC$ from the equal areas $A(\triangle ADC) = A(\triangle BDC)$ leaves $A(\triangle APD) = A(\triangle BPC)$."
q64_text = f"{q64_svg}\nAssertion (A): {q64_assertion}\nReason (R): {q64_reason}"
q64_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Both $\triangle ADC$ and $\triangle BDC$ have common base $CD$ and equal heights (lying between parallel lines $AB \parallel CD$). Hence $A(\triangle ADC) = A(\triangle BDC)$." "\n"
    r"2. Subtracting $A(\triangle DPC)$ from both sides gives $A(\triangle APD) = A(\triangle BPC)$." "\n"
    r"3. Both Assertion and Reason are true, and Reason is the correct explanation of Assertion (Option A)."
)
prac_data.append((q64_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "medium", q64_exp, q64_assertion, q64_reason, q64_svg))

# Q65 (OAR) - Ratio of Areas Equal Heights
q65_assertion = r"In $\triangle ABC$, if $D$ is a point on $BC$ such that $BD : DC = 1 : 4$, then $A(\triangle ABD) = \frac{1}{5} A(\triangle ABC)$."
q65_reason = r"The total base is $BC = BD + DC = 1 + 4 = 5$ parts, and triangles having equal heights have areas proportional to their bases."
q65_text = f"Assertion (A): {q65_assertion}\nReason (R): {q65_reason}"
q65_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $\triangle ABD$ and $\triangle ABC$ share vertex $A$ and collinear bases on line $BC$. Hence, they have equal heights." "\n"
    r"2. Ratio: $\frac{A(\triangle ABD)}{A(\triangle ABC)} = \frac{BD}{BC} = \frac{1}{1 + 4} = \frac{1}{5}$." "\n"
    r"3. Therefore, Assertion is true and Reason correctly explains Assertion."
)
prac_data.append((q65_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "easy", q65_exp, q65_assertion, q65_reason, None))

# Q66 (OAR) - Practice Set 1.1 Q3 Assertion Reason with SVG
q66_svg = svg_practice_set_1_1_q3(rq_val='6', ps_val='6', pr_val='12', qt_label='QT = 3', title="Two Altitudes in a Triangle")
q66_assertion = r"In $\triangle PQR$, if $RQ = 6, PS = 6$ (with $PS \perp \text{ray } RQ$) and $PR = 12, QT \perp PR$, then $QT = 3$."
q66_reason = r"The area of a triangle remains constant regardless of which side is chosen as the base and its corresponding altitude."
q66_text = f"{q66_svg}\nAssertion (A): {q66_assertion}\nReason (R): {q66_reason}"
q66_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Area of $\triangle PQR = \frac{1}{2} \times 6 \times 6 = 18$." "\n"
    r"2. Using base $PR$: $\frac{1}{2} \times 12 \times QT = 18 \implies 6 QT = 18 \implies QT = 3$." "\n"
    r"3. This is true precisely because the area of a triangle is unique and does not depend on the choice of base and corresponding altitude. Reason (R) correctly explains Assertion (A)."
)
prac_data.append((q66_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "medium", q66_exp, q66_assertion, q66_reason, q66_svg))

# Q67 (ONE) - Practice Set 1.1 Q2 Numeric with SVG
q67_svg = svg_practice_set_1_1_q2(bc_val='5', ad_val='10', title="Numeric Ratio Practice")
q67_text = (
    f"{q67_svg}\n"
    r"In the figure, $BC \perp AB$, $AD \perp AB$. If $BC = 5$ and $AD = 10$, "
    r"calculate the decimal value of $\frac{A(\triangle ABC)}{A(\triangle ADB)}$."
)
q67_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Common base $AB \implies \frac{A(\triangle ABC)}{A(\triangle ADB)} = \frac{BC}{AD}$." "\n"
    r"2. $\frac{5}{10} = 0.5$." "\n"
    r"Thus, the answer is $0.5$."
)
prac_data.append((q67_text, [], "0.5", "ONE", "easy", q67_exp))

# Q68 (ONE) - Practice Set 1.1 Q3 Numeric with SVG
q68_svg = svg_practice_set_1_1_q3(rq_val='8', ps_val='6', pr_val='16', qt_label='QT = ?', title="Find Altitude QT")
q68_text = (
    f"{q68_svg}\n"
    r"In $\triangle PQR$, $PS \perp \text{ray } RQ$ with $PS = 6$, and $QT \perp PR$ with $PR = 16$. "
    r"If $RQ = 8$, find the value of $QT$."
)
q68_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Area $= \frac{1}{2} \times 8 \times 6 = 24$." "\n"
    r"2. Area $= \frac{1}{2} \times 16 \times QT = 8 \times QT$." "\n"
    r"3. $8 \times QT = 24 \implies QT = 3$."
)
prac_data.append((q68_text, [], "3", "ONE", "medium", q68_exp))

# Q69 (ONE) - Collinear Base Missing Area with SVG
q69_svg = svg_collinear_base(top='A', b_left='B', b_mid='D', b_right='C', len_bd='4', len_dc='7', show_alt=False, title="Collinear Area Calculation")
q69_text = (
    f"{q69_svg}\n"
    r"In $\triangle ABC$, point $D$ lies on side $BC$ such that $BD : DC = 4 : 7$. "
    r"If the area of $\triangle ABD$ is $24\text{ cm}^2$, find the area of $\triangle ADC$ in $\text{cm}^2$."
)
q69_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Triangles have equal heights $\implies \frac{A(\triangle ABD)}{A(\triangle ADC)} = \frac{BD}{DC}$." "\n"
    r"2. $\frac{24}{A(\triangle ADC)} = \frac{4}{7} \implies A(\triangle ADC) = \frac{24 \times 7}{4} = 6 \times 7 = 42\text{ cm}^2$."
)
prac_data.append((q69_text, [], "42", "ONE", "medium", q69_exp))

# Q70 (ONE) - Median Split Area with SVG
q70_svg = svg_median_triangle(top='A', b_left='B', mid='D', b_right='C', title="Median Half Area")
q70_text = (
    f"{q70_svg}\n"
    r"In $\triangle ABC$, $AD$ is a median to $BC$. "
    r"If the area of $\triangle ABC$ is $96\text{ cm}^2$, find the area of $\triangle ADC$ in $\text{cm}^2$."
)
q70_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Median divides triangle into two equal areas:" "\n"
    r"\[ A(\triangle ADC) = \frac{1}{2} \times A(\triangle ABC) = \frac{96}{2} = 48\text{ cm}^2 \]"
)
prac_data.append((q70_text, [], "48", "ONE", "easy", q70_exp))

print(f"Loaded {len(prac_data)} Practice questions.")

# =========================================================================
# MOCK / FOUNDATION POOL (12 Questions: 071 - 082)
# =========================================================================
mock_data = []

# Q71 (OSC) - Foundation: Core Formula of Triangle Area with SVG
q71_svg = wrap_svg("""  <!-- Foundation Triangle -->
  <polygon points="180,45 60,165 300,165" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="180" y1="45" x2="180" y2="165" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
  <polyline points="180,153 192,153 192,165" fill="none" stroke="#f43f5e" stroke-width="1.3"/>
  <circle cx="180" cy="45" r="3.5" fill="#f8fafc"/>
  <circle cx="60" cy="165" r="3.5" fill="#f8fafc"/>
  <circle cx="300" cy="165" r="3.5" fill="#f8fafc"/>
  <text x="180" y="34" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif" text-anchor="middle">A</text>
  <text x="45" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">B</text>
  <text x="312" y="172" fill="#f8fafc" font-size="13" font-weight="bold" font-family="sans-serif">C</text>
  <text x="195" y="105" fill="#f43f5e" font-size="12" font-weight="bold" font-family="sans-serif">h</text>
  <text x="180" y="186" fill="#38bdf8" font-size="12" font-weight="bold" font-family="sans-serif" text-anchor="middle">Base (b)</text>""", 360, 205)
q71_text = (
    f"{q71_svg}\n"
    r"What is the fundamental formula for the area of a triangle having base $b$ and corresponding height $h$?"
)
q71_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"The area of any triangle is given by half the product of its base and its corresponding perpendicular height:" "\n"
    r"\[ \text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times b \times h \]"
)
mock_data.append((q71_text, [r"\(\frac{1}{2} \times \text{base} \times \text{height}\)", r"\(\text{base} \times \text{height}\)", r"\(\frac{1}{2} \times (\text{base} + \text{height})\)", r"\(\frac{1}{3} \times \text{base} \times \text{height}\)"], "A", "OSC", "easy", q71_exp))

# Q72 (OSC) - Foundation: Ratio of areas general formula
q72_text = (
    r"If two triangles $\triangle_1$ and $\triangle_2$ have bases $b_1, b_2$ and corresponding heights $h_1, h_2$, "
    r"what is the ratio of their areas $\frac{A_1}{A_2}$?"
)
q72_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. $A_1 = \frac{1}{2} b_1 h_1$ and $A_2 = \frac{1}{2} b_2 h_2$." "\n"
    r"2. Dividing $A_1$ by $A_2$:" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{\frac{1}{2} b_1 h_1}{\frac{1}{2} b_2 h_2} = \frac{b_1 \times h_1}{b_2 \times h_2} \]" "\n"
    r"Hence, the ratio is $\frac{b_1 \times h_1}{b_2 \times h_2}$."
)
mock_data.append((q72_text, [r"\(\frac{b_1 \times h_1}{b_2 \times h_2}\)", r"\(\frac{b_1 + h_1}{b_2 + h_2}\)", r"\(\frac{b_1^2}{b_2^2}\)", r"\(\frac{h_1}{h_2}\)"], "A", "OSC", "easy", q72_exp))

# Q73 (OSC) - Foundation: Triangles with equal heights
q73_text = (
    r"If two triangles have **EQUAL HEIGHTS** ($h_1 = h_2$), their areas are proportional to:"
)
q73_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"When heights are equal ($h_1 = h_2 = h$):" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{b_1 \times h}{b_2 \times h} = \frac{b_1}{b_2} \]" "\n"
    r"Thus, their areas are directly proportional to their corresponding bases."
)
mock_data.append((q73_text, ["Their corresponding bases", "Their perimeters", "The squares of their bases", "Their corresponding angles"], "A", "OSC", "easy", q73_exp))

# Q74 (OSC) - Foundation: Triangles with equal bases
q74_text = (
    r"If two triangles have **EQUAL BASES** ($b_1 = b_2$), their areas are proportional to:"
)
q74_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"When bases are equal ($b_1 = b_2 = b$):" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{b \times h_1}{b \times h_2} = \frac{h_1}{h_2} \]" "\n"
    r"Thus, their areas are directly proportional to their corresponding heights."
)
mock_data.append((q74_text, ["Their corresponding heights", "Their corresponding bases", "The squares of their heights", "Their medians"], "A", "OSC", "easy", q74_exp))

# Q75 (OSC) - Foundation: Triangles with equal bases and equal heights with SVG
q75_svg = svg_parallel_lines_triangles(top_l='A', top_r='D', bot_l='B', bot_r='C', title="Equal Bases and Equal Heights")
q75_text = (
    f"{q75_svg}\n"
    r"If two triangles have both **EQUAL BASES** and **EQUAL HEIGHTS**, what is the ratio of their areas?"
)
q75_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"When $b_1 = b_2 = b$ and $h_1 = h_2 = h$:" "\n"
    r"\[ \frac{A_1}{A_2} = \frac{b \times h}{b \times h} = 1 \implies A_1 = A_2 \]" "\n"
    r"Thus, the ratio of their areas is $1 : 1$."
)
mock_data.append((q75_text, [r"\(1 : 1\)", r"\(1 : 2\)", r"\(2 : 1\)", r"\(0\)"], "A", "OSC", "easy", q75_exp))

# Q76 (OSC) - Foundation: Median of a triangle with SVG
q76_svg = svg_median_triangle(top='A', b_left='B', mid='D', b_right='C', title="Foundation - Median Concept")
q76_text = (
    f"{q76_svg}\n"
    r"A line segment connecting a vertex of a triangle to the midpoint of the opposite side is called a:"
)
q76_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"By geometric definition, a line segment drawn from any vertex of a triangle to the midpoint of the opposite side is called a **median**."
)
mock_data.append((q76_text, ["Median", "Altitude", "Angle Bisector", "Perpendicular Bisector"], "A", "OSC", "easy", q76_exp))

# Q77 (OTF) - Foundation: True/False on common vertex collinear base
q77_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'Triangles having a common vertex and their bases lying along the same straight line always have equal heights.'**"
)
q77_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"The height of both triangles is the perpendicular distance from the single common vertex to the straight line containing their bases. Since there is only one such perpendicular distance, their heights are equal." "\n"
    r"Hence, the statement is **True**."
)
mock_data.append((q77_text, ["True", "False"], "A", "OTF", "easy", q77_exp))

# Q78 (OTF) - Foundation: True/False on distance between parallel lines
q78_text = (
    r"State whether the following statement is True or False:" "\n\n"
    r"**'The perpendicular distance between two parallel lines remains constant throughout.'**"
)
q78_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"By definition of parallel lines, they never intersect and the perpendicular distance between them is constant at all points." "\n"
    r"Hence, the statement is **True**."
)
mock_data.append((q78_text, ["True", "False"], "A", "OTF", "easy", q78_exp))

# Q79 (OFB) - Foundation Fill in the blanks: Base property
q79_text = (
    r"Complete the theorem statement:" "\n\n"
    r"The ratio of the areas of two triangles with equal heights is equal to the ratio of their corresponding ________."
)
q79_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"Theorem: Ratio of areas of two triangles with equal heights is equal to the ratio of their corresponding **bases** ($\frac{A_1}{A_2} = \frac{b_1}{b_2}$)."
)
mock_data.append((q79_text, ["bases", "heights", "perimeters", "hypotenuses"], "A", "OFB", "easy", q79_exp))

# Q80 (OFB) - Foundation Fill in the blanks: Height property
q80_text = (
    r"Complete the theorem statement:" "\n\n"
    r"The ratio of the areas of two triangles with equal bases is equal to the ratio of their corresponding ________."
)
q80_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"Theorem: Ratio of areas of two triangles with equal bases is equal to the ratio of their corresponding **heights** ($\frac{A_1}{A_2} = \frac{h_1}{h_2}$)."
)
mock_data.append((q80_text, ["heights", "bases", "angles", "medians"], "A", "OFB", "easy", q80_exp))

# Q81 (OAR) - Foundation Assertion Reason
q81_assertion = r"The ratio of the areas of two triangles is equal to the ratio of the products of their bases and corresponding heights."
q81_reason = r"The area of a triangle is calculated as $\frac{1}{2} \times \text{base} \times \text{height}$, and the factor of $\frac{1}{2}$ cancels out when taking the ratio."
q81_text = f"Assertion (A): {q81_assertion}\nReason (R): {q81_reason}"
q81_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. **Assertion (A):** This is the fundamental property of Topic 1.1: $\frac{A_1}{A_2} = \frac{b_1 \times h_1}{b_2 \times h_2}$. (True)" "\n"
    r"2. **Reason (R):** $\frac{\frac{1}{2} b_1 h_1}{\frac{1}{2} b_2 h_2} = \frac{b_1 h_1}{b_2 h_2}$ because $\frac{1}{2}$ in numerator and denominator cancels out. (True)" "\n"
    r"3. Reason (R) is the exact mathematical proof and justification of Assertion (A)."
)
mock_data.append((q81_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "easy", q81_exp, q81_assertion, q81_reason, None))

# Q82 (OAR) - Foundation Assertion Reason on Median
q82_svg = svg_median_triangle(top='X', b_left='Y', mid='M', b_right='Z', title="Median of a Triangle")
q82_assertion = r"If segment $XM$ is a median of $\triangle XYZ$, then $A(\triangle XYM) = \frac{1}{2} A(\triangle XYZ)$."
q82_reason = r"A median divides the opposite side into two equal segments, creating two triangles that share the same vertex and have equal collinear bases."
q82_text = f"{q82_svg}\nAssertion (A): {q82_assertion}\nReason (R): {q82_reason}"
q82_exp = (
    r"**Step-by-step Solution:**" "\n\n"
    r"1. Since $XM$ is a median, $YM = MZ$." "\n"
    r"2. $\triangle XYM$ and $\triangle XZM$ have equal heights (common vertex $X$, collinear bases on $YZ$)." "\n"
    r"3. Therefore, $A(\triangle XYM) = A(\triangle XZM) = \frac{1}{2} A(\triangle XYZ)$." "\n"
    r"Both Assertion and Reason are true, and Reason is the correct explanation of Assertion (Option A)."
)
mock_data.append((q82_text, [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
], "A", "OAR", "easy", q82_exp, q82_assertion, q82_reason, q82_svg))

print(f"Loaded {len(mock_data)} Mock/Foundation questions.")

# =========================================================================
# ASSEMBLE ALL 82 QUESTIONS
# =========================================================================
all_questions = []

# 40 Exam (001 - 040)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qtype = item[3]
    qcode = f"{TOPIC_CODE}-{qtype}-{qnum:03d}"
    assertion = item[6] if len(item) > 6 else None
    reason = item[7] if len(item) > 7 else None
    diagram = item[8] if len(item) > 8 else None
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], qtype, item[4], "exam", "standard", item[5], assertion, reason, diagram))

# 30 Practice (041 - 070)
for idx, item in enumerate(prac_data):
    qnum = idx + 41
    qtype = item[3]
    qcode = f"{TOPIC_CODE}-{qtype}-{qnum:03d}"
    assertion = item[6] if len(item) > 6 else None
    reason = item[7] if len(item) > 7 else None
    diagram = item[8] if len(item) > 8 else None
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], qtype, item[4], "practice", "standard", item[5], assertion, reason, diagram))

# 12 Mock/Foundation (071 - 082)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qtype = item[3]
    qcode = f"{TOPIC_CODE}-{qtype}-{qnum:03d}"
    assertion = item[6] if len(item) > 6 else None
    reason = item[7] if len(item) > 7 else None
    diagram = item[8] if len(item) > 8 else None
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], qtype, item[4], "mock", "foundation", item[5], assertion, reason, diagram))

print(f"\nTotal canonical questions assembled: {len(all_questions)}")
assert len(all_questions) == 82, f"Expected 82 questions, got {len(all_questions)}"

# Count how many have SVG figures
svg_count = sum(1 for q in all_questions if "<svg" in q["text"])
print(f"Questions containing geometric SVG figures: {svg_count} / {len(all_questions)} ({svg_count/len(all_questions)*100:.1f}%)")

out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mh10_mth2_ch1_t1.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote JSON to {out_file}")
