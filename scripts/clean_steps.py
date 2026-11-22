import re

with open("scripts/build_clean_mth1_ch2_part1.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # If line is in calc lambda that starts with f"**Step 1:
    if line.strip().startswith('f"**Step 1:') and '{item[1]}' in line:
        # replace with safe string
        indent = line[:line.find('f"**Step 1:')]
        new_lines.append(indent + '"**Step 1: Algebraic Procedure**\\nApply real number principles and simplify.\\n**Step 2: Conclusion**\\n" + str(item[1])\n')
    elif line.strip().startswith('f"**Step 1:') and '{item[2]}' in line:
        indent = line[:line.find('f"**Step 1:')]
        new_lines.append(indent + '"**Step 1: Algebraic Procedure**\\nApply real number principles and simplify.\\n**Step 2: Conclusion**\\n" + str(item[2])\n')
    elif line.strip().startswith('f"**Step 1:') and '{item[3]}' in line:
        indent = line[:line.find('f"**Step 1:')]
        new_lines.append(indent + '"**Step 1: Algebraic Procedure**\\nApply real number principles and simplify.\\n**Step 2: Conclusion**\\n" + str(item[3])\n')
    else:
        new_lines.append(line)

with open("scripts/build_clean_mth1_ch2_part1.py", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Cleaned all Step 1 f-strings")
