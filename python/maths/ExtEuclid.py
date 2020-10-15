def ext_euclid(a, b):
    x,y, u,v = 0,1, 1,0

    while a != 0:
        #quotient (q), remainder (r)
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        
        print("Quotient: "+str(q))
        print("GCD: "+str(b))
        print("Remainder: "+str(a))
        print(x,y,u,v)

    gcd = b
    return gcd, x,y

a, b = 30, 20
gcd, x, y = ext_euclid(a, b)
print("gcd(",a,",",b,") = ",gcd)