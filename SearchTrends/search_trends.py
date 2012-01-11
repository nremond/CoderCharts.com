#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
from collections import defaultdict

def main(argv):
	occurences = defaultdict(int)
	
	with open(argv[1],'r') as fin:
		for line in fin.readlines():
			line = line.strip()
			occurences[line] -= 1
	
	l = sorted([(v,k) for k,v in occurences.iteritems()])
		
	for i in xrange(0,min(10, len(l))):
		print -l[i][0], l[i][1]
	
if __name__ == "__main__":
    main(sys.argv)
