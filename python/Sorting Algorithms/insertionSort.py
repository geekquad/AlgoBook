def insertionSort(collection: list) -> list:
    """
    Examples:
    >>> insertionSort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertionSort([])
    []
    >>> insertionSort([-2, -5, -45])
    [-45, -5, -2]
    """

    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (
            insertion_index > 0
            and collection[insertion_index - 1] > collection[insertion_index]
        ):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index -= 1

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{insertionSort(unsorted) = }")
