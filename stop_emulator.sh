#!/usr/bin/env bash
# finish current AVD
$ADB=$ANDROID_HOME/platform-tools/adb
$ADB devices | grep emulator | cut -f1 | while read line; do echo $line; $ADB -s $line emu kill; done
