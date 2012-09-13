solutions = [
  { "name"        : "src",
    "url"         : "http://src.chromium.org/chrome/trunk/src.git",
    "deps_file"   : ".DEPS.git",
    "managed"     : True,
    "custom_deps" : {
        "src/content/test/data/layout_tests": None,
        "src/third_party/WebKit/LayoutTests": None,
        "src/chrome/tools/test/reference_build/chrome": None,
        "src/chrome_frame/tools/test/reference_build/chrome": None,
        "src/chrome/tools/test/reference_build/chrome_linux": None,
        "src/chrome/tools/test/reference_build/chrome_mac": None,
    },
    "safesync_url": "",
  },
]
target_os = ["android"]
