def fibonacci(n):
  if n==0 or n==1:
    return n;
  else:
    arr = [0 for i in range(n+1)]
    arr[1]=1
    for i in range(2,n+1):
      arr[i]=arr[i-1]+arr[i-2]
    return arr[n]
if __name__=="__main__":
  n = int(input("Enter a whole number"));
  val=fibonacci(n)
  print(val)
