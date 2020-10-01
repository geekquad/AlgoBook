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


# user_input
if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n")
    unsorted = [int(x) for x in user_input.split(",")]
    print(stoogesort(unsorted))



#hi this is done by srishti
