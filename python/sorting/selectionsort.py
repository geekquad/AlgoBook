'''
 The Selection Sort algorithm sorts an array by finding the minimum value of the unsorted part and then swapping it with the first unsorted element.
'''

def selectionAscen(arr): #Function to sort array in ascending order
    for i in range(len(arr)-1):
        minInd = i       
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minInd]): 
                minInd = j
        arr[i], arr[minInd] = arr[minInd], arr[i] #Swapping elements  

def selectionDesc(arr): #Function to sort array in descending order
    for i in range(len(arr)-1):
        maxInd = i
        for j in range(i+1,len(arr)):
            if(arr[j]>arr[maxInd]):
                maxInd = j
        arr[i], arr[maxInd] = arr[maxInd], arr[i]
        
def main(): #driver function
    arr= []
    n = int(input("Enter the number of elements: "))
    for i in range(n): #Taking input from the user
        ele = int(input("Enter the element: "))
        arr.append(ele)
    selectionAscen(arr)
    print("Array sorted in ascending order: ")
    print(arr)
    print("Array sorted in descending order")
    selectionDesc(arr)
    print(arr)


main()