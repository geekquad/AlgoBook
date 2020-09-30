'''
   Merge sort is a divide and conquer algorithm.It divides the intial list/array into two halves and
   repeats the process on those two halves and finally merges the sorted halves
'''

def mergesortAscen(arr): #Function to sort list in ascending order
    if(len(arr) > 1):
        midInd = int(len(arr)/2)

        #Splitting the list into two halves
        first = arr[0:midInd]
        second = arr[midInd:]
        
        #recursively divide each list in 2 halves and sorting each respective list 
        mergesortAscen(first)
        mergesortAscen(second)
        
        i=j=k=0
        while i<len(first) and j<len(second):
            if(first[i]<second[j]): #Comparing the elements 
                arr[k] = first[i]
                i+=1
            else:
                arr[k] = second[j]
                j+=1
            k+=1
        
    
        #Adding the remaining elements
        while(i<len(first)):
                arr[k] = first[i]
                i+=1
                k+=1
        while(j<len(second)):
                arr[k]= second[j]
                j+=1
                k+=1

def mergesortDesc(arr): #Function to sort list in descending order
    if(len(arr) > 1):
        midInd = int(len(arr)/2)
        first = arr[0:midInd]
        second = arr[midInd:]

        mergesortDesc(first)
        mergesortDesc(second)
        
        i=j=k=0
        while i<len(first) and j<len(second):
            if(first[i]>second[j]):
                arr[k] = first[i]
                i+=1
            else:
                arr[k] = second[j]
                j+=1
            k+=1
        
    
        while(i<len(first)):
                arr[k] = first[i]
                i+=1
                k+=1
        while(j<len(second)):
                arr[k]= second[j]
                j+=1
                k+=1
        
    

def printarr(arr):
    
    for i in range(len(arr)):
        print(arr[i])

def main(): #Driver function
    arr = [3,5,1,4,2]
    print("Orignal Array:")
    printarr(arr)
    mergesortAscen(arr)
    print('Sorted Array in ascending order:')
    printarr(arr)
    print('Sorted Array in descending order:')
    mergesortDesc(arr)
    printarr(arr)

main()
        

