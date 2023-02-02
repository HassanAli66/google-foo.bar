def solution(l):
	L=[]
	for i in range(len(l)):
		L.append(l[i].split('.'))
		for j in range(len(L[i])):
			L[i][j]=int(L[i][j])
	L=sorted(L)
	for i in range(len(L)):
		for j in range(len(L[i])):
			L[i][j]=str(L[i][j])
		L[i]='.'.join(L[i])
	return L
#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
