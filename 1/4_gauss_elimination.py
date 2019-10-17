a='''i
1 1 2 4
3 1 -3 -4
2 -3 -5 -5
''' 
ai='''i
2 1 3
7 -3 4
'''
n=3
# a=ai;n=2
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]

from itertools import *
from pprint import pprint
import math
import numpy as np
r2=lambda x,y=4: round(x+1e-15,y)
r=[]
for i in range(len(a)):
	r.append(list(map(int,input().split())))

r=np.array(r)
def ggcd(x,y):
	z=math.gcd(x,y)
	if x<0:z*=-1
	return(x//z,-y//z)

for i in range(n):
	zz=''
	if i!=0:
		z=(ggcd(r[0][0],r[i][0]))
		r[i]=(z[0]*r[i]+z[1]*r[0])
		zz=('R{0} -> {2}R{0} {3:=+3}R{1}'.format(i+1,1,*z).replace('1R','R'))
	print(('|{:{s}}'+(' {:{s}}'*(n))+'| ').format(*r[i],s=4)+zz)

print()
for i in range(n):
	zz=''
	if i>1:
		z=(ggcd(r[1][1],r[i][1]))
		r[i]=(z[0]*r[i]+z[1]*r[1])
		zz=('R{0} -> {2}R{0} {3:=+3}R{1}'.format(i+1,1,*z).replace('1R','R'))
	print(('|{:{s}}'+(' {:{s}}'*(n))+'| ').format(*r[i],s=4)+zz)



v='x y z'.split()
b=[]
b.append(r[n-1][n]/r[n-1][n-1])
b.append((r[n-2][n]-r[n-2][n-1]*b[0])/r[n-2][n-2])
if n>2:b.append((r[0][3]-r[0][2]*b[0]-r[0][1]*b[1])/r[0][0])
for i in range(n):
	print('{} ={:5g}'.format(v[i],b[n-i-1]))
