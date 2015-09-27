#!/usr/bin/env python

import os
import re
import subprocess
import time

MEMTOTAL_PATTERN = re.compile('^(MemTotal.*?)(\d+)( kB).*')
MEMFREE_PATTERN = re.compile('^(MemFree.*?)(\d+)( kB).*')

while 1:
    output = subprocess.Popen(
            'adb shell cat /proc/meminfo', stdout=subprocess.PIPE, shell=True)

    free_memory_in_kb = 0
    total_memory_in_kb = 0

    print  output.stdout.readlines()

    for line in output.stdout.readlines():
        import pdb

        print(line.strip())
        total = MEMTOTAL_PATTERN.match(line.strip())
        free = MEMFREE_PATTERN.match(line.strip())
        if total:
            total_memory_in_kb = int(total.group(2))
            # print(total.group(0))
            # print(total_memory_in_kb)
            print line
            break
        if free:
            pdb.set_trace()
            free_memory_in_kb = int(free.group(2))
            # print(free.group(0))
            # print(free_memory_in_kb)
            print line
            break

    output.kill()
    print('')
    time.sleep(1)
