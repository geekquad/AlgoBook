# Program to print the Pascal's Triangle upto a the given row
def printPascal(n):
  for i in range(1, n+1):
    for j in range(0, n-i+1):
      print(' ', end = ' ')
    
    C = 1
    for j in range(1, i + 1):
      print(' ', C, sep=' ', end=' ')
      
      C = C * (i -j) // j
    print()
    
if __name__ == "__main__":
    row = int(input("How many rows to printed? "))
    printPascal(row)
