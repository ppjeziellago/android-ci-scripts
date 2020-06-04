#!/usr/bin/env bash

# CONFIGURE YOUR PROJECT HERE
export PROJECT_LOCATION="/home/user/project-dir"
export IGNORED_MODULES_UI_TEST=":mymodule"
#######

bash create_avd.sh

bash wait_emulator.sh;

$ANDROID_HOME/platform-tools/adb shell input keyevent 82; 

python run_ui_test.py

bash stop_emulator.sh
