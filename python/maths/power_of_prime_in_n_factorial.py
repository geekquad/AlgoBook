# Program to find power of a prime p in n!

# Returns power of p in n!
def power(n, p):
    # initializing answer
    ans = 0
    # initializing divisor
    temp = p

    # loop until temp <= n
    while temp <= n:
        ans += n / temp

        # each time multiply temp by p (to increase its power)
        temp *= p

    return ans


n = int(input("Enter a number n: "))
p = int(input("Enter a number p: "))
print(f"Power of {p} in {n}! is {power(n, p)}")

