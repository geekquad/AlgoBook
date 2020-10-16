def Add(matA, matB):
    """
    Add(matrix1, matix2):
    Adds both matices and returns -1 if order of both matrices different or else returns resultant matrix
    """
    A=len(matA[0])
    B=len(matB[0])
    #checks number of columns equal of not for both matices
    if A!=B:
        return -1
    C=[[]]
    for i in range(A):
        for j in range(B):
            C[-1].append(matA[i][j]+matB[i][j])
        C.append([])
    return C

def Sub(matA, matB):
    """
    Sub(matrix1, matix2):
    Subtracts both matices and returns -1 if order of both matrices different or else returns resultant matrix
    """
    A=len(matA)
    B=len(matB)
    #checks number of columns equal of not for both matices, same as previous
    if A!=B:
        return -1
    C=[[]]
    for i in range(A):
        for j in range(B):
            C[-1].append(matA[i][j]-matB[i][j])
        C.append([])
    return C

def printMat(matrix):
    """
    printMat(matrix1, matix2):
    prints matrix in proper fashion, and returns None
    """
    for row in matrix:
        for item in row:
            print(item,end=" ")
        print()


if "__main__"==__name__:
    A=[
        [1,2,3],
        [3,5,6],
        [3,8,1]
        ]
    
    B=[
        [35,7,8],
        [1,7,4],
        [6,96,3]
        ]
    res=Add(A,B)
    if res==-1:
        print("Both matrices have to be equaal in dimensions")
    else:
         print("Adding A and B: ")
         printMat(res)
         print("Subtracting A and B")
         res=Sub(A,B)
         printMat(res)