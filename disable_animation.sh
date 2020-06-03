#!/usr/bin/env bash
 
$ANDROID_HOME/platform-tools/adb shell settings put global window_animation_scale 0.0;
$ANDROID_HOME/platform-tools/adb shell settings put global transition_animation_scale 0.0;
$ANDROID_HOME/platform-tools/adb shell settings put global animator_duration_scale 0.0;
