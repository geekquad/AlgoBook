# Program to find GCD of the digits of a number

# Recursive function to return gcd of a and b
def gcd(a, b):
    return a if (b == 0) else gcd(b, a % b)


def digitGCD(n):
    ans = 0
    while n > 0:

        ans = gcd(n % 10, ans)

        # If at any point GCD is 1, return
        if gcd == 1:
            return 1

        n = n // 10

    return ans


n = int(input("Enter a number: "))
print("GCD of the digits of n is", digitGCD(n))

