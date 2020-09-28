def quickSort(collection):
    """
    Examples:
    >>> quickSort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quickSort([])
    []
    >>> quickSort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        # Use the last element as the first pivot
        pivot = collection.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quickSort(lesser) + [pivot] + quickSort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quickSort(unsorted))
