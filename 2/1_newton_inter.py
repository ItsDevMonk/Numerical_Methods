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
	print(y[-1])

import numpy as np
# import sympy as sp
from math import factorial

def main(x1):
	# tt=x1.split('$')
	# x1=sp.sympify(tt[0])
	# s=str(type(x1)).split("'")[1].split('.')[-1]
	# s1=s in ['Integer','Float']
	# print(s1)
	s1=True;x1=float(x1)
	if (not s1 and tt[1]=='f') or (x1-x[0]<x[-1]-x1):
		print('forward')
		u=(x1-x[0])/abs(x[0]-x[1])
		z=sum((y[i][0])*(np.prod([u-i for i in range(i)]))/factorial(i) for i in range(t))
	else:
		print('backward')
		v=(x1-x[-1])/abs(x[0]-x[1])
		z=sum((y[i][-1])*(np.prod([v+i for i in range(i)]))/factorial(i)**i for i in range(t))
		
	if s1:z=r2(z)
	else:z=sp.simplify(z)
	print(z)
if __name__ == '__main__':
	[main((i)) for i in input().split()]
