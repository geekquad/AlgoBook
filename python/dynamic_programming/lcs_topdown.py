def lcs(x,y,m,n,memo):
  if m==0 or n==0:
    memo[m][n]=0
    return  memo[m][n]
  if memo[m-1][n-1]!=-1:
    return  memo[m-1][n-1];
  elif x[m-1]==y[n-1]:
    memo[m-1][n-1]=1+lcs(x,y,m-1,n-1,memo)
    return  memo[m-1][n-1]
  else:
    memo[m-1][n-1] = max(lcs(x,y,m,n-1,memo),lcs(x,y,m-1,n,memo))
    return  memo[m-1][n-1]

if __name__=="__main__":
  str1="agbt"
  str2="agbt"
  arr=[[-1 for i in range(len(str2))] for j in range(len(str1))]
  n=lcs(str1,str2,len(str1),len(str2),arr)
  print(n)
