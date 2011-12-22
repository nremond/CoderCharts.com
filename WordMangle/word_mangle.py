#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys

def main(argv):

	with open(argv[1],'r') as fin:
		words = fin.readline().strip().split()
		
		for w in words[::-1]:
			print w,
		print ""
		
		for w in words:
			print w[::-1],
		print ""
	
	
if __name__ == "__main__":
    main(sys.argv)
