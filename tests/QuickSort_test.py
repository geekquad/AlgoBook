
from python.sorting.QuickSort import quicksort

import numpy as np
def asc_sorted(array):
    check=True
    print(array)
    for i in range(len(array)):
        if(i<len(array)-1):
            if(array[i]>array[i+1]):
                check=False
                return check
    return check

def test_nums():
    array=[3,5,7,92,7,9]

    array=quicksort(array)
    isSorted=asc_sorted(array)
    assert isSorted == True, "Test Passed for Normal Numbers"

def test_negative_nums():
    array=[-3,-5,-7,-92,-7,-9]
    array=quicksort(array)
    isSorted=asc_sorted(array)
    assert isSorted == True, "Test Passed for Negative Numbers"
    
def test_random_nums():
    arr = np.random.randint(0,10,50)
    arr=quicksort(arr)
    isSorted=asc_sorted(arr)
    assert isSorted == True, "Test Passed for Random Numbers"

    
def test_random_float():
    low=0
    high=300
    size=60
    arr=[np.random.uniform(low,high) for _ in range(size)]
    arr=quicksort(arr)
    isSorted=asc_sorted(arr)
    assert isSorted == True, "Test Passed for Random float Numbers"


if __name__ == "__main__":
    test_negative_nums()
    test_random_float()
    test_random_nums()
    test_nums()