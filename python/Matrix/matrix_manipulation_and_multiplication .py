a = [
    [1, 23, 4],
    [7, -2, 69],
    [7, 8, -9]
]

b = [
    [4, 5, 8],
    [78, 9, 0],
    [9, -3, 8]
]

def display(matrix: [[], [], []]):
    
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end="\t")
        print()

def multiply_matrix(a, b):

    c = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]
    
    return c


def remove_row(matrix: [[], [], []]):

    return(matrix[0:len(matrix)-1])


if __name__ == "__main__":
    option = 'y'

    print("press 1 for Multiplication ")
    print("press 2 to Remove a column")
    print("press 3 to Remove a row")

    x = int(input())

    if x == 1:
        print("Matrix A")
        display(a)
        print("Matrix B")
        display(b)
        print("Matrix C = A * B")
        display(multiply_matrix(a, b))

    if x == 3:
        print("Matrix A")
        display(a)
        print("After Removing Last Row")
        print(display(remove_row(a)))

