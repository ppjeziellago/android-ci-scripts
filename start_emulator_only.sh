#!/bin/bash
export ANDROID_HOME=$HOME/Library/Android/sdk
echo yes | $ANDROID_HOME/tools/bin/sdkmanager "tools" "system-images;android-28;default;x86"
$ANDROID_HOME/tools/bin/avdmanager create avd -f -n emulator --abi 'default/x86' --package "system-images;android-28;default;x86" --device "pixel"
$ANDROID_HOME/emulator/emulator -avd emulator -noaudio -no-boot-anim -no-snapshot -camera-back none -camera-front none -netfast -accel auto -no-window -wipe-data &
bash wait_emulator.sh
