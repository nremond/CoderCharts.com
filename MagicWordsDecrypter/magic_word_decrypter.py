#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import string


def get_key(s):
	if len(s) <= 3 :
		return s
	else :
		first = s[0]
		last = s[-1:]	
		middle = list(s[1:-1])
		middle.sort()
		return first + "".join(middle) + last


def main(argv):
	if len(argv) != 3 :
		print argv[0] + " takes exactly 2 arguments"
		print argv
		exit(0)
	
	message_filename = argv[1]
	dic_filename = argv[2]
	
	dic = dict()
	
	with open(dic_filename,'r') as dic_file :
		for line in dic_file:
			word = line.lower().strip()
			key = get_key(word)
			value = dic.get(key,None) 
			if value is None or word < value :
				dic[key] = word
	
	with open(message_filename,'r') as message_file :
		for line in message_file:
			for word in line.strip().split():
				print dic[get_key(word)],
			print ""
		
		
if __name__ == "__main__":
    main(sys.argv)			
			
	