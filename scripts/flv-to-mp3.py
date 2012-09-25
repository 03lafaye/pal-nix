#!/usr/bin/python
""" Run in directory with flv files to convert to mp3 with same name """

import os
import sys

def main():
    for file in os.listdir('.'):
        command = 'ffmpeg -i %s.flv -sameq %s.mp3'% (os.path.splitext(file)[0], os.path.splitext(file)[0])
        print(command)
        os.system(command)

if __name__ == '__main__':
    sys.exit(main())
