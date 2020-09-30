def linear(arr,n,x):
    for i in range(n):
        if(arr[i] == x):
            return i
    return -1

n = int(input("Enter the total number of elements\n"))
arr =list(map(int,input().split()))
x = int(input("Enter which element you want to find\n"))
result = linear(arr,n,x)
if (result == -1):
        print("Element not found")
else:
        print("Element found at" ,result+1,"position")

        


    


    



    

    


    
