a='''i
x*sin(x)+cos(x)
x*log10(x)-1.2=0
'''
a=a.splitlines()[1:]
ai=-1

from itertools import *
from math import *
import math
def input():
	global ai
	ai+=1
	return a[ai]

eqn=(input()).split('=')[0]
f=lambda x:eval(eqn)
r2=lambda x,y=4: round(x+1e-15,y)
sign=lambda x:-1 if x<0 else 1 if x>0 else 0
i=1 if 'log' in eqn else 0
s=sign(f(i))
for i in count(i+1):
	_=f(i)
	s1=sign(_)
	if s1!=s or s1==0:
		a,b=(i-1,i);break
	s=s1
xn=lambda a,b:(a*f(b)-b*f(a))/(f(b)-f(a))
print(a,b)
# a,b=2.5,3
for i in count(1):
	z=(xn(a,b))
	print(i,r2(z))
	if r2(a)==r2(z) :break
	a=z