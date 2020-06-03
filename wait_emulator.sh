#!/usr/bin/env bash

set +e

bootanim=""
failcounter=0
timeout_in_sec=600

until [[ "$bootanim" = "1" ]]; do
  bootanim=`$ANDROID_HOME/platform-tools/adb shell getprop sys.boot_completed 2>&1 &`
  if [[ "$bootanim" != "1" ]]; then
    let "failcounter += 1"
    echo "Waiting for emulator to start"
    if [[ $failcounter -gt timeout_in_sec ]]; then
      echo "Timeout ($timeout_in_sec seconds) reached; failed to start emulator"
      exit 1
    fi
  fi
  sleep 1
done

$ANDROID_HOME/platform-tools/adb shell input keyevent 82

echo "Emulator is ready"
