#!/usr/bin/env python

import os
import re
import subprocess
import time

MEMTOTAL_PATTERN = re.compile('^MemTotal.*')
MEMFREE_PATTERN = re.compile('^MemFree.*')

while 1:
    output = subprocess.Popen(
            'adb shell cat /proc/meminfo', stdout=subprocess.PIPE, shell=True)
    for line in output.stdout.readlines():
        if MEMTOTAL_PATTERN.match(line.strip()) or MEMFREE_PATTERN.match(line.strip()):
            print(line.strip())
    output.kill()
    print('')
    time.sleep(1)
