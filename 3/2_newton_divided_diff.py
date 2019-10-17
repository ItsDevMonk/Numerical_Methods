a='''
1 2 4 8 10
0 1 5 21 27
1
4
'''
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]

import numpy as np
from sympy import *
from math import factorial

x=list(map(float,input().split()))
y=list(map(float,input().split()))
print(x)
print()
print(y)
r2=lambda x,y=4: round(x+1e-15,y)
cum=lambda y,j: [Rational((y[1]-y[0]),(x[i+j+1]-x[i])) for i,y in enumerate(zip(y,y[1:]))]

t=len(y)
y=[y]
for i in range(t-1):
	y.append(cum(y[i],i))
	if(any(y[-1])):print(y[-1])



def main(x1,n):
	x1=sympify(x1)
	s=str(type(x1)).split("'")[1].split('.')[-1]
	x2=sympify('x')
	z=sum((y[i][0])*(np.prod([x2-x[i] for i in range(i)])) for i in range(t))
	for i in range(n):
		z1=r2(z.diff(x2,i+1).subs({'x':x1}))
		print(z1)

if __name__ == '__main__':
	n=int(input())
	[main(i,n) for i in input().split()]