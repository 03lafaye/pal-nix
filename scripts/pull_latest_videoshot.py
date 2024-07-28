#!/usr/bin/env python3

import os
import subprocess
import sys

def get_latest_file_from_videoshots():
    try:
        # List all files in the VideoShots directory
        result = subprocess.run(['adb', 'shell', 'ls', '-lt', '/sdcard/Oculus/VideoShots'], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error listing files: {result.stderr}")
            return None
        
        files = result.stdout.strip().split('\n')
        if not files:
            print("No files found in VideoShots directory.")
            return None

        # Skip the total line if present
        if files[0].startswith('total'):
            files = files[1:]
        
        # Extract the filename from the listing
        latest_file = files[0].split()[-1]
        return latest_file
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def pull_file_from_videoshots(destination_dir):
    latest_file = get_latest_file_from_videoshots()
    if not latest_file:
        print("No file to pull.")
        return
    
    # Ensure destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Pull the latest file to the destination directory
    try:
        result = subprocess.run(['adb', 'pull', f'/sdcard/Oculus/VideoShots/{latest_file}', destination_dir])
        if result.returncode == 0:
            print(f"Successfully pulled {latest_file} to {destination_dir}")
        else:
            print(f"Failed to pull the file: {result.stderr}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        destination_dir = sys.argv[1]
    else:
        destination_dir = os.getcwd()

    pull_file_from_videoshots(destination_dir)

