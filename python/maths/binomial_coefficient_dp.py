# A Dynamic Programming based Python implementation to find Binomial Coefficient
  
# Returns value of Binomial Coefficient C(n, k)
def binomial_coefficient(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    # Calculate value of Binomial Coefficient with bottom-up
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            # Base Cases 
            if j == 0 or j == i: 
                C[i][j] = 1
            # Else calculate using existing values
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    return C[n][k] 
    
if __name__ == "__main__":
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    coeff = binomial_coefficient(n, k)
    print(f"Binomial Cofficient C({n}, {k}) is {coeff}")
