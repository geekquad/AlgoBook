"""
A simple python programme to demonstrate Markov's chain principle using matrices.
One can learn more about it here: https://en.wikipedia.org/wiki/Markov_chain 
"""

from fractions import Fraction

tags=[]
n_term=0

def swap_row(i,r,m):
    """
    Swap function for rowise elements using python special powers
    """
    tags[i],tags[r]=tags[r],tags[i]
    m[i],m[r]=m[r],m[i]
    return m 

def swap_col(j,c,m):
    """
    swaping column wise elements
    """
    n_row=len(m)
    for i in range(n_row):
        m[i][j],m[i][c]=m[i][c],m[i][j]
    return m

def canonical_form(m):
    """
    Computes canonical for of the matrix, for applyting markov's chain principle
    """
    global n_term
    sr,sc=len(m)-1,len(m)-1
    i=0
    while i<(len(m)):
        if sum(m[i])==0 and i!=(sr+1):
            n_term+=1
            if i!=len(m)-1:
                if sum(m[i+1])!=0:
                    m=swap_row(i,sr,m)
                    sr-=1
                    m=swap_col(i,sc,m)
                    sc-=1
                    i-=1
                    continue
        i+=1

    for i in range(len(m)):
        s=float(sum(m[i]))
        if s==0:
            m[i][i]=1
        else:
            for j in range(len(m[i])):
                m[i][j]/=s
        
    return m

def form(m):
    """
    returns a part of a matrix to use
    """
    Q=[]
    R=[]
    for i in range(len(m)-n_term):
        Q.append(m[i][:-n_term])
        R.append(m[i][-n_term:])

    return Q,R

def I_form(n):
    """
    returns Identity matrix of order n
    """
    I=[]
    item=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                item.append(1)
            else:
                item.append(0)
        I.append(item)
        item=[]

    return I

def sub(A,B):
    """
    matrix subtraction functions which returns resultant matrix after subtracting two matrices
    """
    n=len(A)
    output=[]
    result=[]
    for i in range(n):
        for j in range(n):
            result.append(A[i][j]-B[i][j])
        output.append(result)
        result=[]

    return output

def multiply(a, b):
    """
    matrix multiplication function
    """
    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            sum = 0
            for i in range(iters):
                sum += a[r][i]*b[i][c]
            mRow.append(sum)
        m.append(mRow)
    return m

# transpose matrix
def transposeMatrix(m):
    """
    returns transpose of a matrix
    """
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    """
    returns minors of a mtrix
    """
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# matrix determinant
def getMatrixDeternminant(m):
    """
    returns determinant of a matrix 
    """
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))

    return d

# matrix inversion
def getMatrixInverse(m):
    """
    returns inverse of a matrix, using minors and determinants of a matrix
    """
    if len(m)==1:
        return [[1/m[0][0]]]
    d = getMatrixDeternminant(m)

    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors

def Pmatrix(A):
    """
    matrix printing function
    """
    for i in A:
        print('{0}\n'.format(i))

def get_lcm(num1,num2):
    """
    returns lowest common multiple amoung two numbers
    """
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm

def normalize(prob):
    """
    normalizes a matrix out of fractional part to decimal part 
    """
    num=[]
    deno=[]
    lcm=0
    for i in range(len(prob)):
        a=Fraction(prob[i]).limit_denominator(1000).denominator
        b=Fraction(prob[i]).limit_denominator(1000).numerator
        num.append(b)
        deno.append(a)    

    lcm=get_lcm(deno[0],deno[1])

    for i in range(2,len(deno)):
        lcm=get_lcm(lcm,deno[i])

    for i in range(len(prob)):
        factor=lcm/deno[i]
        num[i]*=factor
    num.append(lcm)
    return num

def solution(m):
    """
    driver function 
    """
    if len(m) <3:
        return [1,1]
    for i in range(len(m)):
        tags.append(i)

    m=canonical_form(m)
    #Pmatrix(m)
    Q,R=form(m)
    #Pmatrix(R)
    I=I_form(len(Q))
    Q=sub(I,Q)
    Q=getMatrixInverse(Q)
    probs=multiply(Q,R)
    #Pmatrix(probs)
    
    result=normalize(probs[0])
    r={}
    md=result[-1]
    for i in range(len(tags)-n_term,len(tags)):
            r[tags[i]]=result[i-(len(tags)-n_term)]
    idx=sorted(r.keys())
    result=[]
    for i in idx:
        result.append(r[i])
    result.append(md)
    #print(result,r)
    return result
#Few test cases
"""
m=[
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
"""

m=[
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
print(solution(m))