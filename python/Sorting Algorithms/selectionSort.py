def selectionSort(collection):
    """
    Examples:
    >>> selectionSort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selectionSort([])
    []
    >>> selectionSort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = (
                collection[i], collection[least])
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selectionSort(unsorted))
