#!/usr/bin/python

import os
import pdb
import time
import sys

INCLUDED_FILES = ['.py', '.rb', '.java', '.c', '.h', '.cpp', '.cc', '.hpp', '.html', '.js', '.mk', '.xml', '.idl', '.css', '.cs']
EXCLUDED_DIRS = ['.git', '.repo', 'out', '.svn']
OUTPUT_FILE = 'cscope.files'

start_time = time.time()
output_file = open(OUTPUT_FILE, 'w')

current_path = os.path.abspath('.')

for root, dirs, files in os.walk(current_path):
    for directory in EXCLUDED_DIRS:
        if directory in dirs:
            dirs.remove(directory)

    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension in INCLUDED_FILES:
            file_path = os.path.join(root, filename)
            output_file.write('"%s"' % file_path + "\n")
            print(file_path)

# -b: just build
# -q: create inverted index for faster lookup
# -R: recurse in subdirectories
cmd = 'cscope -b -R -q'
print(cmd)
os.system(cmd)

elapsed_time = time.time() - start_time
print("\nGeneration of cscope database took: %.3f secs" % elapsed_time)
