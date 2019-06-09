#!/usr/bin/python

import os 
import sqlite3
from sysdefs import CONFDB


tbl_conf = """CREATE TABLE conf (key TEXT NOT NULL UNIQUE,
	val TEXT, dtc TEXT)"""


def create():
	if os.path.exists(CONFDB):
		return 0
	conn = sqlite3.connect(CONFDB)
	cur = conn.cursor()
	cur.execute(tbl_conf)
	conn.close()
	return 1

def save_key(k, v):
	conn = sqlite3.connect(CONFDB)
	cur = conn.cursor()
	delete = "delete from conf where key = '%s';" % (k,) 
	cur.execute(delete)
	conn.commit()
	ins = "insert into conf values('%s', '%s', datetime());" % (k, v)
	cur.execute(ins)
	conn.commit()
	rcount = cur.rowcount
	conn.close()
	return rcount

def read_key(k):
	conn = sqlite3.connect(SMSDB)
	cur = conn.cursor()
	sel = "select val from conf where key = '%s' limit 1;" % (k,)
	cur.execute(sel)
	#cur.rowcount
	val = cur.fetchone()[0]
	conn.close()
	return val


if __name__ == "__main__":
	pass
