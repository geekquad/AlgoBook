n=int(input("enter the no. of rows"))
m=int(input("enter the no. of columns"))

matrix=[]

for i in range(n):
    a=[]
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)

print("Original matrix:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=" ")
    print()

l=[]

for i in range(n):
    for j in range(m):
        l.append(matrix[i][j])

l.sort()

newmatrix=[]

count=0

for i in range(n):
    p=[]
    for j in range(m):
        p.append(l[count])
        count=count+1
    newmatrix.append(p)
        

print("New matrix:")
for i in range(n):
    for j in range(m):
        print(newmatrix[i][j],end=" ")
    print()
