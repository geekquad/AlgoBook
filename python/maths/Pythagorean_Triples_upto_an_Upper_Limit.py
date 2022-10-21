"""
Pythagorean Triples are quite unique in the mathematics of algebra and geometry (for aspiring high schoolers and professional mathematicians alike).
Any triplets x, y, and z or tuples (x, y, z) from the set of natural numbers which satisfy the property that x² + y² = z² are called Pythagorean Triples. 

Argument(s): None
Returns: pythagorean triples (tuples of integers)

NOTE: This function only deals with integers. When floats are given, it may throw errors/exceptions. 
"""

# Defining the function to return all the Pythagorean Triples up until a certain upper limit.
def PythagoreanTriples():
    limit = int(input("Enter the limit: "))
    while True:
        if (limit > 0):
            break
        else:
            print("Oh no! The number has to be positive.. Try again.")
            limit = int(input("Enter the limit: "))
            
    c = 0
    m = 2
    
    print("The Pythagorean triples upto %s are:"%str(limit))
    triples = []
    while(c < limit):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if (c > limit):
                break
            triples.append((a,b,c))
            print(a, b, c)
        m += 1
    return triples
  
if __name__ == "__main__":
    my_triples = PythagoreanTriples()
    print(f'There are {len(my_triples)} triples.')
