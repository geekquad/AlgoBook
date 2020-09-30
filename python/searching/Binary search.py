def binary(arr,low,high,x):
    while low < high:
        mid = low + (high-1) // 2
        if(arr[mid] == x):
            return mid
        elif(arr[mid] <x):
            low = mid + 1
        else:
            high = mid - 1
    return -1

n =int(input("Enter a sorted list of number\n"))
arr =[]
for i in range(n):
    arr.append(int(input()))

x =int(input("ENter the number to find\n"))

result = binary(arr,0,len(arr)-1,x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at ",result+1," position")
