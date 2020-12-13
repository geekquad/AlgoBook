# Demonstrates the working of Chinese Remainder Theorem

# k is size of num[] and rem[].
# Returns the smallest number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[] are pairwise co-prime (gcd for every pair is 1)


def findMinX(num, rem, k):
    # Initialize result
    x = 1

    # As per the CRT, this loop will always break.
    while True:
        # Check if remainder of x % num[j] is rem[j] or not (for all j from 0 to k-1)
        j = 0
        while j < k:
            if x % num[j] != rem[j]:
                break
            j += 1

        # If all remainders matched, we found x
        if j == k:
            return x
            # Else try next number
        x += 1


num = []
rem = []

print("Enter three numbers (on new lines): ")
for i in range(3):
    num.append(int(input()))

print("Enter three numbers (on new lines): ")
for i in range(3):
    rem.append(int(input()))

k = len(num)
print("x is", findMinX(num, rem, k));
