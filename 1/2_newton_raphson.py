a='''i
x**3-2*x-5=0
x*sin(x)+cos(x)
1/x-19
x**2-5
x*log(x,10)-1.2
E**x-4*x=0
3*x-cos(x)-1=0
'''
a=a.splitlines()[1:]
ai=-1

from itertools import *
from sympy import *
from math import *
import math
def input():
	global ai
	ai+=1
	return a[ai]

x=Symbol('x')
eqn=(input()).split('=')[0]
y=sympify(eqn)
ydash=(y.diff(x))
print(ydash)
f=lambda x:y.subs({'x':x})
f1=lambda x:ydash.subs({'x':x})
r2=lambda x,y=4: round(x+1e-15,y)
sign=lambda x:-1 if x<0 else 1 if x>0 else 0
xn=lambda x:(x-f(x)/f1(x)).evalf()
try:
	i=0
	z=f(i)
	if z==zoo:raise ValueError
except ValueError:
	i=1
print(f(i))
s=sign(f(i))

z=0
if z:
	a=0.05
else:
	for i in count(i+1):
		_=f(i)
		s1=sign(_)
		if s1!=s or s1==0:
			a,b=(i-1,i);break
		s=s1

for i in count(1):
	z=(xn(a))
	print(i,r2(z))
	if r2(a)==r2(z) :break
	a=z