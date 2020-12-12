def SubsetSum(set, n, sum) : 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
    if (set[n - 1] > sum) : 
        return SubsetSum(set, n - 1, sum); 
        
    return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, sum-set[n-1]) 
      
      

n=int(input("number of elements :- "))
sum=int(input("Enter the sum:- ")) 
print("elements in the set:-")
arr=[]
for i in range(0,n):
     arr[i]=int(input(" "))
     arr.append(arr[i])

    
if (SubsetSum(set, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum") 
