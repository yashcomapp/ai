for fpath in ['scripts/build_cbse9_scie_ch2_part2.py', 'scripts/build_cbse9_scie_ch2_part3.py']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace single backslash in \mu with double backslash
    # Note: if it's \\mu, don't duplicate
    import re
    # Fix \mu to \\mu where it's not already \\mu
    # In raw file text, \mu is often just \mu if not raw string
    content = content.replace(r'\mu', r'\\mu')
    content = content.replace(r'\\\\mu', r'\\mu') # avoid double-replacing
    content = content.replace(r'\psi', r'\\psi')
    content = content.replace(r'\\\\psi', r'\\psi')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cleaned up escape sequences!")
