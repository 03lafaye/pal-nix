#!/usr/bin/env python3
"""
oculus_pull_latest_media.py

Examples:
  # pull latest 3 videos
  ./oculus_pull_latest_media.py -v -n 3

  # pull latest 1 screenshot
  ./oculus_pull_latest_media.py -p

  # choose a destination directory
  ./oculus_pull_latest_media.py -v -n 2 -d ~/Downloads/QuestMedia
"""

import argparse
import os
import shutil
import subprocess
import sys
from typing import List, Optional

VIDEO_DIR = "/sdcard/Oculus/VideoShots"
SCREENSHOT_DIR = "/sdcard/Oculus/Screenshots"


def run(cmd: List[str], *, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        check=False,
        text=True,
        capture_output=capture
    )


def ensure_adb_available() -> None:
    if shutil.which("adb") is None:
        print("Error: 'adb' not found in PATH.", file=sys.stderr)
        sys.exit(2)


def ensure_device_connected() -> None:
    # 'adb get-state' returns 'device' when a device is connected and authorized
    proc = run(["adb", "get-state"])
    state = (proc.stdout or proc.stderr or "").strip()
    if proc.returncode != 0 or state != "device":
        print("Error: No authorized device detected via ADB. "
              "Check USB/Wi-Fi connection and authorization (adb devices).",
              file=sys.stderr)
        sys.exit(2)


def list_latest(dir_path: str, limit: int) -> List[str]:
    """
    Return up to `limit` newest filenames from `dir_path` on the device.
    Uses 'ls -1t' to avoid parsing long format columns.
    """
    proc = run(["adb", "shell", "ls", "-1t", dir_path])
    if proc.returncode != 0:
        print(f"Error listing files in {dir_path}: {proc.stderr.strip()}", file=sys.stderr)
        return []

    lines = [ln.strip() for ln in (proc.stdout or "").splitlines() if ln.strip()]
    # Some Android shells may still include a 'total' line; filter it out defensively.
    lines = [ln for ln in lines if not ln.lower().startswith("total")]
    return lines[:max(0, limit)]


def pull_files(dir_path: str, filenames: List[str], dest_dir: str) -> None:
    if not filenames:
        print("No files to pull.")
        return

    os.makedirs(dest_dir, exist_ok=True)

    for name in filenames:
        remote = f"{dir_path}/{name}"
        print(f"Pulling: {remote} → {dest_dir}")
        proc = run(["adb", "pull", remote, dest_dir], capture=False)
        if proc.returncode != 0:
            print(f"Failed to pull: {name}", file=sys.stderr)
        else:
            print(f"✓ Pulled: {name}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Pull latest videos or screenshots from a Meta Quest device via ADB."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--videos", action="store_true", help="Pull from VideoShots")
    group.add_argument("-p", "--photos", action="store_true", help="Pull from Screenshots")

    parser.add_argument("-n", "--num", type=int, default=1,
                        help="Number of latest files to pull (default: 1)")
    parser.add_argument("-d", "--dest", default=os.getcwd(),
                        help="Destination directory (default: current directory)")

    args = parser.parse_args(argv)

    ensure_adb_available()
    ensure_device_connected()

    src_dir = VIDEO_DIR if args.videos else SCREENSHOT_DIR
    count = max(1, args.num)

    files = list_latest(src_dir, count)
    if not files:
        print(f"No files found in {src_dir}.", file=sys.stderr)
        return 1

    pull_files(src_dir, files, args.dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
