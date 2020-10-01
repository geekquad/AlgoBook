# implementation of bubble sort.
# time complexity : O(n^2) space complexity : O(1)


def bubble_sort(array_of_numbers: []):

    n = len(array_of_numbers)

    for i in range(n - 1):  # outer loop
        for j in range(1, n - i - 1):  # inner loop

            # checking if the number is greater than the current arr[i] value
            if array_of_numbers[j] > array_of_numbers[j + 1]:
                # swap
                array_of_numbers[j], array_of_numbers[j + 1] = (
                    array_of_numbers[j + 1],
                    array_of_numbers[j],
                )

    return array_of_numbers


# driver code
if __name__ == "__main__":

    arr = [90, 34, 56, 8, 0, -1, 23, 9]
    print("Array Before sorting : ")
    print(arr)
    print("Array after bubble sort : ")
    print(bubble_sort(arr))