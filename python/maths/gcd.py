def gcd(num1,num2): 
    """Returns the GCD of the two elements."""
    if(num2==0): 
        return num1 
    else: 
        return gcd(num2,num1%num2) 

num1 = int(input("Enter an Integer: "))
num2 = int(input("Enter another Integer: "))
print ("GCD: ",gcd(num1,num2))
