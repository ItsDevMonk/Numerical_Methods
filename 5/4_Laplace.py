a='''i
50 100 100 50
0 u1 u2 0
0 u3 u4 0
0 0 0 0
z
'''
b='''i
a 1 2 b
1 u1 u2 2
2 u3 u4 1
d 2 1 c
z
'''
sz=0 # 0- liebmann
aa=a.splitlines()[1:]
ai=-1
from itertools import *
from math import *
def input():
	global ai
	ai+=1
	return aa[ai]

from sympy import *
var('x t')
r2=lambda x,y=4: round(x+1e-15,y)
u=[]
while 1:
	z=input()
	if z=='z':break
	u.append(list(map(sympify,z.split())))

def dia(i,j):return (((u[i-1][j-1]+u[i-1][j+1]+u[i+1][j-1]+u[i+1][j+1])/4).subs(uv2))
def sfpf(i,j):
	z=uv if sz else uv2
	return (((u[i-1][j]+u[i][j-1]+u[i][j+1]+u[i+1][j])/4).subs(z))

z=1
uv={}
uv2={}
a=var('u1:5')
if sz:
	uv[u3]=uv2[u3]=a[1]
	uv[u4]=uv2[u4]=a[0]
	eqn=[]
	for i in range(z,z+2):uv2[u[z][i]]=sfpf(z,i)
	for i in a:zz=(i-(uv2[i]));eqn.append(zz)
	a=(solve(eqn))
	for i in a:print(i,r2(N(a[i])))
else:
	for i in a:uv[i]=0
	uv2[u4]=0
	for x in count():
		for i in range(z,z+2):
			for j in range(z,z+2):
				if x==0 and i==j==1:uv2[u[i][j]]=dia(i,j)
				else:uv2[u[i][j]]=sfpf(i,j)
		print('Iter',x)
		for i in a:print(i,r2(uv2[i]))
		print('-'*50)
		if all([abs(r2(uv[i])-r2(uv2[i]))<0.05 for i in a]):break
		uv.update(uv2)


