#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import string

def main(argv):
	
	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)
	
	with open(argv[1],'r') as fin:
		total_age = long(string.atoi(fin.readline().rstrip()))
		b1_age = long(string.atoi(fin.readline().rstrip()))
		b2_age = long(string.atoi(fin.readline().rstrip()))

		print (total_age - b1_age - b2_age) / 3L
		
if __name__ == "__main__":
    main(sys.argv)