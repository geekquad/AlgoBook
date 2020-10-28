class edge: 
	def __init__(self, u, w): 
		self.From = u 
		self.weight = w 

def addedge(u, v, w): 
	edges[v].append(edge(u, w)) 

def shortestpath(dp): 
	
	for i in range(V + 1): 
		for j in range(V): 
			dp[i][j] = -1

 
	for i in range(1, V + 1): 
		for j in range(V): 
			for k in range(len(edges[j])): 
				if (dp[i - 1][edges[j][k].From] != -1): 
					curr_wt = (dp[i - 1][edges[j][k].From] +
										edges[j][k].weight) 
					if (dp[i][j] == -1): 
						dp[i][j] = curr_wt 
					else: 
						dp[i][j] = min(dp[i][j], curr_wt) 
vg values 
	avg = [-1] * V 

	for i in range(V): 
		if (dp[V][i] != -1): 
			for j in range(V): 
				if (dp[j][i] != -1): 
					avg[i] = max(avg[i], (dp[V][i] -
										dp[j][i]) / (V - j)) 

	result = avg[0] 
	for i in range(V): 
		if (avg[i] != -1 and avg[i] < result): 
			result = avg[i] 

	return result 

#  Driver Code 
V = 4

#  vector to store edges 
edges = [[] for i in range(V)] 

addedge(0, 1, 1) 
addedge(0, 2, 10) 
addedge(1, 2, 3) 
addedge(2, 3, 2) 
addedge(3, 1, 0) 
addedge(3, 0, 8) 

print(minAvgWeight()) 