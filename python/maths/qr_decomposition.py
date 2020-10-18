import sys
import scipy
import pprint
import numpy as np
import scipy.linalg


def decomposition(A):
     Q, R = scipy.linalg.qr(A)

     print (f"\n\nA:{A}")
     print (f"\nQ:{Q}")
     print (f"\nR:{R}")



if __name__ == "__main__":
    matrix_size = input('Write the size of the matrix seperated by a comma (eg: 3,3): ').split(',')
    if len(matrix_size) > 2:
        print('Error, exiting...')
        sys.exit()
    else:
        pass
    A = np.random.rand(int(matrix_size[0]), int(matrix_size[1]))
    decomposition(A)
