import re

with open("scripts/build_clean_mth1_ch2_part1.py", "r", encoding="utf-8") as f:
    text = f.read()

# In tmpls, any { not followed by \d+} should be {{
# and any } not preceded by \d+ should be }}
# Let's find lines in tmpls lists
lines = text.split("\n")
in_tmpls = False
new_lines = []

for line in lines:
    if "'tmpls': [" in line:
        in_tmpls = True
        new_lines.append(line)
        continue
    if in_tmpls and "]" in line:
        in_tmpls = False
        new_lines.append(line)
        continue
        
    if in_tmpls:
        # replace any { not followed by digit with {{
        # but be careful if already {{
        # First normalize: {{ -> \x01, }} -> \x02
        temp = line.replace("{{", "\x01").replace("}}", "\x02")
        # replace {(\d+)} temporarily
        temp = re.sub(r'\{(\d+)\}', r'\x03\1\x04', temp)
        # Any remaining { or } are literal braces in LaTeX!
        temp = temp.replace("{", "{{").replace("}", "}}")
        # Restore placeholders
        temp = temp.replace("\x03", "{").replace("\x04", "}")
        temp = temp.replace("\x01", "{{").replace("\x02", "}}")
        new_lines.append(temp)
    else:
        new_lines.append(line)

with open("scripts/build_clean_mth1_ch2_part1.py", "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))

print("Fixed literal braces in tmpls lists")
