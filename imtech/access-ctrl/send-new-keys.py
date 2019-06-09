#!/usr/bin/python

import time
import requests
import json


apikey = "DFHID8752ASD0985"
server = "188.252.52.110"
urlGetReady = "http://%s/be/api/%s/apiGetReadyToSend" % (server, apikey)
urlUpdateIds = "http://%s/be/api/%s/apiUpdateSent" % (server, apikey)


def get_ready_to_send():
	r = requests.get(urlGetReady)
	if "text/json" in r.headers["content-type"]:
		return r.json()
	else:
		pass

def enqueue_keys(arr):
	for i in arr:
		print i
	
def update_sent(ids):
	r = requests.post(urlUpdateIds, ids)
	
def main():
	while True:
		try:
			jobj = getReadyToSend()
			ids = enqueueKeys(jobj["arr"])
			updateSent(ids)
			time.sleep(8.0)
		except Exception as x:
			print x


if __name__ == "__main__":
	main()
