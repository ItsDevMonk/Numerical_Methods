a='''
2
1/(x*y),2,2.4,1,1.4,4,4
sin(x+y)**.5,0,pi/2,0,pi/2,2,2
'''
verify=0
a=a.splitlines()[1:]
ai=-1


def input():
	global ai
	ai+=1
	return a[ai]

def crange(a,b,s):
	i=a

	while i<=b+s/2:
		yield i
		i+=s

from sympy import *
import numpy as np
var('x y')

r2=lambda x,y=4: round(x+1e-15,y)
def print2(f):
		for i in (f):

			i='{: .4f}'.format(r2(N(i)))
			print(i,end=' ')
		print()
def print3(x,f):
	for j in zip(x,f):

		for i in ([j[0]]+list(j[1])):
			i='{: .4f}'.format(r2(N(i)))
			print(i,end=' ')
		print()	
def print4(f):
	for j in (f):
		for i in j:
			i='{: .4f}'.format(r2(N(i)))
			print(i,end=' ')
		print()				
def main()		:
	a=input().split(',')
	f,a,b,c,d,n,m=map(sympify,a)
	h=(b-a)/n
	k=(d-c)/m
	fn=lambda x,y:f.subs({'x':x,'y':y})
	
	t1=list(crange(a,b,h))
	t2=list(crange(c,d,k))
	res=[]
	for i in t2:
		t=[]
		for j in t1:
			z=fn(i,j)
			if z is nan:z=0
			t.append(z)
		res.append(t)
	res=np.array(res)
	print('{:6}'.format(r' y\x'),end=' ')
	print2(t1)
	print3(t2,res)
	print('-'*50)
	z=0
	z+=res[[0,-1],:][:,[0,-1]].sum() 	#corner

	z+=2*res[[0,-1],:][:,1:-1].sum() 	#tb border
	z+=2*res[1:-1,[0,-1]].sum() 		#lr border

	z+=4*res[1:-1,1:-1].sum() 			#rem
	
	print(r2(N(z*h*k/4)))
	print('-'*50)
	if verify:
		print(34)
		v=(integrate(f,(x,a,b)))
		print(34)
		v=(integrate(v,(y,c,d)))
		print('V',r2(N(v)))

if __name__ == '__main__':
	for i in range(int(input())):main()