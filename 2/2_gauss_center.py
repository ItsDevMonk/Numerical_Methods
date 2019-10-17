a='''
0.10 0.15 0.20 0.25 0.30 
0.1003 0.1511 0.2027 0.2553 0.3093
0.12 0.28
'''
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]

x=list(map(float,input().split()))
y=list(map(float,input().split()))
print(x)
print()
print(y)
r2=lambda x,y=4: round(x+1e-15,y)
cum=lambda y: [r2(y-x) for x,y in zip(y,y[1:])]

t=len(y)
y=[y]
for i in range(t-1):
	y.append(cum(y[i]))
	# print(y[-1])

import sympy as sp
import numpy as np
from math import factorial
cv=[x for i in range(t) for x in (i,-i)]
def main(x1):
	for i in range(t):
		if (x1<x[i]):
			z=i-1
			break
	if  (x1-x[z]<=x[z+1]-x1):
		print('forward')
		u=(x1-x[z])/abs(x[0]-x[1])
		zz=sum([(y[i][(z-(i)//2)%(t-i)]*np.prod([(u-cv[i+1]) for i in range(i) ])/factorial(i)) for i in range(t)])
		

	else:
		z+=1
		print('backward')
		u=(x1-x[z])/abs(x[0]-x[1])
		zz=sum([(y[i][(z-(i+1)//2)%(t-i)]*np.prod([(u--cv[i+1]) for i in range(i) ])/factorial(i)) for i in range(t)])

	print(r2(zz))
if __name__ == '__main__':
	[main(float(i)) for i in input().split()]
