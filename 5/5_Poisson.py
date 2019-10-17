a='''i
-10*(x**2+y**2+10)
1
0 0 0 0
0 u1 u2 0
0 u3 u4 0
0 0 0 0
z
'''


b='''i
0
1
a {0} {1} b
{0} u1 u2 {2}
{1} u3 u4 {3}
d {2} {3} c
z
'''.format(2,4,6,8)
sz=0 # symmetry
solve=1 # 0 -liebmann 
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
eqn_=sympify(input())
h=int(input())
def f(x,y):x,y=y,lu-x-1;z=eqn_.subs({'x':x,'y':y});return z
r2=lambda x,y=4: round(x+1e-15,y)
u=[]
while 1:
	z=input()
	if z=='z':break
	u.append(list(map(sympify,z.split())))
lu=len(u)
def dia(i,j):return (((u[i-1][j-1]+u[i-1][j+1]+u[i+1][j-1]+u[i+1][j+1])/4).subs(uv2))
def sfpf(i,j):
	z=uv if solve else uv2
	r= (((u[i-1][j]+u[i][j-1]+u[i][j+1]+u[i+1][j])/4-h**2/4*f(h*i,h*j)).subs(z))
	return r

z=1
uv={}
uv2={}
a=var('u1:5')
if solve:
	sk=[]
	if sz in [1,3]:uv[u3]=uv2[u3]=a[1];sk.append(u3)
	if sz in [2,3]:uv[u4]=uv2[u4]=a[0];sk.append(u4)
	eqn=[]
	for i in range(z,z+2):
		for j in range(z,z+2):
			if u[i][j] in sk:continue
			uv2[u[i][j]]=sfpf(i,j)
	for i in a:zz=(i-(uv2[i]));eqn.append(zz)
	a=(solve(eqn))
	print(eqn)
	for i in a:print(i,r2(N(a[i])))
else:
	for i in a:uv[i]=0
	uv2[u4]=0
	for x in count():
		for i in range(z,z+2):
			for j in range(z,z+2):
				if x==0 and i==j==1:uv2[u[i][j]]=dia(i,j)
				else:
					uv2[u[i][j]]=sfpf(i,j)
		print('Iter',x)
		for i in a:print(i,r2(uv2[i]))
		print('-'*50)
		if all([abs(r2(uv[i])-r2(uv2[i]))<0.05 for i in a]):break
		uv.update(uv2)


