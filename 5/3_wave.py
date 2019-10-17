a='''i
x**2*(5-x)
0 0
5 0
Rational(5,4)
1
4
'''
'''
x,0
x1,t
xn,t
m
h
a
'''
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
def r2(x,y=4):
	return  round(x+1e-15,y)
r1=sympify(input())
x1,fc=map(sympify,(input().split()))
xn,lc=map(sympify,(input().split()))
n=xn-x1
m=sympify(input())
h=sympify(input())
av=float(input())
if (int(av)==av):av=int(av)
k=h/av

x=n/h+1
if (int(x)==x):x=int(x)
t=m/k+1
if (int(t)==t):t=int(t)

a=[[0 ] * x for i in range(t)]
xv=[x1+h*i for i in range(x)]
tv=[k*i for i in range(t)]
for i in range(1,x):
	a[0][i]=r1.subs({'x':xv[i],'t':tv[0]})
for i in range(0,t):
	a[i][0]=fc.subs({'x':xv[0],'t':tv[i]})
for i in range(0,t):
	a[i][-1]=lc.subs({'x':xv[-1],'t':tv[i]})



for i in range(1,t):
	for j in range(1,x-1):
		a[i][j]=(((a[i-1][j-1]+a[i-1][j+1])))
		if i>1:a[i][j]-=a[i-2][j]
		else:a[i][j]/=2
import plotly as py
import plotly.graph_objs as go
g=[list(map(lambda x:str(r2(x)),a)) for a in a]
tv=list(map(lambda x:str((x)),tv))
g=list(zip(*g))
data =[go.Table(
    header=dict(values=[r't\x']+list(map(lambda x:str(r2(x)),xv))),
    cells=dict(values=[tuple(tv)]+g))]


py.offline.plot(data, filename = 'Table.html')
# for k,i in enumerate(a):print(tv[k],i)

