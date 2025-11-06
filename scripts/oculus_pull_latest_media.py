#!/usr/bin/env python3
"""
oculus_pull_latest_media.py

Examples:
  # pull latest 3 videos and open the files
  ./oculus_pull_latest_media.py -v -n 3 -o

  # pull latest 1 screenshot and open the folder
  ./oculus_pull_latest_media.py -p -of

  # choose a destination directory and open both files and folder
  ./oculus_pull_latest_media.py -v -n 2 -d ~/Downloads/QuestMedia -o -of
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
        print(
            "Error: No authorized device detected via ADB. "
            "Check USB/Wi-Fi connection and authorization (adb devices).",
            file=sys.stderr
        )
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


def pull_files(dir_path: str, filenames: List[str], dest_dir: str) -> List[str]:
    """
    Pull files and return a list of successfully pulled local paths.
    """
    pulled_local_paths: List[str] = []

    if not filenames:
        print("No files to pull.")
        return pulled_local_paths

    os.makedirs(dest_dir, exist_ok=True)

    for name in filenames:
        remote = f"{dir_path}/{name}"
        print(f"Pulling: {remote} → {dest_dir}")
        proc = run(["adb", "pull", remote, dest_dir], capture=False)
        if proc.returncode != 0:
            print(f"Failed to pull: {name}", file=sys.stderr)
        else:
            local_path = os.path.join(dest_dir, name)
            pulled_local_paths.append(local_path)
            print(f"✓ Pulled: {name}")

    return pulled_local_paths


# -------- platform helpers for opening files/folders --------

def _is_macos() -> bool:
    return sys.platform == "darwin"

def _is_windows() -> bool:
    return os.name == "nt" or sys.platform.startswith("win")

def _is_linux() -> bool:
    return sys.platform.startswith("linux")


def open_file(path: str) -> None:
    path = os.path.abspath(path)
    try:
        if _is_macos():
            subprocess.run(["open", path], check=False)
        elif _is_windows():
            # os.startfile is simplest for files
            try:
                os.startfile(path)  # type: ignore[attr-defined]
            except Exception:
                # fallback to explorer
                subprocess.run(["explorer", path], check=False)
        else:
            # Linux (or other) fallback
            opener = shutil.which("xdg-open")
            if opener:
                subprocess.run([opener, path], check=False)
            else:
                print(f"(Info) Could not find a system opener for {path}.", file=sys.stderr)
    except Exception as e:
        print(f"(Info) Failed to open file {path}: {e}", file=sys.stderr)


def reveal_in_folder(path: str) -> None:
    """
    Reveal the file in its folder (highlight if supported).
    If highlighting is not supported, just open the folder.
    """
    path = os.path.abspath(path)
    folder = os.path.dirname(path)

    try:
        if _is_macos():
            # Reveal (highlight) in Finder
            subprocess.run(["open", "-R", path], check=False)
        elif _is_windows():
            # Explorer highlight
            # Note: '/select,' must be one argument including the comma
            norm = os.path.normpath(path)
            subprocess.run(["explorer", "/select,", norm], check=False)
        else:
            opener = shutil.which("xdg-open")
            if opener:
                subprocess.run([opener, folder], check=False)
            else:
                print(f"(Info) Could not find a system opener for {folder}.", file=sys.stderr)
    except Exception as e:
        print(f"(Info) Failed to reveal {path}: {e}", file=sys.stderr)


def open_folder(path: str) -> None:
    folder = os.path.abspath(path)
    try:
        if _is_macos():
            subprocess.run(["open", folder], check=False)
        elif _is_windows():
            subprocess.run(["explorer", folder], check=False)
        else:
            opener = shutil.which("xdg-open")
            if opener:
                subprocess.run([opener, folder], check=False)
            else:
                print(f"(Info) Could not find a system opener for {folder}.", file=sys.stderr)
    except Exception as e:
        print(f"(Info) Failed to open folder {folder}: {e}", file=sys.stderr)


# ------------------------------------------------------------

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

    # New behavior: these are boolean flags to perform actions after pulling
    parser.add_argument("-o", "--open", dest="open_files", action="store_true",
                        help="Open each pulled file")
    parser.add_argument("-of", "--open-folder", dest="open_folder", action="store_true",
                        help="Open/reveal the containing folder(s) after pulling")

    args = parser.parse_args(argv)

    ensure_adb_available()
    ensure_device_connected()

    src_dir = VIDEO_DIR if args.videos else SCREENSHOT_DIR
    count = max(1, args.num)

    files = list_latest(src_dir, count)
    if not files:
        print(f"No files found in {src_dir}.", file=sys.stderr)
        return 1

    pulled_paths = pull_files(src_dir, files, args.dest)

    if not pulled_paths:
        # Nothing successfully pulled; nothing to open
        return 1

    # Open/reveal actions
    if args.open_files:
        for p in pulled_paths:
            open_file(p)

    if args.open_folder:
        # If you prefer highlighting each file: call reveal_in_folder for each pulled file.
        # If you prefer opening the destination folder once, uncomment the open_folder line.
        # Here we "reveal" each file to match "folder of all files pulled" with highlight.
        for p in pulled_paths:
            reveal_in_folder(p)
        # Alternatively, just open the destination folder once:
        # open_folder(args.dest)

    return 0


if __name__ == "__main__":
    sys.exit(main())
