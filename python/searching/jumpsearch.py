'''
   Jump search is searching algorithm for sorted arrays.It skips some elements by taking fixed steps defined by the block size 
   instead of travesing through all the elements.
'''

import math #for sqrt

def jumpsearch(arr,ele): #function to perform jump search
    
    n = len(arr) #Length of the list/array
    block = int(math.sqrt(n))#Defining size of the block(no of elements to be skipped)
    start=0
    end = 0
    while start < n and arr[start] <= ele:
        end = min(n - 1, start + block)#Taking the minimum of the length and start
        if arr[start] <= ele and arr[end] >= ele: #If block in which element is present is found then break
            break
        start += block #Keep incrementing start with the value of block size unti block is found
    if start >= n or arr[start] > ele: #If element is not found 
        return -1
    end = min(n- 1, end)#Taking the minimum of the length and end
    i = start
    while i <= end and arr[i] <=ele:#Search for the element in the respective block
        if arr[i] == ele:
            return i
        i += 1
    return -1 

def main():#Driver function
    arr = [1,2,3,4,5,6,7,8,9] #Input array/list
    pos = jumpsearch(arr,5)
    if(pos>=0):
        print("Element located at pos: ",pos+1)
    else:
        print("Element not located")

main()