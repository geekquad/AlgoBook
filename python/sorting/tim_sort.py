# The Timsort algorithm is considered a hybrid sorting algorithm.
# it employs a best-of-both-worlds combination of insertion sort and merge sort.

# modifying the implementation of insertion_sort()
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
          key_item = array[i]
          j = i - 1
          while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            array[j + 1] = array[j]
            j -= 1

        # the `key_item` in its correct location
            array[j + 1] = key_item

    return array


def timSort(array):
    min_run = 64
    n = len(array)


    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # merging the sorted slices.

    size = min_run
    while size < n:
        # Determination of arrays that will be merged

        for start in range(0, n, size * 2):
            # Computing the `midpoint`

            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merging the two subarrays.

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # putting the merged array back into array
            array[start:start + len(merged_array)] = merged_array


    return array

    if __name__ == "__main__":
        user_input = input("Enter numbers separated by comma:\n")
        unsorted = [int(x) for x in user_input.split(",")]
        print(timSort(unsorted))
