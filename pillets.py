def solution(n):
	n=int(n)
	c=0
	while(n!=1):
		if(n%2==0):
			n/=2
			c+=1
		else:
			if((n+1)/2 % 2 == 0):
				n+=1
				c+=1
			elif((n-1)/2 % 2 == 0):
				n-=1
				c+=1
	return c
#print(solution('4'))
