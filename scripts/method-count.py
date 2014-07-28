#! /usr/bin/env python

import subprocess, os, operator
from subprocess import DEVNULL


CREATE_DEX = '"${ANDROID_SDK}/build-tools/19.0.0/dx" --dex --output %s.dex %s.jar'
COUNT_METHODS = "cat %s.dex | head -c 92 | tail -c 4 | hexdump -e '1/4 \"%%d\\n\"'"
CLEAN_DEX = 'rm *.dex'

method_counts = {}

for f in os.listdir('.'):
    if not f.lower().endswith('jar'):
        continue

    name = os.path.splitext(f)[0]
    subprocess.call(CREATE_DEX % (name, name), stdout=DEVNULL, stderr=DEVNULL, shell=True)
    cmd = COUNT_METHODS % name
    count = subprocess.check_output(cmd, stderr=DEVNULL, shell=True).strip()
    method_counts[name] = int(count)

subprocess.call(CLEAN_DEX, shell=True)

sum = 0

for k,v in sorted(list(method_counts.items()), key=operator.itemgetter(1)):
    print('%s: %d methods' % (k, v))
    sum += v

print('-' * 10)
print('Total: %d' % sum)
