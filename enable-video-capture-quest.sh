# Set Resolution to 1080p (16:9)
adb shell setprop debug.oculus.capture.width 1920
adb shell setprop debug.oculus.capture.height 1080

# Set Bitrate to 20Mbps (Default is low, causing artifacts)
adb shell setprop debug.oculus.capture.bitrate 20000000

# Optional: Enable Full Rate Capture (60/72/90fps instead of 30fps)
# Warning: Can impact performance on older headsets
adb shell setprop debug.oculus.fullRateCapture 1

adb shell setprop debug.oculus.enableVideoCapture 1
