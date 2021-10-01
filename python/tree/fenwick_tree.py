# Binary Indexed Tree / Fenwick Tree 

# Returns sum of arr[0..index].   
def getsum(BITTree,i): 
	
  #initialize result
  s = 0 
  
	# index in BITree[] is 1 more than the index in arr[] 
	i = i+1

	# Traverse ancestors of BITree[index] 
	while i > 0: 
		# Add current element of BITree to sum 
		s += BITTree[i] 

		# Move index to parent node 
		i -= i & (-i) 
	return s 

# Updates a node 
# The given value 'val' is added to BITree[i] and all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 

	# index in BITree[] is 1 more than the index in arr[] 
	i += 1

	# Traverse all ancestors and add 'val' 
	while i <= n: 
		BITTree[i] += v 

		# Update index to that of parent  
		i += i & (-i) 


# Constructs Binary Indexed Tree for given array of size n. 
def construct(arr, n): 

	# Create and initialize BITree[] as 0 
	BITTree = [0]*(n+1) 

	# Store the actual values in BITree[] using update() 
	for i in range(n): 
		updatebit(BITTree, n, i, arr[i]) 

	return BITTree 

# Driver Code
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 

BITTree = construct(freq,len(freq)) 
# contents of BITree[] 
#for i in range(1,n+1): 
#	 print BITTree[i] 

print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))) 

# Updating at an index 
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+" after update is " + str(getsum(BITTree,5))) 

