import re

with open('scripts/build_cbse9_scie_ch2_part3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# In f-strings, any double backslash followed by { or single { in math triggers python expression parsing.
# Notice lines like: f"**Step 1: ...\n...\n\n**Step 2: ... {item[0]} ...\n{item[1]}\n\n**Step 3: ...\n{item[2]}"
# Let's see what { ... } patterns appear in f-strings:
# {item[0]}, {item[1]}, {item[2]} are the ONLY intended python interpolations.
# Any other { ... } like \text{--}, \mu, \approx, etc. are LaTeX and should either have double braces {{ ... }} or not be in an f-string!

def repl_calc(match):
    calc_block = match.group(0)
    # let's look at the f-string inside
    # Find f"..."
    return calc_block

# Let's inspect where the syntax error occurred: line 125.
# Let's see lines 120-135 of build_cbse9_scie_ch2_part3.py
with open('scripts/build_cbse9_scie_ch2_part3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(120, 130):
    print(f"{i+1}: {repr(lines[i])}")
