def fibonacci(n,memo):
  if n==0 or n==1:
    return n
  if memo[n]!=0:
    return memo[n]
  else:
    memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
if __name__=="__main__":
  n = int(input("Enter a whole number\n"));
  memo = [0 for i in range(n+1)]
  val=fibonacci(n,memo)
  print(val)
