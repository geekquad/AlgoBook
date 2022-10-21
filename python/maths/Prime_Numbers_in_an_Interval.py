"""
Prime numbers are very unique in that they cannot be expressed as products of any other numbers at all!

Argument(s): lower (integer) and upper (integer)
Returns: list of prime numbers in the given interval
"""
# Defining a function to print the prime numbers...
def get_primes(lower, upper)->list:
    primes = list()
    for number in range(lower, upper+1):
        if (number < 0):
            number = -number
        if (number > 1):
            for i in range(2, number):
                if (number%i == 0):
                    break
            else:
                primes.append(number)
    return primes

if __name__ == "__main__":
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    prime_nos = get_primes(lower_limit, upper_limit)
    print("All the primes in the given range are:\n", prime_nos)
    print(f"There are {len(prime_nos)} primes..")
