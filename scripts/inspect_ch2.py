import glob
import re

for f in sorted(glob.glob('scripts/ch2_part*.js')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    topics = set(re.findall(r'topicCode[\'":\s]+([A-Za-z0-9\.\-]+)', c))
    print(f, len(c), 'Topics:', topics)
