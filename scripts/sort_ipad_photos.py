#!/usr/bin/python

import datetime, time, sys, os, shutil

# iPad sorts photos by timestamp rather than by name. A solution to this is to
# change the timestamps for files so that they are sorted in the same order as
# the file names.

def get_next_time(count):
    future = datetime.datetime(2010, 1, 1, 0, 0)
    future += datetime.timedelta(minutes = count) 
    timestamp = time.mktime(future.timetuple())
    return timestamp

def set_timestamps():
    folder = sys.argv[1]

    list = os.listdir(folder)
    list.sort(reverse=True)

    count = 0
    for file in list:
        if file.lower().endswith('jpg') or file.lower().endswith('png'):
            count += 1
            time = get_next_time(count)
            print('Changing timestamp of %s to %d' % (file, time))
            os.utime(file, (time, time))

def create_new_files():
    folder = sys.argv[1]

    list = os.listdir(folder)
    list.sort(reverse=True)
    
    sorted_folder = folder + '/sorted'
    if not os.path.exists(sorted_folder):
        os.mkdir(sorted_folder)

    count = 0
    for file in list: 
        if file.lower().endswith('jpg') or file.lower().endswith('png'):
            shutil.copyfile(file, sorted_folder + '/' + file)
            time.sleep(1)

def main():
    create_new_files()

USAGE = 'Usage: python sort_ipad_photos.py folder'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(USAGE)

    main()
