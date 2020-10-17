"""
Matrix rotation algorithms
"""
n = 3
def display(mat):
    for x in range(0, n):
        print(mat[x])

def rotate_clockwise(mat):
    for i in range(n // 2): 
        for j in range(i, n - i - 1): 
            temp = mat[i][j] 
            mat[i][j] = mat[n - 1 - j][i] 
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j] 
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i] 
            mat[j][n - 1 - i] = temp 
    print("clockwise")
    display(mat)

def rotate_anticlockwise(mat):
    for x in range(0, n // 2):  
        for y in range(x, n-x-1): 
            temp = mat[x][y]  
            mat[x][y] = mat[y][n-1-x] 
            mat[y][n-1-x] = mat[n-1-x][n-1-y] 
            mat[n-1-x][n-1-y] = mat[n-1-y][x] 
            mat[n-1-y][x] = temp
    print("anticlockwise")
    display(mat)

if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_anticlockwise(mat)
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_clockwise(mat)
    