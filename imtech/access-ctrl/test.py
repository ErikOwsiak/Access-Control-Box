#!/usr/bin/python

import io, os


x = os.open("/dev/ttyGSM0", os.O_NOCTTY | os.O_RDWR)
tty = io.TextIOWrapper(io.FileIO(x))


for line in iter(tty.readline, None):
	print(line.strip())
