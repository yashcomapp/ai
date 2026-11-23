with open('scripts/build_cbse9_scie_ch2_part3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip().startswith('f"**Step 1:'):
        # preserve indentation
        indent = line[:len(line) - len(line.lstrip())]
        content = line.strip()
        # strip leading f" and trailing " or "\n
        if content.startswith('f"') and content.endswith('"'):
            inner = content[2:-1]
            inner = inner.replace('{item[0]}', '__ITEM0__')
            inner = inner.replace('{item[1]}', '__ITEM1__')
            inner = inner.replace('{item[2]}', '__ITEM2__')
            inner = inner.replace('{', '{{').replace('}', '}}')
            inner = inner.replace('__ITEM0__', '{item[0]}')
            inner = inner.replace('__ITEM1__', '{item[1]}')
            inner = inner.replace('__ITEM2__', '{item[2]}')
            new_line = indent + 'f"' + inner + '"\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('scripts/build_cbse9_scie_ch2_part3.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated build_cbse9_scie_ch2_part3.py successfully!")
