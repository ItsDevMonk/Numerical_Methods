
a='''
0.1003 0.1511 0.2027 0.2553 0.3093
0.10 0.15 0.20 0.25 0.30 
0.12 0.2875
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
print(y)
t=len(y)
r2=lambda x,y=4: round(x+1e-15,y)
import numpy as np
import sympy as sp
from math import factorial
# 2x3 -6x2+3x+3
def main(x1):
	x1=sp.sympify(x1)
	s=str(type(x1)).split("'")[1].split('.')[-1]
	s1=s in ['Integer','Float']
	z=sum([y[i]*np.prod([(x1-x[j])/(x[i]-x[j]) for j in range(t) if i!=j]) for i in range(t)])
	if s1:z=r2(z)

	else:z=sp.simplify(z)
	print(z)

if __name__ == '__main__':
	[main(i) for i in input().split()]