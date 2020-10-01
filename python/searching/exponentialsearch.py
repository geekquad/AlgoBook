'''
   Exponenetial search works by finding the range in which the desired element is present and performing binary search in that given range
'''

def binarySearch( arr, start, end, x): #Recusrively call binary range in the given range
    if end >= start: 
        mid = int(start + ( end-start ) / 2)
        if arr[mid] == x: 
            return mid 
           
        if arr[mid] > x: 
            return binarySearch(arr,start,mid - 1, x) 

        else: 
            return binarySearch(arr, mid + 1, end, x) 
           
    return -1 #If element is not present in the array
  
def exponentialSearch(arr, n, x): #Function to perform exponential search 
    if arr[0] == x:#If element is present at the first pos 
        return 0
          
    i = 1
    while i < n and arr[i] <= x: #Keep doubling to find the range in which the number is present 
        i = i * 2
      
    return binarySearch( arr, i / 2,min(i, n), x) 
      
  
def main():#driver function
    arr= []
    n = int(input("Enter the number of elements: "))
    for i in range(n): #Taking input from the user
        ele = int(input("Enter the element: "))
        arr.append(ele)
    x = int(input("Enter the element to be searched: "))
    result = exponentialSearch(arr, n, x) 
    if result == -1: 
        print("Element not found in the array")
    else: 
        print("Element present at index: ",result) 

main() 