a='''i
(x+y)/2
0	2
.5 2.6361
1 3.5948
1.5 4.9678
2
'''
a=a.splitlines()[1:]
ai=-1
from itertools import *
from math import *
def input():
	global ai
	ai+=1
	return a[ai]
from sympy import *
eqn=sympify(input())
x0,y0=map(float,input().split())
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
x3,y3=map(float,input().split())
x4=float(input())
r2=lambda x,y=4: round(x+1e-15,y)
f=lambda x,y:eqn.subs({'x':x,'y':y})
yd1=r2(f(x1,y1));print("y'1",yd1)
yd2=r2(f(x2,y2));print("y'2",yd2)
yd3=r2(f(x3,y3));print("y'3",yd3)
h=x1-x0
y4=r2(y0+4*h/3*(2*yd1-yd2+2*yd3));print('y4',y4,end=' ')
yd4=r2(f(x4,y4));print("y'4",yd4)
y4=r2(y2+h/3*(yd2+4*yd3+yd4));print('y4',y4)