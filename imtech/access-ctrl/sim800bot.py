
import time
import serial
import sim800
import smsdb


def send(i):
	print i
	
def run():
	while True:
		try:
			lst = smsdb.get_ready_2_send()
			for i in lst:
				send(i)
			time.sleep(8.0)
		except Exception as x:
			print x
			

if __name__ == "__main__":
	run()
