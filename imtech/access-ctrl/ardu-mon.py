#!/usr/bin/python

import sys
import time
import serial
import sqlite3
import conf
import smsdb
import sim800 as sim


baudRate = 2400
portDelay = 0.08
byteCount = None
# uarts 
ardu = None
gsm = None
ttyARDU = "/dev/ttyARDU0"
ttyGSM = "/dev/ttyGSM0"
# debaunce
doorBellLastPress = None


def door_bell_pressed():
	global doorBellLastPress
	if doorBellLastPress is None:
		doorBellLastPress = time.time()
		#gsm.sendSms("883279496", "Main Door Bell Button Pressed!")
		smsdb.add_msg(0, "", "Main Door Bell Button Pressed!")
	elif time.time() - doorBellLastPress > 4:
		doorBellLastPress = time.time()
		#gsm.sendSms("883279496", "Main Door Bell Button Pressed!")
		smsdb.add_msg(0, "", "Main Door Bell Button Pressed!")
		
def on_ardu_data_in():
	try:
		global ardu
		ardu = serial.Serial(ttyARDU, baudRate, timeout=1)
		while True:
			if not ardu.is_open:
				ardu.open()
			print "ardu on read..."
			ln = ardu.readline().strip()
			if ln == "bellBtnPress":
				door_bell_pressed()
	except Exception as x:
		print x
		on_ardu_data_in()

def system_boot():
	try:
		print "system_boot..."
		val = conf.get_val("adminTels")
		# exp: adminTels:= 883279496; 555222999;
		for s in [s.strip() for s in val.split(";")]:
			smsdb.add_msg(0, s, "System Boot Event")
		return True
	except Exception as x:
		print x
		time.sleep(2)
		system_boot()
		
def main():
	print "__main__"
	system_boot()
	on_ardu_data_in()


if __name__ == "__main__":
	conf.load()
	main()
