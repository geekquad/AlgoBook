def bubbleSort(collection):
    """
    Examples:
    >>> bubbleSort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubbleSort([])
    []
    >>> bubbleSort([-2, -45, -5])
    [-45, -5, -2]
    >>> bubbleSort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubbleSort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    """
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j +
                                          1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == "__main__":
    import time

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubbleSort(unsorted), sep=",")

    # get execution time
    print(f"Processing time: {time.process_time() - start}")
