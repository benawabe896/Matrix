import itertools
from vec import Vec
from mat import Mat
from matutil import *
from vecutil import *
from bitutil import *
from GF2 import one

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""

G = listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]])
I = listlist2mat([[one,0,0,0],[0,one,0,0],[0,0,one,0],[0,0,0,one]])
GR = listlist2mat([[0,0,one,0,one,0,one],[0,0,one,0,0,one,one],[0,0,one,0,0,0,0],[0,0,0,0,one,one,one,one],[0,0,0,0,one,0,0],[0,0,0,0,0,one,0],[0,0,0,0,0,0,one]])

Gcols = mat2coldict(G)
Irows = mat2rowdict(I)
allcomb   = list(itertools.product([0, one], repeat=7))

#print(G)
#print(I)
#print(GR)
#print(Gcols[0])
#print(Irows[0])
#print(list(allcomb[0]))
"""
V1 = list2vec(list(allcomb[0]))
for x in allcomb:
	v = list2vec(list(x))
	if v*G == Irows[0]:
		for x1 in allcomb:
			v1 = list2vec(list(x1))
			if v1*G == Irows[1]:
				for x2 in allcomb:
					v2 = list2vec(list(x2))
					if v2*G == Irows[2]:
						for x3 in allcomb:
							v3 = list2vec(list(x3))
							if v3*G == Irows[3]:
								test = listlist2mat([list(x),list(x1),list(x2),list(x3)])
								if test*G == I and G*test == GR:
									print(test)
									break

"""
#print(V1*G)
#print(allcomb[0] * Gcols[0])

"""
       0 1   2 3   4   5   6
     -----------------------
 0  |  0 0   0 0   0   0 one
 1  |  0 0   0 0   0 one   0
 2  |  0 0   0 0 one   0   0
 3  |  0 0 one 0   0   0   0
"""

## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0,0,one,one,0,0,one]

## Task 2
# Express your answer as an instance of the Mat class.
R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (3, 0): 0, (0, 4): 0, (1, 4): 0, (2, 6): 0, (0, 5): 0, (2, 1): 0, (2, 5): 0, (2, 0): 0, (1, 0): 0, (3, 5): 0, (0, 1): 0, (0, 2): 0, (3, 3): 0, (0, 6): one, (3, 4): 0, (3, 1): 0, (1, 6): 0, (1, 1): 0, (1, 5): one, (3, 6): 0, (2, 2): 0, (1, 3): 0, (2, 3): 0, (0, 3): 0, (2, 4): one})

## Task 3
# Create an instance of Mat representing the check matrix H.
H = Mat(({0, 1, 2}, {0, 1, 2, 3, 4, 5, 6}), {(0, 1): 0, (1, 2): one, (2, 4): one, (0, 0): 0, (2, 6): one, (1, 5): one, (2, 2): one, (1, 1): one, (1, 4): 0, (0, 2): 0, (0, 6): one, (1, 3): 0, (0, 5): one, (2, 1): 0, (2, 5): 0, (0, 4): one, (2, 3): 0, (1, 6): one, (1, 0): 0, (2, 0): one, (0, 3): one})

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    d = sum([0 if e[i] == 0 else 2**(2-i) for i in {0,1,2}])
    e = Vec({0,1,2,3,4,5,6},{})
    if d > 0:
	    e[d-1] = one
    return e

#res = find_error(Vec({0,1,2}, {0:one}))
#res2 = find_error(Vec({0,1,2}, {2:one}))
#res2 = find_error(Vec({0,1,2}, {0:one, 1:one}))
#res3 = find_error(Vec({0,1,2}, {1:one, 2:one}))
#print(res)
#print(res2)
#print(res3)

## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = Vec({0, 1, 2, 3, 4, 5, 6},{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: one})
code_word = Vec({0, 1, 2, 3, 4, 5, 6},{0: one, 1: 0, 2: one, 3: one, 4: 0, 5: one, 6: 0})
original = Vec({0, 1, 2, 3},{0: 0, 1: one, 2: 0, 3: one})

## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    s = mat2coldict(S)
    return coldict2mat({x:find_error(col) for x,col in s.items()})

#s = ''.join([chr(i) for i in range(256)])
#print(s)
#print(str2bits(s))
#print(bits2str(str2bits(s)))


S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
res = find_error_matrix(S)
des = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
#print(S)
#print(res)
#print(des)

## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
P = bits2mat(str2bits(s))
E = noise(P, 0.02)
#print(bits2str(mat2bits(E+P)))
#cols = mat2coldict(P)
#print([G*col for p,col in cols.items()])
#print(G*P)

## Task 7
C = G*P
bits_before = 896
bits_after = 1568


## Ungraded Task
CTILDE = None

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    syn = H * A
    e = find_error_matrix(syn)
    c = e + A
    return c


A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
res = correct(A)
#print(A)
des = Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
#print(des)
#print(res)

cor = correct(C)
#print(bits2str(mat2bits(R*cor)))



