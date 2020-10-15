def gnome_sort(arr):
    arr_len = len(arr)
    index = 0
    while index < arr_len:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index-1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1

    return arr

arr = [34, 2, 10, -9]
print("Array before Gnome sort: ",arr)
arr = gnome_sort(arr)
print("Array after Gnome sort:  ",arr)