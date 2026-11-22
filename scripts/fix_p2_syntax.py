import re

with open("scripts/build_clean_mth1_ch1_part2.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_step_string = False
accumulated = []

for line in lines:
    stripped = line.strip()
    if not in_step_string:
        if 'f"**Step 1:' in line and not line.rstrip().endswith('."') and not line.rstrip().endswith(')"'):
            # start of multi-line f-string
            in_step_string = True
            indent = line[:line.find('f"')]
            content = line[line.find('f"')+2:]
            accumulated = [content.rstrip('\r\n')]
        else:
            new_lines.append(line)
    else:
        # check if this line ends the f-string (ends with ."\n or .)"\n or similar)
        if stripped.endswith('."') or stripped.endswith('."') or stripped.endswith(')"') or stripped.endswith('",') or stripped.endswith(')"'):
            accumulated.append(stripped[:-1]) # remove trailing quote
            trailing = stripped[-1] # the quote
            # combine with \\n
            combined_content = "\\n".join(accumulated)
            new_lines.append(f'{indent}f"{combined_content}"\n')
            in_step_string = False
            accumulated = []
        else:
            accumulated.append(stripped)

with open("scripts/build_clean_mth1_ch1_part2.py", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Processed lines:", len(new_lines))
