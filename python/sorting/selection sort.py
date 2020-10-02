n = int(input())
li = []
for i in range(n):
    m = int(input())
    li.append(m)

for i in range(n):
    mini = i 
    for j in range(i+1,n):
        if(li[j] < li[mini]):
            mini = j
    temp = li[i]
    li[i] = li[mini]
    li[mini] = temp
    print(li)
