#!/usr/bin/python

import os
import pdb
import time
import sys

EXCLUDED_EXTENSIONS = ['.swp', '.swo', '.swn', '.swm', '.pyc', '.class']
EXCLUDED_FILES = ['.git', '.repo', 'out', '.svn', '.DS_Store', '.gitignore']

PREFIX_CHARS = '+-- ';
BRANCH_CHARS = '|';

def print_tree(root, depth=0):
    if depth == 0:
        prefix = PREFIX_CHARS
    else:
        prefix = '%s%s%s' % (BRANCH_CHARS, ' ' * depth * 4, PREFIX_CHARS)

    basename = os.path.basename(root)
    name, extension = os.path.splitext(basename)

    if name not in EXCLUDED_FILES and extension not in EXCLUDED_EXTENSIONS:
        print('%s%s' % (prefix, basename))

    if not os.path.isdir(root):
        return

    for filename in os.listdir(root):
        print_tree(filename, depth + 1)


if __name__ == '__main__':
    print_tree(os.path.abspath('.'))
