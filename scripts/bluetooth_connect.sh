#! /bin/bash

rfkill unblock bluetooth
echo "power on" | bluetoothctl
echo "connect C0:28:8D:64:15:94" | bluetoothctl

