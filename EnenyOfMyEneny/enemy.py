import sys
with open(sys.argv[1],'r') as f: 
	l = f.readline().split()
	ee = {}
	for _ in range(0, int(l[1])):
		(x,y) = tuple(f.readline().split())
		def up(a,b):
			if a in ee: ee[a].append(b)
			else: ee[a] = [b]
		up(x,y)
		up(y,x)
	for n in [f.readline().strip() for _ in range(0, int(f.readline()))]: 
		en = ee[n]
		friends = {}
		for e in en:
			for f in ee[e]:
				if f!=n and f not in en : friends[f] = 0		
		print len(friends.keys())