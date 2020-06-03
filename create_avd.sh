#!/usr/bin/env bash

$ANDROID_HOME/platform-tools/adb kill-server;
$ANDROID_HOME/platform-tools/adb start-server;

echo yes | $ANDROID_HOME/tools/bin/sdkmanager "tools" "system-images;android-28;default;x86"
 
$ANDROID_HOME/tools/bin/avdmanager create avd -f -n emulator --abi 'default/x86' --package "system-images;android-28;default;x86" --device "pixel"

$ANDROID_HOME/emulator/emulator -avd emulator -no-window -noaudio -no-boot-anim -no-snapshot -camera-back none -camera-front none -netfast -accel auto &
