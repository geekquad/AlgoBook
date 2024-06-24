# time complexity - O(log n)

"""
basic concept
|f(n)  |  =  |1 1|  *  |f(n-1)|
|f(n-1)|  =  |1 0|  *  |f(n-2)|

Which finally extends to,

|f(n)  |  =  |1 1|^(n-1)  *  |f(1)|
|f(n-1)|  =  |1 0|        *  |f(0)|

Note that here |x| is a matrix and not a determinant
"""
  
def multiply(F, M):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += F[i][k] * M[k][j]
    
    for i in range(2):
        F[i] = result[i]

  
def power(F, n): 
    M = [[1, 1], 
         [1, 0]] 
   
    for i in range(2, n + 1): 
        multiply(F, M) 

def fib(n): 
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
      
    return F[0][0] 
  
if __name__ == '__main__':
    n = int(input())
    print(fib(n))