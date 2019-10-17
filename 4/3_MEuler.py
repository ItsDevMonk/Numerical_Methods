a='''i
y-2*x/y
0	1
.1 .2
'''
a=a.splitlines()[1:]
ai=-1
from math import *
def input():
	global ai
	ai+=1
	return a[ai]


r2=lambda x,y=4: round(x+1e-15,y)
from sympy import *
eqn=sympify(input())
f=lambda x,y:eqn.subs({'x':x,'y':y})
x,y=[],[]
_=list(map(float,(input().split())))
x.append(_[0])
y.append(_[1])


def main(i):
	h=i-x[-1]
	y.append(y[-1]+h*f(x[-1]+h/2,y[-1]+h/2*f(x[-1],y[-1])))
	x.append(i)

	print(i,r2(y[-1]))

	pass
if __name__ == '__main__':
	[main(float(i)) for i in input().split()]