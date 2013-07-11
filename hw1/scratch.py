import itertools, sys
from GF2 import one
from math import sqrt

"""
a = [one,one,0,0,0,0,0]
b = [0,one,one,0,0,0,0]
c = [0,0,one,one,0,0,0]
d = [0,0,0,one,one,0,0]
e = [0,0,0,0,one,one,0]
f = [0,0,0,0,0,one,one]

a = [one,one,one,0,0,0,0]
b = [0,one,one,one,0,0,0]
c = [0,0,one,one,one,0,0]
d = [0,0,0,one,one,one,0]
e = [0,0,0,0,one,one,one]
f = [0,0,0,0,0,one,one]

ll = [a,b,c,d,e,f]
#u = [0,0,one,0,0,one,0]
#u = [0,one,0,0,0,one,0]
#u = [0,0,one,0,0,one,0]
u = [0,one,0,0,0,one,0]

print(dotprod([1,0],[5,4321]))
print(dotprod([0,1],[12345,6]))
print(dotprod([-1,3],[5,7]))
print(dotprod([-1*(sqrt(2)/2), sqrt(2)/2], [sqrt(2)/2, -1*(sqrt(2)/2)]))
"""

def addn(v, w): return [v[i]+w[i] for i in range(len(v))]
def subn(v, w): return [v[i]-w[i] for i in range(len(v))]
def multn(alpha, v): return [alpha*x for x in v]
def addAll(arr):
	res = [0]*len(arr[0])
	for x in arr:
		res = addn(res, x)
	return res
def match(ll):
	for x in range(2,len(ll)):
		combs = list(itertools.combinations(ll,x))
		for y in combs:
			res = addAll(y)
			if res == u:
				return y
	return set()
def dotprod(u,v): return sum([u[x]*v[x] for x in range(len(v))])

def findvec(): 
	opts = list(itertools.product([one,0], repeat=4))
	for x in opts:
		if dotprod([one,one,0,0],x) != one:
			continue
		if dotprod([one,0,one,0],x) != one:
			continue
		if dotprod([one,one,one,one],x) != one:
			continue
		print(x)
		sys.exit()
