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
cum=lambda y,j: [((y[1]-y[0])/(x[i+j+1]-x[i])) for i,y in enumerate(zip(y,y[1:]))]

t=len(y)
y=[y]
for i in range(t-1):
	y.append(cum(y[i],i))
	print(y[-1])

import numpy as np
import sympy as sp
from math import factorial

def main(x1):
	x1=sp.sympify(x1)
	s=str(type(x1)).split("'")[1].split('.')[-1]
	s1=s in ['Zero','Integer','Float']
	z=sum((y[i][0])*(np.prod([x1-x[i] for i in range(i)])) for i in range(t))
	if s1:z=r2(z)
	else:z=sp.simplify(z)
	print(z)

if __name__ == '__main__':
	[main(i) for i in input().split()]