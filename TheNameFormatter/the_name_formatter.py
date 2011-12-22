import sys;a=open(sys.argv[1]).read().splitlines()
for l in a[1:]:
	p=l.split();s=len(p);
	if s>1:print p[0].capitalize(),
	if s>2:print p[1][-1]=='.' and p[1].upper() or p[1].lower(),
	print p[-1].upper()