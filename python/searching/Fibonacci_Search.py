#Fibonacci search is a comparison technique that uses Fibonacci numbers to search an element in a sorted array
#fibonacci numbers are recursively defined as 
# F(n)=F(n-1)+F(n-2)

def FiboGen(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FiboGen(n - 1) + FiboGen(n - 2)

def FiboSearch(arr, num):
    fm = 0 
    while FiboGen(fm) < len(arr): 
        fm = fm + 1 
    offset = -1    
    while (FiboGen(fm) > 1):
        #check if fm is a valid location
        i = min( offset + FiboGen(fm - 2) , len(arr) - 1) #smallest fibonacci number greater than or equal to num
        if (num > arr[i]):# If num is greater than the value at index fm, cut the subarray array from offset to i  
            fm = fm - 1
            offset = i
        elif (num < arr[i]):# If num is less than the value at index fm, cut the subarray after i+1 
            fm = fm - 2
        else:
            return i  #if element found return index
    #comparing last element with num       
    if(FiboGen(fm - 1) and arr[offset + 1] == num):
        return offset + 1
    return -1

arr = []
n=int(input("enter the number of elements you want to enter"))
for i in range(0,n):
    ele=int(input("enter element {} : ".format(i+1)))
    arr.append(ele)
 
num =int(input("enter the number you want to search : "))

print('found at index :',FiboSearch(arr, num))
