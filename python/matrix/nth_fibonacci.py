"""
Nth Fibonacci Number Using 
Matrix Exponentiation
"""
def mat_mul(mat1, mat2, MOD=0):
    """
    Multiplies two matrices 
    If value of MOD is provided the
    find remainder wrt MOD 
    """
    arr = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            for k in range(0, len(mat2)):
                if(MOD==0):
                    arr[i][j] = (arr[i][j]+mat1[i][k]*mat2[k][j]) 
                else:
                    arr[i][j] = (arr[i][j]+mat1[i][k]*mat2[k][j])%MOD
    return arr

def power(M, n, MOD=0):
    """
    Finds matrix, M, to the power n 
    using binary exponentiation
    """
    res = [[0 for i in range(len(M))] for j in range(len(M))]
    for i in range(len(M)):
        res[i][i] = 1
    while n>0:
        if n & 1:
            res = mat_mul(res, M, MOD)
        n = n>>1
        M = mat_mul(M, M, MOD)
    return res

def nth_fibonacci(n, MOD=0):
    """
    Function to find nth fibonacci number
    If value of MOD is provided 
    function will return fib[n]%MOD
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    F = [[0, 1]]
    M = [[0, 1],
         [1, 1]]
    mat = power(M, n-1, MOD)
    R = mat_mul(F, mat, MOD)
    return R[0][1]


if __name__ == "__main__":
    n   = int(input("Enter the value of n: "))
    MOD = int(input("If want to find remainder\
                    \nthen enter Divisor else 0: "))
    fib = nth_fibonacci(n, MOD)
    print(fib)


