def SubsetSum(set, n, sum) : 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
    if (set[n - 1] > sum) : 
        return SubsetSum(set, n - 1, sum); 
        
    return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, sum-set[n-1]) 
      
      
set = [2,3,6,4.1,56] 
sum = 11
n = len(set) 
if (SubsetSum(set, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum") 
