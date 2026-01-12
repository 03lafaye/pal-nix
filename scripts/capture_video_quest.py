#!/usr/bin/env python3
"""
capture_video_quest.py

Control Oculus / Meta Quest video capture via adb.

Examples:
    # Start capture with default settings (1080p, default bitrate)
    python capture_video_quest.py -s

    # End capture
    python capture_video_quest.py -e

    # Start capture with custom bitrate (e.g. 20 Mbps)
    python capture_video_quest.py -s -b 20000000

    # Start stereo capture (side-by-side)
    python capture_video_quest.py -s --stereo
"""

import argparse
import subprocess
import sys

# Defaults (tweak if you like)
DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080
DEFAULT_BITRATE = 20_000_000  # 20 Mbps


def run_adb_shell(args):
    """Run an adb shell command and handle errors nicely."""
    cmd = ["adb", "shell"] + args
    try:
        print(">", " ".join(cmd))
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("ERROR: 'adb' not found. Make sure Android platform-tools are installed and in your PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: adb command failed with exit code {e.returncode}")
        sys.exit(e.returncode)


def start_capture(bitrate, stereo):
    # Set resolution to 1080p (16:9)
    run_adb_shell(["setprop", "debug.oculus.capture.width", str(DEFAULT_WIDTH)])
    run_adb_shell(["setprop", "debug.oculus.capture.height", str(DEFAULT_HEIGHT)])

    # Set bitrate
    if bitrate is not None:
        run_adb_shell(["setprop", "debug.oculus.capture.bitrate", str(bitrate)])

    # Mono vs stereo
    # 0 = mono (left eye), 2 = stereo (according to Oculus debug props)
    eye_mode = "2" if stereo else "0"
    run_adb_shell(["setprop", "debug.oculus.screenCaptureEye", eye_mode])

    # Start video capture
    run_adb_shell(["setprop", "debug.oculus.enableVideoCapture", "1"])

    print("Video capture started." + (" (stereo)" if stereo else ""))


def end_capture():
    # Stop video capture
    run_adb_shell(["setprop", "debug.oculus.enableVideoCapture", "0"])
    print("Video capture stopped.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enable or disable video capture on a Quest headset via adb."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-s",
        "--start",
        action="store_true",
        help="Start video capture",
    )
    group.add_argument(
        "-e",
        "--end",
        action="store_true",
        help="End video capture",
    )

    parser.add_argument(
        "-b",
        "--bitrate",
        type=int,
        default=DEFAULT_BITRATE,
        help=f"Video bitrate in bits per second (default: {DEFAULT_BITRATE})",
    )

    parser.add_argument(
        "--stereo",
        action="store_true",
        help="Enable stereo (side-by-side) capture when starting",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.start:
        start_capture(bitrate=args.bitrate, stereo=args.stereo)
    elif args.end:
        end_capture()
    else:
        # argparse's mutually exclusive group already enforces one of them,
        # so this is just a safety net.
        print("ERROR: specify either -s/--start or -e/--end")
        sys.exit(1)


if __name__ == "__main__":
    main()
