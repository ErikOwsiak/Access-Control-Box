#!/usr/bin/python

import os
import time 
import smsdb
import confdb


def main():
	smsdb.create()
	confdb.create()


if __name__ == "__main__":
	main()
