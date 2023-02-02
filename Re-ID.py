def solution(i):
	def _is_prime(i):
		for j in range(2,i):
			if (i%j) == 0:
				return False
		return True
	primes=''
	num=2
	while(len(primes)<=i+5):
		if(_is_prime(num)):
			primes+=str(num)
		num+=1
	return primes[i:i+5]
#print(solution(3))
