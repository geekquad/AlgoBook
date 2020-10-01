a = []
n = int(input("Enter Total Number of Elements : "))

for i in range(0,n):
    value = int(input("Please enter Elements of List :"))
    a.append(value)
    
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
             
print("Sorted List: ", a)  #final answer
