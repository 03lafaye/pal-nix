import os, eyed3
for f in os.listdir('.'):
    a = f.split(' - ')
    i = eyed3.load(f)
    print(f)
    print(i)
    # i.tag.artist = a[1]
    # i.tag.track_num = int(a[0])
    # i.tag.album = '2015 - 4th of July Mixtape'
    # i.tag.title = a[2].replace('.mp3','')
    # i.tag.album_artist = 'DJ Pure'
