#!/usr/bin/python

import os
import time 
import sqlite3
from sysdefs import SMSDB


tbl_msgs = """CREATE TABLE msgs 
	(id INTEGER PRIMARY KEY AUTOINCREMENT, flags	INTEGER, 
		tel_num TEXT, msg TEXT, dtc TEXT)"""


def create():
	if os.path.exists(SMSDB):
		return 0
	conn = sqlite3.connect(SMSDB)
	cur = conn.cursor()
	cur.execute(tbl_msgs)
	conn.close()
	return 1

def add_msg(f, t, m):
	conn = sqlite3.connect(SMSDB)
	cur = conn.cursor()
	ins = """insert into msgs values(null, %s, '%s', '%s', 
		datetime());""" % (f, t, m)
	cur.execute(ins)
	conn.commit()
	rcount = cur.rowcount
	conn.close()
	return rcount

def update_sent(ids):
	conn = sqlite3.connect(SMSDB)
	cur = conn.cursor()
	strids = ",".join([str(id) for id in ids])
	upd = "update msgs set flags = 1 where id in (%s);" % (strids,)
	cur.execute(upd)
	conn.commit()
	rcount = cur.rowcount
	conn.close()
	
def get_ready_2_send():
	conn = sqlite3.connect(SMSDB)
	cur = conn.cursor()
	cur.execute("select * from msgs where flags = 0;")
	lst = cur.fetchall()
	conn.close()
	return lst

def mock_send(lst):
	ids = []
	for i in lst:
		ids.append(i[0])
		time.sleep(1.0)
	return ids


if __name__ == "__main__":
	create()
	add_msg(0, "883279496", "TestMsgText")
	lst = get_ready_2_send()
	ids = mock_send(lst)
	update_sent(ids)
