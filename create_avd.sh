#!/usr/bin/env bash

$ANDROID_HOME/platform-tools/adb start-server

echo yes | $ANDROID_HOME/tools/bin/sdkmanager "tools" "system-images;android-28;default;x86"

echo no | $ANDROID_HOME/tools/bin/avdmanager create avd -f -n emulator -k "system-images;android-28;default;x86" --device "Nexus 5"

$ANDROID_HOME/emulator/emulator -avd emulator -no-audio -no-window -no-snapshot -wipe-data &
