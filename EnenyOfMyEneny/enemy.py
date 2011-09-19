#!/usr/bin/python
import sys
from collections import defaultdict
with open(sys.argv[1],'r') as f: 
	l=f.readline().split()
	E=defaultdict(set)
	for _ in range(0, int(l[1])):
		(x,y)=tuple(f.readline().split())
		E[y].add(x)
		E[x].add(y)
	f.readline()
	for n in f.readlines():
		n=n.strip()
		print len(set([k for e in E[n] for k in E[e]-set([n])-E[n]]))