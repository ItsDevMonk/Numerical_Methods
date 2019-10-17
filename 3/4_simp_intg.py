a='''
2
1/(4*x+5),0,5,10
t,47 58 64 65 61 52 38,0,60,6
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
	a=input().split(',')
	if a[0]=="t":
		res=list(map(lambda x:1/float(x),a[1].split()))
		a,b,n=map(sympify,a[2:])
		h=(b-a)/n
	else:
		f,a,b,n=map(sympify,a)
		fx=lambda x:f.subs({'x':x})
		h=(b-a)/n
		res=[]
		r=list(crange(a,b,h))
		for i in r:
			z=fx(i)
			if z is nan:z=0
			res.append(z)
	print2(res)
	# print('-'*50)
	z=(res[0]+res[-1])+2*sum(res[2:-1:2])+4*sum(res[1:-1:2])
	print(r2(N(z*h/3)))
	print('-'*50)

if __name__ == '__main__':
	for i in range(int(input())):main()