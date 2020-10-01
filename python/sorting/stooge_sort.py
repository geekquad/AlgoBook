# Python program to implement stooge sort

def stoogesort(array, l, h):
    if l >= h:
        return

    # If first element is smaller
    # than last, swap them
    if array[l]>array[h]:
        t = array[l]
        array[l] = array[h]
        array[h] = t
    # If there are more than 2 elements in
    # the array
    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        # Recursively sort first 2 / 3 elements
        stoogesort(array, l, (h-t))

        # Recursively sort last 2 / 3 elements
        stoogesort(array, l + t, (h))

        # Recursively sort first 2 / 3 elements
        # again to confirm
        stoogesort(array, l, (h-t))
# checking
array = [2, 4, 5, 3, 1]
n = len(arr)

stoogesort(array, 0, n-1)

for i in range(0, n):
    print(array[i], end = ' ')

#hi this is done by srishti
