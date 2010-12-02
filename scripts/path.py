#! /usr/bin/env python

import os
import sys
import optparse
import pdb

USAGE = 'path.py [-d|-f folder]'
DESCR = 'Utility to remove folders and duplicates from the $PATH'

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x) ]

def remove_from_path(folder):
    path = os.environ['PATH']
    list = path.split(':')
    list.remove(folder)
    #os.putenv('PATH', ':'.join(list))
    os.system('export PATH="%s"' % ':'.join(list))

def remove_duplicates_from_path():
    path = os.environ['PATH']
    list = path.split(':')
    list = uniq(list)
    #os.putenv('PATH', ':'.join(list))
    print('export PATH="%s"' % ':'.join(list))
    os.system('export PATH="%s"' % ':'.join(list))


def cmdln():
    cmdln = optparse.OptionParser(usage=USAGE, description=DESCR)
    cmdln.add_option('-d', '--remove-duplicates', dest='duplicates',
                     action='store_true', default=False,
                     help='Remove duplicates from $PATH')
    cmdln.add_option('-f', '--remove-folder', dest='folder',
                     help='Remove folder from $PATH')
    opts, args = cmdln.parse_args(sys.argv[1:])
    return opts

if __name__ == '__main__':
    opts = cmdln();

    if opts.duplicates:
        remove_duplicates_from_path()
    elif opts.folder:
        remove_from_path(opts.folder)
    else:
        print(USAGE)
