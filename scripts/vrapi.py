#! /usr/bin/env python

import sys
import re

# Calculate average FPS from output of `adb locat VrApi:* TimeWarp:* *:S`

# 12-12 22:47:03.611 20810 21332 W TimeWarp: VSync 294154: Eye=0,late=0.0ms,over=1.2ms,CPU=0.7ms,GPU=3.0ms,Tot=4.9ms
# 12-12 22:47:04.611 20810 21338 I VrApi   : FPS=61,Prd=51ms,Tear=0,Early=61,Stale=0,VSnc=1,Lat=1,CPU2/GPU=2/2,1113/315MHz,OC=F,TA=C/C/C/C,SP=F/F/F/F,Mem=1017MHz,Free=1403MB,PSM=0,PLS=0,Temp=28.7C/28.0C

FPS_PATTERN = '^.*FPS=(\d+).*Tear=(\d+).*$'

fps_sum = 0
tear_sum = 0
num_frames = 0
skip_first_n_frames = 10

matcher = re.compile(FPS_PATTERN)

for line in sys.stdin:
    match = matcher.match(line)
    if match:
        fps = min(int(match.group(1)), 60)
        tears = int(match.group(2))
        if num_frames > skip_first_n_frames:
            fps_sum += fps
            tear_sum += tears
        num_frames += 1

sys.stdout.write("Total Num Frames: %d\n" % (num_frames - skip_first_n_frames))
sys.stdout.write(
        "Avg FPS %f\n" % (fps_sum / (num_frames - skip_first_n_frames)))
sys.stdout.write(
        "Avg Tears %f\n" % (tear_sum / (num_frames - skip_first_n_frames)))
sys.stdout.write(
        "Total Tears %f\n" % (tear_sum)) 



