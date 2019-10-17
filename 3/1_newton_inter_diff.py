a='''
31 32 33 34
.6008 .6249 .6494 .6745
1
31
'''
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]


r2=lambda x,y=4: round(x+1e-15,y)

x=list(map(float,input().split()))
y=list(map(float,input().split()))
print(x)
print('')
print(y)
cum=lambda y: [r2(y-x) for x,y in zip(y,y[1:])]



t=len(y)
y=[y]
for i in range(t-1):
	y.append(cum(y[i]))
	if(any(y[-1])):print(y[-1])


import numpy as np
from sympy import *
from math import factorial
xv=Symbol('x')
def main(x1,n):
	tt=x1.split('$')
	x1=sympify(tt[0])
	s=str(type(x1)).split("'")[1].split('.')[-1]
	s1=s in ['Zero','Integer','Float']
	x2=sympify('x')
	h=abs(x[0]-x[1])
	us=Symbol('u')
	if (not s1 and tt[1]=='f') or (x1-x[0]<x[-1]-x1):
		print('forward')
		u=(x2-x[0])/h
		z=sum(y[i][0]*simplify(sympify(np.prod([us-i for i in range(i)])).diff(us))/factorial(i) for i in range(t))
	else:
		print('backward')
		z=sum(y[i][-1]*simplify(sympify(np.prod([us+i for i in range(i)])).diff(us))/factorial(i) for i in range(t))
		u=(x2-x[-1])/h
	for i in range(n):
		z1=r2(z.diff(us,i).subs({'u':u,'x':x1})/h**(i+1));
		print(z1)
if __name__ == '__main__':
	n=int(input())
	[main(i,n) for i in input().split()]
