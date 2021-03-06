#!/bin/sh

# Helper for building Chrome for Android with ninja

echo "Looking for gclient..."

if ! command -v gclient
then
    echo "gclient not found... make sure depot_tools is in your PATH"
    exit 1
fi

if [ ! -d src ]
then
    echo "No src directory found... configuring gclient"
    gclient config http://git.chromium.org/chromium/src.git --git-deps

    if [ -f $HOME/pal-nix/.gclient ]
    then
        cp $HOME/pal-nix/.gclient .gclient
    else
        echo "target_os = ['android']" >> .gclient
    fi
fi

echo "Executing gclient sync..."

time gclient sync -j12 -v --nohooks

if [ ! -d src/build/android ]
then
    echo "Could not find src/build/android directory... gclient sync failed"
    exit 1
fi

echo "Setting up Chrome for Android build environment..."
pushd src
export CHROME_SRC=
. build/android/envsetup.sh

echo "Executing gclient runhooks using ninja..."
GYP_GENERATORS=ninja gclient runhooks -v

# You may need to install the build dependencies for android:
# pushd build
# sudo ./install-build-deps-android.sh
# popd

ninja -C out/Debug -j 12 content_shell_apk
