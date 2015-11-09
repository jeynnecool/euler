import math
import sys

#set recursion limit to larger number
#!must
sys.setrecursionlimit(10000)

def fibo(i, val=1, prev=0):
	if i == 0:
		return prev
	elif i == 1:
		return val
	else:
		return fibo(i-1, val+prev, val)


n = 1
lenth = 1
while True:
	f = fibo(n)
	if len(str(f)) >= 1000:
		print("#%d: %d" % (n, f))
		exit()
	n += 1


'''
Although there is a better method to calculate the number
no need to use recursion at all

http://mortada.net/fibonacci-numbers-in-python.html
'''