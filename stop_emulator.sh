#!/usr/bin/env bash

$ANDROID_HOME/platform-tools/adb devices | grep emulator | cut -f1 | while read line; do echo $line; $ANDROID_HOME/platform-tools/adb -s $line emu kill; done
