#!/usr/bin/python

import subprocess, sys, re, pdb, multiprocessing
from colorize import UnixConsoleStyler

ERROR_PATTERN = re.compile('(.* error:.*|.* Stop\.$)', re.I)
WARNING_PATTERN = re.compile('(.* warning:.*$)', re.I)
LINKER_ERROR_PATTERN = re.compile('.*undefined reference to.*')
TIME_PATTERN = re.compile(r'^(real|user|sys).*[ \t]+\d+m[\d.]+s$')
OUTPUT_FILE = 'make.out'

""" Make error lines in GNU Make more visible """
def print_with_color(line):
    if ERROR_PATTERN.match(line):
        UnixConsoleStyler.apply_style('red')
    elif WARNING_PATTERN.match(line):
        UnixConsoleStyler.apply_style('yellow')
    elif LINKER_ERROR_PATTERN.match(line):
        UnixConsoleStyler.apply_style('white')
        UnixConsoleStyler.apply_style('on_red')
    elif TIME_PATTERN.match(line):
        pdb.set_trace()
        UnixConsoleStyler.apply_style('magenta')
    print(line.rstrip())
    UnixConsoleStyler.apply_style('default')

def print_command(cmd):
    UnixConsoleStyler.apply_style('blue')
    print(cmd.rstrip())
    UnixConsoleStyler.apply_style('default')

def print_info(info):
    UnixConsoleStyler.apply_style('green')
    print(info.rstrip())
    UnixConsoleStyler.apply_style('default')

""" Execute make and error colorize output """
def make():
    args = ' '.join(sys.argv[1:])
    jobs = 1 + multiprocessing.cpu_count()
    cmd = 'make -j%d %s' % (jobs, args)
    print_command(cmd)
    proc = subprocess.Popen(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            close_fds=True)
    output = []
    for line in proc.stdout:
        print_with_color(line)
        output.append(line)
    output.append("\n# vim:set ft=makeout #")

    open(OUTPUT_FILE, 'w').writelines(output)
    print_info('Output for make: %s' % OUTPUT_FILE)

    proc.wait()
    return proc.returncode

if __name__ == '__main__':
    make()
