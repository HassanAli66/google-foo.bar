from decimal import *
def beatty(n):
	getcontext().prec=102
	if(n==0):return 0
	if(n==1):return 1
	root2=Decimal(2).sqrt()
	n_=int((root2-1)*n)
	return int(Decimal(n*n_+n*(n+1)/2-n_*(n_+1)/2-beatty(n_)))
def solution(str_n):
	return str(beatty(int(str_n)))
# YAAAAAAAAAAAAAYYY, IT'S DONNNNEEEE!!!!!!! \o/

