function android_create_dev_icon {
    version=`git describe --abbrev=0 --tags`
    branch=`git rev-parse --abbrev-ref HEAD`
    commit=`git rev-parse --short HEAD`
    width=`identify -format %w $1`

    convert -background '#0008' -fill white -gravity center -size ${width}x40 \
    caption:"${version} ${branch} ${commit}" $1 +swap -gravity south -composite $1
}

icon="res/drawable-xxxhdpi/ic_launcher.png"
android_create_dev_icon $icon

icon="res/drawable-xxhdpi/ic_launcher.png"
android_create_dev_icon $icon

icon="res/drawable-xhdpi/ic_launcher.png"
android_create_dev_icon $icon

icon="res/drawable-hdpi/ic_launcher.png"
android_create_dev_icon $icon
