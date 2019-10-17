a='''
sin(x)/x,0,pi,6
1/(1+x**2),-1,1,8
x*E**x,0,1,4
1/(1+x**2),1,2,5
'''
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
x=Symbol('x')
r2=lambda x,y=4: round(x+1e-15,y)
def print2(f):
		for k,i in enumerate(f):
			i='{: .4f}'.format(r2(N(i)))
			print(i,end=' ')
		print()
def main()		:
	f,a,b,n=map(sympify,input().split(','))
	h=(b-a)/n
	fx=lambda x:f.subs({'x':x})
	
	res=[]
	r=list(crange(a,b,h))
	for i in r:
		z=fx(i)
		if z is nan:z=0
		res.append(z)
	print2(r)
	print2(res)
	# print('-'*50)
	z=(res[0]+res[-1])+2*sum(res[1:-1])
	print(r2(N(z*h/2)))
	print('-'*50)

if __name__ == '__main__':
	for i in range(4):main()