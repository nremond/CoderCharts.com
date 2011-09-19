#!/usr/bin/python
import sys
l=open(sys.argv[1],'r').readlines()
p=int(l[0].split()[1])
E={}
def a(x,y):	E.setdefault(y, set()).add(x)
for (x,y) in [s.split() for s in l[1:p+1]]:
	a(x,y)
	a(y,x)
for n in l[p+2:]:
	n=n.strip()
	print len(set([k for e in E[n] for k in E[e]-set([n])-E[n]]))