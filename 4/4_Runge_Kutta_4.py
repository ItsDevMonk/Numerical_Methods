a='''i
(x+y)/2
0	2
.5 1 1.5
'''
a=a.splitlines()[1:]
ai=-1
from itertools import *
from math import *
def input():
	global ai
	ai+=1
	return a[ai]

r2=lambda x,y=4: round(x+1e-15,y)
from sympy import *
v=True*0
eqn=sympify(input())
xs=Symbol('x')
ys=Symbol('y')
f=lambda x,y:eqn.subs({'x':x,'y':y})
def print2(**k):
	for i,j in k.items():print(i,r2(N(j)))
def main(x,y,h,p):
	k1=h*f(x,y)
	k2=h*f(x+h/2,y+k1/2)
	k3=h*f(x+h/2,y+k2/2)
	k4=h*f(x+h,y+k3)
	dy=(k1+2*k2+2*k3+k4)/6
	
	if p and v:print2(k1=k1,k2=k2,k3=k3,k4=k4,dy=dy)
	return (y+dy)

if __name__ == '__main__':
	x,y=map(float,(input().split()))
	xv=list(map(float,(input().split())))
	i=0
	h=xv[i]-x
	while x<xv[-1]:
		t=r2(x+h)
		p=t in xv
		y1=main(x,y,h,p)
		x,y=t,y1
		i+=1

		if p:
			print(xv[i-1],r2(y1))
			if v:print("="*50)