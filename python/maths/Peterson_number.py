# This is an example for peterson number.
#  145 = 5! + 4! + 1!
#      = 120 + 24 +1
#      = 145


#This list contains factorials of all the nine digits in order.
#This is beacause, we may need to compute these factorials many times in the numbers given.

factorials = [1, 1, 2, 6, 24, 120, 720,5040, 40320, 362880]

#Function that checks the peterson number condition
def peterson(n):
    num = n
    sum = 0

    while n > 0:
        digit = int(n % 10)
        sum += factorials[digit]
        n = int(n / 10)
 
    # Condition check for a number
    # to be a Peterson Number
    if(sum==num):
        return True
    else:
        return False
 
 
# Driver Code
number = input("Enter the number to be checked for peterson's condition : ");
print("Yes, the number {} is peterson number".format(number) if peterson(int(number)) else "No, {} is not peterson number".format(number))
