# Input  : 2
# Output : 7 
# Explanation:  row 0 have element 1
#               row 1 have elements 1, 1
#               row 2 have elements 1, 2, 1
#               so, sum will be ((1) + (1 + 1) + (1 + 2 + 1)) = 7
# In general, row 0 to n (not included) will have sum 2^n - 1 and row n will have sum 2^n


def calculate_sum(n) : 
      
    # Initialize sum with 0 
    sum = 0
      
    # Calculate 2 ^ n 
    sum = 1 << (n + 1); 
      
    return (sum - 1) 
  
if __name__ == "__main__":
  n = int(input("Enter last row number: "))
  print("Sum of all elements:", calculate_sum(n))
