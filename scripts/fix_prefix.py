# scripts/fix_prefix.py
with open('scripts/generate_mh9_mth2_ch8_all.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace any broken f"{svg}\n"
c = c.replace('prefix = f"{svg}\n" if svg else ""', 'prefix = (svg + "\\n") if svg else ""')
c = c.replace('prefix = f"{svg}\\n" if svg else ""', 'prefix = (svg + "\\n") if svg else ""')
# Also handle case where there is literal newline between f"{svg} and " if svg else ""
c = c.replace('prefix = f"{svg}\n" if svg else ""', 'prefix = (svg + "\\n") if svg else ""')
import re
c = re.sub(r'prefix = f"\{svg\}\s*" if svg else ""', 'prefix = (svg + "\\\\n") if svg else ""', c)

with open('scripts/generate_mh9_mth2_ch8_all.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed!')
