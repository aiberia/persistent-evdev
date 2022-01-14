#!/usr/bin/python

import evdev
import sys

device = evdev.InputDevice(sys.argv[1])
print(device)
print(device.capabilities(verbose=True))

for event in device.read_loop():
    print(evdev.categorize(event))
