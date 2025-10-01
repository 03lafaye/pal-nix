import os

# Get all .wav files in current folder
files = [f for f in os.listdir('.') if f.lower().endswith('.wav')]
files.sort()  # Sort alphabetically (which will handle 01 to 13)

# Write M3U file
with open('playlist.m3u', 'w', encoding='utf-8') as playlist:
    playlist.write('#EXTM3U\n')
    for f in files:
        playlist.write(f"{f}\n")

