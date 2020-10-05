def bubbleSort(array): 
    n = len(array) 

    # Traverse through all array elements 
    for i in range(n-1): 

        # Last i elements are already in place 
        for j in range(0, n-i-1): 

            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 

# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
