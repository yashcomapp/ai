with open("scripts/build_clean_ch1.py", "rb") as f:
    content = f.read()

# Replace broken string
bad = b'"Are rays O{1} and O{2} opposite rays if \\( ngle {1}O{2} = {0}^\\circ \r\ne 180^\\circ\\)?",'
bad_lf = b'"Are rays O{1} and O{2} opposite rays if \\( ngle {1}O{2} = {0}^\\circ \ne 180^\\circ\\)?",'
good = b'"Are rays O{1} and O{2} opposite rays if their angle is {0} degrees?",'

content = content.replace(bad, good).replace(bad_lf, good)
content = content.replace(b'\\( ngle', b'\\(\\angle')
content = content.replace(b'\\(ngle', b'\\(\\angle')

with open("scripts/build_clean_ch1.py", "wb") as f:
    f.write(content)

print("build_clean_ch1.py syntax fixed.")
