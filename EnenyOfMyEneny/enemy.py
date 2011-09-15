#!/usr/bin/python

import sys


def main(argv):

	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)
		
	with open(argv[1],'r') as f: 
		(n, p) = tuple(map(int, f.readline().split()))

		enemies = {}
		for _ in range(0, p):
			(a,b) = tuple(f.readline().split())
			if a in enemies :
				enemies[a].append(b)
			else :
				enemies[a] = [b]
			if b in enemies :
				enemies[b].append(a)
			else :
				enemies[b] = [a]	
		
		names = []
		for _ in range(0, int(f.readline())):
			names.append(f.readline().strip())
	
	
		for name in names : 
			my_enemies = enemies[name]
			
			# my enemies enemies
			friends = {}
			for e in my_enemies :
				for f in enemies[e] :
					friends[f] = 0
			
			# remove my enemies
			for e in my_enemies :
				if e in friends :
					friends.pop(e)
			
			if name in friends :
				friends.pop(name)
			
			print len(friends.keys())
	
# -- The following code executes upon command-line invocation
if __name__ == "__main__": 
	main(sys.argv)
	