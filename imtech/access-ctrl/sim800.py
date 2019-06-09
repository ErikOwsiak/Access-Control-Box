
import time
import serial


CRLZ = '\x1A'
CR = '\r'
CRNL = "\r\n"
DELAY = 1.0
COMMDELAY = 0.08
LONGDELAY = 2.0
MIDDELAY = 1.0
SHORTDELAY = 0.5
# response strings
MSG_RES_STR = "+CMGS:"
ATI_RES_STR = "SIM800 R14.18"
AT_RES_STR = "OK"


class sim800:

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def __init__(self, ttyGSM, baudRate):
		self.comm = serial.Serial(ttyGSM, baudRate, timeout=1)
		if not self.comm.is_open:
			self.comm.open()
		self.comm.flush()
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def init(self):
		print "init..."
		self.sendAT()
		self.sendATE0()
		self.sendCMGFtxt()
		#self.sendATI()
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def sendATE0(self):
		print "sendATE0..."
		self.sendCmd("ATE0", "")
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def sendAT(self):
		print "sendAT..."
		self.sendCmd("AT", "")
		
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def sendCMGFtxt(self):
		print "sendCMGFtxt"
		self.sendCmd("AT+CMGF=1", "")
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -	
	def sendATI(self):
		print "sendATI"
		self.sendCmd("ATI", ATI_RES_STR)
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -	
	def sendCmd(self, CMD, RESTR):
		print "sendCmd: %s / %s" % (CMD, RESTR)
		if not self.comm.is_open:
			self.comm.open()
		self.comm.write(CMD)
		self.comm.write(serial.CR)
		self.blockOn(RESTR)
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def blockOn(self, RESTR):
		if RESTR == "":
			time.sleep(LONGDELAY)
			return
		while True:
			strlen = (len(RESTR) + 1)
			ln = self.comm.read_until(RESTR, strlen).strip()
			print "ln: %s; %s" % (ln, strlen)
			if ln == RESTR:
				print RESTR
	
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def sendSms(self, num, msg):
		print "sendSms..."
		self.comm.write("AT+CMGS=\"%s\"" % num)
		self.comm.write(serial.CR)
		self.delayOnBuffOut()
		time.sleep(MIDDELAY)
		self.comm.write(msg)
		self.comm.write(CRLZ)
		self.delayOnBuffOut()
		time.sleep(MIDDELAY)
		
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	def delayOnBuffOut(self):
		while self.comm.out_waiting > 0:
			time.sleep(0.01)
		time.sleep(0.1);
