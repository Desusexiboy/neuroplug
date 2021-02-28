#!/bin/bash

rfcomm -i hci0 -r connect /dev/rfcomm1 0D:00:18:A1:54:15 2

sleep 2

python2 ./neuroplug.py
