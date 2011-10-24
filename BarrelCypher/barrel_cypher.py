import sys
t=list("abcdefghijklmnopqrstuvwxyz")
l=open(sys.argv[1]).readlines()
for n in range(int(l[0])):
	K=[int(j) for j in list(l[2*n+1][:-1])]
	K=K+K[::-1]
	S=l[2*n+2].strip()
	b=""
	i=0
	for s in S:
		if s==' ': b+=s
		else:
			b+=t[(t.index(s)-K[i]+26)%26]
			i=(i+1)%len(K)
	print b