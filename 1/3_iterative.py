a='''i
x*sin(x)+cos(x);pi-acot(x)
E^-x-10*x
x**3+x**2-1
x**3-2*x-5
'''
nn=4
a=a.splitlines()[1:]
ai=-1

from itertools import *
from sympy import *
from math import *
import numpy as np
import traceback
def input():
	global ai
	ai+=1
	return a[ai]

x=Symbol('x')


r2=lambda x,y=4: round(x+1e-15,y)
sign=lambda x:-1 if x<0 else 1 if x>0 else 0


def main():
	eqn=(input()).split(';')
	var('x')
	p = poly(eqn[0]);

	p1=factor(p-(p).coeff_monomial(1))
	res=[]
	try:
		for i in p1.args:
			if (poly(i).is_monomial):
				z=(np.prod([j for j in p1.args if j!=i]))
				p2=(-(p).coeff_monomial(1)/z)**(1/degree(i));
				v=i.coeff(x)
				if p2:res.append(p2)
				elif v:
					p2=(-z/v)
					res.append(p2)
	except Exception as e:
		print(e)
	try:
		for i in (p.all_terms())[:-1]:

			if i[1]:
				p3= ((i[1]*x**i[0][0]-p)/i[1])**(1/Integer(i[0][0])) ;
				if p3:res.append(p3);

	except Exception as e:
		# print(e)
		pass
	if not res :
		print(eqn[0],'provide phi(x)')
		exit()
	# print(res)
	for i4 in (res+eqn[1:]):
		rr=''
		try:
			y=sympify(i4)
			ydash=(y.diff(x))
			y1=sympify(eqn[0])
			f=lambda x:y1.subs({'x':x}).evalf()
			p=lambda x:y.subs({'x':x}).evalf()
			f1=lambda x:ydash.subs({'x':x}).evalf()
			xn=lambda x:(p(x)).evalf()
			try:
				i=0
				z=f(i)
				if z==zoo:raise ValueError
			except ValueError:
				i=1
			s=sign(f(i))

			z=0
			if z:
				a,b=2,3
			else:
				for i in count(i+1):
					_=f(i)
					s1=sign(_)
					if s1!=s or s1==0 :
						a,b=(i-1,i);break
					s=s1
				rr+='%s %s\n'%(a,b)
			z,z1=f1(a),f1(b)
			if zoo in [z,z1] or not(abs(z)<1 and abs(z1)<1):
				rr+='%s %s %s\n' %('derivative',z,z1)
				rr+=("error")
				continue

			for i in count(1):
				z=(xn(a))
				# print(i,a,b)

				# rr+='%s %s\n' %(i,r2(z))
				if r2(a)==r2(z)  or a>b:
					break
				a=z
			rr+='%s' % (r2(z))
		except Exception as e:
			print(e)
			# traceback.print_exc()
			continue
		print(simplify(i4),'\n',rr)
		break
	else:
		print(eqn[0],'provide other phi(x)')
		print(res)
	# print(i,r2(z))

if __name__ == '__main__':
	for i in range(nn):
			main()	
			print('-'*75)	