import sys,string
a=string.ascii_lowercase
t=dict(enumerate(a))
l=open(sys.argv[1]).readlines()
for n in range(int(l[0])):
	K=[int(j) for j in list(l[2*n+1].strip())]
	K=K+K[::-1]
	S=l[2*n+2].strip()
	b=""
	i=0
	for s in S:
		#(a.index(c)+1)%26
		if s==' ':
			b+=' '
		else:
			print "(%s, %i, %i)" (s, a.index(s), K[i])
		
			t[(a.index(s)+K[i])%26]
			b+= "(%s, %s)" % (s, t[(a.index(s)+K[i])%26])
			i+=1
			i=i%len(K)
	print b

