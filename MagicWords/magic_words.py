#!/usr/bin/python

import sys
import string
from collections import defaultdict
	
def build_mix(dic, sorted_letters) :
	if len(sorted_letters) > 1 : 
		a = sorted_letters.pop(0)
		z = sorted_letters.pop(-1)

		dic[a].append(z)
		dic[z].append(a)
		if len(sorted_letters) > 0 : 
			build_mix(dic, sorted_letters)
	else :
		l = sorted_letters.pop()
		dic[l].append(l)
	
	
def mix_it(s):
	if len(s) <= 3 :
		return s
	else :
		first = s[0]
		last = s[-1]	
		middle = list(s[1:-1])
		buff = list(middle)
		buff.sort()
		
		mix = defaultdict(list)
		build_mix(mix, buff)
		
		new = list()
		for letter in middle :
			new.append(mix[letter].pop())	
		
		return first + "".join(new) + last


def main(argv):
	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)
	
	with open(argv[1],'r') as dic_file :
		for line in dic_file:
			for word in line.lower().strip().split() :
		 		print mix_it(word),
			print ""
	
	
if __name__ == "__main__":
    main(sys.argv)			
			
	