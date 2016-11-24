#!/bin/sh

# Converts from Unity cubemap layout to 360 video 3x2 cubemap format
# Depends on ImageMagick being installed.

# Usage: unitycubmeap-to-3x2.sh cubemap.jpg 1024 converted

source_image=$1 # input is a vertical cubemap (+x,-x,+y,-y,+z,-z)
tile_size=$2 # e.g. 1024
output_file=$3
output_dir="tmp_tiles"

mkdir ${output_dir}
pushd ${output_dir}

# Split into 6 tiles
convert $source_image -crop ${tile_size}x${tile_size} tile_%03d.jpg

# Re-order into 3x2 format:
# -x +x +y
# -y -z +z

mv tile_000.jpg tile_01.jpg
mv tile_001.jpg tile_00.jpg

# mv tile_002.jpg tile_02.jpg
convert tile_002.jpg -rotate 180 tile_02.jpg

# mv tile_003.jpg tile_03.jpg
convert tile_003.jpg -rotate 180 tile_03.jpg

mv tile_004.jpg tile_05.jpg
mv tile_005.jpg tile_04.jpg 

# Create 3x2 output image
montage tile_0[0-9].jpg -tile 3x2 -geometry ${tile_size}x${tile_size}+0+0 ../${output_file}

popd

rm -rf ${output_dir}
