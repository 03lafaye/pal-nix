import eyed3
import os
import sys
import pdb

if len(sys.argv) < 2:
    sys.exit('USAGE: id3 /folder/path')

os.chdir(sys.argv[1])

for f in os.listdir(sys.argv[1]):
    filename, extension = os.path.splitext(f)
    if (extension == '.mp3'):
        audiofile = eyed3.load(f)
        outname = '%02d - %s%s' % (
                audiofile.tag.track_num[0], filename, extension)
        print('Renaming %s to %s' % (f, outname))
        os.rename(f, outname)
