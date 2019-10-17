a='''i
10 -2 3 23
2 10 -5 -33
3 -4 10 41
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
from math import gcd
from functools import reduce
import operator

r2=lambda x,y=4: round(x+1e-15,y)
r=[]
for i in range(len(a)):
	r.append(list(map(int,input().split())))

r=np.array(r)
def ggcd(x,y):
	z=gcd(x,y)
	if x<0:z*=-1
	return(x//z,-y//z)



def g(i):
	z=reduce(gcd,r[i])
	if r[i][i]*z<0:z*=-1
	r[i]//=z
	return z
def v():
	global zz
	if not any(zz):return
	for i in range(n):
		print(('|{:{s}}'+(' {:{s}}'*(n))+'| ').format(*r[i],s=4)+zz[i])
	print()
	zz=['']*3

zz=['Begin']*3

# v()
zz=['']*3
def bb(x,s=operator.lt):
	for i in range(n):
		if s(i,x):
			z=(ggcd(r[x][x],r[i][x]))
			r[i]=(z[0]*r[i]+z[1]*r[x])
			zz[i]=('{2}R{0} {3:=+3}R{1}'.format(i+1,1,*z).replace('1R','R'))
			b=g(i)
			if b!=1:zz[i]='({})/{}'.format(zz[i],b)
			zz[i]='R{0} -> '.format(i)+zz[i]
	v()


		
bb(0,operator.gt)
bb(1,operator.gt)
bb(2)
bb(1)


v='x y z'.split()
for i in range(n):
	print('{} ={:5g}'.format(v[i],r[i][-1]))
