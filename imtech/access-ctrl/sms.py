#!/usr/bin/python

import io
import time
import serial


portDelay = 0.08
byteCount = None
baudRate = 2400
ttyPORT = "/dev/ttyGSM0"
#ttyPORT = "/dev/ttyS0"


def sendMsg(com, num, msg):
	print "sendMsg..."
	if not com.is_open:
		print "port not open"
	buff = "AT+CMGS=%s" % num
	com.write(buff)
	com.write(serial.CR)
	time.sleep(portDelay)
	ln = com.read_until(">", byteCount).strip()
	print "> write msg: %s" % msg
	com.write(msg)
	com.write('\x1A')
	while True:
		print "on read..."
		ln = com.read_until(serial.CR, byteCount).strip()
		if ln == "OK":
			print "msg sent..."
			return True
		else:
			print ln
			return False


def changeMode(com, v):
	print "changeMode..."
	if not com.is_open:
		print "port not open"
	com.write("AT+CMGF=%s" % v)
	com.write(serial.CR)
	time.sleep(portDelay)
	while True:
		print "on read..."
		ln = com.read_until(serial.CR, byteCount).strip()
		print "ln: %s" % ln
		if ln == "OK":
			return True
		elif "ERROR" in ln:
			print "error: %s" % ln


def sendAT(com):
	print "startAT"
	if not com.is_open:
		com.open()
	com.write("AT")
	com.write(serial.CR)
	time.sleep(portDelay)
	while True:
		print "on read..."
		ln = com.read_until(serial.CR, byteCount).strip()
		print "ln: %s" % ln
		if ln == "OK":
			return True
		print "ln: %s" % ln
		
		
def run(i):
	print "run..."
	try:
		com = serial.Serial(ttyPORT, baudRate, timeout=1)
		if not sendAT(com):
			print "sendAT error"
			return
		if not changeMode(com, 1):
			print "changeMode error"
			return
		msg = "i: %s / msg msg text..." % i
		if not sendMsg(com, "883279496", msg):
			print "sendMsg error"
		print "msg sent ok"
	except Exception as e:
		print e
	finally:
		com.close()
		com = None


if __name__ == "__main__":
	for i in range(0, 99):
		run(i)
		time.sleep(2)
