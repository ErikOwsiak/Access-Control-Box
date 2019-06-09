
from sysdefs import CONF


LNS = None


def load():
	global LNS
	if LNS is not None:
		return
	LNS = {}
	f = open(CONF)
	lns = f.readlines()
	for ln in lns:
		if ln.startswith("#"):
			continue
		arr = ln.split(":=")
		key = arr[0].strip()
		# remove last ";"
		val = arr[1].strip()[0:-1]
		LNS[key] = val
	f.close()

def get_val(key):
	return LNS[key]
