with open("scripts/build_clean_ch1.py", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print("Line 1112:", repr(lines[1111]))
print("Line 1113:", repr(lines[1112]))
print("Line 1114:", repr(lines[1113]))
print("Line 1115:", repr(lines[1114]))

# Replace line 1113 with a valid string
lines[1112] = '                "Are rays O{1} and O{2} opposite rays if their angle is {0} degrees?",\n'
if "e 180" in lines[1113]:
    lines.pop(1113)

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Fixed line 1113.")
