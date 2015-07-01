import os, eyed3
from eyed3.id3 import Tag

"""
Reads a properly formated list of mp3s of the form 'dd - Artist - Title.mp3'
and updates the tag information to match.
"""

for f in os.listdir('.'):
    a = f.replace('.mp3', '').split(' - ')
    i = eyed3.load(f)

    if i == None:
        continue

    print(a)

    if i.tag == None:
        i.tag = Tag()

    i.tag.track_num = int(a[0])
    i.tag.artist = unicode(a[1])
    i.tag.title = unicode(a[2])
    i.tag.album = u'2015 - 4th of July Mixtape'
    i.tag.album_artist = u'DJ Pure'

    i.tag.genre = None
    i.tag.original_release_date = None
    i.tag.release_date = None
    i.tag.encoding_date = None
    i.tag.recording_date = None
    i.tag.tagging_date = None

    i.tag.save()
