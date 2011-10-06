#! /usr/bin/env python

import sys, subprocess

USAGE = "Usage: padb.py $ANDROID_SOURCE $LOCAL_DESTINATION"

# Execute multiple pulls using a pattern.
def pull(args):
    cmd = 'adb shell ls -1 %s' % args[0].strip()
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            close_fds=True) 
    for line in proc.stdout:
        cmd = 'adb pull %s %s' % (line.strip(), args[1].strip())
        print(cmd)
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                close_fds=True)  
        print("\n".join(proc.stdout.readlines()))

if __name__ == '__main__':
    args = sys.argv[1:]
    if not len(args) == 2:
        sys.exit(USAGE)
    pull(args)
