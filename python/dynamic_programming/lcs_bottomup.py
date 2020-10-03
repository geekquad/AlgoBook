def lcs(x,y):
  m=len(x)+1
  n=len(y)+1
  arr=[[0 for i in range(n)] for j in range(m)]
  for i in range(1,m):
    for j in range(1,n):
      if x[i-1]==y[j-1]:
        arr[i][j]=1+arr[i-1][j-1]
      else:
        arr[i][j]=max(arr[i-1][j],arr[i][j-1])
  return arr[m-1][n-1]
if __name__=="__main__":
  str1="t"
  str2="agbt"
  n=lcs(str1,str2)
  print(n)
