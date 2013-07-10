import itertools, sys
from GF2 import one

# 4
"""
a = [one,one,0,0,0,0,0]
b = [0,one,one,0,0,0,0]
c = [0,0,one,one,0,0,0]
d = [0,0,0,one,one,0,0]
e = [0,0,0,0,one,one,0]
f = [0,0,0,0,0,one,one]

"""

a = [one,one,one,0,0,0,0]
b = [0,one,one,one,0,0,0]
c = [0,0,one,one,one,0,0]
d = [0,0,0,one,one,one,0]
e = [0,0,0,0,one,one,one]
f = [0,0,0,0,0,one,one]

ll = [a,b,c,d,e,f]

def addn(v, w): return [v[i]+w[i] for i in range(len(v))]
def subn(v, w): return [v[i]-w[i] for i in range(len(v))]
def multn(alpha, v): return [alpha*x for x in v]
def addAll(arr):
	res = [0]*len(arr[0])
	for x in arr:
		res = addn(res, x)
	return res

#u = [0,0,one,0,0,one,0]
#u = [0,one,0,0,0,one,0]
#u = [0,0,one,0,0,one,0]
u = [0,one,0,0,0,one,0]

for x in range(2,len(ll)):
	combs = list(itertools.combinations(ll,x))
	for y in combs:
		res = addAll(y)
		if res == u:
			print(y)
			sys.exit()
print('none')
