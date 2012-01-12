#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys

operators = {
	'*':lambda x, y : x*y,
	'+':lambda x, y : x+y,
	'-':lambda x, y : x-y,
	}

def evaluate(line):	
	tokens = line.split()
	(a,b,c) = map(int, (tokens[0], tokens[2], tokens[4]))
	f,g = operators[tokens[1]], operators[tokens[3]]
	return max(g(f(a,b),c) , f(a, g(b,c)))
		 
def main(argv):
	with open(argv[1],'r') as fin:
		fin.readline()
		for line in fin.readlines():
			print evaluate(line.strip())
		
if __name__ == "__main__":
    main(sys.argv)
