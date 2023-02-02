def solution(ent,ex,pth):
	l=len(pth[0])
	c=0
	for i in range(l):
		if(i in ent):
			for j in range(l):
				if(j not in ent and j not in ex):
					c+=min(max(pth[j]),pth[i][j])
	return c
	
#print(solution([0,1],[4,5],[[0, 0, 4, 6, 0, 0],[0, 0, 5, 2, 0, 0],[0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
