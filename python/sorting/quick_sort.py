# quick sort
# worst case - O(n2), best case - O(n log n) 


# sort the halves and merge
def partition(iarr, low, high):
    pivot = iarr[high]
    i = low - 1
    for j in range(low, high):
        if iarr[j] < pivot:
            i += 1
            iarr[i], iarr[j] = iarr[j], iarr[i]

    iarr[i + 1], iarr[high] = iarr[high], iarr[i + 1]

    return i + 1


def sort(iarr, low, high):
    if low < high:
        # create partition
        pi = partition(iarr, low, high)
        # sort first half
        sort(iarr, low, pi - 1)
        # sort second half
        sort(iarr, pi + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sort(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        print("%d" % arr[i])
