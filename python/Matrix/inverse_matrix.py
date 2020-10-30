import copy,math
#Matrix inverse Finder .Note that matrix starts at [1][1] so for that it contains redundant [None]'s in [0][:]and [:][0]
def reducer(matrix,i,j):#gets the matrix by removing the (i,j)th element
    matcopy=copy.deepcopy(matrix)
    [matcopy[y].pop(j) for y in range(0,len(matcopy))]
    matcopy.pop(i)
    return matcopy
def determinant(matrix):#returns the determinant of the specific matrix
    if len(matrix)==3:
        return matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]
    elif len(matrix)==2:
        return matrix[1][1]
    else:
        det=list()
        for j in range(1,len(matrix)):#this is (?,y)'s value we choose ? always 1
            submatrix=reducer(matrix,1,j)
            det.append(math.pow(-1,1+j)*matrix[1][j]*determinant(submatrix))
        return sum(det)
def inverse(matrix):#returns inverse matrix else 0
    det=determinant(matrix)
    if det==0:
        return 0
    adjoint_matrix=[[None for _ in range(0,m+1)]for _ in range(0,m+1)]
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix)):
            minor=determinant(reducer(matrix,i,j))#minor
            cofactor=math.pow(-1,i+j)*minor#cofactor
            adjoint_matrix[j][i]=cofactor/det#directly swap[i][j]<-->[j][i] and divide by the determinant
    return adjoint_matrix
if __name__=="__main__":#for running as script
    m=int(input("Enter the size of row/column of matrix :"))#get size of m*m matrix
    mat=[[None for _ in range(0,m+1)]for _ in range(0,m+1)]#prefill the matrix and make shallow data for initial from [1][1]
    for i in range(1,m+1):#Get the data from user
        for j in range(1,m+1):
            data_int=False
            while not data_int:
                try:
                    data=int(input(f"Enter the ({i},{j})th element of matrix :"))
                    data_int=True
                except ValueError:
                    print("Enter a valid integer :")
            mat[i][j]=data
    inverse_=inverse(mat)
    if inverse_==0:
        print("Sorry the inverse doesn't exist for this matrix")
    else:
        for x in range(1,m+1):
            print("\t[",end="\t")
            for y in range(1,m+1):
                print(inverse_[x][y],end="\t")
            print("]\t")