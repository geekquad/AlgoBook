#coding: utf-8
def minimum(array, index):
    length = len(array)
    minimum_index = index
    for j in range(index, length):
            if array[minimum_index] > array[j]:
                minimum_index = j
    return minimum_index

def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        minimum_index = minimum(array, i)
        if array[i] > array[minimum_index]:
            array[i], array[minimum_index] = array[minimum_index], array[i]
