def mergeSort(collection: list) -> list:
    """Examples:
    >>> mergeSort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> mergeSort([])
    []
    >>> mergeSort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list, right: list) -> list:
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(mergeSort(collection[:mid]), mergeSort(collection[mid:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*mergeSort(unsorted), sep=",")
