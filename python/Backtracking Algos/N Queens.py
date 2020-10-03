def isSafe(a,i,j):
    row=i
    while row>=0:
        if a[row][j]==1:
            return False
        row-=1
    row=i
    col=j
    while row>=0 and col>=0:
        if a[row][col]==1:
            return False
        row-=1
        col-=1
    row=i
    col=j
    while row>=0 and col<len(a):
        if a[row][col]==1:
            return False
        row-=1
        col+=1
    return True
def nQueen(a,i,n):
    if i==n:
        for m in range(n):
            for j in range(n):
                print(a[m][j],end=' ')
        print()
        return
    for k in range(n):
        if isSafe(a,i,k):
            a[i][k]=1
            nQueen(a,i+1,n)
            a[i][k]=0
    return
    
n=int(input())
a=[[0 for j in range(n)]for i in range(n)]
nQueen(a,0,n)
