def SubsetSum(set, n, sum) : 
    # these are the base cases/corner cases which we need to handle explicitly
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
    # if last number is greater than sum, than we need to ignore it.
    if (set[n - 1] > sum) : 
        return SubsetSum(set, n - 1, sum); 
     # here wwe try to check if we can check the sum by excluding the last element or including the last element.   
    return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, sum-set[n-1]) 
      
      

n=int(input("number of elements :- "))  #n=5 , let the number of elements in the set be 5
sum=int(input("Enter the sum:- "))      #sum=4 , the sum which we need to search is 4
print("elements in the set:-")
a=[]
for i in range(0,n):
     value = int(input("Please enter the %d Element : " %i))
     a.append(value)                    #arr=[2,2,3,6,9] , this is the list of numbers we have

    
if (SubsetSum(a, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum") 
