a='''i
x**2+y**2-2
-0.1 1.09
0	1
0.1 0.89
0.2 0.7608
0.3
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
yd0=r2(f(x0,y0));print("y'0",yd0)
yd1=r2(f(x1,y1));print("y'1",yd1)
yd2=r2(f(x2,y2));print("y'2",yd2)
yd3=r2(f(x3,y3));print("y'3",yd3)
h=x1-x0
y4=r2(y3+h/24*(55*yd3-59*yd2+37*yd1-9*yd0));print('y4',y4,end=' ')
yd4=r2(f(x4,y4));print("y'4",yd4)
y4=r2(y3+h/24*(9*yd4+19*yd3-5*yd2+yd1));print('y4',y4)