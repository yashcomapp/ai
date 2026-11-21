with open("scripts/build_clean_ch3_p1.py", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("\\text{ cm}", "\\text{{ cm}}")
c = c.replace("\\text{ sq cm}", "\\text{{ sq cm}}")

with open("scripts/build_clean_ch3_p1.py", "w", encoding="utf-8") as f:
    f.write(c)

print("Braces fixed successfully.")
