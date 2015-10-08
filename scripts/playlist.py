import os

for f in os.listdir('.'):
    if os.path.splitext(f)[1] != '.mp3':
        continue
    print(f)

