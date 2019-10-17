a='''i
x**2+y**2-2
0	1
-.1  
'''

a=a.splitlines()[1:]
ai=-1
from itertools import *
from math import *
def input():
	global ai
	ai+=1
	return a[ai]

def mtype(yt):
	return str(type(yt)).split('.')[-1][0]
def mydif(eqn,ii):
	z=[]
	if mtype(eqn)=='A':
		for i in eqn.args:
			if y in i.atoms(Symbol) :
				yt=Mul(*[j for j in i.args if j.has(y)]) if type(i)==Mul else i
				yt2={'S':Add(1),'D':Add(1)}
				t=str(type(yt)).split('.')[-1][0]
				if t=='M': 
					for j in yt.args:
						t=str(type(j)).split('.')[-1][0]
						yt2[t]=j
					_=yt2['S'].diff(y)*Derivative(y)*yt2['D']+yt2['D'].diff(y)*yt2['S']
				elif t=='D':_=_=yt.diff(y)
				else:_=_=yt.diff(y)*Derivative(y)
				u=i/yt
				if (u.has(x)):
					_+=yt*u.diff(x)
				else:_*=u
				
				
			else:_=i.diff(x)
			z.append(_)
	else:
		s= x if (eqn.has(x)) else y		
		z=[eqn.diff(s)]
	return Add(*z)

r2=lambda x,y=4: round(x+1e-15,y)
from sympy import *
eqn=sympify(input())
_=list(map(int,(input().split())))
xv=(_[0])
yv=(_[1])
var('x y')
import re
ds=r"Derivative\((.*?)\)"
yy={}
yy2={}
d="y1d"
var(d)
yy2[d]=str(eqn)
yy["y'"]=str(eqn)
for i in range(1,3):
	eqn=(mydif(eqn,1))
	_=str(eqn)
	_2=_
	while 1:
		z=re.search(ds,_)
		if not z:break
		c=(z[0].count('y'))-1
		t=_
		t2=_2
		_=re.sub(ds,'y'+"'"*c,t,1)
		_2=re.sub(ds,'y{}d'.format(c),t2,1)
	d='y'+"'"*(i+1)
	d1='y{}d'.format(i+1)
	var(d1)
	yy[d]=_
	yy2[d1]=_2
dv={}
dv['x']=xv
dv['y']=yv

var('h')
ans=''
for i in range(4):
	ans+='+(y{0}d*h**{0:}/factorial({0:}))'.format(i)

ans=sympify(ans.replace('y0d','y'))
for i in yy:print(i,'=>',yy[i])
print('-'*50)
def main(ii):
	
	for i in yy2:
		t=N(sympify(yy2[i])).subs(dv)
		dv[i]=t
	y=r2(ans.subs(dv))
	dv['x']+=dv['h']
	dv['y']=y
	if r2(dv['x'])!=ii:main(ii);return
	print(ii,y)

if __name__ == '__main__':
	a=[(float(i)) for i in input().split()]
	dv['h']=a[0]-xv
	for i in a:main(i)
	pass