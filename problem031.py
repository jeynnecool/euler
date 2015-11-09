import math

'''
http://www.zhihu.com/question/21075235

use recursion to solve problem
'''

n = 200
v = [1, 2, 5, 10, 20, 50, 100, 200]
L = [0 for i in xrange(n+1)]
L[0] = 1

for i in xrange(len(v)):
	for j in xrange(v[i], len(L)):
		L[j] += L[j - v[i]]

print L
print L[n]